![Omega Race](ORace.jpg)

# Main Board

>>> cpu Z80

>>> binary 0000:roms/omega.m7 + roms/omega.l7 + roms/omega.k7 + roms/omega.j7 

>>> memoryTable hard 
[Hardware Info](Hardware.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
0000: F3              DI                          ; Turn interrupts off
0001: ED 56           IM      1                   ; Mode 1 ... everything to $38
0003: 31 FC 4B        LD      SP,$4BFC            ; Stack at top of RAM (almost)
0006: DB 09           IN      A,($09)             ; Feed watchdog
0008: 3E FF           LD      A,$FF               ; LEDs, screen reverse, meters ... 
000A: D3 13           OUT     ($13),A             ; ... all off
;
000C: 01 FE 07        LD      BC,$07FE            ; Size of vector RAM (minus 2)
000F: 11 02 80        LD      DE,$8002            ; Fill ...
0012: 21 01 80        LD      HL,$8001            ; ... vector ...
0015: 36 B0           LD      (HL),$B0            ; ... RAM ...
0017: 2B              DEC     HL                  ; ... with ...
0018: 36 00           LD      (HL),$00            ; ... 00 B0 ...
001A: ED B0           LDIR                        ; ... HALT
;
001C: 01 80 01        LD      BC,$0180            
001F: 11 81 44        LD      DE,$4481            ; Some kind of vector mirror in RAM? This loads it with HALT
0022: 21 00 80        LD      HL,$8000            
0025: ED B0           LDIR
;                        
0027: 01 30 00        LD      BC,$0030            
002A: 11 01 46        LD      DE,$4601            ; Another vector
002D: 21 D9 30        LD      HL,$30D9            
0030: ED B0           LDIR
;                        
0032: C3 E8 04        JP      $04E8               ;{Diagnostics} Diagnostics OR startup

0035: FF FF FF                 

; Interrupt Mode 1: All interrupts come here
;
0038: F5              PUSH    AF                  
0039: C5              PUSH    BC                  
003A: FD 34 97        INC     (IY+$97)            ;
003D: FD 4E B5        LD      C,(IY+$B5)          
0040: DB 11           IN      A,($11)             ;
0042: CB 67           BIT     4,A                 
0044: 20 36           JR      NZ,$7C              ; 
0046: 3A 82 40        LD      A,($4082)           ; 
0049: B7              OR      A                   
004A: 20 30           JR      NZ,$7C              ; 
004C: 3E 13           LD      A,$13               
004E: D3 14           OUT     ($14),A             ;
0050: 32 82 40        LD      ($4082),A           ; 
0053: 3E 00           LD      A,$00               
0055: 32 25 40        LD      ($4025),A           ; 
0058: 32 26 40        LD      ($4026),A           ; 
005B: 18 0B           JR      $68                 ; 

; Padding to NMI destination
005D: FF FF FF FF FF FF FF FF FF
```

# NMI

```code 
; NMI comes here
0066: ED 45           RETN                        ; Return from non-maskable interrupt
                  
; Continuing from 005B
0068: 3A 2D 40        LD      A,($402D)           ; 
006B: B7              OR      A                   
006C: 28 0A           JR      Z,$78               ; 
006E: D6 01           SUB     $01                 
0070: 27              DAA                         
0071: 32 2D 40        LD      ($402D),A           ; 
0074: FD CB AE F6     SET     6,(IY+$AE)          
0078: FD 36 A1 03     LD      (IY+$A1),$03        
007C: DB 11           IN      A,($11)             ;
007E: E6 03           AND     $03                 
0080: 32 35 40        LD      ($4035),A           ; 
0083: 47              LD      B,A                 
0084: A9              XOR     C                   
0085: 28 10           JR      Z,$97               ; 
0087: CB 47           BIT     0,A                 
0089: 28 04           JR      Z,$8F               ; 
008B: FD 36 9B 05     LD      (IY+$9B),$05        
008F: CB 4F           BIT     1,A                 
0091: 28 04           JR      Z,$97               ; 
0093: FD 36 9C 05     LD      (IY+$9C),$05        
0097: 3A 1B 40        LD      A,($401B)           ; 
009A: B7              OR      A                   
009B: 28 4D           JR      Z,$EA               ; 
009D: FD 35 9B        DEC     (IY+$9B)            
00A0: 20 48           JR      NZ,$EA              ; 
00A2: CB 40           BIT     0,B                 
00A4: 20 44           JR      NZ,$EA              ; 
00A6: DB 11           IN      A,($11)             ;
00A8: CB 7F           BIT     7,A                 
00AA: 28 08           JR      Z,$B4               ; 
00AC: 3E 00           LD      A,$00               
00AE: CD 18 15        CALL    $1518               ; 
00B1: FD 34 9D        INC     (IY+$9D)            ;
00B4: 3E 12           LD      A,$12               
00B6: D3 14           OUT     ($14),A             ;
00B8: FD 34 A5        INC     (IY+$A5)            ;
00BB: 3A 25 40        LD      A,($4025)           ; 
00BE: E5              PUSH    HL                  
00BF: 2A 27 40        LD      HL,($4027)          ; 
00C2: BE              CP      (HL)                
00C3: 38 24           JR      C,$E9               ; 
00C5: FD 36 A5 00     LD      (IY+$A5),$00        
00C9: 23              INC     HL                  
00CA: DB 11           IN      A,($11)             ;
00CC: CB 7F           BIT     7,A                 
00CE: 20 05           JR      NZ,$D5              ; 
00D0: 3E 02           LD      A,$02               
00D2: CD 21 15        CALL    $1521               ; 
00D5: 3A 2D 40        LD      A,($402D)           ; 
00D8: 86              ADD     A,(HL)              
00D9: 27              DAA                         
00DA: 32 2D 40        LD      ($402D),A           ; 
00DD: FD CB AE F6     SET     6,(IY+$AE)          
00E1: FE 21           CP      $21                 
00E3: 38 04           JR      C,$E9               ; 
00E5: FD 36 AD 20     LD      (IY+$AD),$20        
00E9: E1              POP     HL                  
00EA: 3A 1C 40        LD      A,($401C)           ; 
00ED: B7              OR      A                   
00EE: 28 4D           JR      Z,$13D              ; 
00F0: FD 35 9C        DEC     (IY+$9C)            
00F3: 20 48           JR      NZ,$13D             ; 
00F5: CB 48           BIT     1,B                 
00F7: 20 44           JR      NZ,$13D             ; 
00F9: DB 11           IN      A,($11)             ;
00FB: CB 7F           BIT     7,A                 
00FD: 28 08           JR      Z,$107              ; 
00FF: 3E 01           LD      A,$01               
0101: CD 18 15        CALL    $1518               ; 
0104: FD 34 9E        INC     (IY+$9E)            ;
0107: 3E 12           LD      A,$12               
0109: D3 14           OUT     ($14),A             ;
010B: FD 34 A6        INC     (IY+$A6)            ;
010E: 3A 26 40        LD      A,($4026)           ; 
0111: E5              PUSH    HL                  
0112: 2A 29 40        LD      HL,($4029)          ; 
0115: BE              CP      (HL)                
0116: 38 24           JR      C,$13C              ; 
0118: FD 36 A6 00     LD      (IY+$A6),$00        
011C: 23              INC     HL                  
011D: DB 11           IN      A,($11)             ;
011F: CB 7F           BIT     7,A                 
0121: 20 05           JR      NZ,$128             ; 
0123: 3E 02           LD      A,$02               
0125: CD 21 15        CALL    $1521               ; 
0128: 3A 2D 40        LD      A,($402D)           ; 
012B: 86              ADD     A,(HL)              
012C: 27              DAA                         
012D: 32 2D 40        LD      ($402D),A           ; 
0130: FD CB AE F6     SET     6,(IY+$AE)          
0134: FE 21           CP      $21                 
0136: 38 04           JR      C,$13C              ; 
0138: FD 36 AD 20     LD      (IY+$AD),$20        
013C: E1              POP     HL                  
013D: 3A 1F 40        LD      A,($401F)           ; 
0140: B7              OR      A                   
0141: 28 16           JR      Z,$159              ; 
0143: 3D              DEC     A                   
0144: 32 1F 40        LD      ($401F),A           ; 
0147: 28 10           JR      Z,$159              ; 
0149: FE 19           CP      $19                 
014B: 20 4E           JR      NZ,$19B             ; 
014D: 3A 72 40        LD      A,($4072)           ; 
0150: F6 03           OR      $03                 
0152: D3 13           OUT     ($13),A             ;
0154: 32 72 40        LD      ($4072),A           ; 
0157: 18 42           JR      $19B                ; 
0159: 3A 1D 40        LD      A,($401D)           ; 
015C: B7              OR      A                   
015D: 28 0B           JR      Z,$16A              ; 
015F: FD 35 9D        DEC     (IY+$9D)            
0162: FD CB F2 86     RES     0,(IY+$F2)          
0166: FD 36 9F 32     LD      (IY+$9F),$32        
016A: 3A 1E 40        LD      A,($401E)           ; 
016D: B7              OR      A                   
016E: 28 1F           JR      Z,$18F              ; 
0170: 3A 2B 40        LD      A,($402B)           ; 
0173: FD BE AC        CP      (IY+$AC)            
0176: 20 0C           JR      NZ,$184             ; 
0178: FD CB F2 46     BIT     0,(IY+$F2)          
017C: 28 11           JR      Z,$18F              ; 
017E: FD CB F2 86     RES     0,(IY+$F2)          
0182: 18 04           JR      $188                ; 
0184: FD CB F2 8E     RES     1,(IY+$F2)          
0188: FD 35 9E        DEC     (IY+$9E)            
018B: FD 36 9F 32     LD      (IY+$9F),$32        
018F: 3A 1F 40        LD      A,($401F)           ; 
0192: FE 32           CP      $32                 
0194: 20 05           JR      NZ,$19B             ; 
0196: 3A 72 40        LD      A,($4072)           ; 
0199: D3 13           OUT     ($13),A             ;
019B: C1              POP     BC                  
019C: F1              POP     AF                  
019D: FB              EI                          
019E: ED 4D           RETI                        
```

# Setup for Diagnostics

```code
DiagSetup: 
; Init the diagnostic screen (vectors)
;
;                       Dest        opcode
01A0: 20 A3 A0 11     ; 8000(000) A320 11A0     SetBeam x=1A0 y=320 (416,800)
01A4: 00 80 00 00     ; 8004(002) 8000 0000     LongVector  scale=8 x=000 y=000 intensity=0 (0,0)
01A8: 16 E0           ; 8008(004) E016          JMP $016(802C)    ; Jump to main content
;
; space, space, OK, and CF/LF
01AA: 92 CD           ; 800A(005) CD92          JSR $D92(9B24)    ; space
01AC: 92 CD           ; 800C(006) CD92          JSR $D92(9B24)    ; space
01AE: C2 CC           ; 800E(007) CCC2          JSR $CC2(9984)    ; O
01B0: A3 CC           ; 8010(008) CCA3          JSR $CA3(9946)    ; K
01B2: 13 E0           ; 8012(009) E013          JMP $013(8026)    ; CR/LF
;
;
; space, NG, space, and CR/LF
01B4: 92 CD           ; 8014(00A) CD92          JSR $D92(9B24)    ; space
01B6: BA CC           ; 8016(00B) CCBA          JSR $CBA(9974)    ; N
01B8: 7F CC           ; 8018(00C) CC7F          JSR $C7F(98FE)    ; G
01BA: 92 CD           ; 801A(00D) CD92          JSR $D92(9B24)    ; space
01BC: 13 E0           ; 801C(00E) E013          JMP $013(8026)    ; CR/LF
;
;
; 4 spaces and CR/LF
01BE: 92 CD           ; 801E(00F) CD92          JSR $D92(9B24)    ; space
01C0: 92 CD           ; 8020(010) CD92          JSR $D92(9B24)    ; space
01C2: 92 CD           ; 8022(011) CD92          JSR $D92(9B24)    ; space
01C4: 92 CD           ; 8024(012) CD92          JSR $D92(9B24)    ; space
;
; CR/LF
01C6: 4F 74 FF 06     ; 8026(013) 744F 06FF     LongVector  scale=7 x=6FF y=44F intensity=0 (-767,-79)
01CA: 00 D0           ; 802A(015) D000          RTS               ; return to caller
```

# Diagnostics Strings

```code
DiagString: 
; Diagnostic strings ... 8 characters per row

01CC: 50 20 52 4F 4D 20 31 20 2E  ; "P_ROM_1_."             
01D5: 50 20 52 4F 4D 20 32 20 2E  ; "P_ROM_2_."
01DE: 50 20 52 4F 4D 20 33 20 2E  ; "P_ROM_3_."
01E7: 50 20 52 4F 4D 20 34 20 2E  ; "P_ROM_4_."
01F0: 20 20 20 20 20 20 20 20 2E  ; "         "
01F9: 50 20 52 41 4D 20 31 20 2E  ; "P_RAM_1_."
0202: 50 20 52 41 4D 20 32 20 2E  ; "P_RAM_2_."
020B: 50 20 52 41 4D 20 33 20 2E  ; "P_RAM_3_."
0214: 20 20 20 20 20 20 20 20 2E  ; "         "
021D: 42 42 55 20 52 41 4D 20 2E  ; "BBU_RAM_."
0226: 20 20 20 20 20 20 20 20 2E  ; "         "
022F: 56 20 52 41 4D 20 31 20 2E  ; "V_RAM_1_."
0238: 56 20 52 41 4D 20 32 20 2E  ; "V_RAM_2_."
0241: 56 20 52 41 4D 20 33 20 2E  ; "V_RAM_3_."
024A: 56 20 52 41 4D 20 34 20 2E  ; "V_RAM_4_."
0253: 20 20 20 20 20 20 20 20 2E  ; "         "
025C: 56 20 52 4F 4D 20 31 20 2E  ; "V_ROM_1_."
0265: 56 20 52 4F 4D 20 32 20 2E  ; "V_ROM_2_."
         
026E: 84              ADD     A,H                 
026F: A3              AND     E                   
0270: A0              AND     B                   
0271: 01 00 90        LD      BC,$9000            
0274: 00              NOP                         
0275: 00              NOP                         
0276: 16 E0           LD      D,$E0               
0278: 92              SUB     D                   
0279: CD AB CC        CALL    $CCAB               ; 
027C: C2 CC 0B        JP      NZ,$0BCC            ; 
027F: CD 13 E0        CALL    $E013               ; 
0282: 92              SUB     D                   
0283: CD 88 CC        CALL    $CC88               ; 
0286: 91              SUB     C                   
0287: CC 92 CD        CALL    Z,$CD92             ; 
028A: 13              INC     DE                  
028B: E0              RET     PO                  
028C: 92              SUB     D                   
028D: CD 92 CD        CALL    $CD92               ; 
0290: 92              SUB     D                   
0291: CD 92 CD        CALL    $CD92               ; 
0294: 3F              CCF                         
0295: 74              LD      (HL),H              
0296: FF              RST     $38                 
0297: 06 
0298: 00 D0
                  
029A: 43              LD      B,E                 
029B: 4F              LD      C,A                 
029C: 49              LD      C,C                 
029D: 4E              LD      C,(HL)              
029E: 20 31           JR      NZ,$2D1             ; 
02A0: 20 20           JR      NZ,$2C2             ; 
02A2: 2E 43           LD      L,$43               
02A4: 4F              LD      C,A                 
02A5: 49              LD      C,C                 
02A6: 4E              LD      C,(HL)              
02A7: 20 32           JR      NZ,$2DB             ; 
02A9: 20 20           JR      NZ,$2CB             ; 
02AB: 2E 54           LD      L,$54               
02AD: 49              LD      C,C                 
02AE: 4C              LD      C,H                 
02AF: 54              LD      D,H                 
02B0: 20 20           JR      NZ,$2D2             ; 
02B2: 20 20           JR      NZ,$2D4             ; 
02B4: 2E 50           LD      L,$50               
02B6: 31 20 54        LD      SP,$5420            
02B9: 48              LD      C,B                 
02BA: 52              LD      D,D                 
02BB: 55              LD      D,L                 
02BC: 53              LD      D,E                 
02BD: 2E 50           LD      L,$50               
02BF: 31 20 46        LD      SP,$4620            
02C2: 49              LD      C,C                 
02C3: 52              LD      D,D                 
02C4: 45              LD      B,L                 
02C5: 20 2E           JR      NZ,$2F5             ; 
02C7: 54              LD      D,H                 
02C8: 45              LD      B,L                 
02C9: 53              LD      D,E                 
02CA: 54              LD      D,H                 
02CB: 20 20           JR      NZ,$2ED             ; 
02CD: 20 20           JR      NZ,$2EF             ; 
02CF: 2E 20           LD      L,$20               
02D1: 20 20           JR      NZ,$2F3             ; 
02D3: 20 20           JR      NZ,$2F5             ; 
02D5: 20 20           JR      NZ,$2F7             ; 
02D7: 20 2E           JR      NZ,$307             ; 
02D9: 50              LD      D,B                 
02DA: 32 20 54        LD      ($5420),A           ; 
02DD: 48              LD      C,B                 
02DE: 52              LD      D,D                 
02DF: 55              LD      D,L                 
02E0: 53              LD      D,E                 
02E1: 2E 50           LD      L,$50               
02E3: 32 20 46        LD      ($4620),A           ; 
02E6: 49              LD      C,C                 
02E7: 52              LD      D,D                 
02E8: 45              LD      B,L                 
02E9: 20 2E           JR      NZ,$319             ; 
02EB: 32 20 50        LD      ($5020),A           ; 
02EE: 20 31           JR      NZ,$321             ; 
02F0: 20 43           JR      NZ,$335             ; 
02F2: 52              LD      D,D                 
02F3: 2E 32           LD      L,$32               
02F5: 20 50           JR      NZ,$347             ; 
02F7: 20 32           JR      NZ,$32B             ; 
02F9: 20 43           JR      NZ,$33E             ; 
02FB: 52              LD      D,D                 
02FC: 2E 31           LD      L,$31               
02FE: 20 50           JR      NZ,$350             ; 
0300: 20 31           JR      NZ,$333             ; 
0302: 20 43           JR      NZ,$347             ; 
0304: 52              LD      D,D                 
0305: 2E 31           LD      L,$31               
0307: 20 50           JR      NZ,$359             ; 
0309: 20 32           JR      NZ,$33D             ; 
030B: 20 43           JR      NZ,$350             ; 
030D: 52              LD      D,D                 
030E: 2E 20           LD      L,$20               
0310: 20 20           JR      NZ,$332             ; 
0312: 20 20           JR      NZ,$334             ; 
0314: 20 20           JR      NZ,$336             ; 
0316: 20 2E           JR      NZ,$346             ; 
0318: 41              LD      B,C                 
0319: 4E              LD      C,(HL)              
031A: 47              LD      B,A                 
031B: 4C              LD      C,H                 
031C: 45              LD      B,L                 
031D: 31 20 32        LD      SP,$3220            
0320: 2E 41           LD      L,$41               
0322: 4E              LD      C,(HL)              
0323: 47              LD      B,A                 
0324: 4C              LD      C,H                 
0325: 45              LD      B,L                 
0326: 31 20 33        LD      SP,$3320            
0329: 2E 41           LD      L,$41               
032B: 4E              LD      C,(HL)              
032C: 47              LD      B,A                 
032D: 4C              LD      C,H                 
032E: 45              LD      B,L                 
032F: 31 20 34        LD      SP,$3420            
0332: 2E 41           LD      L,$41               
0334: 4E              LD      C,(HL)              
0335: 47              LD      B,A                 
0336: 4C              LD      C,H                 
0337: 45              LD      B,L                 
0338: 31 20 35        LD      SP,$3520            
033B: 2E 41           LD      L,$41               
033D: 4E              LD      C,(HL)              
033E: 47              LD      B,A                 
033F: 4C              LD      C,H                 
0340: 45              LD      B,L                 
0341: 31 20 36        LD      SP,$3620            
0344: 2E 41           LD      L,$41               
0346: 4E              LD      C,(HL)              
0347: 47              LD      B,A                 
0348: 4C              LD      C,H                 
0349: 45              LD      B,L                 
034A: 31 20 37        LD      SP,$3720            
034D: 2E 20           LD      L,$20               
034F: 20 20           JR      NZ,$371             ; 
0351: 20 20           JR      NZ,$373             ; 
0353: 20 20           JR      NZ,$375             ; 
0355: 20 2E           JR      NZ,$385             ; 
0357: 41              LD      B,C                 
0358: 4E              LD      C,(HL)              
0359: 47              LD      B,A                 
035A: 4C              LD      C,H                 
035B: 45              LD      B,L                 
035C: 32 20 30        LD      ($3020),A           ; 
035F: 2E 41           LD      L,$41               
0361: 4E              LD      C,(HL)              
0362: 47              LD      B,A                 
0363: 4C              LD      C,H                 
0364: 45              LD      B,L                 
0365: 32 20 31        LD      ($3120),A           ; 
0368: 2E 41           LD      L,$41               
036A: 4E              LD      C,(HL)              
036B: 47              LD      B,A                 
036C: 4C              LD      C,H                 
036D: 45              LD      B,L                 
036E: 32 20 32        LD      ($3220),A           ; 
0371: 2E 41           LD      L,$41               
0373: 4E              LD      C,(HL)              
0374: 47              LD      B,A                 
0375: 4C              LD      C,H                 
0376: 45              LD      B,L                 
0377: 32 20 33        LD      ($3320),A           ; 
037A: 2E 41           LD      L,$41               
037C: 4E              LD      C,(HL)              
037D: 47              LD      B,A                 
037E: 4C              LD      C,H                 
037F: 45              LD      B,L                 
0380: 32 20 34        LD      ($3420),A           ; 
0383: 2E 41           LD      L,$41               
0385: 4E              LD      C,(HL)              
0386: 47              LD      B,A                 
0387: 4C              LD      C,H                 
0388: 45              LD      B,L                 
0389: 32 20 35        LD      ($3520),A           ; 
038C: 2E 20           LD      L,$20               
038E: 20 20           JR      NZ,$3B0             ; 
0390: 20 20           JR      NZ,$3B2             ; 
0392: 20 20           JR      NZ,$3B4             ; 
0394: 20 2E           JR      NZ,$3C4             ; 
0396: 44              LD      B,H                 
0397: 49              LD      C,C                 
0398: 50              LD      D,B                 
0399: 53              LD      D,E                 
039A: 57              LD      D,A                 
039B: 31 20 30        LD      SP,$3020            
039E: 2E 44           LD      L,$44               
03A0: 49              LD      C,C                 
03A1: 50              LD      D,B                 
03A2: 53              LD      D,E                 
03A3: 57              LD      D,A                 
03A4: 31 20 31        LD      SP,$3120            
03A7: 2E 44           LD      L,$44               
03A9: 49              LD      C,C                 
03AA: 50              LD      D,B                 
03AB: 53              LD      D,E                 
03AC: 57              LD      D,A                 
03AD: 31 20 32        LD      SP,$3220            
03B0: 2E 44           LD      L,$44               
03B2: 49              LD      C,C                 
03B3: 50              LD      D,B                 
03B4: 53              LD      D,E                 
03B5: 57              LD      D,A                 
03B6: 31 20 33        LD      SP,$3320            
03B9: 2E 44           LD      L,$44               
03BB: 49              LD      C,C                 
03BC: 50              LD      D,B                 
03BD: 53              LD      D,E                 
03BE: 57              LD      D,A                 
03BF: 31 20 34        LD      SP,$3420            
03C2: 2E 44           LD      L,$44               
03C4: 49              LD      C,C                 
03C5: 50              LD      D,B                 
03C6: 53              LD      D,E                 
03C7: 57              LD      D,A                 
03C8: 31 20 35        LD      SP,$3520            
03CB: 2E 44           LD      L,$44               
03CD: 49              LD      C,C                 
03CE: 50              LD      D,B                 
03CF: 53              LD      D,E                 
03D0: 57              LD      D,A                 
03D1: 31 20 36        LD      SP,$3620            
03D4: 2E 44           LD      L,$44               
03D6: 49              LD      C,C                 
03D7: 50              LD      D,B                 
03D8: 53              LD      D,E                 
03D9: 57              LD      D,A                 
03DA: 31 20 37        LD      SP,$3720            
03DD: 2E 20           LD      L,$20               
03DF: 20 20           JR      NZ,$401             ; 
03E1: 20 20           JR      NZ,$403             ; 
03E3: 20 20           JR      NZ,$405             ; 
03E5: 20 2E           JR      NZ,$415             ; 
03E7: 44              LD      B,H                 
03E8: 49              LD      C,C                 
03E9: 50              LD      D,B                 
03EA: 53              LD      D,E                 
03EB: 57              LD      D,A                 
03EC: 32 20 30        LD      ($3020),A           ; 
03EF: 2E 44           LD      L,$44               
03F1: 49              LD      C,C                 
03F2: 50              LD      D,B                 
03F3: 53              LD      D,E                 
03F4: 57              LD      D,A                 
03F5: 32 20 31        LD      ($3120),A           ; 
03F8: 2E 44           LD      L,$44               
03FA: 49              LD      C,C                 
03FB: 50              LD      D,B                 
03FC: 53              LD      D,E                 
03FD: 57              LD      D,A                 
03FE: 32 20 32        LD      ($3220),A           ; 
0401: 2E 44           LD      L,$44               
0403: 49              LD      C,C                 
0404: 50              LD      D,B                 
0405: 53              LD      D,E                 
0406: 57              LD      D,A                 
0407: 32 20 33        LD      ($3320),A           ; 
040A: 2E 44           LD      L,$44               
040C: 49              LD      C,C                 
040D: 50              LD      D,B                 
040E: 53              LD      D,E                 
040F: 57              LD      D,A                 
0410: 32 20 34        LD      ($3420),A           ; 
0413: 2E 44           LD      L,$44               
0415: 49              LD      C,C                 
0416: 50              LD      D,B                 
0417: 53              LD      D,E                 
0418: 57              LD      D,A                 
0419: 32 20 35        LD      ($3520),A           ; 
041C: 2E 44           LD      L,$44               
041E: 49              LD      C,C                 
041F: 50              LD      D,B                 
0420: 53              LD      D,E                 
0421: 57              LD      D,A                 
0422: 32 20 36        LD      ($3620),A           ; 
0425: 2E 44           LD      L,$44               
0427: 49              LD      C,C                 
0428: 50              LD      D,B                 
0429: 53              LD      D,E                 
042A: 57              LD      D,A                 
042B: 32 20 37        LD      ($3720),A           ; 
042E: 2E 00           LD      L,$00               
0430: A2              AND     D                   
0431: 00              NOP                         
0432: 00              NOP                         
0433: 00              NOP                         
0434: 80              ADD     A,B                 
0435: 00              NOP                         
0436: 00              NOP                         
0437: FD
0438: 83              ADD     A,E                 
0439: FF              RST     $38                 
043A: C3 FD 87        JP      $87FD               ; 
043D: FD
043E: C3 FF 87        JP      $87FF               ; 
0441: FD
0442: C7              RST     $00                 
0443: FF              RST     $38                 
0444: 83              ADD     A,E                 
0445: FF              RST     $38                 
0446: C7              RST     $00                 
0447: 00              NOP                         
0448: A0              AND     B                   
0449: 00              NOP                         
044A: 00              NOP                         
044B: 00              NOP                         
044C: 90              SUB     B                   
044D: 00              NOP                         
044E: 00              NOP                         
044F: FE 93           CP      $93                 
0451: 00              NOP                         
0452: C0              RET     NZ                  
0453: 00              NOP                         
0454: 90              SUB     B                   
0455: FE C3           CP      $C3                 
0457: FE 97           CP      $97                 
0459: 00              NOP                         
045A: C0              RET     NZ                  
045B: 00              NOP                         
045C: 90              SUB     B                   
045D: FE C7           CP      $C7                 
045F: FE 93           CP      $93                 
0461: FE C3           CP      $C3                 
0463: FE 97           CP      $97                 
0465: 00              NOP                         
0466: 00              NOP                         
0467: FE 93           CP      $93                 
0469: FE C7           CP      $C7                 
046B: BC              CP      H                   
046C: A2              AND     D                   
046D: BA              CP      D                   
046E: 01 00 80        LD      BC,$8000            
0471: 00              NOP                         
0472: 00              NOP                         
0473: 1F              RRA                         
0474: 57              LD      D,A                 
0475: 00              NOP                         
0476: 00              NOP                         
0477: 1F              RRA                         
0478: 53              LD      D,E                 
0479: 9F              SBC     A                   
047A: 00              NOP                         
047B: 1F              RRA                         
047C: 57              LD      D,A                 
047D: 00              NOP                         
047E: 10 1F           DJNZ    $49F                ; 
0480: 53              LD      D,E                 
0481: 9F              SBC     A                   
0482: 00              NOP                         
0483: 1F              RRA                         
0484: 57              LD      D,A                 
0485: 00              NOP                         
0486: 20 1F           JR      NZ,$4A7             ; 
0488: 53              LD      D,E                 
0489: 9F              SBC     A                   
048A: 00              NOP                         
048B: 1F              RRA                         
048C: 57              LD      D,A                 
048D: 00              NOP                         
048E: 30 1F           JR      NC,$4AF             ; 
0490: 53              LD      D,E                 
0491: 9F              SBC     A                   
0492: 00              NOP                         
0493: 1F              RRA                         
0494: 57              LD      D,A                 
0495: 00              NOP                         
0496: 40              LD      B,B                 
0497: 1F              RRA                         
0498: 53              LD      D,E                 
0499: 9F              SBC     A                   
049A: 00              NOP                         
049B: 1F              RRA                         
049C: 57              LD      D,A                 
049D: 00              NOP                         
049E: 50              LD      D,B                 
049F: 1F              RRA                         
04A0: 53              LD      D,E                 
04A1: 9F              SBC     A                   
04A2: 00              NOP                         
04A3: 1F              RRA                         
04A4: 57              LD      D,A                 
04A5: 00              NOP                         
04A6: 60              LD      H,B                 
04A7: 1F              RRA                         
04A8: 53              LD      D,E                 
04A9: 9F              SBC     A                   
04AA: 00              NOP                         
04AB: 1F              RRA                         
04AC: 57              LD      D,A                 
04AD: 00              NOP                         
04AE: 70              LD      (HL),B              
04AF: 1F              RRA                         
04B0: 53              LD      D,E                 
04B1: 9F              SBC     A                   
04B2: 00              NOP                         
04B3: 1F              RRA                         
04B4: 57              LD      D,A                 
04B5: 00              NOP                         
04B6: 80              ADD     A,B                 
04B7: 1F              RRA                         
04B8: 53              LD      D,E                 
04B9: 9F              SBC     A                   
04BA: 00              NOP                         
04BB: 1F              RRA                         
04BC: 57              LD      D,A                 
04BD: 00              NOP                         
04BE: 90              SUB     B                   
04BF: 1F              RRA                         
04C0: 53              LD      D,E                 
04C1: 9F              SBC     A                   
04C2: 00              NOP                         
04C3: 1F              RRA                         
04C4: 57              LD      D,A                 
04C5: 00              NOP                         
04C6: A0              AND     B                   
04C7: 1F              RRA                         
04C8: 53              LD      D,E                 
04C9: 9F              SBC     A                   
04CA: 00              NOP                         
04CB: 1F              RRA                         
04CC: 57              LD      D,A                 
04CD: 00              NOP                         
04CE: B0              OR      B                   
04CF: 1F              RRA                         
04D0: 53              LD      D,E                 
04D1: 9F              SBC     A                   
04D2: 00              NOP                         
04D3: 1F              RRA                         
04D4: 57              LD      D,A                 
04D5: 00              NOP                         
04D6: C0              RET     NZ                  
04D7: 1F              RRA                         
04D8: 53              LD      D,E                 
04D9: 9F              SBC     A                   
04DA: 00              NOP                         
04DB: 1F              RRA                         
04DC: 57              LD      D,A                 
04DD: 00              NOP                         
04DE: E0              RET     PO                  
04DF: 1F              RRA                         
04E0: 53              LD      D,E                 
04E1: 9F              SBC     A                   
04E2: 00              NOP                         
04E3: 1F              RRA                         
04E4: 57              LD      D,A                 
04E5: 00              NOP                         
04E6: F0              RET     P                   
04E7: AA              XOR     D                   
```

# Diagnostics

```code
Diagnostics: 
; This routine is quite clever. It uses IX and IY as link registers to avoid CALL and
; RETURN. After all, if the RAM is not working then CALL/RETURN won't work. The diagnostics
; report "OK" or "NO" in the vector RAM in case the screen is working The diagnostic flashes/beeps
; indicate a bad chip as follows:
;
; Flashes/beeps   Problem   Start-address
;  1               ROM-1    (0000)
;  2               ROM-2    (1000)
;  3               ROM-3    (2000)
;  4               ROM-4    (3000)
;  5               RAM-1    (4000)
;  6               RAM-2    (4400)
;  7               RAM-3    (4800)
;  8               NONVOL   (5C00)
;  9               VRAM-1   (8000)
; 10               VRAM-2   (8400)
; 11               VRAM-3   (8800)
; 12               VRAM-4   (8C00)
; 13               VROM-1   (9000)
; 14               VROM-2   (9800)
;
; The "initialization" vectors take 2C bytes of RAM. After that there are 18 rows of patterns like:
; "P_ROM_1_." The string-print routine puts 2 bytes (a subtroutine call) for each character.
; Each screen row is thus 9*2 = 18 ($12) bytes. The "." character is translated to a vector CR/LF
; to the start of the next line.
; 
; The first "OK" or "NG" goes to 803C, which is 803C-802C=16 ($10) bytes into the first row.
; That's the last character. The LSB of the character is replaced with 05 for "OK" or 0A for "NG".
;
; Thus C00F (the CRLF) is replaced with C00A for ("NG"+CR/LF) or C005 for ("OK"+CR/LF). Note
; that C00F and C005 are subroutine calls to vector RAM. The vector processor sees those as
; word addresses so 00F is 801E, 005 is 800A, and 00A is 8014.
;
; The code adds $12 to the character location each time skipping down a row.
;
04E8: 3E 00           LD      A,$00               ; Sound ...
04EA: D3 14           OUT     ($14),A             ; ... off
04EC: DB 09           IN      A,($09)             ; Feed watchdog
04EE: DD 21 F5 04     LD      IX,$04F5            ; Next after routine
04F2: C3 B6 07        JP      $07B6               ; Clear DVG RAM (1st byte set to HALT)

04F5: 01 2C 00        LD      BC,$002C            ; 2C bytes in pattern
04F8: 11 00 80        LD      DE,$8000            ; Top of DVG RAM
04FB: 21 A0 01        LD      HL,$01A0            ; Initial DVG list
04FE: ED B0           LDIR                        ; Pattern to screen memory
0500: 01 A2 00        LD      BC,$00A2            ; A2 bytes in diagnostics string
0503: DD 21 0A 05     LD      IX,$050A            ; Diagnostics string next in source
0507: C3 C8 08        JP      $08C8               ; Print the test string
050A: DB 11           IN      A,($11)             ; Is test ...
050C: CB 7F           BIT     7,A                 ; ... switch set?
050E: C2 55 09        JP      NZ,$0955            ; No ... skip it
0511: 01 00 00        LD      BC,$0000            
0514: DB 11           IN      A,($11)             ;
0516: 57              LD      D,A                 
0517: 1E 00           LD      E,$00               
0519: D9              EXX                         
051A: 01 FF 0B        LD      BC,$0BFF            ; Size of RAM
051D: 11 01 40        LD      DE,$4001            ; Fill ...
0520: 21 00 40        LD      HL,$4000            ; ... RAM ...
0523: 36 FF           LD      (HL),$FF            ; ... with ...
0525: ED B0           LDIR                        ; ... all FFs
0527: DB 09           IN      A,($09)             ; Feed watchdog
0529: 01 8B 0E        LD      BC,$0E8B            ; Fill DVG ...
052C: 11 75 81        LD      DE,$8175            ; ... RAM past ...
052F: 21 74 81        LD      HL,$8174            ; ... pattern and results with ...
0532: 36 FF           LD      (HL),$FF            ; ... all ...
0534: ED B0           LDIR                        ; ... FFs
0536: DB 09           IN      A,($09)             ; Feed watchdog
;
0538: 01 00 10        LD      BC,$1000            ; 1000 bytes
053B: 11 3C 80        LD      DE,$803C            ; First "OK" or "NO" location
053E: 21 00 00        LD      HL,$0000            ; First ROM chip
0541: DD 21 48 05     LD      IX,$0548            ; After test
0545: C3 E9 07        JP      $07E9               ;{TestROM} Test the ROM chip
0548: 28 09           JR      Z,$553              ; Skip flash if OK
054A: 06 01           LD      B,$01               ; Flash number #1
054C: DD 21 53 05     LD      IX,$0553            ; Next in code
0550: C3 17 09        JP      $0917               ; Go flash 1 ... problems with ROM-1 (0000)
;
0553: 01 00 10        LD      BC,$1000            ; 1000 bytes ...
0556: 21 00 10        LD      HL,$1000            ; ... beginning at 1000
0559: DD 21 60 05     LD      IX,$0560            ; Next location
055D: C3 E9 07        JP      $07E9               ;{TestROM} Check it
;
0560: 28 09           JR      Z,$56B              ; Skip flash if OK
0562: 06 02           LD      B,$02               ; Flash number #2
0564: DD 21 6B 05     LD      IX,$056B            ; Next in code
0568: C3 17 09        JP      $0917               ; Go flash 2 ... problems with ROM-2 (1000)
;
056B: 01 00 10        LD      BC,$1000            ; 1000 bytes ...
056E: 21 00 20        LD      HL,$2000            ; ... beginning at 2000
0571: DD 21 78 05     LD      IX,$0578            ; Next in code
0575: C3 E9 07        JP      $07E9               ;{TestROM} Check it
;
0578: 28 09           JR      Z,$583              ; Skip flash if OK
057A: 06 03           LD      B,$03               ; Flash number #3
057C: DD 21 83 05     LD      IX,$0583            ; Next in code
0580: C3 17 09        JP      $0917               ; Go flash 3 ... problems with ROM-3 (2000)
;
0583: 01 00 10        LD      BC,$1000            ; 1000 bytes ...
0586: 21 00 30        LD      HL,$3000            ; ... beginning at 30000
0589: DD 21 90 05     LD      IX,$0590            ; Next in code
058D: C3 E9 07        JP      $07E9               ;{TestROM} Check it
; 
0590: 28 09           JR      Z,$59B              ; Skip flash if OK
0592: 06 04           LD      B,$04               ; Flash number #4
0594: DD 21 9B 05     LD      IX,$059B            ; Next in code
0598: C3 17 09        JP      $0917               ; Go flash 4 ... problems with ROM-4 (3000)
;
059B: 21 12 00        LD      HL,$0012            ; Skip ...
059E: 19              ADD     HL,DE               ; ... a row  ...
059F: EB              EX      DE,HL               ; ... on screen
;
05A0: 01 00 04        LD      BC,$0400            ; 400 bytes in 1st chip
05A3: 21 00 40        LD      HL,$4000            ; Start of RAM
05A6: DD 21 AD 05     LD      IX,$05AD            ; Nex in code
05AA: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
05AD: 28 09           JR      Z,$5B8              ; Skip flash if OK
05AF: 06 05           LD      B,$05               ; Flash number #5
05B1: DD 21 B8 05     LD      IX,$05B8            ; Next in code
05B5: C3 17 09        JP      $0917               ; Go flash 5 ... problems with RAM-1 (4000)
;
05B8: 01 00 04        LD      BC,$0400            ; 400 bytes in 2nd chip
05BB: 21 00 44        LD      HL,$4400            ; Next chip
05BE: DD 21 C5 05     LD      IX,$05C5            ; Next in code
05C2: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
05C5: 28 09           JR      Z,$5D0              ; Skip flash if OK
05C7: 06 06           LD      B,$06               ; Flash number #6
05C9: DD 21 D0 05     LD      IX,$05D0            ; Next in code
05CD: C3 17 09        JP      $0917               ; Go flash 6 ... problems with RAM-2 (4400)
;
05D0: 01 00 04        LD      BC,$0400            ; 400 bytes in 3rd chip
05D3: 21 00 48        LD      HL,$4800            ; Next chip
05D6: DD 21 DD 05     LD      IX,$05DD            ; Next in code
05DA: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
05DD: 28 09           JR      Z,$5E8              ; Skip flash if OK
05DF: 06 07           LD      B,$07               ; Flash number #7
05E1: DD 21 E8 05     LD      IX,$05E8            ; Next in code
05E5: C3 17 09        JP      $0917               ; Go flash 7 ... problems with RAM-3 (4800)
;
05E8: 21 12 00        LD      HL,$0012            ; Skip ...
05EB: 19              ADD     HL,DE               ; ... a row ...
05EC: EB              EX      DE,HL               ; ... on screen
;
05ED: 01 1A 00        LD      BC,$001A            ; 1A bytes
05F0: 21 00 5C        LD      HL,$5C00            ; Start of nonvol
05F3: DD 21 FA 05     LD      IX,$05FA            ; Next in code
05F7: C3 63 08        JP      $0863               ;{TestNONVOL} Check it
;
05FA: 28 09           JR      Z,$605              ; Skip flash if OK
05FC: 06 08           LD      B,$08               ; Flash number #8
05FE: DD 21 05 06     LD      IX,$0605            ; Next in code
0602: C3 17 09        JP      $0917               ; Go flash 8 ... problems with NONVOL (5C00)
;
0605: 21 12 00        LD      HL,$0012            ; skip ...
0608: 19              ADD     HL,DE               ; ... a row ...
0609: EB              EX      DE,HL               ; ... on screen
;
060A: 01 A6 00        LD      BC,$00A6            ; A6 bytes in 1st vector RAM chip to check
060D: 21 5A 83        LD      HL,$835A            ; Offset into vector RAM past our working area
0610: DD 21 17 06     LD      IX,$0617            ; Next in code
0614: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
0617: 28 09           JR      Z,$622              ; Skip flash if OK
0619: 06 09           LD      B,$09               ; Flash number #9
061B: DD 21 22 06     LD      IX,$0622            ; Next in code
061F: C3 17 09        JP      $0917               ; Go flash 9 ... problems with VRAM-1 (8000)
;
0622: 01 00 04        LD      BC,$0400            ; 400 bytes to check
0625: 21 00 84        LD      HL,$8400            ; Next chip
0628: DD 21 2F 06     LD      IX,$062F            ; Next in code
062C: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
062F: 28 09           JR      Z,$63A              ; Skip flash if OK
0631: 06 0A           LD      B,$0A               ; Flash number #A
0633: DD 21 3A 06     LD      IX,$063A            ; Next in code
0637: C3 17 09        JP      $0917               ; Go flash A ... problems with VRAM-2 (8400)
;
063A: 01 00 04        LD      BC,$0400            ; 400 bytes to check
063D: 21 00 88        LD      HL,$8800            ; Next chip
0640: DD 21 47 06     LD      IX,$0647            ; Next in code
0644: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
0647: 28 09           JR      Z,$652              ; Skip flash if OK
0649: 06 0B           LD      B,$0B               ; Flash number #B
064B: DD 21 52 06     LD      IX,$0652            ; Next in code
064F: C3 17 09        JP      $0917               ; Go flash B ... problems with VRAM-3 (8800)
;
0652: 01 00 04        LD      BC,$0400            ; 400 bytes to check
0655: 21 00 8C        LD      HL,$8C00            ; Next chip
0658: DD 21 5F 06     LD      IX,$065F            ; Next in code
065C: C3 1D 08        JP      $081D               ;{TestRAM} Check it
;
065F: 28 09           JR      Z,$66A              ; Skip flash if OK
0661: 06 0C           LD      B,$0C               ; Flash number #C
0663: DD 21 6A 06     LD      IX,$066A            ; Next in code
0667: C3 17 09        JP      $0917               ; Go flash C ... problems  with VRAM-4 (8C00)
;
066A: 21 12 00        LD      HL,$0012            ; skip ...
066D: 19              ADD     HL,DE               ; ... a row ...
066E: EB              EX      DE,HL               ; ... on screen 

066F: 01 00 08        LD      BC,$0800            ; 800 bytes to check
0672: 21 00 90        LD      HL,$9000            ; 1st chip in vector ROM
0675: DD 21 7C 06     LD      IX,$067C            ; Next in code
0679: C3 E9 07        JP      $07E9               ;{TestROM} Check it
;
067C: 28 09           JR      Z,$687              ; Skip flash if OK
067E: 06 0D           LD      B,$0D               ; Flash number #D
0680: DD 21 87 06     LD      IX,$0687            ; Next in code
0684: C3 17 09        JP      $0917               ; Go flash D ... problems with VROM-1 (9000)
;
0687: 01 00 08        LD      BC,$0800            ; 800 bytes to check
068A: 21 00 98        LD      HL,$9800            ; 2nd chip in vector ROM
068D: DD 21 94 06     LD      IX,$0694            ; Next in code
0691: C3 E9 07        JP      $07E9               ;{TestROM} Check it
;
0694: 28 09           JR      Z,$69F              ; Skip flash if OK
0696: 06 0E           LD      B,$0E               ; Flash number #E
0698: DD 21 9F 06     LD      IX,$069F            ; Next in code
069C: C3 17 09        JP      $0917               ; Go flash E ... problems with VROM-2 (9800)

; Other tests
069F: DD 21 A6 06     LD      IX,$06A6            
06A3: C3 DD 07        JP      $07DD               ; 
06A6: CA 0A 05        JP      Z,$050A             ; 
06A9: DD 21 B0 06     LD      IX,$06B0            
06AD: C3 B6 07        JP      $07B6               ; 
06B0: 01 2C 00        LD      BC,$002C            
06B3: 11 00 80        LD      DE,$8000            
06B6: 21 6E 02        LD      HL,$026E            
06B9: ED B0           LDIR                        
06BB: DB 09           IN      A,($09)             ;
06BD: 01 95 01        LD      BC,$0195            
06C0: DD 21 C7 06     LD      IX,$06C7            
06C4: C3 C8 08        JP      $08C8               ;{PrintString} 
06C7: DD 21 CE 06     LD      IX,$06CE            
06CB: C3 DD 07        JP      $07DD               ; 
06CE: 11 3C 80        LD      DE,$803C            
06D1: DB 11           IN      A,($11)             ;
06D3: E6 03           AND     $03                 
06D5: 4F              LD      C,A                 
06D6: DB 11           IN      A,($11)             ;
06D8: E6 F0           AND     $F0                 
06DA: 0F              RRCA                        
06DB: 0F              RRCA                        
06DC: B1              OR      C                   
06DD: 06 06           LD      B,$06               
06DF: DD 21 E6 06     LD      IX,$06E6            
06E3: C3 A0 08        JP      $08A0               ; 
06E6: DB 12           IN      A,($12)             ;
06E8: E6 0F           AND     $0F                 
06EA: 4F              LD      C,A                 
06EB: DB 12           IN      A,($12)             ;
06ED: E6 C0           AND     $C0                 
06EF: 0F              RRCA                        
06F0: 0F              RRCA                        
06F1: B1              OR      C                   
06F2: 06 06           LD      B,$06               
06F4: DD 21 FB 06     LD      IX,$06FB            
06F8: C3 A0 08        JP      $08A0               ; 
06FB: DB 15           IN      A,($15)             ;
06FD: 0F              RRCA                        
06FE: 0F              RRCA                        
06FF: E6 3F           AND     $3F                 
0701: 06 06           LD      B,$06               
0703: DD 21 0A 07     LD      IX,$070A            
0707: C3 A0 08        JP      $08A0               ; 
070A: DB 16           IN      A,($16)             ;
070C: E6 3F           AND     $3F                 
070E: 06 06           LD      B,$06               
0710: DD 21 17 07     LD      IX,$0717            
0714: C3 A0 08        JP      $08A0               ; 
0717: DB 10           IN      A,($10)             ;
0719: 06 08           LD      B,$08               
071B: DD 21 22 07     LD      IX,$0722            
071F: C3 A0 08        JP      $08A0               ; 
0722: DB 17           IN      A,($17)             ;
0724: 06 08           LD      B,$08               
0726: DD 21 2D 07     LD      IX,$072D            
072A: C3 A0 08        JP      $08A0               ; 
072D: DD 21 34 07     LD      IX,$0734            
0731: C3 DD 07        JP      $07DD               ; 
0734: 28 98           JR      Z,$6CE              ; 
0736: DD 21 3D 07     LD      IX,$073D            
073A: C3 B6 07        JP      $07B6               ; 
073D: 01 18 00        LD      BC,$0018            
0740: 11 00 80        LD      DE,$8000            
0743: 21 2F 04        LD      HL,$042F            
0746: ED B0           LDIR                        
0748: FD 21 4F 07     LD      IY,$074F            
074C: C3 CF 07        JP      $07CF               ;{DogAndDVG} 
074F: DD 21 56 07     LD      IX,$0756            
0753: C3 DD 07        JP      $07DD               ; 
0756: 28 F0           JR      Z,$748              ; 
0758: DD 21 5F 07     LD      IX,$075F            
075C: C3 B6 07        JP      $07B6               ; 
075F: 01 A0 00        LD      BC,$00A0            
0762: 11 00 80        LD      DE,$8000            
0765: 21 47 04        LD      HL,$0447            
0768: ED B0           LDIR                        
076A: FD 21 71 07     LD      IY,$0771            
076E: C3 CF 07        JP      $07CF               ;{DogAndDVG} 
0771: DD 21 78 07     LD      IX,$0778            
0775: C3 DD 07        JP      $07DD               ; 
0778: 28 F0           JR      Z,$76A              ; 
077A: DD 21 81 07     LD      IX,$0781            
077E: C3 DD 07        JP      $07DD               ; 
0781: 3E 16           LD      A,$16               
0783: D3 14           OUT     ($14),A             ;
0785: AF              XOR     A                   
0786: DD 21 8D 07     LD      IX,$078D            
078A: C3 B6 07        JP      $07B6               ; 
078D: 3D              DEC     A                   
078E: 20 F6           JR      NZ,$786             ; 
0790: DD 21 97 07     LD      IX,$0797            
0794: C3 DD 07        JP      $07DD               ; 
0797: 28 ED           JR      Z,$786              ; 
0799: 3E 00           LD      A,$00               
079B: D3 14           OUT     ($14),A             ;
079D: C3 EC 04        JP      $04EC               ; 

07A0: D9              EXX                         
07A1: 08              EX      AF,AF'              
07A2: 21 00 30        LD      HL,$3000            
07A5: DB 09           IN      A,($09)             ;
07A7: DB 0B           IN      A,($0B)             ;
07A9: CB 7F           BIT     7,A                 
07AB: 28 05           JR      Z,$7B2              ; 
07AD: 2B              DEC     HL                  
07AE: 7C              LD      A,H                 
07AF: B5              OR      L                   
07B0: 20 F3           JR      NZ,$7A5             ; 
07B2: 08              EX      AF,AF'              
07B3: D9              EXX                         
07B4: FD E9           JP      (IY)                

; First location of vector RAM to HALT. Clear the rest
07B6: FD 21 BD 07     LD      IY,$07BD            ; Continue after next
07BA: C3 A0 07        JP      $07A0               ; Feed watch dog
07BD: 01 FE 0F        LD      BC,$0FFE            ; Fill ...
07C0: 11 02 80        LD      DE,$8002            ; ... vector ...
07C3: 21 01 80        LD      HL,$8001            ; ... RAM ...
07C6: 36 B0           LD      (HL),$B0            ; ... with ...
07C8: 2B              DEC     HL                  ; ... 00 ...
07C9: 36 00           LD      (HL),$00            ; ... except ...
07CB: ED B0           LDIR                        ; ... 1st with B0 (HALT to DVG)
07CD: DD E9           JP      (IX)                ; No stack ... link
```

# Dog and DVG

```code
DogAndDVG: 
07CF: 08              EX      AF,AF'              ; Hold A
07D0: DB 09           IN      A,($09)             ; Bump watchdog
07D2: DB 0B           IN      A,($0B)             ; Is DVG running
07D4: CB 7F           BIT     7,A                 ; Test run bit
07D6: 20 02           JR      NZ,$7DA             ; Yes ... leave it running
07D8: DB 08           IN      A,($08)             ; Start it up
07DA: 08              EX      AF,AF'              ; Restore A
07DB: FD E9           JP      (IY)                ; Continue routine

07DD: D9              
07DE: DB 11           IN      A,($11)             ;
07E0: 5F              LD      E,A                 
07E1: A2              AND     D                   
07E2: AA              XOR     D                   
07E3: 53              LD      D,E                 
07E4: D9              EXX                         
07E5: CB 77           BIT     6,A                 
07E7: DD E9           JP      (IX)        
```

# Test ROM        

```code
TestROM: 
07E9: 79              LD      A,C                 ; Get LSB of count
07EA: B7              OR      A                   ; Is it 0?
07EB: 28 02           JR      Z,$7EF              ; ? It always is 0 ?
07ED: 04              INC     B                   ; ? Not sure what ?
07EE: AF              XOR     A                   ; ? This was meant to do ?
;
07EF: CB 7C           BIT     7,H                 ; Time to feed watchdog?
07F1: 20 07           JR      NZ,$7FA             ; No ... skip it
07F3: FD 21 FA 07     LD      IY,$07FA            ; Continue after next instruction
07F7: C3 CF 07        JP      $07CF               ;{DogAndDVG} Feed the watchdog
07FA: 86              ADD     A,(HL)              ; Add checksum
07FB: 23              INC     HL                  ; Next address to check
07FC: 0D              DEC     C                   ; Decrement LSB
07FD: 20 F0           JR      NZ,$7EF             ; LSB still non-zero ... keep going
07FF: 05              DEC     B                   ; LSB crossed zero ... borrow from MSB
0800: 20 ED           JR      NZ,$7EF             ; More to do ... keep going
;
0802: FD 21 09 08     LD      IY,$0809            ; Next code after
0806: C3 A0 07        JP      $07A0               ; Delay
0809: FE FF           CP      $FF                 ; Checksum FFs?
080B: 28 04           JR      Z,$811              ; Yes ... use value 05 (OK)
080D: 3E 0A           LD      A,$0A               ; Else ... use value 0A (NG)
080F: 18 02           JR      $813                ; Skip over
0811: 3E 05           LD      A,$05               ; Value 05 (OK)
0813: 12              LD      (DE),A              ; Store "OK" or "NG" token in vector list
0814: 21 12 00        LD      HL,$0012            ; Skip to next ...
0817: 19              ADD     HL,DE               ; ... screen ...
0818: EB              EX      DE,HL               ; ... row
0819: FE 05           CP      $05                 ; Z if OK, NZ if NG
081B: DD E9           JP      (IX)                ; Return
```

# Test RAM

```code
TestRAM: 
081D: CB 7C           BIT     7,H                 ; Time to feed watchdog?
081F: 20 07           JR      NZ,$828             ; No ... skip it
0821: FD 21 28 08     LD      IY,$0828            ; Continue after next instruction
0825: C3 CF 07        JP      $07CF               ;{DogAndDVG} Feed the watchdog and DVG
0828: DB 09           IN      A,($09)             ; Feed the watchdog
082A: 7E              LD      A,(HL)              ; Get value from RAM
082B: FE FF           CP      $FF                 ; We stuffed FF in there earlier
082D: 20 21           JR      NZ,$850             ; Oops ... not FF ... bad
082F: 36 55           LD      (HL),$55            ; Try another pattern
0831: 7E              LD      A,(HL)              ; Did it ...
0832: FE 55           CP      $55                 ; ... change correctly?
0834: 20 1A           JR      NZ,$850             ; Oops ... not 55 ... bad
0836: 36 AA           LD      (HL),$AA            ; Try yet another pattern ... test every bit
0838: 7E              LD      A,(HL)              ; Did it ...
0839: FE AA           CP      $AA                 ; ... change correctly?
083B: 20 13           JR      NZ,$850             ; Oops ... not AA ... bad
083D: 36 00           LD      (HL),$00            ; Clear the memory now that we are done
083F: 23              INC     HL                  ; Next RAM
0840: 0B              DEC     BC                  ; Decrement count
0841: 78              LD      A,B                 ; Jump ...
0842: B1              OR      C                   ; ... and ...
0843: 20 D8           JR      NZ,$81D             ;{TestRAM} ... do all
;
0845: FD 21 4C 08     LD      IY,$084C            ; Continue after next instruction
0849: C3 A0 07        JP      $07A0               ; Delay
084C: 3E 05           LD      A,$05               ; Value 05 (OK)
084E: 18 09           JR      $859                ; Save and out
0850: FD 21 57 08     LD      IY,$0857            ; Continue after next instruction
0854: C3 A0 07        JP      $07A0               ; Delay
0857: 3E 0A           LD      A,$0A               ; Value 0A (NG)
0859: 12              LD      (DE),A              ; Store "OK" or "NG" in vector list
085A: 21 12 00        LD      HL,$0012            ; Skip to ...
085D: 19              ADD     HL,DE               ; ... next row ...
085E: EB              EX      DE,HL               ; ... on screen
085F: FE 05           CP      $05                 ; Z if OK, NZ if bad
0861: DD E9           JP      (IX)                ; Return
```

# Test NONVOL

```code
TestNONVOL: 
0863: FD 21 6A 08     LD      IY,$086A            ; Continue after next
0867: C3 CF 07        JP      $07CF               ;{DogAndDVG} Feed watchdog and make sure DVG is running
086A: 36 0A           LD      (HL),$0A            ; Write pattern to LSB
086C: 7E              LD      A,(HL)              ; See ...
086D: E6 0F           AND     $0F                 ; ... if ...
086F: FE 0A           CP      $0A                 ; ... it took
0871: 20 1A           JR      NZ,$88D             ; Oops ... not xA ... bad
0873: 36 05           LD      (HL),$05            ; Try yet another pattern
0875: 7E              LD      A,(HL)              ; Did it ...
0876: E6 0F           AND     $0F                 ; ... change ...
0878: FE 05           CP      $05                 ; ... correctly?
087A: 20 11           JR      NZ,$88D             ; Oops ... not x5 ... bad
087C: 23              INC     HL                  ; Next in nonvol
087D: 0B              DEC     BC                  ; Decrement count
087E: 78              LD      A,B                 ; Jump ...
087F: B1              OR      C                   ; ... back ...
0880: 20 E1           JR      NZ,$863             ;{TestNONVOL} ... for all
;
0882: FD 21 89 08     LD      IY,$0889            ; Continue after next
0886: C3 A0 07        JP      $07A0               ; Delay
0889: 3E 05           LD      A,$05               ; Value 05 (OK)
088B: 18 09           JR      $896                ; Save and out
088D: FD 21 94 08     LD      IY,$0894            ; Continue after next
0891: C3 A0 07        JP      $07A0               ; Delay
0894: 3E 0A           LD      A,$0A               ; Value 0A (NG)
0896: 12              LD      (DE),A              ; Store "OK" or "NG" in vector list
0897: 21 12 00        LD      HL,$0012            ; Skip to ...
089A: 19              ADD     HL,DE               ; ... next row ...
089B: EB              EX      DE,HL               ; ... on screen
089C: FE 05           CP      $05                 ; Z if OK, NZ if bad
089E: DD E9           JP      (IX)                ; Return

08A0: 4F              LD      C,A                 
08A1: FD 21 A8 08     LD      IY,$08A8            
08A5: C3 A0 07        JP      $07A0               ; 
08A8: CB 09           RRC     C                   
08AA: 38 04           JR      C,$8B0              ; 
08AC: 3E 05           LD      A,$05               
08AE: 18 02           JR      $8B2                ; 
08B0: 3E 0A           LD      A,$0A               
08B2: 12              LD      (DE),A              
08B3: 21 12 00        LD      HL,$0012            
08B6: 19              ADD     HL,DE               
08B7: EB              EX      DE,HL               
08B8: 10 EE           DJNZ    $8A8                ; 
08BA: 21 12 00        LD      HL,$0012            
08BD: 19              ADD     HL,DE               
08BE: EB              EX      DE,HL               
08BF: FD 21 C6 08     LD      IY,$08C6            
08C3: C3 CF 07        JP      $07CF               ;{DogAndDVG} 
08C6: DD E9           JP      (IX)                
```

# Print String

```code
PrintString: 
; HL = ASCII string
; BC = length of string
; DE = vector ram
; IX = return address (link register)
08C8: DB 09           IN      A,($09)             ; Feed watchdog
08CA: 7E              LD      A,(HL)              ; Character from source string
08CB: 23              INC     HL                  ; Bump string pointer
08CC: 13              INC     DE                  ; Bump ...
08CD: 13              INC     DE                  ; ... screen cursor (always 1 ahead)
08CE: FD 21 00 00     LD      IY,$0000            ; Offset of 0
08D2: FD 19           ADD     IY,DE               ; Add offset
08D4: FD F9           LD      SP,IY               ; Screen ponter (use PUSH to store later)
08D6: D9              EXX                         ; Save BC, DE, HL
08D7: 16 00           LD      D,$00               ; DE will be character table offset. MSB=0.
08D9: FE 20           CP      $20                 ; Space character?
08DB: 20 05           JR      NZ,$8E2             ; No ... keep processing
08DD: 11 92 CD        LD      DE,$CD92            ; DJSR($0D92) space
08E0: 18 2C           JR      $90E                ; Store space and continue
08E2: FE 2E           CP      $2E                 ; '.' (used for CR/LF)
08E4: 20 05           JR      NZ,$8EB             ; No ... try other
08E6: 11 0F C0        LD      DE,$C00F            ; DJSR($800F) CR/LF
08E9: 18 23           JR      $90E                ; Store CR/LF and continue
08EB: FE 41           CP      $41                 ; 'A' 
08ED: 38 0D           JR      C,$8FC              ; Less than 'A' ... try numbers
08EF: FE 5A           CP      $5A                 ; 'Z'
08F1: 38 02           JR      C,$8F5              ; Letter A-Z? Yes ... keep it
08F3: 3E 5A           LD      A,$5A               ; Above Z becomes Z
08F5: D6 41           SUB     $41                 ; Offset as A=0, B=1, C=2, etc
08F7: 21 2E 3A        LD      HL,$3A2E            ; Letter offset table
08FA: 18 0B           JR      $907                ; Look up character and print
08FC: FE 30           CP      $30                 ; Range of a number?
08FE: 30 02           JR      NC,$902             ; Yes use it
0900: 3E 30           LD      A,$30               ; Below a '0' becomes a '0'
0902: D6 2F           SUB     $2F                 ; The player-ship is 0
0904: 21 D3 3F        LD      HL,$3FD3            ; Number table
0907: CB 27           SLA     A                   ; 2 bytes per table
0909: 5F              LD      E,A                 ; To LSB (MSB is 0)
090A: 19              ADD     HL,DE               ; Offset into table
090B: 5E              LD      E,(HL)              ; Get ...
090C: 23              INC     HL                  ; ... two byte ...
090D: 56              LD      D,(HL)              ; ... subroutine call
090E: D5              PUSH    DE                  ; Save character in vector RAM
090F: D9              EXX                         ; Restore HL, DE, BC
0910: 0B              DEC     BC                  ; All done?
0911: 78              LD      A,B                 ; If ...
0912: B1              OR      C                   ; ... not ...
0913: 20 B3           JR      NZ,$8C8             ;{PrintString} ... keep printing
0915: DD E9           JP      (IX)                ; Return through link

0917: 78              LD      A,B                 
0918: D9              EXX                         
0919: 47              LD      B,A                 
091A: D9              EXX                         
091B: 04              INC     B                   

091C: 3E C3           LD      A,$C3               ; 1100_0011
091E: D3 13           OUT     ($13),A             ; Turn on all 4 LEDs
0920: 3E 07           LD      A,$07               ; Play ...
0922: D3 14           OUT     ($14),A             ; ... beeping sound
0924: 21 00 30        LD      HL,$3000            ; Delay
0927: FD 21 2E 09     LD      IY,$092E            ; Next code is lights off
092B: C3 CF 07        JP      $07CF               ;{DogAndDVG} Watch dog and DVG

092E: 2B              DEC     HL                  ; Decrement counter
092F: 7C              LD      A,H                 ; Wait ...
0930: B5              OR      L                   ; ... till ...
0931: 20 F4           JR      NZ,$927             ; ... zero
0933: 3E FF           LD      A,$FF               ; LEDs ...
0935: D3 13           OUT     ($13),A             ; ... off
0937: 3E 00           LD      A,$00               ; Sound ...
0939: D3 14           OUT     ($14),A             ; ... off
093B: 21 00 30        LD      HL,$3000            ; Delay
093E: FD 21 45 09     LD      IY,$0945            ; Next code is ??
0942: C3 CF 07        JP      $07CF               ;{DogAndDVG} Watch dog and DVG

0945: 2B              DEC     HL                  ; Decrement counter
0946: 7C              LD      A,H                 ; Wait ...
0947: B5              OR      L                   ; ... till ...
0948: 20 F4           JR      NZ,$93E             ; ... zero
094A: 78              LD      A,B                 ; Flash value
094B: FE 02           CP      $02                 ; Anything but 2 ... 
094D: 20 02           JR      NZ,$951             ; ... lights on
094F: 10 D3           DJNZ    $924                ; Delay then lights off
0951: 10 C9           DJNZ    $91C                ; Lights on
0953: DD E9           JP      (IX)                ; No stack (RAM may be bad) ... use IX as link



0955: 31 FC 4B        LD      SP,$4BFC            
0958: FD 21 80 40     LD      IY,$4080            
095C: 01 81 04        LD      BC,$0481            
095F: 11 01 40        LD      DE,$4001            
0962: 21 00 40        LD      HL,$4000            
0965: 36 00           LD      (HL),$00            
0967: ED B0           LDIR                        
0969: FD 36 F2 FF     LD      (IY+$F2),$FF        
096D: CD BC 18        CALL    $18BC               ; 
0970: DB 11           IN      A,($11)             ;
0972: E6 03           AND     $03                 
0974: 32 35 40        LD      ($4035),A           ; 
0977: DB 17           IN      A,($17)             ;
0979: E6 07           AND     $07                 
097B: 07              RLCA                        
097C: 32 2B 40        LD      ($402B),A           ; 
097F: 6F              LD      L,A                 
0980: 26 00           LD      H,$00               
0982: 11 C3 2F        LD      DE,$2FC3            
0985: 19              ADD     HL,DE               
0986: 22 27 40        LD      ($4027),HL          ; 
0989: DB 17           IN      A,($17)             ;
098B: E6 38           AND     $38                 
098D: 0F              RRCA                        
098E: 0F              RRCA                        
098F: 32 2C 40        LD      ($402C),A           ; 
0992: 6F              LD      L,A                 
0993: 26 00           LD      H,$00               
0995: 11 C3 2F        LD      DE,$2FC3            
0998: 19              ADD     HL,DE               
0999: 22 29 40        LD      ($4029),HL          ; 
099C: 01 2A 00        LD      BC,$002A            
099F: 11 A9 43        LD      DE,$43A9            
09A2: 21 F7 2F        LD      HL,$2FF7            
09A5: ED B0           LDIR                        
09A7: 01 54 00        LD      BC,$0054            
09AA: 11 D3 43        LD      DE,$43D3            
09AD: 21 A9 43        LD      HL,$43A9            
09B0: ED B0           LDIR                        
09B2: 0E 02           LD      C,$02               
09B4: 11 1A 5C        LD      DE,$5C1A            
09B7: 06 10           LD      B,$10               
09B9: 21 C9 30        LD      HL,$30C9            
09BC: 1A              LD      A,(DE)              
09BD: E6 0F           AND     $0F                 
09BF: BE              CP      (HL)                
09C0: 20 79           JR      NZ,$A3B             ; 
09C2: 13              INC     DE                  
09C3: 23              INC     HL                  
09C4: 10 F6           DJNZ    $9BC                ; 
09C6: 0D              DEC     C                   
09C7: 20 EE           JR      NZ,$9B7             ; 
09C9: 06 02           LD      B,$02               
09CB: 11 3A 5C        LD      DE,$5C3A            
09CE: 21 D3 43        LD      HL,$43D3            
09D1: 0E 04           LD      C,$04               
09D3: CD 18 0A        CALL    $0A18               ; 
09D6: 30 63           JR      NC,$A3B             ; 
09D8: 0D              DEC     C                   
09D9: 20 F8           JR      NZ,$9D3             ; 
09DB: 0E 03           LD      C,$03               
09DD: 1A              LD      A,(DE)              
09DE: 13              INC     DE                  
09DF: ED 67           RRD                         
09E1: 1A              LD      A,(DE)              
09E2: 13              INC     DE                  
09E3: ED 67           RRD                         
09E5: 7E              LD      A,(HL)              
09E6: 23              INC     HL                  
09E7: FE 20           CP      $20                 
09E9: 28 08           JR      Z,$9F3              ; 
09EB: FE 41           CP      $41                 
09ED: 38 4C           JR      C,$A3B              ; 
09EF: FE 5B           CP      $5B                 
09F1: 30 48           JR      NC,$A3B             ; 
09F3: 0D              DEC     C                   
09F4: 20 E7           JR      NZ,$9DD             ; 
09F6: 21 FD 43        LD      HL,$43FD            
09F9: 10 D6           DJNZ    $9D1                ; 
09FB: 06 40           LD      B,$40               
09FD: 11 58 5C        LD      DE,$5C58            
0A00: 21 27 44        LD      HL,$4427            
0A03: CD 18 0A        CALL    $0A18               ; 
0A06: 30 33           JR      NC,$A3B             ; 
0A08: 10 F9           DJNZ    $A03                ; 
0A0A: 11 56 5C        LD      DE,$5C56            
0A0D: 21 2D 40        LD      HL,$402D            
0A10: CD 18 0A        CALL    $0A18               ; 
0A13: 30 26           JR      NC,$A3B             ; 
0A15: C3 9D 0A        JP      $0A9D               ; 
0A18: 1A              LD      A,(DE)              
0A19: 13              INC     DE                  
0A1A: E6 0F           AND     $0F                 
0A1C: FE 0A           CP      $0A                 
0A1E: 30 0D           JR      NC,$A2D             ; 
0A20: ED 67           RRD                         
0A22: 1A              LD      A,(DE)              
0A23: 13              INC     DE                  
0A24: E6 0F           AND     $0F                 
0A26: FE 0A           CP      $0A                 
0A28: 30 03           JR      NC,$A2D             ; 
0A2A: ED 67           RRD                         
0A2C: 23              INC     HL                  
0A2D: C9              RET                         
0A2E: 1A              LD      A,(DE)              
0A2F: 13              INC     DE                  
0A30: 77              LD      (HL),A              
0A31: 23              INC     HL                  
0A32: 0F              RRCA                        
0A33: 0F              RRCA                        
0A34: 0F              RRCA                        
0A35: 0F              RRCA                        
0A36: 77              LD      (HL),A              
0A37: 23              INC     HL                  
0A38: 10 F4           DJNZ    $A2E                ; 
0A3A: C9              RET                         
0A3B: AF              XOR     A                   
0A3C: 32 2D 40        LD      ($402D),A           ; 
0A3F: 01 3F 00        LD      BC,$003F            
0A42: 11 28 44        LD      DE,$4428            
0A45: 21 27 44        LD      HL,$4427            
0A48: 36 00           LD      (HL),$00            
0A4A: ED B0           LDIR                        
0A4C: 01 2A 00        LD      BC,$002A            
0A4F: 11 A9 43        LD      DE,$43A9            
0A52: 21 F7 2F        LD      HL,$2FF7            
0A55: ED B0           LDIR                        
0A57: 01 54 00        LD      BC,$0054            
0A5A: 11 D3 43        LD      DE,$43D3            
0A5D: 21 A9 43        LD      HL,$43A9            
0A60: ED B0           LDIR                        
0A62: CD 68 0A        CALL    $0A68               ; 
0A65: C3 9D 0A        JP      $0A9D               ; 
0A68: 06 07           LD      B,$07               
0A6A: 11 D3 43        LD      DE,$43D3            
0A6D: 21 3A 5C        LD      HL,$5C3A            
0A70: CD 2E 0A        CALL    $0A2E               ; 
0A73: 06 07           LD      B,$07               
0A75: 11 FD 43        LD      DE,$43FD            
0A78: CD 2E 0A        CALL    $0A2E               ; 
0A7B: 06 40           LD      B,$40               
0A7D: 11 27 44        LD      DE,$4427            
0A80: 21 58 5C        LD      HL,$5C58            
0A83: CD 2E 0A        CALL    $0A2E               ; 
0A86: CD E3 16        CALL    $16E3               ; 
0A89: 01 10 00        LD      BC,$0010            
0A8C: 11 1A 5C        LD      DE,$5C1A            
0A8F: 21 C9 30        LD      HL,$30C9            
0A92: ED B0           LDIR                        
0A94: 01 10 00        LD      BC,$0010            
0A97: 21 1A 5C        LD      HL,$5C1A            
0A9A: ED B0           LDIR                        
0A9C: C9              RET                         
0A9D: FD 21 80 40     LD      IY,$4080            
0AA1: FB              EI                          
0AA2: CD 48 12        CALL    $1248               ; 
0AA5: CD 6C 12        CALL    $126C               ; 
0AA8: FD 36 AE 00     LD      (IY+$AE),$00        
0AAC: FD 36 A4 01     LD      (IY+$A4),$01        
0AB0: FD CB C1 7E     BIT     7,(IY+$C1)          
0AB4: 28 0C           JR      Z,$AC2              ; 
0AB6: FD CB C1 76     BIT     6,(IY+$C1)          
0ABA: 20 06           JR      NZ,$AC2             ; 
0ABC: 21 46 40        LD      HL,$4046            
0ABF: CD 8E 2C        CALL    $2C8E               ; 
0AC2: DB 17           IN      A,($17)             ;
0AC4: CB 77           BIT     6,A                 
0AC6: 28 04           JR      Z,$ACC              ; 
0AC8: FD 36 AD 04     LD      (IY+$AD),$04        
0ACC: 3A 41 40        LD      A,($4041)           ; 
0ACF: E6 40           AND     $40                 
0AD1: 32 41 40        LD      ($4041),A           ; 
0AD4: FD 36 BF 01     LD      (IY+$BF),$01        
0AD8: FD 36 BE 01     LD      (IY+$BE),$01        
0ADC: FD 36 04 00     LD      (IY+$04),$00        
0AE0: FD 36 0B 00     LD      (IY+$0B),$00        
0AE4: FD 36 09 01     LD      (IY+$09),$01        
0AE8: FD 36 03 01     LD      (IY+$03),$01        
0AEC: FD 36 A0 00     LD      (IY+$A0),$00        
0AF0: FD 36 A1 00     LD      (IY+$A1),$00        
0AF4: FD 36 E7 04     LD      (IY+$E7),$04        
0AF8: FD 36 02 00     LD      (IY+$02),$00        
0AFC: FD 36 F0 00     LD      (IY+$F0),$00        
0B00: CD 23 18        CALL    $1823               ; 
0B03: 3A 2D 40        LD      A,($402D)           ; 
0B06: B7              OR      A                   
0B07: CA 76 0B        JP      Z,$0B76             ; 
0B0A: FD 36 A1 3C     LD      (IY+$A1),$3C        
0B0E: DB 10           IN      A,($10)             ;
0B10: E6 03           AND     $03                 
0B12: 07              RLCA                        
0B13: 5F              LD      E,A                 
0B14: 16 00           LD      D,$00               
0B16: 21 E5 2F        LD      HL,$2FE5            
0B19: 19              ADD     HL,DE               
0B1A: 5E              LD      E,(HL)              
0B1B: 23              INC     HL                  
0B1C: 56              LD      D,(HL)              
0B1D: ED 53 60 40     LD      ($4060),DE          ; 
0B21: DB 10           IN      A,($10)             ;
0B23: E6 0C           AND     $0C                 
0B25: 0F              RRCA                        
0B26: 5F              LD      E,A                 
0B27: 16 00           LD      D,$00               
0B29: 21 ED 2F        LD      HL,$2FED            
0B2C: 19              ADD     HL,DE               
0B2D: 5E              LD      E,(HL)              
0B2E: 23              INC     HL                  
0B2F: 56              LD      D,(HL)              
0B30: 23              INC     HL                  
0B31: ED 53 62 40     LD      ($4062),DE          ; 
0B35: 5E              LD      E,(HL)              
0B36: 23              INC     HL                  
0B37: 56              LD      D,(HL)              
0B38: ED 53 64 40     LD      ($4064),DE          ; 
0B3C: FD 36 04 04     LD      (IY+$04),$04        
0B40: CD F3 2A        CALL    $2AF3               ; 
0B43: DB 10           IN      A,($10)             ;
0B45: E6 30           AND     $30                 
0B47: 0F              RRCA                        
0B48: 0F              RRCA                        
0B49: 0F              RRCA                        
0B4A: 5F              LD      E,A                 
0B4B: 16 00           LD      D,$00               
0B4D: 21 D3 2F        LD      HL,$2FD3            
0B50: 19              ADD     HL,DE               
0B51: 46              LD      B,(HL)              
0B52: 23              INC     HL                  
0B53: 3E 08           LD      A,$08               
0B55: 96              SUB     (HL)                
0B56: 4F              LD      C,A                 
0B57: 21 00 F0        LD      HL,$F000            
0B5A: 78              LD      A,B                 
0B5B: FE 02           CP      $02                 
0B5D: 20 03           JR      NZ,$B62             ; 
0B5F: 22 F0 80        LD      ($80F0),HL          ; 
0B62: 0D              DEC     C                   
0B63: 28 16           JR      Z,$B7B              ; 
0B65: 0D              DEC     C                   
0B66: 28 09           JR      Z,$B71              ; 
0B68: 0D              DEC     C                   
0B69: 28 03           JR      Z,$B6E              ; 
0B6B: 22 30 81        LD      ($8130),HL          ; 
0B6E: 22 32 81        LD      ($8132),HL          ; 
0B71: 22 34 81        LD      ($8134),HL          ; 
0B74: 18 05           JR      $B7B                ; 
0B76: 3E 00           LD      A,$00               
0B78: CD 04 2E        CALL    $2E04               ; 
0B7B: 06 01           LD      B,$01               
0B7D: CD 1D 29        CALL    $291D               ; 
0B80: C3 30 0F        JP      $0F30               ; 
0B83: CD 48 12        CALL    $1248               ; 
0B86: CD 54 18        CALL    $1854               ; 
0B89: CD 6C 12        CALL    $126C               ; 
0B8C: FD 36 A4 02     LD      (IY+$A4),$02        
0B90: FD 36 AE 00     LD      (IY+$AE),$00        
0B94: FD CB C1 7E     BIT     7,(IY+$C1)          
0B98: 28 0C           JR      Z,$BA6              ; 
0B9A: FD CB C1 76     BIT     6,(IY+$C1)          
0B9E: 20 06           JR      NZ,$BA6             ; 
0BA0: 21 46 40        LD      HL,$4046            
0BA3: CD 8E 2C        CALL    $2C8E               ; 
0BA6: 3A 83 40        LD      A,($4083)           ; 
0BA9: FE 07           CP      $07                 
0BAB: 28 06           JR      Z,$BB3              ; 
0BAD: 3A 2D 40        LD      A,($402D)           ; 
0BB0: B7              OR      A                   
0BB1: 20 1E           JR      NZ,$BD1             ; 
0BB3: FD CB C1 EE     SET     5,(IY+$C1)          
0BB7: FD 36 BE 01     LD      (IY+$BE),$01        
0BBB: FD CB C1 76     BIT     6,(IY+$C1)          
0BBF: 28 5D           JR      Z,$C1E              ; 
0BC1: FD 36 BE 02     LD      (IY+$BE),$02        
0BC5: DB 17           IN      A,($17)             ;
0BC7: CB 7F           BIT     7,A                 
0BC9: 28 53           JR      Z,$C1E              ; 
0BCB: FD CB C1 D6     SET     2,(IY+$C1)          
0BCF: 18 4D           JR      $C1E                ; 
0BD1: FD 36 A4 03     LD      (IY+$A4),$03        
0BD5: FD CB C1 FE     SET     7,(IY+$C1)          
0BD9: DB 17           IN      A,($17)             ;
0BDB: CB 77           BIT     6,A                 
0BDD: 20 0C           JR      NZ,$BEB             ; 
0BDF: F3              DI                          
0BE0: 3A 2D 40        LD      A,($402D)           ; 
0BE3: FD 96 C0        SUB     (IY+$C0)            
0BE6: 27              DAA                         
0BE7: 32 2D 40        LD      ($402D),A           ; 
0BEA: FB              EI                          
0BEB: FD CB AE FE     SET     7,(IY+$AE)          
0BEF: 2A 36 40        LD      HL,($4036)          ; 
0BF2: 22 42 40        LD      ($4042),HL          ; 
0BF5: 2A 38 40        LD      HL,($4038)          ; 
0BF8: 22 44 40        LD      ($4044),HL          ; 
0BFB: 21 00 00        LD      HL,$0000            
0BFE: 22 36 40        LD      ($4036),HL          ; 
0C01: 22 38 40        LD      ($4038),HL          ; 
0C04: 22 3A 40        LD      ($403A),HL          ; 
0C07: 22 3C 40        LD      ($403C),HL          ; 
0C0A: 01 2A 00        LD      BC,$002A            
0C0D: 11 A9 43        LD      DE,$43A9            
0C10: 21 D3 43        LD      HL,$43D3            
0C13: FD CB C1 6E     BIT     5,(IY+$C1)          
0C17: 28 03           JR      Z,$C1C              ; 
0C19: 21 FD 43        LD      HL,$43FD            
0C1C: ED B0           LDIR                        
0C1E: DB 10           IN      A,($10)             ;
0C20: E6 30           AND     $30                 
0C22: 0F              RRCA                        
0C23: 0F              RRCA                        
0C24: 0F              RRCA                        
0C25: FD CB C1 6E     BIT     5,(IY+$C1)          
0C29: 28 01           JR      Z,$C2C              ; 
0C2B: 3C              INC     A                   
0C2C: 5F              LD      E,A                 
0C2D: 16 00           LD      D,$00               
0C2F: 21 D3 2F        LD      HL,$2FD3            
0C32: 19              ADD     HL,DE               
0C33: 7E              LD      A,(HL)              
0C34: 32 66 40        LD      ($4066),A           ; 
0C37: FD 36 E7 06     LD      (IY+$E7),$06        
0C3B: FD 36 ED 00     LD      (IY+$ED),$00        
0C3F: FD 36 A0 00     LD      (IY+$A0),$00        
0C43: FD 36 A1 00     LD      (IY+$A1),$00        
0C47: FD 36 A2 19     LD      (IY+$A2),$19        
0C4B: FD 36 EA 00     LD      (IY+$EA),$00        
0C4F: FD 36 EB 00     LD      (IY+$EB),$00        
0C53: FD 36 EC 00     LD      (IY+$EC),$00        
0C57: FD 36 E8 01     LD      (IY+$E8),$01        
0C5B: 21 46 40        LD      HL,$4046            
0C5E: CD 8E 2C        CALL    $2C8E               ; 
0C61: 21 53 40        LD      HL,$4053            
0C64: CD 8E 2C        CALL    $2C8E               ; 
0C67: CD 23 18        CALL    $1823               ; 
0C6A: CD 02 19        CALL    $1902               ; 
0C6D: FD CB C1 76     BIT     6,(IY+$C1)          
0C71: 28 15           JR      Z,$C88              ; 
0C73: FD 36 04 07     LD      (IY+$04),$07        
0C77: CD F3 2A        CALL    $2AF3               ; 
0C7A: FD 36 04 08     LD      (IY+$04),$08        
0C7E: CD F3 2A        CALL    $2AF3               ; 
0C81: FD 36 04 0A     LD      (IY+$04),$0A        
0C85: CD F3 2A        CALL    $2AF3               ; 
0C88: CD 68 0A        CALL    $0A68               ; 
0C8B: 06 20           LD      B,$20               
0C8D: CD 1D 29        CALL    $291D               ; 
0C90: CD B2 29        CALL    $29B2               ; 
0C93: 10 F8           DJNZ    $C8D                ; 
0C95: FD 34 EE        INC     (IY+$EE)            ;
0C98: CD 54 18        CALL    $1854               ; 
0C9B: FD CB EB 76     BIT     6,(IY+$EB)          
0C9F: 28 7A           JR      Z,$D1B              ; 
0CA1: FD 34 EC        INC     (IY+$EC)            ;
0CA4: 3A 6C 40        LD      A,($406C)           ; 
0CA7: E6 03           AND     $03                 
0CA9: 20 70           JR      NZ,$D1B             ; 
0CAB: 3A 6C 40        LD      A,($406C)           ; 
0CAE: CB 2F           SRA     A                   
0CB0: CB 2F           SRA     A                   
0CB2: FE 06           CP      $06                 
0CB4: 38 02           JR      C,$CB8              ; 
0CB6: 3E 06           LD      A,$06               
0CB8: C6 16           ADD     A,$16               
0CBA: 32 84 40        LD      ($4084),A           ; 
0CBD: CD F3 2A        CALL    $2AF3               ; 
0CC0: FD 36 04 16     LD      (IY+$04),$16        
0CC4: CD F3 2A        CALL    $2AF3               ; 
0CC7: 21 00 B0        LD      HL,$B000            
0CCA: 22 92 80        LD      ($8092),HL          ; 
0CCD: 22 94 80        LD      ($8094),HL          ; 
0CD0: FD 36 A1 05     LD      (IY+$A1),$05        
0CD4: DB 09           IN      A,($09)             ;
0CD6: CD D5 17        CALL    $17D5               ; 
0CD9: 3A 17 40        LD      A,($4017)           ; 
0CDC: 47              LD      B,A                 
0CDD: FD 96 98        SUB     (IY+$98)            
0CE0: FD 70 98        LD      (IY+$98),B          
0CE3: 30 EF           JR      NC,$CD4             ; 
0CE5: 11 3A 40        LD      DE,$403A            
0CE8: 21 F7 3F        LD      HL,$3FF7            
0CEB: CD D5 16        CALL    $16D5               ; 
0CEE: FD 35 A1        DEC     (IY+$A1)            
0CF1: 3A 21 40        LD      A,($4021)           ; 
0CF4: B7              OR      A                   
0CF5: 28 13           JR      Z,$D0A              ; 
0CF7: FE 02           CP      $02                 
0CF9: 20 D9           JR      NZ,$CD4             ; 
0CFB: FD 36 A1 00     LD      (IY+$A1),$00        
0CFF: 3E 14           LD      A,$14               
0D01: CD 04 2E        CALL    $2E04               ; 
0D04: FD 36 A1 02     LD      (IY+$A1),$02        
0D08: 18 CA           JR      $CD4                ; 
0D0A: 20 C8           JR      NZ,$CD4             ; 
0D0C: CD 54 18        CALL    $1854               ; 
0D0F: 06 02           LD      B,$02               
0D11: 3E 05           LD      A,$05               
0D13: CD 35 23        CALL    $2335               ; 
0D16: 10 F9           DJNZ    $D11                ; 
0D18: CD 54 18        CALL    $1854               ; 
0D1B: FD CB C1 76     BIT     6,(IY+$C1)          
0D1F: CA DF 0D        JP      Z,$0DDF             ; 
0D22: FD CB 32 7E     BIT     7,(IY+$32)          
0D26: 28 07           JR      Z,$D2F              ; 
0D28: FD CB 32 66     BIT     4,(IY+$32)          
0D2C: C2 DF 0D        JP      NZ,$0DDF            ; 
0D2F: 3A 6D 40        LD      A,($406D)           ; 
0D32: B7              OR      A                   
0D33: 28 1C           JR      Z,$D51              ; 
0D35: FD 35 ED        DEC     (IY+$ED)            
0D38: 2A F3 3E        LD      HL,($3EF3)          ; 
0D3B: 22 42 82        LD      ($8242),HL          ; 
0D3E: FD 36 04 0B     LD      (IY+$04),$0B        
0D42: CD F3 2A        CALL    $2AF3               ; 
0D45: FD 36 A1 00     LD      (IY+$A1),$00        
0D49: 3E 14           LD      A,$14               
0D4B: CD 04 2E        CALL    $2E04               ; 
0D4E: C3 DF 0D        JP      $0DDF               ; 
0D51: 3A 3E 40        LD      A,($403E)           ; 
0D54: FE 01           CP      $01                 
0D56: 28 32           JR      Z,$D8A              ; 
0D58: 21 53 40        LD      HL,$4053            
0D5B: CD 8E 2C        CALL    $2C8E               ; 
0D5E: FD 36 BE 01     LD      (IY+$BE),$01        
0D62: 21 46 40        LD      HL,$4046            
0D65: CD BD 2C        CALL    $2CBD               ; 
0D68: CD 55 12        CALL    $1255               ; 
0D6B: 01 10 00        LD      BC,$0010            
0D6E: 11 34 82        LD      DE,$8234            
0D71: 21 F5 3E        LD      HL,$3EF5            
0D74: ED B0           LDIR                        
0D76: 01 64 00        LD      BC,$0064            
0D79: 11 58 82        LD      DE,$8258            
0D7C: 21 B1 31        LD      HL,$31B1            
0D7F: ED B0           LDIR                        
0D81: FD 36 04 0C     LD      (IY+$04),$0C        
0D85: CD F3 2A        CALL    $2AF3               ; 
0D88: 18 30           JR      $DBA                ; 
0D8A: 21 46 40        LD      HL,$4046            
0D8D: CD 8E 2C        CALL    $2C8E               ; 
0D90: FD 36 BE 02     LD      (IY+$BE),$02        
0D94: 21 53 40        LD      HL,$4053            
0D97: CD BD 2C        CALL    $2CBD               ; 
0D9A: CD 55 12        CALL    $1255               ; 
0D9D: 01 10 00        LD      BC,$0010            
0DA0: 11 34 82        LD      DE,$8234            
0DA3: 21 05 3F        LD      HL,$3F05            
0DA6: ED B0           LDIR                        
0DA8: 01 64 00        LD      BC,$0064            
0DAB: 11 58 82        LD      DE,$8258            
0DAE: 21 69 3F        LD      HL,$3F69            
0DB1: ED B0           LDIR                        
0DB3: FD 36 04 0D     LD      (IY+$04),$0D        
0DB7: CD F3 2A        CALL    $2AF3               ; 
0DBA: FD 36 EB 00     LD      (IY+$EB),$00        
0DBE: 06 04           LD      B,$04               
0DC0: 11 39 40        LD      DE,$4039            
0DC3: 21 17 46        LD      HL,$4617            
0DC6: CD 0E 24        CALL    $240E               ; 
0DC9: 06 01           LD      B,$01               
0DCB: 11 2D 40        LD      DE,$402D            
0DCE: 21 2B 46        LD      HL,$462B            
0DD1: CD 0E 24        CALL    $240E               ; 
0DD4: 06 04           LD      B,$04               
0DD6: 11 45 40        LD      DE,$4045            
0DD9: 21 46 82        LD      HL,$8246            
0DDC: CD 0E 24        CALL    $240E               ; 
0DDF: 06 08           LD      B,$08               
0DE1: 21 9B 40        LD      HL,$409B            
0DE4: 36 01           LD      (HL),$01            
0DE6: 23              INC     HL                  
0DE7: 10 FB           DJNZ    $DE4                ; 
0DE9: FD 36 1A 80     LD      (IY+$1A),$80        
0DED: FD 36 24 01     LD      (IY+$24),$01        
0DF1: FD 36 27 01     LD      (IY+$27),$01        
0DF5: FD 36 2A 01     LD      (IY+$2A),$01        
0DF9: FD 36 2D 01     LD      (IY+$2D),$01        
0DFD: 3A 23 40        LD      A,($4023)           ; 
0E00: B7              OR      A                   
0E01: 20 04           JR      NZ,$E07             ; 
0E03: FD 36 A3 02     LD      (IY+$A3),$02        
0E07: 3A 23 40        LD      A,($4023)           ; 
0E0A: 32 21 40        LD      ($4021),A           ; 
0E0D: FD 36 E8 01     LD      (IY+$E8),$01        
0E11: FD 36 E9 00     LD      (IY+$E9),$00        
0E15: CD 86 21        CALL    $2186               ; 
0E18: CD 06 29        CALL    $2906               ; 
0E1B: 32 79 40        LD      ($4079),A           ; 
0E1E: FD CB EB 76     BIT     6,(IY+$EB)          
0E22: 28 19           JR      Z,$E3D              ; 
0E24: FD 34 E7        INC     (IY+$E7)            ;
0E27: FD 34 E7        INC     (IY+$E7)            ;
0E2A: 3A 67 40        LD      A,($4067)           ; 
0E2D: FE 0A           CP      $0A                 
0E2F: 38 04           JR      C,$E35              ; 
0E31: FD CB EA FE     SET     7,(IY+$EA)          
0E35: FE 0C           CP      $0C                 
0E37: 38 04           JR      C,$E3D              ; 
0E39: FD 36 E7 0C     LD      (IY+$E7),$0C        
0E3D: 3A 67 40        LD      A,($4067)           ; 
0E40: 06 15           LD      B,$15               
0E42: FE 06           CP      $06                 
0E44: 20 02           JR      NZ,$E48             ; 
0E46: 06 20           LD      B,$20               
0E48: CD B2 29        CALL    $29B2               ; 
0E4B: 10 FB           DJNZ    $E48                ; 
0E4D: FD 46 E7        LD      B,(IY+$E7)          
0E50: 04              INC     B                   
0E51: CD 1D 29        CALL    $291D               ; 
0E54: 10 FB           DJNZ    $E51                ; 
0E56: 3A 67 40        LD      A,($4067)           ; 
0E59: FE 06           CP      $06                 
0E5B: 20 30           JR      NZ,$E8D             ; 
0E5D: DD 21 C9 40     LD      IX,$40C9            
0E61: DD CB 00 B6     RES     6,(IX+$00)          
0E65: DD 21 E0 40     LD      IX,$40E0            
0E69: DD CB 00 B6     RES     6,(IX+$00)          
0E6D: DD 21 F7 40     LD      IX,$40F7            
0E71: DD CB 00 B6     RES     6,(IX+$00)          
0E75: DD 21 0E 41     LD      IX,$410E            
0E79: DD CB 00 B6     RES     6,(IX+$00)          
0E7D: DD 21 25 41     LD      IX,$4125            
0E81: DD CB 00 B6     RES     6,(IX+$00)          
0E85: DD 21 3C 41     LD      IX,$413C            
0E89: DD CB 00 B6     RES     6,(IX+$00)          
0E8D: FD 36 FA 00     LD      (IY+$FA),$00        
0E91: FD 36 FB 00     LD      (IY+$FB),$00        
0E95: FD 36 EB 00     LD      (IY+$EB),$00        
0E99: DD 21 C9 40     LD      IX,$40C9            
0E9D: FD 36 F7 02     LD      (IY+$F7),$02        
0EA1: CD 67 24        CALL    $2467               ; 
0EA4: 3A 24 40        LD      A,($4024)           ; 
0EA7: FE 02           CP      $02                 
0EA9: 20 10           JR      NZ,$EBB             ; 
0EAB: FD CB 33 FE     SET     7,(IY+$33)          
0EAF: FD CB 32 C6     SET     0,(IY+$32)          
0EB3: FD 36 44 0E     LD      (IY+$44),$0E        
0EB7: FD 36 40 14     LD      (IY+$40),$14        
0EBB: CD F9 2C        CALL    $2CF9               ; 
0EBE: FD CB C1 76     BIT     6,(IY+$C1)          
0EC2: 20 06           JR      NZ,$ECA             ; 
0EC4: 21 00 D0        LD      HL,$D000            
0EC7: 22 34 83        LD      ($8334),HL          ; 
0ECA: 3A 67 40        LD      A,($4067)           ; 
0ECD: FE 0C           CP      $0C                 
0ECF: 30 04           JR      NC,$ED5             ; 
0ED1: FD 36 A2 19     LD      (IY+$A2),$19        
0ED5: FD 36 FC FA     LD      (IY+$FC),$FA        
0ED9: 3A 6C 40        LD      A,($406C)           ; 
0EDC: FE 07           CP      $07                 
0EDE: 38 04           JR      C,$EE4              ; 
0EE0: FD 36 FC 4B     LD      (IY+$FC),$4B        
0EE4: 18 4A           JR      $F30                ; 
0EE6: 3E 00           LD      A,$00               
0EE8: CD 04 2E        CALL    $2E04               ; 
0EEB: 06 01           LD      B,$01               
0EED: CD 1D 29        CALL    $291D               ; 
0EF0: FD 36 F7 02     LD      (IY+$F7),$02        
0EF4: CD 23 18        CALL    $1823               ; 
0EF7: 01 7A 00        LD      BC,$007A            
0EFA: 11 81 44        LD      DE,$4481            
0EFD: 21 0E 3A        LD      HL,$3A0E            
0F00: ED B0           LDIR                        
0F02: FD 36 18 00     LD      (IY+$18),$00        
0F06: FD 36 A0 00     LD      (IY+$A0),$00        
0F0A: FD 36 04 11     LD      (IY+$04),$11        
0F0E: CD F3 2A        CALL    $2AF3               ; 
0F11: FD CB C1 76     BIT     6,(IY+$C1)          
0F15: 28 19           JR      Z,$F30              ; 
0F17: CD 55 12        CALL    $1255               ; 
0F1A: FD CB BE 46     BIT     0,(IY+$BE)          
0F1E: 28 09           JR      Z,$F29              ; 
0F20: FD 36 04 12     LD      (IY+$04),$12        
0F24: CD F3 2A        CALL    $2AF3               ; 
0F27: 18 07           JR      $F30                ; 
0F29: FD 36 04 13     LD      (IY+$04),$13        
0F2D: CD F3 2A        CALL    $2AF3               ; 
0F30: 3E 00           LD      A,$00               
0F32: 32 17 40        LD      ($4017),A           ; 
0F35: 32 18 40        LD      ($4018),A           ; 
0F38: FB              EI                          
0F39: FD 21 80 40     LD      IY,$4080            
0F3D: DB 09           IN      A,($09)             ;
0F3F: 3A 17 40        LD      A,($4017)           ; 
0F42: FD 96 98        SUB     (IY+$98)            
0F45: 32 19 40        LD      ($4019),A           ; 
0F48: 47              LD      B,A                 
0F49: 3A 17 40        LD      A,($4017)           ; 
0F4C: 32 18 40        LD      ($4018),A           ; 
0F4F: 30 7B           JR      NC,$FCC             ; 
0F51: FD 34 A0        INC     (IY+$A0)            ;
0F54: 11 3A 40        LD      DE,$403A            
0F57: 21 F7 3F        LD      HL,$3FF7            
0F5A: CD D5 16        CALL    $16D5               ; 
0F5D: 3A 21 40        LD      A,($4021)           ; 
0F60: B7              OR      A                   
0F61: 28 30           JR      Z,$F93              ; 
0F63: FD 35 A1        DEC     (IY+$A1)            
0F66: 20 2B           JR      NZ,$F93             ; 
0F68: 3A 82 40        LD      A,($4082)           ; 
0F6B: B7              OR      A                   
0F6C: FD 36 02 00     LD      (IY+$02),$00        
0F70: 28 08           JR      Z,$F7A              ; 
0F72: 3E 00           LD      A,$00               
0F74: CD 04 2E        CALL    $2E04               ; 
0F77: C3 9D 0A        JP      $0A9D               ; 
0F7A: FD 36 E9 00     LD      (IY+$E9),$00        
0F7E: 3A 68 40        LD      A,($4068)           ; 
0F81: FD 36 E8 00     LD      (IY+$E8),$00        
0F85: CD F6 2D        CALL    $2DF6               ; 
0F88: FD CB AF 6E     BIT     5,(IY+$AF)          
0F8C: 20 05           JR      NZ,$F93             ; 
0F8E: 3E 09           LD      A,$09               
0F90: CD 04 2E        CALL    $2E04               ; 
0F93: 3A 22 40        LD      A,($4022)           ; 
0F96: B7              OR      A                   
0F97: 28 09           JR      Z,$FA2              ; 
0F99: FD 35 A2        DEC     (IY+$A2)            
0F9C: 20 04           JR      NZ,$FA2             ; 
0F9E: FD CB EA FE     SET     7,(IY+$EA)          
0FA2: 3A 23 40        LD      A,($4023)           ; 
0FA5: B7              OR      A                   
0FA6: 28 24           JR      Z,$FCC              ; 
0FA8: 3D              DEC     A                   
0FA9: 32 23 40        LD      ($4023),A           ; 
0FAC: 20 1E           JR      NZ,$FCC             ; 
0FAE: FD CB EA F6     SET     6,(IY+$EA)          
0FB2: FD CB EB FE     SET     7,(IY+$EB)          
0FB6: FD CB AE 7E     BIT     7,(IY+$AE)          
0FBA: 28 10           JR      Z,$FCC              ; 
0FBC: 3A 24 40        LD      A,($4024)           ; 
0FBF: FE 01           CP      $01                 
0FC1: 28 09           JR      Z,$FCC              ; 
0FC3: CD 54 18        CALL    $1854               ; 
0FC6: 21 00 F0        LD      HL,$F000            
0FC9: 22 42 82        LD      ($8242),HL          ; 
0FCC: 3A 70 40        LD      A,($4070)           ; 
0FCF: 90              SUB     B                   
0FD0: 30 02           JR      NC,$FD4             ; 
0FD2: 3E 00           LD      A,$00               
0FD4: 32 70 40        LD      ($4070),A           ; 
0FD7: CD F4 14        CALL    $14F4               ; 
0FDA: FD CB A4 4E     BIT     1,(IY+$A4)          
0FDE: 28 24           JR      Z,$1004             ; 
0FE0: CD 50 17        CALL    $1750               ; 
0FE3: CD 65 19        CALL    $1965               ; 
0FE6: FD CB A4 46     BIT     0,(IY+$A4)          
0FEA: C2 D2 12        JP      NZ,$12D2            ; 
0FED: CD AA 11        CALL    $11AA               ; 
0FF0: C2 83 0B        JP      NZ,$0B83            ; 
0FF3: FD CB AE 76     BIT     6,(IY+$AE)          
0FF7: C2 9D 0A        JP      NZ,$0A9D            ; 
0FFA: 3A 20 40        LD      A,($4020)           ; 
0FFD: FE 2D           CP      $2D                 
0FFF: DA D2 12        JP      C,$12D2             ; 
1002: 18 2C           JR      $1030               ; 
1004: CD AA 11        CALL    $11AA               ; 
1007: C2 83 0B        JP      NZ,$0B83            ; 
100A: 3A 24 40        LD      A,($4024)           ; 
100D: FE 01           CP      $01                 
100F: C2 7B 12        JP      NZ,$127B            ; 
1012: FD CB AE 76     BIT     6,(IY+$AE)          
1016: C4 E3 16        CALL    NZ,$16E3            ; 
1019: DB 11           IN      A,($11)             ;
101B: CB 7F           BIT     7,A                 
101D: CA 37 11        JP      Z,$1137             ; 
1020: 3A 21 40        LD      A,($4021)           ; 
1023: B7              OR      A                   
1024: C2 94 11        JP      NZ,$1194            ; 
1027: 3A 8B 40        LD      A,($408B)           ; 
102A: FD BE 09        CP      (IY+$09)            
102D: D2 94 11        JP      NC,$1194            ; 
1030: FD 34 03        INC     (IY+$03)            ;
1033: 3A 83 40        LD      A,($4083)           ; 
1036: 3D              DEC     A                   
1037: 28 2A           JR      Z,$1063             ; 
1039: 3D              DEC     A                   
103A: 28 2A           JR      Z,$1066             ; 
103C: 3D              DEC     A                   
103D: 28 38           JR      Z,$1077             ; 
103F: 3D              DEC     A                   
1040: 28 46           JR      Z,$1088             ; 
1042: 3D              DEC     A                   
1043: 28 54           JR      Z,$1099             ; 
1045: 3D              DEC     A                   
1046: 28 6D           JR      Z,$10B5             ; 
1048: 3D              DEC     A                   
1049: CA D1 10        JP      Z,$10D1             ; 
104C: 3D              DEC     A                   
104D: CA D8 10        JP      Z,$10D8             ; 
1050: 3D              DEC     A                   
1051: CA DA 10        JP      Z,$10DA             ; 
1054: 3D              DEC     A                   
1055: CA DC 10        JP      Z,$10DC             ; 
1058: 3D              DEC     A                   
1059: CA 31 11        JP      Z,$1131             ; 
105C: 3D              DEC     A                   
105D: CA 34 11        JP      Z,$1134             ; 
1060: C3 9D 0A        JP      $0A9D               ; 
1063: C3 94 11        JP      $1194               ; 
1066: FD 36 04 01     LD      (IY+$04),$01        
106A: FD 36 A1 0F     LD      (IY+$A1),$0F        
106E: CD F1 16        CALL    $16F1               ; 
1071: CD F3 2A        CALL    $2AF3               ; 
1074: C3 94 11        JP      $1194               ; 
1077: CD 23 18        CALL    $1823               ; 
107A: FD 36 04 02     LD      (IY+$04),$02        
107E: FD 36 A1 06     LD      (IY+$A1),$06        
1082: CD F3 2A        CALL    $2AF3               ; 
1085: C3 94 11        JP      $1194               ; 
1088: FD 36 04 03     LD      (IY+$04),$03        
108C: FD 36 A1 08     LD      (IY+$A1),$08        
1090: CD F1 16        CALL    $16F1               ; 
1093: CD F3 2A        CALL    $2AF3               ; 
1096: C3 94 11        JP      $1194               ; 
1099: FD 36 A4 01     LD      (IY+$A4),$01        
109D: CD 23 18        CALL    $1823               ; 
10A0: FD 36 A1 0A     LD      (IY+$A1),$0A        
10A4: FD 36 BE 01     LD      (IY+$BE),$01        
10A8: CD 6C 12        CALL    $126C               ; 
10AB: FD 36 04 0F     LD      (IY+$04),$0F        
10AF: CD F3 2A        CALL    $2AF3               ; 
10B2: C3 94 11        JP      $1194               ; 
10B5: FD 36 A4 01     LD      (IY+$A4),$01        
10B9: CD 23 18        CALL    $1823               ; 
10BC: FD 36 A1 0A     LD      (IY+$A1),$0A        
10C0: FD 36 BE 01     LD      (IY+$BE),$01        
10C4: CD 6C 12        CALL    $126C               ; 
10C7: FD 36 04 10     LD      (IY+$04),$10        
10CB: CD F3 2A        CALL    $2AF3               ; 
10CE: C3 94 11        JP      $1194               ; 
10D1: FD 36 A1 1E     LD      (IY+$A1),$1E        
10D5: C3 83 0B        JP      $0B83               ; 
10D8: 18 BF           JR      $1099               ; 
10DA: 18 D9           JR      $10B5               ; 
10DC: 3A 2D 40        LD      A,($402D)           ; 
10DF: B7              OR      A                   
10E0: C2 9D 0A        JP      NZ,$0A9D            ; 
10E3: CD 23 18        CALL    $1823               ; 
10E6: FD 36 04 14     LD      (IY+$04),$14        
10EA: CD F3 2A        CALL    $2AF3               ; 
10ED: FD 36 A1 05     LD      (IY+$A1),$05        
10F1: 2A 27 40        LD      HL,($4027)          ; 
10F4: 4E              LD      C,(HL)              
10F5: 23              INC     HL                  
10F6: 46              LD      B,(HL)              
10F7: 11 D5 3F        LD      DE,$3FD5            
10FA: 69              LD      L,C                 
10FB: CD 27 11        CALL    $1127               ; 
10FE: 22 24 80        LD      ($8024),HL          ; 
1101: 68              LD      L,B                 
1102: CD 27 11        CALL    $1127               ; 
1105: 22 3A 80        LD      ($803A),HL          ; 
1108: 79              LD      A,C                 
1109: 81              ADD     A,C                 
110A: 6F              LD      L,A                 
110B: CD 27 11        CALL    $1127               ; 
110E: 22 54 80        LD      ($8054),HL          ; 
1111: 78              LD      A,B                 
1112: 80              ADD     A,B                 
1113: 6F              LD      L,A                 
1114: CD 27 11        CALL    $1127               ; 
1117: 22 6A 80        LD      ($806A),HL          ; 
111A: 78              LD      A,B                 
111B: FE 02           CP      $02                 
111D: 38 06           JR      C,$1125             ; 
111F: 21 00 B0        LD      HL,$B000            
1122: 22 54 80        LD      ($8054),HL          ; 
1125: 18 6D           JR      $1194               ; 
1127: CB 25           SLA     L                   
1129: 26 00           LD      H,$00               
112B: 19              ADD     HL,DE               
112C: 7E              LD      A,(HL)              
112D: 23              INC     HL                  
112E: 66              LD      H,(HL)              
112F: 6F              LD      L,A                 
1130: C9              RET                         
1131: C3 99 10        JP      $1099               ; 
1134: C3 B5 10        JP      $10B5               ; 
1137: 01 33 44        LD      BC,$4433            
113A: 11 71 44        LD      DE,$4471            
113D: 21 43 44        LD      HL,$4443            
1140: CD 46 16        CALL    $1646               ; 
1143: 01 35 44        LD      BC,$4435            
1146: 11 79 44        LD      DE,$4479            
1149: 21 5B 44        LD      HL,$445B            
114C: CD 46 16        CALL    $1646               ; 
114F: FD 36 04 15     LD      (IY+$04),$15        
1153: CD 23 18        CALL    $1823               ; 
1156: CD F3 2A        CALL    $2AF3               ; 
1159: FD CB AE B6     RES     6,(IY+$AE)          
115D: CD D5 17        CALL    $17D5               ; 
1160: CD F4 14        CALL    $14F4               ; 
1163: FD CB AE 76     BIT     6,(IY+$AE)          
1167: 20 CE           JR      NZ,$1137            ; 
1169: FD CB B0 6E     BIT     5,(IY+$B0)          
116D: 20 16           JR      NZ,$1185            ; 
116F: FD CB B0 76     BIT     6,(IY+$B0)          
1173: C2 4C 0A        JP      NZ,$0A4C            ; 
1176: FD CB B2 76     BIT     6,(IY+$B2)          
117A: 28 0F           JR      Z,$118B             ; 
117C: FD CB B1 7E     BIT     7,(IY+$B1)          
1180: C2 9D 0A        JP      NZ,$0A9D            ; 
1183: 18 D8           JR      $115D               ; 
1185: FD 36 AD 00     LD      (IY+$AD),$00        
1189: 18 AC           JR      $1137               ; 
118B: FD CB B3 7E     BIT     7,(IY+$B3)          
118F: C2 3B 0A        JP      NZ,$0A3B            ; 
1192: 18 E8           JR      $117C               ; 
1194: 3A 8B 40        LD      A,($408B)           ; 
1197: FD BE 09        CP      (IY+$09)            
119A: D4 6D 2B        CALL    NC,$2B6D            ; 
119D: CD D5 17        CALL    $17D5               ; 
11A0: FD CB AE 76     BIT     6,(IY+$AE)          
11A4: C2 9D 0A        JP      NZ,$0A9D            ; 
11A7: C3 D2 12        JP      $12D2               ; 
11AA: 3A 2D 40        LD      A,($402D)           ; 
11AD: B7              OR      A                   
11AE: CA 47 12        JP      Z,$1247             ; 
11B1: FD CB 97 76     BIT     6,(IY+$97)          
11B5: 28 1D           JR      Z,$11D4             ; 

11B7: F3              DI                          ; Interrupts off (atomic operation)
11B8: FD 46 F2        LD      B,(IY+$F2)          ;
11BB: CB 90           RES     2,B                 ; At least one credit: 1P1C start on
11BD: FE 02           CP      $02                 ; Two or more credits?
11BF: 38 0A           JR      C,$11CB             ; No ... skip
11C1: CB 98           RES     3,B                 ; 2 or more: 1P1C start
11C3: CB A0           RES     4,B                 ; 2 or more: 2P1C start
11C5: FE 04           CP      $04                 ; At least four credits?
11C7: 38 02           JR      C,$11CB             ; No ... skip
11C9: CB A8           RES     5,B                 ; 4 or more: 2P2C start
11CB: 78              LD      A,B                 ; Value to A for OUT
11CC: D3 13           OUT     ($13),A             ; Write the LED values
11CE: 32 72 40        LD      ($4072),A           ; Remember what we wrote
11D1: FB              EI                          ; Done ... interrupts back on

11D2: 18 03           JR      $11D7               ; 
11D4: CD 48 12        CALL    $1248               ; 
11D7: 3A 2D 40        LD      A,($402D)           ; 
11DA: FE 02           CP      $02                 
11DC: 38 52           JR      C,$1230             ; 
11DE: FE 04           CP      $04                 
11E0: 38 14           JR      C,$11F6             ; 
11E2: FD CB B3 5E     BIT     3,(IY+$B3)          
11E6: 28 0E           JR      Z,$11F6             ; 
11E8: FD 36 C1 00     LD      (IY+$C1),$00        
11EC: FD 36 C0 04     LD      (IY+$C0),$04        
11F0: FD CB C1 EE     SET     5,(IY+$C1)          
11F4: 18 0E           JR      $1204               ; 
11F6: FD CB B3 56     BIT     2,(IY+$B3)          
11FA: 28 20           JR      Z,$121C             ; 
11FC: FD 36 C1 00     LD      (IY+$C1),$00        
1200: FD 36 C0 02     LD      (IY+$C0),$02        
1204: FD 36 BF 02     LD      (IY+$BF),$02        
1208: FD 36 BE 02     LD      (IY+$BE),$02        
120C: FD CB C1 F6     SET     6,(IY+$C1)          
1210: DB 17           IN      A,($17)             ;
1212: CB 7F           BIT     7,A                 
1214: 28 28           JR      Z,$123E             ; 
1216: FD CB C1 D6     SET     2,(IY+$C1)          
121A: 18 22           JR      $123E               ; 
121C: FD CB B3 7E     BIT     7,(IY+$B3)          
1220: 28 0E           JR      Z,$1230             ; 
1222: FD 36 C1 00     LD      (IY+$C1),$00        
1226: FD CB C1 EE     SET     5,(IY+$C1)          
122A: FD 36 C0 02     LD      (IY+$C0),$02        
122E: 18 0E           JR      $123E               ; 
1230: FD CB B3 76     BIT     6,(IY+$B3)          
1234: 28 11           JR      Z,$1247             ; 
1236: FD 36 C1 00     LD      (IY+$C1),$00        
123A: FD 36 C0 01     LD      (IY+$C0),$01        
123E: CD 48 12        CALL    $1248               ; 
1241: FD 36 03 01     LD      (IY+$03),$01        
1245: F6 FF           OR      $FF                 
1247: C9              RET                         
1248: F3              DI                          
1249: 3A 72 40        LD      A,($4072)           ; 
124C: F6 3C           OR      $3C                 
124E: D3 13           OUT     ($13),A             ;
1250: 32 72 40        LD      ($4072),A           ; 
1253: FB              EI                          
1254: C9              RET                         
1255: FD CB C1 56     BIT     2,(IY+$C1)          
1259: 28 1C           JR      Z,$1277             ; 
125B: F3              DI                          
125C: 3A 3E 40        LD      A,($403E)           ; 
125F: FD AE EE        XOR     (IY+$EE)            
1262: CB 47           BIT     0,A                 
1264: 28 07           JR      Z,$126D             ; 
1266: FD CB F2 B6     RES     6,(IY+$F2)          
126A: 18 05           JR      $1271               ; 
126C: F3              DI                          
126D: FD CB F2 F6     SET     6,(IY+$F2)          
1271: 3A 72 40        LD      A,($4072)           ; 
1274: D3 13           OUT     ($13),A             ;
1276: FB              EI                          
1277: C9              RET                         
1278: C3 83 0B        JP      $0B83               ; 
127B: CD 0D 18        CALL    $180D               ; 
127E: CD 35 2A        CALL    $2A35               ; 
1281: CD AA 11        CALL    $11AA               ; 
1284: C2 83 0B        JP      NZ,$0B83            ; 
1287: 3A 24 40        LD      A,($4024)           ; 
128A: FE 04           CP      $04                 
128C: 28 44           JR      Z,$12D2             ; 
128E: FD 36 03 0C     LD      (IY+$03),$0C        
1292: 01 2A 00        LD      BC,$002A            
1295: 21 A9 43        LD      HL,$43A9            
1298: 11 D3 43        LD      DE,$43D3            
129B: FD CB C1 6E     BIT     5,(IY+$C1)          
129F: 28 03           JR      Z,$12A4             ; 
12A1: 11 FD 43        LD      DE,$43FD            
12A4: ED B0           LDIR                        
12A6: FD CB C1 E6     SET     4,(IY+$C1)          
12AA: FD 35 BF        DEC     (IY+$BF)            
12AD: 28 19           JR      Z,$12C8             ; 
12AF: FD CB C1 5E     BIT     3,(IY+$C1)          
12B3: 20 09           JR      NZ,$12BE            ; 
12B5: FD 36 BE 02     LD      (IY+$BE),$02        
12B9: 21 53 40        LD      HL,$4053            
12BC: 18 07           JR      $12C5               ; 
12BE: FD 36 BE 01     LD      (IY+$BE),$01        
12C2: 21 46 40        LD      HL,$4046            
12C5: C3 78 14        JP      $1478               ; 
12C8: FD CB C1 6E     BIT     5,(IY+$C1)          
12CC: CA 99 10        JP      Z,$1099             ; 
12CF: C3 B5 10        JP      $10B5               ; 
12D2: CD 37 17        CALL    $1737               ; 
12D5: EE 3F           XOR     $3F                 
12D7: E6 3F           AND     $3F                 
12D9: 5F              LD      E,A                 
12DA: 16 00           LD      D,$00               
12DC: 21 61 30        LD      HL,$3061            
12DF: 19              ADD     HL,DE               
12E0: 7E              LD      A,(HL)              
12E1: EE 3F           XOR     $3F                 
12E3: 47              LD      B,A                 
12E4: 3A 24 40        LD      A,($4024)           ; 
12E7: FE 03           CP      $03                 
12E9: 38 0E           JR      C,$12F9             ; 
12EB: FE 04           CP      $04                 
12ED: 28 06           JR      Z,$12F5             ; 
12EF: FD CB 33 6E     BIT     5,(IY+$33)          
12F3: 20 04           JR      NZ,$12F9            ; 
12F5: 78              LD      A,B                 
12F6: 32 BC 40        LD      ($40BC),A           ; 
12F9: FD CB AF 6E     BIT     5,(IY+$AF)          
12FD: 20 0A           JR      NZ,$1309            ; 
12FF: FD CB 32 6E     BIT     5,(IY+$32)          
1303: 28 04           JR      Z,$1309             ; 
1305: FD CB 32 C6     SET     0,(IY+$32)          
1309: FD CB B0 76     BIT     6,(IY+$B0)          
130D: 28 14           JR      Z,$1323             ; 
130F: 3A 70 40        LD      A,($4070)           ; 
1312: B7              OR      A                   
1313: 20 0E           JR      NZ,$1323            ; 
1315: FD CB 33 6E     BIT     5,(IY+$33)          
1319: 20 08           JR      NZ,$1323            ; 
131B: FD CB 32 D6     SET     2,(IY+$32)          
131F: FD 36 F0 02     LD      (IY+$F0),$02        
1323: FD CB 32 7E     BIT     7,(IY+$32)          
1327: 28 0D           JR      Z,$1336             ; 
1329: 3A 77 40        LD      A,($4077)           ; 
132C: B7              OR      A                   
132D: C2 94 14        JP      NZ,$1494            ; 
1330: FD CB 33 6E     BIT     5,(IY+$33)          
1334: 28 14           JR      Z,$134A             ; 
1336: FD CB EB 6E     BIT     5,(IY+$EB)          
133A: 20 5A           JR      NZ,$1396            ; 
133C: FD CB EB EE     SET     5,(IY+$EB)          
1340: FD 36 A1 0A     LD      (IY+$A1),$0A        
1344: FD 36 A3 04     LD      (IY+$A3),$04        
1348: 18 4C           JR      $1396               ; 
134A: FD CB EB 6E     BIT     5,(IY+$EB)          
134E: 20 46           JR      NZ,$1396            ; 
1350: FD CB EB EE     SET     5,(IY+$EB)          
1354: DD 21 0E 00     LD      IX,$000E            
1358: DD CB 00 BE     RES     7,(IX+$00)          
135C: DD 21 0F 00     LD      IX,$000F            
1360: DD CB 00 BE     RES     7,(IX+$00)          
1364: DD 21 10 00     LD      IX,$0010            
1368: DD CB 00 BE     RES     7,(IX+$00)          
136C: DD 21 11 00     LD      IX,$0011            
1370: DD CB 00 BE     RES     7,(IX+$00)          
1374: FD 36 E9 00     LD      (IY+$E9),$00        
1378: 3E 00           LD      A,$00               
137A: CD 04 2E        CALL    $2E04               ; 
137D: FD 36 A1 00     LD      (IY+$A1),$00        
1381: 3E 04           LD      A,$04               
1383: CD 04 2E        CALL    $2E04               ; 
1386: FD 36 A1 05     LD      (IY+$A1),$05        
138A: FD 36 A3 05     LD      (IY+$A3),$05        
138E: FD 36 97 00     LD      (IY+$97),$00        
1392: FD 36 98 00     LD      (IY+$98),$00        
1396: 3A 23 40        LD      A,($4023)           ; 
1399: FE 03           CP      $03                 
139B: D2 94 14        JP      NC,$1494            ; 
139E: FD CB 33 6E     BIT     5,(IY+$33)          
13A2: 20 07           JR      NZ,$13AB            ; 
13A4: FD CB 32 7E     BIT     7,(IY+$32)          
13A8: C2 98 0C        JP      NZ,$0C98            ; 
13AB: FD CB 32 7E     BIT     7,(IY+$32)          
13AF: C2 94 14        JP      NZ,$1494            ; 
13B2: 3A 66 40        LD      A,($4066)           ; 
13B5: FE 01           CP      $01                 
13B7: 20 71           JR      NZ,$142A            ; 
13B9: FD CB AE 7E     BIT     7,(IY+$AE)          
13BD: 28 0D           JR      Z,$13CC             ; 
13BF: FD CB EA 4E     BIT     1,(IY+$EA)          
13C3: 20 07           JR      NZ,$13CC            ; 
13C5: FD CB EA CE     SET     1,(IY+$EA)          
13C9: CD 40 15        CALL    $1540               ; 
13CC: FD CB C1 76     BIT     6,(IY+$C1)          
13D0: 28 07           JR      Z,$13D9             ; 
13D2: 3A 3E 40        LD      A,($403E)           ; 
13D5: FE 02           CP      $02                 
13D7: 20 51           JR      NZ,$142A            ; 
13D9: CD AA 11        CALL    $11AA               ; 
13DC: C2 83 0B        JP      NZ,$0B83            ; 
13DF: FD CB C1 4E     BIT     1,(IY+$C1)          
13E3: 20 32           JR      NZ,$1417            ; 
13E5: FD CB C1 CE     SET     1,(IY+$C1)          
13E9: 06 20           LD      B,$20               
13EB: CD B2 29        CALL    $29B2               ; 
13EE: 10 FB           DJNZ    $13EB               ; 
13F0: FD 36 A2 05     LD      (IY+$A2),$05        
13F4: 3E 00           LD      A,$00               
13F6: CD 04 2E        CALL    $2E04               ; 
13F9: 01 1A 00        LD      BC,$001A            
13FC: 11 36 83        LD      DE,$8336            
13FF: 21 00 D0        LD      HL,$D000            
1402: 22 34 83        LD      ($8334),HL          ; 
1405: 21 34 83        LD      HL,$8334            
1408: ED B0           LDIR                        
140A: 2A F3 3E        LD      HL,($3EF3)          ; 
140D: 22 42 82        LD      ($8242),HL          ; 
1410: FD 36 04 0E     LD      (IY+$04),$0E        
1414: CD F3 2A        CALL    $2AF3               ; 
1417: 3A 8B 40        LD      A,($408B)           ; 
141A: FD BE 09        CP      (IY+$09)            
141D: 38 05           JR      C,$1424             ; 
141F: CD 6D 2B        CALL    $2B6D               ; 
1422: 18 70           JR      $1494               ; 
1424: 3A 22 40        LD      A,($4022)           ; 
1427: B7              OR      A                   
1428: 20 6A           JR      NZ,$1494            ; 
142A: 3E 00           LD      A,$00               
142C: CD 04 2E        CALL    $2E04               ; 
142F: FD 35 E6        DEC     (IY+$E6)            
1432: C2 98 0C        JP      NZ,$0C98            ; 
1435: FD CB EB B6     RES     6,(IY+$EB)          
1439: FD CB AE 7E     BIT     7,(IY+$AE)          
143D: CA 9D 0A        JP      Z,$0A9D             ; 
1440: FD CB C1 76     BIT     6,(IY+$C1)          
1444: 28 35           JR      Z,$147B             ; 
1446: 3A 3E 40        LD      A,($403E)           ; 
1449: FE 02           CP      $02                 
144B: C2 98 0C        JP      NZ,$0C98            ; 
144E: 21 53 40        LD      HL,$4053            
1451: CD 8E 2C        CALL    $2C8E               ; 
1454: 06 04           LD      B,$04               
1456: 11 4B 40        LD      DE,$404B            
1459: 21 58 40        LD      HL,$4058            
145C: AF              XOR     A                   
145D: 1A              LD      A,(DE)              
145E: 9E              SBC     (HL)                
145F: 27              DAA                         
1460: 13              INC     DE                  
1461: 23              INC     HL                  
1462: 10 F9           DJNZ    $145D               ; 
1464: FD 36 BE 01     LD      (IY+$BE),$01        
1468: 21 46 40        LD      HL,$4046            
146B: 30 0B           JR      NC,$1478            ; 
146D: FD 36 BE 02     LD      (IY+$BE),$02        
1471: 21 53 40        LD      HL,$4053            
1474: FD CB C1 DE     SET     3,(IY+$C1)          
1478: CD BD 2C        CALL    $2CBD               ; 
147B: CD CD 29        CALL    $29CD               ; 
147E: 3A 24 40        LD      A,($4024)           ; 
1481: FE 04           CP      $04                 
1483: CA E6 0E        JP      Z,$0EE6             ; 
1486: FD 36 03 09     LD      (IY+$03),$09        
148A: FD CB C1 66     BIT     4,(IY+$C1)          
148E: C2 C8 12        JP      NZ,$12C8            ; 
1491: C3 9D 0A        JP      $0A9D               ; 
1494: FD CB 33 6E     BIT     5,(IY+$33)          
1498: 20 18           JR      NZ,$14B2            ; 
149A: FD CB B0 6E     BIT     5,(IY+$B0)          
149E: 28 07           JR      Z,$14A7             ; 
14A0: 3E 09           LD      A,$09               
14A2: CD 04 2E        CALL    $2E04               ; 
14A5: 18 0B           JR      $14B2               ; 
14A7: FD CB B1 6E     BIT     5,(IY+$B1)          
14AB: 28 05           JR      Z,$14B2             ; 
14AD: 3E 0A           LD      A,$0A               
14AF: CD 04 2E        CALL    $2E04               ; 
14B2: FD CB EB 66     BIT     4,(IY+$EB)          
14B6: 20 39           JR      NZ,$14F1            ; 
14B8: 3A B9 40        LD      A,($40B9)           ; 
14BB: FE D0           CP      $D0                 
14BD: 30 32           JR      NC,$14F1            ; 
14BF: FE 30           CP      $30                 
14C1: 38 2E           JR      C,$14F1             ; 
14C3: FD CB EB E6     SET     4,(IY+$EB)          
14C7: 3A BB 40        LD      A,($40BB)           ; 
14CA: FE 80           CP      $80                 
14CC: 38 23           JR      C,$14F1             ; 
14CE: 3A 67 40        LD      A,($4067)           ; 
14D1: CB 2F           SRA     A                   
14D3: 47              LD      B,A                 
14D4: C6 01           ADD     A,$01               
14D6: CB 27           SLA     A                   
14D8: 4F              LD      C,A                 
14D9: CB 27           SLA     A                   
14DB: 81              ADD     A,C                 
14DC: 4F              LD      C,A                 
14DD: 21 90 2E        LD      HL,$2E90            
14E0: 59              LD      E,C                 
14E1: 16 00           LD      D,$00               
14E3: 19              ADD     HL,DE               
14E4: 5E              LD      E,(HL)              
14E5: 23              INC     HL                  
14E6: 56              LD      D,(HL)              
14E7: 1A              LD      A,(DE)              
14E8: EE 02           XOR     $02                 
14EA: 12              LD      (DE),A              
14EB: 3E 06           LD      A,$06               
14ED: 81              ADD     A,C                 
14EE: 4F              LD      C,A                 
14EF: 10 EC           DJNZ    $14DD               ; 
14F1: C3 39 0F        JP      $0F39               ; 
14F4: FD 56 AF        LD      D,(IY+$AF)          
14F7: CD 11 17        CALL    $1711               ; 
14FA: 32 2F 40        LD      ($402F),A           ; 
14FD: 5F              LD      E,A                 
14FE: A2              AND     D                   
14FF: AA              XOR     D                   
1500: 32 30 40        LD      ($4030),A           ; 
1503: 7B              LD      A,E                 
1504: B2              OR      D                   
1505: AA              XOR     D                   
1506: 32 31 40        LD      ($4031),A           ; 
1509: FD 56 B2        LD      D,(IY+$B2)          
150C: DB 12           IN      A,($12)             ;
150E: 32 32 40        LD      ($4032),A           ; 
1511: 5F              LD      E,A                 
1512: A2              AND     D                   
1513: AA              XOR     D                   
1514: 32 33 40        LD      ($4033),A           ; 
1517: C9              RET                         
1518: E5              PUSH    HL                  
1519: 21 F7 3F        LD      HL,$3FF7            
151C: CD 21 15        CALL    $1521               ; 
151F: E1              POP     HL                  
1520: C9              RET                         
1521: F5              PUSH    AF                  
1522: C5              PUSH    BC                  
1523: E5              PUSH    HL                  
1524: B7              OR      A                   
1525: 07              RLCA                        
1526: 07              RLCA                        
1527: 4F              LD      C,A                 
1528: 06 00           LD      B,$00               
152A: 7E              LD      A,(HL)              
152B: 21 27 44        LD      HL,$4427            
152E: 09              ADD     HL,BC               
152F: 06 03           LD      B,$03               
1531: 86              ADD     A,(HL)              
1532: 27              DAA                         
1533: 77              LD      (HL),A              
1534: 23              INC     HL                  
1535: 7E              LD      A,(HL)              
1536: CE 00           ADC     A,$00               
1538: 27              DAA                         
1539: 77              LD      (HL),A              
153A: 10 F8           DJNZ    $1534               ; 
153C: E1              POP     HL                  
153D: C1              POP     BC                  
153E: F1              POP     AF                  
153F: C9              RET                         
1540: FD 36 12 00     LD      (IY+$12),$00        
1544: FD CB C1 6E     BIT     5,(IY+$C1)          
1548: 20 07           JR      NZ,$1551            ; 
154A: 3E 04           LD      A,$04               
154C: 11 33 44        LD      DE,$4433            
154F: 18 09           JR      $155A               ; 
1551: 3E 0A           LD      A,$0A               
1553: 11 35 44        LD      DE,$4435            
1556: FD CB 12 FE     SET     7,(IY+$12)          
155A: ED 53 67 44     LD      ($4467),DE          ; 
155E: FD CB EA 6E     BIT     5,(IY+$EA)          
1562: C4 18 15        CALL    NZ,$1518            ; 
1565: 3C              INC     A                   
1566: FD CB EA 66     BIT     4,(IY+$EA)          
156A: C4 18 15        CALL    NZ,$1518            ; 
156D: 3C              INC     A                   
156E: FD CB EA 5E     BIT     3,(IY+$EA)          
1572: C4 18 15        CALL    NZ,$1518            ; 
1575: 3C              INC     A                   
1576: 21 36 40        LD      HL,$4036            
1579: CD 8C 15        CALL    $158C               ; 
157C: 3C              INC     A                   
157D: FD CB 12 F6     SET     6,(IY+$12)          
1581: 21 3A 40        LD      HL,$403A            
1584: CD 8C 15        CALL    $158C               ; 
1587: 3C              INC     A                   
1588: CD 14 16        CALL    $1614               ; 
158B: C9              RET                         
158C: F5              PUSH    AF                  
158D: C5              PUSH    BC                  
158E: D5              PUSH    DE                  
158F: E5              PUSH    HL                  
1590: CD 39 16        CALL    $1639               ; 
1593: E5              PUSH    HL                  
1594: 13              INC     DE                  
1595: 1A              LD      A,(DE)              
1596: B7              OR      A                   
1597: 28 3C           JR      Z,$15D5             ; 
1599: 23              INC     HL                  
159A: 11 69 44        LD      DE,$4469            
159D: 01 03 00        LD      BC,$0003            
15A0: ED B0           LDIR                        
15A2: AF              XOR     A                   
15A3: 12              LD      (DE),A              
15A4: 06 04           LD      B,$04               
15A6: D1              POP     DE                  
15A7: D5              PUSH    DE                  
15A8: 21 69 44        LD      HL,$4469            
15AB: 1A              LD      A,(DE)              
15AC: 9E              SBC     (HL)                
15AD: 27              DAA                         
15AE: 12              LD      (DE),A              
15AF: 13              INC     DE                  
15B0: 23              INC     HL                  
15B1: 10 F8           DJNZ    $15AB               ; 
15B3: AF              XOR     A                   
15B4: 06 03           LD      B,$03               
15B6: D1              POP     DE                  
15B7: E1              POP     HL                  
15B8: E5              PUSH    HL                  
15B9: FD CB 12 76     BIT     6,(IY+$12)          
15BD: 20 01           JR      NZ,$15C0            ; 
15BF: 23              INC     HL                  
15C0: 1A              LD      A,(DE)              
15C1: 8E              ADC     A,(HL)              
15C2: 27              DAA                         
15C3: 12              LD      (DE),A              
15C4: 13              INC     DE                  
15C5: 23              INC     HL                  
15C6: 10 F8           DJNZ    $15C0               ; 
15C8: FD CB 12 76     BIT     6,(IY+$12)          
15CC: 20 41           JR      NZ,$160F            ; 
15CE: 1A              LD      A,(DE)              
15CF: CE 00           ADC     A,$00               
15D1: 27              DAA                         
15D2: 12              LD      (DE),A              
15D3: 18 3A           JR      $160F               ; 
15D5: 06 04           LD      B,$04               
15D7: E1              POP     HL                  
15D8: D1              POP     DE                  
15D9: D5              PUSH    DE                  
15DA: E5              PUSH    HL                  
15DB: AF              XOR     A                   
15DC: 1A              LD      A,(DE)              
15DD: 8E              ADC     A,(HL)              
15DE: 27              DAA                         
15DF: 77              LD      (HL),A              
15E0: 13              INC     DE                  
15E1: 23              INC     HL                  
15E2: 10 F8           DJNZ    $15DC               ; 
15E4: 2A 67 44        LD      HL,($4467)          ; 
15E7: 7E              LD      A,(HL)              
15E8: C6 01           ADD     A,$01               
15EA: 27              DAA                         
15EB: 38 0A           JR      C,$15F7             ; 
15ED: FD CB 12 76     BIT     6,(IY+$12)          
15F1: 28 01           JR      Z,$15F4             ; 
15F3: 77              LD      (HL),A              
15F4: E1              POP     HL                  
15F5: 18 18           JR      $160F               ; 
15F7: FD CB 12 76     BIT     6,(IY+$12)          
15FB: 20 0E           JR      NZ,$160B            ; 
15FD: E1              POP     HL                  
15FE: 54              LD      D,H                 
15FF: 5D              LD      E,L                 
1600: 23              INC     HL                  
1601: 01 03 00        LD      BC,$0003            
1604: ED B0           LDIR                        
1606: 3E 00           LD      A,$00               
1608: 12              LD      (DE),A              
1609: 18 04           JR      $160F               ; 
160B: 77              LD      (HL),A              
160C: 23              INC     HL                  
160D: 34              INC     (HL)                
160E: E1              POP     HL                  
160F: E1              POP     HL                  
1610: D1              POP     DE                  
1611: C1              POP     BC                  
1612: F1              POP     AF                  
1613: C9              RET                         
1614: F5              PUSH    AF                  
1615: C5              PUSH    BC                  
1616: D5              PUSH    DE                  
1617: E5              PUSH    HL                  
1618: CD 39 16        CALL    $1639               ; 
161B: E5              PUSH    HL                  
161C: AF              XOR     A                   
161D: 06 04           LD      B,$04               
161F: 11 3A 40        LD      DE,$403A            
1622: 1A              LD      A,(DE)              
1623: 9E              SBC     (HL)                
1624: 27              DAA                         
1625: 23              INC     HL                  
1626: 13              INC     DE                  
1627: 10 F9           DJNZ    $1622               ; 
1629: D1              POP     DE                  
162A: 38 08           JR      C,$1634             ; 
162C: 01 04 00        LD      BC,$0004            
162F: 21 3A 40        LD      HL,$403A            
1632: ED B0           LDIR                        
1634: E1              POP     HL                  
1635: D1              POP     DE                  
1636: C1              POP     BC                  
1637: F1              POP     AF                  
1638: C9              RET                         
1639: C5              PUSH    BC                  
163A: B7              OR      A                   
163B: 07              RLCA                        
163C: 07              RLCA                        
163D: 4F              LD      C,A                 
163E: 06 00           LD      B,$00               
1640: 21 27 44        LD      HL,$4427            
1643: 09              ADD     HL,BC               
1644: C1              POP     BC                  
1645: C9              RET                         
1646: C5              PUSH    BC                  
1647: D5              PUSH    DE                  
1648: E5              PUSH    HL                  
1649: 03              INC     BC                  
164A: 0A              LD      A,(BC)              
164B: B7              OR      A                   
164C: 28 07           JR      Z,$1655             ; 
164E: 01 08 00        LD      BC,$0008            
1651: ED B0           LDIR                        
1653: 18 1B           JR      $1670               ; 
1655: 0B              DEC     BC                  
1656: 0A              LD      A,(BC)              
1657: 32 93 40        LD      ($4093),A           ; 
165A: CD 74 16        CALL    $1674               ; 
165D: CD 74 16        CALL    $1674               ; 
1660: E1              POP     HL                  
1661: D1              POP     DE                  
1662: D5              PUSH    DE                  
1663: E5              PUSH    HL                  
1664: 21 06 00        LD      HL,$0006            
1667: 19              ADD     HL,DE               
1668: 54              LD      D,H                 
1669: 5D              LD      E,L                 
166A: 13              INC     DE                  
166B: 01 03 00        LD      BC,$0003            
166E: ED B8           LDDR                        
1670: E1              POP     HL                  
1671: D1              POP     DE                  
1672: C1              POP     BC                  
1673: C9              RET                         
1674: C5              PUSH    BC                  
1675: D5              PUSH    DE                  
1676: 01 04 00        LD      BC,$0004            
1679: 11 69 44        LD      DE,$4469            
167C: ED B0           LDIR                        
167E: E5              PUSH    HL                  
167F: 01 03 00        LD      BC,$0003            
1682: 11 6E 44        LD      DE,$446E            
1685: 21 6D 44        LD      HL,$446D            
1688: 36 00           LD      (HL),$00            
168A: ED B0           LDIR                        
168C: 3A 93 40        LD      A,($4093)           ; 
168F: B7              OR      A                   
1690: 28 33           JR      Z,$16C5             ; 
1692: DB 09           IN      A,($09)             ;
1694: 21 69 44        LD      HL,$4469            
1697: 7E              LD      A,(HL)              
1698: FD 96 13        SUB     (IY+$13)            
169B: 27              DAA                         
169C: 77              LD      (HL),A              
169D: 30 0E           JR      NC,$16AD            ; 
169F: 06 03           LD      B,$03               
16A1: 23              INC     HL                  
16A2: 7E              LD      A,(HL)              
16A3: DE 00           SBC     A,$00               
16A5: 27              DAA                         
16A6: 77              LD      (HL),A              
16A7: 30 04           JR      NC,$16AD            ; 
16A9: 10 F6           DJNZ    $16A1               ; 
16AB: 18 18           JR      $16C5               ; 
16AD: 21 6D 44        LD      HL,$446D            
16B0: 7E              LD      A,(HL)              
16B1: C6 01           ADD     A,$01               
16B3: 27              DAA                         
16B4: 77              LD      (HL),A              
16B5: 30 DB           JR      NC,$1692            ; 
16B7: 06 03           LD      B,$03               
16B9: 23              INC     HL                  
16BA: 7E              LD      A,(HL)              
16BB: CE 00           ADC     A,$00               
16BD: 27              DAA                         
16BE: 77              LD      (HL),A              
16BF: 30 D1           JR      NC,$1692            ; 
16C1: 10 F6           DJNZ    $16B9               ; 
16C3: 18 CD           JR      $1692               ; 
16C5: 01 04 00        LD      BC,$0004            
16C8: E1              POP     HL                  
16C9: D1              POP     DE                  
16CA: D5              PUSH    DE                  
16CB: E5              PUSH    HL                  
16CC: 21 6D 44        LD      HL,$446D            
16CF: ED B0           LDIR                        
16D1: E1              POP     HL                  
16D2: C1              POP     BC                  
16D3: C1              POP     BC                  
16D4: C9              RET                         
16D5: C5              PUSH    BC                  
16D6: AF              XOR     A                   
16D7: 06 04           LD      B,$04               
16D9: 1A              LD      A,(DE)              
16DA: 8E              ADC     A,(HL)              
16DB: 27              DAA                         
16DC: 12              LD      (DE),A              
16DD: 23              INC     HL                  
16DE: 13              INC     DE                  
16DF: 10 F8           DJNZ    $16D9               ; 
16E1: C1              POP     BC                  
16E2: C9              RET                         
16E3: 3A 2D 40        LD      A,($402D)           ; 
16E6: 32 56 5C        LD      ($5C56),A           ; 
16E9: 0F              RRCA                        
16EA: 0F              RRCA                        
16EB: 0F              RRCA                        
16EC: 0F              RRCA                        
16ED: 32 57 5C        LD      ($5C57),A           ; 
16F0: C9              RET                         
16F1: CD 23 18        CALL    $1823               ; 
16F4: 2A D9 33        LD      HL,($33D9)          ; 
16F7: 22 00 80        LD      ($8000),HL          ; 
16FA: 01 00 03        LD      BC,$0300            
16FD: 11 02 80        LD      DE,$8002            
1700: 21 00 80        LD      HL,$8000            
1703: ED B0           LDIR                        
1705: 01 1A 00        LD      BC,$001A            
1708: 11 00 83        LD      DE,$8300            
170B: 21 DB 33        LD      HL,$33DB            
170E: ED B0           LDIR                        
1710: C9              RET                         
1711: FD CB C1 56     BIT     2,(IY+$C1)          
1715: 20 04           JR      NZ,$171B            ; 
1717: DB 11           IN      A,($11)             ;
1719: 18 1B           JR      $1736               ; 
171B: 3A 3E 40        LD      A,($403E)           ; 
171E: FD AE EE        XOR     (IY+$EE)            
1721: CB 47           BIT     0,A                 
1723: 28 F2           JR      Z,$1717             ; 
1725: DB 12           IN      A,($12)             ;
1727: E6 03           AND     $03                 
1729: 0F              RRCA                        
172A: 0F              RRCA                        
172B: 0F              RRCA                        
172C: 32 34 40        LD      ($4034),A           ; 
172F: DB 11           IN      A,($11)             ;
1731: E6 9F           AND     $9F                 
1733: FD B6 B4        OR      (IY+$B4)            
1736: C9              RET                         
1737: FD CB C1 56     BIT     2,(IY+$C1)          
173B: 20 06           JR      NZ,$1743            ; 
173D: DB 15           IN      A,($15)             ;
173F: 0F              RRCA                        
1740: 0F              RRCA                        
1741: 18 0C           JR      $174F               ; 
1743: 3A 3E 40        LD      A,($403E)           ; 
1746: FD AE EE        XOR     (IY+$EE)            
1749: CB 47           BIT     0,A                 
174B: 28 F0           JR      Z,$173D             ; 
174D: DB 16           IN      A,($16)             ;
174F: C9              RET                         
1750: DB 09           IN      A,($09)             ;
1752: DB 0B           IN      A,($0B)             ;
1754: CB 7F           BIT     7,A                 
1756: 20 7C           JR      NZ,$17D4            ; 
1758: 01 B0 01        LD      BC,$01B0            
175B: 11 00 80        LD      DE,$8000            
175E: 21 81 44        LD      HL,$4481            
1761: ED B0           LDIR                        
1763: 21 00 D0        LD      HL,$D000            
1766: FD CB AF 6E     BIT     5,(IY+$AF)          
176A: 20 0C           JR      NZ,$1778            ; 
176C: FD 34 F1        INC     (IY+$F1)            ;
176F: FD CB F1 46     BIT     0,(IY+$F1)          
1773: 28 03           JR      Z,$1778             ; 
1775: 2A 11 46        LD      HL,($4611)          ; 
1778: 22 8C 81        LD      ($818C),HL          ; 
177B: FD CB AE 76     BIT     6,(IY+$AE)          
177F: 28 19           JR      Z,$179A             ; 
1781: 3A 24 40        LD      A,($4024)           ; 
1784: FE 03           CP      $03                 
1786: 20 12           JR      NZ,$179A            ; 
1788: FD CB AE B6     RES     6,(IY+$AE)          
178C: 06 01           LD      B,$01               
178E: 11 2D 40        LD      DE,$402D            
1791: 21 2B 46        LD      HL,$462B            
1794: CD 0E 24        CALL    $240E               ; 
1797: CD E3 16        CALL    $16E3               ; 
179A: FD CB C1 76     BIT     6,(IY+$C1)          
179E: 28 17           JR      Z,$17B7             ; 
17A0: FD CB 97 6E     BIT     5,(IY+$97)          
17A4: 20 05           JR      NZ,$17AB            ; 
17A6: 21 00 F0        LD      HL,$F000            
17A9: 18 09           JR      $17B4               ; 
17AB: 21 C2 0D        LD      HL,$0DC2            
17AE: 7C              LD      A,H                 
17AF: E6 0F           AND     $0F                 
17B1: F6 C0           OR      $C0                 
17B3: 67              LD      H,A                 
17B4: 22 A6 81        LD      ($81A6),HL          ; 
17B7: 3A 17 40        LD      A,($4017)           ; 
17BA: FD 96 9A        SUB     (IY+$9A)            
17BD: 4F              LD      C,A                 
17BE: FE 0A           CP      $0A                 
17C0: 38 03           JR      C,$17C5             ; 
17C2: 00              NOP                         
17C3: 00              NOP                         
17C4: 00              NOP                         
17C5: 3A 17 40        LD      A,($4017)           ; 
17C8: 32 1A 40        LD      ($401A),A           ; 
17CB: FD CB 1A 7E     BIT     7,(IY+$1A)          
17CF: C4 68 18        CALL    NZ,$1868            ; 
17D2: DB 08           IN      A,($08)             ;
17D4: C9              RET                         
17D5: DB 09           IN      A,($09)             ;
17D7: DB 0B           IN      A,($0B)             ;
17D9: CB 7F           BIT     7,A                 
17DB: 20 2F           JR      NZ,$180C            ; 
17DD: 3A 24 40        LD      A,($4024)           ; 
17E0: FE 01           CP      $01                 
17E2: 20 26           JR      NZ,$180A            ; 
17E4: 3A 84 40        LD      A,($4084)           ; 
17E7: FE 02           CP      $02                 
17E9: 20 1F           JR      NZ,$180A            ; 
17EB: 3A 17 40        LD      A,($4017)           ; 
17EE: E6 0C           AND     $0C                 
17F0: 0F              RRCA                        
17F1: 5F              LD      E,A                 
17F2: 16 00           LD      D,$00               
17F4: 21 4D 3F        LD      HL,$3F4D            
17F7: 19              ADD     HL,DE               
17F8: 4E              LD      C,(HL)              
17F9: 23              INC     HL                  
17FA: 46              LD      B,(HL)              
17FB: ED 43 80 80     LD      ($8080),BC          ; 
17FF: 21 55 3F        LD      HL,$3F55            
1802: 19              ADD     HL,DE               
1803: 4E              LD      C,(HL)              
1804: 23              INC     HL                  
1805: 46              LD      B,(HL)              
1806: ED 43 A8 80     LD      ($80A8),BC          ; 
180A: DB 08           IN      A,($08)             ;
180C: C9              RET                         
180D: DB 09           IN      A,($09)             ;
180F: DB 0B           IN      A,($0B)             ;
1811: CB 7F           BIT     7,A                 
1813: 20 0D           JR      NZ,$1822            ; 
1815: 01 7A 00        LD      BC,$007A            
1818: 11 00 80        LD      DE,$8000            
181B: 21 81 44        LD      HL,$4481            
181E: ED B0           LDIR                        
1820: DB 08           IN      A,($08)             ;
1822: C9              RET                         
1823: DB 09           IN      A,($09)             ;
1825: CD 54 18        CALL    $1854               ; 
1828: 21 00 B0        LD      HL,$B000            
182B: 22 81 44        LD      ($4481),HL          ; 
182E: 22 00 80        LD      ($8000),HL          ; 
1831: 01 00 06        LD      BC,$0600            
1834: 11 83 44        LD      DE,$4483            
1837: 21 81 44        LD      HL,$4481            
183A: ED B0           LDIR                        
183C: DB 09           IN      A,($09)             ;
183E: 11 08 04        LD      DE,$0408            
1841: 21 FE 0F        LD      HL,$0FFE            
1844: B7              OR      A                   
1845: ED 52           SBC     HL,DE               
1847: 44              LD      B,H                 
1848: 4D              LD      C,L                 
1849: 11 02 80        LD      DE,$8002            
184C: 21 00 80        LD      HL,$8000            
184F: ED B0           LDIR                        
1851: DB 09           IN      A,($09)             ;
1853: C9              RET                         
1854: DB 0B           IN      A,($0B)             ;
1856: CB 7F           BIT     7,A                 
1858: 20 FA           JR      NZ,$1854            ; 
185A: DB 09           IN      A,($09)             ;
185C: C9              RET                         
185D: F5              PUSH    AF                  
185E: 3A 17 40        LD      A,($4017)           ; 
1861: FD BE 97        CP      (IY+$97)            
1864: 28 FB           JR      Z,$1861             ; 
1866: F1              POP     AF                  
1867: C9              RET                         
1868: 06 13           LD      B,$13               
186A: 11 BB 81        LD      DE,$81BB            
186D: 21 9B 40        LD      HL,$409B            
1870: 7E              LD      A,(HL)              
1871: B7              OR      A                   
1872: 28 2F           JR      Z,$18A3             ; 
1874: FD CB EA 76     BIT     6,(IY+$EA)          
1878: 28 29           JR      Z,$18A3             ; 
187A: 91              SUB     C                   
187B: 30 02           JR      NC,$187F            ; 
187D: 3E 00           LD      A,$00               
187F: 77              LD      (HL),A              
1880: 38 11           JR      C,$1893             ; 
1882: 28 0F           JR      Z,$1893             ; 
1884: FD CB 1A F6     SET     6,(IY+$1A)          
1888: CB 67           BIT     4,A                 
188A: 20 07           JR      NZ,$1893            ; 
188C: 1A              LD      A,(DE)              
188D: E6 0F           AND     $0F                 
188F: F6 C0           OR      $C0                 
1891: 18 0F           JR      $18A2               ; 
1893: 78              LD      A,B                 
1894: FE 0B           CP      $0B                 
1896: 38 05           JR      C,$189D             ; 
1898: 1A              LD      A,(DE)              
1899: E6 0F           AND     $0F                 
189B: 18 05           JR      $18A2               ; 
189D: 1A              LD      A,(DE)              
189E: E6 0F           AND     $0F                 
18A0: F6 70           OR      $70                 
18A2: 12              LD      (DE),A              
18A3: 13              INC     DE                  
18A4: 13              INC     DE                  
18A5: 13              INC     DE                  
18A6: 13              INC     DE                  
18A7: 13              INC     DE                  
18A8: 13              INC     DE                  
18A9: 23              INC     HL                  
18AA: 10 C4           DJNZ    $1870               ; 
18AC: 3A 9A 40        LD      A,($409A)           ; 
18AF: CB 77           BIT     6,A                 
18B1: 28 04           JR      Z,$18B7             ; 
18B3: 3E 80           LD      A,$80               
18B5: 18 01           JR      $18B8               ; 
18B7: AF              XOR     A                   
18B8: 32 9A 40        LD      ($409A),A           ; 
18BB: C9              RET                         
18BC: 01 08 04        LD      BC,$0408            
18BF: 11 F8 9B        LD      DE,$9BF8            
18C2: 21 00 90        LD      HL,$9000            
18C5: ED B0           LDIR                        
18C7: DB 09           IN      A,($09)             ;
18C9: 01 08 04        LD      BC,$0408            
18CC: 11 F8 8B        LD      DE,$8BF8            
18CF: 21 00 90        LD      HL,$9000            
18D2: ED B0           LDIR                        
18D4: DB 09           IN      A,($09)             ;
18D6: 01 08 04        LD      BC,$0408            
18D9: 11 F0 87        LD      DE,$87F0            
18DC: 21 00 90        LD      HL,$9000            
18DF: ED B0           LDIR                        
18E1: DB 09           IN      A,($09)             ;
18E3: 01 08 04        LD      BC,$0408            
18E6: DD 21 F8 9B     LD      IX,$9BF8            
18EA: CD 56 2D        CALL    $2D56               ; 
18ED: 01 08 04        LD      BC,$0408            
18F0: DD 21 F8 8B     LD      IX,$8BF8            
18F4: CD 8A 2D        CALL    $2D8A               ; 
18F7: 01 08 04        LD      BC,$0408            
18FA: DD 21 F0 87     LD      IX,$87F0            
18FE: CD C8 2D        CALL    $2DC8               ; 
1901: C9              RET                         
1902: CD BC 18        CALL    $18BC               ; 
1905: 01 30 00        LD      BC,$0030            
1908: 11 01 46        LD      DE,$4601            
190B: 21 D9 30        LD      HL,$30D9            
190E: ED B0           LDIR                        
1910: 06 04           LD      B,$04               
1912: 11 39 40        LD      DE,$4039            
1915: 21 17 46        LD      HL,$4617            
1918: CD 0E 24        CALL    $240E               ; 
191B: 06 01           LD      B,$01               
191D: 11 2D 40        LD      DE,$402D            
1920: 21 2B 46        LD      HL,$462B            
1923: CD 0E 24        CALL    $240E               ; 
1926: 01 B0 01        LD      BC,$01B0            
1929: 11 00 80        LD      DE,$8000            
192C: 21 81 44        LD      HL,$4481            
192F: ED B0           LDIR                        
1931: 01 0E 01        LD      BC,$010E            
1934: 21 09 31        LD      HL,$3109            
1937: ED B0           LDIR                        
1939: 01 10 00        LD      BC,$0010            
193C: 11 34 82        LD      DE,$8234            
193F: 21 E5 3E        LD      HL,$3EE5            
1942: ED B0           LDIR                        
1944: 06 04           LD      B,$04               
1946: 11 45 40        LD      DE,$4045            
1949: 21 46 82        LD      HL,$8246            
194C: CD 0E 24        CALL    $240E               ; 
194F: FD 36 04 05     LD      (IY+$04),$05        
1953: CD F3 2A        CALL    $2AF3               ; 
1956: FD 36 04 06     LD      (IY+$04),$06        
195A: CD F3 2A        CALL    $2AF3               ; 
195D: FD 36 04 09     LD      (IY+$04),$09        
1961: CD F3 2A        CALL    $2AF3               ; 
1964: C9              RET                         
1965: DB 09           IN      A,($09)             ;
1967: 06 20           LD      B,$20               
1969: FD 36 F5 80     LD      (IY+$F5),$80        
196D: FD 36 F6 80     LD      (IY+$F6),$80        
1971: FD 36 F4 00     LD      (IY+$F4),$00        
1975: FD 4E 99        LD      C,(IY+$99)          
1978: F3              DI                          
1979: 21 00 00        LD      HL,$0000            
197C: 39              ADD     HL,SP               
197D: EB              EX      DE,HL               
197E: 31 90 2E        LD      SP,$2E90            
1981: FD 36 FD 00     LD      (IY+$FD),$00        
1985: FD 34 FD        INC     (IY+$FD)            ;
1988: DD E1           POP     IX                  
198A: DD 7E 13        LD      A,(IX+$13)          
198D: 91              SUB     C                   
198E: DD 77 13        LD      (IX+$13),A          
1991: DD CB 00 7E     BIT     7,(IX+$00)          
1995: 28 04           JR      Z,$199B             ; 
1997: 30 63           JR      NC,$19FC            ; 
1999: 18 26           JR      $19C1               ; 
199B: D2 4D 1A        JP      NC,$1A4D            ; 
199E: DD CB 01 5E     BIT     3,(IX+$01)          
19A2: C2 4D 1A        JP      NZ,$1A4D            ; 
19A5: DD CB 01 DE     SET     3,(IX+$01)          
19A9: D9              EXX                         
19AA: C1              POP     BC                  
19AB: C1              POP     BC                  
19AC: 60              LD      H,B                 
19AD: 69              LD      L,C                 
19AE: 11 75 84        LD      DE,$8475            
19B1: B7              OR      A                   
19B2: ED 52           SBC     HL,DE               
19B4: CB 2C           SRA     H                   
19B6: CB 1D           RR      L                   
19B8: 7D              LD      A,L                 
19B9: 02              LD      (BC),A              
19BA: 03              INC     BC                  
19BB: 7C              LD      A,H                 
19BC: 02              LD      (BC),A              
19BD: D9              EXX                         
19BE: C3 51 1A        JP      $1A51               ; 
19C1: DD CB 01 4E     BIT     1,(IX+$01)          
19C5: 28 06           JR      Z,$19CD             ; 
19C7: DD CB 01 56     BIT     2,(IX+$01)          
19CB: 20 2F           JR      NZ,$19FC            ; 
19CD: D9              EXX                         
19CE: E1              POP     HL                  
19CF: E1              POP     HL                  
19D0: D9              EXX                         
19D1: 21 00 00        LD      HL,$0000            
19D4: 39              ADD     HL,SP               
19D5: EB              EX      DE,HL               
19D6: F9              LD      SP,HL               
19D7: D9              EXX                         
19D8: E5              PUSH    HL                  
19D9: DD E3           EX      (SP),IX             
19DB: E1              POP     HL                  
19DC: FB              EI                          
19DD: E5              PUSH    HL                  
19DE: 01 17 00        LD      BC,$0017            
19E1: 11 00 40        LD      DE,$4000            
19E4: ED B0           LDIR                        
19E6: CD 59 1A        CALL    $1A59               ; 
19E9: 01 17 00        LD      BC,$0017            
19EC: D1              POP     DE                  
19ED: 21 00 40        LD      HL,$4000            
19F0: ED B0           LDIR                        
19F2: F3              DI                          
19F3: D9              EXX                         
19F4: EB              EX      DE,HL               
19F5: F9              LD      SP,HL               
19F6: FD CB F4 FE     SET     7,(IY+$F4)          
19FA: 18 55           JR      $1A51               ; 
19FC: FD CB F4 7E     BIT     7,(IY+$F4)          
1A00: 28 3F           JR      Z,$1A41             ; 
1A02: 3A 75 40        LD      A,($4075)           ; 
1A05: DD 96 07        SUB     (IX+$07)            
1A08: 30 02           JR      NC,$1A0C            ; 
1A0A: ED 44           NEG                         
1A0C: 67              LD      H,A                 
1A0D: 3A 76 40        LD      A,($4076)           ; 
1A10: DD 96 09        SUB     (IX+$09)            
1A13: 30 02           JR      NC,$1A17            ; 
1A15: ED 44           NEG                         
1A17: BC              CP      H                   
1A18: 38 01           JR      C,$1A1B             ; 
1A1A: 67              LD      H,A                 
1A1B: 2E 08           LD      L,$08               
1A1D: 3E 90           LD      A,$90               
1A1F: CB 04           RLC     H                   
1A21: 38 05           JR      C,$1A28             ; 
1A23: D6 10           SUB     $10                 
1A25: 2D              DEC     L                   
1A26: 20 F7           JR      NZ,$1A1F            ; 
1A28: DD 96 0B        SUB     (IX+$0B)            
1A2B: 67              LD      H,A                 
1A2C: DD 7E 07        LD      A,(IX+$07)          
1A2F: 32 75 40        LD      ($4075),A           ; 
1A32: DD 7E 09        LD      A,(IX+$09)          
1A35: 32 76 40        LD      ($4076),A           ; 
1A38: DD E1           POP     IX                  
1A3A: DD E1           POP     IX                  
1A3C: DD 74 07        LD      (IX+$07),H          
1A3F: 18 10           JR      $1A51               ; 
1A41: DD 7E 07        LD      A,(IX+$07)          
1A44: 32 75 40        LD      ($4075),A           ; 
1A47: DD 7E 09        LD      A,(IX+$09)          
1A4A: 32 76 40        LD      ($4076),A           ; 
1A4D: DD E1           POP     IX                  
1A4F: DD E1           POP     IX                  
1A51: 05              DEC     B                   
1A52: C2 85 19        JP      NZ,$1985            ; 
1A55: EB              EX      DE,HL               
1A56: F9              LD      SP,HL               
1A57: FB              EI                          
1A58: C9              RET                         
1A59: DB 09           IN      A,($09)             ;
1A5B: DB 0B           IN      A,($0B)             ;
1A5D: CB 7F           BIT     7,A                 
1A5F: CC 50 17        CALL    Z,$1750             ; 
1A62: 3A 17 40        LD      A,($4017)           ; 
1A65: FD 96 98        SUB     (IY+$98)            
1A68: FD 86 92        ADD     A,(IY+$92)          
1A6B: 32 13 40        LD      ($4013),A           ; 
1A6E: FD CB 81 6E     BIT     5,(IY+$81)          
1A72: C2 F9 1A        JP      NZ,$1AF9            ; 
1A75: 3A 7D 40        LD      A,($407D)           ; 
1A78: FE 01           CP      $01                 
1A7A: 28 28           JR      Z,$1AA4             ; 
1A7C: FE 0E           CP      $0E                 
1A7E: 38 58           JR      C,$1AD8             ; 
1A80: FE 16           CP      $16                 
1A82: 30 75           JR      NC,$1AF9            ; 
1A84: FE 12           CP      $12                 
1A86: 38 5E           JR      C,$1AE6             ; 
1A88: DD E5           PUSH    IX                  
1A8A: DD 21 96 2E     LD      IX,$2E96            
1A8E: FD 46 E7        LD      B,(IY+$E7)          
1A91: FD 36 FE 02     LD      (IY+$FE),$02        
1A95: CD 99 21        CALL    $2199               ; 
1A98: DD 21 0E 2F     LD      IX,$2F0E            
1A9C: 06 0B           LD      B,$0B               
1A9E: FD 36 FE 16     LD      (IY+$FE),$16        
1AA2: 18 50           JR      $1AF4               ; 
1AA4: 3A 7A 40        LD      A,($407A)           ; 
1AA7: B7              OR      A                   
1AA8: 20 20           JR      NZ,$1ACA            ; 
1AAA: 3A 67 40        LD      A,($4067)           ; 
1AAD: FE 06           CP      $06                 
1AAF: 20 08           JR      NZ,$1AB9            ; 
1AB1: 3A 22 40        LD      A,($4022)           ; 
1AB4: B7              OR      A                   
1AB5: 20 13           JR      NZ,$1ACA            ; 
1AB7: 18 05           JR      $1ABE               ; 
1AB9: FD 35 FC        DEC     (IY+$FC)            
1ABC: 20 0C           JR      NZ,$1ACA            ; 
1ABE: FD CB 81 E6     SET     4,(IY+$81)          
1AC2: FD 36 00 FF     LD      (IY+$00),$FF        
1AC6: FD 36 01 FF     LD      (IY+$01),$FF        
1ACA: DD E5           PUSH    IX                  
1ACC: DD 21 96 2E     LD      IX,$2E96            
1AD0: 06 1F           LD      B,$1F               
1AD2: FD 36 FE 02     LD      (IY+$FE),$02        
1AD6: 18 1C           JR      $1AF4               ; 
1AD8: DD E5           PUSH    IX                  
1ADA: DD 21 0E 2F     LD      IX,$2F0E            
1ADE: 06 0B           LD      B,$0B               
1AE0: FD 36 FE 0E     LD      (IY+$FE),$0E        
1AE4: 18 0E           JR      $1AF4               ; 
1AE6: 18 11           JR      $1AF9               ; 
1AE8: DD E5           PUSH    IX                  
1AEA: DD 21 90 2E     LD      IX,$2E90            
1AEE: 06 01           LD      B,$01               
1AF0: FD 36 FE 01     LD      (IY+$FE),$01        
1AF4: CD 99 21        CALL    $2199               ; 
1AF7: DD E1           POP     IX                  
1AF9: FD CB 81 56     BIT     2,(IY+$81)          
1AFD: 20 17           JR      NZ,$1B16            ; 
1AFF: FD CB 81 D6     SET     2,(IY+$81)          
1B03: DD E5           PUSH    IX                  
1B05: E1              POP     HL                  
1B06: 11 7F 84        LD      DE,$847F            
1B09: B7              OR      A                   
1B0A: ED 52           SBC     HL,DE               
1B0C: CB 2C           SRA     H                   
1B0E: CB 1D           RR      L                   
1B10: DD 74 01        LD      (IX+$01),H          
1B13: DD 75 00        LD      (IX+$00),L          
1B16: FD CB 80 46     BIT     0,(IY+$80)          
1B1A: 28 77           JR      Z,$1B93             ; 
1B1C: FD CB EB 7E     BIT     7,(IY+$EB)          
1B20: 28 71           JR      Z,$1B93             ; 
1B22: FD CB 81 7E     BIT     7,(IY+$81)          
1B26: C4 3F 28        CALL    NZ,$283F            ; 
1B29: 3A 0A 40        LD      A,($400A)           ; 
1B2C: CB 67           BIT     4,A                 
1B2E: 28 02           JR      Z,$1B32             ; 
1B30: EE 0F           XOR     $0F                 
1B32: E6 0F           AND     $0F                 
1B34: 07              RLCA                        
1B35: 5F              LD      E,A                 
1B36: 16 00           LD      D,$00               
1B38: 21 21 30        LD      HL,$3021            
1B3B: 19              ADD     HL,DE               
1B3C: 5E              LD      E,(HL)              
1B3D: 23              INC     HL                  
1B3E: 56              LD      D,(HL)              
1B3F: 3A 0A 40        LD      A,($400A)           ; 
1B42: E6 30           AND     $30                 
1B44: 28 08           JR      Z,$1B4E             ; 
1B46: FE 30           CP      $30                 
1B48: 28 04           JR      Z,$1B4E             ; 
1B4A: 7A              LD      A,D                 
1B4B: ED 44           NEG                         
1B4D: 57              LD      D,A                 
1B4E: 3A 0A 40        LD      A,($400A)           ; 
1B51: CB 6F           BIT     5,A                 
1B53: 28 04           JR      Z,$1B59             ; 
1B55: 7B              LD      A,E                 
1B56: ED 44           NEG                         
1B58: 5F              LD      E,A                 
1B59: 2A 02 40        LD      HL,($4002)          ; 
1B5C: 4A              LD      C,D                 
1B5D: 06 00           LD      B,$00               
1B5F: CB 7A           BIT     7,D                 
1B61: 28 02           JR      Z,$1B65             ; 
1B63: 06 FF           LD      B,$FF               
1B65: CB 21           SLA     C                   
1B67: 09              ADD     HL,BC               
1B68: CD 64 21        CALL    $2164               ; 
1B6B: 22 02 40        LD      ($4002),HL          ; 
1B6E: 2A 04 40        LD      HL,($4004)          ; 
1B71: 4B              LD      C,E                 
1B72: 06 00           LD      B,$00               
1B74: CB 7B           BIT     7,E                 
1B76: 28 02           JR      Z,$1B7A             ; 
1B78: 06 FF           LD      B,$FF               
1B7A: CB 21           SLA     C                   
1B7C: 09              ADD     HL,BC               
1B7D: CD 64 21        CALL    $2164               ; 
1B80: 22 04 40        LD      ($4004),HL          ; 
1B83: FD CB 81 7E     BIT     7,(IY+$81)          
1B87: 20 0A           JR      NZ,$1B93            ; 
1B89: FD CB 81 76     BIT     6,(IY+$81)          
1B8D: 28 04           JR      Z,$1B93             ; 
1B8F: FD CB 80 86     RES     0,(IY+$80)          
1B93: FD CB 80 5E     BIT     3,(IY+$80)          
1B97: 28 1C           JR      Z,$1BB5             ; 
1B99: FD CB 81 7E     BIT     7,(IY+$81)          
1B9D: 20 04           JR      NZ,$1BA3            ; 
1B9F: FD CB 80 9E     RES     3,(IY+$80)          
1BA3: 2A 02 40        LD      HL,($4002)          ; 
1BA6: CD 48 21        CALL    $2148               ; 
1BA9: 22 02 40        LD      ($4002),HL          ; 
1BAC: 2A 04 40        LD      HL,($4004)          ; 
1BAF: CD 48 21        CALL    $2148               ; 
1BB2: 22 04 40        LD      ($4004),HL          ; 
1BB5: FD CB 80 76     BIT     6,(IY+$80)          
1BB9: 28 30           JR      Z,$1BEB             ; 
1BBB: CD 2A 1F        CALL    $1F2A               ; 
1BBE: FD CB F8 7E     BIT     7,(IY+$F8)          
1BC2: 28 11           JR      Z,$1BD5             ; 
1BC4: FD CB 81 46     BIT     0,(IY+$81)          
1BC8: 28 0B           JR      Z,$1BD5             ; 
1BCA: 3A 7D 40        LD      A,($407D)           ; 
1BCD: 32 7E 40        LD      ($407E),A           ; 
1BD0: CD BF 27        CALL    $27BF               ; 
1BD3: 18 16           JR      $1BEB               ; 
1BD5: ED 5B 02 40     LD      DE,($4002)          ; 
1BD9: 2A 06 40        LD      HL,($4006)          ; 
1BDC: 19              ADD     HL,DE               
1BDD: 22 06 40        LD      ($4006),HL          ; 
1BE0: ED 5B 04 40     LD      DE,($4004)          ; 
1BE4: 2A 08 40        LD      HL,($4008)          ; 
1BE7: 19              ADD     HL,DE               
1BE8: 22 08 40        LD      ($4008),HL          ; 
1BEB: 3A 7B 40        LD      A,($407B)           ; 
1BEE: FD BE FD        CP      (IY+$FD)            
1BF1: 20 30           JR      NZ,$1C23            ; 
1BF3: FD BE FA        CP      (IY+$FA)            
1BF6: 28 06           JR      Z,$1BFE             ; 
1BF8: FD CB 81 6E     BIT     5,(IY+$81)          
1BFC: 28 09           JR      Z,$1C07             ; 
1BFE: FD 36 FB 00     LD      (IY+$FB),$00        
1C02: CD 67 24        CALL    $2467               ; 
1C05: 18 1C           JR      $1C23               ; 
1C07: 3E 1E           LD      A,$1E               
1C09: FD 96 E7        SUB     (IY+$E7)            
1C0C: FD 96 E7        SUB     (IY+$E7)            
1C0F: 32 12 40        LD      ($4012),A           ; 
1C12: FD CB 80 F6     SET     6,(IY+$80)          
1C16: 3A 0E 40        LD      A,($400E)           ; 
1C19: B7              OR      A                   
1C1A: 20 04           JR      NZ,$1C20            ; 
1C1C: FD 36 8E 0C     LD      (IY+$8E),$0C        
1C20: CD 2F 25        CALL    $252F               ; 
1C23: 3A 7A 40        LD      A,($407A)           ; 
1C26: FD BE FD        CP      (IY+$FD)            
1C29: C2 B4 1D        JP      NZ,$1DB4            ; 
1C2C: FD CB 81 6E     BIT     5,(IY+$81)          
1C30: C2 AD 1D        JP      NZ,$1DAD            ; 
1C33: FD CB 33 66     BIT     4,(IY+$33)          
1C37: 28 2E           JR      Z,$1C67             ; 
1C39: FD CB 33 A6     RES     4,(IY+$33)          
1C3D: 3A 0A 40        LD      A,($400A)           ; 
1C40: 32 0F 40        LD      ($400F),A           ; 
1C43: CD 2F 25        CALL    $252F               ; 
1C46: 3A 67 40        LD      A,($4067)           ; 
1C49: FE 06           CP      $06                 
1C4B: 28 16           JR      Z,$1C63             ; 
1C4D: CD 06 29        CALL    $2906               ; 
1C50: E6 0F           AND     $0F                 
1C52: F6 20           OR      $20                 
1C54: FD 77 8E        LD      (IY+$8E),A          
1C57: E6 07           AND     $07                 
1C59: F6 04           OR      $04                 
1C5B: 32 7F 40        LD      ($407F),A           ; 
1C5E: CD 58 27        CALL    $2758               ; 
1C61: 18 04           JR      $1C67               ; 
1C63: FD 36 FC FA     LD      (IY+$FC),$FA        
1C67: FD CB 80 F6     SET     6,(IY+$80)          
1C6B: FD 7E 8E        LD      A,(IY+$8E)          
1C6E: FE 01           CP      $01                 
1C70: 20 09           JR      NZ,$1C7B            ; 
1C72: FD 35 FF        DEC     (IY+$FF)            
1C75: 20 04           JR      NZ,$1C7B            ; 
1C77: FD 36 8E 00     LD      (IY+$8E),$00        
1C7B: 3A 68 40        LD      A,($4068)           ; 
1C7E: FE 0F           CP      $0F                 
1C80: 28 22           JR      Z,$1CA4             ; 
1C82: 3A 22 40        LD      A,($4022)           ; 
1C85: FE 0A           CP      $0A                 
1C87: 38 0B           JR      C,$1C94             ; 
1C89: FE 0F           CP      $0F                 
1C8B: 30 17           JR      NC,$1CA4            ; 
1C8D: 3E 02           LD      A,$02               
1C8F: CD F6 2D        CALL    $2DF6               ; 
1C92: 18 10           JR      $1CA4               ; 
1C94: FE 05           CP      $05                 
1C96: 38 07           JR      C,$1C9F             ; 
1C98: 3E 03           LD      A,$03               
1C9A: CD F6 2D        CALL    $2DF6               ; 
1C9D: 18 05           JR      $1CA4               ; 
1C9F: 3E 04           LD      A,$04               
1CA1: CD F6 2D        CALL    $2DF6               ; 
1CA4: 3A 77 40        LD      A,($4077)           ; 
1CA7: FE 01           CP      $01                 
1CA9: 28 0A           JR      Z,$1CB5             ; 
1CAB: 3A 22 40        LD      A,($4022)           ; 
1CAE: B7              OR      A                   
1CAF: CA D6 1C        JP      Z,$1CD6             ; 
1CB2: C3 3C 1D        JP      $1D3C               ; 
1CB5: FD CB EA 7E     BIT     7,(IY+$EA)          
1CB9: CA 3C 1D        JP      Z,$1D3C             ; 
1CBC: FD 36 92 0C     LD      (IY+$92),$0C        
1CC0: 3A 22 40        LD      A,($4022)           ; 
1CC3: FE 0C           CP      $0C                 
1CC5: 30 75           JR      NC,$1D3C            ; 
1CC7: FD 36 92 0A     LD      (IY+$92),$0A        
1CCB: FE 06           CP      $06                 
1CCD: 30 6D           JR      NC,$1D3C            ; 
1CCF: FD 36 92 08     LD      (IY+$92),$08        
1CD3: B7              OR      A                   
1CD4: 20 66           JR      NZ,$1D3C            ; 
1CD6: FD CB EA FE     SET     7,(IY+$EA)          
1CDA: FD 36 92 04     LD      (IY+$92),$04        
1CDE: 3E 11           LD      A,$11               
1CE0: FD 96 E7        SUB     (IY+$E7)            
1CE3: 32 22 40        LD      ($4022),A           ; 
1CE6: CD 06 29        CALL    $2906               ; 
1CE9: E6 0F           AND     $0F                 
1CEB: F6 10           OR      $10                 
1CED: 32 0E 40        LD      ($400E),A           ; 
1CF0: FD CB EA 46     BIT     0,(IY+$EA)          
1CF4: 28 04           JR      Z,$1CFA             ; 
1CF6: FD 36 8E 02     LD      (IY+$8E),$02        
1CFA: FD CB 81 BE     RES     7,(IY+$81)          
1CFE: FD CB 80 DE     SET     3,(IY+$80)          
1D02: FD 36 92 04     LD      (IY+$92),$04        
1D06: FD CB EB 5E     BIT     3,(IY+$EB)          
1D0A: 20 0C           JR      NZ,$1D18            ; 
1D0C: FD CB EB DE     SET     3,(IY+$EB)          
1D10: 3E 10           LD      A,$10               
1D12: FD 96 E7        SUB     (IY+$E7)            
1D15: 32 12 40        LD      ($4012),A           ; 
1D18: FD 36 FF FA     LD      (IY+$FF),$FA        
1D1C: 3E 05           LD      A,$05               
1D1E: CD F6 2D        CALL    $2DF6               ; 
1D21: 3A 3B 40        LD      A,($403B)           ; 
1D24: B7              OR      A                   
1D25: 20 58           JR      NZ,$1D7F            ; 
1D27: 3A 3A 40        LD      A,($403A)           ; 
1D2A: FE 35           CP      $35                 
1D2C: 30 51           JR      NC,$1D7F            ; 
1D2E: FD 36 8E 00     LD      (IY+$8E),$00        
1D32: FD 36 FF FA     LD      (IY+$FF),$FA        
1D36: FD 36 92 10     LD      (IY+$92),$10        
1D3A: 18 43           JR      $1D7F               ; 
1D3C: FD CB 81 7E     BIT     7,(IY+$81)          
1D40: 20 4F           JR      NZ,$1D91            ; 
1D42: 3A 77 40        LD      A,($4077)           ; 
1D45: FE 01           CP      $01                 
1D47: 20 22           JR      NZ,$1D6B            ; 
1D49: 3A 7C 40        LD      A,($407C)           ; 
1D4C: FE 14           CP      $14                 
1D4E: 38 04           JR      C,$1D54             ; 
1D50: FD 36 FC 14     LD      (IY+$FC),$14        
1D54: 3A B9 40        LD      A,($40B9)           ; 
1D57: FD AE 87        XOR     (IY+$87)            
1D5A: 4F              LD      C,A                 
1D5B: 3A BB 40        LD      A,($40BB)           ; 
1D5E: FD AE 89        XOR     (IY+$89)            
1D61: B1              OR      C                   
1D62: E6 80           AND     $80                 
1D64: 28 05           JR      Z,$1D6B             ; 
1D66: CD 3F 28        CALL    $283F               ; 
1D69: 18 26           JR      $1D91               ; 
1D6B: 3A 0F 40        LD      A,($400F)           ; 
1D6E: 32 0A 40        LD      ($400A),A           ; 
1D71: 3A 22 40        LD      A,($4022)           ; 
1D74: B7              OR      A                   
1D75: CA D6 1C        JP      Z,$1CD6             ; 
1D78: E6 07           AND     $07                 
1D7A: 20 15           JR      NZ,$1D91            ; 
1D7C: FD 35 A2        DEC     (IY+$A2)            
1D7F: 3A 0F 40        LD      A,($400F)           ; 
1D82: C6 20           ADD     A,$20               
1D84: 32 0F 40        LD      ($400F),A           ; 
1D87: CD 06 29        CALL    $2906               ; 
1D8A: CB 47           BIT     0,A                 
1D8C: 28 03           JR      Z,$1D91             ; 
1D8E: FD 35 8F        DEC     (IY+$8F)            
1D91: CD 2F 25        CALL    $252F               ; 
1D94: 3A 7F 40        LD      A,($407F)           ; 
1D97: B7              OR      A                   
1D98: 28 13           JR      Z,$1DAD             ; 
1D9A: 3A 7A 40        LD      A,($407A)           ; 
1D9D: B7              OR      A                   
1D9E: 28 0D           JR      Z,$1DAD             ; 
1DA0: FD 35 FC        DEC     (IY+$FC)            
1DA3: 20 0F           JR      NZ,$1DB4            ; 
1DA5: CD 58 27        CALL    $2758               ; 
1DA8: CD 86 21        CALL    $2186               ; 
1DAB: 18 07           JR      $1DB4               ; 
1DAD: FD 36 FA 00     LD      (IY+$FA),$00        
1DB1: CD 86 21        CALL    $2186               ; 
1DB4: FD CB 81 6E     BIT     5,(IY+$81)          
1DB8: 28 17           JR      Z,$1DD1             ; 
1DBA: 3A 0A 40        LD      A,($400A)           ; 
1DBD: E6 03           AND     $03                 
1DBF: 07              RLCA                        
1DC0: FD 34 8A        INC     (IY+$8A)            ;
1DC3: 5F              LD      E,A                 
1DC4: 16 00           LD      D,$00               
1DC6: 21 5D 3F        LD      HL,$3F5D            
1DC9: 19              ADD     HL,DE               
1DCA: 5E              LD      E,(HL)              
1DCB: 23              INC     HL                  
1DCC: 56              LD      D,(HL)              
1DCD: EB              EX      DE,HL               
1DCE: C3 5B 1E        JP      $1E5B               ; 
1DD1: FD CB 80 66     BIT     4,(IY+$80)          
1DD5: CA 63 1E        JP      Z,$1E63             ; 
1DD8: FD CB 81 76     BIT     6,(IY+$81)          
1DDC: 20 3A           JR      NZ,$1E18            ; 
1DDE: FD 34 94        INC     (IY+$94)            ;
1DE1: 3A 14 40        LD      A,($4014)           ; 
1DE4: 07              RLCA                        
1DE5: E6 06           AND     $06                 
1DE7: 20 1A           JR      NZ,$1E03            ; 
1DE9: 3A 0E 40        LD      A,($400E)           ; 
1DEC: B7              OR      A                   
1DED: 3E 00           LD      A,$00               
1DEF: 28 0C           JR      Z,$1DFD             ; 
1DF1: FD CB 81 7E     BIT     7,(IY+$81)          
1DF5: 28 0C           JR      Z,$1E03             ; 
1DF7: FD 36 94 02     LD      (IY+$94),$02        
1DFB: 18 06           JR      $1E03               ; 
1DFD: 3E 02           LD      A,$02               
1DFF: FD 36 94 01     LD      (IY+$94),$01        
1E03: FD CB 81 7E     BIT     7,(IY+$81)          
1E07: 20 02           JR      NZ,$1E0B            ; 
1E09: CB DF           SET     3,A                 
1E0B: 5F              LD      E,A                 
1E0C: 16 00           LD      D,$00               
1E0E: 21 4D 3F        LD      HL,$3F4D            
1E11: 19              ADD     HL,DE               
1E12: 5E              LD      E,(HL)              
1E13: 23              INC     HL                  
1E14: 56              LD      D,(HL)              
1E15: EB              EX      DE,HL               
1E16: 18 43           JR      $1E5B               ; 
1E18: 3A 0A 40        LD      A,($400A)           ; 
1E1B: 32 0F 40        LD      ($400F),A           ; 
1E1E: E6 30           AND     $30                 
1E20: 0F              RRCA                        
1E21: 0F              RRCA                        
1E22: 0F              RRCA                        
1E23: 5F              LD      E,A                 
1E24: 16 00           LD      D,$00               
1E26: 21 A1 30        LD      HL,$30A1            
1E29: 19              ADD     HL,DE               
1E2A: 5E              LD      E,(HL)              
1E2B: 23              INC     HL                  
1E2C: 56              LD      D,(HL)              
1E2D: 3A 0A 40        LD      A,($400A)           ; 
1E30: CB 67           BIT     4,A                 
1E32: 28 02           JR      Z,$1E36             ; 
1E34: EE 0F           XOR     $0F                 
1E36: E6 0F           AND     $0F                 
1E38: 07              RLCA                        
1E39: 4F              LD      C,A                 
1E3A: 06 00           LD      B,$00               
1E3C: 21 A9 30        LD      HL,$30A9            
1E3F: 09              ADD     HL,BC               
1E40: 4E              LD      C,(HL)              
1E41: 23              INC     HL                  
1E42: 46              LD      B,(HL)              
1E43: EB              EX      DE,HL               
1E44: 09              ADD     HL,BC               
1E45: 7C              LD      A,H                 
1E46: E6 0F           AND     $0F                 
1E48: F6 C0           OR      $C0                 
1E4A: 67              LD      H,A                 
1E4B: 22 0B 46        LD      ($460B),HL          ; 
1E4E: 11 F9 FF        LD      DE,$FFF9            
1E51: 19              ADD     HL,DE               
1E52: 22 0D 46        LD      ($460D),HL          ; 
1E55: 22 11 46        LD      ($4611),HL          ; 
1E58: 2A 65 3F        LD      HL,($3F65)          ; 
1E5B: DD 74 0B        LD      (IX+$0B),H          
1E5E: DD 75 0A        LD      (IX+$0A),L          
1E61: 18 0C           JR      $1E6F               ; 
1E63: 3A 16 40        LD      A,($4016)           ; 
1E66: DD 77 0B        LD      (IX+$0B),A          
1E69: 3A 15 40        LD      A,($4015)           ; 
1E6C: DD 77 0A        LD      (IX+$0A),A          
1E6F: 3A 0C 40        LD      A,($400C)           ; 
1E72: B7              OR      A                   
1E73: 28 09           JR      Z,$1E7E             ; 
1E75: FD 35 8C        DEC     (IY+$8C)            
1E78: 20 04           JR      NZ,$1E7E            ; 
1E7A: FD CB 80 BE     RES     7,(IY+$80)          
1E7E: 3A 0E 40        LD      A,($400E)           ; 
1E81: B7              OR      A                   
1E82: 28 17           JR      Z,$1E9B             ; 
1E84: FD 35 8E        DEC     (IY+$8E)            
1E87: 20 12           JR      NZ,$1E9B            ; 
1E89: 3E 2C           LD      A,$2C               
1E8B: FD 96 E7        SUB     (IY+$E7)            
1E8E: FD 96 E7        SUB     (IY+$E7)            
1E91: FD 96 E7        SUB     (IY+$E7)            
1E94: 32 0E 40        LD      ($400E),A           ; 
1E97: FD CB 80 D6     SET     2,(IY+$80)          
1E9B: FD CB 80 56     BIT     2,(IY+$80)          
1E9F: C4 EB 25        CALL    NZ,$25EB            ; 
1EA2: 2A 08 40        LD      HL,($4008)          ; 
1EA5: 7C              LD      A,H                 
1EA6: CB 04           RLC     H                   
1EA8: CB 04           RLC     H                   
1EAA: CB 05           RLC     L                   
1EAC: 17              RLA                         
1EAD: CB 05           RLC     L                   
1EAF: 17              RLA                         
1EB0: DD 77 02        LD      (IX+$02),A          
1EB3: 7C              LD      A,H                 
1EB4: E6 03           AND     $03                 
1EB6: F6 A0           OR      $A0                 
1EB8: DD 77 03        LD      (IX+$03),A          
1EBB: 2A 06 40        LD      HL,($4006)          ; 
1EBE: 7C              LD      A,H                 
1EBF: CB 04           RLC     H                   
1EC1: CB 04           RLC     H                   
1EC3: CB 05           RLC     L                   
1EC5: 17              RLA                         
1EC6: CB 05           RLC     L                   
1EC8: 17              RLA                         
1EC9: DD 77 04        LD      (IX+$04),A          
1ECC: 7C              LD      A,H                 
1ECD: E6 03           AND     $03                 
1ECF: 67              LD      H,A                 
1ED0: 3A 0B 40        LD      A,($400B)           ; 
1ED3: E6 F0           AND     $F0                 
1ED5: B4              OR      H                   
1ED6: DD 77 05        LD      (IX+$05),A          
1ED9: DD 36 06 00     LD      (IX+$06),$00        
1EDD: DD 36 08 00     LD      (IX+$08),$00        
1EE1: DD 36 09 00     LD      (IX+$09),$00        
1EE5: 3A 75 40        LD      A,($4075)           ; 
1EE8: FD 96 87        SUB     (IY+$87)            
1EEB: 30 02           JR      NC,$1EEF            ; 
1EED: ED 44           NEG                         
1EEF: 57              LD      D,A                 
1EF0: 3A 76 40        LD      A,($4076)           ; 
1EF3: FD 96 89        SUB     (IY+$89)            
1EF6: 30 02           JR      NC,$1EFA            ; 
1EF8: ED 44           NEG                         
1EFA: BA              CP      D                   
1EFB: 30 01           JR      NC,$1EFE            ; 
1EFD: 7A              LD      A,D                 
1EFE: 06 08           LD      B,$08               
1F00: 4F              LD      C,A                 
1F01: 3E 90           LD      A,$90               
1F03: CB 01           RLC     C                   
1F05: 38 04           JR      C,$1F0B             ; 
1F07: D6 10           SUB     $10                 
1F09: 10 F8           DJNZ    $1F03               ; 
1F0B: FD 96 8B        SUB     (IY+$8B)            
1F0E: DD 77 07        LD      (IX+$07),A          
1F11: 3A 07 40        LD      A,($4007)           ; 
1F14: 32 75 40        LD      ($4075),A           ; 
1F17: 3A 09 40        LD      A,($4009)           ; 
1F1A: 32 76 40        LD      ($4076),A           ; 
1F1D: DB 0B           IN      A,($0B)             ;
1F1F: CB FF           SET     7,A                 
1F21: CC 50 17        CALL    Z,$1750             ; 
1F24: FD CB 81 D6     SET     2,(IY+$81)          
1F28: C9              RET                         
1F29: C3 DB 09        JP      $09DB               ; 
1F2C: FD 36 F8 00     LD      (IY+$F8),$00        
1F30: ED 5B 08 40     LD      DE,($4008)          ; 
1F34: 2A 04 40        LD      HL,($4004)          ; 
1F37: 19              ADD     HL,DE               
1F38: CB 7A           BIT     7,D                 
1F3A: 20 0F           JR      NZ,$1F4B            ; 
1F3C: CB 72           BIT     6,D                 
1F3E: 20 18           JR      NZ,$1F58            ; 
1F40: CB 7C           BIT     7,H                 
1F42: 28 14           JR      Z,$1F58             ; 
1F44: CB 74           BIT     6,H                 
1F46: 28 10           JR      Z,$1F58             ; 
1F48: C3 17 20        JP      $2017               ; 
1F4B: CB 72           BIT     6,D                 
1F4D: 28 09           JR      Z,$1F58             ; 
1F4F: CB 7C           BIT     7,H                 
1F51: 20 05           JR      NZ,$1F58            ; 
1F53: CB 74           BIT     6,H                 
1F55: CA 17 20        JP      Z,$2017             ; 
1F58: 7C              LD      A,H                 
1F59: D6 80           SUB     $80                 
1F5B: 30 02           JR      NC,$1F5F            ; 
1F5D: ED 44           NEG                         
1F5F: 5F              LD      E,A                 
1F60: ED 4B 06 40     LD      BC,($4006)          ; 
1F64: 2A 02 40        LD      HL,($4002)          ; 
1F67: 09              ADD     HL,BC               
1F68: 7C              LD      A,H                 
1F69: D6 80           SUB     $80                 
1F6B: 30 02           JR      NC,$1F6F            ; 
1F6D: ED 44           NEG                         
1F6F: 57              LD      D,A                 
1F70: CB 78           BIT     7,B                 
1F72: 20 0E           JR      NZ,$1F82            ; 
1F74: CB 70           BIT     6,B                 
1F76: 20 1E           JR      NZ,$1F96            ; 
1F78: CB 7C           BIT     7,H                 
1F7A: 28 1A           JR      Z,$1F96             ; 
1F7C: CB 74           BIT     6,H                 
1F7E: 28 16           JR      Z,$1F96             ; 
1F80: 18 0C           JR      $1F8E               ; 
1F82: CB 70           BIT     6,B                 
1F84: 28 10           JR      Z,$1F96             ; 
1F86: CB 7C           BIT     7,H                 
1F88: 20 0C           JR      NZ,$1F96            ; 
1F8A: CB 74           BIT     6,H                 
1F8C: 20 08           JR      NZ,$1F96            ; 
1F8E: 7B              LD      A,E                 
1F8F: FE 78           CP      $78                 
1F91: 30 4B           JR      NC,$1FDE            ; 
1F93: C3 30 20        JP      $2030               ; 
1F96: 7B              LD      A,E                 
1F97: FE 78           CP      $78                 
1F99: 38 07           JR      C,$1FA2             ; 
1F9B: 7A              LD      A,D                 
1F9C: FE 7F           CP      $7F                 
1F9E: 38 77           JR      C,$2017             ; 
1FA0: 18 3C           JR      $1FDE               ; 
1FA2: 7A              LD      A,D                 
1FA3: FD CB 81 7E     BIT     7,(IY+$81)          
1FA7: 20 07           JR      NZ,$1FB0            ; 
1FA9: FE 7F           CP      $7F                 
1FAB: D2 30 20        JP      NC,$2030            ; 
1FAE: 18 04           JR      $1FB4               ; 
1FB0: FE 78           CP      $78                 
1FB2: 30 7C           JR      NC,$2030            ; 
1FB4: FD CB F8 F6     SET     6,(IY+$F8)          
1FB8: FE 50           CP      $50                 
1FBA: 28 17           JR      Z,$1FD3             ; 
1FBC: D2 CD 20        JP      NC,$20CD            ; 
1FBF: 7B              LD      A,E                 
1FC0: FE 21           CP      $21                 
1FC2: 28 03           JR      Z,$1FC7             ; 
1FC4: D2 CD 20        JP      NC,$20CD            ; 
1FC7: C6 30           ADD     A,$30               
1FC9: BA              CP      D                   
1FCA: CA DE 1F        JP      Z,$1FDE             ; 
1FCD: D2 17 20        JP      NC,$2017            ; 
1FD0: C3 30 20        JP      $2030               ; 
1FD3: 7B              LD      A,E                 
1FD4: FE 21           CP      $21                 
1FD6: CA DE 1F        JP      Z,$1FDE             ; 
1FD9: D2 CD 20        JP      NC,$20CD            ; 
1FDC: 18 52           JR      $2030               ; 
1FDE: 3A 07 40        LD      A,($4007)           ; 
1FE1: FD AE 83        XOR     (IY+$83)            
1FE4: CB 7F           BIT     7,A                 
1FE6: 20 2F           JR      NZ,$2017            ; 
1FE8: 3A 09 40        LD      A,($4009)           ; 
1FEB: FD AE 85        XOR     (IY+$85)            
1FEE: CB 7F           BIT     7,A                 
1FF0: 20 3E           JR      NZ,$2030            ; 
1FF2: FD CB 81 46     BIT     0,(IY+$81)          
1FF6: 20 56           JR      NZ,$204E            ; 
1FF8: ED 5B 02 40     LD      DE,($4002)          ; 
1FFC: 2A 04 40        LD      HL,($4004)          ; 
1FFF: 7A              LD      A,D                 
2000: 2F              CPL                         
2001: 57              LD      D,A                 
2002: 7B              LD      A,E                 
2003: 2F              CPL                         
2004: 5F              LD      E,A                 
2005: 13              INC     DE                  
2006: 7C              LD      A,H                 
2007: 2F              CPL                         
2008: 67              LD      H,A                 
2009: 7D              LD      A,L                 
200A: 2F              CPL                         
200B: 6F              LD      L,A                 
200C: 23              INC     HL                  
200D: ED 53 04 40     LD      ($4004),DE          ; 
2011: 22 02 40        LD      ($4002),HL          ; 
2014: C3 74 20        JP      $2074               ; 
2017: FD CB F8 EE     SET     5,(IY+$F8)          
201B: FD CB 81 46     BIT     0,(IY+$81)          
201F: 20 2D           JR      NZ,$204E            ; 
2021: 2A 04 40        LD      HL,($4004)          ; 
2024: 7C              LD      A,H                 
2025: 2F              CPL                         
2026: 67              LD      H,A                 
2027: 7D              LD      A,L                 
2028: 2F              CPL                         
2029: 6F              LD      L,A                 
202A: 23              INC     HL                  
202B: 22 04 40        LD      ($4004),HL          ; 
202E: 18 44           JR      $2074               ; 
2030: FD CB 81 46     BIT     0,(IY+$81)          
2034: 20 0F           JR      NZ,$2045            ; 
2036: 2A 02 40        LD      HL,($4002)          ; 
2039: 7C              LD      A,H                 
203A: 2F              CPL                         
203B: 67              LD      H,A                 
203C: 7D              LD      A,L                 
203D: 2F              CPL                         
203E: 6F              LD      L,A                 
203F: 23              INC     HL                  
2040: 22 02 40        LD      ($4002),HL          ; 
2043: 18 2F           JR      $2074               ; 
2045: CD CE 20        CALL    $20CE               ; 
2048: FD CB F8 FE     SET     7,(IY+$F8)          
204C: 18 7F           JR      $20CD               ; 
204E: CD CE 20        CALL    $20CE               ; 
2051: FD CB F8 FE     SET     7,(IY+$F8)          
2055: 3A 07 40        LD      A,($4007)           ; 
2058: FE 7E           CP      $7E                 
205A: 30 71           JR      NC,$20CD            ; 
205C: 2A 06 40        LD      HL,($4006)          ; 
205F: ED 5B 02 40     LD      DE,($4002)          ; 
2063: 19              ADD     HL,DE               
2064: 22 06 40        LD      ($4006),HL          ; 
2067: 2A 08 40        LD      HL,($4008)          ; 
206A: ED 5B 04 40     LD      DE,($4004)          ; 
206E: 19              ADD     HL,DE               
206F: 22 04 40        LD      ($4004),HL          ; 
2072: 18 59           JR      $20CD               ; 
2074: CD CE 20        CALL    $20CE               ; 
2077: FD CB 83 2E     SRA     (IY+$83)            
207B: FD CB 82 1E     RR      (IY+$82)            
207F: FD CB 85 2E     SRA     (IY+$85)            
2083: FD CB 84 1E     RR      (IY+$84)            
2087: FD 6E 82        LD      L,(IY+$82)          
208A: FD 66 83        LD      H,(IY+$83)          
208D: 23              INC     HL                  
208E: 7C              LD      A,H                 
208F: B5              OR      L                   
2090: 20 08           JR      NZ,$209A            ; 
2092: FD 36 82 00     LD      (IY+$82),$00        
2096: FD 36 83 00     LD      (IY+$83),$00        
209A: FD 6E 84        LD      L,(IY+$84)          
209D: FD 66 85        LD      H,(IY+$85)          
20A0: 23              INC     HL                  
20A1: 7C              LD      A,H                 
20A2: B5              OR      L                   
20A3: 20 08           JR      NZ,$20AD            ; 
20A5: FD 36 84 00     LD      (IY+$84),$00        
20A9: FD 36 85 00     LD      (IY+$85),$00        
20AD: 3A 02 40        LD      A,($4002)           ; 
20B0: FD B6 83        OR      (IY+$83)            
20B3: FD B6 84        OR      (IY+$84)            
20B6: FD B6 85        OR      (IY+$85)            
20B9: 28 12           JR      Z,$20CD             ; 
20BB: FD CB F8 FE     SET     7,(IY+$F8)          
20BF: FD CB 80 66     BIT     4,(IY+$80)          
20C3: 28 05           JR      Z,$20CA             ; 
20C5: 3E 08           LD      A,$08               
20C7: CD 04 2E        CALL    $2E04               ; 
20CA: C3 2A 1F        JP      $1F2A               ; 
20CD: C9              RET                         
20CE: FD 36 1A 80     LD      (IY+$1A),$80        
20D2: 11 00 00        LD      DE,$0000            
20D5: FD 66 87        LD      H,(IY+$87)          
20D8: FD 6E 89        LD      L,(IY+$89)          
20DB: 3A 78 40        LD      A,($4078)           ; 
20DE: CB 77           BIT     6,A                 
20E0: 20 31           JR      NZ,$2113            ; 
20E2: CB 7C           BIT     7,H                 
20E4: 28 17           JR      Z,$20FD             ; 
20E6: CB 7D           BIT     7,L                 
20E8: 28 0A           JR      Z,$20F4             ; 
20EA: 1E 01           LD      E,$01               
20EC: CB 6F           BIT     5,A                 
20EE: 28 51           JR      Z,$2141             ; 
20F0: 1E 08           LD      E,$08               
20F2: 18 4D           JR      $2141               ; 
20F4: 1E 02           LD      E,$02               
20F6: CB 6F           BIT     5,A                 
20F8: 28 47           JR      Z,$2141             ; 
20FA: 1C              INC     E                   
20FB: 18 44           JR      $2141               ; 
20FD: CB 7D           BIT     7,L                 
20FF: 28 09           JR      Z,$210A             ; 
2101: 1E 06           LD      E,$06               
2103: CB 6F           BIT     5,A                 
2105: 28 3A           JR      Z,$2141             ; 
2107: 1C              INC     E                   
2108: 18 37           JR      $2141               ; 
210A: 1E 04           LD      E,$04               
210C: CB 6F           BIT     5,A                 
210E: 20 31           JR      NZ,$2141            ; 
2110: 1C              INC     E                   
2111: 18 2E           JR      $2141               ; 
2113: CB 7C           BIT     7,H                 
2115: 28 16           JR      Z,$212D             ; 
2117: 1E 0A           LD      E,$0A               
2119: CB 7D           BIT     7,L                 
211B: 28 08           JR      Z,$2125             ; 
211D: CB 6F           BIT     5,A                 
211F: 28 20           JR      Z,$2141             ; 
2121: 1E 13           LD      E,$13               
2123: 18 1C           JR      $2141               ; 
2125: CB 6F           BIT     5,A                 
2127: 28 18           JR      Z,$2141             ; 
2129: 1E 0D           LD      E,$0D               
212B: 18 14           JR      $2141               ; 
212D: 1E 10           LD      E,$10               
212F: CB 7D           BIT     7,L                 
2131: 28 08           JR      Z,$213B             ; 
2133: CB 6F           BIT     5,A                 
2135: 28 0A           JR      Z,$2141             ; 
2137: 1E 13           LD      E,$13               
2139: 18 06           JR      $2141               ; 
213B: CB 6F           BIT     5,A                 
213D: 28 02           JR      Z,$2141             ; 
213F: 1E 0D           LD      E,$0D               
2141: 21 9A 40        LD      HL,$409A            
2144: 19              ADD     HL,DE               
2145: 36 96           LD      (HL),$96            
2147: C9              RET                         
2148: 7C              LD      A,H                 
2149: B5              OR      L                   
214A: 28 17           JR      Z,$2163             ; 
214C: 54              LD      D,H                 
214D: 5D              LD      E,L                 
214E: CB 2A           SRA     D                   
2150: CB 1B           RR      E                   
2152: CB 2A           SRA     D                   
2154: CB 1B           RR      E                   
2156: CB 2A           SRA     D                   
2158: CB 1B           RR      E                   
215A: 7A              LD      A,D                 
215B: B3              OR      E                   
215C: 20 02           JR      NZ,$2160            ; 
215E: 1E 01           LD      E,$01               
2160: AF              XOR     A                   
2161: ED 52           SBC     HL,DE               
2163: C9              RET                         
2164: F5              PUSH    AF                  
2165: D5              PUSH    DE                  
2166: EB              EX      DE,HL               
2167: B7              OR      A                   
2168: CB 7A           BIT     7,D                 
216A: 20 0C           JR      NZ,$2178            ; 
216C: 21 BC 02        LD      HL,$02BC            
216F: ED 52           SBC     HL,DE               
2171: 30 0F           JR      NC,$2182            ; 
2173: 11 BC 02        LD      DE,$02BC            
2176: 18 0A           JR      $2182               ; 
2178: 21 44 FD        LD      HL,$FD44            
217B: ED 52           SBC     HL,DE               
217D: 38 03           JR      C,$2182             ; 
217F: 11 44 FD        LD      DE,$FD44            
2182: EB              EX      DE,HL               
2183: D1              POP     DE                  
2184: F1              POP     AF                  
2185: C9              RET                         
2186: 3A 67 40        LD      A,($4067)           ; 
2189: 07              RLCA                        
218A: E6 1E           AND     $1E                 
218C: 47              LD      B,A                 
218D: CD 06 29        CALL    $2906               ; 
2190: E6 2F           AND     $2F                 
2192: CB EF           SET     5,A                 
2194: 90              SUB     B                   
2195: 32 7C 40        LD      ($407C),A           ; 
2198: C9              RET                         
2199: DB 09           IN      A,($09)             ;
219B: DD 5E 00        LD      E,(IX+$00)          
219E: DD 56 01        LD      D,(IX+$01)          
21A1: DD E5           PUSH    IX                  
21A3: D5              PUSH    DE                  
21A4: DD E1           POP     IX                  
21A6: DD CB 00 7E     BIT     7,(IX+$00)          
21AA: 28 55           JR      Z,$2201             ; 
21AC: DD CB 01 6E     BIT     5,(IX+$01)          
21B0: 20 4F           JR      NZ,$2201            ; 
21B2: DD 7E 01        LD      A,(IX+$01)          
21B5: CB 4F           BIT     1,A                 
21B7: 20 07           JR      NZ,$21C0            ; 
21B9: FD AE 81        XOR     (IY+$81)            
21BC: CB 77           BIT     6,A                 
21BE: 28 41           JR      Z,$2201             ; 
21C0: DD 7E 07        LD      A,(IX+$07)          
21C3: FD 96 87        SUB     (IY+$87)            
21C6: 30 02           JR      NC,$21CA            ; 
21C8: ED 44           NEG                         
21CA: 57              LD      D,A                 
21CB: DD 7E 09        LD      A,(IX+$09)          
21CE: FD 96 89        SUB     (IY+$89)            
21D1: 30 02           JR      NC,$21D5            ; 
21D3: ED 44           NEG                         
21D5: 5F              LD      E,A                 
21D6: FD CB 81 66     BIT     4,(IY+$81)          
21DA: 28 09           JR      Z,$21E5             ; 
21DC: DD CB 00 66     BIT     4,(IX+$00)          
21E0: 28 03           JR      Z,$21E5             ; 
21E2: CD EC 24        CALL    $24EC               ; 
21E5: DD 7E 10        LD      A,(IX+$10)          
21E8: FD BE 90        CP      (IY+$90)            
21EB: 30 03           JR      NC,$21F0            ; 
21ED: FD 7E 90        LD      A,(IY+$90)          
21F0: BA              CP      D                   
21F1: 38 0E           JR      C,$2201             ; 
21F3: DD 7E 11        LD      A,(IX+$11)          
21F6: FD BE 91        CP      (IY+$91)            
21F9: 30 03           JR      NC,$21FE            ; 
21FB: FD 7E 91        LD      A,(IY+$91)          
21FE: BB              CP      E                   
21FF: 30 0F           JR      NC,$2210            ; 
2201: DD E1           POP     IX                  
2203: 11 06 00        LD      DE,$0006            
2206: DD 19           ADD     IX,DE               
2208: FD 34 FE        INC     (IY+$FE)            ;
220B: 10 8E           DJNZ    $219B               ; 
220D: C3 34 23        JP      $2334               ; 
2210: FD CB 81 76     BIT     6,(IY+$81)          
2214: 20 3D           JR      NZ,$2253            ; 
2216: DD CB 01 4E     BIT     1,(IX+$01)          
221A: 28 37           JR      Z,$2253             ; 
221C: FD CB 80 66     BIT     4,(IY+$80)          
2220: CA 4F 22        JP      Z,$224F             ; 
2223: 3A 0E 40        LD      A,($400E)           ; 
2226: B7              OR      A                   
2227: C2 4F 22        JP      NZ,$224F            ; 
222A: DD 36 0D 02     LD      (IX+$0D),$02        
222E: DD 36 11 06     LD      (IX+$11),$06        
2232: 21 AF CB        LD      HL,$CBAF            
2235: DD 74 16        LD      (IX+$16),H          
2238: DD 75 15        LD      (IX+$15),L          
223B: DD E1           POP     IX                  
223D: DD 56 05        LD      D,(IX+$05)          
2240: DD 5E 04        LD      E,(IX+$04)          
2243: D5              PUSH    DE                  
2244: DD E1           POP     IX                  
2246: DD 74 0B        LD      (IX+$0B),H          
2249: DD 75 0A        LD      (IX+$0A),L          
224C: C3 34 23        JP      $2334               ; 
224F: F1              POP     AF                  
2250: C3 34 23        JP      $2334               ; 
2253: F1              POP     AF                  
2254: DD CB 00 BE     RES     7,(IX+$00)          
2258: DD 36 13 00     LD      (IX+$13),$00        
225C: 3A 7D 40        LD      A,($407D)           ; 
225F: FE 0E           CP      $0E                 
2261: 38 17           JR      C,$227A             ; 
2263: 3A 7E 40        LD      A,($407E)           ; 
2266: FD BE FA        CP      (IY+$FA)            
2269: 28 05           JR      Z,$2270             ; 
226B: FD BE FB        CP      (IY+$FB)            
226E: 20 55           JR      NZ,$22C5            ; 
2270: 3E 04           LD      A,$04               
2272: DD CB 01 7E     BIT     7,(IX+$01)          
2276: 20 58           JR      NZ,$22D0            ; 
2278: 18 12           JR      $228C               ; 
227A: FD BE FA        CP      (IY+$FA)            
227D: 28 05           JR      Z,$2284             ; 
227F: FD BE FB        CP      (IY+$FB)            
2282: 20 41           JR      NZ,$22C5            ; 
2284: 3E 04           LD      A,$04               
2286: FD CB 81 7E     BIT     7,(IY+$81)          
228A: 20 44           JR      NZ,$22D0            ; 
228C: 3E 02           LD      A,$02               
228E: CD F6 2D        CALL    $2DF6               ; 
2291: 3E 05           LD      A,$05               
2293: FD CB F7 46     BIT     0,(IY+$F7)          
2297: 20 06           JR      NZ,$229F            ; 
2299: FD CB EA 46     BIT     0,(IY+$EA)          
229D: 20 31           JR      NZ,$22D0            ; 
229F: DD E5           PUSH    IX                  
22A1: DD 21 DD 41     LD      IX,$41DD            
22A5: DD CB 00 BE     RES     7,(IX+$00)          
22A9: DD 21 F4 41     LD      IX,$41F4            
22AD: DD CB 00 BE     RES     7,(IX+$00)          
22B1: DD 21 0B 42     LD      IX,$420B            
22B5: DD CB 00 BE     RES     7,(IX+$00)          
22B9: DD 21 22 42     LD      IX,$4222            
22BD: DD CB 00 BE     RES     7,(IX+$00)          
22C1: DD E1           POP     IX                  
22C3: 18 0B           JR      $22D0               ; 
22C5: 3A 0D 40        LD      A,($400D)           ; 
22C8: DD BE 0D        CP      (IX+$0D)            
22CB: 30 03           JR      NC,$22D0            ; 
22CD: DD 7E 0D        LD      A,(IX+$0D)          
22D0: 32 6F 40        LD      ($406F),A           ; 
22D3: B7              OR      A                   
22D4: C4 35 23        CALL    NZ,$2335            ; 
22D7: FD CB 81 46     BIT     0,(IY+$81)          
22DB: 28 0C           JR      Z,$22E9             ; 
22DD: DD 7E 07        LD      A,(IX+$07)          
22E0: 32 07 40        LD      ($4007),A           ; 
22E3: DD 7E 09        LD      A,(IX+$09)          
22E6: 32 09 40        LD      ($4009),A           ; 
22E9: 3E 00           LD      A,$00               
22EB: FD CB 80 66     BIT     4,(IY+$80)          
22EF: 28 02           JR      Z,$22F3             ; 
22F1: 3E 10           LD      A,$10               
22F3: CD BF 27        CALL    $27BF               ; 
22F6: FD 77 8B        LD      (IY+$8B),A          
22F9: 3A 7D 40        LD      A,($407D)           ; 
22FC: FE 01           CP      $01                 
22FE: 28 04           JR      Z,$2304             ; 
2300: FE 0E           CP      $0E                 
2302: 38 03           JR      C,$2307             ; 
2304: 3A 7E 40        LD      A,($407E)           ; 
2307: FD BE FA        CP      (IY+$FA)            
230A: 20 1A           JR      NZ,$2326            ; 
230C: FD 36 FA 00     LD      (IY+$FA),$00        
2310: FD 36 A2 07     LD      (IY+$A2),$07        
2314: FD 36 FC 05     LD      (IY+$FC),$05        
2318: FD CB EA 46     BIT     0,(IY+$EA)          
231C: 28 08           JR      Z,$2326             ; 
231E: FD 36 A2 02     LD      (IY+$A2),$02        
2322: FD 36 FC 02     LD      (IY+$FC),$02        
2326: FD BE FB        CP      (IY+$FB)            
2329: 20 04           JR      NZ,$232F            ; 
232B: FD 36 FB 00     LD      (IY+$FB),$00        
232F: FE 0E           CP      $0E                 
2331: DC 67 24        CALL    C,$2467             ; 
2334: C9              RET                         
2335: F5              PUSH    AF                  
2336: C5              PUSH    BC                  
2337: D5              PUSH    DE                  
2338: E5              PUSH    HL                  
2339: FD CB AE 7E     BIT     7,(IY+$AE)          
233D: CA 09 24        JP      Z,$2409             ; 
2340: 3D              DEC     A                   
2341: B7              OR      A                   
2342: 07              RLCA                        
2343: 5F              LD      E,A                 
2344: 16 00           LD      D,$00               
2346: 21 DB 2F        LD      HL,$2FDB            
2349: 19              ADD     HL,DE               
234A: 06 02           LD      B,$02               
234C: 11 36 40        LD      DE,$4036            
234F: AF              XOR     A                   
2350: 1A              LD      A,(DE)              
2351: 8E              ADC     A,(HL)              
2352: 27              DAA                         
2353: 12              LD      (DE),A              
2354: 23              INC     HL                  
2355: 13              INC     DE                  
2356: 10 F8           DJNZ    $2350               ; 
2358: 06 02           LD      B,$02               
235A: 1A              LD      A,(DE)              
235B: CE 00           ADC     A,$00               
235D: 27              DAA                         
235E: 12              LD      (DE),A              
235F: 13              INC     DE                  
2360: 10 F8           DJNZ    $235A               ; 
2362: 06 04           LD      B,$04               
2364: 11 39 40        LD      DE,$4039            
2367: 21 17 46        LD      HL,$4617            
236A: CD 0E 24        CALL    $240E               ; 
236D: ED 5B 60 40     LD      DE,($4060)          ; 
2371: 2A 38 40        LD      HL,($4038)          ; 
2374: B7              OR      A                   
2375: ED 52           SBC     HL,DE               
2377: DA 09 24        JP      C,$2409             ; 
237A: FD CB EA 6E     BIT     5,(IY+$EA)          
237E: 20 19           JR      NZ,$2399            ; 
2380: FD CB EA EE     SET     5,(IY+$EA)          
2384: 21 07 00        LD      HL,$0007            
2387: 11 FC 0D        LD      DE,$0DFC            
238A: 19              ADD     HL,DE               
238B: 7C              LD      A,H                 
238C: E6 0F           AND     $0F                 
238E: F6 C0           OR      $C0                 
2390: 67              LD      H,A                 
2391: CD 54 18        CALL    $1854               ; 
2394: 22 A6 82        LD      ($82A6),HL          ; 
2397: 18 54           JR      $23ED               ; 
2399: ED 5B 62 40     LD      DE,($4062)          ; 
239D: 2A 38 40        LD      HL,($4038)          ; 
23A0: B7              OR      A                   
23A1: ED 52           SBC     HL,DE               
23A3: 38 64           JR      C,$2409             ; 
23A5: FD CB EA 66     BIT     4,(IY+$EA)          
23A9: 20 19           JR      NZ,$23C4            ; 
23AB: FD CB EA E6     SET     4,(IY+$EA)          
23AF: 21 07 00        LD      HL,$0007            
23B2: 11 FC 0D        LD      DE,$0DFC            
23B5: 19              ADD     HL,DE               
23B6: 7C              LD      A,H                 
23B7: E6 0F           AND     $0F                 
23B9: F6 C0           OR      $C0                 
23BB: 67              LD      H,A                 
23BC: CD 54 18        CALL    $1854               ; 
23BF: 22 B0 82        LD      ($82B0),HL          ; 
23C2: 18 29           JR      $23ED               ; 
23C4: ED 5B 64 40     LD      DE,($4064)          ; 
23C8: 2A 38 40        LD      HL,($4038)          ; 
23CB: B7              OR      A                   
23CC: ED 52           SBC     HL,DE               
23CE: 38 39           JR      C,$2409             ; 
23D0: FD CB EA 5E     BIT     3,(IY+$EA)          
23D4: 20 33           JR      NZ,$2409            ; 
23D6: FD CB EA DE     SET     3,(IY+$EA)          
23DA: 21 07 00        LD      HL,$0007            
23DD: 11 FC 0D        LD      DE,$0DFC            
23E0: 19              ADD     HL,DE               
23E1: 7C              LD      A,H                 
23E2: E6 0F           AND     $0F                 
23E4: F6 C0           OR      $C0                 
23E6: 67              LD      H,A                 
23E7: CD 54 18        CALL    $1854               ; 
23EA: 22 BA 82        LD      ($82BA),HL          ; 
23ED: 3E 00           LD      A,$00               
23EF: CD 04 2E        CALL    $2E04               ; 
23F2: FD 36 A1 00     LD      (IY+$A1),$00        
23F6: 3E 14           LD      A,$14               
23F8: CD 04 2E        CALL    $2E04               ; 
23FB: FD 36 A1 03     LD      (IY+$A1),$03        
23FF: FD 36 E9 FF     LD      (IY+$E9),$FF        
2403: FD 34 E6        INC     (IY+$E6)            ;
2406: FD 34 ED        INC     (IY+$ED)            ;
2409: E1              POP     HL                  
240A: D1              POP     DE                  
240B: C1              POP     BC                  
240C: F1              POP     AF                  
240D: C9              RET                         
240E: FD 36 11 FF     LD      (IY+$11),$FF        
2412: 1A              LD      A,(DE)              
2413: 0F              RRCA                        
2414: 0F              RRCA                        
2415: 0F              RRCA                        
2416: 0F              RRCA                        
2417: E6 0F           AND     $0F                 
2419: 20 0A           JR      NZ,$2425            ; 
241B: FD CB 11 7E     BIT     7,(IY+$11)          
241F: 28 04           JR      Z,$2425             ; 
2421: 3E 0A           LD      A,$0A               
2423: 18 04           JR      $2429               ; 
2425: FD 36 11 00     LD      (IY+$11),$00        
2429: CD 4A 24        CALL    $244A               ; 
242C: 1A              LD      A,(DE)              
242D: E6 0F           AND     $0F                 
242F: 20 0E           JR      NZ,$243F            ; 
2431: FD CB 11 7E     BIT     7,(IY+$11)          
2435: 28 0C           JR      Z,$2443             ; 
2437: 78              LD      A,B                 
2438: 3D              DEC     A                   
2439: 28 08           JR      Z,$2443             ; 
243B: 3E 0A           LD      A,$0A               
243D: 18 04           JR      $2443               ; 
243F: FD 36 11 00     LD      (IY+$11),$00        
2443: CD 4A 24        CALL    $244A               ; 
2446: 1B              DEC     DE                  
2447: 10 C9           DJNZ    $2412               ; 
2449: C9              RET                         
244A: D5              PUSH    DE                  
244B: DD E5           PUSH    IX                  
244D: E6 0F           AND     $0F                 
244F: 07              RLCA                        
2450: 5F              LD      E,A                 
2451: 16 00           LD      D,$00               
2453: DD 21 D5 3F     LD      IX,$3FD5            
2457: DD 19           ADD     IX,DE               
2459: DD 7E 00        LD      A,(IX+$00)          
245C: 77              LD      (HL),A              
245D: 23              INC     HL                  
245E: DD 7E 01        LD      A,(IX+$01)          
2461: 77              LD      (HL),A              
2462: 23              INC     HL                  
2463: DD E1           POP     IX                  
2465: D1              POP     DE                  
2466: C9              RET                         
2467: F5              PUSH    AF                  
2468: C5              PUSH    BC                  
2469: D5              PUSH    DE                  
246A: E5              PUSH    HL                  
246B: DD E5           PUSH    IX                  
246D: FD 46 E7        LD      B,(IY+$E7)          
2470: 0E 02           LD      C,$02               
2472: 21 96 2E        LD      HL,$2E96            
2475: 5E              LD      E,(HL)              
2476: 23              INC     HL                  
2477: 56              LD      D,(HL)              
2478: 1A              LD      A,(DE)              
2479: CB 7F           BIT     7,A                 
247B: 28 30           JR      Z,$24AD             ; 
247D: 13              INC     DE                  
247E: 1A              LD      A,(DE)              
247F: 1B              DEC     DE                  
2480: CB 6F           BIT     5,A                 
2482: 20 29           JR      NZ,$24AD            ; 
2484: 0D              DEC     C                   
2485: 28 5A           JR      Z,$24E1             ; 
2487: 3A 7B 40        LD      A,($407B)           ; 
248A: B7              OR      A                   
248B: 20 20           JR      NZ,$24AD            ; 
248D: 3A 77 40        LD      A,($4077)           ; 
2490: FE 01           CP      $01                 
2492: 28 19           JR      Z,$24AD             ; 
2494: 78              LD      A,B                 
2495: ED 44           NEG                         
2497: FD 86 E7        ADD     A,(IY+$E7)          
249A: C6 02           ADD     A,$02               
249C: FD BE FA        CP      (IY+$FA)            
249F: 28 0C           JR      Z,$24AD             ; 
24A1: 32 7B 40        LD      ($407B),A           ; 
24A4: D5              PUSH    DE                  
24A5: DD E1           POP     IX                  
24A7: DD 7E 0A        LD      A,(IX+$0A)          
24AA: DD 77 0F        LD      (IX+$0F),A          
24AD: 11 05 00        LD      DE,$0005            
24B0: 19              ADD     HL,DE               
24B1: 10 C2           DJNZ    $2475               ; 
24B3: CB 41           BIT     0,C                 
24B5: 20 0A           JR      NZ,$24C1            ; 
24B7: FD CB EB F6     SET     6,(IY+$EB)          
24BB: FD 36 F7 00     LD      (IY+$F7),$00        
24BF: 18 24           JR      $24E5               ; 
24C1: FD 36 F7 01     LD      (IY+$F7),$01        
24C5: 3A 67 40        LD      A,($4067)           ; 
24C8: FE 0C           CP      $0C                 
24CA: 38 08           JR      C,$24D4             ; 
24CC: FD 36 A2 02     LD      (IY+$A2),$02        
24D0: FD 36 FC 02     LD      (IY+$FC),$02        
24D4: 3A 3B 40        LD      A,($403B)           ; 
24D7: FE 03           CP      $03                 
24D9: 38 0A           JR      C,$24E5             ; 
24DB: FD CB EA C6     SET     0,(IY+$EA)          
24DF: 18 04           JR      $24E5               ; 
24E1: FD 36 F7 02     LD      (IY+$F7),$02        
24E5: DD E1           POP     IX                  
24E7: E1              POP     HL                  
24E8: D1              POP     DE                  
24E9: C1              POP     BC                  
24EA: F1              POP     AF                  
24EB: C9              RET                         
24EC: D5              PUSH    DE                  
24ED: CD AA 25        CALL    $25AA               ; 
24F0: EB              EX      DE,HL               
24F1: 2A 80 40        LD      HL,($4080)          ; 
24F4: B7              OR      A                   
24F5: ED 52           SBC     HL,DE               
24F7: 38 34           JR      C,$252D             ; 
24F9: 78              LD      A,B                 
24FA: ED 44           NEG                         
24FC: C6 21           ADD     A,$21               
24FE: FD BE FB        CP      (IY+$FB)            
2501: 20 0D           JR      NZ,$2510            ; 
2503: 08              EX      AF,AF'              
2504: 3A 77 40        LD      A,($4077)           ; 
2507: FE 02           CP      $02                 
2509: 30 22           JR      NC,$252D            ; 
250B: 08              EX      AF,AF'              
250C: FD 36 FB 00     LD      (IY+$FB),$00        
2510: ED 53 80 40     LD      ($4080),DE          ; 
2514: 32 7A 40        LD      ($407A),A           ; 
2517: 3A 77 40        LD      A,($4077)           ; 
251A: FE 01           CP      $01                 
251C: 20 0F           JR      NZ,$252D            ; 
251E: DD CB 00 8E     RES     1,(IX+$00)          
2522: CD 06 29        CALL    $2906               ; 
2525: CB 67           BIT     4,A                 
2527: 28 04           JR      Z,$252D             ; 
2529: DD CB 00 CE     SET     1,(IX+$00)          
252D: D1              POP     DE                  
252E: C9              RET                         
252F: 3A B9 40        LD      A,($40B9)           ; 
2532: FD 96 87        SUB     (IY+$87)            
2535: 06 00           LD      B,$00               
2537: 30 04           JR      NC,$253D            ; 
2539: ED 44           NEG                         
253B: 06 FF           LD      B,$FF               
253D: 57              LD      D,A                 
253E: 3A BB 40        LD      A,($40BB)           ; 
2541: FD 96 89        SUB     (IY+$89)            
2544: 0E 00           LD      C,$00               
2546: 30 04           JR      NC,$254C            ; 
2548: ED 44           NEG                         
254A: 0E FF           LD      C,$FF               
254C: 5F              LD      E,A                 
254D: CD C1 25        CALL    $25C1               ; 
2550: DD E5           PUSH    IX                  
2552: 3E 0F           LD      A,$0F               
2554: EB              EX      DE,HL               
2555: DD 21 41 30     LD      IX,$3041            
2559: DD 6E 00        LD      L,(IX+$00)          
255C: DD 23           INC     IX                  
255E: DD 66 00        LD      H,(IX+$00)          
2561: DD 23           INC     IX                  
2563: B7              OR      A                   
2564: ED 52           SBC     HL,DE               
2566: 38 03           JR      C,$256B             ; 
2568: 3D              DEC     A                   
2569: 20 EE           JR      NZ,$2559            ; 
256B: DD E1           POP     IX                  
256D: CB 78           BIT     7,B                 
256F: 20 0A           JR      NZ,$257B            ; 
2571: CB 79           BIT     7,C                 
2573: 28 12           JR      Z,$2587             ; 
2575: EE 0F           XOR     $0F                 
2577: C6 30           ADD     A,$30               
2579: 18 0C           JR      $2587               ; 
257B: CB 79           BIT     7,C                 
257D: 28 04           JR      Z,$2583             ; 
257F: C6 20           ADD     A,$20               
2581: 18 04           JR      $2587               ; 
2583: EE 0F           XOR     $0F                 
2585: C6 10           ADD     A,$10               
2587: 47              LD      B,A                 
2588: 3A 0F 40        LD      A,($400F)           ; 
258B: E6 3F           AND     $3F                 
258D: 4F              LD      C,A                 
258E: 90              SUB     B                   
258F: 28 14           JR      Z,$25A5             ; 
2591: 38 06           JR      C,$2599             ; 
2593: FE 20           CP      $20                 
2595: 30 0A           JR      NC,$25A1            ; 
2597: 18 04           JR      $259D               ; 
2599: FE E0           CP      $E0                 
259B: 30 04           JR      NC,$25A1            ; 
259D: 79              LD      A,C                 
259E: 3D              DEC     A                   
259F: 18 05           JR      $25A6               ; 
25A1: 79              LD      A,C                 
25A2: 3C              INC     A                   
25A3: 18 01           JR      $25A6               ; 
25A5: 79              LD      A,C                 
25A6: 32 0F 40        LD      ($400F),A           ; 
25A9: C9              RET                         
25AA: C5              PUSH    BC                  
25AB: D5              PUSH    DE                  
25AC: 7A              LD      A,D                 
25AD: 16 00           LD      D,$00               
25AF: 06 08           LD      B,$08               
25B1: 21 00 00        LD      HL,$0000            
25B4: 0F              RRCA                        
25B5: 30 01           JR      NC,$25B8            ; 
25B7: 19              ADD     HL,DE               
25B8: CB 23           SLA     E                   
25BA: CB 12           RL      D                   
25BC: 10 F6           DJNZ    $25B4               ; 
25BE: D1              POP     DE                  
25BF: C1              POP     BC                  
25C0: C9              RET                         
25C1: C5              PUSH    BC                  
25C2: D5              PUSH    DE                  
25C3: D5              PUSH    DE                  
25C4: 43              LD      B,E                 
25C5: 0E 00           LD      C,$00               
25C7: 7A              LD      A,D                 
25C8: 2F              CPL                         
25C9: 5F              LD      E,A                 
25CA: 16 FF           LD      D,$FF               
25CC: 13              INC     DE                  
25CD: 21 00 00        LD      HL,$0000            
25D0: 3E 11           LD      A,$11               
25D2: E5              PUSH    HL                  
25D3: 19              ADD     HL,DE               
25D4: 30 01           JR      NC,$25D7            ; 
25D6: E3              EX      (SP),HL             
25D7: E1              POP     HL                  
25D8: F5              PUSH    AF                  
25D9: CB 11           RL      C                   
25DB: CB 10           RL      B                   
25DD: CB 15           RL      L                   
25DF: CB 14           RL      H                   
25E1: F1              POP     AF                  
25E2: 3D              DEC     A                   
25E3: 20 ED           JR      NZ,$25D2            ; 
25E5: 60              LD      H,B                 
25E6: 69              LD      L,C                 
25E7: D1              POP     DE                  
25E8: D1              POP     DE                  
25E9: C1              POP     BC                  
25EA: C9              RET                         
25EB: DD E5           PUSH    IX                  
25ED: 0E 04           LD      C,$04               
25EF: FD CB 81 76     BIT     6,(IY+$81)          
25F3: 28 07           JR      Z,$25FC             ; 
25F5: 06 08           LD      B,$08               
25F7: 21 09 2F        LD      HL,$2F09            
25FA: 18 05           JR      $2601               ; 
25FC: 06 04           LD      B,$04               
25FE: 21 F1 2E        LD      HL,$2EF1            
2601: 56              LD      D,(HL)              
2602: 2B              DEC     HL                  
2603: 5E              LD      E,(HL)              
2604: 1A              LD      A,(DE)              
2605: CB 7F           BIT     7,A                 
2607: 28 0B           JR      Z,$2614             ; 
2609: 11 FB FF        LD      DE,$FFFB            
260C: 19              ADD     HL,DE               
260D: 05              DEC     B                   
260E: 0D              DEC     C                   
260F: 20 F0           JR      NZ,$2601            ; 
2611: C3 51 27        JP      $2751               ; 
2614: D5              PUSH    DE                  
2615: DD E1           POP     IX                  
2617: 78              LD      A,B                 
2618: C6 0D           ADD     A,$0D               
261A: 47              LD      B,A                 
261B: CD 1D 29        CALL    $291D               ; 
261E: FD 7E 86        LD      A,(IY+$86)          
2621: DD 77 06        LD      (IX+$06),A          
2624: FD 7E 87        LD      A,(IY+$87)          
2627: DD 77 07        LD      (IX+$07),A          
262A: FD 7E 88        LD      A,(IY+$88)          
262D: DD 77 08        LD      (IX+$08),A          
2630: FD 7E 89        LD      A,(IY+$89)          
2633: DD 77 09        LD      (IX+$09),A          
2636: FD 7E 8F        LD      A,(IY+$8F)          
2639: DD 77 0F        LD      (IX+$0F),A          
263C: FD CB 81 76     BIT     6,(IY+$81)          
2640: 28 04           JR      Z,$2646             ; 
2642: DD CB 01 F6     SET     6,(IX+$01)          
2646: DD 7E 0F        LD      A,(IX+$0F)          
2649: CB 67           BIT     4,A                 
264B: 28 02           JR      Z,$264F             ; 
264D: EE 0F           XOR     $0F                 
264F: E6 0F           AND     $0F                 
2651: 07              RLCA                        
2652: 21 21 30        LD      HL,$3021            
2655: 5F              LD      E,A                 
2656: 16 00           LD      D,$00               
2658: 19              ADD     HL,DE               
2659: 5E              LD      E,(HL)              
265A: 7B              LD      A,E                 
265B: CB 2F           SRA     A                   
265D: CB 2F           SRA     A                   
265F: DD 77 11        LD      (IX+$11),A          
2662: 23              INC     HL                  
2663: 4E              LD      C,(HL)              
2664: 79              LD      A,C                 
2665: CB 2F           SRA     A                   
2667: CB 2F           SRA     A                   
2669: DD 77 10        LD      (IX+$10),A          
266C: 06 00           LD      B,$00               
266E: 16 00           LD      D,$00               
2670: DD 7E 0F        LD      A,(IX+$0F)          
2673: E6 30           AND     $30                 
2675: 28 09           JR      Z,$2680             ; 
2677: FE 30           CP      $30                 
2679: 28 05           JR      Z,$2680             ; 
267B: 79              LD      A,C                 
267C: 2F              CPL                         
267D: 4F              LD      C,A                 
267E: 06 FF           LD      B,$FF               
2680: DD 7E 0F        LD      A,(IX+$0F)          
2683: CB 6F           BIT     5,A                 
2685: 28 05           JR      Z,$268C             ; 
2687: 7B              LD      A,E                 
2688: 2F              CPL                         
2689: 5F              LD      E,A                 
268A: 16 FF           LD      D,$FF               
268C: FD CB 81 76     BIT     6,(IY+$81)          
2690: 28 22           JR      Z,$26B4             ; 
2692: 79              LD      A,C                 
2693: CB 2F           SRA     A                   
2695: CB 2F           SRA     A                   
2697: DD 86 07        ADD     A,(IX+$07)          
269A: CB 78           BIT     7,B                 
269C: 20 04           JR      NZ,$26A2            ; 
269E: 38 07           JR      C,$26A7             ; 
26A0: 18 02           JR      $26A4               ; 
26A2: 30 03           JR      NC,$26A7            ; 
26A4: DD 77 07        LD      (IX+$07),A          
26A7: 7B              LD      A,E                 
26A8: CB 2F           SRA     A                   
26AA: CB 2F           SRA     A                   
26AC: DD 86 09        ADD     A,(IX+$09)          
26AF: DD 77 09        LD      (IX+$09),A          
26B2: 18 22           JR      $26D6               ; 
26B4: DD 36 0C 19     LD      (IX+$0C),$19        
26B8: 3A 0F 40        LD      A,($400F)           ; 
26BB: FD 96 8A        SUB     (IY+$8A)            
26BE: 30 02           JR      NC,$26C2            ; 
26C0: ED 44           NEG                         
26C2: FE 10           CP      $10                 
26C4: 38 04           JR      C,$26CA             ; 
26C6: FE 30           CP      $30                 
26C8: 38 15           JR      C,$26DF             ; 
26CA: FD CB EA 7E     BIT     7,(IY+$EA)          
26CE: 28 0F           JR      Z,$26DF             ; 
26D0: DD CB 00 D6     SET     2,(IX+$00)          
26D4: 18 09           JR      $26DF               ; 
26D6: 3E 07           LD      A,$07               
26D8: CD 04 2E        CALL    $2E04               ; 
26DB: DD CB 00 D6     SET     2,(IX+$00)          
26DF: 21 00 00        LD      HL,$0000            
26E2: 09              ADD     HL,BC               
26E3: 29              ADD     HL,HL               
26E4: 29              ADD     HL,HL               
26E5: 29              ADD     HL,HL               
26E6: 29              ADD     HL,HL               
26E7: 29              ADD     HL,HL               
26E8: DD CB 00 56     BIT     2,(IX+$00)          
26EC: 28 03           JR      Z,$26F1             ; 
26EE: 29              ADD     HL,HL               
26EF: 18 12           JR      $2703               ; 
26F1: 3A 67 40        LD      A,($4067)           ; 
26F4: FD CB EB 5E     BIT     3,(IY+$EB)          
26F8: 20 02           JR      NZ,$26FC            ; 
26FA: D6 03           SUB     $03                 
26FC: 09              ADD     HL,BC               
26FD: 09              ADD     HL,BC               
26FE: 09              ADD     HL,BC               
26FF: 09              ADD     HL,BC               
2700: 3D              DEC     A                   
2701: 20 F9           JR      NZ,$26FC            ; 
2703: DD 74 03        LD      (IX+$03),H          
2706: DD 75 02        LD      (IX+$02),L          
2709: 21 00 00        LD      HL,$0000            
270C: 19              ADD     HL,DE               
270D: 29              ADD     HL,HL               
270E: 29              ADD     HL,HL               
270F: 29              ADD     HL,HL               
2710: 29              ADD     HL,HL               
2711: 29              ADD     HL,HL               
2712: DD CB 00 56     BIT     2,(IX+$00)          
2716: 28 03           JR      Z,$271B             ; 
2718: 29              ADD     HL,HL               
2719: 18 12           JR      $272D               ; 
271B: 3A 67 40        LD      A,($4067)           ; 
271E: FD CB EB 5E     BIT     3,(IY+$EB)          
2722: 20 02           JR      NZ,$2726            ; 
2724: D6 03           SUB     $03                 
2726: 19              ADD     HL,DE               
2727: 19              ADD     HL,DE               
2728: 19              ADD     HL,DE               
2729: 19              ADD     HL,DE               
272A: 3D              DEC     A                   
272B: 20 F9           JR      NZ,$2726            ; 
272D: DD CB 00 96     RES     2,(IX+$00)          
2731: DD 74 05        LD      (IX+$05),H          
2734: DD 75 04        LD      (IX+$04),L          
2737: 3A 0F 40        LD      A,($400F)           ; 
273A: E6 3F           AND     $3F                 
273C: 5F              LD      E,A                 
273D: 83              ADD     A,E                 
273E: 83              ADD     A,E                 
273F: 5F              LD      E,A                 
2740: 16 00           LD      D,$00               
2742: 21 E7 0A        LD      HL,$0AE7            
2745: 19              ADD     HL,DE               
2746: 7C              LD      A,H                 
2747: E6 0F           AND     $0F                 
2749: F6 C0           OR      $C0                 
274B: DD 77 16        LD      (IX+$16),A          
274E: DD 75 15        LD      (IX+$15),L          
2751: FD CB 80 96     RES     2,(IY+$80)          
2755: DD E1           POP     IX                  
2757: C9              RET                         
2758: DD E5           PUSH    IX                  
275A: FD 56 87        LD      D,(IY+$87)          
275D: FD 5E 89        LD      E,(IY+$89)          
2760: 7B              LD      A,E                 
2761: FE A0           CP      $A0                 
2763: 38 09           JR      C,$276E             ; 
2765: 7A              LD      A,D                 
2766: FE 10           CP      $10                 
2768: 38 52           JR      C,$27BC             ; 
276A: FE F0           CP      $F0                 
276C: 30 4E           JR      NC,$27BC            ; 
276E: 7A              LD      A,D                 
276F: FE 26           CP      $26                 
2771: 38 0D           JR      C,$2780             ; 
2773: FE DA           CP      $DA                 
2775: 30 09           JR      NC,$2780            ; 
2777: 7B              LD      A,E                 
2778: FE 56           CP      $56                 
277A: 38 04           JR      C,$2780             ; 
277C: FE AA           CP      $AA                 
277E: 38 3C           JR      C,$27BC             ; 
2780: 0E 0C           LD      C,$0C               
2782: 06 0B           LD      B,$0B               
2784: 21 4B 2F        LD      HL,$2F4B            
2787: 56              LD      D,(HL)              
2788: 2B              DEC     HL                  
2789: 5E              LD      E,(HL)              
278A: 1A              LD      A,(DE)              
278B: CB 7F           BIT     7,A                 
278D: 28 17           JR      Z,$27A6             ; 
278F: 0D              DEC     C                   
2790: 28 14           JR      Z,$27A6             ; 
2792: 11 FB FF        LD      DE,$FFFB            
2795: 19              ADD     HL,DE               
2796: 10 EF           DJNZ    $2787               ; 
2798: CD 06 29        CALL    $2906               ; 
279B: E6 0F           AND     $0F                 
279D: 28 F9           JR      Z,$2798             ; 
279F: FE 0B           CP      $0B                 
27A1: 30 F5           JR      NC,$2798            ; 
27A3: 4F              LD      C,A                 
27A4: 18 DC           JR      $2782               ; 
27A6: D5              PUSH    DE                  
27A7: DD E1           POP     IX                  
27A9: 3E 15           LD      A,$15               
27AB: 80              ADD     A,B                 
27AC: 47              LD      B,A                 
27AD: CD 1D 29        CALL    $291D               ; 
27B0: 3A 07 40        LD      A,($4007)           ; 
27B3: DD 77 07        LD      (IX+$07),A          
27B6: 3A 09 40        LD      A,($4009)           ; 
27B9: DD 77 09        LD      (IX+$09),A          
27BC: DD E1           POP     IX                  
27BE: C9              RET                         
27BF: F5              PUSH    AF                  
27C0: 3A 00 40        LD      A,($4000)           ; 
27C3: FD 66 87        LD      H,(IY+$87)          
27C6: FD 6E 89        LD      L,(IY+$89)          
27C9: E5              PUSH    HL                  
27CA: 01 17 00        LD      BC,$0017            
27CD: 11 00 40        LD      DE,$4000            
27D0: 21 AC 2F        LD      HL,$2FAC            
27D3: ED B0           LDIR                        
27D5: E1              POP     HL                  
27D6: FD 74 87        LD      (IY+$87),H          
27D9: FD 75 89        LD      (IY+$89),L          
27DC: 3A 7D 40        LD      A,($407D)           ; 
27DF: FE 0E           CP      $0E                 
27E1: 38 07           JR      C,$27EA             ; 
27E3: FE 16           CP      $16                 
27E5: 30 03           JR      NC,$27EA            ; 
27E7: 3A 7E 40        LD      A,($407E)           ; 
27EA: FE 16           CP      $16                 
27EC: 30 41           JR      NC,$282F            ; 
27EE: FE 0E           CP      $0E                 
27F0: 30 4B           JR      NC,$283D            ; 
27F2: FE 02           CP      $02                 
27F4: 30 23           JR      NC,$2819            ; 
27F6: 3A 66 40        LD      A,($4066)           ; 
27F9: FE 01           CP      $01                 
27FB: 20 04           JR      NZ,$2801            ; 
27FD: FD 36 A2 0A     LD      (IY+$A2),$0A        
2801: FD 36 A1 00     LD      (IY+$A1),$00        
2805: 3E 00           LD      A,$00               
2807: CD 04 2E        CALL    $2E04               ; 
280A: FD 36 8C 0F     LD      (IY+$8C),$0F        
280E: 3E 01           LD      A,$01               
2810: CD 04 2E        CALL    $2E04               ; 
2813: FD 36 A1 05     LD      (IY+$A1),$05        
2817: 18 24           JR      $283D               ; 
2819: 3A 6F 40        LD      A,($406F)           ; 
281C: FE 03           CP      $03                 
281E: 3E 02           LD      A,$02               
2820: 28 18           JR      Z,$283A             ; 
2822: 3A 6F 40        LD      A,($406F)           ; 
2825: FE 04           CP      $04                 
2827: 3E 10           LD      A,$10               
2829: 28 0F           JR      Z,$283A             ; 
282B: 3E 15           LD      A,$15               
282D: 18 0B           JR      $283A               ; 
282F: 3A 6F 40        LD      A,($406F)           ; 
2832: FE 01           CP      $01                 
2834: 3E 03           LD      A,$03               
2836: 28 02           JR      Z,$283A             ; 
2838: 3E 11           LD      A,$11               
283A: CD 04 2E        CALL    $2E04               ; 
283D: F1              POP     AF                  
283E: C9              RET                         
283F: FD 56 87        LD      D,(IY+$87)          
2842: FD 5E 89        LD      E,(IY+$89)          
2845: FD CB 80 4E     BIT     1,(IY+$80)          
2849: C2 76 28        JP      NZ,$2876            ; 
284C: CB 7A           BIT     7,D                 
284E: 20 06           JR      NZ,$2856            ; 
2850: CB 7B           BIT     7,E                 
2852: 20 0D           JR      NZ,$2861            ; 
2854: 18 12           JR      $2868               ; 
2856: CB 7B           BIT     7,E                 
2858: 28 15           JR      Z,$286F             ; 
285A: 21 30 3E        LD      HL,$3E30            
285D: 0E 00           LD      C,$00               
285F: 18 3D           JR      $289E               ; 
2861: 21 00 0E        LD      HL,$0E00            
2864: 0E 01           LD      C,$01               
2866: 18 36           JR      $289E               ; 
2868: 21 10 1E        LD      HL,$1E10            
286B: 0E 00           LD      C,$00               
286D: 18 2F           JR      $289E               ; 
286F: 21 20 2E        LD      HL,$2E20            
2872: 0E 01           LD      C,$01               
2874: 18 28           JR      $289E               ; 
2876: CB 7A           BIT     7,D                 
2878: 20 06           JR      NZ,$2880            ; 
287A: CB 7B           BIT     7,E                 
287C: 20 0D           JR      NZ,$288B            ; 
287E: 18 12           JR      $2892               ; 
2880: CB 7B           BIT     7,E                 
2882: 28 15           JR      Z,$2899             ; 
2884: 21 20 12        LD      HL,$1220            
2887: 0E 01           LD      C,$01               
2889: 18 13           JR      $289E               ; 
288B: 21 30 22        LD      HL,$2230            
288E: 0E 00           LD      C,$00               
2890: 18 0C           JR      $289E               ; 
2892: 21 00 32        LD      HL,$3200            
2895: 0E 01           LD      C,$01               
2897: 18 05           JR      $289E               ; 
2899: 21 10 02        LD      HL,$0210            
289C: 0E 00           LD      C,$00               
289E: 7A              LD      A,D                 
289F: D6 80           SUB     $80                 
28A1: 30 02           JR      NC,$28A5            ; 
28A3: ED 44           NEG                         
28A5: 57              LD      D,A                 
28A6: 7B              LD      A,E                 
28A7: D6 80           SUB     $80                 
28A9: 30 02           JR      NC,$28AD            ; 
28AB: ED 44           NEG                         
28AD: 5F              LD      E,A                 
28AE: CB 41           BIT     0,C                 
28B0: 28 14           JR      Z,$28C6             ; 
28B2: 7A              LD      A,D                 
28B3: FE 58           CP      $58                 
28B5: 30 07           JR      NC,$28BE            ; 
28B7: 7B              LD      A,E                 
28B8: FE 21           CP      $21                 
28BA: 38 2D           JR      C,$28E9             ; 
28BC: 18 2A           JR      $28E8               ; 
28BE: 7A              LD      A,D                 
28BF: D6 40           SUB     $40                 
28C1: BB              CP      E                   
28C2: 38 24           JR      C,$28E8             ; 
28C4: 18 23           JR      $28E9               ; 
28C6: 7A              LD      A,D                 
28C7: FE 21           CP      $21                 
28C9: 38 1E           JR      C,$28E9             ; 
28CB: FE 68           CP      $68                 
28CD: 30 19           JR      NC,$28E8            ; 
28CF: 7B              LD      A,E                 
28D0: FE 30           CP      $30                 
28D2: 38 08           JR      C,$28DC             ; 
28D4: 7A              LD      A,D                 
28D5: D6 10           SUB     $10                 
28D7: BB              CP      E                   
28D8: 38 0F           JR      C,$28E9             ; 
28DA: 18 0C           JR      $28E8               ; 
28DC: 7A              LD      A,D                 
28DD: FE 53           CP      $53                 
28DF: 30 07           JR      NC,$28E8            ; 
28E1: ED 44           NEG                         
28E3: C6 70           ADD     A,$70               
28E5: BB              CP      E                   
28E6: 30 01           JR      NC,$28E9            ; 
28E8: 65              LD      H,L                 
28E9: 3A 0A 40        LD      A,($400A)           ; 
28EC: E6 3F           AND     $3F                 
28EE: 4F              LD      C,A                 
28EF: 94              SUB     H                   
28F0: 28 10           JR      Z,$2902             ; 
28F2: 38 06           JR      C,$28FA             ; 
28F4: FE 20           CP      $20                 
28F6: 30 09           JR      NC,$2901            ; 
28F8: 18 04           JR      $28FE               ; 
28FA: FE E0           CP      $E0                 
28FC: 30 03           JR      NC,$2901            ; 
28FE: 0D              DEC     C                   
28FF: 18 01           JR      $2902               ; 
2901: 0C              INC     C                   
2902: FD 71 8A        LD      (IY+$8A),C          
2905: C9              RET                         
2906: FD 86 F3        ADD     A,(IY+$F3)          
2909: 32 73 40        LD      ($4073),A           ; 
290C: DB 09           IN      A,($09)             ;
290E: ED 5F           LD      A,R                 
2910: FD 86 F3        ADD     A,(IY+$F3)          
2913: 07              RLCA                        
2914: 07              RLCA                        
2915: 07              RLCA                        
2916: FD 96 97        SUB     (IY+$97)            
2919: 32 73 40        LD      ($4073),A           ; 
291C: C9              RET                         
291D: F5              PUSH    AF                  
291E: C5              PUSH    BC                  
291F: D5              PUSH    DE                  
2920: E5              PUSH    HL                  
2921: DD E5           PUSH    IX                  
2923: C5              PUSH    BC                  
2924: CB 20           SLA     B                   
2926: 78              LD      A,B                 
2927: 80              ADD     A,B                 
2928: 80              ADD     A,B                 
2929: 4F              LD      C,A                 
292A: 06 00           LD      B,$00               
292C: DD 21 8A 2E     LD      IX,$2E8A            
2930: DD 09           ADD     IX,BC               
2932: DD 5E 00        LD      E,(IX+$00)          
2935: DD 56 01        LD      D,(IX+$01)          
2938: D5              PUSH    DE                  
2939: DD 6E 02        LD      L,(IX+$02)          
293C: DD 66 03        LD      H,(IX+$03)          
293F: 01 17 00        LD      BC,$0017            
2942: ED B0           LDIR                        
2944: DD E1           POP     IX                  
2946: C1              POP     BC                  
2947: DD 70 13        LD      (IX+$13),B          
294A: 78              LD      A,B                 
294B: FE 0E           CP      $0E                 
294D: 30 5C           JR      NC,$29AB            ; 
294F: 05              DEC     B                   
2950: 20 1C           JR      NZ,$296E            ; 
2952: CD 06 29        CALL    $2906               ; 
2955: E6 0F           AND     $0F                 
2957: F6 B0           OR      $B0                 
2959: DD 77 09        LD      (IX+$09),A          
295C: FD CB F9 7E     BIT     7,(IY+$F9)          
2960: CA AB 29        JP      Z,$29AB             ; 
2963: DD 7E 07        LD      A,(IX+$07)          
2966: ED 44           NEG                         
2968: DD 77 07        LD      (IX+$07),A          
296B: C3 AB 29        JP      $29AB               ; 
296E: 3E 1E           LD      A,$1E               
2970: 80              ADD     A,B                 
2971: DD 77 12        LD      (IX+$12),A          
2974: 11 C0 0D        LD      DE,$0DC0            
2977: 21 00 19        LD      HL,$1900            
297A: FD CB F9 7E     BIT     7,(IY+$F9)          
297E: 28 12           JR      Z,$2992             ; 
2980: DD CB 00 CE     SET     1,(IX+$00)          
2984: 11 40 F2        LD      DE,$F240            
2987: 21 00 E7        LD      HL,$E700            
298A: DD 7E 0A        LD      A,(IX+$0A)          
298D: C6 20           ADD     A,$20               
298F: DD 77 0A        LD      (IX+$0A),A          
2992: 19              ADD     HL,DE               
2993: 10 FD           DJNZ    $2992               ; 
2995: DD 75 06        LD      (IX+$06),L          
2998: DD 74 07        LD      (IX+$07),H          
299B: CD 06 29        CALL    $2906               ; 
299E: CB BF           RES     7,A                 
29A0: FE 0C           CP      $0C                 
29A2: 38 F7           JR      C,$299B             ; 
29A4: FE 5A           CP      $5A                 
29A6: 30 F3           JR      NC,$299B            ; 
29A8: DD 77 09        LD      (IX+$09),A          
29AB: DD E1           POP     IX                  
29AD: E1              POP     HL                  
29AE: D1              POP     DE                  
29AF: C1              POP     BC                  
29B0: F1              POP     AF                  
29B1: C9              RET                         
29B2: F5              PUSH    AF                  
29B3: C5              PUSH    BC                  
29B4: D5              PUSH    DE                  
29B5: E5              PUSH    HL                  
29B6: CB 20           SLA     B                   
29B8: 78              LD      A,B                 
29B9: 80              ADD     A,B                 
29BA: 80              ADD     A,B                 
29BB: 4F              LD      C,A                 
29BC: 06 00           LD      B,$00               
29BE: 21 8A 2E        LD      HL,$2E8A            
29C1: 09              ADD     HL,BC               
29C2: 5E              LD      E,(HL)              
29C3: 23              INC     HL                  
29C4: 56              LD      D,(HL)              
29C5: EB              EX      DE,HL               
29C6: CB BE           RES     7,(HL)              
29C8: E1              POP     HL                  
29C9: D1              POP     DE                  
29CA: C1              POP     BC                  
29CB: F1              POP     AF                  
29CC: C9              RET                         
29CD: F5              PUSH    AF                  
29CE: C5              PUSH    BC                  
29CF: D5              PUSH    DE                  
29D0: E5              PUSH    HL                  
29D1: 06 06           LD      B,$06               
29D3: 21 A9 43        LD      HL,$43A9            
29D6: 11 36 40        LD      DE,$4036            
29D9: 0E 04           LD      C,$04               
29DB: AF              XOR     A                   
29DC: 1A              LD      A,(DE)              
29DD: 13              INC     DE                  
29DE: 9E              SBC     (HL)                
29DF: 27              DAA                         
29E0: 23              INC     HL                  
29E1: 0D              DEC     C                   
29E2: 20 F8           JR      NZ,$29DC            ; 
29E4: 23              INC     HL                  
29E5: 23              INC     HL                  
29E6: 23              INC     HL                  
29E7: 30 08           JR      NC,$29F1            ; 
29E9: 10 EB           DJNZ    $29D6               ; 
29EB: FD 36 A4 01     LD      (IY+$A4),$01        
29EF: 18 3F           JR      $2A30               ; 
29F1: 11 F9 FF        LD      DE,$FFF9            
29F4: 19              ADD     HL,DE               
29F5: E5              PUSH    HL                  
29F6: 11 07 00        LD      DE,$0007            
29F9: 21 00 00        LD      HL,$0000            
29FC: 78              LD      A,B                 
29FD: 05              DEC     B                   
29FE: 28 03           JR      Z,$2A03             ; 
2A00: 19              ADD     HL,DE               
2A01: 18 FA           JR      $29FD               ; 
2A03: 44              LD      B,H                 
2A04: 4D              LD      C,L                 
2A05: 11 D2 43        LD      DE,$43D2            
2A08: 21 CB 43        LD      HL,$43CB            
2A0B: 3D              DEC     A                   
2A0C: 28 02           JR      Z,$2A10             ; 
2A0E: ED B8           LDDR                        
2A10: D1              POP     DE                  
2A11: 01 04 00        LD      BC,$0004            
2A14: 21 36 40        LD      HL,$4036            
2A17: ED B0           LDIR                        
2A19: ED 53 96 40     LD      ($4096),DE          ; 
2A1D: ED 53 94 40     LD      ($4094),DE          ; 
2A21: FD 36 18 00     LD      (IY+$18),$00        
2A25: 3E 20           LD      A,$20               
2A27: 12              LD      (DE),A              
2A28: 13              INC     DE                  
2A29: 12              LD      (DE),A              
2A2A: 13              INC     DE                  
2A2B: 12              LD      (DE),A              
2A2C: FD 36 A4 04     LD      (IY+$A4),$04        
2A30: E1              POP     HL                  
2A31: D1              POP     DE                  
2A32: C1              POP     BC                  
2A33: F1              POP     AF                  
2A34: C9              RET                         
2A35: F5              PUSH    AF                  
2A36: C5              PUSH    BC                  
2A37: D5              PUSH    DE                  
2A38: E5              PUSH    HL                  
2A39: 3A BC 40        LD      A,($40BC)           ; 
2A3C: E6 3E           AND     $3E                 
2A3E: 0F              RRCA                        
2A3F: 32 99 40        LD      ($4099),A           ; 
2A42: 57              LD      D,A                 
2A43: 1E 20           LD      E,$20               
2A45: CD AA 25        CALL    $25AA               ; 
2A48: 11 20 00        LD      DE,$0020            
2A4B: 19              ADD     HL,DE               
2A4C: 7C              LD      A,H                 
2A4D: 32 92 44        LD      ($4492),A           ; 
2A50: 7D              LD      A,L                 
2A51: 32 91 44        LD      ($4491),A           ; 
2A54: 2A 96 40        LD      HL,($4096)          ; 
2A57: CD AA 11        CALL    $11AA               ; 
2A5A: 20 32           JR      NZ,$2A8E            ; 
2A5C: 3A 20 40        LD      A,($4020)           ; 
2A5F: FE 14           CP      $14                 
2A61: 30 2B           JR      NC,$2A8E            ; 
2A63: FD CB 32 56     BIT     2,(IY+$32)          
2A67: CA EE 2A        JP      Z,$2AEE             ; 
2A6A: FD CB 32 96     RES     2,(IY+$32)          
2A6E: 3A 99 40        LD      A,($4099)           ; 
2A71: FE 1A           CP      $1A                 
2A73: 38 43           JR      C,$2AB8             ; 
2A75: FE 1D           CP      $1D                 
2A77: 28 15           JR      Z,$2A8E             ; 
2A79: FE 1B           CP      $1B                 
2A7B: 20 71           JR      NZ,$2AEE            ; 
2A7D: 3A 98 40        LD      A,($4098)           ; 
2A80: B7              OR      A                   
2A81: 28 6B           JR      Z,$2AEE             ; 
2A83: FD 35 18        DEC     (IY+$18)            
2A86: 2B              DEC     HL                  
2A87: 22 96 40        LD      ($4096),HL          ; 
2A8A: 36 20           LD      (HL),$20            
2A8C: 18 3D           JR      $2ACB               ; 
2A8E: FD 36 A4 01     LD      (IY+$A4),$01        
2A92: 2A 94 40        LD      HL,($4094)          ; 
2A95: 7E              LD      A,(HL)              
2A96: FE 46           CP      $46                 
2A98: 28 04           JR      Z,$2A9E             ; 
2A9A: FE 53           CP      $53                 
2A9C: 20 18           JR      NZ,$2AB6            ; 
2A9E: 23              INC     HL                  
2A9F: 7E              LD      A,(HL)              
2AA0: FE 55           CP      $55                 
2AA2: 20 12           JR      NZ,$2AB6            ; 
2AA4: 23              INC     HL                  
2AA5: 7E              LD      A,(HL)              
2AA6: FE 43           CP      $43                 
2AA8: 28 04           JR      Z,$2AAE             ; 
2AAA: FE 4B           CP      $4B                 
2AAC: 20 08           JR      NZ,$2AB6            ; 
2AAE: 36 20           LD      (HL),$20            
2AB0: 2B              DEC     HL                  
2AB1: 36 20           LD      (HL),$20            
2AB3: 2B              DEC     HL                  
2AB4: 36 20           LD      (HL),$20            
2AB6: 18 36           JR      $2AEE               ; 
2AB8: 47              LD      B,A                 
2AB9: 3A 98 40        LD      A,($4098)           ; 
2ABC: FE 03           CP      $03                 
2ABE: 30 2E           JR      NC,$2AEE            ; 
2AC0: FD 34 18        INC     (IY+$18)            ;
2AC3: 78              LD      A,B                 
2AC4: C6 41           ADD     A,$41               
2AC6: 77              LD      (HL),A              
2AC7: 23              INC     HL                  
2AC8: 22 96 40        LD      ($4096),HL          ; 
2ACB: FD 36 A0 00     LD      (IY+$A0),$00        
2ACF: FD 36 F0 14     LD      (IY+$F0),$14        
2AD3: ED 5B 94 40     LD      DE,($4094)          ; 
2AD7: 21 89 44        LD      HL,$4489            
2ADA: CD 36 2C        CALL    $2C36               ; 
2ADD: CD 36 2C        CALL    $2C36               ; 
2AE0: CD 36 2C        CALL    $2C36               ; 
2AE3: 3A 98 40        LD      A,($4098)           ; 
2AE6: FE 03           CP      $03                 
2AE8: 20 04           JR      NZ,$2AEE            ; 
2AEA: FD 36 A0 10     LD      (IY+$A0),$10        
2AEE: E1              POP     HL                  
2AEF: D1              POP     DE                  
2AF0: C1              POP     BC                  
2AF1: F1              POP     AF                  
2AF2: C9              RET                         
2AF3: F5              PUSH    AF                  
2AF4: C5              PUSH    BC                  
2AF5: D5              PUSH    DE                  
2AF6: E5              PUSH    HL                  
2AF7: DD E5           PUSH    IX                  
2AF9: CD 54 18        CALL    $1854               ; 
2AFC: FD 36 09 01     LD      (IY+$09),$01        
2B00: FD 36 0A 00     LD      (IY+$0A),$00        
2B04: FD 36 0B 00     LD      (IY+$0B),$00        
2B08: FD 4E 04        LD      C,(IY+$04)          
2B0B: 0D              DEC     C                   
2B0C: CB 21           SLA     C                   
2B0E: 06 00           LD      B,$00               
2B10: 21 15 3F        LD      HL,$3F15            
2B13: 09              ADD     HL,BC               
2B14: 5E              LD      E,(HL)              
2B15: 23              INC     HL                  
2B16: 56              LD      D,(HL)              
2B17: ED 53 85 40     LD      ($4085),DE          ; 
2B1B: 13              INC     DE                  
2B1C: EB              EX      DE,HL               
2B1D: 5E              LD      E,(HL)              
2B1E: 23              INC     HL                  
2B1F: 56              LD      D,(HL)              
2B20: 23              INC     HL                  
2B21: E5              PUSH    HL                  
2B22: EB              EX      DE,HL               
2B23: 22 87 40        LD      ($4087),HL          ; 
2B26: B7              OR      A                   
2B27: ED 52           SBC     HL,DE               
2B29: 01 0A 00        LD      BC,$000A            
2B2C: ED 42           SBC     HL,BC               
2B2E: FD 75 0C        LD      (IY+$0C),L          
2B31: 01 08 00        LD      BC,$0008            
2B34: E1              POP     HL                  
2B35: 5E              LD      E,(HL)              
2B36: 23              INC     HL                  
2B37: 56              LD      D,(HL)              
2B38: 23              INC     HL                  
2B39: ED B0           LDIR                        
2B3B: 22 8D 40        LD      ($408D),HL          ; 
2B3E: ED 53 8F 40     LD      ($408F),DE          ; 
2B42: 2A 87 40        LD      HL,($4087)          ; 
2B45: FD 34 0B        INC     (IY+$0B)            ;
2B48: 5E              LD      E,(HL)              
2B49: 23              INC     HL                  
2B4A: 56              LD      D,(HL)              
2B4B: EB              EX      DE,HL               
2B4C: 7C              LD      A,H                 
2B4D: B5              OR      L                   
2B4E: 20 F5           JR      NZ,$2B45            ; 
2B50: 2A 85 40        LD      HL,($4085)          ; 
2B53: CB 7E           BIT     7,(HL)              
2B55: 20 0F           JR      NZ,$2B66            ; 
2B57: FD 36 F0 00     LD      (IY+$F0),$00        
2B5B: CD 6D 2B        CALL    $2B6D               ; 
2B5E: 3A 8B 40        LD      A,($408B)           ; 
2B61: FD BE 09        CP      (IY+$09)            
2B64: 30 F1           JR      NC,$2B57            ; 
2B66: DD E1           POP     IX                  
2B68: E1              POP     HL                  
2B69: D1              POP     DE                  
2B6A: C1              POP     BC                  
2B6B: F1              POP     AF                  
2B6C: C9              RET                         
2B6D: F5              PUSH    AF                  
2B6E: C5              PUSH    BC                  
2B6F: D5              PUSH    DE                  
2B70: E5              PUSH    HL                  
2B71: DB 09           IN      A,($09)             ;
2B73: 3A 70 40        LD      A,($4070)           ; 
2B76: B7              OR      A                   
2B77: C2 0F 2C        JP      NZ,$2C0F            ; 
2B7A: FD 36 F0 0A     LD      (IY+$F0),$0A        
2B7E: FD 34 0A        INC     (IY+$0A)            ;
2B81: ED 5B 8D 40     LD      DE,($408D)          ; 
2B85: 2A 8F 40        LD      HL,($408F)          ; 
2B88: CB 7C           BIT     7,H                 
2B8A: C4 54 18        CALL    NZ,$1854            ; 
2B8D: 1A              LD      A,(DE)              
2B8E: CB 7F           BIT     7,A                 
2B90: 28 2F           JR      Z,$2BC1             ; 
2B92: FD 34 0A        INC     (IY+$0A)            ;
2B95: FD 34 0A        INC     (IY+$0A)            ;
2B98: 13              INC     DE                  
2B99: CB 77           BIT     6,A                 
2B9B: 20 11           JR      NZ,$2BAE            ; 
2B9D: E6 3F           AND     $3F                 
2B9F: 47              LD      B,A                 
2BA0: 1A              LD      A,(DE)              
2BA1: 13              INC     DE                  
2BA2: 4F              LD      C,A                 
2BA3: 1A              LD      A,(DE)              
2BA4: 13              INC     DE                  
2BA5: D5              PUSH    DE                  
2BA6: 57              LD      D,A                 
2BA7: 59              LD      E,C                 
2BA8: CD 0E 24        CALL    $240E               ; 
2BAB: D1              POP     DE                  
2BAC: 18 16           JR      $2BC4               ; 
2BAE: E6 3F           AND     $3F                 
2BB0: 47              LD      B,A                 
2BB1: 1A              LD      A,(DE)              
2BB2: 13              INC     DE                  
2BB3: 4F              LD      C,A                 
2BB4: 1A              LD      A,(DE)              
2BB5: 13              INC     DE                  
2BB6: D5              PUSH    DE                  
2BB7: 57              LD      D,A                 
2BB8: 59              LD      E,C                 
2BB9: CD 36 2C        CALL    $2C36               ; 
2BBC: 10 FB           DJNZ    $2BB9               ; 
2BBE: D1              POP     DE                  
2BBF: 18 03           JR      $2BC4               ; 
2BC1: CD 36 2C        CALL    $2C36               ; 
2BC4: ED 53 8D 40     LD      ($408D),DE          ; 
2BC8: 22 8F 40        LD      ($408F),HL          ; 
2BCB: 3A 8A 40        LD      A,($408A)           ; 
2BCE: FD BE 0C        CP      (IY+$0C)            
2BD1: 38 3C           JR      C,$2C0F             ; 
2BD3: FD 36 F0 19     LD      (IY+$F0),$19        
2BD7: FD 34 09        INC     (IY+$09)            ;
2BDA: 3A 8B 40        LD      A,($408B)           ; 
2BDD: FD BE 09        CP      (IY+$09)            
2BE0: 38 2D           JR      C,$2C0F             ; 
2BE2: 2A 87 40        LD      HL,($4087)          ; 
2BE5: 5E              LD      E,(HL)              
2BE6: 23              INC     HL                  
2BE7: 56              LD      D,(HL)              
2BE8: 23              INC     HL                  
2BE9: ED 53 87 40     LD      ($4087),DE          ; 
2BED: E5              PUSH    HL                  
2BEE: EB              EX      DE,HL               
2BEF: B7              OR      A                   
2BF0: ED 52           SBC     HL,DE               
2BF2: 01 0A 00        LD      BC,$000A            
2BF5: ED 42           SBC     HL,BC               
2BF7: FD 75 0C        LD      (IY+$0C),L          
2BFA: E1              POP     HL                  
2BFB: 5E              LD      E,(HL)              
2BFC: 23              INC     HL                  
2BFD: 56              LD      D,(HL)              
2BFE: 23              INC     HL                  
2BFF: 01 08 00        LD      BC,$0008            
2C02: ED B0           LDIR                        
2C04: 22 8D 40        LD      ($408D),HL          ; 
2C07: ED 53 8F 40     LD      ($408F),DE          ; 
2C0B: FD 36 0A 00     LD      (IY+$0A),$00        
2C0F: E1              POP     HL                  
2C10: D1              POP     DE                  
2C11: C1              POP     BC                  
2C12: F1              POP     AF                  
2C13: C9              RET                         
2C14: D5              PUSH    DE                  
2C15: 06 04           LD      B,$04               
2C17: CD 0E 24        CALL    $240E               ; 
2C1A: 11 67 3F        LD      DE,$3F67            
2C1D: CD 36 2C        CALL    $2C36               ; 
2C20: CD 36 2C        CALL    $2C36               ; 
2C23: D1              POP     DE                  
2C24: D5              PUSH    DE                  
2C25: 13              INC     DE                  
2C26: CD 36 2C        CALL    $2C36               ; 
2C29: CD 36 2C        CALL    $2C36               ; 
2C2C: CD 36 2C        CALL    $2C36               ; 
2C2F: D1              POP     DE                  
2C30: 21 07 00        LD      HL,$0007            
2C33: 19              ADD     HL,DE               
2C34: EB              EX      DE,HL               
2C35: C9              RET                         
2C36: F5              PUSH    AF                  
2C37: C5              PUSH    BC                  
2C38: D5              PUSH    DE                  
2C39: E5              PUSH    HL                  
2C3A: DB 09           IN      A,($09)             ;
2C3C: 1A              LD      A,(DE)              
2C3D: FE 41           CP      $41                 
2C3F: 38 0D           JR      C,$2C4E             ; 
2C41: FE 5B           CP      $5B                 
2C43: 38 02           JR      C,$2C47             ; 
2C45: 3E 5A           LD      A,$5A               
2C47: D6 41           SUB     $41                 
2C49: 21 2E 3A        LD      HL,$3A2E            
2C4C: 18 2C           JR      $2C7A               ; 
2C4E: FE 20           CP      $20                 
2C50: 20 07           JR      NZ,$2C59            ; 
2C52: 3E 0B           LD      A,$0B               
2C54: 21 D3 3F        LD      HL,$3FD3            
2C57: 18 21           JR      $2C7A               ; 
2C59: FE 2E           CP      $2E                 
2C5B: 20 07           JR      NZ,$2C64            ; 
2C5D: 3E 00           LD      A,$00               
2C5F: 21 CF 3F        LD      HL,$3FCF            
2C62: 18 16           JR      $2C7A               ; 
2C64: FE 2C           CP      $2C                 
2C66: 20 07           JR      NZ,$2C6F            ; 
2C68: 3E 01           LD      A,$01               
2C6A: 21 CF 3F        LD      HL,$3FCF            
2C6D: 18 0B           JR      $2C7A               ; 
2C6F: FE 2F           CP      $2F                 
2C71: 30 02           JR      NC,$2C75            ; 
2C73: 3E 30           LD      A,$30               
2C75: D6 2F           SUB     $2F                 
2C77: 21 D3 3F        LD      HL,$3FD3            
2C7A: CB 27           SLA     A                   
2C7C: 5F              LD      E,A                 
2C7D: 16 00           LD      D,$00               
2C7F: 19              ADD     HL,DE               
2C80: EB              EX      DE,HL               
2C81: E1              POP     HL                  
2C82: 1A              LD      A,(DE)              
2C83: 13              INC     DE                  
2C84: 77              LD      (HL),A              
2C85: 23              INC     HL                  
2C86: 1A              LD      A,(DE)              
2C87: 77              LD      (HL),A              
2C88: 23              INC     HL                  
2C89: D1              POP     DE                  
2C8A: 13              INC     DE                  
2C8B: C1              POP     BC                  
2C8C: F1              POP     AF                  
2C8D: C9              RET                         
2C8E: F5              PUSH    AF                  
2C8F: C5              PUSH    BC                  
2C90: D5              PUSH    DE                  
2C91: 3A 22 40        LD      A,($4022)           ; 
2C94: 77              LD      (HL),A              
2C95: 23              INC     HL                  
2C96: 3A 66 40        LD      A,($4066)           ; 
2C99: 77              LD      (HL),A              
2C9A: 23              INC     HL                  
2C9B: 3A 67 40        LD      A,($4067)           ; 
2C9E: 77              LD      (HL),A              
2C9F: 23              INC     HL                  
2CA0: 3A 6A 40        LD      A,($406A)           ; 
2CA3: 77              LD      (HL),A              
2CA4: 23              INC     HL                  
2CA5: 3A 6C 40        LD      A,($406C)           ; 
2CA8: 77              LD      (HL),A              
2CA9: 23              INC     HL                  
2CAA: FD CB C1 7E     BIT     7,(IY+$C1)          
2CAE: 28 09           JR      Z,$2CB9             ; 
2CB0: EB              EX      DE,HL               
2CB1: 01 08 00        LD      BC,$0008            
2CB4: 21 36 40        LD      HL,$4036            
2CB7: ED B0           LDIR                        
2CB9: D1              POP     DE                  
2CBA: C1              POP     BC                  
2CBB: F1              POP     AF                  
2CBC: C9              RET                         
2CBD: F5              PUSH    AF                  
2CBE: C5              PUSH    BC                  
2CBF: D5              PUSH    DE                  
2CC0: 7E              LD      A,(HL)              
2CC1: 23              INC     HL                  
2CC2: 32 22 40        LD      ($4022),A           ; 
2CC5: 7E              LD      A,(HL)              
2CC6: 23              INC     HL                  
2CC7: 32 66 40        LD      ($4066),A           ; 
2CCA: 7E              LD      A,(HL)              
2CCB: 23              INC     HL                  
2CCC: 32 67 40        LD      ($4067),A           ; 
2CCF: 7E              LD      A,(HL)              
2CD0: 23              INC     HL                  
2CD1: 32 6A 40        LD      ($406A),A           ; 
2CD4: 7E              LD      A,(HL)              
2CD5: 23              INC     HL                  
2CD6: 32 6C 40        LD      ($406C),A           ; 
2CD9: 01 08 00        LD      BC,$0008            
2CDC: 11 36 40        LD      DE,$4036            
2CDF: ED B0           LDIR                        
2CE1: 01 04 00        LD      BC,$0004            
2CE4: 11 42 40        LD      DE,$4042            
2CE7: 21 4B 40        LD      HL,$404B            
2CEA: FD CB BE 46     BIT     0,(IY+$BE)          
2CEE: 28 03           JR      Z,$2CF3             ; 
2CF0: 21 58 40        LD      HL,$4058            
2CF3: ED B0           LDIR                        
2CF5: D1              POP     DE                  
2CF6: C1              POP     BC                  
2CF7: F1              POP     AF                  
2CF8: C9              RET                         
2CF9: 3A 66 40        LD      A,($4066)           ; 
2CFC: 21 00 F0        LD      HL,$F000            
2CFF: 3D              DEC     A                   
2D00: 28 09           JR      Z,$2D0B             ; 
2D02: FD CB EA 5E     BIT     3,(IY+$EA)          
2D06: 28 03           JR      Z,$2D0B             ; 
2D08: 3D              DEC     A                   
2D09: 18 03           JR      $2D0E               ; 
2D0B: 22 BA 82        LD      ($82BA),HL          ; 
2D0E: B7              OR      A                   
2D0F: 28 09           JR      Z,$2D1A             ; 
2D11: FD CB EA 66     BIT     4,(IY+$EA)          
2D15: 28 03           JR      Z,$2D1A             ; 
2D17: 3D              DEC     A                   
2D18: 18 03           JR      $2D1D               ; 
2D1A: 22 B0 82        LD      ($82B0),HL          ; 
2D1D: B7              OR      A                   
2D1E: 28 09           JR      Z,$2D29             ; 
2D20: FD CB EA 6E     BIT     5,(IY+$EA)          
2D24: 28 03           JR      Z,$2D29             ; 
2D26: 3D              DEC     A                   
2D27: 18 03           JR      $2D2C               ; 
2D29: 22 A6 82        LD      ($82A6),HL          ; 
2D2C: B7              OR      A                   
2D2D: 28 11           JR      Z,$2D40             ; 
2D2F: 3D              DEC     A                   
2D30: 28 11           JR      Z,$2D43             ; 
2D32: 3D              DEC     A                   
2D33: 28 11           JR      Z,$2D46             ; 
2D35: 3D              DEC     A                   
2D36: 28 11           JR      Z,$2D49             ; 
2D38: 3D              DEC     A                   
2D39: 28 11           JR      Z,$2D4C             ; 
2D3B: 3D              DEC     A                   
2D3C: 28 11           JR      Z,$2D4F             ; 
2D3E: 18 12           JR      $2D52               ; 
2D40: 22 9C 82        LD      ($829C),HL          ; 
2D43: 22 92 82        LD      ($8292),HL          ; 
2D46: 22 88 82        LD      ($8288),HL          ; 
2D49: 22 7E 82        LD      ($827E),HL          ; 
2D4C: 22 74 82        LD      ($8274),HL          ; 
2D4F: 22 6A 82        LD      ($826A),HL          ; 
2D52: 22 60 82        LD      ($8260),HL          ; 
2D55: C9              RET                         
2D56: DB 09           IN      A,($09)             ;
2D58: DD 7E 01        LD      A,(IX+$01)          
2D5B: FE F0           CP      $F0                 
2D5D: 30 18           JR      NC,$2D77            ; 
2D5F: FE B0           CP      $B0                 
2D61: 30 1C           JR      NC,$2D7F            ; 
2D63: FE A0           CP      $A0                 
2D65: 30 08           JR      NC,$2D6F            ; 
2D67: DD 7E 03        LD      A,(IX+$03)          
2D6A: EE 04           XOR     $04                 
2D6C: DD 77 03        LD      (IX+$03),A          
2D6F: 0B              DEC     BC                  
2D70: DD 23           INC     IX                  
2D72: 0B              DEC     BC                  
2D73: DD 23           INC     IX                  
2D75: 18 08           JR      $2D7F               ; 
2D77: DD 7E 00        LD      A,(IX+$00)          
2D7A: EE 04           XOR     $04                 
2D7C: DD 77 00        LD      (IX+$00),A          
2D7F: DD 23           INC     IX                  
2D81: 0B              DEC     BC                  
2D82: DD 23           INC     IX                  
2D84: 0B              DEC     BC                  
2D85: 78              LD      A,B                 
2D86: B1              OR      C                   
2D87: 20 CD           JR      NZ,$2D56            ; 
2D89: C9              RET                         
2D8A: DB 09           IN      A,($09)             ;
2D8C: DD 7E 01        LD      A,(IX+$01)          
2D8F: FE F0           CP      $F0                 
2D91: 30 1D           JR      NC,$2DB0            ; 
2D93: FE B0           CP      $B0                 
2D95: 30 26           JR      NC,$2DBD            ; 
2D97: FE A0           CP      $A0                 
2D99: 30 0D           JR      NC,$2DA8            ; 
2D9B: EE 04           XOR     $04                 
2D9D: DD 77 01        LD      (IX+$01),A          
2DA0: DD 7E 03        LD      A,(IX+$03)          
2DA3: EE 04           XOR     $04                 
2DA5: DD 77 03        LD      (IX+$03),A          
2DA8: DD 23           INC     IX                  
2DAA: 0B              DEC     BC                  
2DAB: DD 23           INC     IX                  
2DAD: 0B              DEC     BC                  
2DAE: 18 0D           JR      $2DBD               ; 
2DB0: EE 04           XOR     $04                 
2DB2: DD 77 01        LD      (IX+$01),A          
2DB5: DD 7E 00        LD      A,(IX+$00)          
2DB8: EE 04           XOR     $04                 
2DBA: DD 77 00        LD      (IX+$00),A          
2DBD: DD 23           INC     IX                  
2DBF: 0B              DEC     BC                  
2DC0: DD 23           INC     IX                  
2DC2: 0B              DEC     BC                  
2DC3: 78              LD      A,B                 
2DC4: B1              OR      C                   
2DC5: 20 C3           JR      NZ,$2D8A            ; 
2DC7: C9              RET                         
2DC8: DB 09           IN      A,($09)             ;
2DCA: DD 7E 01        LD      A,(IX+$01)          
2DCD: FE F0           CP      $F0                 
2DCF: 30 15           JR      NC,$2DE6            ; 
2DD1: FE B0           CP      $B0                 
2DD3: 30 16           JR      NC,$2DEB            ; 
2DD5: FE A0           CP      $A0                 
2DD7: 30 05           JR      NC,$2DDE            ; 
2DD9: EE 04           XOR     $04                 
2DDB: DD 77 01        LD      (IX+$01),A          
2DDE: DD 23           INC     IX                  
2DE0: 0B              DEC     BC                  
2DE1: DD 23           INC     IX                  
2DE3: 0B              DEC     BC                  
2DE4: 18 05           JR      $2DEB               ; 
2DE6: EE 04           XOR     $04                 
2DE8: DD 77 01        LD      (IX+$01),A          
2DEB: DD 23           INC     IX                  
2DED: 0B              DEC     BC                  
2DEE: DD 23           INC     IX                  
2DF0: 0B              DEC     BC                  
2DF1: 78              LD      A,B                 
2DF2: B1              OR      C                   
2DF3: 20 D3           JR      NZ,$2DC8            ; 
2DF5: C9              RET                         
2DF6: C6 0A           ADD     A,$0A               
2DF8: FD BE E8        CP      (IY+$E8)            
2DFB: 28 06           JR      Z,$2E03             ; 
2DFD: 32 68 40        LD      ($4068),A           ; 
2E00: CD 04 2E        CALL    $2E04               ; 
2E03: C9              RET                         
2E04: F5              PUSH    AF                  
2E05: FE 00           CP      $00                 
2E07: 28 15           JR      Z,$2E1E             ; 
2E09: FD CB AE 7E     BIT     7,(IY+$AE)          
2E0D: 28 3A           JR      Z,$2E49             ; 
2E0F: 3A 21 40        LD      A,($4021)           ; 
2E12: B7              OR      A                   
2E13: 20 19           JR      NZ,$2E2E            ; 
2E15: 3A 24 40        LD      A,($4024)           ; 
2E18: FE 03           CP      $03                 
2E1A: 20 2D           JR      NZ,$2E49            ; 
2E1C: 18 1D           JR      $2E3B               ; 
2E1E: D3 14           OUT     ($14),A             ;
2E20: CD 5D 18        CALL    $185D               ; 
2E23: CD 5D 18        CALL    $185D               ; 
2E26: CD 5D 18        CALL    $185D               ; 
2E29: CD 5D 18        CALL    $185D               ; 
2E2C: 18 1B           JR      $2E49               ; 
2E2E: 3A 69 40        LD      A,($4069)           ; 
2E31: B7              OR      A                   
2E32: 28 15           JR      Z,$2E49             ; 
2E34: F1              POP     AF                  
2E35: F5              PUSH    AF                  
2E36: FD BE E8        CP      (IY+$E8)            
2E39: 28 0E           JR      Z,$2E49             ; 
2E3B: F1              POP     AF                  
2E3C: F5              PUSH    AF                  
2E3D: D3 14           OUT     ($14),A             ;
2E3F: 3E 00           LD      A,$00               
2E41: 00              NOP                         
2E42: 00              NOP                         
2E43: 00              NOP                         
2E44: 3D              DEC     A                   
2E45: 20 FA           JR      NZ,$2E41            ; 
2E47: 18 00           JR      $2E49               ; 
2E49: F1              POP     AF                  
2E4A: C9              RET                         
2E4B: 94              SUB     H                   
2E4C: 00              NOP                         
2E4D: 00              NOP                         
2E4E: 00              NOP                         
2E4F: 00              NOP                         
2E50: 00              NOP                         
2E51: 00              NOP                         
2E52: 00              NOP                         
2E53: 00              NOP                         
2E54: 00              NOP                         
2E55: 00              NOP                         
2E56: 00              NOP                         
2E57: 00              NOP                         
2E58: 00              NOP                         
2E59: 00              NOP                         
2E5A: 00              NOP                         
2E5B: 00              NOP                         
2E5C: 00              NOP                         
2E5D: 00              NOP                         
2E5E: 00              NOP                         
2E5F: 00              NOP                         
2E60: 00              NOP                         
2E61: 00              NOP                         
2E62: 00              NOP                         
2E63: 00              NOP                         
2E64: 00              NOP                         
2E65: 00              NOP                         
2E66: 00              NOP                         
2E67: 00              NOP                         
2E68: 00              NOP                         
2E69: 00              NOP                         
2E6A: 00              NOP                         
2E6B: 00              NOP                         
2E6C: 00              NOP                         
2E6D: 00              NOP                         
2E6E: 00              NOP                         
2E6F: 00              NOP                         
2E70: 00              NOP                         
2E71: 00              NOP                         
2E72: 00              NOP                         
2E73: 00              NOP                         
2E74: 00              NOP                         
2E75: 00              NOP                         
2E76: 00              NOP                         
2E77: 00              NOP                         
2E78: 00              NOP                         
2E79: 00              NOP                         
2E7A: 00              NOP                         
2E7B: 00              NOP                         
2E7C: 00              NOP                         
2E7D: 00              NOP                         
2E7E: 00              NOP                         
2E7F: 00              NOP                         
2E80: 00              NOP                         
2E81: 00              NOP                         
2E82: 00              NOP                         
2E83: 00              NOP                         
2E84: 00              NOP                         
2E85: 00              NOP                         
2E86: 00              NOP                         
2E87: 00              NOP                         
2E88: 00              NOP                         
2E89: 00              NOP                         
2E8A: 00              NOP                         
2E8B: 00              NOP                         
2E8C: 00              NOP                         
2E8D: 00              NOP                         
2E8E: 00              NOP                         
2E8F: 00              NOP                         
2E90: B2              OR      D                   
2E91: 40              LD      B,B                 
2E92: 50              LD      D,B                 
2E93: 2F              CPL                         
2E94: 81              ADD     A,C                 
2E95: 44              LD      B,H                 
2E96: C9              RET                         
2E97: 40              LD      B,B                 
2E98: 67              LD      H,A                 
2E99: 2F              CPL                         
2E9A: 8D              ADC     A,L                 
2E9B: 44              LD      B,H                 
2E9C: E0              RET     PO                  
2E9D: 40              LD      B,B                 
2E9E: 67              LD      H,A                 
2E9F: 2F              CPL                         
2EA0: 99              SBC     C                   
2EA1: 44              LD      B,H                 
2EA2: F7              RST     $30                 
2EA3: 40              LD      B,B                 
2EA4: 67              LD      H,A                 
2EA5: 2F              CPL                         
2EA6: A5              AND     L                   
2EA7: 44              LD      B,H                 
2EA8: 0E 41           LD      C,$41               
2EAA: 67              LD      H,A                 
2EAB: 2F              CPL                         
2EAC: B1              OR      C                   
2EAD: 44              LD      B,H                 
2EAE: 25              DEC     H                   
2EAF: 41              LD      B,C                 
2EB0: 67              LD      H,A                 
2EB1: 2F              CPL                         
2EB2: BD              CP      L                   
2EB3: 44              LD      B,H                 
2EB4: 3C              INC     A                   
2EB5: 41              LD      B,C                 
2EB6: 67              LD      H,A                 
2EB7: 2F              CPL                         
2EB8: C9              RET                         
2EB9: 44              LD      B,H                 
2EBA: 53              LD      D,E                 
2EBB: 41              LD      B,C                 
2EBC: 67              LD      H,A                 
2EBD: 2F              CPL                         
2EBE: D5              PUSH    DE                  
2EBF: 44              LD      B,H                 
2EC0: 6A              LD      L,D                 
2EC1: 41              LD      B,C                 
2EC2: 67              LD      H,A                 
2EC3: 2F              CPL                         
2EC4: E1              POP     HL                  
2EC5: 44              LD      B,H                 
2EC6: 81              ADD     A,C                 
2EC7: 41              LD      B,C                 
2EC8: 67              LD      H,A                 
2EC9: 2F              CPL                         
2ECA: ED 44           NEG                         
2ECC: 98              SBC     B                   
2ECD: 41              LD      B,C                 
2ECE: 67              LD      H,A                 
2ECF: 2F              CPL                         
2ED0: F9              LD      SP,HL               
2ED1: 44              LD      B,H                 
2ED2: AF              XOR     A                   
2ED3: 41              LD      B,C                 
2ED4: 67              LD      H,A                 
2ED5: 2F              CPL                         
2ED6: 05              DEC     B                   
2ED7: 45              LD      B,L                 
2ED8: C6 41           ADD     A,$41               
2EDA: 67              LD      H,A                 
2EDB: 2F              CPL                         
2EDC: 11 45 DD        LD      DE,$DD45            
2EDF: 41              LD      B,C                 
2EE0: 7E              LD      A,(HL)              
2EE1: 2F              CPL                         
2EE2: 1D              DEC     E                   
2EE3: 45              LD      B,L                 
2EE4: F4 41 7E        CALL    P,$7E41             ; 
2EE7: 2F              CPL                         
2EE8: 29              ADD     HL,HL               
2EE9: 45              LD      B,L                 
2EEA: 0B              DEC     BC                  
2EEB: 42              LD      B,D                 
2EEC: 7E              LD      A,(HL)              
2EED: 2F              CPL                         
2EEE: 35              DEC     (HL)                
2EEF: 45              LD      B,L                 
2EF0: 22 42 7E        LD      ($7E42),HL          ; 
2EF3: 2F              CPL                         
2EF4: 41              LD      B,C                 
2EF5: 45              LD      B,L                 
2EF6: 39              ADD     HL,SP               
2EF7: 42              LD      B,D                 
2EF8: 7E              LD      A,(HL)              
2EF9: 2F              CPL                         
2EFA: 4D              LD      C,L                 
2EFB: 45              LD      B,L                 
2EFC: 50              LD      D,B                 
2EFD: 42              LD      B,D                 
2EFE: 7E              LD      A,(HL)              
2EFF: 2F              CPL                         
2F00: 59              LD      E,C                 
2F01: 45              LD      B,L                 
2F02: 67              LD      H,A                 
2F03: 42              LD      B,D                 
2F04: 7E              LD      A,(HL)              
2F05: 2F              CPL                         
2F06: 65              LD      H,L                 
2F07: 45              LD      B,L                 
2F08: 7E              LD      A,(HL)              
2F09: 42              LD      B,D                 
2F0A: 7E              LD      A,(HL)              
2F0B: 2F              CPL                         
2F0C: 71              LD      (HL),C              
2F0D: 45              LD      B,L                 
2F0E: 95              SUB     L                   
2F0F: 42              LD      B,D                 
2F10: 95              SUB     L                   
2F11: 2F              CPL                         
2F12: 7D              LD      A,L                 
2F13: 45              LD      B,L                 
2F14: AC              XOR     H                   
2F15: 42              LD      B,D                 
2F16: 95              SUB     L                   
2F17: 2F              CPL                         
2F18: 89              ADC     A,C                 
2F19: 45              LD      B,L                 
2F1A: C3 42 95        JP      $9542               ; 
2F1D: 2F              CPL                         
2F1E: 95              SUB     L                   
2F1F: 45              LD      B,L                 
2F20: DA 42 95        JP      C,$9542             ; 
2F23: 2F              CPL                         
2F24: A1              AND     C                   
2F25: 45              LD      B,L                 
2F26: F1              POP     AF                  
2F27: 42              LD      B,D                 
2F28: 95              SUB     L                   
2F29: 2F              CPL                         
2F2A: AD              XOR     L                   
2F2B: 45              LD      B,L                 
2F2C: 08              EX      AF,AF'              
2F2D: 43              LD      B,E                 
2F2E: 95              SUB     L                   
2F2F: 2F              CPL                         
2F30: B9              CP      C                   
2F31: 45              LD      B,L                 
2F32: 1F              RRA                         
2F33: 43              LD      B,E                 
2F34: 95              SUB     L                   
2F35: 2F              CPL                         
2F36: C5              PUSH    BC                  
2F37: 45              LD      B,L                 
2F38: 36 43           LD      (HL),$43            
2F3A: 95              SUB     L                   
2F3B: 2F              CPL                         
2F3C: D1              POP     DE                  
2F3D: 45              LD      B,L                 
2F3E: 4D              LD      C,L                 
2F3F: 43              LD      B,E                 
2F40: 95              SUB     L                   
2F41: 2F              CPL                         
2F42: DD
2F43: 45              LD      B,L                 
2F44: 64              LD      H,H                 
2F45: 43              LD      B,E                 
2F46: 95              SUB     L                   
2F47: 2F              CPL                         
2F48: E9              JP      (HL)                
2F49: 45              LD      B,L                 
2F4A: 7B              LD      A,E                 
2F4B: 43              LD      B,E                 
2F4C: 95              SUB     L                   
2F4D: 2F              CPL                         
2F4E: F5              PUSH    AF                  
2F4F: 45              LD      B,L                 
2F50: F8              RET     M                   
2F51: 40              LD      B,B                 
2F52: 00              NOP                         
2F53: 00              NOP                         
2F54: 00              NOP                         
2F55: 00              NOP                         
2F56: 00              NOP                         
2F57: F5              PUSH    AF                  
2F58: 80              ADD     A,B                 
2F59: ED
2F5A: 30 00           JR      NC,$2F5C            ; 
2F5C: 00              NOP                         
2F5D: 00              NOP                         
2F5E: 00              NOP                         
2F5F: 00              NOP                         
2F60: 04              INC     B                   
2F61: 04              INC     B                   
2F62: 05              DEC     B                   
2F63: 00              NOP                         
2F64: 00              NOP                         
2F65: A1              AND     C                   
2F66: 30 F9           JR      NC,$2F61            ; 
2F68: 80              ADD     A,B                 
2F69: 00              NOP                         
2F6A: 00              NOP                         
2F6B: 00              NOP                         
2F6C: 00              NOP                         
2F6D: 00              NOP                         
2F6E: 40              LD      B,B                 
2F6F: 00              NOP                         
2F70: 40              LD      B,B                 
2F71: 20 00           JR      NZ,$2F73            ; 
2F73: 00              NOP                         
2F74: 03              INC     BC                  
2F75: 00              NOP                         
2F76: 00              NOP                         
2F77: 04              INC     B                   
2F78: 04              INC     B                   
2F79: 0C              INC     C                   
2F7A: 00              NOP                         
2F7B: 00              NOP                         
2F7C: 04              INC     B                   
2F7D: CA C0 01        JP      Z,$01C0             ; 
2F80: 01 00 01        LD      BC,$0100            
2F83: 00              NOP                         
2F84: 00              NOP                         
2F85: 00              NOP                         
2F86: 00              NOP                         
2F87: 00              NOP                         
2F88: 00              NOP                         
2F89: 00              NOP                         
2F8A: 19              ADD     HL,DE               
2F8B: 00              NOP                         
2F8C: 00              NOP                         
2F8D: 00              NOP                         
2F8E: 01 01 0C        LD      BC,$0C01            
2F91: 00              NOP                         
2F92: 00              NOP                         
2F93: F8              RET     M                   
2F94: F8              RET     M                   
2F95: 80              ADD     A,B                 
2F96: 02              LD      (BC),A              
2F97: 00              NOP                         
2F98: 00              NOP                         
2F99: 00              NOP                         
2F9A: 00              NOP                         
2F9B: 00              NOP                         
2F9C: 00              NOP                         
2F9D: 00              NOP                         
2F9E: 00              NOP                         
2F9F: 00              NOP                         
2FA0: 00              NOP                         
2FA1: 00              NOP                         
2FA2: 01 00 00        LD      BC,$0000            
2FA5: 03              INC     BC                  
2FA6: 03              INC     BC                  
2FA7: FF              RST     $38                 
2FA8: 00              NOP                         
2FA9: 00              NOP                         
2FAA: A7              AND     A                   
2FAB: CB 80           RES     0,B                 
2FAD: 20 00           JR      NZ,$2FAF            ; 
2FAF: 00              NOP                         
2FB0: 00              NOP                         
2FB1: 00              NOP                         
2FB2: 00              NOP                         
2FB3: 00              NOP                         
2FB4: 00              NOP                         
2FB5: 00              NOP                         
2FB6: 03              INC     BC                  
2FB7: 00              NOP                         
2FB8: 04              INC     B                   
2FB9: 00              NOP                         
2FBA: 00              NOP                         
2FBB: 00              NOP                         
2FBC: 01 01 19        LD      BC,$1901            
2FBF: 00              NOP                         
2FC0: 00              NOP                         
2FC1: BA              CP      D                   
2FC2: CB 01           RLC     C                   
2FC4: 02              LD      (BC),A              
2FC5: 01 03 01        LD      BC,$0103            
2FC8: 05              DEC     B                   
2FC9: 04              INC     B                   
2FCA: 05              DEC     B                   
2FCB: 03              INC     BC                  
2FCC: 04              INC     B                   
2FCD: 02              LD      (BC),A              
2FCE: 03              INC     BC                  
2FCF: 02              LD      (BC),A              
2FD0: 01 01 01        LD      BC,$0101            
2FD3: 02              LD      (BC),A              
2FD4: 04              INC     B                   
2FD5: 02              LD      (BC),A              
2FD6: 05              DEC     B                   
2FD7: 03              INC     BC                  
2FD8: 06 03           LD      B,$03               
2FDA: 07              RLCA                        
2FDB: 50              LD      D,B                 
2FDC: 03              INC     BC                  
2FDD: 00              NOP                         
2FDE: 05              DEC     B                   
2FDF: 00              NOP                         
2FE0: 10 00           DJNZ    $2FE2               ; 
2FE2: 15              DEC     D                   
2FE3: 00              NOP                         
2FE4: 25              DEC     H                   
2FE5: 04              INC     B                   
2FE6: 00              NOP                         
2FE7: 05              DEC     B                   
2FE8: 00              NOP                         
2FE9: 07              RLCA                        
2FEA: 00              NOP                         
2FEB: 10 00           DJNZ    $2FED               ; 
2FED: 15              DEC     D                   
2FEE: 00              NOP                         
2FEF: 25              DEC     H                   
2FF0: 00              NOP                         
2FF1: 50              LD      D,B                 
2FF2: 00              NOP                         
2FF3: 75              LD      (HL),L              
2FF4: 00              NOP                         
2FF5: 50              LD      D,B                 
2FF6: 01 50 82        LD      BC,$8250            
2FF9: 03              INC     BC                  
2FFA: 00              NOP                         
2FFB: 41              LD      B,C                 
2FFC: 45              LD      B,L                 
2FFD: 20 50           JR      NZ,$304F            ; 
2FFF: 13              INC     DE                  
3000: 03              INC     BC                  
3001: 00              NOP                         
3002: 44              LD      B,H                 
3003: 4C              LD      C,H                 
3004: 4D              LD      C,L                 
3005: 00              NOP                         
3006: 05              DEC     B                   
3007: 03              INC     BC                  
3008: 00              NOP                         
3009: 4D              LD      C,L                 
300A: 49              LD      C,C                 
300B: 43              LD      B,E                 
300C: 50              LD      D,B                 
300D: 33              INC     SP                  
300E: 02              LD      (BC),A              
300F: 00              NOP                         
3010: 4C              LD      C,H                 
3011: 52              LD      D,D                 
3012: 53              LD      D,E                 
3013: 00              NOP                         
3014: 24              INC     H                   
3015: 02              LD      (BC),A              
3016: 00              NOP                         
3017: 4A              LD      C,D                 
3018: 41              LD      B,C                 
3019: 43              LD      B,E                 
301A: 50              LD      D,B                 
301B: 95              SUB     L                   
301C: 01 00 52        LD      BC,$5200            
301F: 44              LD      B,H                 
3020: 48              LD      C,B        

         
3021: 00              NOP                         
3022: 20 03           JR      NZ,$3027            ; 
3024: 1F              RRA                         
3025: 06 1F           LD      B,$1F               
3027: 09              ADD     HL,BC               
3028: 1E 0C           LD      E,$0C               
302A: 1D              DEC     E                   
302B: 0F              RRCA                        
302C: 1C              INC     E                   
302D: 12              LD      (DE),A              
302E: 1A              LD      A,(DE)              
302F: 14              INC     D                   
3030: 19              ADD     HL,DE               
3031: 16 16           LD      D,$16               
3033: 19              ADD     HL,DE               
3034: 14              INC     D                   
3035: 1A              LD      A,(DE)              
3036: 12              LD      (DE),A              
3037: 1C              INC     E                   
3038: 0F              RRCA                        
3039: 1D              DEC     E                   
303A: 0C              INC     C                   
303B: 1E 09           LD      E,$09               
303D: 1F              RRA                         
303E: 06 20           LD      B,$20               
3040: 00              NOP                         
3041: 00              NOP                         
3042: 14              INC     D                   
3043: 99              SBC     C                   
3044: 06 0A           LD      B,$0A               
3046: 04              INC     B                   
3047: C3 02 24        JP      $2402               ; 
304A: 02              LD      (BC),A              
304B: AF              XOR     A                   
304C: 01 55 01        LD      BC,$0155            
304F: 1A              LD      A,(DE)              
3050: 01 E7 00        LD      BC,$00E7            
3053: C0              RET     NZ                  
3054: 00              NOP                         
3055: 98              SBC     B                   
3056: 00              NOP                         
3057: 77              LD      (HL),A              
3058: 00              NOP                         
3059: 5D              LD      E,L                 
305A: 00              NOP                         
305B: 3F              CCF                         
305C: 00              NOP                         
305D: 26 00           LD      H,$00               
305F: 0C              INC     C                   
3060: 00              NOP                         


3061: 00              NOP                         
3062: 01 03 02        LD      BC,$0203            
3065: 07              RLCA                        
3066: 06 04           LD      B,$04               
3068: 05              DEC     B                   
3069: 0F              RRCA                        
306A: 0E 0C           LD      C,$0C               
306C: 0D              DEC     C                   
306D: 08              EX      AF,AF'              
306E: 09              ADD     HL,BC               
306F: 0B              DEC     BC                  
3070: 0A              LD      A,(BC)              
3071: 1F              RRA                         
3072: 1E 1C           LD      E,$1C               
3074: 1D              DEC     E                   
3075: 18 19           JR      $3090               ; 
3077: 1B              DEC     DE                  
3078: 1A              LD      A,(DE)              
3079: 10 11           DJNZ    $308C               ; 
307B: 13              INC     DE                  
307C: 12              LD      (DE),A              
307D: 17              RLA                         
307E: 16 14           LD      D,$14               
3080: 15              DEC     D                   
3081: 3F              CCF                         
3082: 3E 3C           LD      A,$3C               
3084: 3D              DEC     A                   
3085: 38 39           JR      C,$30C0             ; 
3087: 3B              DEC     SP                  
3088: 3A 30 31        LD      A,($3130)           ; 
308B: 33              INC     SP                  
308C: 32 37 36        LD      ($3637),A           ; 
308F: 34              INC     (HL)                
3090: 35              DEC     (HL)                
3091: 20 21           JR      NZ,$30B4            ; 
3093: 23              INC     HL                  
3094: 22 27 26        LD      ($2627),HL          ; 
3097: 24              INC     H                   
3098: 25              DEC     H                   
3099: 2F              CPL                         
309A: 2E 2C           LD      L,$2C               
309C: 2D              DEC     L                   
309D: 28 29           JR      Z,$30C8             ; 
309F: 2B              DEC     HL                  
30A0: 2A 

30A1: 00 08          
30A3: FC 0D FC             
30A6: 05                   
30A7: F8                   
30A8: 03                  

30A9: 07 00 ; Player facing right
30AB: 27 00 ; CCW
30AD: 48 00 ; CCW
30AF: 69 00 ; CCW
30B1: 8B 00 ; CCW
30B3: AB 00 ; CCW
30B5: C9 00 ; CCW
30B7: E9 00 ; CCW
30B9: 09 01 ; CCW
30BB: 28 01 ; CCW
30BD: 48 01 ; CCW
30BF: 68 01 ; CCW
30C1: 86 01 ; CCW
30C3: A6 01 ; CCW
30C5: C8 01 ; CCW
30C7: E9 01 ; Player facing almost up

      
30C9: 0F              RRCA                        
30CA: 0D              DEC     C                   
30CB: 0B              DEC     BC                  
30CC: 09              ADD     HL,BC               
30CD: 07              RLCA                        
30CE: 05              DEC     B                   
30CF: 03              INC     BC                  
30D0: 01 00 02        LD      BC,$0200            
30D3: 04              INC     B                   
30D4: 06 08           LD      B,$08               
30D6: 0A              LD      A,(BC)              
30D7: 0C              INC     C                   
30D8: 0E 

; Copied 48 bytes to 4601 at startup
30D9: D8             
30DA: E0              RET     PO                  
30DB: FF              RST     $38                 
30DC: FF              RST     $38                 
30DD: FF              RST     $38                 
30DE: FF              RST     $38                 
30DF: FF              RST     $38                 
30E0: FF              RST     $38                 
30E1: FF              RST     $38                 
30E2: FF              RST     $38                 
30E3: 07              RLCA                        
30E4: C8              RET     Z                   
30E5: 00              NOP                         
30E6: C8              RET     Z                   
30E7: 00              NOP                         
30E8: D0              RET     NC                  
30E9: 00              NOP                         
30EA: D0              RET     NC                  
30EB: 00              NOP                         
30EC: F0              RET     P                   
30ED: 00              NOP                         
30EE: D0              RET     NC                  
30EF: 92              SUB     D                   
30F0: CD 92 CD        CALL    $CD92               ; 
30F3: 92              SUB     D                   
30F4: CD 92 CD        CALL    $CD92               ; 
30F7: 92              SUB     D                   
30F8: CD 92 CD        CALL    $CD92               ; 
30FB: 92              SUB     D                   
30FC: CD 2F CD        CALL    $CD2F               ; 
30FF: 00              NOP                         
3100: D0              RET     NC                  
3101: 00              NOP                         
3102: D0              RET     NC                  
3103: 92              SUB     D                   
3104: CD 2F CD        CALL    $CD2F               ; 
3107: 00              NOP                         
3108: D0              RET     NC
                  
3109: F8              RET     M                   
310A: A3              AND     E                   
310B: F8              RET     M                   
310C: 03              INC     BC                  
310D: 00              NOP                         
310E: 90              SUB     B                   
310F: 00              NOP                         
3110: 00              NOP                         
3111: EF              RST     $28                 
3112: 87              ADD     A,A                 
3113: 00              NOP                         
3114: 70              LD      (HL),B              
3115: F0              RET     P                   
3116: F0              RET     P                   
3117: DF              RST     $18                 
3118: 87              ADD     A,A                 
3119: 00              NOP                         
311A: 70              LD      (HL),B              
311B: F0              RET     P                   
311C: F0              RET     P                   
311D: 00              NOP                         
311E: 80              ADD     A,B                 
311F: EF              RST     $28                 
3120: 77              LD      (HL),A              
3121: F0              RET     P                   
3122: F0              RET     P                   
3123: 00              NOP                         
3124: 80              ADD     A,B                 
3125: EF              RST     $28                 
3126: 77              LD      (HL),A              
3127: F0              RET     P                   
3128: F0              RET     P                   
3129: DF              RST     $18                 
312A: 83              ADD     A,E                 
312B: 00              NOP                         
312C: 70              LD      (HL),B              
312D: F0              RET     P                   
312E: F0              RET     P                   
312F: DF              RST     $18                 
3130: 83              ADD     A,E                 
3131: 00              NOP                         
3132: 70              LD      (HL),B              
3133: F0              RET     P                   
3134: F0              RET     P                   
3135: 00              NOP                         
3136: 80              ADD     A,B                 
3137: EF              RST     $28                 
3138: 73              LD      (HL),E              
3139: F0              RET     P                   
313A: F0              RET     P                   
313B: 00              NOP                         
313C: 80              ADD     A,B                 
313D: EF              RST     $28                 
313E: 73              LD      (HL),E              
313F: F0              RET     P                   
3140: F0              RET     P                   
3141: DF              RST     $18                 
3142: 86              ADD     A,(HL)              
3143: 6F              LD      L,A                 
3144: 05              DEC     B                   
3145: 00              NOP                         
3146: F0              RET     P                   
3147: FF              RST     $38                 
3148: 77              LD      (HL),A              
3149: 00              NOP                         
314A: 70              LD      (HL),B              
314B: F0              RET     P                   
314C: F0              RET     P                   
314D: 08              EX      AF,AF'              
314E: F2 F0 F0        JP      P,$F0F0             ; 
3151: 08              EX      AF,AF'              
3152: F6 0E           OR      $0E                 
3154: F0              RET     P                   
3155: F0              RET     P                   
3156: F0              RET     P                   
3157: 0A              LD      A,(BC)              
3158: F0              RET     P                   
3159: 00              NOP                         
315A: 90              SUB     B                   
315B: 7F              LD      A,A                 
315C: 76              HALT                        
315D: F0              RET     P                   
315E: F0              RET     P                   
315F: 0A              LD      A,(BC)              
3160: F0              RET     P                   
3161: F0              RET     P                   
3162: F0              RET     P                   
3163: 0E F0           LD      C,$F0               
3165: 08              EX      AF,AF'              
3166: F2 F0 F0        JP      P,$F0F0             ; 
3169: 08              EX      AF,AF'              
316A: F6 FF           OR      $FF                 
316C: 73              LD      (HL),E              
316D: 00              NOP                         
316E: 70              LD      (HL),B              
316F: F0              RET     P                   
3170: F0              RET     P                   
3171: 08              EX      AF,AF'              
3172: F6 F0           OR      $F0                 
3174: F0              RET     P                   
3175: 08              EX      AF,AF'              
3176: F2 0A F0        JP      P,$F00A             ; 
3179: F0              RET     P                   
317A: F0              RET     P                   
317B: 0E F0           LD      C,$F0               
317D: 00              NOP                         
317E: 90              SUB     B                   
317F: 7F              LD      A,A                 
3180: 72              LD      (HL),D              
3181: F0              RET     P                   
3182: F0              RET     P                   
3183: 0E F0           LD      C,$F0               
3185: F0              RET     P                   
3186: F0              RET     P                   
3187: 0A              LD      A,(BC)              
3188: F0              RET     P                   
3189: 08              EX      AF,AF'              
318A: F6 F0           OR      $F0                 
318C: F0              RET     P                   
318D: FF              RST     $38                 
318E: FF              RST     $38                 
318F: FF              RST     $38                 
3190: FF              RST     $38                 
3191: FF              RST     $38                 
3192: FF              RST     $38                 
3193: FF              RST     $38                 
3194: FF              RST     $38                 
3195: FF              RST     $38                 
3196: FF              RST     $38                 
3197: FF              RST     $38                 
3198: FF              RST     $38                 
3199: FF              RST     $38                 
319A: FF              RST     $38                 
319B: FF              RST     $38                 
319C: FF              RST     $38                 
319D: 00              NOP                         
319E: B0              OR      B                   
319F: 92              SUB     D                   
31A0: CD 92 CD        CALL    $CD92               ; 
31A3: 92              SUB     D                   
31A4: CD 92 CD        CALL    $CD92               ; 
31A7: 92              SUB     D                   
31A8: CD 92 CD        CALL    $CD92               ; 
31AB: 92              SUB     D                   
31AC: CD 2F CD        CALL    $CD2F               ; 
31AF: 00              NOP                         
31B0: D0              RET     NC                  
31B1: E0              RET     PO                  
31B2: A1              AND     C                   
31B3: 0E 01           LD      C,$01               
31B5: 00              NOP                         
31B6: 70              LD      (HL),B              
31B7: 00              NOP                         
31B8: 00              NOP                         
31B9: 07              RLCA                        
31BA: C8              RET     Z                   
31BB: 08              EX      AF,AF'              
31BC: A2              AND     D                   
31BD: 0E 01           LD      C,$01               
31BF: 00              NOP                         
31C0: 50              LD      D,B                 
31C1: 00              NOP                         
31C2: 00              NOP                         
31C3: 07              RLCA                        
31C4: C8              RET     Z                   
31C5: 30 A2           JR      NC,$3169            ; 
31C7: 0E 01           LD      C,$01               
31C9: 00              NOP                         
31CA: 50              LD      D,B                 
31CB: 00              NOP                         
31CC: 00              NOP                         
31CD: 07              RLCA                        
31CE: C8              RET     Z                   
31CF: B8              CP      B                   
31D0: A1              AND     C                   
31D1: DC 00 00        CALL    C,$0000             ; 
31D4: 60              LD      H,B                 
31D5: 00              NOP                         
31D6: 00              NOP                         
31D7: 07              RLCA                        
31D8: C8              RET     Z                   
31D9: E0              RET     PO                  
31DA: A1              AND     C                   
31DB: DC 00 00        CALL    C,$0000             ; 
31DE: 50              LD      D,B                 
31DF: 00              NOP                         
31E0: 00              NOP                         
31E1: 07              RLCA                        
31E2: C8              RET     Z                   
31E3: 08              EX      AF,AF'              
31E4: A2              AND     D                   
31E5: DC 00 00        CALL    C,$0000             ; 
31E8: 50              LD      D,B                 
31E9: 00              NOP                         
31EA: 00              NOP                         
31EB: 07              RLCA                        
31EC: C8              RET     Z                   
31ED: 30 A2           JR      NC,$3191            ; 
31EF: DC 00 00        CALL    C,$0000             ; 
31F2: 50              LD      D,B                 
31F3: 00              NOP                         
31F4: 00              NOP                         
31F5: 07              RLCA                        
31F6: C8              RET     Z                   
31F7: 1C              INC     E                   
31F8: A2              AND     D                   
31F9: 40              LD      B,B                 
31FA: 01 00 60        LD      BC,$6000            
31FD: 00              NOP                         
31FE: 00              NOP                         
31FF: E9              JP      (HL)                
3200: C9              RET                         
3201: F4 A1 40        CALL    P,$40A1             ; 
3204: 01 00 50        LD      BC,$5000            
3207: 00              NOP                         
3208: 00              NOP                         
3209: E9              JP      (HL)                
320A: C9              RET                         
320B: CC A1 40        CALL    Z,$40A1             ; 
320E: 01 00 50        LD      BC,$5000            
3211: 00              NOP                         
3212: 00              NOP                         
3213: E9              JP      (HL)                
3214: C9              RET                         
3215: 00              NOP                         
3216: D0              RET     NC                  
3217: 80              ADD     A,B                 
3218: 4F              LD      C,A                 
3219: 32 00 80        LD      ($8000),A           ; 
321C: 84              ADD     A,H                 
321D: A3              AND     E                   
321E: F8              RET     M                   
321F: 00              NOP                         
3220: 00              NOP                         
3221: 90              SUB     B                   
3222: 00              NOP                         
3223: 00              NOP                         
3224: 49              LD      C,C                 
3225: 4E              LD      C,(HL)              
3226: 20 54           JR      NZ,$327C            ; 
3228: 48              LD      C,B                 
3229: 45              LD      B,L                 
322A: 20 59           JR      NZ,$3285            ; 
322C: 45              LD      B,L                 
322D: 41              LD      B,C                 
322E: 52              LD      D,D                 
322F: 20 32           JR      NZ,$3263            ; 
3231: 30 30           JR      NC,$3263            ; 
3233: 33              INC     SP                  
3234: 2C              INC     L                   
3235: 20 54           JR      NZ,$328B            ; 
3237: 48              LD      C,B                 
3238: 45              LD      B,L                 
3239: 20 4F           JR      NZ,$328A            ; 
323B: 4D              LD      C,L                 
323C: 45              LD      B,L                 
323D: 47              LD      B,A                 
323E: 41              LD      B,C                 
323F: 20 53           JR      NZ,$3294            ; 
3241: 59              LD      E,C                 
3242: 53              LD      D,E                 
3243: 54              LD      D,H                 
3244: 45              LD      B,L                 
3245: 4D              LD      C,L                 
3246: 20 20           JR      NZ,$3268            ; 
3248: 20 20           JR      NZ,$326A            ; 
324A: 20 20           JR      NZ,$326C            ; 
324C: 20 20           JR      NZ,$326E            ; 
324E: 20 86           JR      NZ,$31D6            ; 
3250: 32 5E 80        LD      ($805E),A           ; 
3253: 64              LD      H,H                 
3254: A3              AND     E                   
3255: F0              RET     P                   
3256: 00              NOP                         
3257: 00              NOP                         
3258: 90              SUB     B                   
3259: 00              NOP                         
325A: 00              NOP                         
325B: 44              LD      B,H                 
325C: 45              LD      B,L                 
325D: 56              LD      D,(HL)              
325E: 45              LD      B,L                 
325F: 4C              LD      C,H                 
3260: 4F              LD      C,A                 
3261: 50              LD      D,B                 
3262: 45              LD      B,L                 
3263: 44              LD      B,H                 
3264: 20 41           JR      NZ,$32A7            ; 
3266: 20 4D           JR      NZ,$32B5            ; 
3268: 45              LD      B,L                 
3269: 54              LD      D,H                 
326A: 48              LD      C,B                 
326B: 4F              LD      C,A                 
326C: 44              LD      B,H                 
326D: 20 4F           JR      NZ,$32BE            ; 
326F: 46              LD      B,(HL)              
3270: 20 54           JR      NZ,$32C6            ; 
3272: 52              LD      D,D                 
3273: 41              LD      B,C                 
3274: 49              LD      C,C                 
3275: 4E              LD      C,(HL)              
3276: 49              LD      C,C                 
3277: 4E              LD      C,(HL)              
3278: 47              LD      B,A                 
3279: 20 49           JR      NZ,$32C4            ; 
327B: 54              LD      D,H                 
327C: 53              LD      D,E                 
327D: 20 20           JR      NZ,$329F            ; 
327F: 20 20           JR      NZ,$32A1            ; 
3281: 20 20           JR      NZ,$32A3            ; 
3283: 20 20           JR      NZ,$32A5            ; 
3285: 20 C4           JR      NZ,$324B            ; 
3287: 32 BC 80        LD      ($80BC),A           ; 
328A: 42              LD      B,D                 
328B: A3              AND     E                   
328C: C0              RET     NZ                  
328D: 00              NOP                         
328E: 00              NOP                         
328F: 90              SUB     B                   
3290: 00              NOP                         
3291: 00              NOP                         
3292: 57              LD      D,A                 
3293: 41              LD      B,C                 
3294: 52              LD      D,D                 
3295: 52              LD      D,D                 
3296: 49              LD      C,C                 
3297: 4F              LD      C,A                 
3298: 52              LD      D,D                 
3299: 53              LD      D,E                 
329A: 20 54           JR      NZ,$32F0            ; 
329C: 4F              LD      C,A                 
329D: 20 50           JR      NZ,$32EF            ; 
329F: 52              LD      D,D                 
32A0: 4F              LD      C,A                 
32A1: 54              LD      D,H                 
32A2: 45              LD      B,L                 
32A3: 43              LD      B,E                 
32A4: 54              LD      D,H                 
32A5: 20 54           JR      NZ,$32FB            ; 
32A7: 48              LD      C,B                 
32A8: 45              LD      B,L                 
32A9: 49              LD      C,C                 
32AA: 52              LD      D,D                 
32AB: 20 53           JR      NZ,$3300            ; 
32AD: 54              LD      D,H                 
32AE: 41              LD      B,C                 
32AF: 52              LD      D,D                 
32B0: 20 43           JR      NZ,$32F5            ; 
32B2: 4F              LD      C,A                 
32B3: 4C              LD      C,H                 
32B4: 4F              LD      C,A                 
32B5: 4E              LD      C,(HL)              
32B6: 49              LD      C,C                 
32B7: 45              LD      B,L                 
32B8: 53              LD      D,E                 
32B9: 2E 20           LD      L,$20               
32BB: 20 20           JR      NZ,$32DD            ; 
32BD: 20 20           JR      NZ,$32DF            ; 
32BF: 20 20           JR      NZ,$32E1            ; 
32C1: 20 20           JR      NZ,$32E3            ; 
32C3: 20 FE           JR      NZ,$32C3            ; 
32C5: 32 28 81        LD      ($8128),A           ; 
32C8: 22 A3 B0        ;LD      ($B0A3),HL          
32CB: 00              NOP                         
32CC: 00              NOP                         
32CD: 90              SUB     B                   
32CE: 00              NOP                         
32CF: 00              NOP                         
32D0: 4F              LD      C,A                 
32D1: 56              LD      D,(HL)              
32D2: 45              LD      B,L                 
32D3: 52              LD      D,D                 
32D4: 20 54           JR      NZ,$332A            ; 
32D6: 48              LD      C,B                 
32D7: 45              LD      B,L                 
32D8: 20 43           JR      NZ,$331D            ; 
32DA: 49              LD      C,C                 
32DB: 54              LD      D,H                 
32DC: 59              LD      E,C                 
32DD: 20 4F           JR      NZ,$332E            ; 
32DF: 46              LD      B,(HL)              
32E0: 20 4B           JR      NZ,$332D            ; 
32E2: 4F              LD      C,A                 
32E3: 4D              LD      C,L                 
32E4: 41              LD      B,C                 
32E5: 52              LD      D,D                 
32E6: 2C              INC     L                   
32E7: 20 41           JR      NZ,$332A            ; 
32E9: 4E              LD      C,(HL)              
32EA: 44              LD      B,H                 
32EB: 52              LD      D,D                 
32EC: 4F              LD      C,A                 
32ED: 49              LD      C,C                 
32EE: 44              LD      B,H                 
32EF: 20 43           JR      NZ,$3334            ; 
32F1: 4F              LD      C,A                 
32F2: 4E              LD      C,(HL)              
32F3: 54              LD      D,H                 
32F4: 52              LD      D,D                 
32F5: 4F              LD      C,A                 
32F6: 4C              LD      C,H                 
32F7: 4C              LD      C,H                 
32F8: 45              LD      B,L                 
32F9: 44              LD      B,H                 
32FA: 20 20           JR      NZ,$331C            ; 
32FC: 20 20           JR      NZ,$331E            ; 
32FE: 38 33           JR      C,$3333             ; 
3300: 8C              ADC     A,H                 
3301: 81              ADD     A,C                 
3302: 02              LD      (BC),A              
3303: A3              AND     E                   
3304: B0              OR      B                   
3305: 00              NOP                         
3306: 00              NOP                         
3307: 90              SUB     B                   
3308: 00              NOP                         
3309: 00              NOP                         
330A: 46              LD      B,(HL)              
330B: 49              LD      C,C                 
330C: 47              LD      B,A                 
330D: 48              LD      C,B                 
330E: 54              LD      D,H                 
330F: 45              LD      B,L                 
3310: 52              LD      D,D                 
3311: 53              LD      D,E                 
3312: 20 52           JR      NZ,$3366            ; 
3314: 41              LD      B,C                 
3315: 43              LD      B,E                 
3316: 45              LD      B,L                 
3317: 44              LD      B,H                 
3318: 20 54           JR      NZ,$336E            ; 
331A: 4F              LD      C,A                 
331B: 20 45           JR      NZ,$3362            ; 
331D: 4E              LD      C,(HL)              
331E: 47              LD      B,A                 
331F: 41              LD      B,C                 
3320: 47              LD      B,A                 
3321: 45              LD      B,L                 
3322: 20 41           JR      NZ,$3365            ; 
3324: 4E              LD      C,(HL)              
3325: 44              LD      B,H                 
3326: 20 44           JR      NZ,$336C            ; 
3328: 45              LD      B,L                 
3329: 53              LD      D,E                 
332A: 54              LD      D,H                 
332B: 52              LD      D,D                 
332C: 4F              LD      C,A                 
332D: 59              LD      E,C                 
332E: 20 54           JR      NZ,$3384            ; 
3330: 48              LD      C,B                 
3331: 45              LD      B,L                 
3332: 53              LD      D,E                 
3333: 45              LD      B,L                 
3334: 20 20           JR      NZ,$3356            ; 
3336: 20 20           JR      NZ,$3358            ; 
3338: 68              LD      L,B                 
3339: 33              INC     SP                  
333A: F0              RET     P                   
333B: 81              ADD     A,C                 
333C: E2 A2 80        JP      PO,$80A2            ; 
333F: 01 00 90        LD      BC,$9000            
3342: 00              NOP                         
3343: 00              NOP                         
3344: 4F              LD      C,A                 
3345: 4D              LD      C,L                 
3346: 45              LD      B,L                 
3347: 47              LD      B,A                 
3348: 41              LD      B,C                 
3349: 4E              LD      C,(HL)              
334A: 20 57           JR      NZ,$33A3            ; 
334C: 41              LD      B,C                 
334D: 52              LD      D,D                 
334E: 52              LD      D,D                 
334F: 49              LD      C,C                 
3350: 4F              LD      C,A                 
3351: 52              LD      D,D                 
3352: 53              LD      D,E                 
3353: 2E 20           LD      L,$20               
3355: 20 20           JR      NZ,$3377            ; 
3357: 20 20           JR      NZ,$3379            ; 
3359: 20 20           JR      NZ,$337B            ; 
335B: 20 20           JR      NZ,$337D            ; 
335D: 20 20           JR      NZ,$337F            ; 
335F: 20 20           JR      NZ,$3381            ; 
3361: 20 20           JR      NZ,$3383            ; 
3363: 20 20           JR      NZ,$3385            ; 
3365: 20 20           JR      NZ,$3387            ; 
3367: 20 A4           JR      NZ,$330D            ; 
3369: 33              INC     SP                  
336A: 40              LD      B,B                 
336B: 82              ADD     A,D                 
336C: A2              AND     D                   
336D: A2              AND     D                   
336E: D0              RET     NC                  
336F: 00              NOP                         
3370: 00              NOP                         
3371: 90              SUB     B                   
3372: 00              NOP                         
3373: 00              NOP                         
3374: 50              LD      D,B                 
3375: 4F              LD      C,A                 
3376: 49              LD      C,C                 
3377: 4E              LD      C,(HL)              
3378: 54              LD      D,H                 
3379: 53              LD      D,E                 
337A: 20 57           JR      NZ,$33D3            ; 
337C: 45              LD      B,L                 
337D: 52              LD      D,D                 
337E: 45              LD      B,L                 
337F: 20 41           JR      NZ,$33C2            ; 
3381: 57              LD      D,A                 
3382: 41              LD      B,C                 
3383: 52              LD      D,D                 
3384: 44              LD      B,H                 
3385: 45              LD      B,L                 
3386: 44              LD      B,H                 
3387: 20 46           JR      NZ,$33CF            ; 
3389: 4F              LD      C,A                 
338A: 52              LD      D,D                 
338B: 20 54           JR      NZ,$33E1            ; 
338D: 48              LD      C,B                 
338E: 45              LD      B,L                 
338F: 20 41           JR      NZ,$33D2            ; 
3391: 42              LD      B,D                 
3392: 49              LD      C,C                 
3393: 4C              LD      C,H                 
3394: 49              LD      C,C                 
3395: 54              LD      D,H                 
3396: 59              LD      E,C                 
3397: 20 54           JR      NZ,$33ED            ; 
3399: 4F              LD      C,A                 
339A: 20 20           JR      NZ,$33BC            ; 
339C: 20 20           JR      NZ,$33BE            ; 
339E: 20 20           JR      NZ,$33C0            ; 
33A0: 20 20           JR      NZ,$33C2            ; 
33A2: 20 20           JR      NZ,$33C4            ; 
33A4: D7              RST     $10                 
33A5: 33              INC     SP                  
33A6: A8              XOR     B                   
33A7: 82              ADD     A,D                 
33A8: 82              ADD     A,D                 
33A9: A2              AND     D                   
33AA: C8              RET     Z                   
33AB: 00              NOP                         
33AC: 00              NOP                         
33AD: 90              SUB     B                   
33AE: 00              NOP                         
33AF: 00              NOP                         
33B0: 4E              LD      C,(HL)              
33B1: 45              LD      B,L                 
33B2: 55              LD      D,L                 
33B3: 54              LD      D,H                 
33B4: 52              LD      D,D                 
33B5: 41              LD      B,C                 
33B6: 4C              LD      C,H                 
33B7: 49              LD      C,C                 
33B8: 5A              LD      E,D                 
33B9: 45              LD      B,L                 
33BA: 20 54           JR      NZ,$3410            ; 
33BC: 48              LD      C,B                 
33BD: 49              LD      C,C                 
33BE: 53              LD      D,E                 
33BF: 20 44           JR      NZ,$3405            ; 
33C1: 52              LD      D,D                 
33C2: 4F              LD      C,A                 
33C3: 49              LD      C,C                 
33C4: 44              LD      B,H                 
33C5: 20 46           JR      NZ,$340D            ; 
33C7: 4F              LD      C,A                 
33C8: 52              LD      D,D                 
33C9: 43              LD      B,E                 
33CA: 45              LD      B,L                 
33CB: 20 41           JR      NZ,$340E            ; 
33CD: 53              LD      D,E                 
33CE: 20 46           JR      NZ,$3416            ; 
33D0: 4F              LD      C,A                 
33D1: 4C              LD      C,H                 
33D2: 4C              LD      C,H                 
33D3: 4F              LD      C,A                 
33D4: 57              LD      D,A                 
33D5: 53              LD      D,E                 
33D6: 2C              INC     L                   
33D7: 00              NOP                         
33D8: 00              NOP                         
33D9: 80              ADD     A,B                 
33DA: E1              POP     HL                  
33DB: FF              RST     $38                 
33DC: A3              AND     E                   
33DD: 00              NOP                         
33DE: 00              NOP                         
33DF: 00              NOP                         
33E0: 90              SUB     B                   
33E1: 00              NOP                         
33E2: 00              NOP                         
33E3: 00              NOP                         
33E4: 90              SUB     B                   
33E5: FE 03           CP      $03                 
33E7: FE 97           CP      $97                 
33E9: 00              NOP                         
33EA: 00              NOP                         
33EB: 00              NOP                         
33EC: 90              SUB     B                   
33ED: FE 07           CP      $07                 
33EF: FE 93           CP      $93                 
33F1: 00              NOP                         
33F2: 00              NOP                         
33F3: 00              NOP                         
33F4: B0              OR      B                   
33F5: 00              NOP                         
33F6: 03              INC     BC                  
33F7: 34              INC     (HL)                
33F8: 00              NOP                         
33F9: 80              ADD     A,B                 
33FA: BC              CP      H                   
33FB: A2              AND     D                   
33FC: C8              RET     Z                   
33FD: 00              NOP                         
33FE: 00              NOP                         
33FF: 90              SUB     B                   
3400: 00              NOP                         
3401: 00              NOP                         
3402: 3B              DEC     SP                  
3403: 19              ADD     HL,DE               
3404: 34              INC     (HL)                
3405: 0A              LD      A,(BC)              
3406: 80              ADD     A,B                 
3407: BC              CP      H                   
3408: A2              AND     D                   
3409: F4 11 00        CALL    P,$0011             ; 
340C: 70              LD      (HL),B              
340D: 00              NOP                         
340E: 00              NOP                         
340F: 82              ADD     A,D                 
3410: DC 2F 20        CALL    C,$202F             ; 
3413: 50              LD      D,B                 
3414: 4F              LD      C,A                 
3415: 49              LD      C,C                 
3416: 4E              LD      C,(HL)              
3417: 54              LD      D,H                 
3418: 53              LD      D,E                 
3419: 26 34           LD      H,$34               
341B: 28 80           JR      Z,$339D             ; 
341D: 58              LD      E,B                 
341E: A2              AND     D                   
341F: C8              RET     Z                   
3420: 00              NOP                         
3421: 00              NOP                         
3422: 90              SUB     B                   
3423: 00              NOP                         
3424: 00              NOP                         
3425: 3E 3C           LD      A,$3C               
3427: 34              INC     (HL)                
3428: 32 80 58        LD      ($5880),A           ; 
342B: A2              AND     D                   
342C: F4 11 00        CALL    P,$0011             ; 
342F: 70              LD      (HL),B              
3430: 00              NOP                         
3431: 00              NOP                         
3432: 82              ADD     A,D                 
3433: DE 2F           SBC     A,$2F               
3435: 20 50           JR      NZ,$3487            ; 
3437: 4F              LD      C,A                 
3438: 49              LD      C,C                 
3439: 4E              LD      C,(HL)              
343A: 54              LD      D,H                 
343B: 53              LD      D,E                 
343C: 49              LD      C,C                 
343D: 34              INC     (HL)                
343E: 50              LD      D,B                 
343F: 80              ADD     A,B                 
3440: F4 A1 C8        CALL    P,$C8A1             ; 
3443: 00              NOP                         
3444: 00              NOP                         
3445: 90              SUB     B                   
3446: 00              NOP                         
3447: 00              NOP                         
3448: 40              LD      B,B                 
3449: 5F              LD      E,A                 
344A: 34              INC     (HL)                
344B: 5A              LD      E,D                 
344C: 80              ADD     A,B                 
344D: F4 A1 F4        CALL    P,$F4A1             ; 
3450: 11 00 70        LD      DE,$7000            
3453: 00              NOP                         
3454: 00              NOP                         
3455: 82              ADD     A,D                 
3456: E0              RET     PO                  
3457: 2F              CPL                         
3458: 20 50           JR      NZ,$34AA            ; 
345A: 4F              LD      C,A                 
345B: 49              LD      C,C                 
345C: 4E              LD      C,(HL)              
345D: 54              LD      D,H                 
345E: 53              LD      D,E                 
345F: 6C              LD      L,H                 
3460: 34              INC     (HL)                
3461: 78              LD      A,B                 
3462: 80              ADD     A,B                 
3463: 90              SUB     B                   
3464: A1              AND     C                   
3465: C8              RET     Z                   
3466: 00              NOP                         
3467: 00              NOP                         
3468: 90              SUB     B                   
3469: 00              NOP                         
346A: 00              NOP                         
346B: 3F              CCF                         
346C: 82              ADD     A,D                 
346D: 34              INC     (HL)                
346E: 82              ADD     A,D                 
346F: 80              ADD     A,B                 
3470: 90              SUB     B                   
3471: A1              AND     C                   
3472: F4 11 00        CALL    P,$0011             ; 
3475: 70              LD      (HL),B              
3476: 00              NOP                         
3477: 00              NOP                         
3478: 82              ADD     A,D                 
3479: E2 2F 20        JP      PO,$202F            ; 
347C: 50              LD      D,B                 
347D: 4F              LD      C,A                 
347E: 49              LD      C,C                 
347F: 4E              LD      C,(HL)              
3480: 54              LD      D,H                 
3481: 53              LD      D,E                 
3482: 8F              ADC     A,A                 
3483: 34              INC     (HL)                
3484: A0              AND     B                   
3485: 80              ADD     A,B                 
3486: 2C              INC     L                   
3487: A1              AND     C                   
3488: C8              RET     Z                   
3489: 00              NOP                         
348A: 00              NOP                         
348B: 90              SUB     B                   
348C: 00              NOP                         
348D: 00              NOP                         
348E: 3F              CCF                         
348F: A5              AND     L                   
3490: 34              INC     (HL)                
3491: AA              XOR     D                   
3492: 80              ADD     A,B                 
3493: 2C              INC     L                   
3494: A1              AND     C                   
3495: F4 11 00        CALL    P,$0011             ; 
3498: 70              LD      (HL),B              
3499: 00              NOP                         
349A: 00              NOP                         
349B: 82              ADD     A,D                 
349C: E4 2F 20        CALL    PO,$202F            ; 
349F: 50              LD      D,B                 
34A0: 4F              LD      C,A                 
34A1: 49              LD      C,C                 
34A2: 4E              LD      C,(HL)              
34A3: 54              LD      D,H                 
34A4: 53              LD      D,E                 
34A5: 00              NOP                         
34A6: 00              NOP                         
34A7: 80              ADD     A,B                 
34A8: E1              POP     HL                  
34A9: 34              INC     (HL)                
34AA: 00              NOP                         
34AB: 80              ADD     A,B                 
34AC: 20 A3           JR      NZ,$3451            ; 
34AE: E8              RET     PE                  
34AF: 00              NOP                         
34B0: 00              NOP                         
34B1: 90              SUB     B                   
34B2: 00              NOP                         
34B3: 00              NOP                         
34B4: 54              LD      D,H                 
34B5: 48              LD      C,B                 
34B6: 45              LD      B,L                 
34B7: 20 4F           JR      NZ,$3508            ; 
34B9: 4D              LD      C,L                 
34BA: 45              LD      B,L                 
34BB: 47              LD      B,A                 
34BC: 41              LD      B,C                 
34BD: 4E              LD      C,(HL)              
34BE: 20 4D           JR      NZ,$350D            ; 
34C0: 45              LD      B,L                 
34C1: 54              LD      D,H                 
34C2: 48              LD      C,B                 
34C3: 4F              LD      C,A                 
34C4: 44              LD      B,H                 
34C5: 20 49           JR      NZ,$3510            ; 
34C7: 53              LD      D,E                 
34C8: 20 53           JR      NZ,$351D            ; 
34CA: 4F              LD      C,A                 
34CB: 20 53           JR      NZ,$3520            ; 
34CD: 55              LD      D,L                 
34CE: 43              LD      B,E                 
34CF: 43              LD      B,E                 
34D0: 45              LD      B,L                 
34D1: 53              LD      D,E                 
34D2: 53              LD      D,E                 
34D3: 46              LD      B,(HL)              
34D4: 55              LD      D,L                 
34D5: 4C              LD      C,H                 
34D6: 2C              INC     L                   
34D7: 20 20           JR      NZ,$34F9            ; 
34D9: 20 20           JR      NZ,$34FB            ; 
34DB: 20 20           JR      NZ,$34FD            ; 
34DD: 20 20           JR      NZ,$34FF            ; 
34DF: 20 20           JR      NZ,$3501            ; 
34E1: 1C              INC     E                   
34E2: 35              DEC     (HL)                
34E3: 62              LD      H,D                 
34E4: 80              ADD     A,B                 
34E5: 00              NOP                         
34E6: A3              AND     E                   
34E7: D8              RET     C                   
34E8: 00              NOP                         
34E9: 00              NOP                         
34EA: 90              SUB     B                   
34EB: 00              NOP                         
34EC: 00              NOP                         
34ED: 49              LD      C,C                 
34EE: 54              LD      D,H                 
34EF: 20 43           JR      NZ,$3534            ; 
34F1: 4F              LD      C,A                 
34F2: 4D              LD      C,L                 
34F3: 4D              LD      C,L                 
34F4: 41              LD      B,C                 
34F5: 4E              LD      C,(HL)              
34F6: 44              LD      B,H                 
34F7: 53              LD      D,E                 
34F8: 20 46           JR      NZ,$3540            ; 
34FA: 45              LD      B,L                 
34FB: 41              LD      B,C                 
34FC: 52              LD      D,D                 
34FD: 20 41           JR      NZ,$3540            ; 
34FF: 4E              LD      C,(HL)              
3500: 44              LD      B,H                 
3501: 20 52           JR      NZ,$3555            ; 
3503: 45              LD      B,L                 
3504: 53              LD      D,E                 
3505: 50              LD      D,B                 
3506: 45              LD      B,L                 
3507: 43              LD      B,E                 
3508: 54              LD      D,H                 
3509: 20 46           JR      NZ,$3551            ; 
350B: 52              LD      D,D                 
350C: 4F              LD      C,A                 
350D: 4D              LD      C,L                 
350E: 20 41           JR      NZ,$3551            ; 
3510: 4C              LD      C,H                 
3511: 4C              LD      C,H                 
3512: 20 20           JR      NZ,$3534            ; 
3514: 20 20           JR      NZ,$3536            ; 
3516: 20 20           JR      NZ,$3538            ; 
3518: 20 20           JR      NZ,$353A            ; 
351A: 20 20           JR      NZ,$353C            ; 
351C: 62              LD      H,D                 
351D: 35              DEC     (HL)                
351E: C8              RET     Z                   
351F: 80              ADD     A,B                 
3520: DE A2           SBC     A,$A2               
3522: 40              LD      B,B                 
3523: 00              NOP                         
3524: 00              NOP                         
3525: 90              SUB     B                   
3526: 00              NOP                         
3527: 00              NOP                         
3528: 54              LD      D,H                 
3529: 48              LD      C,B                 
352A: 52              LD      D,D                 
352B: 4F              LD      C,A                 
352C: 55              LD      D,L                 
352D: 47              LD      B,A                 
352E: 48              LD      C,B                 
352F: 4F              LD      C,A                 
3530: 55              LD      D,L                 
3531: 54              LD      D,H                 
3532: 20 54           JR      NZ,$3588            ; 
3534: 48              LD      C,B                 
3535: 45              LD      B,L                 
3536: 20 47           JR      NZ,$357F            ; 
3538: 41              LD      B,C                 
3539: 4C              LD      C,H                 
353A: 41              LD      B,C                 
353B: 58              LD      E,B                 
353C: 49              LD      C,C                 
353D: 45              LD      B,L                 
353E: 53              LD      D,E                 
353F: 2E 20           LD      L,$20               
3541: 20 54           JR      NZ,$3597            ; 
3543: 48              LD      C,B                 
3544: 45              LD      B,L                 
3545: 20 4D           JR      NZ,$3594            ; 
3547: 45              LD      B,L                 
3548: 54              LD      D,H                 
3549: 48              LD      C,B                 
354A: 4F              LD      C,A                 
354B: 44              LD      B,H                 
354C: 20 49           JR      NZ,$3597            ; 
354E: 53              LD      D,E                 
354F: 20 43           JR      NZ,$3594            ; 
3551: 4F              LD      C,A                 
3552: 44              LD      B,H                 
3553: 45              LD      B,L                 
3554: 20 4E           JR      NZ,$35A4            ; 
3556: 41              LD      B,C                 
3557: 4D              LD      C,L                 
3558: 45              LD      B,L                 
3559: 44              LD      B,H                 
355A: 20 2E           JR      NZ,$358A            ; 
355C: 20 2E           JR      NZ,$358C            ; 
355E: 20 2E           JR      NZ,$358E            ; 
3560: 20 20           JR      NZ,$3582            ; 
3562: 78              LD      A,B                 
3563: 35              DEC     (HL)                
3564: 44              LD      B,H                 
3565: 81              ADD     A,C                 
3566: 3E A2           LD      A,$A2               
3568: 60              LD      H,B                 
3569: 11 00 80        LD      DE,$8000            
356C: 00              NOP                         
356D: 00              NOP                         
356E: 4F              LD      C,A                 
356F: 4D              LD      C,L                 
3570: 45              LD      B,L                 
3571: 47              LD      B,A                 
3572: 41              LD      B,C                 
3573: 20 52           JR      NZ,$35C7            ; 
3575: 41              LD      B,C                 
3576: 43              LD      B,E                 
3577: 45              LD      B,L                 
3578: 00              NOP                         
3579: 00              NOP                         
357A: 00              NOP                         
357B: 99              SBC     C                   
357C: 35              DEC     (HL)                
357D: 00              NOP                         
357E: 80              ADD     A,B                 
357F: 2C              INC     L                   
3580: A1              AND     C                   
3581: 00              NOP                         
3582: 11 00 70        LD      DE,$7000            
3585: 00              NOP                         
3586: 00              NOP                         
3587: 50              LD      D,B                 
3588: 52              LD      D,D                 
3589: 45              LD      B,L                 
358A: 53              LD      D,E                 
358B: 53              LD      D,E                 
358C: 20 4F           JR      NZ,$35DD            ; 
358E: 4E              LD      C,(HL)              
358F: 45              LD      B,L                 
3590: 20 4F           JR      NZ,$35E1            ; 
3592: 46              LD      B,(HL)              
3593: 20 54           JR      NZ,$35E9            ; 
3595: 48              LD      C,B                 
3596: 45              LD      B,L                 
3597: 20 20           JR      NZ,$35B9            ; 
3599: B7              OR      A                   
359A: 35              DEC     (HL)                
359B: 2C              INC     L                   
359C: 80              ADD     A,B                 
359D: FA A0 00        JP      M,$00A0             ; 
35A0: 11 00 80        LD      DE,$8000            
35A3: 00              NOP                         
35A4: 00              NOP                         
35A5: 46              LD      B,(HL)              
35A6: 4C              LD      C,H                 
35A7: 41              LD      B,C                 
35A8: 53              LD      D,E                 
35A9: 48              LD      C,B                 
35AA: 49              LD      C,C                 
35AB: 4E              LD      C,(HL)              
35AC: 47              LD      B,A                 
35AD: 20 42           JR      NZ,$35F1            ; 
35AF: 55              LD      D,L                 
35B0: 54              LD      D,H                 
35B1: 54              LD      D,H                 
35B2: 4F              LD      C,A                 
35B3: 4E              LD      C,(HL)              
35B4: 53              LD      D,E                 
35B5: 20 20           JR      NZ,$35D7            ; 
35B7: E4 35 58        CALL    PO,$5835            ; 
35BA: 80              ADD     A,B                 
35BB: C8              RET     Z                   
35BC: A0              AND     B                   
35BD: 60              LD      H,B                 
35BE: 10 00           DJNZ    $35C0               ; 
35C0: 80              ADD     A,B                 
35C1: 00              NOP                         
35C2: 00              NOP                         
35C3: 4F              LD      C,A                 
35C4: 52              LD      D,D                 
35C5: 20 49           JR      NZ,$3610            ; 
35C7: 4E              LD      C,(HL)              
35C8: 53              LD      D,E                 
35C9: 45              LD      B,L                 
35CA: 52              LD      D,D                 
35CB: 54              LD      D,H                 
35CC: 20 41           JR      NZ,$360F            ; 
35CE: 44              LD      B,H                 
35CF: 44              LD      B,H                 
35D0: 49              LD      C,C                 
35D1: 54              LD      D,H                 
35D2: 49              LD      C,C                 
35D3: 4F              LD      C,A                 
35D4: 4E              LD      C,(HL)              
35D5: 41              LD      B,C                 
35D6: 4C              LD      C,H                 
35D7: 20 43           JR      NZ,$361C            ; 
35D9: 4F              LD      C,A                 
35DA: 49              LD      C,C                 
35DB: 4E              LD      C,(HL)              
35DC: 53              LD      D,E                 
35DD: 20 20           JR      NZ,$35FF            ; 
35DF: 20 20           JR      NZ,$3601            ; 
35E1: 20 20           JR      NZ,$3603            ; 
35E3: 20 FB           JR      NZ,$35E0            ; 
35E5: 35              DEC     (HL)                
35E6: A2              AND     D                   
35E7: 80              ADD     A,B                 
35E8: 96              SUB     (HL)                
35E9: A0              AND     B                   
35EA: B0              OR      B                   
35EB: 01 00 90        LD      BC,$9000            
35EE: 00              NOP                         
35EF: 00              NOP                         
35F0: 43              LD      B,E                 
35F1: 52              LD      D,D                 
35F2: 45              LD      B,L                 
35F3: 44              LD      B,H                 
35F4: 49              LD      C,C                 
35F5: 54              LD      D,H                 
35F6: 20 20           JR      NZ,$3618            ; 
35F8: 81              ADD     A,C                 
35F9: 2D              DEC     L                   
35FA: 40              LD      B,B                 
35FB: 1F              RRA                         
35FC: 36 BE           LD      (HL),$BE            
35FE: 80              ADD     A,B                 
35FF: 52              LD      D,D                 
3600: A3              AND     E                   
3601: D0              RET     NC                  
3602: 00              NOP                         
3603: 00              NOP                         
3604: 90              SUB     B                   
3605: 00              NOP                         
3606: 00              NOP                         
3607: 20 20           JR      NZ,$3629            ; 
3609: 20 20           JR      NZ,$362B            ; 
360B: 20 20           JR      NZ,$362D            ; 
360D: 31 20 43        LD      SP,$4320            
3610: 52              LD      D,D                 
3611: 45              LD      B,L                 
3612: 44              LD      B,H                 
3613: 49              LD      C,C                 
3614: 54              LD      D,H                 
3615: 20 47           JR      NZ,$365E            ; 
3617: 41              LD      B,C                 
3618: 4D              LD      C,L                 
3619: 45              LD      B,L                 
361A: 20 3D           JR      NZ,$3659            ; 
361C: 2F              CPL                         
361D: 2F              CPL                         
361E: 2F              CPL                         
361F: 49              LD      C,C                 
3620: 36 F6           LD      (HL),$F6            
3622: 80              ADD     A,B                 
3623: 20 A3           JR      NZ,$35C8            ; 
3625: B0              OR      B                   
3626: 00              NOP                         
3627: 00              NOP                         
3628: 80              ADD     A,B                 
3629: 00              NOP                         
362A: 00              NOP                         
362B: 20 20           JR      NZ,$364D            ; 
362D: 20 20           JR      NZ,$364F            ; 
362F: 20 20           JR      NZ,$3651            ; 
3631: 20 20           JR      NZ,$3653            ; 
3633: 32 20 43        LD      ($4320),A           ; 
3636: 52              LD      D,D                 
3637: 45              LD      B,L                 
3638: 44              LD      B,H                 
3639: 49              LD      C,C                 
363A: 54              LD      D,H                 
363B: 20 47           JR      NZ,$3684            ; 
363D: 41              LD      B,C                 
363E: 4D              LD      C,L                 
363F: 45              LD      B,L                 
3640: 20 3D           JR      NZ,$367F            ; 
3642: 2F              CPL                         
3643: 2F              CPL                         
3644: 2F              CPL                         
3645: 2F              CPL                         
3646: 2F              CPL                         
3647: 2F              CPL                         
3648: 2F              CPL                         
3649: 69              LD      L,C                 
364A: 36 3A           LD      (HL),$3A            
364C: 81              ADD     A,C                 
364D: 8A              ADC     A,D                 
364E: A2              AND     D                   
364F: 98              SBC     B                   
3650: 01 00 70        LD      BC,$7000            
3653: 00              NOP                         
3654: 00              NOP                         
3655: 42              LD      B,D                 
3656: 4F              LD      C,A                 
3657: 4E              LD      C,(HL)              
3658: 55              LD      D,L                 
3659: 53              LD      D,E                 
365A: 20 53           JR      NZ,$36AF            ; 
365C: 48              LD      C,B                 
365D: 49              LD      C,C                 
365E: 50              LD      D,B                 
365F: 53              LD      D,E                 
3660: 20 41           JR      NZ,$36A3            ; 
3662: 54              LD      D,H                 
3663: 20 20           JR      NZ,$3685            ; 
3665: 20 20           JR      NZ,$3687            ; 
3667: 20 20           JR      NZ,$3689            ; 
3669: 7C              LD      A,H                 
366A: 36 6A           LD      (HL),$6A            
366C: 81              ADD     A,C                 
366D: 58              LD      E,B                 
366E: A2              AND     D                   
366F: C0              RET     NZ                  
3670: 01 00 80        LD      BC,$8000            
3673: 00              NOP                         
3674: 00              NOP                         
3675: 82              ADD     A,D                 
3676: 61              LD      H,C                 
3677: 40              LD      B,B                 
3678: 30 30           JR      NC,$36AA            ; 
367A: 30 30           JR      NC,$36AC            ; 
367C: 8F              ADC     A,A                 
367D: 36 82           LD      (HL),$82            
367F: 81              ADD     A,C                 
3680: 26 A2           LD      H,$A2               
3682: C0              RET     NZ                  
3683: 01 00 60        LD      BC,$6000            
3686: 00              NOP                         
3687: 00              NOP                         
3688: 82              ADD     A,D                 
3689: 63              LD      H,E                 
368A: 40              LD      B,B                 
368B: 30 30           JR      NC,$36BD            ; 
368D: 30 30           JR      NC,$36BF            ; 
368F: A2              AND     D                   
3690: 36 9A           LD      (HL),$9A            
3692: 81              ADD     A,C                 
3693: F4 A1 C0        CALL    P,$C0A1             ; 
3696: 01 00 60        LD      BC,$6000            
3699: 00              NOP                         
369A: 00              NOP                         
369B: 82              ADD     A,D                 
369C: 65              LD      H,L                 
369D: 40              LD      B,B                 
369E: 30 30           JR      NC,$36D0            ; 
36A0: 30 30           JR      NC,$36D2            ; 
36A2: 00              NOP                         
36A3: 00              NOP                         
36A4: 00              NOP                         
36A5: BA              CP      D                   
36A6: 36 BE           LD      (HL),$BE            
36A8: 82              ADD     A,D                 
36A9: 1C              INC     E                   
36AA: A2              AND     D                   
36AB: 10 02           DJNZ    $36AF               ; 
36AD: 00              NOP                         
36AE: 80              ADD     A,B                 
36AF: 00              NOP                         
36B0: 00              NOP                         
36B1: 53              LD      D,E                 
36B2: 43              LD      B,E                 
36B3: 4F              LD      C,A                 
36B4: 52              LD      D,D                 
36B5: 45              LD      B,L                 
36B6: 20 20           JR      NZ,$36D8            ; 
36B8: 20 20           JR      NZ,$36DA            ; 
36BA: C7              RST     $00                 
36BB: 36 D8           LD      (HL),$D8            
36BD: 82              ADD     A,D                 
36BE: F4 A1 60        CALL    P,$60A1             ; 
36C1: 11 00 70        LD      DE,$7000            
36C4: 00              NOP                         
36C5: 00              NOP                         
36C6: 3C              INC     A                   
36C7: 00              NOP                         
36C8: 00              NOP                         
36C9: 00              NOP                         
36CA: E6 36           AND     $36                 
36CC: E2 82 B8        JP      PO,$B882            ; 
36CF: A1              AND     C                   
36D0: C0              RET     NZ                  
36D1: 01 00 60        LD      BC,$6000            
36D4: 00              NOP                         
36D5: 00              NOP                         
36D6: 4C              LD      C,H                 
36D7: 41              LD      B,C                 
36D8: 53              LD      D,E                 
36D9: 54              LD      D,H                 
36DA: 20 53           JR      NZ,$372F            ; 
36DC: 43              LD      B,E                 
36DD: 4F              LD      C,A                 
36DE: 52              LD      D,D                 
36DF: 45              LD      B,L                 
36E0: 20 20           JR      NZ,$3702            ; 
36E2: 20 20           JR      NZ,$3704            ; 
36E4: 20 20           JR      NZ,$3706            ; 
36E6: F3              DI                          
36E7: 36 0A           LD      (HL),$0A            
36E9: 83              ADD     A,E                 
36EA: 90              SUB     B                   
36EB: A1              AND     C                   
36EC: 60              LD      H,B                 
36ED: 11 00 70        LD      DE,$7000            
36F0: 00              NOP                         
36F1: 00              NOP                         
36F2: 3C              INC     A                   
36F3: 00              NOP                         
36F4: 00              NOP                         
36F5: 00              NOP                         
36F6: 0B              DEC     BC                  
36F7: 37              SCF                         
36F8: BE              CP      (HL)                
36F9: 82              ADD     A,D                 
36FA: 71              LD      (HL),C              
36FB: A2              AND     D                   
36FC: 28 01           JR      Z,$36FF             ; 
36FE: 00              NOP                         
36FF: 90              SUB     B                   
3700: 00              NOP                         
3701: 00              NOP                         
3702: 50              LD      D,B                 
3703: 4C              LD      C,H                 
3704: 41              LD      B,C                 
3705: 59              LD      E,C                 
3706: 45              LD      B,L                 
3707: 52              LD      D,D                 
3708: 20 31           JR      NZ,$373B            ; 
370A: 20 18           JR      NZ,$3724            ; 
370C: 37              SCF                         
370D: D8              RET     C                   
370E: 82              ADD     A,D                 
370F: 51              LD      D,C                 
3710: A2              AND     D                   
3711: 98              SBC     B                   
3712: 10 00           DJNZ    $3714               ; 
3714: 60              LD      H,B                 
3715: 00              NOP                         
3716: 00              NOP                         
3717: 3C              INC     A                   
3718: 00              NOP                         
3719: 00              NOP                         
371A: 00              NOP                         
371B: 30 37           JR      NC,$3754            ; 
371D: E2 82 71        JP      PO,$7182            ; 
3720: A2              AND     D                   
3721: A8              XOR     B                   
3722: 02              LD      (BC),A              
3723: 00              NOP                         
3724: 80              ADD     A,B                 
3725: 00              NOP                         
3726: 00              NOP                         
3727: 50              LD      D,B                 
3728: 4C              LD      C,H                 
3729: 41              LD      B,C                 
372A: 59              LD      E,C                 
372B: 45              LD      B,L                 
372C: 52              LD      D,D                 
372D: 20 32           JR      NZ,$3761            ; 
372F: 20 3D           JR      NZ,$376E            ; 
3731: 37              SCF                         
3732: FC 82 51        CALL    M,$5182             ; 
3735: A2              AND     D                   
3736: 18 12           JR      $374A               ; 
3738: 00              NOP                         
3739: 60              LD      H,B                 
373A: 00              NOP                         
373B: 00              NOP                         
373C: 3C              INC     A                   
373D: 00              NOP                         
373E: 00              NOP                         
373F: 00              NOP                         
3740: 55              LD      D,L                 
3741: 37              SCF                         
3742: 1A              LD      A,(DE)              
3743: 83              ADD     A,E                 
3744: 90              SUB     B                   
3745: A1              AND     C                   
3746: DC 00 00        CALL    C,$0000             ; 
3749: 60              LD      H,B                 
374A: 00              NOP                         
374B: 00              NOP                         
374C: 43              LD      B,E                 
374D: 52              LD      D,D                 
374E: 45              LD      B,L                 
374F: 44              LD      B,H                 
3750: 49              LD      C,C                 
3751: 54              LD      D,H                 
3752: 20 20           JR      NZ,$3774            ; 
3754: 3C              INC     A                   
3755: 00              NOP                         
3756: 00              NOP                         
3757: 00              NOP                         
3758: 6D              LD      L,L                 
3759: 37              SCF                         
375A: 1A              LD      A,(DE)              
375B: 83              ADD     A,E                 
375C: 90              SUB     B                   
375D: A1              AND     C                   
375E: B8              CP      B                   
375F: 01 00 70        LD      BC,$7000            
3762: 00              NOP                         
3763: 00              NOP                         
3764: 43              LD      B,E                 
3765: 52              LD      D,D                 
3766: 45              LD      B,L                 
3767: 44              LD      B,H                 
3768: 49              LD      C,C                 
3769: 54              LD      D,H                 
376A: 20 20           JR      NZ,$378C            ; 
376C: 3C              INC     A                   
376D: 00              NOP                         
376E: 00              NOP                         
376F: 00              NOP                         
3770: 94              SUB     H                   
3771: 37              SCF                         
3772: 34              INC     (HL)                
3773: 83              ADD     A,E                 
3774: BC              CP      H                   
3775: A2              AND     D                   
3776: F0              RET     P                   
3777: 10 00           DJNZ    $3779               ; 
3779: 70              LD      (HL),B              
377A: 00              NOP                         
377B: 00              NOP                         
377C: 53              LD      D,E                 
377D: 41              LD      B,C                 
377E: 4D              LD      C,L                 
377F: 45              LD      B,L                 
3780: 20 50           JR      NZ,$37D2            ; 
3782: 4C              LD      C,H                 
3783: 41              LD      B,C                 
3784: 59              LD      E,C                 
3785: 45              LD      B,L                 
3786: 52              LD      D,D                 
3787: 20 41           JR      NZ,$37CA            ; 
3789: 47              LD      B,A                 
378A: 41              LD      B,C                 
378B: 49              LD      C,C                 
378C: 4E              LD      C,(HL)              
378D: 3C              INC     A                   
378E: 20 20           JR      NZ,$37B0            ; 
3790: 20 20           JR      NZ,$37B2            ; 
3792: 20 20           JR      NZ,$37B4            ; 
3794: 00              NOP                         
3795: 00              NOP                         
3796: 00              NOP                         
3797: B3              OR      E                   
3798: 37              SCF                         
3799: 34              INC     (HL)                
379A: 83              ADD     A,E                 
379B: A4              AND     H                   
379C: A3              AND     E                   
379D: 10 11           DJNZ    $37B0               ; 
379F: 00              NOP                         
37A0: 80              ADD     A,B                 
37A1: 00              NOP                         
37A2: 00              NOP                         
37A3: 46              LD      B,(HL)              
37A4: 49              LD      C,C                 
37A5: 52              LD      D,D                 
37A6: 53              LD      D,E                 
37A7: 54              LD      D,H                 
37A8: 20 50           JR      NZ,$37FA            ; 
37AA: 4C              LD      C,H                 
37AB: 41              LD      B,C                 
37AC: 59              LD      E,C                 
37AD: 45              LD      B,L                 
37AE: 52              LD      D,D                 
37AF: 20 55           JR      NZ,$3806            ; 
37B1: 50              LD      D,B                 
37B2: 3C              INC     A                   
37B3: 00              NOP                         
37B4: 00              NOP                         
37B5: 00              NOP                         
37B6: D3 37           OUT     ($37),A             ;
37B8: 34              INC     (HL)                
37B9: 83              ADD     A,E                 
37BA: A4              AND     H                   
37BB: A3              AND     E                   
37BC: 00              NOP                         
37BD: 11 00 80        LD      DE,$8000            
37C0: 00              NOP                         
37C1: 00              NOP                         
37C2: 53              LD      D,E                 
37C3: 45              LD      B,L                 
37C4: 43              LD      B,E                 
37C5: 4F              LD      C,A                 
37C6: 4E              LD      C,(HL)              
37C7: 44              LD      B,H                 
37C8: 20 50           JR      NZ,$381A            ; 
37CA: 4C              LD      C,H                 
37CB: 41              LD      B,C                 
37CC: 59              LD      E,C                 
37CD: 45              LD      B,L                 
37CE: 52              LD      D,D                 
37CF: 20 55           JR      NZ,$3826            ; 
37D1: 50              LD      D,B                 
37D2: 3C              INC     A                   
37D3: 00              NOP                         
37D4: 00              NOP                         
37D5: 80              ADD     A,B                 
37D6: EC 37 34        CALL    PE,$3437            ; 
37D9: 83              ADD     A,E                 
37DA: BC              CP      H                   
37DB: A2              AND     D                   
37DC: 70              LD      (HL),B              
37DD: 11 00 70        LD      DE,$7000            
37E0: 00              NOP                         
37E1: 00              NOP                         
37E2: 47              LD      B,A                 
37E3: 41              LD      B,C                 
37E4: 4D              LD      C,L                 
37E5: 45              LD      B,L                 
37E6: 20 4F           JR      NZ,$3837            ; 
37E8: 56              LD      D,(HL)              
37E9: 45              LD      B,L                 
37EA: 52              LD      D,D                 
37EB: 3C              INC     A                   
37EC: 00              NOP                         
37ED: 00              NOP                         
37EE: 00              NOP                         
37EF: 0E 38           LD      C,$38               
37F1: 00              NOP                         
37F2: 80              ADD     A,B                 
37F3: BC              CP      H                   
37F4: A2              AND     D                   
37F5: C8              RET     Z                   
37F6: 10 00           DJNZ    $37F8               ; 
37F8: 70              LD      (HL),B              
37F9: 00              NOP                         
37FA: 00              NOP                         
37FB: 31 20 43        LD      SP,$4320            
37FE: 52              LD      D,D                 
37FF: 45              LD      B,L                 
3800: 44              LD      B,H                 
3801: 49              LD      C,C                 
3802: 54              LD      D,H                 
3803: 20 47           JR      NZ,$384C            ; 
3805: 41              LD      B,C                 
3806: 4D              LD      C,L                 
3807: 45              LD      B,L                 
3808: 20 20           JR      NZ,$382A            ; 
380A: 20 20           JR      NZ,$382C            ; 
380C: 20 20           JR      NZ,$382E            ; 
380E: 2F              CPL                         
380F: 38 2E           JR      C,$383F             ; 
3811: 80              ADD     A,B                 
3812: 94              SUB     H                   
3813: A2              AND     D                   
3814: C8              RET     Z                   
3815: 10 00           DJNZ    $3817               ; 
3817: 80              ADD     A,B                 
3818: 00              NOP                         
3819: 00              NOP                         
381A: 41              LD      B,C                 
381B: 4C              LD      C,H                 
381C: 4C              LD      C,H                 
381D: 20 54           JR      NZ,$3873            ; 
381F: 49              LD      C,C                 
3820: 4D              LD      C,L                 
3821: 45              LD      B,L                 
3822: 20 48           JR      NZ,$386C            ; 
3824: 49              LD      C,C                 
3825: 47              LD      B,A                 
3826: 48              LD      C,B                 
3827: 20 20           JR      NZ,$3849            ; 
3829: 20 20           JR      NZ,$384B            ; 
382B: 20 20           JR      NZ,$384D            ; 
382D: 20 20           JR      NZ,$384F            ; 
382F: 43              LD      B,E                 
3830: 38 60           JR      C,$3892             ; 
3832: 80              ADD     A,B                 
3833: 58              LD      E,B                 
3834: A2              AND     D                   
3835: C8              RET     Z                   
3836: 10 00           DJNZ    $3838               ; 
3838: 80              ADD     A,B                 
3839: 00              NOP                         
383A: 00              NOP                         
383B: 84              ADD     A,H                 
383C: D6 43           SUB     $43                 
383E: 20 20           JR      NZ,$3860            ; 
3840: C3 D7 43        JP      $43D7               ; 
3843: 64              LD      H,H                 
3844: 38 82           JR      C,$37C8             ; 
3846: 80              ADD     A,B                 
3847: 08              EX      AF,AF'              
3848: A2              AND     D                   
3849: E8              RET     PE                  
384A: 10 00           DJNZ    $384C               ; 
384C: 70              LD      (HL),B              
384D: 00              NOP                         
384E: 00              NOP                         
384F: 44              LD      B,H                 
3850: 41              LD      B,C                 
3851: 49              LD      C,C                 
3852: 4C              LD      C,H                 
3853: 59              LD      E,C                 
3854: 20 48           JR      NZ,$389E            ; 
3856: 49              LD      C,C                 
3857: 47              LD      B,A                 
3858: 48              LD      C,B                 
3859: 53              LD      D,E                 
385A: 20 20           JR      NZ,$387C            ; 
385C: 20 20           JR      NZ,$387E            ; 
385E: 20 20           JR      NZ,$3880            ; 
3860: 20 20           JR      NZ,$3882            ; 
3862: 20 20           JR      NZ,$3884            ; 
3864: 78              LD      A,B                 
3865: 38 B4           JR      C,$381B             ; 
3867: 80              ADD     A,B                 
3868: CC A1 C8        CALL    Z,$C8A1             ; 
386B: 10 00           DJNZ    $386D               ; 
386D: 80              ADD     A,B                 
386E: 00              NOP                         
386F: 00              NOP                         
3870: 84              ADD     A,H                 
3871: DD
3872: 43              LD      B,E                 
3873: 20 20           JR      NZ,$3895            ; 
3875: C3 DE 43        JP      $43DE               ; 
3878: 8C              ADC     A,H                 
3879: 38 D6           JR      C,$3851             ; 
387B: 80              ADD     A,B                 
387C: A4              AND     H                   
387D: A1              AND     C                   
387E: C8              RET     Z                   
387F: 10 00           DJNZ    $3881               ; 
3881: 70              LD      (HL),B              
3882: 00              NOP                         
3883: 00              NOP                         
3884: 84              ADD     A,H                 
3885: E4 43 20        CALL    PO,$2043            ; 
3888: 20 C3           JR      NZ,$384D            ; 
388A: E5              PUSH    HL                  
388B: 43              LD      B,E                 
388C: A0              AND     B                   
388D: 38 F8           JR      C,$3887             ; 
388F: 80              ADD     A,B                 
3890: 7C              LD      A,H                 
3891: A1              AND     C                   
3892: C8              RET     Z                   
3893: 10 00           DJNZ    $3895               ; 
3895: 70              LD      (HL),B              
3896: 00              NOP                         
3897: 00              NOP                         
3898: 84              ADD     A,H                 
3899: EB              EX      DE,HL               
389A: 43              LD      B,E                 
389B: 20 20           JR      NZ,$38BD            ; 
389D: C3 EC 43        JP      $43EC               ; 
38A0: B4              OR      H                   
38A1: 38 1A           JR      C,$38BD             ; 
38A3: 81              ADD     A,C                 
38A4: 54              LD      D,H                 
38A5: A1              AND     C                   
38A6: C8              RET     Z                   
38A7: 10 00           DJNZ    $38A9               ; 
38A9: 70              LD      (HL),B              
38AA: 00              NOP                         
38AB: 00              NOP                         
38AC: 84              ADD     A,H                 
38AD: F2 43 20        JP      P,$2043             ; 
38B0: 20 C3           JR      NZ,$3875            ; 
38B2: F3              DI                          
38B3: 43              LD      B,E                 
38B4: C8              RET     Z                   
38B5: 38 3C           JR      C,$38F3             ; 
38B7: 81              ADD     A,C                 
38B8: 2C              INC     L                   
38B9: A1              AND     C                   
38BA: C8              RET     Z                   
38BB: 10 00           DJNZ    $38BD               ; 
38BD: 70              LD      (HL),B              
38BE: 00              NOP                         
38BF: 00              NOP                         
38C0: 84              ADD     A,H                 
38C1: F9              LD      SP,HL               
38C2: 43              LD      B,E                 
38C3: 20 20           JR      NZ,$38E5            ; 
38C5: C3 FA 43        JP      $43FA               ; 
38C8: D6 38           SUB     $38                 
38CA: 5E              LD      E,(HL)              
38CB: 81              ADD     A,C                 
38CC: 60              LD      H,B                 
38CD: A0              AND     B                   
38CE: 13              INC     DE                  
38CF: 11 00 70        LD      DE,$7000            
38D2: 00              NOP                         
38D3: 00              NOP                         
38D4: 30 30           JR      NC,$3906            ; 
38D6: FB              EI                          
38D7: 38 6A           JR      C,$3943             ; 
38D9: 81              ADD     A,C                 
38DA: 64              LD      H,H                 
38DB: A0              AND     B                   
38DC: 18 01           JR      $38DF               ; 
38DE: 00              NOP                         
38DF: 50              LD      D,B                 
38E0: 00              NOP                         
38E1: 00              NOP                         
38E2: 43              LD      B,E                 
38E3: 20 50           JR      NZ,$3935            ; 
38E5: 20 20           JR      NZ,$3907            ; 
38E7: 31 39 38        LD      SP,$3839            
38EA: 31 20 4D        LD      SP,$4D20            
38ED: 49              LD      C,C                 
38EE: 44              LD      B,H                 
38EF: 57              LD      D,A                 
38F0: 41              LD      B,C                 
38F1: 59              LD      E,C                 
38F2: 20 4D           JR      NZ,$3941            ; 
38F4: 46              LD      B,(HL)              
38F5: 47              LD      B,A                 
38F6: 2E 20           LD      L,$20               
38F8: 43              LD      B,E                 
38F9: 4F              LD      C,A                 
38FA: 2E 00           LD      L,$00               
38FC: 00              NOP                         
38FD: 00              NOP                         
38FE: 1F              RRA                         
38FF: 39              ADD     HL,SP               
3900: 00              NOP                         
3901: 80              ADD     A,B                 
3902: BC              CP      H                   
3903: A2              AND     D                   
3904: 98              SBC     B                   
3905: 11 00 70        LD      DE,$7000            
3908: 00              NOP                         
3909: 00              NOP                         
390A: 32 20 43        LD      ($4320),A           ; 
390D: 52              LD      D,D                 
390E: 45              LD      B,L                 
390F: 44              LD      B,H                 
3910: 49              LD      C,C                 
3911: 54              LD      D,H                 
3912: 20 47           JR      NZ,$395B            ; 
3914: 41              LD      B,C                 
3915: 4D              LD      C,L                 
3916: 45              LD      B,L                 
3917: 20 20           JR      NZ,$3939            ; 
3919: 20 20           JR      NZ,$393B            ; 
391B: 20 20           JR      NZ,$393D            ; 
391D: 20 20           JR      NZ,$393F            ; 
391F: 40              LD      B,B                 
3920: 39              ADD     HL,SP               
3921: 32 80 94        LD      ($9480),A           ; 
3924: A2              AND     D                   
3925: 98              SBC     B                   
3926: 11 00 80        LD      DE,$8000            
3929: 00              NOP                         
392A: 00              NOP                         
392B: 41              LD      B,C                 
392C: 4C              LD      C,H                 
392D: 4C              LD      C,H                 
392E: 20 54           JR      NZ,$3984            ; 
3930: 49              LD      C,C                 
3931: 4D              LD      C,L                 
3932: 45              LD      B,L                 
3933: 20 48           JR      NZ,$397D            ; 
3935: 49              LD      C,C                 
3936: 47              LD      B,A                 
3937: 48              LD      C,B                 
3938: 20 20           JR      NZ,$395A            ; 
393A: 20 20           JR      NZ,$395C            ; 
393C: 20 20           JR      NZ,$395E            ; 
393E: 20 20           JR      NZ,$3960            ; 
3940: 54              LD      D,H                 
3941: 39              ADD     HL,SP               
3942: 64              LD      H,H                 
3943: 80              ADD     A,B                 
3944: 58              LD      E,B                 
3945: A2              AND     D                   
3946: 98              SBC     B                   
3947: 11 00 80        LD      DE,$8000            
394A: 00              NOP                         
394B: 00              NOP                         
394C: 84              ADD     A,H                 
394D: 00              NOP                         
394E: 44              LD      B,H                 
394F: 20 20           JR      NZ,$3971            ; 
3951: C3 01 44        JP      $4401               ; 
3954: 75              LD      (HL),L              
3955: 39              ADD     HL,SP               
3956: 86              ADD     A,(HL)              
3957: 80              ADD     A,B                 
3958: 08              EX      AF,AF'              
3959: A2              AND     D                   
395A: B8              CP      B                   
395B: 11 00 70        LD      DE,$7000            
395E: 00              NOP                         
395F: 00              NOP                         
3960: 44              LD      B,H                 
3961: 41              LD      B,C                 
3962: 49              LD      C,C                 
3963: 4C              LD      C,H                 
3964: 59              LD      E,C                 
3965: 20 48           JR      NZ,$39AF            ; 
3967: 49              LD      C,C                 
3968: 47              LD      B,A                 
3969: 48              LD      C,B                 
396A: 53              LD      D,E                 
396B: 20 20           JR      NZ,$398D            ; 
396D: 20 20           JR      NZ,$398F            ; 
396F: 20 20           JR      NZ,$3991            ; 
3971: 20 20           JR      NZ,$3993            ; 
3973: 20 20           JR      NZ,$3995            ; 
3975: 89              ADC     A,C                 
3976: 39              ADD     HL,SP               
3977: B8              CP      B                   
3978: 80              ADD     A,B                 
3979: CC A1 98        CALL    Z,$98A1             ; 
397C: 11 00 80        LD      DE,$8000            
397F: 00              NOP                         
3980: 00              NOP                         
3981: 84              ADD     A,H                 
3982: 07              RLCA                        
3983: 44              LD      B,H                 
3984: 20 20           JR      NZ,$39A6            ; 
3986: C3 08 44        JP      $4408               ; 
3989: 9D              SBC     L                   
398A: 39              ADD     HL,SP               
398B: DA 80 A4        JP      C,$A480             ; 
398E: A1              AND     C                   
398F: 98              SBC     B                   
3990: 11 00 70        LD      DE,$7000            
3993: 00              NOP                         
3994: 00              NOP                         
3995: 84              ADD     A,H                 
3996: 0E 44           LD      C,$44               
3998: 20 20           JR      NZ,$39BA            ; 
399A: C3 0F 44        JP      $440F               ; 
399D: B1              OR      C                   
399E: 39              ADD     HL,SP               
399F: FC 80 7C        CALL    M,$7C80             ; 
39A2: A1              AND     C                   
39A3: 98              SBC     B                   
39A4: 11 00 70        LD      DE,$7000            
39A7: 00              NOP                         
39A8: 00              NOP                         
39A9: 84              ADD     A,H                 
39AA: 15              DEC     D                   
39AB: 44              LD      B,H                 
39AC: 20 20           JR      NZ,$39CE            ; 
39AE: C3 16 44        JP      $4416               ; 
39B1: C5              PUSH    BC                  
39B2: 39              ADD     HL,SP               
39B3: 1E 81           LD      E,$81               
39B5: 54              LD      D,H                 
39B6: A1              AND     C                   
39B7: 98              SBC     B                   
39B8: 11 00 70        LD      DE,$7000            
39BB: 00              NOP                         
39BC: 00              NOP                         
39BD: 84              ADD     A,H                 
39BE: 1C              INC     E                   
39BF: 44              LD      B,H                 
39C0: 20 20           JR      NZ,$39E2            ; 
39C2: C3 1D 44        JP      $441D               ; 
39C5: D9              EXX                         
39C6: 39              ADD     HL,SP               
39C7: 40              LD      B,B                 
39C8: 81              ADD     A,C                 
39C9: 2C              INC     L                   
39CA: A1              AND     C                   
39CB: 98              SBC     B                   
39CC: 11 00 70        LD      DE,$7000            
39CF: 00              NOP                         
39D0: 00              NOP                         
39D1: 84              ADD     A,H                 
39D2: 23              INC     HL                  
39D3: 44              LD      B,H                 
39D4: 20 20           JR      NZ,$39F6            ; 
39D6: C3 24 44        JP      $4424               ; 
39D9: E7              RST     $20                 
39DA: 39              ADD     HL,SP               
39DB: 62              LD      H,D                 
39DC: 81              ADD     A,C                 
39DD: 60              LD      H,B                 
39DE: A0              AND     B                   
39DF: 13              INC     DE                  
39E0: 11 00 80        LD      DE,$8000            
39E3: 00              NOP                         
39E4: 00              NOP                         
39E5: 30 30           JR      NC,$3A17            ; 
39E7: 0C              INC     C                   
39E8: 3A 6E 81        LD      A,($816E)           ; 
39EB: 64              LD      H,H                 
39EC: A0              AND     B                   
39ED: 18 01           JR      $39F0               ; 
39EF: 00              NOP                         
39F0: 50              LD      D,B                 
39F1: 00              NOP                         
39F2: 00              NOP                         
39F3: 43              LD      B,E                 
39F4: 20 50           JR      NZ,$3A46            ; 
39F6: 20 20           JR      NZ,$3A18            ; 
39F8: 31 39 38        LD      SP,$3839            
39FB: 31 20 4D        LD      SP,$4D20            
39FE: 49              LD      C,C                 
39FF: 44              LD      B,H                 
3A00: 57              LD      D,A                 
3A01: 41              LD      B,C                 
3A02: 59              LD      E,C                 
3A03: 20 4D           JR      NZ,$3A52            ; 
3A05: 46              LD      B,(HL)              
3A06: 47              LD      B,A                 
3A07: 2E 20           LD      L,$20               
3A09: 43              LD      B,E                 
3A0A: 4F              LD      C,A                 
3A0B: 2E 00           LD      L,$00               
3A0D: 00              NOP                         
3A0E: 00              NOP                         
3A0F: A1              AND     C                   
3A10: A0              AND     B                   
3A11: 21 00 60        LD      HL,$6000            
3A14: 00              NOP                         
3A15: 00              NOP                         
3A16: 92              SUB     D                   
3A17: CD 92 CD        CALL    $CD92               ; 
3A1A: 92              SUB     D                   
3A1B: CD F4 A1        CALL    $A1F4               ; 
3A1E: 00              NOP                         
3A1F: 02              LD      (BC),A              
3A20: 00              NOP                         
3A21: 70              LD      (HL),B              
3A22: 00              NOP                         
3A23: 00              NOP                         
3A24: FA F0 00        JP      M,$00F0             ; 
3A27: A2              AND     D                   
3A28: 20 10           JR      NZ,$3A3A            ; 
3A2A: 00              NOP                         
3A2B: 80              ADD     A,B                 
3A2C: 00              NOP                         
3A2D: 00              NOP            
```

# Character Vectors

```code
VTableChars: 
; Character DJSR for letters A-Z
3A2E: 4D CC     ; (DJSR $8C4D)    A
3A30: 58 CC     ; (DJSR $8C58)    B
3A32: 64 CC     ; (DJSR $8C64)    C
3A34: 6C CC     ; (DJSR $8C6C)    D
3A36: 75 CC     ; (DJSR $8C75)    E
3A38: 77 CC     ; (DJSR $8C77)    F
3A3A: 7F CC     ; (DJSR $8C7F)    G
3A3C: 88 CC     ; (DJSR $8C88)    H
3A3E: 91 CC     ; (DJSR $8C91)    I
3A40: 9B CC     ; (DJSR $8C9B)    J
3A42: A3 CC     ; (DJSR $8CA3)    K
3A44: AB CC     ; (DJSR $8CAB)    L
3A46: B2 CC     ; (DJSR $8CB2)    M
3A48: BA CC     ; (DJSR $8CBA)    N
3A4A: C2 CC     ; (DJSR $8CC2)    O
3A4C: CA CC     ; (DJSR $8CCA)    P
3A4E: D2 CC     ; (DJSR $8CD2)    Q
3A50: DC CC     ; (DJSR $8CDC)    R
3A52: E6 CC     ; (DJSR $8CE6)    S
3A54: F0 CC     ; (DJSR $8CF0)    T
3A56: F8 CC     ; (DJSR $8CF8)    U
3A58: 02 CD     ; (DJSR $8D02)    V
3A5A: 0B CD     ; (DJSR $8D0B)    W
3A5C: 16 CD     ; (DJSR $8D16)    X
3A5E: 1D CD     ; (DJSR $8D1D)    Y
3A60: 27 CD     ; (DJSR $8D27)    Z
;
; The table continues but is never used. Note the pattern " E.R.A.S.E".
; I wonder if this would have shown up in a character test pattern.
;
3A62: 92 CD     ; (DJSR $8D92)    space
3A64: 75 CC     ; (DJSR $8C75)    E       (Note the pattern below ... E R A S E)
3A66: BF CD     ; (DJSR $8DBF)    CR/LF
3A68: DC CC     ; (DJSR $8CDC)    R
3A6A: BF CD     ; (DJSR $8DBF)    CR/LF
3A6C: 4D CC     ; (DJSR $8C4D)    A
3A6E: BF CD     ; (DJSR $8DBF)    CR/LF
3A70: E6 CC     ; (DJSR $8CE6)    S
3A72: BF CD     ; (DJSR $8DBF)    CR/LF
3A74: 75 CC     ; (DJSR $8C75)    E
           
3A76: 00              NOP                         
3A77: A2              AND     D                   
3A78: C0              RET     NZ                  
3A79: 13              INC     DE                  
3A7A: 00              NOP                         
3A7B: 80              ADD     A,B                 
3A7C: 00              NOP                         
3A7D: 00              NOP                         
3A7E: 75              LD      (HL),L              
3A7F: CC BF CD        CALL    Z,$CDBF             ; 
3A82: BA              CP      D                   
3A83: CC BF CD        CALL    Z,$CDBF             ; 
3A86: 6C              LD      L,H                 
3A87: CC 00 C8        CALL    Z,$C800             ; 
3A8A: 3A 7A 80        LD      A,($807A)           ; 
3A8D: 84              ADD     A,H                 
3A8E: A3              AND     E                   
3A8F: C0              RET     NZ                  
3A90: 00              NOP                         
3A91: 00              NOP                         
3A92: 90              SUB     B                   
3A93: 00              NOP                         
3A94: 00              NOP                         


3A95: 59 ; YOUR_SC                 
3A96: 4F              LD      C,A                 
3A97: 55              LD      D,L                 
3A98: 52              LD      D,D                 
3A99: 20 53           JR      NZ,$3AEE            ; 
3A9B: 43              LD      B,E                 
3A9C: 4F              LD      C,A                 
3A9D: 52              LD      D,D                 
3A9E: 45              LD      B,L                 
3A9F: 20 49           JR      NZ,$3AEA            ; 
3AA1: 53              LD      D,E                 
3AA2: 20 4F           JR      NZ,$3AF3            ; 
3AA4: 4E              LD      C,(HL)              
3AA5: 45              LD      B,L                 
3AA6: 20 4F           JR      NZ,$3AF7            ; 
3AA8: 46              LD      B,(HL)              
3AA9: 20 54           JR      NZ,$3AFF            ; 
3AAB: 48              LD      C,B                 
3AAC: 45              LD      B,L                 
3AAD: 20 54           JR      NZ,$3B03            ; 
3AAF: 4F              LD      C,A                 
3AB0: 50              LD      D,B                 
3AB1: 20 48           JR      NZ,$3AFB            ; 
3AB3: 49              LD      C,C                 
3AB4: 47              LD      B,A                 
3AB5: 48              LD      C,B                 
3AB6: 20 53           JR      NZ,$3B0B            ; 
3AB8: 43              LD      B,E                 
3AB9: 4F              LD      C,A                 
3ABA: 52              LD      D,D                 
3ABB: 45              LD      B,L                 
3ABC: 53              LD      D,E                 
3ABD: 2E 20           LD      L,$20               
3ABF: 20 20           JR      NZ,$3AE1            ; 
3AC1: 20 20           JR      NZ,$3AE3            ; 
3AC3: 20 20           JR      NZ,$3AE5            ; 
3AC5: 20 20           JR      NZ,$3AE7            ; 
3AC7: 20 0F           JR      NZ,$3AD8            ; 
3AC9: 3B              DEC     SP                  
3ACA: E8              RET     PE                  
3ACB: 80              ADD     A,B                 
3ACC: 64              LD      H,H                 
3ACD: A3              AND     E                   
3ACE: A0              AND     B                   
3ACF: 00              NOP                         
3AD0: 00              NOP                         
3AD1: 90              SUB     B                   
3AD2: 00              NOP                         
3AD3: 00              NOP                         
3AD4: 54              LD      D,H                 
3AD5: 4F              LD      C,A                 
3AD6: 20 45           JR      NZ,$3B1D            ; 
3AD8: 4E              LD      C,(HL)              
3AD9: 54              LD      D,H                 
3ADA: 45              LD      B,L                 
3ADB: 52              LD      D,D                 
3ADC: 20 59           JR      NZ,$3B37            ; 
3ADE: 4F              LD      C,A                 
3ADF: 55              LD      D,L                 
3AE0: 52              LD      D,D                 
3AE1: 20 49           JR      NZ,$3B2C            ; 
3AE3: 4E              LD      C,(HL)              
3AE4: 49              LD      C,C                 
3AE5: 54              LD      D,H                 
3AE6: 49              LD      C,C                 
3AE7: 41              LD      B,C                 
3AE8: 4C              LD      C,H                 
3AE9: 53              LD      D,E                 
3AEA: 2C              INC     L                   
3AEB: 20 54           JR      NZ,$3B41            ; 
3AED: 55              LD      D,L                 
3AEE: 52              LD      D,D                 
3AEF: 4E              LD      C,(HL)              
3AF0: 20 54           JR      NZ,$3B46            ; 
3AF2: 48              LD      C,B                 
3AF3: 45              LD      B,L                 
3AF4: 20 52           JR      NZ,$3B48            ; 
3AF6: 4F              LD      C,A                 
3AF7: 54              LD      D,H                 
3AF8: 41              LD      B,C                 
3AF9: 54              LD      D,H                 
3AFA: 45              LD      B,L                 
3AFB: 20 4B           JR      NZ,$3B48            ; 
3AFD: 4E              LD      C,(HL)              
3AFE: 4F              LD      C,A                 
3AFF: 42              LD      B,D                 
3B00: 20 20           JR      NZ,$3B22            ; 
3B02: 20 20           JR      NZ,$3B24            ; 
3B04: 20 20           JR      NZ,$3B26            ; 
3B06: 20 20           JR      NZ,$3B28            ; 
3B08: 20 20           JR      NZ,$3B2A            ; 
3B0A: 20 20           JR      NZ,$3B2C            ; 
3B0C: 20 20           JR      NZ,$3B2E            ; 
3B0E: 20 4E           JR      NZ,$3B5E            ; 
3B10: 3B              DEC     SP                  
3B11: 66              LD      H,(HL)              
3B12: 81              ADD     A,C                 
3B13: 42              LD      B,D                 
3B14: A3              AND     E                   
3B15: B8              CP      B                   
3B16: 00              NOP                         
3B17: 00              NOP                         
3B18: 90              SUB     B                   
3B19: 00              NOP                         
3B1A: 00              NOP                         
3B1B: 54              LD      D,H                 
3B1C: 4F              LD      C,A                 
3B1D: 20 53           JR      NZ,$3B72            ; 
3B1F: 45              LD      B,L                 
3B20: 4C              LD      C,H                 
3B21: 45              LD      B,L                 
3B22: 43              LD      B,E                 
3B23: 54              LD      D,H                 
3B24: 20 41           JR      NZ,$3B67            ; 
3B26: 20 4C           JR      NZ,$3B74            ; 
3B28: 45              LD      B,L                 
3B29: 54              LD      D,H                 
3B2A: 54              LD      D,H                 
3B2B: 45              LD      B,L                 
3B2C: 52              LD      D,D                 
3B2D: 20 41           JR      NZ,$3B70            ; 
3B2F: 4E              LD      C,(HL)              
3B30: 44              LD      B,H                 
3B31: 20 54           JR      NZ,$3B87            ; 
3B33: 48              LD      C,B                 
3B34: 45              LD      B,L                 
3B35: 4E              LD      C,(HL)              
3B36: 20 50           JR      NZ,$3B88            ; 
3B38: 52              LD      D,D                 
3B39: 45              LD      B,L                 
3B3A: 53              LD      D,E                 
3B3B: 53              LD      D,E                 
3B3C: 20 46           JR      NZ,$3B84            ; 
3B3E: 49              LD      C,C                 
3B3F: 52              LD      D,D                 
3B40: 45              LD      B,L                 
3B41: 20 54           JR      NZ,$3B97            ; 
3B43: 4F              LD      C,A                 
3B44: 20 20           JR      NZ,$3B66            ; 
3B46: 20 20           JR      NZ,$3B68            ; 
3B48: 20 20           JR      NZ,$3B6A            ; 
3B4A: 20 20           JR      NZ,$3B6C            ; 
3B4C: 20 20           JR      NZ,$3B6E            ; 
3B4E: 93              SUB     E                   
3B4F: 3B              DEC     SP                  
3B50: D4 81 20        CALL    NC,$2081            ; 
3B53: A3              AND     E                   
3B54: 78              LD      A,B                 
3B55: 01 00 90        LD      BC,$9000            
3B58: 00              NOP                         
3B59: 00              NOP                         
3B5A: 45              LD      B,L                 
3B5B: 4E              LD      C,(HL)              
3B5C: 54              LD      D,H                 
3B5D: 45              LD      B,L                 
3B5E: 52              LD      D,D                 
3B5F: 20 54           JR      NZ,$3BB5            ; 
3B61: 48              LD      C,B                 
3B62: 45              LD      B,L                 
3B63: 20 4C           JR      NZ,$3BB1            ; 
3B65: 45              LD      B,L                 
3B66: 54              LD      D,H                 
3B67: 54              LD      D,H                 
3B68: 45              LD      B,L                 
3B69: 52              LD      D,D                 
3B6A: 2E 20           LD      L,$20               
3B6C: 20 20           JR      NZ,$3B8E            ; 
3B6E: 20 20           JR      NZ,$3B90            ; 
3B70: 20 20           JR      NZ,$3B92            ; 
3B72: 20 20           JR      NZ,$3B94            ; 
3B74: 20 20           JR      NZ,$3B96            ; 
3B76: 20 20           JR      NZ,$3B98            ; 
3B78: 20 20           JR      NZ,$3B9A            ; 
3B7A: 20 20           JR      NZ,$3B9C            ; 
3B7C: 20 20           JR      NZ,$3B9E            ; 
3B7E: 20 20           JR      NZ,$3BA0            ; 
3B80: 20 20           JR      NZ,$3BA2            ; 
3B82: 20 20           JR      NZ,$3BA4            ; 
3B84: 20 20           JR      NZ,$3BA6            ; 
3B86: 20 20           JR      NZ,$3BA8            ; 
3B88: 20 20           JR      NZ,$3BAA            ; 
3B8A: 20 20           JR      NZ,$3BAC            ; 
3B8C: 20 20           JR      NZ,$3BAE            ; 
3B8E: 20 20           JR      NZ,$3BB0            ; 
3B90: 20 20           JR      NZ,$3BB2            ; 
3B92: 20 00           JR      NZ,$3B94            ; 
3B94: 00              NOP                         
3B95: 00              NOP                         
3B96: AB              XOR     E                   
3B97: 3B              DEC     SP                  
3B98: 4E              LD      C,(HL)              
3B99: 82              ADD     A,D                 
3B9A: A4              AND     H                   
3B9B: A3              AND     E                   
3B9C: 80              ADD     A,B                 
3B9D: 11 00 80        LD      DE,$8000            
3BA0: 00              NOP                         
3BA1: 00              NOP                         
3BA2: 50              LD      D,B                 
3BA3: 4C              LD      C,H                 
3BA4: 41              LD      B,C                 
3BA5: 59              LD      E,C                 
3BA6: 45              LD      B,L                 
3BA7: 52              LD      D,D                 
3BA8: 20 31           JR      NZ,$3BDB            ; 
3BAA: 20 00           JR      NZ,$3BAC            ; 
3BAC: 00              NOP                         
3BAD: 00              NOP                         
3BAE: C3 3B 4E        JP      $4E3B               ; 
3BB1: 82              ADD     A,D                 
3BB2: A4              AND     H                   
3BB3: A3              AND     E                   
3BB4: 80              ADD     A,B                 
3BB5: 11 00 70        LD      DE,$7000            
3BB8: 00              NOP                         
3BB9: 00              NOP                         
3BBA: 50              LD      D,B                 
3BBB: 4C              LD      C,H                 
3BBC: 41              LD      B,C                 
3BBD: 59              LD      E,C                 
3BBE: 45              LD      B,L                 
3BBF: 52              LD      D,D                 
3BC0: 20 32           JR      NZ,$3BF4            ; 
3BC2: 20 00           JR      NZ,$3BC4            ; 
3BC4: 00              NOP                         
3BC5: 00              NOP                         
3BC6: DC 3B 00        CALL    C,$003B             ; 
3BC9: 80              ADD     A,B                 
3BCA: 58              LD      E,B                 
3BCB: A2              AND     D                   
3BCC: 60              LD      H,B                 
3BCD: 11 00 80        LD      DE,$8000            
3BD0: 00              NOP                         
3BD1: 00              NOP                         
3BD2: 4F              LD      C,A                 
3BD3: 4D              LD      C,L                 
3BD4: 45              LD      B,L                 
3BD5: 47              LD      B,A                 
3BD6: 41              LD      B,C                 
3BD7: 20 52           JR      NZ,$3C2B            ; 
3BD9: 41              LD      B,C                 
3BDA: 43              LD      B,E                 
3BDB: 45              LD      B,L                 
3BDC: FC 3B 1C        CALL    M,$1C3B             ; 
3BDF: 80              ADD     A,B                 
3BE0: F4 A1 F0        CALL    P,$F0A1             ; 
3BE3: 10 00           DJNZ    $3BE5               ; 
3BE5: 70              LD      (HL),B              
3BE6: 00              NOP                         
3BE7: 00              NOP                         
3BE8: 31 20 43        LD      SP,$4320            
3BEB: 4F              LD      C,A                 
3BEC: 49              LD      C,C                 
3BED: 4E              LD      C,(HL)              
3BEE: 20 20           JR      NZ,$3C10            ; 
3BF0: 20 3D           JR      NZ,$3C2F            ; 
3BF2: 20 31           JR      NZ,$3C25            ; 
3BF4: 20 43           JR      NZ,$3C39            ; 
3BF6: 52              LD      D,D                 
3BF7: 45              LD      B,L                 
3BF8: 44              LD      B,H                 
3BF9: 49              LD      C,C                 
3BFA: 54              LD      D,H                 
3BFB: 20 1C           JR      NZ,$3C19            ; 
3BFD: 3C              INC     A                   
3BFE: 4C              LD      C,H                 
3BFF: 80              ADD     A,B                 
3C00: 90              SUB     B                   
3C01: A1              AND     C                   
3C02: F0              RET     P                   
3C03: 10 00           DJNZ    $3C05               ; 
3C05: 80              ADD     A,B                 
3C06: 00              NOP                         
3C07: 00              NOP                         
3C08: 32 20 43        LD      ($4320),A           ; 
3C0B: 4F              LD      C,A                 
3C0C: 49              LD      C,C                 
3C0D: 4E              LD      C,(HL)              
3C0E: 53              LD      D,E                 
3C0F: 20 20           JR      NZ,$3C31            ; 
3C11: 3D              DEC     A                   
3C12: 20 32           JR      NZ,$3C46            ; 
3C14: 20 43           JR      NZ,$3C59            ; 
3C16: 52              LD      D,D                 
3C17: 45              LD      B,L                 
3C18: 44              LD      B,H                 
3C19: 49              LD      C,C                 
3C1A: 54              LD      D,H                 
3C1B: 53              LD      D,E                 
3C1C: 00              NOP                         
3C1D: 00              NOP                         
3C1E: 00              NOP                         
3C1F: 43              LD      B,E                 
3C20: 3C              INC     A                   
3C21: 00              NOP                         
3C22: 80              ADD     A,B                 
3C23: 3E A3           LD      A,$A3               
3C25: E0              RET     PO                  
3C26: 00              NOP                         
3C27: 00              NOP                         
3C28: 90              SUB     B                   
3C29: 00              NOP                         
3C2A: 00              NOP                         
3C2B: 43              LD      B,E                 
3C2C: 4F              LD      C,A                 
3C2D: 49              LD      C,C                 
3C2E: 4E              LD      C,(HL)              
3C2F: 20 43           JR      NZ,$3C74            ; 
3C31: 48              LD      C,B                 
3C32: 55              LD      D,L                 
3C33: 54              LD      D,H                 
3C34: 45              LD      B,L                 
3C35: 20 31           JR      NZ,$3C68            ; 
3C37: 20 20           JR      NZ,$3C59            ; 
3C39: 20 20           JR      NZ,$3C5B            ; 
3C3B: 20 20           JR      NZ,$3C5D            ; 
3C3D: 20 20           JR      NZ,$3C5F            ; 
3C3F: 20 84           JR      NZ,$3BC5            ; 
3C41: 2A 44 67        LD      HL,($6744)          ; 
3C44: 3C              INC     A                   
3C45: 42              LD      B,D                 
3C46: 80              ADD     A,B                 
3C47: 16 A3           LD      D,$A3               
3C49: E0              RET     PO                  
3C4A: 00              NOP                         
3C4B: 00              NOP                         
3C4C: 80              ADD     A,B                 
3C4D: 00              NOP                         
3C4E: 00              NOP                         
3C4F: 43              LD      B,E                 
3C50: 4F              LD      C,A                 
3C51: 49              LD      C,C                 
3C52: 4E              LD      C,(HL)              
3C53: 20 43           JR      NZ,$3C98            ; 
3C55: 48              LD      C,B                 
3C56: 55              LD      D,L                 
3C57: 54              LD      D,H                 
3C58: 45              LD      B,L                 
3C59: 20 32           JR      NZ,$3C8D            ; 
3C5B: 20 20           JR      NZ,$3C7D            ; 
3C5D: 20 20           JR      NZ,$3C7F            ; 
3C5F: 20 20           JR      NZ,$3C81            ; 
3C61: 20 20           JR      NZ,$3C83            ; 
3C63: 20 84           JR      NZ,$3BE9            ; 
3C65: 2E 44           LD      L,$44               
3C67: 8B              ADC     A,E                 
3C68: 3C              INC     A                   
3C69: 84              ADD     A,H                 
3C6A: 80              ADD     A,B                 
3C6B: C6 A2           ADD     A,$A2               
3C6D: E0              RET     PO                  
3C6E: 00              NOP                         
3C6F: 00              NOP                         
3C70: 80              ADD     A,B                 
3C71: 00              NOP                         
3C72: 00              NOP                         
3C73: 54              LD      D,H                 
3C74: 45              LD      B,L                 
3C75: 53              LD      D,E                 
3C76: 54              LD      D,H                 
3C77: 20 43           JR      NZ,$3CBC            ; 
3C79: 52              LD      D,D                 
3C7A: 45              LD      B,L                 
3C7B: 44              LD      B,H                 
3C7C: 49              LD      C,C                 
3C7D: 54              LD      D,H                 
3C7E: 53              LD      D,E                 
3C7F: 20 20           JR      NZ,$3CA1            ; 
3C81: 20 20           JR      NZ,$3CA3            ; 
3C83: 20 20           JR      NZ,$3CA5            ; 
3C85: 20 20           JR      NZ,$3CA7            ; 
3C87: 20 84           JR      NZ,$3C0D            ; 
3C89: 32 44 C0        ;LD      ($C044),A           
3C8C: 3C              INC     A                   
3C8D: C6 80           ADD     A,$80               
3C8F: 26 A2           LD      H,$A2               
3C91: E0              RET     PO                  
3C92: 00              NOP                         
3C93: 00              NOP                         
3C94: 80              ADD     A,B                 
3C95: 00              NOP                         
3C96: 00              NOP                         
3C97: 20 20           JR      NZ,$3CB9            ; 
3C99: 20 20           JR      NZ,$3CBB            ; 
3C9B: 20 20           JR      NZ,$3CBD            ; 
3C9D: 20 20           JR      NZ,$3CBF            ; 
3C9F: 20 20           JR      NZ,$3CC1            ; 
3CA1: 20 20           JR      NZ,$3CC3            ; 
3CA3: 20 20           JR      NZ,$3CC5            ; 
3CA5: 20 20           JR      NZ,$3CC7            ; 
3CA7: 20 20           JR      NZ,$3CC9            ; 
3CA9: 20 20           JR      NZ,$3CCB            ; 
3CAB: 20 20           JR      NZ,$3CCD            ; 
3CAD: 31 20 43        LD      SP,$4320            
3CB0: 52              LD      D,D                 
3CB1: 45              LD      B,L                 
3CB2: 44              LD      B,H                 
3CB3: 49              LD      C,C                 
3CB4: 54              LD      D,H                 
3CB5: 20 20           JR      NZ,$3CD7            ; 
3CB7: 20 32           JR      NZ,$3CEB            ; 
3CB9: 20 43           JR      NZ,$3CFE            ; 
3CBB: 52              LD      D,D                 
3CBC: 45              LD      B,L                 
3CBD: 44              LD      B,H                 
3CBE: 49              LD      C,C                 
3CBF: 54              LD      D,H                 
3CC0: EA 3C 20        JP      PE,$203C            ; 
3CC3: 81              ADD     A,C                 
3CC4: D6 A1           SUB     $A1                 
3CC6: E0              RET     PO                  
3CC7: 00              NOP                         
3CC8: 00              NOP                         
3CC9: 90              SUB     B                   
3CCA: 00              NOP                         
3CCB: 00              NOP                         
3CCC: 46              LD      B,(HL)              
3CCD: 49              LD      C,C                 
3CCE: 52              LD      D,D                 
3CCF: 53              LD      D,E                 
3CD0: 54              LD      D,H                 
3CD1: 20 46           JR      NZ,$3D19            ; 
3CD3: 52              LD      D,D                 
3CD4: 45              LD      B,L                 
3CD5: 45              LD      B,L                 
3CD6: 20 53           JR      NZ,$3D2B            ; 
3CD8: 48              LD      C,B                 
3CD9: 49              LD      C,C                 
3CDA: 50              LD      D,B                 
3CDB: 20 20           JR      NZ,$3CFD            ; 
3CDD: 20 20           JR      NZ,$3CFF            ; 
3CDF: 20 20           JR      NZ,$3D01            ; 
3CE1: 84              ADD     A,H                 
3CE2: 3A 44 20        LD      A,($2044)           ; 
3CE5: 20 20           JR      NZ,$3D07            ; 
3CE7: 84              ADD     A,H                 
3CE8: 52              LD      D,D                 
3CE9: 44              LD      B,H                 
3CEA: 14              INC     D                   
3CEB: 3D              DEC     A                   
3CEC: 78              LD      A,B                 
3CED: 81              ADD     A,C                 
3CEE: AE              XOR     (HL)                
3CEF: A1              AND     C                   
3CF0: E0              RET     PO                  
3CF1: 00              NOP                         
3CF2: 00              NOP                         
3CF3: 90              SUB     B                   
3CF4: 00              NOP                         
3CF5: 00              NOP                         
3CF6: 53              LD      D,E                 
3CF7: 45              LD      B,L                 
3CF8: 43              LD      B,E                 
3CF9: 4F              LD      C,A                 
3CFA: 4E              LD      C,(HL)              
3CFB: 44              LD      B,H                 
3CFC: 20 46           JR      NZ,$3D44            ; 
3CFE: 52              LD      D,D                 
3CFF: 45              LD      B,L                 
3D00: 45              LD      B,L                 
3D01: 20 53           JR      NZ,$3D56            ; 
3D03: 48              LD      C,B                 
3D04: 49              LD      C,C                 
3D05: 50              LD      D,B                 
3D06: 20 20           JR      NZ,$3D28            ; 
3D08: 20 20           JR      NZ,$3D2A            ; 
3D0A: 20 84           JR      NZ,$3C90            ; 
3D0C: 3E 44           LD      A,$44               
3D0E: 20 20           JR      NZ,$3D30            ; 
3D10: 20 84           JR      NZ,$3C96            ; 
3D12: 56              LD      D,(HL)              
3D13: 44              LD      B,H                 
3D14: 3E 3D           LD      A,$3D               
3D16: D0              RET     NC                  
3D17: 81              ADD     A,C                 
3D18: 86              ADD     A,(HL)              
3D19: A1              AND     C                   
3D1A: E0              RET     PO                  
3D1B: 00              NOP                         
3D1C: 00              NOP                         
3D1D: 90              SUB     B                   
3D1E: 00              NOP                         
3D1F: 00              NOP                         
3D20: 54              LD      D,H                 
3D21: 48              LD      C,B                 
3D22: 49              LD      C,C                 
3D23: 52              LD      D,D                 
3D24: 44              LD      B,H                 
3D25: 20 46           JR      NZ,$3D6D            ; 
3D27: 52              LD      D,D                 
3D28: 45              LD      B,L                 
3D29: 45              LD      B,L                 
3D2A: 20 53           JR      NZ,$3D7F            ; 
3D2C: 48              LD      C,B                 
3D2D: 49              LD      C,C                 
3D2E: 50              LD      D,B                 
3D2F: 20 20           JR      NZ,$3D51            ; 
3D31: 20 20           JR      NZ,$3D53            ; 
3D33: 20 20           JR      NZ,$3D55            ; 
3D35: 84              ADD     A,H                 
3D36: 42              LD      B,D                 
3D37: 44              LD      B,H                 
3D38: 20 20           JR      NZ,$3D5A            ; 
3D3A: 20 84           JR      NZ,$3CC0            ; 
3D3C: 5A              LD      E,D                 
3D3D: 44              LD      B,H                 
3D3E: 68              LD      L,B                 
3D3F: 3D              DEC     A                   
3D40: 28 82           JR      Z,$3CC4             ; 
3D42: 36 A1           LD      (HL),$A1            
3D44: E0              RET     PO                  
3D45: 00              NOP                         
3D46: 00              NOP                         
3D47: 90              SUB     B                   
3D48: 00              NOP                         
3D49: 00              NOP                         
3D4A: 41              LD      B,C                 
3D4B: 56              LD      D,(HL)              
3D4C: 45              LD      B,L                 
3D4D: 52              LD      D,D                 
3D4E: 41              LD      B,C                 
3D4F: 47              LD      B,A                 
3D50: 45              LD      B,L                 
3D51: 20 53           JR      NZ,$3DA6            ; 
3D53: 43              LD      B,E                 
3D54: 4F              LD      C,A                 
3D55: 52              LD      D,D                 
3D56: 45              LD      B,L                 
3D57: 20 20           JR      NZ,$3D79            ; 
3D59: 20 20           JR      NZ,$3D7B            ; 
3D5B: 20 20           JR      NZ,$3D7D            ; 
3D5D: 20 20           JR      NZ,$3D7F            ; 
3D5F: 84              ADD     A,H                 
3D60: 74              LD      (HL),H              
3D61: 44              LD      B,H                 
3D62: 20 20           JR      NZ,$3D84            ; 
3D64: 20 84           JR      NZ,$3CEA            ; 
3D66: 7C              LD      A,H                 
3D67: 44              LD      B,H                 
3D68: 92              SUB     D                   
3D69: 3D              DEC     A                   
3D6A: 80              ADD     A,B                 
3D6B: 82              ADD     A,D                 
3D6C: 0E A1           LD      C,$A1               
3D6E: E0              RET     PO                  
3D6F: 00              NOP                         
3D70: 00              NOP                         
3D71: 90              SUB     B                   
3D72: 00              NOP                         
3D73: 00              NOP                         
3D74: 48              LD      C,B                 
3D75: 49              LD      C,C                 
3D76: 47              LD      B,A                 
3D77: 48              LD      C,B                 
3D78: 45              LD      B,L                 
3D79: 53              LD      D,E                 
3D7A: 54              LD      D,H                 
3D7B: 20 53           JR      NZ,$3DD0            ; 
3D7D: 43              LD      B,E                 
3D7E: 4F              LD      C,A                 
3D7F: 52              LD      D,D                 
3D80: 45              LD      B,L                 
3D81: 20 20           JR      NZ,$3DA3            ; 
3D83: 20 20           JR      NZ,$3DA5            ; 
3D85: 20 20           JR      NZ,$3DA7            ; 
3D87: 20 20           JR      NZ,$3DA9            ; 
3D89: 84              ADD     A,H                 
3D8A: D6 43           SUB     $43                 
3D8C: 20 20           JR      NZ,$3DAE            ; 
3D8E: 20 84           JR      NZ,$3D14            ; 
3D90: 00              NOP                         
3D91: 44              LD      B,H                 
3D92: C0              RET     NZ                  
3D93: 3D              DEC     A                   
3D94: D8              RET     C                   
3D95: 82              ADD     A,D                 
3D96: BE              CP      (HL)                
3D97: A0              AND     B                   
3D98: E0              RET     PO                  
3D99: 00              NOP                         
3D9A: 00              NOP                         
3D9B: 90              SUB     B                   
3D9C: 00              NOP                         
3D9D: 00              NOP                         
3D9E: 41              LD      B,C                 
3D9F: 56              LD      D,(HL)              
3DA0: 45              LD      B,L                 
3DA1: 52              LD      D,D                 
3DA2: 41              LD      B,C                 
3DA3: 47              LD      B,A                 
3DA4: 45              LD      B,L                 
3DA5: 20 53           JR      NZ,$3DFA            ; 
3DA7: 45              LD      B,L                 
3DA8: 43              LD      B,E                 
3DA9: 2E 20           LD      L,$20               
3DAB: 50              LD      D,B                 
3DAC: 45              LD      B,L                 
3DAD: 52              LD      D,D                 
3DAE: 20 47           JR      NZ,$3DF7            ; 
3DB0: 41              LD      B,C                 
3DB1: 4D              LD      C,L                 
3DB2: 45              LD      B,L                 
3DB3: 20 20           JR      NZ,$3DD5            ; 
3DB5: 83              ADD     A,E                 
3DB6: 78              LD      A,B                 
3DB7: 44              LD      B,H                 
3DB8: 20 20           JR      NZ,$3DDA            ; 
3DBA: 20 20           JR      NZ,$3DDC            ; 
3DBC: 20 83           JR      NZ,$3D41            ; 
3DBE: 80              ADD     A,B                 
3DBF: 44              LD      B,H                 
3DC0: EA 3D 30        JP      PE,$303D            ; 
3DC3: 83              ADD     A,E                 
3DC4: 96              SUB     (HL)                
3DC5: A0              AND     B                   
3DC6: E0              RET     PO                  
3DC7: 00              NOP                         
3DC8: 00              NOP                         
3DC9: 90              SUB     B                   
3DCA: 00              NOP                         
3DCB: 00              NOP                         
3DCC: 4D              LD      C,L                 
3DCD: 41              LD      B,C                 
3DCE: 58              LD      E,B                 
3DCF: 49              LD      C,C                 
3DD0: 4D              LD      C,L                 
3DD1: 55              LD      D,L                 
3DD2: 4D              LD      C,L                 
3DD3: 20 53           JR      NZ,$3E28            ; 
3DD5: 45              LD      B,L                 
3DD6: 43              LD      B,E                 
3DD7: 2E 20           LD      L,$20               
3DD9: 50              LD      D,B                 
3DDA: 45              LD      B,L                 
3DDB: 52              LD      D,D                 
3DDC: 20 47           JR      NZ,$3E25            ; 
3DDE: 41              LD      B,C                 
3DDF: 4D              LD      C,L                 
3DE0: 45              LD      B,L                 
3DE1: 84              ADD     A,H                 
3DE2: 4E              LD      C,(HL)              
3DE3: 44              LD      B,H                 
3DE4: 20 20           JR      NZ,$3E06            ; 
3DE6: 20 84           JR      NZ,$3D6C            ; 
3DE8: 66              LD      H,(HL)              
3DE9: 44              LD      B,H                 
3DEA: 0E 3E           LD      C,$3E               
3DEC: 88              ADC     A,B                 
3DED: 83              ADD     A,E                 
3DEE: 64              LD      H,H                 
3DEF: A0              AND     B                   
3DF0: E0              RET     PO                  
3DF1: 00              NOP                         
3DF2: 00              NOP                         
3DF3: 90              SUB     B                   
3DF4: 00              NOP                         
3DF5: 00              NOP                         
3DF6: 43              LD      B,E                 
3DF7: 55              LD      D,L                 
3DF8: 52              LD      D,D                 
3DF9: 52              LD      D,D                 
3DFA: 45              LD      B,L                 
3DFB: 4E              LD      C,(HL)              
3DFC: 54              LD      D,H                 
3DFD: 20 43           JR      NZ,$3E42            ; 
3DFF: 52              LD      D,D                 
3E00: 45              LD      B,L                 
3E01: 44              LD      B,H                 
3E02: 49              LD      C,C                 
3E03: 54              LD      D,H                 
3E04: 20 20           JR      NZ,$3E26            ; 
3E06: 20 20           JR      NZ,$3E28            ; 
3E08: 20 20           JR      NZ,$3E2A            ; 
3E0A: 20 81           JR      NZ,$3D8D            ; 
3E0C: 2D              DEC     L                   
3E0D: 40              LD      B,B                 
3E0E: 00              NOP                         
3E0F: 00              NOP                         
3E10: 00              NOP                         
3E11: 3E 3E           LD      A,$3E               
3E13: 16 80           LD      D,$80               
3E15: 8A              ADC     A,D                 
3E16: A2              AND     D                   
3E17: 00              NOP                         
3E18: 11 00 80        LD      DE,$8000            
3E1B: 00              NOP                         
3E1C: 00              NOP                         
3E1D: 20 44           JR      NZ,$3E63            ; 
3E1F: 52              LD      D,D                 
3E20: 4F              LD      C,A                 
3E21: 49              LD      C,C                 
3E22: 44              LD      B,H                 
3E23: 20 46           JR      NZ,$3E6B            ; 
3E25: 4F              LD      C,A                 
3E26: 52              LD      D,D                 
3E27: 43              LD      B,E                 
3E28: 45              LD      B,L                 
3E29: 20 45           JR      NZ,$3E70            ; 
3E2B: 4C              LD      C,H                 
3E2C: 49              LD      C,C                 
3E2D: 4D              LD      C,L                 
3E2E: 49              LD      C,C                 
3E2F: 4E              LD      C,(HL)              
3E30: 41              LD      B,C                 
3E31: 54              LD      D,H                 
3E32: 45              LD      B,L                 
3E33: 44              LD      B,H                 
3E34: 20 20           JR      NZ,$3E56            ; 
3E36: 20 20           JR      NZ,$3E58            ; 
3E38: 20 20           JR      NZ,$3E5A            ; 
3E3A: 20 20           JR      NZ,$3E5C            ; 
3E3C: 20 20           JR      NZ,$3E5E            ; 
3E3E: 5F              LD      E,A                 
3E3F: 3E 60           LD      A,$60               
3E41: 80              ADD     A,B                 
3E42: 90              SUB     B                   
3E43: A1              AND     C                   
3E44: D0              RET     NC                  
3E45: 10 00           DJNZ    $3E47               ; 
3E47: 80              ADD     A,B                 
3E48: 00              NOP                         
3E49: 00              NOP                         
3E4A: 35              DEC     (HL)                
3E4B: 2C              INC     L                   
3E4C: 30 30           JR      NC,$3E7E            ; 
3E4E: 30 20           JR      NC,$3E70            ; 
3E50: 42              LD      B,D                 
3E51: 4F              LD      C,A                 
3E52: 4E              LD      C,(HL)              
3E53: 55              LD      D,L                 
3E54: 53              LD      D,E                 
3E55: 20 50           JR      NZ,$3EA7            ; 
3E57: 4F              LD      C,A                 
3E58: 49              LD      C,C                 
3E59: 4E              LD      C,(HL)              
3E5A: 54              LD      D,H                 
3E5B: 53              LD      D,E                 
3E5C: 20 20           JR      NZ,$3E7E            ; 
3E5E: 20 00           JR      NZ,$3E60            ; 
3E60: 00              NOP                         
3E61: 00              NOP                         
3E62: 75              LD      (HL),L              
3E63: 3E 00           LD      A,$00               
3E65: 80              ADD     A,B                 
3E66: 8A              ADC     A,D                 
3E67: A2              AND     D                   
3E68: 20 10           JR      NZ,$3E7A            ; 
3E6A: 00              NOP                         
3E6B: 80              ADD     A,B                 
3E6C: 00              NOP                         
3E6D: 00              NOP                         
3E6E: 20 20           JR      NZ,$3E90            ; 
3E70: 46              LD      B,(HL)              
3E71: 49              LD      C,C                 
3E72: 52              LD      D,D                 
3E73: 53              LD      D,E                 
3E74: 54              LD      D,H                 
3E75: 00              NOP                         
3E76: 00              NOP                         
3E77: 00              NOP                         
3E78: 8B              ADC     A,E                 
3E79: 3E 00           LD      A,$00               
3E7B: 80              ADD     A,B                 
3E7C: 8A              ADC     A,D                 
3E7D: A2              AND     D                   
3E7E: 20 10           JR      NZ,$3E90            ; 
3E80: 00              NOP                         
3E81: 80              ADD     A,B                 
3E82: 00              NOP                         
3E83: 00              NOP                         
3E84: 20 53           JR      NZ,$3ED9            ; 
3E86: 45              LD      B,L                 
3E87: 43              LD      B,E                 
3E88: 4F              LD      C,A                 
3E89: 4E              LD      C,(HL)              
3E8A: 44              LD      B,H                 
3E8B: 00              NOP                         
3E8C: 00              NOP                         
3E8D: 00              NOP                         
3E8E: A1              AND     C                   
3E8F: 3E 00           LD      A,$00               
3E91: 80              ADD     A,B                 
3E92: 8A              ADC     A,D                 
3E93: A2              AND     D                   
3E94: 20 10           JR      NZ,$3EA6            ; 
3E96: 00              NOP                         
3E97: 80              ADD     A,B                 
3E98: 00              NOP                         
3E99: 00              NOP                         
3E9A: 20 20           JR      NZ,$3EBC            ; 
3E9C: 54              LD      D,H                 
3E9D: 48              LD      C,B                 
3E9E: 49              LD      C,C                 
3E9F: 52              LD      D,D                 
3EA0: 44              LD      B,H                 
3EA1: 00              NOP                         
3EA2: 00              NOP                         
3EA3: 00              NOP                         
3EA4: B7              OR      A                   
3EA5: 3E 00           LD      A,$00               
3EA7: 80              ADD     A,B                 
3EA8: 8A              ADC     A,D                 
3EA9: A2              AND     D                   
3EAA: 20 10           JR      NZ,$3EBC            ; 
3EAC: 00              NOP                         
3EAD: 80              ADD     A,B                 
3EAE: 00              NOP                         
3EAF: 00              NOP                         
3EB0: 20 46           JR      NZ,$3EF8            ; 
3EB2: 4F              LD      C,A                 
3EB3: 55              LD      D,L                 
3EB4: 52              LD      D,D                 
3EB5: 54              LD      D,H                 
3EB6: 48              LD      C,B                 
3EB7: 00              NOP                         
3EB8: 00              NOP                         
3EB9: 00              NOP                         
3EBA: CD 3E 00        CALL    $003E               ; 
3EBD: 80              ADD     A,B                 
3EBE: 8A              ADC     A,D                 
3EBF: A2              AND     D                   
3EC0: 20 10           JR      NZ,$3ED2            ; 
3EC2: 00              NOP                         
3EC3: 80              ADD     A,B                 
3EC4: 00              NOP                         
3EC5: 00              NOP                         
3EC6: 20 20           JR      NZ,$3EE8            ; 
3EC8: 46              LD      B,(HL)              
3EC9: 49              LD      C,C                 
3ECA: 46              LD      B,(HL)              
3ECB: 54              LD      D,H                 
3ECC: 48              LD      C,B                 
3ECD: 00              NOP                         
3ECE: 00              NOP                         
3ECF: 00              NOP                         
3ED0: E3              EX      (SP),HL             
3ED1: 3E 00           LD      A,$00               
3ED3: 80              ADD     A,B                 
3ED4: 8A              ADC     A,D                 
3ED5: A2              AND     D                   
3ED6: 20 10           JR      NZ,$3EE8            ; 
3ED8: 00              NOP                         
3ED9: 80              ADD     A,B                 
3EDA: 00              NOP                         
3EDB: 00              NOP                         
3EDC: 41              LD      B,C                 
3EDD: 4E              LD      C,(HL)              
3EDE: 4F              LD      C,A                 
3EDF: 54              LD      D,H                 
3EE0: 48              LD      C,B                 
3EE1: 45              LD      B,L                 
3EE2: 52              LD      D,D                 
3EE3: 00              NOP                         
3EE4: 00              NOP                         
3EE5: 5F              LD      E,A                 
3EE6: C1              POP     BC                  
3EE7: CB C0           SET     0,B                 
3EE9: 71              LD      (HL),C              
3EEA: C1              POP     BC                  
3EEB: 23              INC     HL                  
3EEC: C1              POP     BC                  
3EED: 2C              INC     L                   
3EEE: C1              POP     BC                  
3EEF: 8D              ADC     A,L                 
3EF0: C1              POP     BC                  
3EF1: D5              PUSH    DE                  
3EF2: C0              RET     NZ                  
3EF3: 9A              SBC     D                   
3EF4: C1              POP     BC                  
3EF5: 5F              LD      E,A                 
3EF6: C1              POP     BC                  
3EF7: CB C0           SET     0,B                 
3EF9: 2C              INC     L                   
3EFA: C1              POP     BC                  
3EFB: 8D              ADC     A,L                 
3EFC: C1              POP     BC                  
3EFD: D5              PUSH    DE                  
3EFE: C0              RET     NZ                  
3EFF: 71              LD      (HL),C              
3F00: C1              POP     BC                  
3F01: 23              INC     HL                  
3F02: C1              POP     BC                  
3F03: 9A              SBC     D                   
3F04: C1              POP     BC                  
3F05: 5F              LD      E,A                 
3F06: C1              POP     BC                  
3F07: 23              INC     HL                  
3F08: C1              POP     BC                  
3F09: 8D              ADC     A,L                 
3F0A: C1              POP     BC                  
3F0B: D5              PUSH    DE                  
3F0C: C0              RET     NZ                  
3F0D: 71              LD      (HL),C              
3F0E: C1              POP     BC                  
3F0F: CB C0           SET     0,B                 
3F11: 2C              INC     L                   
3F12: C1              POP     BC                  
3F13: 9A              SBC     D                   
3F14: C1              POP     BC                  
3F15: 17              RLA                         
3F16: 32 F5 33        LD      ($33F5),A           ; 
3F19: A7              AND     A                   
3F1A: 34              INC     (HL)                
3F1B: 7A              LD      A,D                 
3F1C: 35              DEC     (HL)                
3F1D: A4              AND     H                   
3F1E: 36 C9           LD      (HL),$C9            
3F20: 36 F5           LD      (HL),$F5            
3F22: 36 1A           LD      (HL),$1A            
3F24: 37              SCF                         
3F25: 3F              CCF                         
3F26: 37              SCF                         
3F27: 57              LD      D,A                 
3F28: 37              SCF                         
3F29: 6F              LD      L,A                 
3F2A: 37              SCF                         
3F2B: 96              SUB     (HL)                
3F2C: 37              SCF                         
3F2D: B5              OR      L                   
3F2E: 37              SCF                         
3F2F: D5              PUSH    DE                  
3F30: 37              SCF                         
3F31: EE 37           XOR     $37                 
3F33: FD
3F34: 38 88           JR      C,$3EBE             ; 
3F36: 3A 95 3B        LD      A,($3B95)           ; 
3F39: AD              XOR     L                   
3F3A: 3B              DEC     SP                  
3F3B: C5              PUSH    BC                  
3F3C: 3B              DEC     SP                  
3F3D: 1E 3C           LD      E,$3C               
3F3F: 10 3E           DJNZ    $3F7F               ; 
3F41: 61              LD      H,C                 
3F42: 3E 77           LD      A,$77               
3F44: 3E 8D           LD      A,$8D               
3F46: 3E A3           LD      A,$A3               
3F48: 3E B9           LD      A,$B9               
3F4A: 3E CF           LD      A,$CF               
3F4C: 3E 04           LD      A,$04               
3F4E: CA 2E CA        JP      Z,$CA2E             ; 
3F51: 51              LD      D,C                 
3F52: CA 74 CA        JP      Z,$CA74             ; 
3F55: 97              SUB     A                   
3F56: CA AA CA        JP      Z,$CAAA             ; 
3F59: BE              CP      (HL)                
3F5A: CA D2 CA        JP      Z,$CAD2             ; 
3F5D: 12              LD      (DE),A              
3F5E: CC BA CB        CALL    Z,$CBBA             ; 
3F61: D8              RET     C                   
3F62: CB 12           RL      D                   
3F64: CC C5 C0        CALL    Z,$C0C5             ; 
3F67: 20 20           JR      NZ,$3F89            ; 
3F69: E0              RET     PO                  
3F6A: A1              AND     C                   
3F6B: F2 02 00        JP      P,$0002             ; 
3F6E: 60              LD      H,B                 
3F6F: 00              NOP                         
3F70: 00              NOP                         
3F71: E9              JP      (HL)                
3F72: C9              RET                         
3F73: 08              EX      AF,AF'              
3F74: A2              AND     D                   
3F75: F2 02 00        JP      P,$0002             ; 
3F78: 50              LD      D,B                 
3F79: 00              NOP                         
3F7A: 00              NOP                         
3F7B: E9              JP      (HL)                
3F7C: C9              RET                         
3F7D: 30 A2           JR      NC,$3F21            ; 
3F7F: F2 02 00        JP      P,$0002             ; 
3F82: 50              LD      D,B                 
3F83: 00              NOP                         
3F84: 00              NOP                         
3F85: E9              JP      (HL)                
3F86: C9              RET                         
3F87: B8              CP      B                   
3F88: A1              AND     C                   
3F89: 24              INC     H                   
3F8A: 03              INC     BC                  
3F8B: 00              NOP                         
3F8C: 60              LD      H,B                 
3F8D: 00              NOP                         
3F8E: 00              NOP                         
3F8F: E9              JP      (HL)                
3F90: C9              RET                         
3F91: E0              RET     PO                  
3F92: A1              AND     C                   
3F93: 24              INC     H                   
3F94: 03              INC     BC                  
3F95: 00              NOP                         
3F96: 50              LD      D,B                 
3F97: 00              NOP                         
3F98: 00              NOP                         
3F99: E9              JP      (HL)                
3F9A: C9              RET                         
3F9B: 08              EX      AF,AF'              
3F9C: A2              AND     D                   
3F9D: 24              INC     H                   
3F9E: 03              INC     BC                  
3F9F: 00              NOP                         
3FA0: 50              LD      D,B                 
3FA1: 00              NOP                         
3FA2: 00              NOP                         
3FA3: E9              JP      (HL)                
3FA4: C9              RET                         
3FA5: 30 A2           JR      NC,$3F49            ; 
3FA7: 24              INC     H                   
3FA8: 03              INC     BC                  
3FA9: 00              NOP                         
3FAA: 50              LD      D,B                 
3FAB: 00              NOP                         
3FAC: 00              NOP                         
3FAD: E9              JP      (HL)                
3FAE: C9              RET                         
3FAF: 1C              INC     E                   
3FB0: A2              AND     D                   
3FB1: C0              RET     NZ                  
3FB2: 02              LD      (BC),A              
3FB3: 00              NOP                         
3FB4: 60              LD      H,B                 
3FB5: 00              NOP                         
3FB6: 00              NOP                         
3FB7: 07              RLCA                        
3FB8: C8              RET     Z                   
3FB9: F4 A1 C0        CALL    P,$C0A1             ; 
3FBC: 02              LD      (BC),A              
3FBD: 00              NOP                         
3FBE: 50              LD      D,B                 
3FBF: 00              NOP                         
3FC0: 00              NOP                         
3FC1: 07              RLCA                        
3FC2: C8              RET     Z                   
3FC3: CC A1 C0        CALL    Z,$C0A1             ; 
3FC6: 02              LD      (BC),A              
3FC7: 00              NOP                         
3FC8: 50              LD      D,B                 
3FC9: 00              NOP                         
3FCA: 00              NOP                         
3FCB: 07              RLCA                        
3FCC: C8              RET     Z                   
3FCD: 00              NOP                         
3FCE: D0              RET     NC                  
3FCF: AA              XOR     D                   
3FD0: CD B3 CD        CALL    $CDB3         ; 
```

# Number Vectors

```code
VTableNums: 
; Character DJSR calls for numbers and etc      
3FD3: D3 CD     ; (DJSR $8DD3)   player
3FD5: 2F CD     ; (DJSR $8D2F)   0
3FD7: 3B CD     ; (DJSR $8D3B)   1
3FD9: 46 CD     ; (DJSR $8D46)   2
3FDB: 52 CD     ; (DJSR $8D52)   3
3FDD: 64 CD     ; (DJSR $8D64)   4
3FDF: 6F CD     ; (DJSR $8D6F)   5
3FE1: 81 CD     ; (DJSR $8D81)   6
3FE3: 8D CD     ; (DJSR $8D8D)   7
3FE5: 94 CD     ; (DJSR $8D94)   8
3FE7: A0 CD     ; (DJSR $8DA0)   9
3FE9: 92 CD     ; (DJSR $8D92)   space
3FEB: A7 CB     ; (DJSR $8BA7)   triangle (up)
3FED: 00 D0     ; (DRTSL)   
3FEF: CA CD     ; (DJSR $8DCA)   - 
3FF1: AF CB     ; (DJSR $8BAF)   triangles (up and down)
3FF3: 04 CA     ; (DJSR $8A04)   circle with triangle
3FF5: 2E CA     ; (DJSR $8A2E)   circle (no triangle)

3FF7: 01 00 00 00 D6 00 00 00 1F
```
