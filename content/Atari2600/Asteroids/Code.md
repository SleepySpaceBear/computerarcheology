![Atari2600 Asteroids](A2600Asteroids.jpg)

# Atari 2600 Asteroids

>>> cpu 6502

>>> binary D000:ASTEROID.BIN

>>> memoryTable hard 

[Hardware Info](../Stella.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

# Start

```plainCode
; The code is designed to run in 2 * 4K bank-switch mode or
; flat 8K mode (in 12K map ... D000 to FFFF).

; B9       bumped every frame for odd/even task switching

; E4,E5    D0xx
; E6,E7    D1xx

; E8
; E9
; EA
; EB

; EC,ED    DFxx   Asteroid pictures
; EE,EF    DFxx   Asteroid pictures
; F0,F1    DExx
; F2,F3    DExx

; F4,F5    pointer to digit memory for building digit images
; F6       value of digit 0
; F7       value of digit 1
; F8       value of digit 2
; F9       value of digit 3
; FA       value of digit 4
; FB       value of digit 6 (digit 5 is always blank)
; FC       Digit image 0    (00F4),F6
; FD       Digit image 1,2  (00F4),F7 combined with (00F4),F8
; FE       Digit image 3,4  (00F4),F9 combined with (00F4),FA
; FF       Digit image 5,6  (00F4),FB (always a single digit)
```

# Bank 0

```code
Bank0:

D000: 4C DA F9        JMP     $F9DA               ; {code.Reset1} Jump to reset vector ... in Bank 1. Good for flat 8K version.

D003: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D005: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE Apply horizontal motionHMOVE:lots
D007: 85 1C           STA     $1C                 ; {hard.GRP1} GRP1 Graphics player 1 bitsGRP1:lots
D009: 86 05           STX     $05                 ; {hard.NUSIZ1} Number/size player 1 missileNUSIZ1:lots
D00B: 6C E3 00        JMP     ($00E3)             ; {ram.mE3}

D00E: EA              NOP                         
D00F: 08              PHP                         
D010: 28              PLP                         
D011: EA              NOP                         
D012: EA              NOP                         
D013: A5 E9           LDA     $E9                 ; {ram.mE9}
D015: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D017: 85 20           STA     $20                 ; {hard.HMP0} HMP0:lots
D019: A9 83           LDA     #$83                
D01B: 85 E3           STA     $E3                 ; {ram.mE3}
D01D: A6 E7           LDX     $E7                 ; {ram.mE7}
D01F: A9 00           LDA     #$00                
D021: CA              DEX                         
D022: D0 05           BNE     $D029               ; {}
D024: 85 10           STA     $10                 ; {hard.RESP0}
D026: 4C 00 D1        JMP     $D100               ; {}

D029: CA              DEX                         
D02A: D0 04           BNE     $D030               ; {}
D02C: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D02E: F0 F6           BEQ     $D026               ; {}
D030: CA              DEX                         
D031: D0 04           BNE     $D037               ; {}
D033: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D035: F0 EF           BEQ     $D026               ; {}
D037: CA              DEX                         
D038: D0 05           BNE     $D03F               ; {}
D03A: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D03C: 4C 00 D1        JMP     $D100               ; {}

D03F: CA              DEX                         
D040: EA              NOP                         
D041: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D043: 4C 02 D1        JMP     $D102               ; {}

D046: A6 E7           LDX     $E7                 ; {ram.mE7}
D048: CA              DEX                         
D049: D0 05           BNE     $D050               ; {}
D04B: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D04D: EA              NOP                         
D04E: F0 05           BEQ     $D055               ; {}
D050: CA              DEX                         
D051: D0 05           BNE     $D058               ; {}
D053: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D055: EA              NOP                         
D056: F0 05           BEQ     $D05D               ; {}
D058: CA              DEX                         
D059: D0 05           BNE     $D060               ; {}
D05B: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D05D: EA              NOP                         
D05E: F0 05           BEQ     $D065               ; {}
D060: CA              DEX                         
D061: D0 05           BNE     $D068               ; {}
D063: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D065: EA              NOP                         
D066: F0 05           BEQ     $D06D               ; {}
D068: CA              DEX                         
D069: D0 05           BNE     $D070               ; {}
D06B: 85 10           STA     $10                 ; {hard.RESP0}
D06D: EA              NOP                         
D06E: F0 04           BEQ     $D074               ; {}
D070: CA              DEX                         
D071: EA              NOP                         
D072: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D074: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D076: A5 E9           LDA     $E9                 ; {ram.mE9}
D078: 85 20           STA     $20                 ; {hard.HMP0} HMP0:lots
D07A: A9 83           LDA     #$83                
D07C: 85 E3           STA     $E3                 ; {ram.mE3}
D07E: A9 00           LDA     #$00                
D080: 4C 00 D1        JMP     $D100               ; {}

D083: A2 00           LDX     #$00                
D085: A1 EF           LDA     ($EF,X)             ; {ram.mEF}
D087: D0 19           BNE     $D0A2               ; {}
D089: E6 DC           INC     $DC                 ; {ram.mDC}
D08B: A6 DC           LDX     $DC                 ; {ram.mDC}
D08D: B5 95           LDA     $95,X               ; {ram.m95}
D08F: 85 2B           STA     $2B                 ; {hard.HMCLR} Clear horizontal motion (strobe)HMCLR:lots
D091: 85 E9           STA     $E9                 ; {ram.mE9}
D093: 4A              LSR     A                   
D094: 29 07           AND     #$07                
D096: 85 E7           STA     $E7                 ; {ram.mE7}
D098: A9 C0           LDA     #$C0                
D09A: 85 E3           STA     $E3                 ; {ram.mE3}
D09C: A9 00           LDA     #$00                
D09E: AA              TAX                         
D09F: 4C 00 D1        JMP     $D100               ; {}

D0A2: 85 2B           STA     $2B                 ; {hard.HMCLR} Clear horizontal motion (strobe)HMCLR:lots
D0A4: 85 20           STA     $20                 ; {hard.HMP0} Horizontal motion value (player 1)HMP0:lots
D0A6: 85 F3           STA     $F3                 ; {ram.mF3}
D0A8: A6 F8           LDX     $F8                 ; {ram.mF8}
D0AA: BD 75 DE        LDA     $DE75,X             ; {}
D0AD: 85 06           STA     $06                 ; {hard.COLUP0} COLUP0 ... color of asteroidCOLUP0:lots
D0AF: A2 00           LDX     #$00                ; Read asteroid ...
D0B1: A1 EB           LDA     ($EB,X)             ; {ram.mEB} ... image from (EB)
D0B3: E6 EB           INC     $EB                 ; {ram.mEB} Next image bits
D0B5: E6 EF           INC     $EF                 ; {ram.mEF}
D0B7: EA              NOP                         ; Kill ...
D0B8: EA              NOP                         ; ... some ...
D0B9: EA              NOP                         ; ... time
D0BA: A6 F3           LDX     $F3                 ; {ram.mF3}
D0BC: EA              NOP                         
D0BD: 4C 02 D1        JMP     $D102               ; {}

D0C0: A6 DC           LDX     $DC                 ; {ram.mDC}
D0C2: B5 A7           LDA     $A7,X               ; {ram.mA7}
D0C4: 29 70           AND     #$70                
D0C6: 85 EB           STA     $EB                 ; {ram.mEB}
D0C8: 85 EF           STA     $EF                 ; {ram.mEF}
D0CA: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D0CC: B5 A7           LDA     $A7,X               ; {ram.mA7}
D0CE: 29 07           AND     #$07                
D0D0: 85 F8           STA     $F8                 ; {ram.mF8}
D0D2: EA              NOP                         
D0D3: EA              NOP                         
D0D4: EA              NOP                         
D0D5: 98              TYA                         
D0D6: D5 83           CMP     $83,X               ; {ram.m83}
D0D8: D0 1A           BNE     $D0F4               ; {}
D0DA: A5 E9           LDA     $E9                 ; {ram.mE9}
D0DC: 6A              ROR     A                   
D0DD: A2 46           LDX     #$46                
D0DF: B0 0A           BCS     $D0EB               ; {}
D0E1: A2 0E           LDX     #$0E                
D0E3: 86 E3           STX     $E3                 ; {ram.mE3}
D0E5: A9 00           LDA     #$00                
D0E7: AA              TAX                         
D0E8: 4C 02 D1        JMP     $D102               ; {}

D0EB: 8E E3 00        STX     $00E3               ; {ram.mE3}
D0EE: A9 00           LDA     #$00                
D0F0: AA              TAX                         
D0F1: 4C 02 D1        JMP     $D102               ; {}

D0F4: A9 00           LDA     #$00                
D0F6: AA              TAX                         
D0F7: 4C 00 D1        JMP     $D100               ; {}

D0FA: 4C 2B D4        JMP     $D42B               ; {}
D0FD: 00              BRK                         
D0FE: 00              BRK                         
D0FF: 00              BRK                         

D100: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D102: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE Apply horizontal motionHMOVE:lots
D104: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0 Graphics player 0GRP0:lots
D106: 86 04           STX     $04                 ; {hard.NUSIZ0} Number/size player 0 missileNUSIZ0:lots
D108: 6C E5 00        JMP     ($00E5)             ; {ram.mE5}

D10B: C8              INY                         
D10C: 08              PHP                         
D10D: 28              PLP                         
D10E: C0 59           CPY     #$59                
D110: F0 E8           BEQ     $D0FA               ; {}
D112: A5 EA           LDA     $EA                 ; {ram.mEA}
D114: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D116: 85 21           STA     $21                 ; {hard.HMP1} HMP1:lots
D118: A9 88           LDA     #$88                
D11A: 85 E5           STA     $E5                 ; {ram.mE5}
D11C: A6 E8           LDX     $E8                 ; {ram.mE8}
D11E: A9 00           LDA     #$00                
D120: CA              DEX                         
D121: D0 05           BNE     $D128               ; {}
D123: 85 11           STA     $11                 ; {hard.RESP1}
D125: 4C 03 D0        JMP     $D003               ; {}
D128: CA              DEX                         
D129: D0 04           BNE     $D12F               ; {}
D12B: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D12D: F0 F6           BEQ     $D125               ; {}
D12F: CA              DEX                         
D130: D0 04           BNE     $D136               ; {}
D132: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D134: F0 EF           BEQ     $D125               ; {}
D136: CA              DEX                         
D137: D0 05           BNE     $D13E               ; {}
D139: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D13B: 4C 03 D0        JMP     $D003               ; {}
D13E: CA              DEX                         
D13F: EA              NOP                         
D140: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D142: 4C 05 D0        JMP     $D005               ; {}
D145: A6 E8           LDX     $E8                 ; {ram.mE8}
D147: CA              DEX                         
D148: D0 05           BNE     $D14F               ; {}
D14A: 85 11           STA     $11                 ; {hard.RESP1}
D14C: EA              NOP                         
D14D: F0 05           BEQ     $D154               ; {}
D14F: CA              DEX                         
D150: D0 05           BNE     $D157               ; {}
D152: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D154: EA              NOP                         
D155: F0 05           BEQ     $D15C               ; {}
D157: CA              DEX                         
D158: D0 05           BNE     $D15F               ; {}
D15A: 85 11           STA     $11                 ; {hard.RESP1}
D15C: EA              NOP                         
D15D: F0 05           BEQ     $D164               ; {}
D15F: CA              DEX                         
D160: D0 05           BNE     $D167               ; {}
D162: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D164: EA              NOP                         
D165: F0 05           BEQ     $D16C               ; {}
D167: CA              DEX                         
D168: D0 05           BNE     $D16F               ; {}
D16A: 85 11           STA     $11                 ; {hard.RESP1}
D16C: EA              NOP                         
D16D: F0 04           BEQ     $D173               ; {}
D16F: CA              DEX                         
D170: EA              NOP                         
D171: 85 11           STA     $11                 ; {hard.RESP1}
D173: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D175: A5 EA           LDA     $EA                 ; {ram.mEA}
D177: 85 21           STA     $21                 ; {hard.HMP1} HMP1:lots
D179: C8              INY                         
D17A: C0 59           CPY     #$59                
D17C: F0 4E           BEQ     $D1CC               ; {}
D17E: A9 88           LDA     #$88                
D180: 85 E5           STA     $E5                 ; {ram.mE5}
D182: A9 00           LDA     #$00                
D184: EA              NOP                         
D185: 4C 05 D0        JMP     $D005               ; {}
D188: A2 00           LDX     #$00                
D18A: A1 F1           LDA     ($F1,X)             ; {ram.mF1}
D18C: D0 1E           BNE     $D1AC               ; {}
D18E: E6 DD           INC     $DD                 ; {ram.mDD}
D190: A6 DD           LDX     $DD                 ; {ram.mDD}
D192: B5 95           LDA     $95,X               ; {ram.m95}
D194: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D196: 85 EA           STA     $EA                 ; {ram.mEA}
D198: 4A              LSR     A                   
D199: 29 07           AND     #$07                
D19B: 85 E8           STA     $E8                 ; {ram.mE8}
D19D: C8              INY                         
D19E: C0 59           CPY     #$59                
D1A0: F0 2A           BEQ     $D1CC               ; {}
D1A2: A9 CF           LDA     #$CF                
D1A4: 85 E5           STA     $E5                 ; {ram.mE5}
D1A6: A9 00           LDA     #$00                
D1A8: AA              TAX                         
D1A9: 4C 03 D0        JMP     $D003               ; {}
D1AC: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D1AE: 85 21           STA     $21                 ; {hard.HMP1} HMP1:lots
D1B0: 85 F3           STA     $F3                 ; {ram.mF3}
D1B2: A6 F9           LDX     $F9                 ; {ram.mF9}
D1B4: BD 75 DE        LDA     $DE75,X             ; {}
D1B7: 85 07           STA     $07                 ; {hard.COLUP1} COLUP1:lots
D1B9: A2 00           LDX     #$00                
D1BB: A1 ED           LDA     ($ED,X)             ; {ram.mED}
D1BD: E6 ED           INC     $ED                 ; {ram.mED}
D1BF: E6 F1           INC     $F1                 ; {ram.mF1}
D1C1: C8              INY                         
D1C2: C0 59           CPY     #$59                
D1C4: F0 06           BEQ     $D1CC               ; {}
D1C6: A6 F3           LDX     $F3                 ; {ram.mF3}
D1C8: EA              NOP                         
D1C9: 4C 05 D0        JMP     $D005               ; {}
D1CC: 4C 2B D4        JMP     $D42B               ; {}
D1CF: A6 DD           LDX     $DD                 ; {ram.mDD}
D1D1: B5 A7           LDA     $A7,X               ; {ram.mA7}
D1D3: 29 70           AND     #$70                
D1D5: 85 ED           STA     $ED                 ; {ram.mED}
D1D7: 85 F1           STA     $F1                 ; {ram.mF1}
D1D9: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D1DB: B5 A7           LDA     $A7,X               ; {ram.mA7}
D1DD: 29 07           AND     #$07                
D1DF: 85 F9           STA     $F9                 ; {ram.mF9}
D1E1: 98              TYA                         
D1E2: D5 83           CMP     $83,X               ; {ram.m83}
D1E4: D0 27           BNE     $D20D               ; {}
D1E6: A5 EA           LDA     $EA                 ; {ram.mEA}
D1E8: 6A              ROR     A                   
D1E9: A2 45           LDX     #$45                
D1EB: B0 13           BCS     $D200               ; {}
D1ED: A2 0B           LDX     #$0B                
D1EF: 86 E5           STX     $E5                 ; {ram.mE5}
D1F1: A9 00           LDA     #$00                
D1F3: C8              INY                         
D1F4: C0 59           CPY     #$59                
D1F6: F0 20           BEQ     $D218               ; {}
D1F8: AA              TAX                         
D1F9: 4C 05 D0        JMP     $D005               ; {}
D1FC: 4C 2D D4        JMP     $D42D               ; {}
D1FF: 00              BRK                         
D200: 86 E5           STX     $E5                 ; {ram.mE5}
D202: A9 00           LDA     #$00                
D204: C8              INY                         
D205: C0 59           CPY     #$59                
D207: F0 F3           BEQ     $D1FC               ; {}
D209: AA              TAX                         
D20A: 4C 05 D0        JMP     $D005               ; {}
D20D: C8              INY                         
D20E: C0 59           CPY     #$59                
D210: F0 BA           BEQ     $D1CC               ; {}
D212: A9 00           LDA     #$00                
D214: AA              TAX                         
D215: 4C 03 D0        JMP     $D003               ; {}
D218: 4C 2D D4        JMP     $D42D               ; {}
```

# Visible Frame

```code
VisibleFrame:

; Draw digit lines
; The score is 5 digits with the right always 01234 ..... 56.

; FC ... digit image 0    (00F4),F6
; FD ... digit image 1,2  (00F4),F7 combined with (00F4),F8
; FE ... digit image 3,4  (00F4),F9 combined with (00F4),FA
; FF ... digit image 5,6  (00F4),FB (always a single digit)

D21B: A6 F3           LDX     $F3                 ; {ram.mF3}

D21D: A5 FC           LDA     $FC                 ; {ram.mFC} Left PF0 value
D21F: 85 02           STA     $02                 ; {hard.WSYNC} WSYNC Skip two ...WSYNC:41
D221: 85 02           STA     $02                 ; {hard.WSYNC} WSYNC ... rowsWSYNC:42

D223: 85 0D           STA     $0D                 ; {hard.PF0} PF0 value        ($DIGIT 0)PF0:43,45,47,49
D225: A5 FD           LDA     $FD                 ; {ram.mFD} Set ...
D227: 85 0E           STA     $0E                 ; {hard.PF1} ... PF1 value    (DIGIT 1,2)PF1:43,45,47,49
D229: A5 FE           LDA     $FE                 ; {ram.mFE} Set ...
D22B: 85 0F           STA     $0F                 ; {hard.PF2} PF2 value        ($DIGIT 3,4)PF2:43,45,47,49

D22D: BD C8 DD        LDA     $DDC8,X             ; {} Set ...
D230: 85 1B           STA     $1B                 ; {hard.GRP0} ... GRP0 value   (?? Never seems to do anything)GRP0:43,45,47,49
D232: BD D7 DD        LDA     $DDD7,X             ; {} Set ...
D235: 85 1C           STA     $1C                 ; {hard.GRP1} ... GRP1 value   (?? Never seems to do anything)GRP1:43,45,47,49
D237: CA              DEX                         ; 

D238: A9 00           LDA     #$00                ; 0 to ...
D23A: 85 0D           STA     $0D                 ; {hard.PF0} ... PF0 PlayfieldPF0:43,45,47,49
D23C: A4 F7           LDY     $F7                 ; {ram.mF7} Value of DIGIT 1
D23E: 85 0E           STA     $0E                 ; {hard.PF1} 0 to PF1PF1:43,45,47,49
D240: B1 F4           LDA     ($F4),Y             ; {ram.mF4} Image for DIGIT 1
D242: A4 FF           LDY     $FF                 ; {ram.mFF} Right number ...
D244: 84 0F           STY     $0F                 ; {hard.PF2} ... PF2 value   (DIGIT 5,6)PF2:43,45,47,49

D246: A4 FC           LDY     $FC                 ; {ram.mFC} Repeat DIGIT 0 ...
D248: 84 0D           STY     $0D                 ; {hard.PF0} .. on next line PF0PF0:43,45,47,49
D24A: A4 FD           LDY     $FD                 ; {ram.mFD} Repeat DIGIT 1,2 ...
D24C: EA              NOP                         ; Pause
D24D: 84 0E           STY     $0E                 ; {hard.PF1} ... on next line PF1PF1:43,45,47,49
D24F: A4 F8           LDY     $F8                 ; {ram.mF8} Value for DIGIT 2
D251: 11 F4           ORA     ($F4),Y             ; {ram.mF4} Image for DIGIT 2 (combine with DIGIT 1)
D253: 85 FD           STA     $FD                 ; {ram.mFD} Hold image pattern

D255: A5 FE           LDA     $FE                 ; {ram.mFE} Repeat DIGIT 3,4 ...
D257: 85 0F           STA     $0F                 ; {hard.PF2} ... to PF2PF2:44,46,48,50

D259: A4 F9           LDY     $F9                 ; {ram.mF9} Get image pattern ...
D25B: B1 F4           LDA     ($F4),Y             ; {ram.mF4} ... for ...
D25D: A4 FA           LDY     $FA                 ; {ram.mFA} ... DIGIT 3 ...
D25F: 11 F4           ORA     ($F4),Y             ; {ram.mF4} ... and DIGIT 4
D261: 85 FE           STA     $FE                 ; {ram.mFE} Hold image pattern

D263: A4 FB           LDY     $FB                 ; {ram.mFB} Get image pattern ...
D265: B1 F4           LDA     ($F4),Y             ; {ram.mF4} ... for DIGIT 5 (always blank) and DIGIT 6
```

# Code Bug 1

```code
CodeBug1:
; The right digits (5 and 6) probably started out as doubles. This may be left
; over from a duplication of the other two-digit combination code. The second
; LDY makes the first pointless (except for timing) since there is no jump
; to D269 anywhere.
D267: A4 FB           LDY     $FB                 ; {ram.mFB} Value for DIGIT 6
D269: A0 00           LDY     #$00                ; Clear playfield 0,1
;
D26B: 84 0D           STY     $0D                 ; {hard.PF0} PF0PF0:44,46,48,50
D26D: 84 0E           STY     $0E                 ; {hard.PF1} PF1PF1:44,46,48,50
D26F: A4 FF           LDY     $FF                 ; {ram.mFF} Store DIGIT 6 ...
D271: 84 0F           STY     $0F                 ; {hard.PF2} ... tio PF2PF2:44,46,48,50
D273: 85 FF           STA     $FF                 ; {ram.mFF} Store image pattern for DIGIT 6
D275: A4 F6           LDY     $F6                 ; {ram.mF6} Get image pattern ...
D277: B1 F4           LDA     ($F4),Y             ; {ram.mF4} ... for DIGIT 1
D279: 85 FC           STA     $FC                 ; {ram.mFC} Store it
D27B: EA              NOP                         ; Kill a cycle
D27C: C6 F4           DEC     $F4                 ; {ram.mF4} All rows done?
D27E: 10 A3           BPL     $D223               ; {} No ... back to top of loop

D280: 85 0D           STA     $0D                 ; {hard.PF0} Store DIGIT 0 to PF0PF0:50
D282: A5 FD           LDA     $FD                 ; {ram.mFD} Store DIGIT 1,2 to ...
D284: 85 0E           STA     $0E                 ; {hard.PF1} ... PF1PF1:51
D286: A5 FE           LDA     $FE                 ; {ram.mFE} Digit pattern for DIGIT 3, 4
D288: 85 0F           STA     $0F                 ; {hard.PF2} To screen in PF2PF2:51
;
D28A: BD C8 DD        LDA     $DDC8,X             ; {} ?? Never seems to do anything
D28D: 85 1B           STA     $1B                 ; {hard.GRP0} ??GRP0:51
D28F: BD D7 DD        LDA     $DDD7,X             ; {} ?? Never seems to do anything
D292: 85 1C           STA     $1C                 ; {hard.GRP1} ??GRP1:51
;
D294: A5 B9           LDA     $B9                 ; {ram.mB9} Frame count
D296: 6A              ROR     A                   ; Test for odd or even
D297: A9 00           LDA     #$00                ; Clear ...
D299: 85 0D           STA     $0D                 ; {hard.PF0} ... PF0 ...PF0:51
D29B: 85 0E           STA     $0E                 ; {hard.PF1} ... and PF1 ...PF1:51
D29D: B0 02           BCS     $D2A1               ; {code.DrawOddFieldPlayer} Odd frames ... go handle player
D29F: 90 52           BCC     $D2F3               ; {code.DrawEvenFieldAsteroids} Otherwise even frames ... go handle asteroids
```

# Draw Odd Field Player

```code
DrawOddFieldPlayer:
D2A1: A5 FF           LDA     $FF                 ; {ram.mFF}
D2A3: 85 0F           STA     $0F                 ; {hard.PF2} PF2:51
D2A5: A2 09           LDX     #$09                
D2A7: B5 A7           LDA     $A7,X               ; {ram.mA7}
D2A9: 29 07           AND     #$07                
D2AB: 85 F9           STA     $F9                 ; {ram.mF9}
D2AD: AA              TAX                         
D2AE: BD 75 DE        LDA     $DE75,X             ; {}
D2B1: 85 F6           STA     $F6                 ; {ram.mF6}
D2B3: A5 FC           LDA     $FC                 ; {ram.mFC}
D2B5: 85 0D           STA     $0D                 ; {hard.PF0} PF0:51
D2B7: A5 FD           LDA     $FD                 ; {ram.mFD}
D2B9: 85 0E           STA     $0E                 ; {hard.PF1} PF1:52
D2BB: A5 FE           LDA     $FE                 ; {ram.mFE}
D2BD: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
D2BF: A2 00           LDX     #$00                
D2C1: B5 A7           LDA     $A7,X               ; {ram.mA7}
D2C3: 29 07           AND     #$07                
D2C5: 85 F8           STA     $F8                 ; {ram.mF8}
D2C7: AA              TAX                         
D2C8: BD 75 DE        LDA     $DE75,X             ; {}
D2CB: AA              TAX                         
D2CC: A9 00           LDA     #$00                
D2CE: A0 FF           LDY     #$FF                
D2D0: 85 0D           STA     $0D                 ; {hard.PF0} PF0:52
D2D2: 85 0E           STA     $0E                 ; {hard.PF1} PF1:52
D2D4: EA              NOP                         
D2D5: A5 FF           LDA     $FF                 ; {ram.mFF}
D2D7: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
;
; At the end of the last digit row
D2D9: A9 00           LDA     #$00                ; OFF value
D2DB: EA              NOP                         ; Wait ...
D2DC: EA              NOP                         ; ... for ...
D2DD: EA              NOP                         ; ... end ...
D2DE: EA              NOP                         ; ... of ...
D2DF: EA              NOP                         ; ... row
D2E0: 86 06           STX     $06                 ; {hard.COLUP0} PF2 offCOLUP0:52
D2E2: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0 offGRP0:52
D2E4: 85 1C           STA     $1C                 ; {hard.GRP1} GRP1 offGRP1:52
D2E6: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
D2E8: A6 F6           LDX     $F6                 ; {ram.mF6}
D2EA: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:53
D2EC: 86 07           STX     $07                 ; {hard.COLUP1} COLUP1:53
D2EE: 85 05           STA     $05                 ; {hard.NUSIZ1} NUSIZ1:53
D2F0: 6C E3 00        JMP     ($00E3)             ; {ram.mE3}
```

# Draw Even Field Asteroids

```code
DrawEvenFieldAsteroids:
D2F3: A5 FF           LDA     $FF                 ; {ram.mFF}
D2F5: 85 0F           STA     $0F                 ; {hard.PF2} PF2:51
D2F7: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:51 CXM1FB:51 INPT5:51
D2F9: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:51 CXM1FB:51 INPT5:51
D2FB: A5 FC           LDA     $FC                 ; {ram.mFC}
D2FD: 85 0D           STA     $0D                 ; {hard.PF0} PF0:51
D2FF: A5 FD           LDA     $FD                 ; {ram.mFD}
D301: 85 0E           STA     $0E                 ; {hard.PF1} PF1:51
D303: A5 FE           LDA     $FE                 ; {ram.mFE}
D305: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
D307: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:52 CXM1FB:52 INPT5:52
D309: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:52 CXM1FB:52 INPT5:52
D30B: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:52 CXM1FB:52 INPT5:52
D30D: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:52 CXM1FB:52 INPT5:52
D30F: A1 83           LDA     ($83,X)             ; {ram.m83} CXBLPF:52 CXM1FB:52 INPT5:52
D311: A2 1F           LDX     #$1F                ; Set stack to ENABL ...
D313: 9A              TXS                         ; ... makes for fast register writes with PUSH
D314: A9 00           LDA     #$00                
D316: 85 0D           STA     $0D                 ; {hard.PF0} PF0:52
D318: 85 0E           STA     $0E                 ; {hard.PF1} PF1:52
D31A: A5 FF           LDA     $FF                 ; {ram.mFF}
D31C: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
D31E: A9 00           LDA     #$00                
D320: A8              TAY                         
D321: A6 E8           LDX     $E8                 ; {ram.mE8}
D323: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0:52
D325: 85 1C           STA     $1C                 ; {hard.GRP1} GRP1:52
D327: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0:52
D329: 85 0F           STA     $0F                 ; {hard.PF2} PF2:52
D32B: 86 08           STX     $08                 ; {hard.COLUPF} COLUPF:52
D32D: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:53
D32F: A5 C9           LDA     $C9                 ; {ram.mC9}
D331: 6A              ROR     A                   
D332: 29 07           AND     #$07                
D334: AA              TAX                         
D335: B0 36           BCS     $D36D               ; {}
D337: A5 E9           LDA     $E9                 ; {ram.mE9}
D339: 85 06           STA     $06                 ; {hard.COLUP0}
D33B: A5 EB           LDA     $EB                 ; {ram.mEB}
D33D: 85 25           STA     $25                 ; {hard.VDELP0}
D33F: 85 0B           STA     $0B                 ; {hard.REFP0}
D341: A5 C9           LDA     $C9                 ; {ram.mC9}
D343: 85 20           STA     $20                 ; {hard.HMP0}
D345: A9 00           LDA     #$00                
D347: 85 04           STA     $04                 ; {hard.NUSIZ0}
D349: A1 83           LDA     ($83,X)             ; {ram.m83}
D34B: CA              DEX                         
D34C: D0 04           BNE     $D352               ; {}
D34E: 85 10           STA     $10                 ; {hard.RESP0}
D350: F0 31           BEQ     $D383               ; {}
D352: CA              DEX                         
D353: D0 04           BNE     $D359               ; {}
D355: 85 10           STA     $10                 ; {hard.RESP0}
D357: F0 2A           BEQ     $D383               ; {}
D359: CA              DEX                         
D35A: D0 04           BNE     $D360               ; {}
D35C: 85 10           STA     $10                 ; {hard.RESP0}
D35E: F0 23           BEQ     $D383               ; {}
D360: CA              DEX                         
D361: D0 04           BNE     $D367               ; {}
D363: 85 10           STA     $10                 ; {hard.RESP0}
D365: F0 1C           BEQ     $D383               ; {}
D367: CA              DEX                         
D368: EA              NOP                         
D369: 85 10           STA     $10                 ; {hard.RESP0}
D36B: F0 18           BEQ     $D385               ; {}
D36D: EA              NOP                         
D36E: CA              DEX                         
D36F: D0 FD           BNE     $D36E               ; {}
D371: 85 10           STA     $10                 ; {hard.RESP0} RESP0:53
D373: A5 C9           LDA     $C9                 ; {ram.mC9}
D375: 85 20           STA     $20                 ; {hard.HMP0} HMP0:53
D377: A5 E9           LDA     $E9                 ; {ram.mE9}
D379: 85 06           STA     $06                 ; {hard.COLUP0} COLUP0:53
D37B: A5 EB           LDA     $EB                 ; {ram.mEB}
D37D: 85 25           STA     $25                 ; {hard.VDELP0} VDELP0:53
D37F: 85 0B           STA     $0B                 ; {hard.REFP0} REFP0:53
D381: 86 04           STX     $04                 ; {hard.NUSIZ0} NUSIZ0NUSIZ0:53
D383: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:53
D385: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVEHMOVE:54
D387: A5 D1           LDA     $D1                 ; {ram.mD1}
D389: 6A              ROR     A                   
D38A: 29 07           AND     #$07                
D38C: AA              TAX                         
D38D: B0 36           BCS     $D3C5               ; {}
D38F: A5 EA           LDA     $EA                 ; {ram.mEA}
D391: 85 07           STA     $07                 ; {hard.COLUP1} COLUP1:54
D393: A5 EC           LDA     $EC                 ; {ram.mEC}
D395: 85 26           STA     $26                 ; {hard.VDELP1} VDELP1:54
D397: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:54
D399: A5 D1           LDA     $D1                 ; {ram.mD1}
D39B: 85 21           STA     $21                 ; {hard.HMP1} HMP1:54
D39D: A1 83           LDA     ($83,X)             ; {ram.m83} CXM0P:54
D39F: A9 00           LDA     #$00                
D3A1: 85 05           STA     $05                 ; {hard.NUSIZ1} NUSIZ1:54
D3A3: CA              DEX                         
D3A4: D0 04           BNE     $D3AA               ; {}
D3A6: 85 11           STA     $11                 ; {hard.RESP1}
D3A8: F0 31           BEQ     $D3DB               ; {}
D3AA: CA              DEX                         
D3AB: D0 04           BNE     $D3B1               ; {}
D3AD: 85 11           STA     $11                 ; {hard.RESP1}
D3AF: F0 2A           BEQ     $D3DB               ; {}
D3B1: CA              DEX                         
D3B2: D0 04           BNE     $D3B8               ; {}
D3B4: 85 11           STA     $11                 ; {hard.RESP1} RESP1:54
D3B6: F0 23           BEQ     $D3DB               ; {}
D3B8: CA              DEX                         
D3B9: D0 04           BNE     $D3BF               ; {}
D3BB: 85 11           STA     $11                 ; {hard.RESP1}
D3BD: F0 1C           BEQ     $D3DB               ; {}
D3BF: CA              DEX                         
D3C0: EA              NOP                         
D3C1: 85 11           STA     $11                 ; {hard.RESP1}
D3C3: F0 18           BEQ     $D3DD               ; {}
D3C5: EA              NOP                         
D3C6: CA              DEX                         
D3C7: D0 FD           BNE     $D3C6               ; {}
D3C9: 85 11           STA     $11                 ; {hard.RESP1}
D3CB: 85 2B           STA     $2B                 ; {hard.HMCLR}
D3CD: A5 D1           LDA     $D1                 ; {ram.mD1}
D3CF: 85 21           STA     $21                 ; {hard.HMP1}
D3D1: A5 EA           LDA     $EA                 ; {ram.mEA}
D3D3: 85 07           STA     $07                 ; {hard.COLUP1}
D3D5: A5 EC           LDA     $EC                 ; {ram.mEC}
D3D7: 85 26           STA     $26                 ; {hard.VDELP1}
D3D9: 86 05           STX     $05                 ; {hard.NUSIZ1}
D3DB: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D3DD: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:lots
D3DF: 86 1C           STX     $1C                 ; {hard.GRP1} GRP1:lots
D3E1: C4 D8           CPY     $D8                 ; {ram.mD8}
D3E3: 08              PHP                         ; ENABL:lots
D3E4: C4 D7           CPY     $D7                 ; {ram.mD7}
D3E6: 08              PHP                         ; ENAM1:lots
D3E7: C4 D6           CPY     $D6                 ; {ram.mD6}
D3E9: 08              PHP                         ; ENAM0:lots
;
D3EA: A2 00           LDX     #$00                
D3EC: A1 ED           LDA     ($ED,X)             ; {ram.mED}
D3EE: C9 FF           CMP     #$FF                
D3F0: F0 04           BEQ     $D3F6               ; {}
D3F2: E6 ED           INC     $ED                 ; {ram.mED}
D3F4: D0 0C           BNE     $D402               ; {}
D3F6: C4 EF           CPY     $EF                 ; {ram.mEF}
D3F8: D0 07           BNE     $D401               ; {}
D3FA: A5 F1           LDA     $F1                 ; {ram.mF1}
D3FC: 85 ED           STA     $ED                 ; {ram.mED}
D3FE: 4C EC D3        JMP     $D3EC               ; {}

D401: 8A              TXA                         
D402: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
D404: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D406: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:lots
D408: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0:lots
D40A: A2 00           LDX     #$00                
D40C: A1 E6           LDA     ($E6,X)             ; {ram.mE6}
D40E: C9 FF           CMP     #$FF                
D410: F0 04           BEQ     $D416               ; {}
D412: E6 E6           INC     $E6                 ; {ram.mE6}
D414: D0 0C           BNE     $D422               ; {}
D416: C4 D2           CPY     $D2                 ; {ram.mD2}
D418: D0 07           BNE     $D421               ; {}
D41A: A5 F2           LDA     $F2                 ; {ram.mF2}
D41C: 85 E6           STA     $E6                 ; {ram.mE6}
D41E: 4C 0C D4        JMP     $D40C               ; {}
D421: 8A              TXA                         
D422: A2 1F           LDX     #$1F                
D424: 9A              TXS                         
D425: AA              TAX                         
D426: C8              INY                         
D427: C0 59           CPY     #$59                
D429: D0 B0           BNE     $D3DB               ; {}

D42B: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:232
D42D: A9 00           LDA     #$00                
D42F: 85 1B           STA     $1B                 ; {hard.GRP0} GRP0:233
D431: 85 1C           STA     $1C                 ; {hard.GRP1} GRP1:233
D433: 85 1F           STA     $1F                 ; {hard.ENABL} ENABL:233
D435: 85 1D           STA     $1D                 ; {hard.ENAM0} ENAM0:233
D437: 85 1E           STA     $1E                 ; {hard.ENAM1} ENAM1:233
D439: 4C 86 D5        JMP     $D586               ; {}

D43C: 24 C7           BIT     $C7                 ; {ram.mC7}
D43E: 50 48           BVC     $D488               ; {}
D440: A5 80           LDA     $80                 ; {ram.m80}
D442: 29 BF           AND     #$BF                
D444: 10 0C           BPL     $D452               ; {}
D446: C9 80           CMP     #$80                
D448: D0 04           BNE     $D44E               ; {}
D44A: A9 21           LDA     #$21                
D44C: D0 0C           BNE     $D45A               ; {}
D44E: A9 42           LDA     #$42                
D450: D0 08           BNE     $D45A               ; {}
D452: AA              TAX                         
D453: E8              INX                         
D454: 29 20           AND     #$20                
D456: F0 01           BEQ     $D459               ; {}
D458: E8              INX                         
D459: 8A              TXA                         
D45A: A2 00           LDX     #$00                
D45C: C9 0A           CMP     #$0A                
D45E: 90 06           BCC     $D466               ; {}
D460: E8              INX                         
D461: 38              SEC                         
D462: E9 0A           SBC     #$0A                
D464: B0 F6           BCS     $D45C               ; {}
D466: 85 F4           STA     $F4                 ; {ram.mF4}
D468: 8A              TXA                         
D469: 0A              ASL     A                   
D46A: 0A              ASL     A                   
D46B: 0A              ASL     A                   
D46C: 0A              ASL     A                   
D46D: 05 F4           ORA     $F4                 ; {ram.mF4}
D46F: 85 BE           STA     $BE                 ; {ram.mBE}
D471: A9 00           LDA     #$00                
D473: 85 BD           STA     $BD                 ; {ram.mBD}
D475: A9 C8           LDA     #$C8                ; Blank image ...
D477: 85 FA           STA     $FA                 ; {ram.mFA} ... for Digit 2
D479: A2 37           LDX     #$37                
D47B: A5 80           LDA     $80                 ; {ram.m80}
D47D: 29 20           AND     #$20                
D47F: F0 02           BEQ     $D483               ; {}
D481: A2 3C           LDX     #$3C                
D483: 86 FB           STX     $FB                 ; {ram.mFB}
D485: 4C AB D4        JMP     $D4AB               ; {}

D488: A5 C8           LDA     $C8                 ; {ram.mC8}
D48A: 6A              ROR     A                   
D48B: 90 0A           BCC     $D497               ; {}
D48D: A9 37           LDA     #$37                
D48F: 24 C7           BIT     $C7                 ; {ram.mC7}
D491: 10 12           BPL     $D4A5               ; {}
D493: A9 3C           LDA     #$3C                
D495: D0 0E           BNE     $D4A5               ; {}
D497: A5 BC           LDA     $BC                 ; {ram.mBC}
D499: 29 F0           AND     #$F0                
D49B: 4A              LSR     A                   
D49C: 4A              LSR     A                   
D49D: 85 F6           STA     $F6                 ; {ram.mF6}
D49F: 4A              LSR     A                   
D4A0: 4A              LSR     A                   
D4A1: 65 F6           ADC     $F6                 ; {ram.mF6}
D4A3: 69 32           ADC     #$32                
D4A5: 85 FB           STA     $FB                 ; {ram.mFB}
D4A7: A9 00           LDA     #$00                ; Image "0" ...
D4A9: 85 FA           STA     $FA                 ; {ram.mFA} ... for Digit 2
D4AB: A9 00           LDA     #$00                
D4AD: 4A              LSR     A                   
D4AE: 4A              LSR     A                   
D4AF: 4A              LSR     A                   
D4B0: 4A              LSR     A                   
D4B1: C9 08           CMP     #$08                
D4B3: 90 02           BCC     $D4B7               ; {}
D4B5: A9 07           LDA     #$07                
D4B7: AA              TAX                         
D4B8: BD 7D DE        LDA     $DE7D,X             ; {}
D4BB: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D4BD: 85 F3           STA     $F3                 ; {ram.mF3}
D4BF: BD 85 DE        LDA     $DE85,X             ; {}
D4C2: 85 20           STA     $20                 ; {hard.HMP0} HMP0:lots
D4C4: 0A              ASL     A                   
D4C5: 0A              ASL     A                   
D4C6: 0A              ASL     A                   
D4C7: 0A              ASL     A                   
D4C8: 85 21           STA     $21                 ; {hard.HMP1} HMP1:lots
D4CA: BD 8D DE        LDA     $DE8D,X             ; {}
D4CD: 85 04           STA     $04                 ; {hard.NUSIZ0} NUSIZ0:lots
D4CF: 4A              LSR     A                   
D4D0: 4A              LSR     A                   
D4D1: 4A              LSR     A                   
D4D2: 4A              LSR     A                   
D4D3: 85 05           STA     $05                 ; {hard.NUSIZ1} NUSIZ1:lots
D4D5: BC 95 DE        LDY     $DE95,X             ; {}
D4D8: 88              DEY                         
D4D9: 10 FD           BPL     $D4D8               ; {}
D4DB: 85 10           STA     $10                 ; {hard.RESP0} RESP0:lots
D4DD: 85 11           STA     $11                 ; {hard.RESP1} RESP1:lots
D4DF: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
D4E1: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:lots
;
D4E3: A9 DD           LDA     #$DD                ; DDxx ...
D4E5: 85 F5           STA     $F5                 ; {ram.mF5} ... pointer to F4
D4E7: A9 04           LDA     #$04                ; Bottom of "0" ...
D4E9: 85 F4           STA     $F4                 ; {ram.mF4} ... to F4
;
D4EB: A5 BE           LDA     $BE                 ; {ram.mBE}
D4ED: 29 0F           AND     #$0F                ; BCD lower digit
D4EF: 85 F6           STA     $F6                 ; {ram.mF6} Hold value.
D4F1: 0A              ASL     A                   ; Multiply ...
D4F2: 0A              ASL     A                   ; ... value ...
D4F3: 65 F6           ADC     $F6                 ; {ram.mF6} ... by 5
D4F5: 69 32           ADC     #$32                ; Add 10*5
D4F7: 85 F9           STA     $F9                 ; {ram.mF9} Digit 2
D4F9: A5 BE           LDA     $BE                 ; {ram.mBE}
D4FB: 29 F0           AND     #$F0                ; BCD upper digit (example 32 would be 2)
D4FD: 4A              LSR     A                   ; (16)
D4FE: 4A              LSR     A                   ; (8)
D4FF: 85 F6           STA     $F6                 ; {ram.mF6} Hold for a sec
D501: 4A              LSR     A                   ; (4)
D502: 4A              LSR     A                   ; (2)
D503: 65 F6           ADC     $F6                 ; {ram.mF6} (10)
D505: 69 96           ADC     #$96                ; 15*10 (160) .. DDA0 which is where we should be
D507: 85 F8           STA     $F8                 ; {ram.mF8} Digit 1

D509: A5 BD           LDA     $BD                 ; {ram.mBD}
D50B: 29 0F           AND     #$0F                
D50D: 85 F6           STA     $F6                 ; {ram.mF6}
D50F: 0A              ASL     A                   
D510: 0A              ASL     A                   
D511: 65 F6           ADC     $F6                 ; {ram.mF6}
D513: 69 64           ADC     #$64                
D515: 85 F7           STA     $F7                 ; {ram.mF7}
;
D517: A5 BD           LDA     $BD                 ; {ram.mBD}
D519: 29 F0           AND     #$F0                
D51B: 4A              LSR     A                   
D51C: 4A              LSR     A                   
D51D: 85 F6           STA     $F6                 ; {ram.mF6}
D51F: 4A              LSR     A                   
D520: 4A              LSR     A                   
D521: 65 F6           ADC     $F6                 ; {ram.mF6}
D523: 85 F6           STA     $F6                 ; {ram.mF6}
D525: A2 00           LDX     #$00                
D527: A0 C8           LDY     #$C8                
D529: B5 F6           LDA     $F6,X               ; {ram.mF6}
D52B: F0 0C           BEQ     $D539               ; {}
D52D: C9 32           CMP     #$32                
D52F: F0 08           BEQ     $D539               ; {}
D531: C9 64           CMP     #$64                
D533: F0 04           BEQ     $D539               ; {}
D535: C9 96           CMP     #$96                
D537: D0 07           BNE     $D540               ; {}
D539: 94 F6           STY     $F6,X               ; {ram.mF6}
D53B: E8              INX                         
D53C: E0 04           CPX     #$04                
D53E: D0 E9           BNE     $D529               ; {}
D540: 85 2B           STA     $2B                 ; {hard.HMCLR} HMCLR:lots
;
D542: A4 F6           LDY     $F6                 ; {ram.mF6}
D544: B1 F4           LDA     ($F4),Y             ; {ram.mF4}
D546: 85 FC           STA     $FC                 ; {ram.mFC}
;
D548: A4 F7           LDY     $F7                 ; {ram.mF7}
D54A: B1 F4           LDA     ($F4),Y             ; {ram.mF4}
D54C: A4 F8           LDY     $F8                 ; {ram.mF8}
D54E: 11 F4           ORA     ($F4),Y             ; {ram.mF4}
D550: 85 FD           STA     $FD                 ; {ram.mFD}
;
D552: A4 F9           LDY     $F9                 ; {ram.mF9}
D554: B1 F4           LDA     ($F4),Y             ; {ram.mF4}
D556: A4 FA           LDY     $FA                 ; {ram.mFA}
D558: 11 F4           ORA     ($F4),Y             ; {ram.mF4}
D55A: 85 FE           STA     $FE                 ; {ram.mFE}
;
D55C: A4 FB           LDY     $FB                 ; {ram.mFB}
D55E: B1 F4           LDA     ($F4),Y             ; {ram.mF4}
D560: 85 FF           STA     $FF                 ; {ram.mFF}
;
D562: C6 F4           DEC     $F4                 ; {ram.mF4}
D564: A9 74           LDA     #$74                
D566: 85 06           STA     $06                 ; {hard.COLUP0} COLUP0:lots
D568: 85 07           STA     $07                 ; {hard.COLUP1} COLUP1:lots
D56A: A9 44           LDA     #$44                
D56C: 24 C7           BIT     $C7                 ; {ram.mC7}
D56E: 10 02           BPL     $D572               ; {}
D570: A9 D6           LDA     #$D6                
D572: 45 E0           EOR     $E0                 ; {ram.mE0}
D574: 85 08           STA     $08                 ; {hard.COLUPF} COLUPF:lots
D576: A9 00           LDA     #$00                
D578: 85 25           STA     $25                 ; {hard.VDELP0} VDELP0:lots
D57A: 85 26           STA     $26                 ; {hard.VDELP1} VDELP1:lots
D57C: 85 0B           STA     $0B                 ; {hard.REFP0} REFP0:lots
D57E: AD 84 02        LDA     $0284               ; {hard.INTIM} INTIM:lots
D581: D0 FB           BNE     $D57E               ; {}
D583: 4C 1B D2        JMP     $D21B               ; {code.VisibleFrame}
;
D586: A9 00           LDA     #$00                
D588: 85 F7           STA     $F7                 ; {ram.mF7}
D58A: A9 F0           LDA     #$F0                
D58C: 85 F8           STA     $F8                 ; {ram.mF8}
D58E: 4C F0 DF        JMP     $DFF0               ; {code.SwitchToBank1} Bank switch to F000
```

# Reset (Bank 0)

```code
Reset0:
; Reset comes here if in 1st bank. If so we switch banks
; and go to the reset in the 2nd bank.
D591: A9 DA           LDA     #$DA                ; Go to ...
D593: 85 F7           STA     $F7                 ; {ram.mF7} ... F9DA ...
D595: A9 F9           LDA     #$F9                ; ... in Bank 1
D597: 85 F8           STA     $F8                 ; {ram.mF8} F9DA is the RESET
D599: 4C F0 DF        JMP     $DFF0               ; {code.SwitchToBank1} ... vector in bank 1

D59C: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00     
D5AC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   
D5BC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D5CC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
D5DC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   
D5EC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D5FC: 00 00 00 00   

D600: B4 95           LDY     $95,X               ; {ram.m95}
D602: 86 F4           STX     $F4                 ; {ram.mF4}
D604: AA              TAX                         
D605: B0 09           BCS     $D610               ; {}
D607: B9 00 D7        LDA     $D700,Y             ; {}
D60A: A8              TAY                         
D60B: CA              DEX                         
D60C: D0 F9           BNE     $D607               ; {}
D60E: F0 07           BEQ     $D617               ; {}
D610: B9 00 D8        LDA     $D800,Y             ; {}
D613: A8              TAY                         
D614: CA              DEX                         
D615: D0 F9           BNE     $D610               ; {}
D617: A6 F4           LDX     $F4                 ; {ram.mF4}
D619: 95 95           STA     $95,X               ; {ram.m95}
D61B: A0 FA           LDY     #$FA                
D61D: 84 F8           STY     $F8                 ; {ram.mF8}
D61F: A0 C4           LDY     #$C4                
D621: 84 F7           STY     $F7                 ; {ram.mF7}
D623: 4C F0 DF        JMP     $DFF0               ; {code.SwitchToBank1} Bank switch to FAC4

D626: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D636: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D646: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D656: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D666: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D676: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D686: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D696: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6A6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6B6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6C6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6D6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6E6: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D6F6: 00 00 00 00 00 00 00 00 00 00
   

D700: F0 F1           BEQ     $D6F3               ; {}
D702: F2             
D703: F3              
D704: F4                 
D705: F5 F6           SBC     $F6,X               ; {ram.mF6}
D707: F7                 
D708: F8              SED                         
D709: F9 FA FB        SBC     $FBFA,Y             ; {}
D70C: FC                 
D70D: FD FE FF        SBC     $FFFE,X             ; {}
D710: 00              BRK                         
D711: 01 02           ORA     ($02,X)             ; {hard.CXP0FB}
D713: 03                 
D714: 04                 
D715: 05 06           ORA     $06                 ; {hard.CXBLPF}
D717: 07                 
D718: 08              PHP                         
D719: 09 0A           ORA     #$0A                
D71B: 0B                 
D71C: 0C                 
D71D: 0D 0E 0F      ;ORA   $0F0E               ;
D720: 10 11           BPL     $D733               ; {}
D722: 12                 
D723: 13                 
D724: 14                 
D725: 15 16           ORA     $16,X               
D727: 17                 
D728: 18              CLC                         
D729: 19 1A 1B        ORA     $1B1A,Y             
D72C: 1C                 
D72D: 1D 1E 1F        ORA     $1F1E,X             
D730: 20 21 22        JSR     $2221               ; 
D733: 23                 
D734: 24 25         ;BIT   $25                 ;
D736: 26 27         ;ROL   $27                 ;
D738: 28              PLP                         
D739: 29 2A           AND     #$2A                
D73B: 2B                 
D73C: 2C 2D 2E        BIT     $2E2D               ; 
D73F: 2F                 
D740: 30 31           BMI     $D773               ; {}
D742: 32                 
D743: 33                 
D744: 34                 
D745: 35 36           AND     $36,X               ; {hard.CXBLPF}
D747: 37                 
D748: 38              SEC                         
D749: 39 3A 3B        AND     $3B3A,Y             
D74C: 3C                 
D74D: 3D 3E 3F        AND     $3F3E,X             
D750: 40              RTI                         
D751: 41 42           EOR     ($42,X)             
D753: 43                 
D754: 44                 
D755: 45 46         ;EOR   $46                 ;
D757: 47                 
D758: 48              PHA                         
D759: 49 4A           EOR     #$4A                
D75B: 4B                 
D75C: 4C 4D 4E        JMP     $4E4D               ; 
D75F: 4F                 
D760: 50 51           BVC     $D7B3               ; {}
D762: 52                 
D763: 53                 
D764: 54                 
D765: 55 56           EOR     $56,X               
D767: 57                 
D768: 58              CLI                         
D769: 59 5A 5B        EOR     $5B5A,Y             
D76C: 5C 5D 5E   
D76F: 5F                 
D770: 00              BRK                         
D771: 00              BRK                         
D772: 00              BRK                         
D773: 00              BRK                         
D774: 00              BRK                         
D775: 00              BRK                         
D776: 00              BRK                         
D777: 00              BRK                         
D778: 00              BRK                         
D779: 00              BRK                         
D77A: 00              BRK                         
D77B: 00              BRK                         
D77C: 00              BRK                         
D77D: 00              BRK                         
D77E: 00              BRK                         
D77F: 00              BRK                         
D780: 62                 
D781: 63                 
D782: 64                 
D783: 65 66         ;ADC   $66                 ;
D785: 67                 
D786: 68              PLA                         
D787: 69 6A           ADC     #$6A                
D789: 6B                 
D78A: 63                 
D78B: 6D 6E 32      ;ADC   $326E               ;
D78E: 00              BRK                         
D78F: 00              BRK                         
D790: 80                 
D791: 81 82           STA     ($82,X)             ; {ram.m82}
D793: 83                 
D794: 84 85           STY     $85                 ; {ram.m85}
D796: 86 87           STX     $87                 ; {ram.m87}
D798: 88              DEY                         
D799: 89                 
D79A: 8A              TXA                         
D79B: 8B                 
D79C: 8C 8D 8E      ;STY   $8E8D               ;
D79F: 8F                 
D7A0: 90 91           BCC     $D733               ; {}
D7A2: 92                 
D7A3: 65 94           ADC     $94                 ; {ram.m94}
D7A5: 95 96           STA     $96,X               ; {ram.m96}
D7A7: 97                 
D7A8: 98              TYA                         
D7A9: 99 9A 9B        STA     $9B9A,Y             
D7AC: 9C                 
D7AD: 9D 9E 9F        STA     $9F9E,X             
D7B0: A0 A1           LDY     #$A1                
D7B2: A2 A3           LDX     #$A3                
D7B4: A4 A5           LDY     $A5                 ; {ram.mA5}
D7B6: A6 A7           LDX     $A7                 ; {ram.mA7}
D7B8: A8              TAY                         
D7B9: A9 AA           LDA     #$AA                
D7BB: AB                 
D7BC: AC AD AE      ;LDY   $AEAD               ;
D7BF: AF                 
D7C0: B0 B1           BCS     $D773               ; {}
D7C2: B2                 
D7C3: B3                 
D7C4: B4 B5           LDY     $B5,X               ; {ram.mB5}
D7C6: B6 B7           LDX     $B7,Y               ; {ram.mB7}
D7C8: B8              CLV                         
D7C9: B9 BA BB        LDA     $BBBA,Y             
D7CC: BC BD BE        LDY     $BEBD,X             
D7CF: BF                 
D7D0: C0 C1           CPY     #$C1                
D7D2: C2                 
D7D3: C3                 
D7D4: C4 C5           CPY     $C5                 ; {ram.mC5}
D7D6: C6 C7           DEC     $C7                 ; {ram.mC7}
D7D8: C8              INY                         
D7D9: C9 CA           CMP     #$CA                
D7DB: CB                 
D7DC: CC CD CE      ;CPY   $CECD               ;
D7DF: CF                 
D7E0: D0 D1           BNE     $D7B3               ; {}
D7E2: D2                 
D7E3: D3                 
D7E4: D4                 
D7E5: D5 D6           CMP     $D6,X               ; {ram.mD6}
D7E7: D7                 
D7E8: D8              CLD                         
D7E9: D9 DA DB        CMP     $DBDA,Y             ; {}
D7EC: DC                 
D7ED: DD DE DF        CMP     $DFDE,X             ; {}
D7F0: E0 E1           CPX     #$E1                
D7F2: E2                 
D7F3: E3                 
D7F4: E4 E5           CPX     $E5                 ; {ram.mE5}
D7F6: E6 E7           INC     $E7                 ; {ram.mE7}
D7F8: E8              INX                         
D7F9: E9 EA           SBC     #$EA                
D7FB: EB                 
D7FC: EC ED EE      ;CPX   $EEED               ;
D7FF: EF                 


D800: 10 11           BPL     $D813               ; {}
D802: 12                 
D803: 13                 
D804: 14                 
D805: 15 16           ORA     $16,X               
D807: 17                 
D808: 18              CLC                         
D809: 19 1A 1B        ORA     $1B1A,Y             
D80C: 1C                 
D80D: 1D 1E 1F        ORA     $1F1E,X             
D810: 20 21 22        JSR     $2221               ; 
D813: 23                 
D814: 24 25           BIT     $25                 ; 
D816: 26 27           ROL     $27                 ; 
D818: 28              PLP                         
D819: 29 2A           AND     #$2A                
D81B: 2B                 
D81C: 2C 2D 2E        BIT     $2E2D               ; 
D81F: 2F                 
D820: 30 31           BMI     $D853               ; {}
D822: 32                 
D823: 33                 
D824: 34                 
D825: 35 36           AND     $36,X               ; {hard.CXBLPF}
D827: 37                 
D828: 38              SEC                         
D829: 39 3A 3B        AND     $3B3A,Y             
D82C: 3C                 
D82D: 3D 3E 3F        AND     $3F3E,X             
D830: 40              RTI                         
D831: 41 8D           EOR     ($8D,X)             ; {ram.m8D}
D833: 43                 
D834: 44                 
D835: 45 46           EOR     $46                 ; 
D837: 47                 
D838: 48              PHA                         
D839: 49 4A           EOR     #$4A                
D83B: 4B                 
D83C: 4C 4D 4E        JMP     $4E4D               ; 
D83F: 4F                 
D840: 50 51           BVC     $D893               ; {}
D842: 52                 
D843: 53                 
D844: 54                 
D845: 55 56           EOR     $56,X               
D847: 57                 
D848: 58              CLI                         
D849: 59 5A 5B        EOR     $5B5A,Y             
D84C: 5C 5D 5E   ;GOTO(5E5D)
D84F: 5F                 
D850: 60              RTS                         
D851: 61 62           ADC     ($62,X)             
D853: 63                 
D854: 64                 
D855: 65 66           ADC     $66                 ; 
D857: 67                 
D858: 68              PLA                         
D859: 69 6A           ADC     #$6A                
D85B: 6B                 
D85C: 6C 6D 6E        JMP     ($6E6D)             ; 
D85F: 6F                 
D860: 00              BRK                         
D861: 00              BRK                         
D862: 00              BRK                         
D863: 8A              TXA                         
D864: 82                 
D865: 83                 
D866: 84 85           STY     $85                 ; {ram.m85}
D868: 86 87           STX     $87                 ; {ram.m87}
D86A: 88              DEY                         
D86B: 89                 
D86C: 8A              TXA                         
D86D: 8B                 
D86E: 8C 8D 00        STY     $008D               ; {ram.m8D}
D871: 00              BRK                         
D872: 00              BRK                         
D873: 00              BRK                         
D874: 00              BRK                         
D875: 00              BRK                         
D876: 00              BRK                         
D877: 00              BRK                         
D878: 00              BRK                         
D879: 00              BRK                         
D87A: 00              BRK                         
D87B: 00              BRK                         
D87C: 00              BRK                         
D87D: 00              BRK                         
D87E: 00              BRK                         
D87F: 00              BRK                         
D880: 90 91           BCC     $D813               ; {}
D882: 92                 
D883: 93                 
D884: 94 95           STY     $95,X               ; {ram.m95}
D886: 96 97           STX     $97,Y               ; {ram.m97}
D888: 98              TYA                         
D889: 99 9A 9B        STA     $9B9A,Y             
D88C: 9C                 
D88D: 9D 9E 9F        STA     $9F9E,X             
D890: A0 A1           LDY     #$A1                
D892: A2 A3           LDX     #$A3                
D894: A4 A5           LDY     $A5                 ; {ram.mA5}
D896: A6 A7           LDX     $A7                 ; {ram.mA7}
D898: A8              TAY                         
D899: A9 AA           LDA     #$AA                
D89B: AB                 
D89C: AC AD AE        LDY     $AEAD               ; 
D89F: AF                 
D8A0: B0 B1           BCS     $D853               ; {}
D8A2: B2                 
D8A3: B3                 
D8A4: B4 B5           LDY     $B5,X               ; {ram.mB5}
D8A6: B6 B7           LDX     $B7,Y               ; {ram.mB7}
D8A8: B8              CLV                         
D8A9: B9 BA BB        LDA     $BBBA,Y             
D8AC: BC BD BE        LDY     $BEBD,X             
D8AF: BF                 
D8B0: C0 C1           CPY     #$C1                
D8B2: C2                 
D8B3: C3                 
D8B4: C4 C5           CPY     $C5                 ; {ram.mC5}
D8B6: C6 C7           DEC     $C7                 ; {ram.mC7}
D8B8: C8              INY                         
D8B9: C9 CA           CMP     #$CA                
D8BB: CB                 
D8BC: CC CD CE        CPY     $CECD               ; 
D8BF: CF                 
D8C0: D0 D1           BNE     $D893               ; {}
D8C2: D2                 
D8C3: D3                 
D8C4: D4                 
D8C5: D5 D6           CMP     $D6,X               ; {ram.mD6}
D8C7: D7                 
D8C8: D8              CLD                         
D8C9: D9 DA DB        CMP     $DBDA,Y             ; {}
D8CC: DC                 
D8CD: DD DE DF        CMP     $DFDE,X             ; {}
D8D0: E0 E1           CPX     #$E1                
D8D2: E2                 
D8D3: E3                 
D8D4: E4 E5           CPX     $E5                 ; {ram.mE5}
D8D6: E6 E7           INC     $E7                 ; {ram.mE7}
D8D8: E8              INX                         
D8D9: E9 EA           SBC     #$EA                
D8DB: EB                 
D8DC: EC ED EE        CPX     $EEED               ; {}
D8DF: EF                 
D8E0: F0 F1           BEQ     $D8D3               ; {}
D8E2: F2                 
D8E3: F3                 
D8E4: F4                 
D8E5: F5 F6           SBC     $F6,X               ; {ram.mF6}
D8E7: F7                 
D8E8: F8              SED                         
D8E9: F9 FA FB        SBC     $FBFA,Y             ; {}
D8EC: FC                 
D8ED: FD FE FF        SBC     $FFFE,X             ; {}
D8F0: 00              BRK                         
D8F1: 01 02           ORA     ($02,X)             ; {hard.CXP0FB}
D8F3: 03                 
D8F4: 04                 
D8F5: 05 06           ORA     $06                 ; {hard.CXBLPF}
D8F7: 07                 
D8F8: 08              PHP                         
D8F9: 09 0A           ORA     #$0A                
D8FB: 0B                 
D8FC: 0C                 
D8FD: 0D 0E 0F        ORA     $0F0E               ; 


D900: A0 00           LDY     #$00                
D902: B1 EF           LDA     ($EF),Y             ; {ram.mEF}
D904: A0 F4           LDY     #$F4                
D906: 84 F8           STY     $F8                 ; {ram.mF8}
D908: A0 80           LDY     #$80                
D90A: 84 F7           STY     $F7                 ; {ram.mF7}
D90C: 4C F0 DF        JMP     $DFF0               ; {code.SwitchToBank1} Bank switch to F480

D90F: A0 00           LDY     #$00                
D911: B1 F1           LDA     ($F1),Y             ; {ram.mF1}
D913: A0 F4           LDY     #$F4                
D915: 84 F8           STY     $F8                 ; {ram.mF8}
D917: A0 0C           LDY     #$0C                
D919: 84 F7           STY     $F7                 ; {ram.mF7}
D91B: 4C F0 DF        JMP     $DFF0               ; {code.SwitchToBank1} Bank switch to F40C

; 994 bytes of nothing
;
D91E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D92E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D93E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D94E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D95E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D96E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D97E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D98E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D99E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9AE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9BE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9CE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9DE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9EE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
D9FE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA0E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA1E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA2E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA3E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA4E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA5E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA6E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA7E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA8E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DA9E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DAAE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DABE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DACE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DADE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DAEE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DAFE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB0E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB1E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB2E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB3E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB4E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB5E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB6E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB7E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB8E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DB9E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBAE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBBE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBCE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBDE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBEE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DBFE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC0E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC1E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC2E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC3E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC4E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC5E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC6E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC7E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC8E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DC9E: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCAE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCBE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCCE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCDE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCEE: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
DCFE: 00 00
```

# Digit Images

```code
DigitImages:
DD00: E0 ; ***.....
DD01: A0 ; *.*.....
DD02: A0 ; *.*.....
DD03: A0 ; *.*.....
DD04: E0 ; ***.....

DD05: E0 ; ***.....
DD06: 40 ; .*......
DD07: 40 ; .*......
DD08: 60 ; .**.....
DD09: 40 ; .*......

DD0A: E0 ; ***.....
DD0B: 20 ; ..*.....
DD0C: E0 ; ***.....
DD0D: 80 ; *.......
DD0E: E0 ; ***.....

DD0F: E0 ; ***.....
DD10: 80 ; *.......
DD11: C0 ; **......
DD12: 80 ; *.......
DD13: E0 ; ***.....

DD14: 80 ; *.......
DD15: 80 ; *.......
DD16: E0 ; ***.....
DD17: A0 ; *.*.....
DD18: A0 ; *.*.....

DD19: E0 ; ***.....
DD1A: 80 ; *.......
DD1B: E0 ; ***.....
DD1C: 20 ; ..*.....
DD1D: E0 ; ***.....

DD1E: E0 ; ***.....
DD1F: A0 ; *.*.....
DD20: E0 ; ***.....
DD21: 20 ; ..*.....
DD22: 20 ; ..*.....

DD23: 80 ; *.......
DD24: 80 ; *.......
DD25: 80 ; *.......
DD26: 80 ; *.......
DD27: E0 ; ***.....

DD28: E0 ; ***.....
DD29: A0 ; *.*.....
DD2A: E0 ; ***.....
DD2B: A0 ; *.*.....
DD2C: E0 ; ***.....

DD2D: 80 ; *.......
DD2E: 80 ; *.......
DD2F: E0 ; ***.....
DD30: A0 ; *.*.....
DD31: E0 ; ***.....

DD32: 0E ; ....***.
DD33: 0A ; ....*.*.
DD34: 0A ; ....*.*.
DD35: 0A ; ....*.*.
DD36: 0E ; ....***.

DD37: 0E ; ....***.
DD38: 04 ; .....*..
DD39: 04 ; .....*..
DD3A: 06 ; .....**.
DD3B: 04 ; .....*..

DD3C: 0E ; ....***.
DD3D: 02 ; ......*.
DD3E: 0E ; ....***.
DD3F: 08 ; ....*...
DD40: 0E ; ....***.

DD41: 0E ; ....***.
DD42: 08 ; ....*...
DD43: 0C ; ....**..
DD44: 08 ; ....*...
DD45: 0E ; ....***.

DD46: 08 ; ....*...
DD47: 08 ; ....*...
DD48: 0E ; ....***.
DD49: 0A ; ....*.*.
DD4A: 0A ; ....*.*.

DD4B: 0E ; ....***.
DD4C: 08 ; ....*...
DD4D: 0E ; ....***.
DD4E: 02 ; ......*.
DD4F: 0E ; ....***.

DD50: 0E ; ....***.
DD51: 0A ; ....*.*.
DD52: 0E ; ....***.
DD53: 02 ; ......*.
DD54: 02 ; ......*.

DD55: 08 ; ....*...
DD56: 08 ; ....*...
DD57: 08 ; ....*...
DD58: 08 ; ....*...
DD59: 0E ; ....***.

DD5A: 0E ; ....***.
DD5B: 0A ; ....*.*.
DD5C: 0E ; ....***.
DD5D: 0A ; ....*.*.
DD5E: 0E ; ....***.

DD5F: 08 ; ....*...
DD60: 08 ; ....*...
DD61: 0E ; ....***.
DD62: 0A ; ....*.*.
DD63: 0E ; ....***.

DD64: 70 ; .***....
DD65: 50 ; .*.*....
DD66: 50 ; .*.*....
DD67: 50 ; .*.*....
DD68: 70 ; .***....

DD69: 70 ; .***....
DD6A: 20 ; ..*.....
DD6B: 20 ; ..*.....
DD6C: 60 ; .**.....
DD6D: 20 ; ..*.....

DD6E: 70 ; .***....
DD6F: 40 ; .*......
DD70: 70 ; .***....
DD71: 10 ; ...*....
DD72: 70 ; .***....

DD73: 70 ; .***....
DD74: 10 ; ...*....
DD75: 30 ; ..**....
DD76: 10 ; ...*....
DD77: 70 ; .***....

DD78: 10 ; ...*....
DD79: 10 ; ...*....
DD7A: 70 ; .***....
DD7B: 50 ; .*.*....
DD7C: 50 ; .*.*....

DD7D: 70 ; .***....
DD7E: 10 ; ...*....
DD7F: 70 ; .***....
DD80: 40 ; .*......
DD81: 70 ; .***....

DD82: 70 ; .***....
DD83: 50 ; .*.*....
DD84: 70 ; .***....
DD85: 40 ; .*......
DD86: 40 ; .*......

DD87: 10 ; ...*....
DD88: 10 ; ...*....
DD89: 10 ; ...*....
DD8A: 10 ; ...*....
DD8B: 70 ; .***....

DD8C: 70 ; .***....
DD8D: 50 ; .*.*....
DD8E: 70 ; .***....
DD8F: 50 ; .*.*....
DD90: 70 ; .***....

DD91: 10 ; ...*....
DD92: 10 ; ...*....
DD93: 70 ; .***....
DD94: 50 ; .*.*....
DD95: 70 ; .***....

DD96: 07 ; .....***
DD97: 05 ; .....*.*
DD98: 05 ; .....*.*
DD99: 05 ; .....*.*
DD9A: 07 ; .....***

DD9B: 07 ; .....***
DD9C: 02 ; ......*.
DD9D: 02 ; ......*.
DD9E: 06 ; .....**.
DD9F: 02 ; ......*.

DDA0: 07 ; .....***
DDA1: 04 ; .....*..
DDA2: 07 ; .....***
DDA3: 01 ; .......*
DDA4: 07 ; .....***

DDA5: 07 ; .....***
DDA6: 01 ; .......*
DDA7: 03 ; ......**
DDA8: 01 ; .......*
DDA9: 07 ; .....***

DDAA: 01 ; .......*
DDAB: 01 ; .......*
DDAC: 07 ; .....***
DDAD: 05 ; .....*.*
DDAE: 05 ; .....*.*

DDAF: 07 ; .....***
DDB0: 01 ; .......*
DDB1: 07 ; .....***
DDB2: 04 ; .....*..
DDB3: 07 ; .....***

DDB4: 07 ; .....***
DDB5: 05 ; .....*.*
DDB6: 07 ; .....***
DDB7: 04 ; .....*..
DDB8: 04 ; .....*..

DDB9: 01 ; .......*
DDBA: 01 ; .......*
DDBB: 01 ; .......*
DDBC: 01 ; .......*
DDBD: 07 ; .....***

DDBE: 07 ; .....***
DDBF: 05 ; .....*.*
DDC0: 07 ; .....***
DDC1: 05 ; .....*.*
DDC2: 07 ; .....***

DDC3: 01 ; .......*
DDC4: 01 ; .......*
DDC5: 07 ; .....***
DDC6: 05 ; .....*.*
DDC7: 07 ; .....***

DDC8: 00 ; ........
DDC9: 00 ; ........
DDCA: 00 ; ........
DDCB: 00 ; ........
DDCC: 00 ; ........

DDCD: 7C ; .*****..
DDCE: 38 ; ..***...
DDCF: 38 ; ..***...
DDD0: 10 ; ...*....
DDD1: 10 ; ...*....

DDD2: 7C ; .*****..
DDD3: 38 ; ..***...
DDD4: 38 ; ..***...
DDD5: 10 ; ...*....
DDD6: 10 ; ...*....

DDD7: 00 ; ........
DDD8: 00 ; ........
DDD9: 00 ; ........
DDDA: 00 ; ........
DDDB: 00 ; ........

DDDC: 00 ; ........
DDDD: 00 ; ........
DDDE: 00 ; ........
DDDF: 00 ; ........
DDE0: 00 ; ........

DDE1: 7C ; .*****..
DDE2: 38 ; ..***...
DDE3: 38 ; ..***...
DDE4: 10 ; ...*....
DDE5: 10 ; ...*....

DDE6: 00 ; ........
DDE7: 00 ; ........
DDE8: 00 ; ........
DDE9: 00 ; ........
DDEA: 00 ; ........

DDEB: 00 ; ........
DDEC: 00 ; ........
DDED: 00 ; ........
DDEE: 00 ; ........
DDEF: 00 ; ........

DDF0: 00 ; ........
DDF1: 00 ; ........
DDF2: 00 ; ........
DDF3: 00 ; ........
DDF4: 00 ; ........

DDF5: 00 ; ........
DDF6: 00 ; ........
DDF7: 00 ; ........
DDF8: 00 ; ........
DDF9: 00 ; ........

DDFA: 00 ; ........
DDFB: 00 ; ........
DDFC: 00 ; ........
DDFD: 00 ; ........
DDFE: 00 ; ........

DDFF: 00 ; ........

DE00: 0D ; ....**.*
DE01: 0D ; ....**.*
DE02: 1D ; ...***.*
DE03: 05 ; .....*.*
DE04: 05 ; .....*.*
DE05: 05 ; .....*.*
DE06: 05 ; .....*.*
DE07: F5 ; ****.*.*
DE08: 1D ; ...***.*
DE09: F5 ; ****.*.*
DE0A: 1D ; ...***.*
DE0B: F5 ; ****.*.*
DE0C: 0D ; ....**.*
DE0D: 0D ; ....**.*
DE0E: 0D ; ....**.*
DE0F: 00 ; ........

DE10: 0D ; ....**.*
DE11: 0D ; ....**.*
DE12: 0D ; ....**.*
DE13: 0D ; ....**.*
DE14: 0D ; ....**.*
DE15: 0D ; ....**.*
DE16: 0D ; ....**.*
DE17: 0D ; ....**.*
DE18: 0D ; ....**.*
DE19: 1D ; ...***.*
DE1A: 05 ; .....*.*
DE1B: 05 ; .....*.*
DE1C: F5 ; ****.*.*
DE1D: 0D ; ....**.*
DE1E: 0D ; ....**.*
DE1F: 00 ; ........

DE20: 08 ; ....*...
DE21: 08 ; ....*...
DE22: 08 ; ....*...
DE23: 08 ; ....*...
DE24: 08 ; ....*...
DE25: 08 ; ....*...
DE26: 08 ; ....*...
DE27: 00 ; ........
DE28: 00 ; ........
DE29: 00 ; ........
DE2A: 00 ; ........
DE2B: 00 ; ........
DE2C: 00 ; ........
DE2D: 00 ; ........
DE2E: 00 ; ........
DE2F: 00 ; ........

DE30: 08 ; ....*...
DE31: 08 ; ....*...
DE32: 08 ; ....*...
DE33: 08 ; ....*...
DE34: 00 ; ........
DE35: 00 ; ........
DE36: 00 ; ........
DE37: 00 ; ........
DE38: 00 ; ........
DE39: 00 ; ........
DE3A: 00 ; ........
DE3B: 00 ; ........
DE3C: 00 ; ........
DE3D: 00 ; ........
DE3E: 00 ; ........
DE3F: 00 ; ........

DE40: 08 ; ....*...
DE41: 08 ; ....*...
DE42: 08 ; ....*...
DE43: 08 ; ....*...
DE44: 08 ; ....*...
DE45: 08 ; ....*...
DE46: 08 ; ....*...
DE47: 08 ; ....*...
DE48: 08 ; ....*...
DE49: 08 ; ....*...
DE4A: 08 ; ....*...
DE4B: 00 ; ........
DE4C: 00 ; ........
DE4D: 00 ; ........
DE4E: 00 ; ........
DE4F: 00 ; ........

DE50: 08 ; ....*...
DE51: 08 ; ....*...
DE52: 08 ; ....*...
DE53: 08 ; ....*...
DE54: 08 ; ....*...
DE55: 08 ; ....*...
DE56: 08 ; ....*...
DE57: 08 ; ....*...
DE58: 08 ; ....*...
DE59: 08 ; ....*...
DE5A: 08 ; ....*...
DE5B: 00 ; ........
DE5C: 00 ; ........
DE5D: 00 ; ........
DE5E: 00 ; ........
DE5F: 00 ; ........

DE60: 08 ; ....*...
DE61: 08 ; ....*...
DE62: 08 ; ....*...
DE63: 08 ; ....*...
DE64: 08 ; ....*...
DE65: 08 ; ....*...
DE66: 08 ; ....*...
DE67: 08 ; ....*...
DE68: 00 ; ........
DE69: 00 ; ........
DE6A: 00 ; ........
DE6B: 00 ; ........
DE6C: 00 ; ........
DE6D: 00 ; ........
DE6E: 00 ; ........
DE6F: 00 ; ........

DE70: 08 ; ....*...
DE71: 08 ; ....*...
DE72: 08 ; ....*...
DE73: 08 ; ....*...
DE74: 00 ; ........

DE75: 0C ; ....**..
DE76: 44 ; .*...*..
DE77: 9C ; *..***..
DE78: 18 ; ...**...
DE79: 26 ; ..*..**.
DE7A: 56 ; .*.*.**.
DE7B: 76 ; .***.**.
DE7C: E6 ; ***..**.
DE7D: 04 ; .....*..
DE7E: 04 ; .....*..
DE7F: 09 ; ....*..*
DE80: 0E ; ....***.
DE81: 0E ; ....***.
DE82: 0E ; ....***.
DE83: 0E ; ....***.
DE84: 0E ; ....***.
DE85: 55 ; .*.*.*.*
DE86: 55 ; .*.*.*.*
DE87: 25 ; ..*..*.*
DE88: BC ; *.****..
DE89: 34 ; ..**.*..
DE8A: CD ; **..**.*
DE8B: 45 ; .*...*.*
DE8C: 45 ; .*...*.*
DE8D: 00 ; ........
DE8E: 00 ; ........
DE8F: 00 ; ........
DE90: 00 ; ........
DE91: 01 ; .......*
DE92: 11 ; ...*...*
DE93: 13 ; ...*..**
DE94: 33 ; ..**..**
DE95: 00 ; ........
DE96: 00 ; ........
DE97: 02 ; ......*.
DE98: 01 ; .......*
DE99: 01 ; .......*
DE9A: 00 ; ........
DE9B: 00 ; ........
DE9C: 00 ; ........
DE9D: 00 ; ........
DE9E: 00 ; ........
DE9F: 00 ; ........
DEA0: 00 ; ........
DEA1: 00 ; ........
DEA2: 00 ; ........
DEA3: 00 ; ........
DEA4: 00 ; ........
DEA5: 00 ; ........
DEA6: 00 ; ........
DEA7: 00 ; ........
DEA8: 00 ; ........
DEA9: 00 ; ........
DEAA: 00 ; ........
DEAB: 00 ; ........
DEAC: 00 ; ........
DEAD: 00 ; ........
DEAE: 00 ; ........
DEAF: 00 ; ........
DEB0: 00 ; ........
DEB1: 00 ; ........
DEB2: 00 ; ........
DEB3: 00 ; ........
DEB4: 00 ; ........
DEB5: 00 ; ........
DEB6: 00 ; ........
DEB7: 00 ; ........
DEB8: 00 ; ........
DEB9: 00 ; ........
DEBA: 00 ; ........
DEBB: 00 ; ........
DEBC: 00 ; ........
DEBD: 00 ; ........
DEBE: 00 ; ........
DEBF: 00 ; ........
DEC0: 00 ; ........
DEC1: 00 ; ........
DEC2: 00 ; ........
DEC3: 00 ; ........
DEC4: 00 ; ........
DEC5: 00 ; ........
DEC6: 00 ; ........
DEC7: 00 ; ........
DEC8: 00 ; ........
DEC9: 00 ; ........
DECA: 00 ; ........
DECB: 00 ; ........
DECC: 00 ; ........
DECD: 00 ; ........
DECE: 00 ; ........
DECF: 00 ; ........
DED0: 00 ; ........
DED1: 00 ; ........
DED2: 00 ; ........
DED3: 00 ; ........
DED4: 00 ; ........
DED5: 00 ; ........
DED6: 00 ; ........
DED7: 00 ; ........
DED8: 00 ; ........
DED9: 00 ; ........
DEDA: 00 ; ........
DEDB: 00 ; ........
DEDC: 00 ; ........
DEDD: 00 ; ........
DEDE: 00 ; ........
DEDF: 00 ; ........
DEE0: 00 ; ........
DEE1: 00 ; ........
DEE2: 00 ; ........
DEE3: 00 ; ........
DEE4: 00 ; ........
DEE5: 00 ; ........
DEE6: 00 ; ........
DEE7: 00 ; ........
DEE8: 00 ; ........
DEE9: 00 ; ........
DEEA: 00 ; ........
DEEB: 00 ; ........
DEEC: 00 ; ........
DEED: 00 ; ........
DEEE: 00 ; ........
DEEF: 00 ; ........
DEF0: 00 ; ........
DEF1: 00 ; ........
DEF2: 00 ; ........
DEF3: 00 ; ........
DEF4: 00 ; ........
DEF5: 00 ; ........
DEF6: 00 ; ........
DEF7: 00 ; ........
DEF8: 00 ; ........
DEF9: 00 ; ........
DEFA: 00 ; ........
DEFB: 00 ; ........
DEFC: 00 ; ........
DEFD: 00 ; ........
DEFE: 00 ; ........
DEFF: 00 ; ........
```

# Asteroid Images

```code
AsteroidImages:
; 16 rows each

DF00: 00 ; ........
DF01: 10 ; ...*....
DF02: 1C ; ...***..
DF03: 1E ; ...****.
DF04: 3E ; ..*****.
DF05: 3F ; ..******
DF06: 7F ; .*******
DF07: FF ; ********
DF08: 7F ; .*******
DF09: FF ; ********
DF0A: 7F ; .*******
DF0B: 3E ; ..*****.
DF0C: 3E ; ..*****.
DF0D: 1C ; ...***..
DF0E: 0C ; ....**..
DF0F: 00 ; ........

DF10: 00 ; ........
DF11: 3C ; ..****..
DF12: 7E ; .******.
DF13: 7F ; .*******
DF14: 3F ; ..******
DF15: 7F ; .*******
DF16: FF ; ********
DF17: FE ; *******.
DF18: FE ; *******.
DF19: 7F ; .*******
DF1A: 7F ; .*******
DF1B: 3F ; ..******
DF1C: 3E ; ..*****.
DF1D: 3E ; ..*****.
DF1E: 1C ; ...***..
DF1F: 00 ; ........

DF20: 18 ; ...**...
DF21: 3C ; ..****..
DF22: 7E ; .******.
DF23: FF ; ********
DF24: FF ; ********
DF25: 7E ; .******.
DF26: 0C ; ....**..
DF27: 00 ; ........
DF28: 00 ; ........
DF29: 00 ; ........
DF2A: 00 ; ........
DF2B: 00 ; ........
DF2C: 00 ; ........
DF2D: 00 ; ........
DF2E: 00 ; ........
DF2F: 00 ; ........

DF30: 60 ; .**.....
DF31: F0 ; ****....
DF32: F0 ; ****....
DF33: 20 ; ..*.....
DF34: 00 ; ........
DF35: 00 ; ........
DF36: 00 ; ........
DF37: 00 ; ........
DF38: 00 ; ........
DF39: 00 ; ........
DF3A: 00 ; ........
DF3B: 00 ; ........
DF3C: 00 ; ........
DF3D: 00 ; ........
DF3E: 00 ; ........
DF3F: 00 ; ........
```

# Asteroid Explosions

```code
AsteroidExplosions:
; 16 rows each
DF40: A0 ; *.*.....
DF41: 04 ; .....*..
DF42: 40 ; .*......
DF43: 09 ; ....*..*
DF44: 20 ; ..*.....
DF45: 00 ; ........
DF46: 88 ; *...*...
DF47: 01 ; .......*
DF48: 10 ; ...*....
DF49: 40 ; .*......
DF4A: 11 ; ...*...*
DF4B: 00 ; ........
DF4C: 00 ; ........
DF4D: 00 ; ........
DF4E: 00 ; ........
DF4F: 00 ; ........

DF50: 48 ; .*..*...
DF51: 02 ; ......*.
DF52: 20 ; ..*.....
DF53: 88 ; *...*...
DF54: 01 ; .......*
DF55: 40 ; .*......
DF56: 14 ; ...*.*..
DF57: 40 ; .*......
DF58: 00 ; ........
DF59: 21 ; ..*....*
DF5A: 84 ; *....*..
DF5B: 00 ; ........
DF5C: 00 ; ........
DF5D: 00 ; ........
DF5E: 00 ; ........
DF5F: 00 ; ........

DF60: 50 ; .*.*....
DF61: 02 ; ......*.
DF62: 20 ; ..*.....
DF63: 81 ; *......*
DF64: 04 ; .....*..
DF65: 40 ; .*......
DF66: 10 ; ...*....
DF67: 41 ; .*.....*
DF68: 00 ; ........
DF69: 00 ; ........
DF6A: 00 ; ........
DF6B: 00 ; ........
DF6C: 00 ; ........
DF6D: 00 ; ........
DF6E: 00 ; ........
DF6F: 00 ; ........

DF70: 40 ; .*......
DF71: 10 ; ...*....
DF72: 80 ; *.......
DF73: 20 ; ..*.....
```

# Ship Images

```code
ShipImages:
; 5 rows each. Each image ends with an FF terminator.

DF74: 10 ; ...*....
DF75: 10 ; ...*....
DF76: 38 ; ..***...
DF77: 38 ; ..***...
DF78: 7C ; .*****..
;
DF79: FF ; ********

DF7A: 20 ; ..*.....
DF7B: 30 ; ..**....
DF7C: 38 ; ..***...
DF7D: 3C ; ..****..
DF7E: 30 ; ..**....
;
DF7F: FF ; ********

DF80: 40 ; .*......
DF81: 30 ; ..**....
DF82: 3C ; ..****..
DF83: 18 ; ...**...
DF84: 10 ; ...*....
;
DF85: FF ; ********

DF86: 00 ; ........
DF87: 40 ; .*......
DF88: 3E ; ..*****.
DF89: 1C ; ...***..
DF8A: 0C ; ....**..
;
DF8B: FF ; ********

DF8C: 04 ; .....*..
DF8D: 1C ; ...***..
DF8E: FC ; ******..
DF8F: 1C ; ...***..
DF90: 04 ; .....*..
;
DF91: FF ; ********

DF92: 0C ; ....**..
DF93: 1C ; ...***..
DF94: 3E ; ..*****.
DF95: 40 ; .*......
DF96: 00 ; ........
;
DF97: FF ; ********

DF98: 10 ; ...*....
DF99: 18 ; ...**...
DF9A: 3C ; ..****..
DF9B: 30 ; ..**....
DF9C: 40 ; .*......
;
DF9D: FF ; ********

DF9E: 30 ; ..**....
DF9F: 3C ; ..****..
DFA0: 38 ; ..***...
DFA1: 30 ; ..**....
DFA2: 20 ; ..*.....
;
DFA3: FF ; ********

DFA4: 7C ; .*****..
DFA5: 38 ; ..***...
DFA6: 38 ; ..***...
DFA7: 10 ; ...*....
DFA8: 10 ; ...*....
;
DFA9: FF ; ********
```

# Ship Explosions

```code
ShipExplosions:
DFAA: 10 ; ...*....
DFAB: 02 ; ......*.
DFAC: 08 ; ....*...
DFAD: 22 ; ..*...*.
DFAE: 08 ; ....*...
;
DFAF: FF ; ********

DFB0: 08 ; ....*...
DFB1: 10 ; ...*....
DFB2: 80 ; *.......
DFB3: 04 ; .....*..
DFB4: A2 ; *.*...*.
;
DFB5: FF ; ********

DFB6: 20 ; ..*.....
DFB7: 81 ; *......*
DFB8: 22 ; ..*...*.
DFB9: 10 ; ...*....
DFBA: 04 ; .....*..
;
DFBB: FF ; ********
```

# Shield Image

```code
ShieldImage:
DFBC: 38 ; ..***...
DFBD: 44 ; .*...*..
DFBE: 54 ; .*.*.*..
DFBF: 44 ; .*...*..
DFC0: 38 ; ..***...
;
DFC1: FF ; ********
```

# Satellite Image

```code
SatelliteImage: 
DFC2: 10 ; ...*....
DFC3: 7C ; .*****..
DFC4: 38 ; ..***...
;
DFC5: FF ; ********
```

# UFO Image

```code
UFOImage: 
DFC6: 10 ; ...*....
DFC7: 38 ; ..***...
DFC8: FE ; *******.
DFC9: 7C ; .*****..
DFCA: 38 ; ..***...
;
DFCB: FF ; ********

DFCC: 00              BRK                         
DFCD: 00              BRK                         
DFCE: 00              BRK                         
DFCF: 00              BRK                         
DFD0: 00              BRK                         
DFD1: 00              BRK                         
DFD2: 00              BRK                         
DFD3: 00              BRK                         
DFD4: 00              BRK                         
DFD5: 00              BRK                         
DFD6: 00              BRK                         
DFD7: 00              BRK                         
DFD8: 00              BRK                         
DFD9: 00              BRK                         
DFDA: 00              BRK                         
DFDB: 00              BRK                         
DFDC: 00              BRK                         
DFDD: 00              BRK                         
DFDE: 00              BRK                         
DFDF: 00              BRK                         
DFE0: 00              BRK                         
DFE1: 00              BRK                         
DFE2: 00              BRK                         
DFE3: 00              BRK                         
DFE4: 00              BRK                         
DFE5: 00              BRK                         
DFE6: 00              BRK                         
DFE7: 00              BRK                         
DFE8: 00              BRK                         
DFE9: 00              BRK                         
DFEA: 00              BRK                         
DFEB: 00              BRK                         
DFEC: 00              BRK                         
DFED: 00              BRK                         
DFEE: 00              BRK                         
DFEF: 00              BRK                         
```

# Switch to Bank 1

```code
SwitchToBank1: 
; The destination address after the bank switch is in F7.
DFF0: 8D F9 FF        STA     $FFF9               ; {} Switch to bank 0 (goto FFF3)
DFF3: 6C F7 00        JMP     ($00F7)             ; {ram.mF7} Here after FFF0. Goto target address.
; 
DFF6: 00 00 00 00 ; Padding
```

# Vectors (Bank 0)

```code
Vectors0: 
DFFA: 91 D5       ; NMI vector to D591
DFFC: 91 D5       ; Reset vector to D591
DFFE: 91 D5       ; IRQ/BRK vector to D591
```

# Bank 1

>>> originGap E000

```code
;----------------------------------------------------------------------------------------------
Bank1:
; Second 2K bank of ROM.

F000: A2 FF           LDX     #$FF                ; Reset ...
F002: 9A              TXS                         ; ... stack pointer
F003: A9 24           LDA     #$24                ; 36 * 64 ...
F005: 8D 96 02        STA     $0296               ; {hard.TIM64T} ... 2304 clocksTIM64T:233
F008: AD 82 02        LDA     $0282               ; {hard.SWCHB} Console switchesSWCHB:233
F00B: 6A              ROR     A                   ; Check ...
F00C: 6A              ROR     A                   ; ... GAME SELECT
F00D: B0 4A           BCS     $F059               ; {} No ... skip SELECT

GameSelect:
F00F: 24 80           BIT     $80                 ; {ram.m80}
F011: 70 22           BVS     $F035               ; {}
F013: A5 80           LDA     $80                 ; {ram.m80}
F015: 09 40           ORA     #$40                
F017: 85 80           STA     $80                 ; {ram.m80}
F019: A5 C7           LDA     $C7                 ; {ram.mC7}
F01B: 09 40           ORA     #$40                
F01D: 85 C7           STA     $C7                 ; {ram.mC7}
F01F: A5 C8           LDA     $C8                 ; {ram.mC8}
F021: 09 01           ORA     #$01                
F023: 85 C8           STA     $C8                 ; {ram.mC8}
F025: A9 E0           LDA     #$E0                
F027: 85 CA           STA     $CA                 ; {ram.mCA}
F029: 85 D2           STA     $D2                 ; {ram.mD2}
F02B: A9 00           LDA     #$00                
F02D: 85 B9           STA     $B9                 ; {ram.mB9}
F02F: 85 BA           STA     $BA                 ; {ram.mBA}
F031: 85 BC           STA     $BC                 ; {ram.mBC}
F033: 85 BF           STA     $BF                 ; {ram.mBF}

F035: AD 82 02        LDA     $0282               ; {hard.SWCHB} Console switces
F038: 6A              ROR     A                   ; Check GAME RESET
F039: A5 B9           LDA     $B9                 ; {ram.mB9}
F03B: 29 3F           AND     #$3F                
F03D: B0 02           BCS     $F041               ; {} Yes ... go handle RESET
F03F: 29 0F           AND     #$0F                
F041: D0 13           BNE     $F056               ; {}
F043: E6 80           INC     $80                 ; {ram.m80}
F045: A5 80           LDA     $80                 ; {ram.m80}
F047: A2 04           LDX     #$04                
F049: CA              DEX                         
F04A: 30 0A           BMI     $F056               ; {}
F04C: DD 56 FF        CMP     $FF56,X             ; {}
F04F: D0 F8           BNE     $F049               ; {}
F051: BD 5A FF        LDA     $FF5A,X             ; {}
F054: 85 80           STA     $80                 ; {ram.m80}
F056: 4C 7D F0        JMP     $F07D               ; {}


F059: A5 80           LDA     $80                 ; {ram.m80}
F05B: 29 BF           AND     #$BF                
F05D: 85 80           STA     $80                 ; {ram.m80}
F05F: AD 82 02        LDA     $0282               ; {hard.SWCHB} SWCHB:233
F062: 6A              ROR     A                   
F063: B0 18           BCS     $F07D               ; {}
F065: A9 00           LDA     #$00                
F067: 85 09           STA     $09                 ; {hard.COLUBK}
F069: A2 83           LDX     #$83                
F06B: 95 00           STA     $00,X               ; {hard.VSYNC}
F06D: E8              INX                         
F06E: D0 FB           BNE     $F06B               ; {}
F070: A9 40           LDA     #$40                
F072: 85 BC           STA     $BC                 ; {ram.mBC}
F074: 85 BF           STA     $BF                 ; {ram.mBF}
F076: A9 29           LDA     #$29                
F078: 85 CA           STA     $CA                 ; {ram.mCA}
F07A: 4C FA F9        JMP     $F9FA               ; {}

F07D: A2 00           LDX     #$00                
F07F: B5 83           LDA     $83,X               ; {ram.m83}
F081: C9 E0           CMP     #$E0                
F083: F0 03           BEQ     $F088               ; {}
F085: E8              INX                         
F086: 10 F7           BPL     $F07F               ; {}
F088: E0 00           CPX     #$00                
F08A: F0 01           BEQ     $F08D               ; {}
F08C: CA              DEX                         
F08D: 86 DC           STX     $DC                 ; {ram.mDC}
F08F: A2 09           LDX     #$09                
F091: B5 83           LDA     $83,X               ; {ram.m83}
F093: C9 E0           CMP     #$E0                
F095: F0 03           BEQ     $F09A               ; {}
F097: E8              INX                         
F098: 10 F7           BPL     $F091               ; {}
F09A: E0 09           CPX     #$09                
F09C: F0 01           BEQ     $F09F               ; {}
F09E: CA              DEX                         
F09F: 86 DD           STX     $DD                 ; {ram.mDD}
F0A1: A2 00           LDX     #$00                
F0A3: B5 83           LDA     $83,X               ; {ram.m83}
F0A5: C9 E0           CMP     #$E0                
F0A7: D0 0E           BNE     $F0B7               ; {}
F0A9: A2 09           LDX     #$09                
F0AB: B5 83           LDA     $83,X               ; {ram.m83}
F0AD: C9 E0           CMP     #$E0                
F0AF: D0 06           BNE     $F0B7               ; {}
F0B1: 20 EA FD        JSR     $FDEA               ; {}
F0B4: 4C 0F F2        JMP     $F20F               ; {}
F0B7: A5 C2           LDA     $C2                 ; {ram.mC2}
F0B9: D0 7B           BNE     $F136               ; {}
F0BB: 24 C8           BIT     $C8                 ; {ram.mC8}
F0BD: 70 0F           BVS     $F0CE               ; {}
F0BF: A5 C8           LDA     $C8                 ; {ram.mC8}
F0C1: 6A              ROR     A                   
F0C2: B0 6B           BCS     $F12F               ; {}
F0C4: A5 CA           LDA     $CA                 ; {ram.mCA}
F0C6: C9 E0           CMP     #$E0                
F0C8: D0 68           BNE     $F132               ; {}
F0CA: A5 DE           LDA     $DE                 ; {ram.mDE}
F0CC: F0 11           BEQ     $F0DF               ; {}
F0CE: A5 D2           LDA     $D2                 ; {ram.mD2}
F0D0: C9 E0           CMP     #$E0                
F0D2: D0 5E           BNE     $F132               ; {}
F0D4: A5 D9           LDA     $D9                 ; {ram.mD9}
F0D6: 05 DA           ORA     $DA                 ; {ram.mDA}
F0D8: 05 DB           ORA     $DB                 ; {ram.mDB}
F0DA: D0 56           BNE     $F132               ; {}
F0DC: 4C 0F F2        JMP     $F20F               ; {}
F0DF: A5 C8           LDA     $C8                 ; {ram.mC8}
F0E1: 29 02           AND     #$02                
F0E3: F0 18           BEQ     $F0FD               ; {}
F0E5: A5 D2           LDA     $D2                 ; {ram.mD2}
F0E7: C9 E0           CMP     #$E0                
F0E9: D0 47           BNE     $F132               ; {}
F0EB: A5 DB           LDA     $DB                 ; {ram.mDB}
F0ED: D0 43           BNE     $F132               ; {}
F0EF: A2 00           LDX     #$00                
F0F1: 20 A0 FE        JSR     $FEA0               ; {}
F0F4: D0 39           BNE     $F12F               ; {}
F0F6: A2 09           LDX     #$09                
F0F8: 20 A0 FE        JSR     $FEA0               ; {}
F0FB: D0 32           BNE     $F12F               ; {}
F0FD: A5 DF           LDA     $DF                 ; {ram.mDF}
F0FF: 85 CA           STA     $CA                 ; {ram.mCA}
F101: A9 00           LDA     #$00                
F103: A2 05           LDX     #$05                
F105: 95 CB           STA     $CB,X               ; {ram.mCB}
F107: CA              DEX                         
F108: 10 FB           BPL     $F105               ; {}
F10A: A5 80           LDA     $80                 ; {ram.m80}
F10C: 29 20           AND     #$20                
F10E: D0 04           BNE     $F114               ; {}
F110: 85 BF           STA     $BF                 ; {ram.mBF}
F112: F0 1B           BEQ     $F12F               ; {}
F114: A5 BF           LDA     $BF                 ; {ram.mBF}
F116: F0 17           BEQ     $F12F               ; {}
F118: A5 C8           LDA     $C8                 ; {ram.mC8}
F11A: 29 02           AND     #$02                
F11C: F0 11           BEQ     $F12F               ; {}
F11E: 20 C5 FA        JSR     $FAC5               ; {}
F121: A9 E0           LDA     #$E0                
F123: 85 83           STA     $83                 ; {ram.m83}
F125: 85 8C           STA     $8C                 ; {ram.m8C}
F127: A9 00           LDA     #$00                
F129: 85 DC           STA     $DC                 ; {ram.mDC}
F12B: A9 09           LDA     #$09                
F12D: 85 DD           STA     $DD                 ; {ram.mDD}
F12F: 4C 0F F2        JMP     $F20F               ; {}
F132: A5 C2           LDA     $C2                 ; {ram.mC2}
F134: F0 1C           BEQ     $F152               ; {}
F136: A6 DC           LDX     $DC                 ; {ram.mDC}
F138: 86 F5           STX     $F5                 ; {ram.mF5}
F13A: A2 00           LDX     #$00                
F13C: 20 DE FC        JSR     $FCDE               ; {}
F13F: 86 DC           STX     $DC                 ; {ram.mDC}
F141: A6 DD           LDX     $DD                 ; {ram.mDD}
F143: 86 F5           STX     $F5                 ; {ram.mF5}
F145: A2 09           LDX     #$09                
F147: 20 DE FC        JSR     $FCDE               ; {}
F14A: 86 DD           STX     $DD                 ; {ram.mDD}
F14C: A9 00           LDA     #$00                
F14E: 85 C2           STA     $C2                 ; {ram.mC2}
F150: F0 DD           BEQ     $F12F               ; {}
F152: A5 E1           LDA     $E1                 ; {ram.mE1}
F154: 24 E1           BIT     $E1                 ; {ram.mE1}
F156: 10 42           BPL     $F19A               ; {}
F158: 49 C0           EOR     #$C0                
F15A: 85 E1           STA     $E1                 ; {ram.mE1}
F15C: 50 1E           BVC     $F17C               ; {}
F15E: A5 D9           LDA     $D9                 ; {ram.mD9}
F160: F0 F0           BEQ     $F152               ; {}
F162: A5 D6           LDA     $D6                 ; {ram.mD6}
F164: A4 D3           LDY     $D3                 ; {ram.mD3}
F166: A2 07           LDX     #$07                
F168: 20 E7 FA        JSR     $FAE7               ; {}
F16B: A4 D2           LDY     $D2                 ; {ram.mD2}
F16D: C0 E0           CPY     #$E0                
F16F: F0 08           BEQ     $F179               ; {}
F171: 20 D3 FC        JSR     $FCD3               ; {}
F174: A4 D1           LDY     $D1                 ; {ram.mD1}
F176: 20 A0 FB        JSR     $FBA0               ; {}
F179: 4C 0F F2        JMP     $F20F               ; {}
F17C: A5 DA           LDA     $DA                 ; {ram.mDA}
F17E: F0 D2           BEQ     $F152               ; {}
F180: A5 D7           LDA     $D7                 ; {ram.mD7}
F182: A4 D4           LDY     $D4                 ; {ram.mD4}
F184: A2 08           LDX     #$08                
F186: 20 E7 FA        JSR     $FAE7               ; {}
F189: A4 D2           LDY     $D2                 ; {ram.mD2}
F18B: C0 E0           CPY     #$E0                
F18D: F0 08           BEQ     $F197               ; {}
F18F: 20 D3 FC        JSR     $FCD3               ; {}
F192: A4 D1           LDY     $D1                 ; {ram.mD1}
F194: 20 A0 FB        JSR     $FBA0               ; {}
F197: 4C 0F F2        JMP     $F20F               ; {}
F19A: 29 03           AND     #$03                
F19C: AA              TAX                         
F19D: E6 E1           INC     $E1                 ; {ram.mE1}
F19F: A5 E1           LDA     $E1                 ; {ram.mE1}
F1A1: 09 80           ORA     #$80                
F1A3: A8              TAY                         
F1A4: 29 03           AND     #$03                
F1A6: C9 03           CMP     #$03                
F1A8: D0 04           BNE     $F1AE               ; {}
F1AA: 98              TYA                         
F1AB: 29 FC           AND     #$FC                
F1AD: A8              TAY                         
F1AE: 84 E1           STY     $E1                 ; {ram.mE1}
F1B0: CA              DEX                         
F1B1: 30 39           BMI     $F1EC               ; {}
F1B3: CA              DEX                         
F1B4: 30 25           BMI     $F1DB               ; {}
F1B6: 24 C8           BIT     $C8                 ; {ram.mC8}
F1B8: 50 03           BVC     $F1BD               ; {}
F1BA: 4C 52 F1        JMP     $F152               ; {}
F1BD: A5 DE           LDA     $DE                 ; {ram.mDE}
F1BF: 30 17           BMI     $F1D8               ; {}
F1C1: A4 C9           LDY     $C9                 ; {ram.mC9}
F1C3: A2 04           LDX     #$04                
F1C5: A5 CA           LDA     $CA                 ; {ram.mCA}
F1C7: 20 E7 FA        JSR     $FAE7               ; {}
F1CA: A4 D2           LDY     $D2                 ; {ram.mD2}
F1CC: C0 E0           CPY     #$E0                
F1CE: F0 08           BEQ     $F1D8               ; {}
F1D0: 20 D3 FC        JSR     $FCD3               ; {}
F1D3: A4 D1           LDY     $D1                 ; {ram.mD1}
F1D5: 20 A0 FB        JSR     $FBA0               ; {}
F1D8: 4C 0F F2        JMP     $F20F               ; {}
F1DB: A4 D2           LDY     $D2                 ; {ram.mD2}
F1DD: C0 E0           CPY     #$E0                
F1DF: F0 D9           BEQ     $F1BA               ; {}
F1E1: 20 D3 FC        JSR     $FCD3               ; {}
F1E4: A4 D1           LDY     $D1                 ; {ram.mD1}
F1E6: 20 E7 FA        JSR     $FAE7               ; {}
F1E9: 4C 0F F2        JMP     $F20F               ; {}
F1EC: A5 DB           LDA     $DB                 ; {ram.mDB}
F1EE: F0 CA           BEQ     $F1BA               ; {}
F1F0: A5 D8           LDA     $D8                 ; {ram.mD8}
F1F2: A4 D5           LDY     $D5                 ; {ram.mD5}
F1F4: A2 09           LDX     #$09                
F1F6: 20 E7 FA        JSR     $FAE7               ; {}
F1F9: A4 CA           LDY     $CA                 ; {ram.mCA}
F1FB: C0 E0           CPY     #$E0                
F1FD: F0 10           BEQ     $F20F               ; {}
F1FF: 24 C8           BIT     $C8                 ; {ram.mC8}
F201: 70 0C           BVS     $F20F               ; {}
F203: A5 DE           LDA     $DE                 ; {ram.mDE}
F205: 30 08           BMI     $F20F               ; {}
F207: A2 04           LDX     #$04                
F209: 98              TYA                         
F20A: A4 C9           LDY     $C9                 ; {ram.mC9}
F20C: 20 A0 FB        JSR     $FBA0               ; {}
F20F: A5 C8           LDA     $C8                 ; {ram.mC8}
F211: 6A              ROR     A                   
F212: 90 09           BCC     $F21D               ; {}
F214: A9 00           LDA     #$00                
F216: 85 19           STA     $19                 ; {hard.AUDV0} AUDV0:237,235,236
F218: 85 1A           STA     $1A                 ; {hard.AUDV1} AUDV1:237,235,236
F21A: 4C 16 F3        JMP     $F316               ; {code.VerticalBlank}
F21D: A5 C5           LDA     $C5                 ; {ram.mC5}
F21F: 85 F4           STA     $F4                 ; {ram.mF4}
F221: A0 08           LDY     #$08                
F223: 66 F4           ROR     $F4                 ; {ram.mF4}
F225: 90 19           BCC     $F240               ; {}
F227: A5 B9           LDA     $B9                 ; {ram.mB9}
F229: 6A              ROR     A                   
F22A: B0 0C           BCS     $F238               ; {}
F22C: C6 C3           DEC     $C3                 ; {ram.mC3}
F22E: D0 08           BNE     $F238               ; {}
F230: A5 C5           LDA     $C5                 ; {ram.mC5}
F232: 29 FE           AND     #$FE                
F234: 85 C5           STA     $C5                 ; {ram.mC5}
F236: 90 08           BCC     $F240               ; {}
F238: 66 F4           ROR     $F4                 ; {ram.mF4}
F23A: A2 1F           LDX     #$1F                
F23C: A5 C3           LDA     $C3                 ; {ram.mC3}
F23E: 10 0C           BPL     $F24C               ; {}
F240: 66 F4           ROR     $F4                 ; {ram.mF4}
F242: 90 06           BCC     $F24A               ; {}
F244: A2 08           LDX     #$08                
F246: A9 06           LDA     #$06                
F248: 10 02           BPL     $F24C               ; {}
F24A: A9 00           LDA     #$00                
F24C: 84 15           STY     $15                 ; {hard.AUDC0} AUDC0:lots
F24E: 86 17           STX     $17                 ; {hard.AUDF0} AUDF0:lots
F250: 85 19           STA     $19                 ; {hard.AUDV0} AUDV0:lots
F252: 66 F4           ROR     $F4                 ; {ram.mF4}
F254: 90 1E           BCC     $F274               ; {}
F256: A2 04           LDX     #$04                
F258: A0 0F           LDY     #$0F                
F25A: A5 C4           LDA     $C4                 ; {ram.mC4}
F25C: 29 10           AND     #$10                
F25E: F0 02           BEQ     $F262               ; {}
F260: A0 00           LDY     #$00                
F262: 98              TYA                         
F263: A0 04           LDY     #$04                
F265: C6 C4           DEC     $C4                 ; {ram.mC4}
F267: D0 59           BNE     $F2C2               ; {}
F269: A5 C5           LDA     $C5                 ; {ram.mC5}
F26B: 29 EB           AND     #$EB                
F26D: 85 C5           STA     $C5                 ; {ram.mC5}
F26F: E6 C4           INC     $C4                 ; {ram.mC4}
F271: 4C A4 F2        JMP     $F2A4               ; {}
F274: 66 F4           ROR     $F4                 ; {ram.mF4}
F276: 90 18           BCC     $F290               ; {}
F278: A2 08           LDX     #$08                
F27A: A5 C7           LDA     $C7                 ; {ram.mC7}
F27C: 29 20           AND     #$20                
F27E: D0 02           BNE     $F282               ; {}
F280: A2 10           LDX     #$10                
F282: A5 B9           LDA     $B9                 ; {ram.mB9}
F284: 29 02           AND     #$02                
F286: F0 02           BEQ     $F28A               ; {}
F288: CA              DEX                         
F289: CA              DEX                         
F28A: A0 0C           LDY     #$0C                
F28C: A9 08           LDA     #$08                
F28E: 10 32           BPL     $F2C2               ; {}
F290: 66 F4           ROR     $F4                 ; {ram.mF4}
F292: 90 36           BCC     $F2CA               ; {}
F294: C6 C4           DEC     $C4                 ; {ram.mC4}
F296: D0 13           BNE     $F2AB               ; {}
F298: A5 C5           LDA     $C5                 ; {ram.mC5}
F29A: 29 EF           AND     #$EF                
F29C: 09 60           ORA     #$60                
F29E: 85 C5           STA     $C5                 ; {ram.mC5}
F2A0: A9 08           LDA     #$08                
F2A2: 85 C4           STA     $C4                 ; {ram.mC4}
F2A4: A9 00           LDA     #$00                
F2A6: 85 1A           STA     $1A                 ; {hard.AUDV1} AUDV1:244
F2A8: 4C 16 F3        JMP     $F316               ; {code.VerticalBlank}
F2AB: A0 0C           LDY     #$0C                
F2AD: A5 C4           LDA     $C4                 ; {ram.mC4}
F2AF: C9 08           CMP     #$08                
F2B1: 90 07           BCC     $F2BA               ; {}
F2B3: A5 B9           LDA     $B9                 ; {ram.mB9}
F2B5: 6A              ROR     A                   
F2B6: 90 02           BCC     $F2BA               ; {}
F2B8: A0 08           LDY     #$08                
F2BA: A9 0F           LDA     #$0F                
F2BC: 38              SEC                         
F2BD: E5 C4           SBC     $C4                 ; {ram.mC4}
F2BF: AA              TAX                         
F2C0: A9 0D           LDA     #$0D                
F2C2: 84 16           STY     $16                 ; {hard.AUDC1} AUDC1:lots
F2C4: 86 18           STX     $18                 ; {hard.AUDF1} AUDF1:lots
F2C6: 85 1A           STA     $1A                 ; {hard.AUDV1} AUDV1:lots
F2C8: 10 4C           BPL     $F316               ; {code.VerticalBlank}
F2CA: A0 06           LDY     #$06                
F2CC: C6 C4           DEC     $C4                 ; {ram.mC4}
F2CE: D0 25           BNE     $F2F5               ; {}
F2D0: A5 C5           LDA     $C5                 ; {ram.mC5}
F2D2: 29 9F           AND     #$9F                
F2D4: 66 F4           ROR     $F4                 ; {ram.mF4}
F2D6: B0 30           BCS     $F308               ; {}
F2D8: 09 20           ORA     #$20                
F2DA: 66 F4           ROR     $F4                 ; {ram.mF4}
F2DC: 90 02           BCC     $F2E0               ; {}
F2DE: 09 40           ORA     #$40                
F2E0: 85 C5           STA     $C5                 ; {ram.mC5}
F2E2: A5 BA           LDA     $BA                 ; {ram.mBA}
F2E4: 30 0B           BMI     $F2F1               ; {}
F2E6: A9 0E           LDA     #$0E                
F2E8: 38              SEC                         
F2E9: E5 BA           SBC     $BA                 ; {ram.mBA}
F2EB: 30 04           BMI     $F2F1               ; {}
F2ED: C9 06           CMP     #$06                
F2EF: B0 02           BCS     $F2F3               ; {}
F2F1: A9 06           LDA     #$06                
F2F3: 85 C4           STA     $C4                 ; {ram.mC4}
F2F5: A5 C5           LDA     $C5                 ; {ram.mC5}
F2F7: 2A              ROL     A                   
F2F8: 2A              ROL     A                   
F2F9: 30 04           BMI     $F2FF               ; {}
F2FB: A9 00           LDA     #$00                
F2FD: F0 C3           BEQ     $F2C2               ; {}
F2FF: A2 13           LDX     #$13                
F301: 90 01           BCC     $F304               ; {}
F303: E8              INX                         
F304: A9 0C           LDA     #$0C                
F306: 10 BA           BPL     $F2C2               ; {}
F308: 66 F4           ROR     $F4                 ; {ram.mF4}
F30A: B0 02           BCS     $F30E               ; {}
F30C: 09 40           ORA     #$40                
F30E: 85 C5           STA     $C5                 ; {ram.mC5}
F310: A9 08           LDA     #$08                
F312: 85 C4           STA     $C4                 ; {ram.mC4}
F314: 10 DF           BPL     $F2F5               ; {}
```

# Vertical Blank

```code
VerticalBlank:
F316: A2 FF           LDX     #$FF                ; All 1s
F318: AD 84 02        LDA     $0284               ; {hard.INTIM} Timer reached zero?INTIM:lots
F31B: D0 FB           BNE     $F318               ; {} No ... wait for end of frame
F31D: 86 01           STX     $01                 ; {hard.VBLANK} Vertical blank clearVBLANK:74,263
F31F: 86 00           STX     $00                 ; {hard.VSYNC} Vertical sync clearVSYNC:74,263
F321: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:1
F323: 85 02           STA     $02                 ; {hard.WSYNC} WSYNC  3 linesWSYNC:2
F325: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:3
F327: 85 00           STA     $00                 ; {hard.VSYNC} Vertical syncVSYNC:4
F329: 85 01           STA     $01                 ; {hard.VBLANK} Veritcal blankVBLANK:4
F32B: A9 2D           LDA     #$2D                ; 45 * 64 = 2880 clocks
F32D: 8D 96 02        STA     $0296               ; {hard.TIM64T} Start TIM64T timer for vertical blankTIM64T:4
F330: E6 B9           INC     $B9                 ; {ram.mB9} Count frames for odd/even actions
F332: D0 1E           BNE     $F352               ; {}
F334: E6 BA           INC     $BA                 ; {ram.mBA}
F336: 24 C7           BIT     $C7                 ; {ram.mC7}
F338: 70 18           BVS     $F352               ; {}
F33A: A5 C8           LDA     $C8                 ; {ram.mC8}
F33C: 6A              ROR     A                   
F33D: 90 13           BCC     $F352               ; {}
F33F: A5 BA           LDA     $BA                 ; {ram.mBA}
F341: 10 06           BPL     $F349               ; {}
F343: A5 C7           LDA     $C7                 ; {ram.mC7}
F345: 09 40           ORA     #$40                
F347: 85 C7           STA     $C7                 ; {ram.mC7}
F349: A5 80           LDA     $80                 ; {ram.m80}
F34B: 29 20           AND     #$20                
F34D: F0 03           BEQ     $F352               ; {}
F34F: 20 C5 FA        JSR     $FAC5               ; {}
F352: 20 D9 FA        JSR     $FAD9               ; {}
F355: A5 B9           LDA     $B9                 ; {ram.mB9}
F357: 6A              ROR     A                   
F358: B0 03           BCS     $F35D               ; {}
F35A: 4C D7 F5        JMP     $F5D7               ; {}
F35D: A0 00           LDY     #$00                
F35F: A5 BB           LDA     $BB                 ; {ram.mBB}
F361: 38              SEC                         
F362: E9 11           SBC     #$11                
F364: C9 10           CMP     #$10                
F366: B0 04           BCS     $F36C               ; {}
F368: 09 70           ORA     #$70                
F36A: C8              INY                         
F36B: C8              INY                         
F36C: AA              TAX                         
F36D: 29 0F           AND     #$0F                
F36F: D0 05           BNE     $F376               ; {}
F371: 8A              TXA                         
F372: 09 03           ORA     #$03                
F374: AA              TAX                         
F375: C8              INY                         
F376: 86 BB           STX     $BB                 ; {ram.mBB}
F378: 98              TYA                         
F379: 6A              ROR     A                   
F37A: 6A              ROR     A                   
F37B: 6A              ROR     A                   
F37C: 85 EC           STA     $EC                 ; {ram.mEC}
F37E: A9 C0           LDA     #$C0                
F380: 85 E3           STA     $E3                 ; {ram.mE3}
F382: A9 CF           LDA     #$CF                
F384: 85 E5           STA     $E5                 ; {ram.mE5}
F386: A9 DE           LDA     #$DE                
F388: 85 F2           STA     $F2                 ; {ram.mF2}
F38A: A2 09           LDX     #$09                
F38C: B5 83           LDA     $83,X               ; {ram.m83}
F38E: C9 E0           CMP     #$E0                
F390: F0 08           BEQ     $F39A               ; {}
F392: F6 83           INC     $83,X               ; {ram.m83}
F394: 20 32 FA        JSR     $FA32               ; {}
F397: E8              INX                         
F398: D0 F2           BNE     $F38C               ; {}
F39A: A6 DD           LDX     $DD                 ; {ram.mDD}
F39C: B5 83           LDA     $83,X               ; {ram.m83}
F39E: C9 E0           CMP     #$E0                
F3A0: F0 75           BEQ     $F417               ; {}
F3A2: C9 59           CMP     #$59                
F3A4: 90 08           BCC     $F3AE               ; {}
F3A6: A9 E0           LDA     #$E0                
F3A8: 95 83           STA     $83,X               ; {ram.m83}
F3AA: C6 DD           DEC     $DD                 ; {ram.mDD}
F3AC: D0 EC           BNE     $F39A               ; {}
F3AE: B5 A7           LDA     $A7,X               ; {ram.mA7}
F3B0: 4A              LSR     A                   
F3B1: 4A              LSR     A                   
F3B2: 4A              LSR     A                   
F3B3: 4A              LSR     A                   
F3B4: 29 03           AND     #$03                
F3B6: A8              TAY                         
F3B7: B5 83           LDA     $83,X               ; {ram.m83}
F3B9: D9 52 FF        CMP     $FF52,Y             ; {}
F3BC: D0 11           BNE     $F3CF               ; {}
F3BE: 86 F5           STX     $F5                 ; {ram.mF5}
F3C0: A9 09           LDA     #$09                
F3C2: 85 F4           STA     $F4                 ; {ram.mF4}
F3C4: 20 6B FE        JSR     $FE6B               ; {}
F3C7: B9 83 00        LDA     $0083,Y             ; {ram.m83}
F3CA: 38              SEC                         
F3CB: E9 59           SBC     #$59                
F3CD: 95 83           STA     $83,X               ; {ram.m83}
F3CF: A2 09           LDX     #$09                
F3D1: B5 83           LDA     $83,X               ; {ram.m83}
F3D3: C9 E0           CMP     #$E0                
F3D5: F0 40           BEQ     $F417               ; {}
F3D7: B5 95           LDA     $95,X               ; {ram.m95}
F3D9: 85 EA           STA     $EA                 ; {ram.mEA}
F3DB: 4A              LSR     A                   
F3DC: 29 07           AND     #$07                
F3DE: 85 E8           STA     $E8                 ; {ram.mE8}
F3E0: B5 83           LDA     $83,X               ; {ram.m83}
F3E2: 10 33           BPL     $F417               ; {}
F3E4: C9 FF           CMP     #$FF                
F3E6: F0 2F           BEQ     $F417               ; {}
F3E8: B5 95           LDA     $95,X               ; {ram.m95}
F3EA: 6A              ROR     A                   
F3EB: A0 45           LDY     #$45                
F3ED: B0 02           BCS     $F3F1               ; {}
F3EF: A0 0B           LDY     #$0B                
F3F1: 84 E5           STY     $E5                 ; {ram.mE5}
F3F3: B5 A7           LDA     $A7,X               ; {ram.mA7}
F3F5: 29 70           AND     #$70                
F3F7: 38              SEC                         
F3F8: E9 02           SBC     #$02                
F3FA: 38              SEC                         
F3FB: F5 83           SBC     $83,X               ; {ram.m83}
F3FD: 85 ED           STA     $ED                 ; {ram.mED}
F3FF: 85 F1           STA     $F1                 ; {ram.mF1}
F401: A0 D9           LDY     #$D9                
F403: 84 F8           STY     $F8                 ; {ram.mF8}
F405: A0 0F           LDY     #$0F                
F407: 84 F7           STY     $F7                 ; {ram.mF7}
F409: 4C F0 FF        JMP     $FFF0               ; {code.SwitchToBank0} Bank switch to D90F
F40C: 29 08           AND     #$08                
F40E: D0 07           BNE     $F417               ; {}
F410: A5 EA           LDA     $EA                 ; {ram.mEA}
F412: 18              CLC                         
F413: 69 10           ADC     #$10                
F415: 85 EA           STA     $EA                 ; {ram.mEA}
F417: A5 95           LDA     $95                 ; {ram.m95}
F419: 85 E9           STA     $E9                 ; {ram.mE9}
F41B: 4A              LSR     A                   
F41C: 29 07           AND     #$07                
F41E: 85 E7           STA     $E7                 ; {ram.mE7}
F420: A2 00           LDX     #$00                
F422: F0 06           BEQ     $F42A               ; {}
F424: D6 83           DEC     $83,X               ; {ram.m83}
F426: 20 32 FA        JSR     $FA32               ; {}
F429: E8              INX                         
F42A: B5 83           LDA     $83,X               ; {ram.m83}
F42C: F0 08           BEQ     $F436               ; {}
F42E: 10 F4           BPL     $F424               ; {}
F430: C9 E0           CMP     #$E0                
F432: F0 6A           BEQ     $F49E               ; {}
F434: D0 1F           BNE     $F455               ; {}
F436: A6 DC           LDX     $DC                 ; {ram.mDC}
F438: B5 83           LDA     $83,X               ; {ram.m83}
F43A: C9 E0           CMP     #$E0                
F43C: F0 01           BEQ     $F43F               ; {}
F43E: E8              INX                         
F43F: A9 59           LDA     #$59                
F441: 95 83           STA     $83,X               ; {ram.m83}
F443: A5 95           LDA     $95                 ; {ram.m95}
F445: 95 95           STA     $95,X               ; {ram.m95}
F447: A5 A7           LDA     $A7                 ; {ram.mA7}
F449: 95 A7           STA     $A7,X               ; {ram.mA7}
F44B: A9 E0           LDA     #$E0                
F44D: 95 84           STA     $84,X               ; {ram.m84}
F44F: E6 DC           INC     $DC                 ; {ram.mDC}
F451: A2 00           LDX     #$00                
F453: F0 CF           BEQ     $F424               ; {}
F455: C6 83           DEC     $83                 ; {ram.m83}
F457: A5 A7           LDA     $A7                 ; {ram.mA7}
F459: 6A              ROR     A                   
F45A: 6A              ROR     A                   
F45B: 6A              ROR     A                   
F45C: 6A              ROR     A                   
F45D: 29 03           AND     #$03                
F45F: A8              TAY                         
F460: A5 83           LDA     $83                 ; {ram.m83}
F462: D9 4E FF        CMP     $FF4E,Y             ; {}
F465: F0 31           BEQ     $F498               ; {}
F467: A5 A7           LDA     $A7                 ; {ram.mA7}
F469: 29 70           AND     #$70                
F46B: 38              SEC                         
F46C: E5 83           SBC     $83                 ; {ram.m83}
F46E: 38              SEC                         
F46F: E9 02           SBC     #$02                
F471: 85 EB           STA     $EB                 ; {ram.mEB}
F473: 85 EF           STA     $EF                 ; {ram.mEF}
F475: A0 D9           LDY     #$D9                
F477: 84 F8           STY     $F8                 ; {ram.mF8}
F479: A0 00           LDY     #$00                
F47B: 84 F7           STY     $F7                 ; {ram.mF7}
F47D: 4C F0 FF        JMP     $FFF0               ; {code.SwitchToBank0} Bank switch to D900
F480: 29 08           AND     #$08                
F482: D0 07           BNE     $F48B               ; {}
F484: A5 E9           LDA     $E9                 ; {ram.mE9}
F486: 18              CLC                         
F487: 69 10           ADC     #$10                
F489: 85 E9           STA     $E9                 ; {ram.mE9}
F48B: A0 46           LDY     #$46                
F48D: A5 95           LDA     $95                 ; {ram.m95}
F48F: 6A              ROR     A                   
F490: B0 02           BCS     $F494               ; {}
F492: A0 0E           LDY     #$0E                
F494: 84 E3           STY     $E3                 ; {ram.mE3}
F496: D0 8E           BNE     $F426               ; {}
F498: 20 D8 FD        JSR     $FDD8               ; {}
F49B: 4C 17 F4        JMP     $F417               ; {}
F49E: AD 82 02        LDA     $0282               ; {hard.SWCHB} SWCHB:lots
F4A1: 24 C7           BIT     $C7                 ; {ram.mC7}
F4A3: 30 01           BMI     $F4A6               ; {}
F4A5: 0A              ASL     A                   
F4A6: 0A              ASL     A                   
F4A7: B0 07           BCS     $F4B0               ; {}
F4A9: A5 C5           LDA     $C5                 ; {ram.mC5}
F4AB: 29 F7           AND     #$F7                
F4AD: 4C 60 F5        JMP     $F560               ; {}
F4B0: A5 D2           LDA     $D2                 ; {ram.mD2}
F4B2: C9 E0           CMP     #$E0                
F4B4: D0 5B           BNE     $F511               ; {}
F4B6: A5 CA           LDA     $CA                 ; {ram.mCA}
F4B8: C9 E0           CMP     #$E0                
F4BA: F0 4A           BEQ     $F506               ; {}
F4BC: A9 03           LDA     #$03                
F4BE: C5 BA           CMP     $BA                 ; {ram.mBA}
F4C0: B0 44           BCS     $F506               ; {}
F4C2: C6 C6           DEC     $C6                 ; {ram.mC6}
F4C4: D0 40           BNE     $F506               ; {}
F4C6: A5 C5           LDA     $C5                 ; {ram.mC5}
F4C8: 09 08           ORA     #$08                
F4CA: 85 C5           STA     $C5                 ; {ram.mC5}
F4CC: 20 D9 FA        JSR     $FAD9               ; {}
F4CF: 4A              LSR     A                   
F4D0: AA              TAX                         
F4D1: 29 06           AND     #$06                
F4D3: 85 F4           STA     $F4                 ; {ram.mF4}
F4D5: A5 C7           LDA     $C7                 ; {ram.mC7}
F4D7: 29 F8           AND     #$F8                
F4D9: 05 F4           ORA     $F4                 ; {ram.mF4}
F4DB: 90 02           BCC     $F4DF               ; {}
F4DD: 09 01           ORA     #$01                
F4DF: 85 C7           STA     $C7                 ; {ram.mC7}
F4E1: A9 BA           LDA     #$BA                
F4E3: 85 D1           STA     $D1                 ; {ram.mD1}
F4E5: 8A              TXA                         
F4E6: C9 4F           CMP     #$4F                
F4E8: F0 04           BEQ     $F4EE               ; {}
F4EA: 90 02           BCC     $F4EE               ; {}
F4EC: E9 4F           SBC     #$4F                
F4EE: 85 D2           STA     $D2                 ; {ram.mD2}
F4F0: A5 BD           LDA     $BD                 ; {ram.mBD}
F4F2: C9 15           CMP     #$15                
F4F4: B0 13           BCS     $F509               ; {}
F4F6: C9 07           CMP     #$07                
F4F8: 90 06           BCC     $F500               ; {}
F4FA: 20 D9 FA        JSR     $FAD9               ; {}
F4FD: 6A              ROR     A                   
F4FE: 90 09           BCC     $F509               ; {}
F500: A5 C7           LDA     $C7                 ; {ram.mC7}
F502: 29 DF           AND     #$DF                
F504: 85 C7           STA     $C7                 ; {ram.mC7}
F506: 4C B8 F5        JMP     $F5B8               ; {}
F509: A5 C7           LDA     $C7                 ; {ram.mC7}
F50B: 09 20           ORA     #$20                
F50D: 85 C7           STA     $C7                 ; {ram.mC7}
F50F: D0 F5           BNE     $F506               ; {}
F511: A5 C7           LDA     $C7                 ; {ram.mC7}
F513: 29 06           AND     #$06                
F515: F0 33           BEQ     $F54A               ; {}
F517: C9 06           CMP     #$06                
F519: F0 2F           BEQ     $F54A               ; {}
F51B: C9 02           CMP     #$02                
F51D: F0 0A           BEQ     $F529               ; {}
F51F: E6 D2           INC     $D2                 ; {ram.mD2}
F521: A5 D2           LDA     $D2                 ; {ram.mD2}
F523: C9 4F           CMP     #$4F                
F525: D0 0F           BNE     $F536               ; {}
F527: F0 04           BEQ     $F52D               ; {}
F529: C6 D2           DEC     $D2                 ; {ram.mD2}
F52B: D0 09           BNE     $F536               ; {}
F52D: A5 C7           LDA     $C7                 ; {ram.mC7}
F52F: 49 06           EOR     #$06                
F531: 85 C7           STA     $C7                 ; {ram.mC7}
F533: 4C 4A F5        JMP     $F54A               ; {}
F536: A5 B9           LDA     $B9                 ; {ram.mB9}
F538: 0A              ASL     A                   
F539: D0 0F           BNE     $F54A               ; {}
F53B: 20 D9 FA        JSR     $FAD9               ; {}
F53E: 29 06           AND     #$06                
F540: 85 F4           STA     $F4                 ; {ram.mF4}
F542: A5 C7           LDA     $C7                 ; {ram.mC7}
F544: 29 F9           AND     #$F9                
F546: 05 F4           ORA     $F4                 ; {ram.mF4}
F548: 85 C7           STA     $C7                 ; {ram.mC7}
F54A: A2 3C           LDX     #$3C                
F54C: A5 C7           LDA     $C7                 ; {ram.mC7}
F54E: 6A              ROR     A                   
F54F: 20 59 FA        JSR     $FA59               ; {}
F552: A5 D1           LDA     $D1                 ; {ram.mD1}
F554: C9 BA           CMP     #$BA                
F556: D0 10           BNE     $F568               ; {}
F558: A9 00           LDA     #$00                
F55A: 85 C6           STA     $C6                 ; {ram.mC6}
F55C: A5 C5           LDA     $C5                 ; {ram.mC5}
F55E: 29 E7           AND     #$E7                
F560: 85 C5           STA     $C5                 ; {ram.mC5}
F562: A9 E0           LDA     #$E0                
F564: 85 D2           STA     $D2                 ; {ram.mD2}
F566: D0 9E           BNE     $F506               ; {}
F568: A5 DB           LDA     $DB                 ; {ram.mDB}
F56A: D0 9A           BNE     $F506               ; {}
F56C: 20 D9 FA        JSR     $FAD9               ; {}
F56F: 29 0F           AND     #$0F                
F571: AA              TAX                         
F572: A5 C7           LDA     $C7                 ; {ram.mC7}
F574: 0A              ASL     A                   
F575: 0A              ASL     A                   
F576: 0A              ASL     A                   
F577: 8A              TXA                         
F578: 90 2D           BCC     $F5A7               ; {}
F57A: 29 03           AND     #$03                
F57C: 85 F4           STA     $F4                 ; {ram.mF4}
F57E: A5 D1           LDA     $D1                 ; {ram.mD1}
F580: 20 C1 FC        JSR     $FCC1               ; {}
F583: 85 F5           STA     $F5                 ; {ram.mF5}
F585: A5 C9           LDA     $C9                 ; {ram.mC9}
F587: 20 C1 FC        JSR     $FCC1               ; {}
F58A: A0 00           LDY     #$00                
F58C: 38              SEC                         
F58D: E5 F5           SBC     $F5                 ; {ram.mF5}
F58F: 90 02           BCC     $F593               ; {}
F591: A0 08           LDY     #$08                
F593: A5 CA           LDA     $CA                 ; {ram.mCA}
F595: 38              SEC                         
F596: E5 D2           SBC     $D2                 ; {ram.mD2}
F598: 98              TYA                         
F599: 90 07           BCC     $F5A2               ; {}
F59B: D0 07           BNE     $F5A4               ; {}
F59D: 18              CLC                         
F59E: 69 04           ADC     #$04                
F5A0: 10 02           BPL     $F5A4               ; {}
F5A2: D0 F9           BNE     $F59D               ; {}
F5A4: 18              CLC                         
F5A5: 65 F4           ADC     $F4                 ; {ram.mF4}
F5A7: AA              TAX                         
F5A8: 1D D5 FE        ORA     $FED5,X             ; {}
F5AB: 85 DB           STA     $DB                 ; {ram.mDB}
F5AD: A5 D1           LDA     $D1                 ; {ram.mD1}
F5AF: 85 D5           STA     $D5                 ; {ram.mD5}
F5B1: A5 D2           LDA     $D2                 ; {ram.mD2}
F5B3: 18              CLC                         
F5B4: 69 03           ADC     #$03                
F5B6: 85 D8           STA     $D8                 ; {ram.mD8}
F5B8: A9 DF           LDA     #$DF                
F5BA: 85 EC           STA     $EC                 ; {ram.mEC}
F5BC: 85 EE           STA     $EE                 ; {ram.mEE}
F5BE: A9 DE           LDA     #$DE                
F5C0: 85 F0           STA     $F0                 ; {ram.mF0}
F5C2: 85 F2           STA     $F2                 ; {ram.mF2}
F5C4: A9 D0           LDA     #$D0                
F5C6: 85 E4           STA     $E4                 ; {ram.mE4}
F5C8: A9 D1           LDA     #$D1                
F5CA: 85 E6           STA     $E6                 ; {ram.mE6}
F5CC: A9 00           LDA     #$00                
F5CE: 85 DC           STA     $DC                 ; {ram.mDC}
F5D0: A9 09           LDA     #$09                
F5D2: 85 DD           STA     $DD                 ; {ram.mDD}
F5D4: 4C 8E FF        JMP     $FF8E               ; {}
F5D7: A9 4C           LDA     #$4C                
F5D9: 24 C7           BIT     $C7                 ; {ram.mC7}
F5DB: 10 02           BPL     $F5DF               ; {}
F5DD: A9 DC           LDA     #$DC                
F5DF: 85 E9           STA     $E9                 ; {ram.mE9}
F5E1: 85 E8           STA     $E8                 ; {ram.mE8}
F5E3: A2 9C           LDX     #$9C                
F5E5: A5 C7           LDA     $C7                 ; {ram.mC7}
F5E7: 29 20           AND     #$20                
F5E9: F0 02           BEQ     $F5ED               ; {}
F5EB: A2 EC           LDX     #$EC                
F5ED: 86 EA           STX     $EA                 ; {ram.mEA}
F5EF: A9 00           LDA     #$00                
F5F1: 85 E0           STA     $E0                 ; {ram.mE0}
F5F3: A5 BC           LDA     $BC                 ; {ram.mBC}
F5F5: 05 BF           ORA     $BF                 ; {ram.mBF}
F5F7: 29 F0           AND     #$F0                
F5F9: D0 2B           BNE     $F626               ; {}
F5FB: 85 1A           STA     $1A                 ; {hard.AUDV1} AUDV1:5
F5FD: A5 C8           LDA     $C8                 ; {ram.mC8}
F5FF: 6A              ROR     A                   
F600: B0 0D           BCS     $F60F               ; {}
F602: A2 01           LDX     #$01                
F604: 86 BA           STX     $BA                 ; {ram.mBA}
F606: CA              DEX                         
F607: 86 B9           STX     $B9                 ; {ram.mB9}
F609: A5 C8           LDA     $C8                 ; {ram.mC8}
F60B: 09 01           ORA     #$01                
F60D: 85 C8           STA     $C8                 ; {ram.mC8}
F60F: A5 BA           LDA     $BA                 ; {ram.mBA}
F611: 2A              ROL     A                   
F612: 69 00           ADC     #$00                
F614: 2A              ROL     A                   
F615: 69 00           ADC     #$00                
F617: 2A              ROL     A                   
F618: 69 00           ADC     #$00                
F61A: 2A              ROL     A                   
F61B: 69 00           ADC     #$00                
F61D: 29 F7           AND     #$F7                
F61F: 85 09           STA     $09                 ; {hard.COLUBK} COLUBK:5
F621: 85 E0           STA     $E0                 ; {ram.mE0}
F623: 4C 34 F8        JMP     $F834               ; {}
F626: AD 80 02        LDA     $0280               ; {hard.SWCHA} SWCHA:5
F629: 24 C7           BIT     $C7                 ; {ram.mC7}
F62B: 10 04           BPL     $F631               ; {}
F62D: 0A              ASL     A                   
F62E: 0A              ASL     A                   
F62F: 0A              ASL     A                   
F630: 0A              ASL     A                   
F631: 29 F0           AND     #$F0                
F633: 85 F3           STA     $F3                 ; {ram.mF3}
F635: 24 C8           BIT     $C8                 ; {ram.mC8}
F637: 50 30           BVC     $F669               ; {}
F639: 29 20           AND     #$20                
F63B: F0 09           BEQ     $F646               ; {}
F63D: A5 C8           LDA     $C8                 ; {ram.mC8}
F63F: 29 BF           AND     #$BF                
F641: 85 C8           STA     $C8                 ; {ram.mC8}
F643: 4C 69 F6        JMP     $F669               ; {}
F646: E6 DE           INC     $DE                 ; {ram.mDE}
F648: A5 DE           LDA     $DE                 ; {ram.mDE}
F64A: 29 1F           AND     #$1F                
F64C: D0 18           BNE     $F666               ; {}
F64E: A5 C8           LDA     $C8                 ; {ram.mC8}
F650: 29 BF           AND     #$BF                
F652: 09 02           ORA     #$02                
F654: 85 C8           STA     $C8                 ; {ram.mC8}
F656: A9 80           LDA     #$80                
F658: 85 DE           STA     $DE                 ; {ram.mDE}
F65A: A5 C5           LDA     $C5                 ; {ram.mC5}
F65C: 09 01           ORA     #$01                
F65E: 29 FD           AND     #$FD                
F660: 85 C5           STA     $C5                 ; {ram.mC5}
F662: A9 0F           LDA     #$0F                
F664: 85 C3           STA     $C3                 ; {ram.mC3}
F666: 4C B1 F7        JMP     $F7B1               ; {}
F669: A5 CA           LDA     $CA                 ; {ram.mCA}
F66B: C9 E0           CMP     #$E0                
F66D: F0 0A           BEQ     $F679               ; {}
F66F: A5 DE           LDA     $DE                 ; {ram.mDE}
F671: F0 0F           BEQ     $F682               ; {}
F673: 30 0A           BMI     $F67F               ; {}
F675: C6 DE           DEC     $DE                 ; {ram.mDE}
F677: 10 09           BPL     $F682               ; {}
F679: A5 DE           LDA     $DE                 ; {ram.mDE}
F67B: F0 02           BEQ     $F67F               ; {}
F67D: C6 DE           DEC     $DE                 ; {ram.mDE}
F67F: 4C 34 F8        JMP     $F834               ; {}
F682: A5 F3           LDA     $F3                 ; {ram.mF3}
F684: C9 D0           CMP     #$D0                
F686: D0 68           BNE     $F6F0               ; {}
F688: A5 80           LDA     $80                 ; {ram.m80}
F68A: 29 18           AND     #$18                
F68C: F0 24           BEQ     $F6B2               ; {}
F68E: C9 18           CMP     #$18                
F690: F0 5E           BEQ     $F6F0               ; {}
F692: 29 08           AND     #$08                
F694: D0 12           BNE     $F6A8               ; {}
F696: 24 C8           BIT     $C8                 ; {ram.mC8}
F698: 30 5C           BMI     $F6F6               ; {}
F69A: A5 BC           LDA     $BC                 ; {ram.mBC}
F69C: 49 08           EOR     #$08                
F69E: 85 BC           STA     $BC                 ; {ram.mBC}
F6A0: A5 C8           LDA     $C8                 ; {ram.mC8}
F6A2: 09 80           ORA     #$80                
F6A4: 85 C8           STA     $C8                 ; {ram.mC8}
F6A6: D0 4E           BNE     $F6F6               ; {}
F6A8: A5 C8           LDA     $C8                 ; {ram.mC8}
F6AA: 09 40           ORA     #$40                
F6AC: 85 C8           STA     $C8                 ; {ram.mC8}
F6AE: E6 DE           INC     $DE                 ; {ram.mDE}
F6B0: D0 44           BNE     $F6F6               ; {}
F6B2: A5 C8           LDA     $C8                 ; {ram.mC8}
F6B4: 29 04           AND     #$04                
F6B6: D0 08           BNE     $F6C0               ; {}
F6B8: A5 C8           LDA     $C8                 ; {ram.mC8}
F6BA: 09 04           ORA     #$04                
F6BC: 85 C8           STA     $C8                 ; {ram.mC8}
F6BE: D0 36           BNE     $F6F6               ; {}
F6C0: A5 CA           LDA     $CA                 ; {ram.mCA}
F6C2: C9 E0           CMP     #$E0                
F6C4: F0 30           BEQ     $F6F6               ; {}
F6C6: A9 E0           LDA     #$E0                
F6C8: 85 CA           STA     $CA                 ; {ram.mCA}
F6CA: A5 C8           LDA     $C8                 ; {ram.mC8}
F6CC: 29 F9           AND     #$F9                
F6CE: 85 C8           STA     $C8                 ; {ram.mC8}
F6D0: 20 94 FA        JSR     $FA94               ; {}
F6D3: 85 C9           STA     $C9                 ; {ram.mC9}
F6D5: A5 81           LDA     $81                 ; {ram.m81}
F6D7: 4A              LSR     A                   
F6D8: C9 4F           CMP     #$4F                
F6DA: 90 02           BCC     $F6DE               ; {}
F6DC: E9 4F           SBC     #$4F                
F6DE: 85 DF           STA     $DF                 ; {ram.mDF}
F6E0: A9 00           LDA     #$00                
F6E2: A2 05           LDX     #$05                
F6E4: 95 CB           STA     $CB,X               ; {ram.mCB}
F6E6: CA              DEX                         
F6E7: 10 FB           BPL     $F6E4               ; {}
F6E9: A9 1F           LDA     #$1F                
F6EB: 85 DE           STA     $DE                 ; {ram.mDE}
F6ED: 4C 34 F8        JMP     $F834               ; {}
F6F0: A5 C8           LDA     $C8                 ; {ram.mC8}
F6F2: 29 3B           AND     #$3B                
F6F4: 85 C8           STA     $C8                 ; {ram.mC8}
F6F6: A5 B9           LDA     $B9                 ; {ram.mB9}
F6F8: 6A              ROR     A                   
F6F9: 6A              ROR     A                   
F6FA: 90 1D           BCC     $F719               ; {}
F6FC: A5 BC           LDA     $BC                 ; {ram.mBC}
F6FE: 29 F0           AND     #$F0                
F700: 85 F4           STA     $F4                 ; {ram.mF4}
F702: 06 F3           ASL     $F3                 ; {ram.mF3}
F704: B0 02           BCS     $F708               ; {}
F706: C6 BC           DEC     $BC                 ; {ram.mBC}
F708: 06 F3           ASL     $F3                 ; {ram.mF3}
F70A: B0 02           BCS     $F70E               ; {}
F70C: E6 BC           INC     $BC                 ; {ram.mBC}
F70E: A5 BC           LDA     $BC                 ; {ram.mBC}
F710: 29 0F           AND     #$0F                
F712: 05 F4           ORA     $F4                 ; {ram.mF4}
F714: 85 BC           STA     $BC                 ; {ram.mBC}
F716: 4C 1D F7        JMP     $F71D               ; {}
F719: 06 F3           ASL     $F3                 ; {ram.mF3}
F71B: 06 F3           ASL     $F3                 ; {ram.mF3}
F71D: 06 F3           ASL     $F3                 ; {ram.mF3}
F71F: A0 01           LDY     #$01                
F721: 24 C7           BIT     $C7                 ; {ram.mC7}
F723: 30 02           BMI     $F727               ; {}
F725: A0 00           LDY     #$00                
F727: B9 3C 00        LDA     $003C,Y             ; {hard.INPT4} INPT4:6
F72A: 30 46           BMI     $F772               ; {}
F72C: A5 C7           LDA     $C7                 ; {ram.mC7}
F72E: 29 10           AND     #$10                
F730: D0 46           BNE     $F778               ; {}
F732: A5 C7           LDA     $C7                 ; {ram.mC7}
F734: 09 10           ORA     #$10                
F736: 85 C7           STA     $C7                 ; {ram.mC7}
F738: A0 01           LDY     #$01                
F73A: A5 DA           LDA     $DA                 ; {ram.mDA}
F73C: F0 05           BEQ     $F743               ; {}
F73E: 88              DEY                         
F73F: A5 D9           LDA     $D9                 ; {ram.mD9}
F741: D0 35           BNE     $F778               ; {}
F743: A5 CA           LDA     $CA                 ; {ram.mCA}
F745: 18              CLC                         
F746: 69 03           ADC     #$03                
F748: 99 D6 00        STA     $00D6,Y             ; {ram.mD6}
F74B: A5 C9           LDA     $C9                 ; {ram.mC9}
F74D: 99 D3 00        STA     $00D3,Y             ; {ram.mD3}
F750: A5 C5           LDA     $C5                 ; {ram.mC5}
F752: 29 04           AND     #$04                
F754: D0 0A           BNE     $F760               ; {}
F756: A5 C5           LDA     $C5                 ; {ram.mC5}
F758: 09 10           ORA     #$10                
F75A: 85 C5           STA     $C5                 ; {ram.mC5}
F75C: A9 0F           LDA     #$0F                
F75E: 85 C4           STA     $C4                 ; {ram.mC4}
F760: A5 BC           LDA     $BC                 ; {ram.mBC}
F762: 29 07           AND     #$07                
F764: AA              TAX                         
F765: A5 BC           LDA     $BC                 ; {ram.mBC}
F767: 29 0F           AND     #$0F                
F769: 1D D5 FE        ORA     $FED5,X             ; {}
F76C: 99 D9 00        STA     $00D9,Y             ; {ram.mD9}
F76F: 4C 78 F7        JMP     $F778               ; {}
F772: A5 C7           LDA     $C7                 ; {ram.mC7}
F774: 29 EF           AND     #$EF                
F776: 85 C7           STA     $C7                 ; {ram.mC7}
F778: 06 F3           ASL     $F3                 ; {ram.mF3}
F77A: B0 35           BCS     $F7B1               ; {}
F77C: A5 C5           LDA     $C5                 ; {ram.mC5}
F77E: 09 02           ORA     #$02                
F780: 85 C5           STA     $C5                 ; {ram.mC5}
F782: A5 BC           LDA     $BC                 ; {ram.mBC}
F784: 29 0F           AND     #$0F                
F786: A8              TAY                         
F787: B9 5E FF        LDA     $FF5E,Y             ; {}
F78A: 10 02           BPL     $F78E               ; {}
F78C: C6 CE           DEC     $CE                 ; {ram.mCE}
F78E: 18              CLC                         
F78F: 65 D0           ADC     $D0                 ; {ram.mD0}
F791: 85 D0           STA     $D0                 ; {ram.mD0}
F793: 90 02           BCC     $F797               ; {}
F795: E6 CE           INC     $CE                 ; {ram.mCE}
F797: 98              TYA                         
F798: 18              CLC                         
F799: 69 04           ADC     #$04                
F79B: 29 0F           AND     #$0F                
F79D: A8              TAY                         
F79E: B9 5E FF        LDA     $FF5E,Y             ; {}
F7A1: 10 02           BPL     $F7A5               ; {}
F7A3: C6 CD           DEC     $CD                 ; {ram.mCD}
F7A5: 18              CLC                         
F7A6: 65 CF           ADC     $CF                 ; {ram.mCF}
F7A8: 85 CF           STA     $CF                 ; {ram.mCF}
F7AA: 90 02           BCC     $F7AE               ; {}
F7AC: E6 CD           INC     $CD                 ; {ram.mCD}
F7AE: 4C D7 F7        JMP     $F7D7               ; {}
F7B1: A5 C5           LDA     $C5                 ; {ram.mC5}
F7B3: 29 FD           AND     #$FD                
F7B5: 85 C5           STA     $C5                 ; {ram.mC5}
F7B7: A2 01           LDX     #$01                
F7B9: B5 CD           LDA     $CD,X               ; {ram.mCD}
F7BB: 15 CF           ORA     $CF,X               ; {ram.mCF}
F7BD: F0 15           BEQ     $F7D4               ; {}
F7BF: B5 CD           LDA     $CD,X               ; {ram.mCD}
F7C1: 0A              ASL     A                   
F7C2: A0 FF           LDY     #$FF                
F7C4: 18              CLC                         
F7C5: 49 FF           EOR     #$FF                
F7C7: 30 02           BMI     $F7CB               ; {}
F7C9: C8              INY                         
F7CA: 38              SEC                         
F7CB: 75 CF           ADC     $CF,X               ; {ram.mCF}
F7CD: 95 CF           STA     $CF,X               ; {ram.mCF}
F7CF: 98              TYA                         
F7D0: 75 CD           ADC     $CD,X               ; {ram.mCD}
F7D2: 95 CD           STA     $CD,X               ; {ram.mCD}
F7D4: CA              DEX                         
F7D5: 10 E2           BPL     $F7B9               ; {}
F7D7: A2 01           LDX     #$01                
F7D9: B5 CD           LDA     $CD,X               ; {ram.mCD}
F7DB: A8              TAY                         
F7DC: 2A              ROL     A                   
F7DD: 55 CD           EOR     $CD,X               ; {ram.mCD}
F7DF: 2A              ROL     A                   
F7E0: 98              TYA                         
F7E1: 90 04           BCC     $F7E7               ; {}
F7E3: 49 7F           EOR     #$7F                
F7E5: 95 CD           STA     $CD,X               ; {ram.mCD}
F7E7: 6A              ROR     A                   
F7E8: 6A              ROR     A                   
F7E9: 6A              ROR     A                   
F7EA: 6A              ROR     A                   
F7EB: 29 0F           AND     #$0F                
F7ED: C0 00           CPY     #$00                
F7EF: 10 02           BPL     $F7F3               ; {}
F7F1: 09 F0           ORA     #$F0                
F7F3: 85 F4           STA     $F4                 ; {ram.mF4}
F7F5: 98              TYA                         
F7F6: 2A              ROL     A                   
F7F7: 2A              ROL     A                   
F7F8: 2A              ROL     A                   
F7F9: 2A              ROL     A                   
F7FA: 29 F0           AND     #$F0                
F7FC: 85 F5           STA     $F5                 ; {ram.mF5}
F7FE: B5 CF           LDA     $CF,X               ; {ram.mCF}
F800: 6A              ROR     A                   
F801: 6A              ROR     A                   
F802: 6A              ROR     A                   
F803: 6A              ROR     A                   
F804: 29 0F           AND     #$0F                
F806: 05 F5           ORA     $F5                 ; {ram.mF5}
F808: 18              CLC                         
F809: 75 CB           ADC     $CB,X               ; {ram.mCB}
F80B: 95 CB           STA     $CB,X               ; {ram.mCB}
F80D: A5 F4           LDA     $F4                 ; {ram.mF4}
F80F: 08              PHP                         
F810: E0 00           CPX     #$00                
F812: F0 08           BEQ     $F81C               ; {}
F814: 28              PLP                         
F815: 65 CA           ADC     $CA                 ; {ram.mCA}
F817: 85 CA           STA     $CA                 ; {ram.mCA}
F819: CA              DEX                         
F81A: 10 BD           BPL     $F7D9               ; {}
F81C: 28              PLP                         
F81D: 30 04           BMI     $F823               ; {}
F81F: 69 00           ADC     #$00                
F821: 10 02           BPL     $F825               ; {}
F823: E9 00           SBC     #$00                
F825: 38              SEC                         
F826: C9 00           CMP     #$00                
F828: 10 03           BPL     $F82D               ; {}
F82A: 49 FF           EOR     #$FF                
F82C: 18              CLC                         
F82D: F0 05           BEQ     $F834               ; {}
F82F: A2 34           LDX     #$34                
F831: 20 B9 FA        JSR     $FAB9               ; {}
F834: A9 DF           LDA     #$DF                
F836: 85 EE           STA     $EE                 ; {ram.mEE}
F838: 85 E7           STA     $E7                 ; {ram.mE7}
F83A: A5 C7           LDA     $C7                 ; {ram.mC7}
F83C: 29 08           AND     #$08                
F83E: F0 26           BEQ     $F866               ; {}
F840: A9 AA           LDA     #$AA                
F842: 18              CLC                         
F843: 65 C6           ADC     $C6                 ; {ram.mC6}
F845: 85 F2           STA     $F2                 ; {ram.mF2}
F847: A5 C6           LDA     $C6                 ; {ram.mC6}
F849: 18              CLC                         
F84A: 69 06           ADC     #$06                
F84C: 85 C6           STA     $C6                 ; {ram.mC6}
F84E: C9 12           CMP     #$12                
F850: D0 20           BNE     $F872               ; {}
F852: A5 C7           LDA     $C7                 ; {ram.mC7}
F854: 29 F7           AND     #$F7                
F856: 85 C7           STA     $C7                 ; {ram.mC7}
F858: A5 C5           LDA     $C5                 ; {ram.mC5}
F85A: 29 E7           AND     #$E7                
F85C: 85 C5           STA     $C5                 ; {ram.mC5}
F85E: A9 00           LDA     #$00                
F860: 85 C6           STA     $C6                 ; {ram.mC6}
F862: A9 E0           LDA     #$E0                
F864: 85 D2           STA     $D2                 ; {ram.mD2}
F866: A2 C2           LDX     #$C2                
F868: A5 C7           LDA     $C7                 ; {ram.mC7}
F86A: 29 20           AND     #$20                
F86C: D0 02           BNE     $F870               ; {}
F86E: A2 C6           LDX     #$C6                
F870: 86 F2           STX     $F2                 ; {ram.mF2}
F872: A9 79           LDA     #$79                
F874: 85 E6           STA     $E6                 ; {ram.mE6}
F876: A2 00           LDX     #$00                
F878: A5 DE           LDA     $DE                 ; {ram.mDE}
F87A: 10 31           BPL     $F8AD               ; {}
F87C: E6 DE           INC     $DE                 ; {ram.mDE}
F87E: A5 DE           LDA     $DE                 ; {ram.mDE}
F880: 6A              ROR     A                   
F881: 29 07           AND     #$07                
F883: 18              CLC                         
F884: 69 09           ADC     #$09                
F886: C9 0C           CMP     #$0C                
F888: D0 3F           BNE     $F8C9               ; {}
F88A: A9 E0           LDA     #$E0                
F88C: 85 CA           STA     $CA                 ; {ram.mCA}
F88E: A9 3F           LDA     #$3F                
F890: 85 DE           STA     $DE                 ; {ram.mDE}
F892: A9 1D           LDA     #$1D                
F894: 85 C9           STA     $C9                 ; {ram.mC9}
F896: A9 29           LDA     #$29                
F898: 85 DF           STA     $DF                 ; {ram.mDF}
F89A: A5 BC           LDA     $BC                 ; {ram.mBC}
F89C: 29 F0           AND     #$F0                
F89E: 38              SEC                         
F89F: E9 10           SBC     #$10                
F8A1: A8              TAY                         
F8A2: 29 F0           AND     #$F0                
F8A4: D0 01           BNE     $F8A7               ; {}
F8A6: A8              TAY                         
F8A7: 84 BC           STY     $BC                 ; {ram.mBC}
F8A9: A9 0C           LDA     #$0C                
F8AB: 10 1C           BPL     $F8C9               ; {}
F8AD: 24 C8           BIT     $C8                 ; {ram.mC8}
F8AF: 50 08           BVC     $F8B9               ; {}
F8B1: A9 00           LDA     #$00                
F8B3: 85 F4           STA     $F4                 ; {ram.mF4}
F8B5: A9 BC           LDA     #$BC                
F8B7: D0 1A           BNE     $F8D3               ; {}
F8B9: A5 BC           LDA     $BC                 ; {ram.mBC}
F8BB: 29 0F           AND     #$0F                
F8BD: C9 08           CMP     #$08                
F8BF: 90 08           BCC     $F8C9               ; {}
F8C1: A2 08           LDX     #$08                
F8C3: 29 07           AND     #$07                
F8C5: 49 FF           EOR     #$FF                
F8C7: 69 08           ADC     #$08                
F8C9: 86 F4           STX     $F4                 ; {ram.mF4}
F8CB: 85 F5           STA     $F5                 ; {ram.mF5}
F8CD: 0A              ASL     A                   
F8CE: 65 F5           ADC     $F5                 ; {ram.mF5}
F8D0: 0A              ASL     A                   
F8D1: 69 74           ADC     #$74                
F8D3: 85 F1           STA     $F1                 ; {ram.mF1}
F8D5: A5 CA           LDA     $CA                 ; {ram.mCA}
F8D7: C9 E0           CMP     #$E0                
F8D9: D0 08           BNE     $F8E3               ; {}
F8DB: 85 EF           STA     $EF                 ; {ram.mEF}
F8DD: A9 79           LDA     #$79                
F8DF: 85 ED           STA     $ED                 ; {ram.mED}
F8E1: D0 3E           BNE     $F921               ; {}
F8E3: A5 CA           LDA     $CA                 ; {ram.mCA}
F8E5: 30 15           BMI     $F8FC               ; {}
F8E7: 85 EF           STA     $EF                 ; {ram.mEF}
F8E9: 38              SEC                         
F8EA: E9 54           SBC     #$54                
F8EC: 90 08           BCC     $F8F6               ; {}
F8EE: 18              CLC                         
F8EF: 69 FB           ADC     #$FB                
F8F1: 85 CA           STA     $CA                 ; {ram.mCA}
F8F3: 4C D5 F8        JMP     $F8D5               ; {}
F8F6: A9 79           LDA     #$79                
F8F8: 85 ED           STA     $ED                 ; {ram.mED}
F8FA: D0 1B           BNE     $F917               ; {}
F8FC: C9 FB           CMP     #$FB                
F8FE: B0 09           BCS     $F909               ; {}
F900: A9 59           LDA     #$59                
F902: 18              CLC                         
F903: 65 CA           ADC     $CA                 ; {ram.mCA}
F905: 85 CA           STA     $CA                 ; {ram.mCA}
F907: D0 DE           BNE     $F8E7               ; {}
F909: 49 FF           EOR     #$FF                
F90B: 38              SEC                         
F90C: 65 F1           ADC     $F1                 ; {ram.mF1}
F90E: 85 ED           STA     $ED                 ; {ram.mED}
F910: A9 59           LDA     #$59                
F912: 18              CLC                         
F913: 65 CA           ADC     $CA                 ; {ram.mCA}
F915: 85 EF           STA     $EF                 ; {ram.mEF}
F917: A5 CC           LDA     $CC                 ; {ram.mCC}
F919: 2A              ROL     A                   
F91A: 2A              ROL     A                   
F91B: 29 01           AND     #$01                
F91D: 05 F4           ORA     $F4                 ; {ram.mF4}
F91F: 85 EB           STA     $EB                 ; {ram.mEB}
F921: A2 40           LDX     #$40                
F923: 86 F6           STX     $F6                 ; {ram.mF6}
F925: A2 02           LDX     #$02                
F927: B5 D9           LDA     $D9,X               ; {ram.mD9}
F929: D0 1B           BNE     $F946               ; {}
F92B: A0 E0           LDY     #$E0                
F92D: A5 C9           LDA     $C9                 ; {ram.mC9}
F92F: E0 02           CPX     #$02                
F931: D0 02           BNE     $F935               ; {}
F933: A5 D1           LDA     $D1                 ; {ram.mD1}
F935: 94 D6           STY     $D6,X               ; {ram.mD6}
F937: 95 D3           STA     $D3,X               ; {ram.mD3}
F939: 86 F5           STX     $F5                 ; {ram.mF5}
F93B: A6 F6           LDX     $F6                 ; {ram.mF6}
F93D: 18              CLC                         
F93E: A9 02           LDA     #$02                
F940: 20 B9 FA        JSR     $FAB9               ; {}
F943: 4C AA F9        JMP     $F9AA               ; {}
F946: A5 B9           LDA     $B9                 ; {ram.mB9}
F948: 6A              ROR     A                   
F949: 6A              ROR     A                   
F94A: B0 0F           BCS     $F95B               ; {}
F94C: B5 D9           LDA     $D9,X               ; {ram.mD9}
F94E: 38              SEC                         
F94F: E9 10           SBC     #$10                
F951: 95 D9           STA     $D9,X               ; {ram.mD9}
F953: 29 F0           AND     #$F0                
F955: D0 04           BNE     $F95B               ; {}
F957: 95 D9           STA     $D9,X               ; {ram.mD9}
F959: F0 D0           BEQ     $F92B               ; {}
F95B: B5 D9           LDA     $D9,X               ; {ram.mD9}
F95D: 29 0F           AND     #$0F                
F95F: A8              TAY                         
F960: A5 CE           LDA     $CE                 ; {ram.mCE}
F962: 08              PHP                         
F963: 4A              LSR     A                   
F964: 4A              LSR     A                   
F965: 4A              LSR     A                   
F966: 4A              LSR     A                   
F967: 28              PLP                         
F968: 10 05           BPL     $F96F               ; {}
F96A: 09 F0           ORA     #$F0                
F96C: 18              CLC                         
F96D: 69 01           ADC     #$01                
F96F: 18              CLC                         
F970: 79 6E FF        ADC     $FF6E,Y             ; {}
F973: 18              CLC                         
F974: 75 D6           ADC     $D6,X               ; {ram.mD6}
F976: 95 D6           STA     $D6,X               ; {ram.mD6}
F978: 10 05           BPL     $F97F               ; {}
F97A: 18              CLC                         
F97B: 69 59           ADC     #$59                
F97D: 10 05           BPL     $F984               ; {}
F97F: 38              SEC                         
F980: E9 59           SBC     #$59                
F982: 90 02           BCC     $F986               ; {}
F984: 95 D6           STA     $D6,X               ; {ram.mD6}
F986: A5 CD           LDA     $CD                 ; {ram.mCD}
F988: 08              PHP                         
F989: 4A              LSR     A                   
F98A: 4A              LSR     A                   
F98B: 4A              LSR     A                   
F98C: 4A              LSR     A                   
F98D: 28              PLP                         
F98E: 10 05           BPL     $F995               ; {}
F990: 09 F0           ORA     #$F0                
F992: 18              CLC                         
F993: 69 01           ADC     #$01                
F995: 86 F5           STX     $F5                 ; {ram.mF5}
F997: A6 F6           LDX     $F6                 ; {ram.mF6}
F999: 18              CLC                         
F99A: 79 7E FF        ADC     $FF7E,Y             ; {}
F99D: 38              SEC                         
F99E: 10 05           BPL     $F9A5               ; {}
F9A0: 49 FF           EOR     #$FF                
F9A2: 69 01           ADC     #$01                
F9A4: 18              CLC                         
F9A5: F0 03           BEQ     $F9AA               ; {}
F9A7: 20 B9 FA        JSR     $FAB9               ; {}
F9AA: 8A              TXA                         
F9AB: 38              SEC                         
F9AC: E9 3E           SBC     #$3E                
F9AE: A8              TAY                         
F9AF: B5 95           LDA     $95,X               ; {ram.m95}
F9B1: 85 02           STA     $02                 ; {hard.WSYNC} WSYNCWSYNC:lots
F9B3: 99 22 00        STA     $0022,Y             ; {hard.HMM0} HMM1:lots HMBL:10,17,15,16 HMM0:lots
F9B6: 6A              ROR     A                   
F9B7: 29 07           AND     #$07                
F9B9: B0 0E           BCS     $F9C9               ; {}
F9BB: A2 06           LDX     #$06                
F9BD: CA              DEX                         
F9BE: D0 FD           BNE     $F9BD               ; {}
F9C0: EA              NOP                         
F9C1: AA              TAX                         
F9C2: CA              DEX                         
F9C3: D0 FD           BNE     $F9C2               ; {}
F9C5: 96 12           STX     $12,Y               ; {hard.RESM0} RESM0:lots RESBL:10,17,15,16 RESM1:lots
F9C7: F0 03           BEQ     $F9CC               ; {}
F9C9: AA              TAX                         
F9CA: B0 F6           BCS     $F9C2               ; {}
F9CC: C6 F6           DEC     $F6                 ; {ram.mF6}
F9CE: C6 F5           DEC     $F5                 ; {ram.mF5}
F9D0: A6 F5           LDX     $F5                 ; {ram.mF5}
F9D2: 30 03           BMI     $F9D7               ; {}
F9D4: 4C 27 F9        JMP     $F927               ; {}
F9D7: 4C 8E FF        JMP     $FF8E               ; {}
```

# Reset (Bank 1)

```code
Reset1:
; Reset comes here if in 2nd ROM bank. The reset in 1st bank does
; a bank switch and comes here.
;
F9DA: 78              SEI                         ; Disable interrupts
F9DB: D8              CLD                         ; Decimal flag
F9DC: A2 FF           LDX     #$FF                ; Set ...
F9DE: 9A              TXS                         ; ... stack pointer
F9DF: E8              INX                         ; Now 0
F9E0: 8A              TXA                         ; Clear ...
F9E1: 95 00           STA     $00,X               ; {hard.VSYNC} ... 1st ...
F9E3: E8              INX                         ; ... 256 bytes ...
F9E4: D0 FB           BNE     $F9E1               ; {} ... of address space

F9E6: A9 E0           LDA     #$E0                
F9E8: 85 CA           STA     $CA                 ; {ram.mCA}
F9EA: A9 34           LDA     #$34                
F9EC: 85 82           STA     $82                 ; {ram.m82}
F9EE: 85 81           STA     $81                 ; {ram.m81}
F9F0: A9 40           LDA     #$40                
F9F2: 85 C7           STA     $C7                 ; {ram.mC7}
F9F4: A9 01           LDA     #$01                
F9F6: 85 C8           STA     $C8                 ; {ram.mC8}
F9F8: D0 04           BNE     $F9FE               ; {}
F9FA: A9 08           LDA     #$08                
F9FC: 85 C7           STA     $C7                 ; {ram.mC7}
F9FE: 85 C4           STA     $C4                 ; {ram.mC4}
FA00: A9 FE           LDA     #$FE                
FA02: 85 F0           STA     $F0                 ; {ram.mF0}
FA04: 85 F2           STA     $F2                 ; {ram.mF2}
FA06: A9 FF           LDA     #$FF                
FA08: 85 EC           STA     $EC                 ; {ram.mEC}
FA0A: 85 EE           STA     $EE                 ; {ram.mEE}
FA0C: A9 F0           LDA     #$F0                
FA0E: 85 E4           STA     $E4                 ; {ram.mE4}
FA10: A9 F1           LDA     #$F1                
FA12: 85 E6           STA     $E6                 ; {ram.mE6}
FA14: 20 EA FD        JSR     $FDEA               ; {}
FA17: A9 73           LDA     #$73                
FA19: 85 BB           STA     $BB                 ; {ram.mBB}
FA1B: A9 CF           LDA     #$CF                
FA1D: 85 E5           STA     $E5                 ; {ram.mE5}
FA1F: A9 E0           LDA     #$E0                
FA21: 85 D8           STA     $D8                 ; {ram.mD8}
FA23: 85 D2           STA     $D2                 ; {ram.mD2}
FA25: A9 1D           LDA     #$1D                
FA27: 85 C9           STA     $C9                 ; {ram.mC9}
FA29: A9 C6           LDA     #$C6                
FA2B: 85 D1           STA     $D1                 ; {ram.mD1}
FA2D: 85 C2           STA     $C2                 ; {ram.mC2}
FA2F: 4C 16 F3        JMP     $F316               ; {code.VerticalBlank}
FA32: B5 A7           LDA     $A7,X               ; {ram.mA7}
FA34: 4A              LSR     A                   
FA35: 4A              LSR     A                   
FA36: 4A              LSR     A                   
FA37: 4A              LSR     A                   
FA38: 85 F5           STA     $F5                 ; {ram.mF5}
FA3A: A5 80           LDA     $80                 ; {ram.m80}
FA3C: 30 17           BMI     $FA55               ; {}
FA3E: 29 01           AND     #$01                
FA40: D0 06           BNE     $FA48               ; {}
FA42: A5 F5           LDA     $F5                 ; {ram.mF5}
FA44: 29 07           AND     #$07                
FA46: 10 02           BPL     $FA4A               ; {}
FA48: A5 F5           LDA     $F5                 ; {ram.mF5}
FA4A: A8              TAY                         
FA4B: B9 DD FE        LDA     $FEDD,Y             ; {}
FA4E: F0 09           BEQ     $FA59               ; {}
FA50: 24 EC           BIT     $EC                 ; {ram.mEC}
FA52: D0 05           BNE     $FA59               ; {}
FA54: 60              RTS                         
FA55: A9 80           LDA     #$80                
FA57: D0 F7           BNE     $FA50               ; {}
FA59: B0 1C           BCS     $FA77               ; {}
FA5B: A9 F0           LDA     #$F0                
FA5D: 75 95           ADC     $95,X               ; {ram.m95}
FA5F: C9 93           CMP     #$93                
FA61: D0 04           BNE     $FA67               ; {}
FA63: A9 65           LDA     #$65                
FA65: D0 2A           BNE     $FA91               ; {}
FA67: C9 70           CMP     #$70                
FA69: 90 26           BCC     $FA91               ; {}
FA6B: C9 80           CMP     #$80                
FA6D: B0 22           BCS     $FA91               ; {}
FA6F: 29 0F           AND     #$0F                
FA71: A8              TAY                         
FA72: B9 EB FE        LDA     $FEEB,Y             ; {}
FA75: D0 1A           BNE     $FA91               ; {}
FA77: A9 0F           LDA     #$0F                
FA79: 75 95           ADC     $95,X               ; {ram.m95}
FA7B: C9 42           CMP     #$42                
FA7D: D0 04           BNE     $FA83               ; {}
FA7F: A9 8D           LDA     #$8D                
FA81: D0 0E           BNE     $FA91               ; {}
FA83: C9 70           CMP     #$70                
FA85: 90 0A           BCC     $FA91               ; {}
FA87: C9 80           CMP     #$80                
FA89: B0 06           BCS     $FA91               ; {}
FA8B: 29 0F           AND     #$0F                
FA8D: A8              TAY                         
FA8E: B9 F6 FE        LDA     $FEF6,Y             ; {}
FA91: 95 95           STA     $95,X               ; {ram.m95}
FA93: 60              RTS                         
FA94: A5 82           LDA     $82                 ; {ram.m82}
FA96: 29 07           AND     #$07                
FA98: A8              TAY                         
FA99: A5 82           LDA     $82                 ; {ram.m82}
FA9B: 29 F0           AND     #$F0                
FA9D: C9 70           CMP     #$70                
FA9F: 90 06           BCC     $FAA7               ; {}
FAA1: C9 80           CMP     #$80                
FAA3: B0 02           BCS     $FAA7               ; {}
FAA5: A9 80           LDA     #$80                
FAA7: 19 04 FF        ORA     $FF04,Y             ; {}
FAAA: C9 42           CMP     #$42                
FAAC: D0 0A           BNE     $FAB8               ; {}
FAAE: C9 52           CMP     #$52                
FAB0: D0 06           BNE     $FAB8               ; {}
FAB2: C9 62           CMP     #$62                
FAB4: D0 02           BNE     $FAB8               ; {}
FAB6: A9 8D           LDA     #$8D                
FAB8: 60              RTS                         

FAB9: A0 D6           LDY     #$D6                
FABB: 84 F8           STY     $F8                 ; {ram.mF8}
FABD: A0 00           LDY     #$00                
FABF: 84 F7           STY     $F7                 ; {ram.mF7}
FAC1: 4C F0 FF        JMP     $FFF0               ; {code.SwitchToBank0} Bank switch to D600

FAC4: 60              RTS                         
FAC5: A2 02           LDX     #$02                
FAC7: B4 BC           LDY     $BC,X               ; {ram.mBC}
FAC9: B5 BF           LDA     $BF,X               ; {ram.mBF}
FACB: 94 BF           STY     $BF,X               ; {ram.mBF}
FACD: 95 BC           STA     $BC,X               ; {ram.mBC}
FACF: CA              DEX                         
FAD0: 10 F5           BPL     $FAC7               ; {}
FAD2: A5 C7           LDA     $C7                 ; {ram.mC7}
FAD4: 49 80           EOR     #$80                
FAD6: 85 C7           STA     $C7                 ; {ram.mC7}
FAD8: 60              RTS                         
FAD9: A5 81           LDA     $81                 ; {ram.m81}
FADB: 0A              ASL     A                   
FADC: 45 81           EOR     $81                 ; {ram.m81}
FADE: 0A              ASL     A                   
FADF: 0A              ASL     A                   
FAE0: 26 82           ROL     $82                 ; {ram.m82}
FAE2: 26 81           ROL     $81                 ; {ram.m81}
FAE4: A5 82           LDA     $82                 ; {ram.m82}
FAE6: 60              RTS                         
FAE7: 86 F6           STX     $F6                 ; {ram.mF6}
FAE9: 18              CLC                         
FAEA: 69 11           ADC     #$11                
FAEC: 85 F5           STA     $F5                 ; {ram.mF5}
FAEE: 18              CLC                         
FAEF: 7D 2A FF        ADC     $FF2A,X             ; {}
FAF2: 85 E2           STA     $E2                 ; {ram.mE2}
FAF4: 98              TYA                         
FAF5: 20 C1 FC        JSR     $FCC1               ; {}
FAF8: 85 F4           STA     $F4                 ; {ram.mF4}
FAFA: A2 00           LDX     #$00                
FAFC: B5 83           LDA     $83,X               ; {ram.m83}
FAFE: C9 E0           CMP     #$E0                
FB00: F0 48           BEQ     $FB4A               ; {}
FB02: A8              TAY                         
FB03: 18              CLC                         
FB04: 69 11           ADC     #$11                
FB06: 30 0A           BMI     $FB12               ; {}
FB08: C5 E2           CMP     $E2                 ; {ram.mE2}
FB0A: B0 24           BCS     $FB30               ; {}
FB0C: 69 0F           ADC     #$0F                
FB0E: C5 F5           CMP     $F5                 ; {ram.mF5}
FB10: 90 1E           BCC     $FB30               ; {}
FB12: B5 A7           LDA     $A7,X               ; {ram.mA7}
FB14: 2A              ROL     A                   
FB15: 2A              ROL     A                   
FB16: B0 18           BCS     $FB30               ; {}
FB18: 2A              ROL     A                   
FB19: 2A              ROL     A                   
FB1A: 2A              ROL     A                   
FB1B: 29 07           AND     #$07                
FB1D: 85 F2           STA     $F2                 ; {ram.mF2}
FB1F: 98              TYA                         
FB20: 18              CLC                         
FB21: 69 03           ADC     #$03                
FB23: B4 95           LDY     $95,X               ; {ram.m95}
FB25: 86 F1           STX     $F1                 ; {ram.mF1}
FB27: A6 F2           LDX     $F2                 ; {ram.mF2}
FB29: 20 A0 FB        JSR     $FBA0               ; {}
FB2C: B0 05           BCS     $FB33               ; {}
FB2E: A6 F1           LDX     $F1                 ; {ram.mF1}
FB30: E8              INX                         
FB31: D0 C9           BNE     $FAFC               ; {}
FB33: A5 83           LDA     $83                 ; {ram.m83}
FB35: 10 12           BPL     $FB49               ; {}
FB37: A6 DC           LDX     $DC                 ; {ram.mDC}
FB39: A5 A7           LDA     $A7                 ; {ram.mA7}
FB3B: 15 A7           ORA     $A7,X               ; {ram.mA7}
FB3D: 29 40           AND     #$40                
FB3F: F0 08           BEQ     $FB49               ; {}
FB41: A5 A7           LDA     $A7                 ; {ram.mA7}
FB43: 09 44           ORA     #$44                
FB45: 85 A7           STA     $A7                 ; {ram.mA7}
FB47: 95 A7           STA     $A7,X               ; {ram.mA7}
FB49: 60              RTS                         
FB4A: A2 09           LDX     #$09                
FB4C: B5 83           LDA     $83,X               ; {ram.m83}
FB4E: C9 E0           CMP     #$E0                
FB50: F0 31           BEQ     $FB83               ; {}
FB52: A8              TAY                         
FB53: 18              CLC                         
FB54: 69 11           ADC     #$11                
FB56: 30 0A           BMI     $FB62               ; {}
FB58: C5 E2           CMP     $E2                 ; {ram.mE2}
FB5A: B0 24           BCS     $FB80               ; {}
FB5C: 69 0F           ADC     #$0F                
FB5E: C5 F5           CMP     $F5                 ; {ram.mF5}
FB60: 90 1E           BCC     $FB80               ; {}
FB62: B5 A7           LDA     $A7,X               ; {ram.mA7}
FB64: 2A              ROL     A                   
FB65: 2A              ROL     A                   
FB66: B0 18           BCS     $FB80               ; {}
FB68: 2A              ROL     A                   
FB69: 2A              ROL     A                   
FB6A: 2A              ROL     A                   
FB6B: 29 07           AND     #$07                
FB6D: 85 F2           STA     $F2                 ; {ram.mF2}
FB6F: 98              TYA                         
FB70: 18              CLC                         
FB71: 69 03           ADC     #$03                
FB73: B4 95           LDY     $95,X               ; {ram.m95}
FB75: 86 F1           STX     $F1                 ; {ram.mF1}
FB77: A6 F2           LDX     $F2                 ; {ram.mF2}
FB79: 20 A0 FB        JSR     $FBA0               ; {}
FB7C: B0 05           BCS     $FB83               ; {}
FB7E: A6 F1           LDX     $F1                 ; {ram.mF1}
FB80: E8              INX                         
FB81: D0 C9           BNE     $FB4C               ; {}
FB83: A0 09           LDY     #$09                
FB85: B9 83 00        LDA     $0083,Y             ; {ram.m83}
FB88: 10 15           BPL     $FB9F               ; {}
FB8A: A6 DD           LDX     $DD                 ; {ram.mDD}
FB8C: B5 A7           LDA     $A7,X               ; {ram.mA7}
FB8E: 19 A7 00        ORA     $00A7,Y             ; {ram.mA7}
FB91: 29 40           AND     #$40                
FB93: F0 0A           BEQ     $FB9F               ; {}
FB95: B9 A7 00        LDA     $00A7,Y             ; {ram.mA7}
FB98: 09 44           ORA     #$44                
FB9A: 95 A7           STA     $A7,X               ; {ram.mA7}
FB9C: 99 A7 00        STA     $00A7,Y             ; {ram.mA7}
FB9F: 60              RTS                         
FBA0: 86 F3           STX     $F3                 ; {ram.mF3}
FBA2: 84 F7           STY     $F7                 ; {ram.mF7}
FBA4: 18              CLC                         
FBA5: 69 11           ADC     #$11                
FBA7: 85 F8           STA     $F8                 ; {ram.mF8}
FBA9: C5 F5           CMP     $F5                 ; {ram.mF5}
FBAB: 90 0D           BCC     $FBBA               ; {}
FBAD: A5 F5           LDA     $F5                 ; {ram.mF5}
FBAF: A6 F6           LDX     $F6                 ; {ram.mF6}
FBB1: 7D 2A FF        ADC     $FF2A,X             ; {}
FBB4: 38              SEC                         
FBB5: E5 F8           SBC     $F8                 ; {ram.mF8}
FBB7: B0 0A           BCS     $FBC3               ; {}
FBB9: 60              RTS                         
FBBA: 18              CLC                         
FBBB: 7D 2A FF        ADC     $FF2A,X             ; {}
FBBE: 38              SEC                         
FBBF: E5 F5           SBC     $F5                 ; {ram.mF5}
FBC1: 90 F6           BCC     $FBB9               ; {}
FBC3: A5 F7           LDA     $F7                 ; {ram.mF7}
FBC5: 20 C1 FC        JSR     $FCC1               ; {}
FBC8: 85 F7           STA     $F7                 ; {ram.mF7}
FBCA: A6 F3           LDX     $F3                 ; {ram.mF3}
FBCC: C5 F4           CMP     $F4                 ; {ram.mF4}
FBCE: 90 0D           BCC     $FBDD               ; {}
FBD0: A5 F4           LDA     $F4                 ; {ram.mF4}
FBD2: A6 F6           LDX     $F6                 ; {ram.mF6}
FBD4: 7D 35 FF        ADC     $FF35,X             ; {}
FBD7: 38              SEC                         
FBD8: E5 F7           SBC     $F7                 ; {ram.mF7}
FBDA: B0 0A           BCS     $FBE6               ; {}
FBDC: 60              RTS                         
FBDD: 18              CLC                         
FBDE: 7D 35 FF        ADC     $FF35,X             ; {}
FBE1: 38              SEC                         
FBE2: E5 F4           SBC     $F4                 ; {ram.mF4}
FBE4: 90 D3           BCC     $FBB9               ; {}
FBE6: A6 F6           LDX     $F6                 ; {ram.mF6}
FBE8: E0 0A           CPX     #$0A                
FBEA: D0 03           BNE     $FBEF               ; {}
FBEC: 4C BB FC        JMP     $FCBB               ; {}
FBEF: E0 05           CPX     #$05                
FBF1: F0 0E           BEQ     $FC01               ; {}
FBF3: E0 06           CPX     #$06                
FBF5: F0 0A           BEQ     $FC01               ; {}
FBF7: A4 F3           LDY     $F3                 ; {ram.mF3}
FBF9: C0 05           CPY     #$05                
FBFB: F0 04           BEQ     $FC01               ; {}
FBFD: C0 06           CPY     #$06                
FBFF: D0 11           BNE     $FC12               ; {}
FC01: A5 C7           LDA     $C7                 ; {ram.mC7}
FC03: 29 08           AND     #$08                
FC05: F0 01           BEQ     $FC08               ; {}
FC07: 60              RTS                         
FC08: A5 C7           LDA     $C7                 ; {ram.mC7}
FC0A: 09 08           ORA     #$08                
FC0C: 85 C7           STA     $C7                 ; {ram.mC7}
FC0E: A9 00           LDA     #$00                
FC10: 85 C6           STA     $C6                 ; {ram.mC6}
FC12: E0 04           CPX     #$04                
FC14: F0 0A           BEQ     $FC20               ; {}
FC16: E0 09           CPX     #$09                
FC18: D0 14           BNE     $FC2E               ; {}
FC1A: A5 F3           LDA     $F3                 ; {ram.mF3}
FC1C: C9 04           CMP     #$04                
FC1E: D0 0E           BNE     $FC2E               ; {}
FC20: A5 DE           LDA     $DE                 ; {ram.mDE}
FC22: 30 E3           BMI     $FC07               ; {}
FC24: A5 C8           LDA     $C8                 ; {ram.mC8}
FC26: 09 02           ORA     #$02                
FC28: 85 C8           STA     $C8                 ; {ram.mC8}
FC2A: A9 80           LDA     #$80                
FC2C: 85 DE           STA     $DE                 ; {ram.mDE}
FC2E: A5 C5           LDA     $C5                 ; {ram.mC5}
FC30: 09 01           ORA     #$01                
FC32: 29 FD           AND     #$FD                
FC34: 85 C5           STA     $C5                 ; {ram.mC5}
FC36: A9 0F           LDA     #$0F                
FC38: 85 C3           STA     $C3                 ; {ram.mC3}
FC3A: A4 F3           LDY     $F3                 ; {ram.mF3}
FC3C: C0 04           CPY     #$04                
FC3E: B0 0C           BCS     $FC4C               ; {}
FC40: A4 F1           LDY     $F1                 ; {ram.mF1}
FC42: B9 A7 00        LDA     $00A7,Y             ; {ram.mA7}
FC45: 09 44           ORA     #$44                
FC47: 99 A7 00        STA     $00A7,Y             ; {ram.mA7}
FC4A: 85 C2           STA     $C2                 ; {ram.mC2}
FC4C: E0 07           CPX     #$07                
FC4E: 10 08           BPL     $FC58               ; {}
FC50: A4 F3           LDY     $F3                 ; {ram.mF3}
FC52: C0 09           CPY     #$09                
FC54: D0 06           BNE     $FC5C               ; {}
FC56: A2 09           LDX     #$09                
FC58: A9 00           LDA     #$00                
FC5A: 95 D2           STA     $D2,X               ; {ram.mD2}
FC5C: E0 09           CPX     #$09                
FC5E: F0 58           BEQ     $FCB8               ; {}
FC60: E0 05           CPX     #$05                
FC62: F0 54           BEQ     $FCB8               ; {}
FC64: E0 06           CPX     #$06                
FC66: F0 50           BEQ     $FCB8               ; {}
FC68: A4 F3           LDY     $F3                 ; {ram.mF3}
FC6A: 18              CLC                         
FC6B: F8              SED                         
FC6C: A5 BE           LDA     $BE                 ; {ram.mBE}
FC6E: 79 40 FF        ADC     $FF40,Y             ; {}
FC71: 85 BE           STA     $BE                 ; {ram.mBE}
FC73: B9 47 FF        LDA     $FF47,Y             ; {}
FC76: B0 02           BCS     $FC7A               ; {}
FC78: F0 3E           BEQ     $FCB8               ; {}
FC7A: 65 BD           ADC     $BD                 ; {ram.mBD}
FC7C: 85 BD           STA     $BD                 ; {ram.mBD}
FC7E: D8              CLD                         
FC7F: A8              TAY                         
FC80: A5 80           LDA     $80                 ; {ram.m80}
FC82: 29 06           AND     #$06                
FC84: F0 11           BEQ     $FC97               ; {}
FC86: C9 06           CMP     #$06                
FC88: F0 2E           BEQ     $FCB8               ; {}
FC8A: 6A              ROR     A                   
FC8B: 6A              ROR     A                   
FC8C: 98              TYA                         
FC8D: 29 1F           AND     #$1F                
FC8F: 90 02           BCC     $FC93               ; {}
FC91: 29 0F           AND     #$0F                
FC93: D0 23           BNE     $FCB8               ; {}
FC95: F0 09           BEQ     $FCA0               ; {}
FC97: 98              TYA                         
FC98: 29 0F           AND     #$0F                
FC9A: F0 04           BEQ     $FCA0               ; {}
FC9C: C9 05           CMP     #$05                
FC9E: D0 18           BNE     $FCB8               ; {}
FCA0: A5 BC           LDA     $BC                 ; {ram.mBC}
FCA2: 18              CLC                         
FCA3: 69 10           ADC     #$10                
FCA5: A8              TAY                         
FCA6: 29 F0           AND     #$F0                
FCA8: C9 A0           CMP     #$A0                
FCAA: F0 0C           BEQ     $FCB8               ; {}
FCAC: 84 BC           STY     $BC                 ; {ram.mBC}
FCAE: A5 C5           LDA     $C5                 ; {ram.mC5}
FCB0: 09 04           ORA     #$04                
FCB2: 85 C5           STA     $C5                 ; {ram.mC5}
FCB4: A9 7F           LDA     #$7F                
FCB6: 85 C4           STA     $C4                 ; {ram.mC4}
FCB8: D8              CLD                         
FCB9: 38              SEC                         
FCBA: 60              RTS                         
FCBB: 86 C2           STX     $C2                 ; {ram.mC2}
FCBD: 68              PLA                         
FCBE: 68              PLA                         
FCBF: 38              SEC                         
FCC0: 60              RTS                         
FCC1: AA              TAX                         
FCC2: 29 0F           AND     #$0F                
FCC4: A8              TAY                         
FCC5: 8A              TXA                         
FCC6: 4A              LSR     A                   
FCC7: 4A              LSR     A                   
FCC8: 4A              LSR     A                   
FCC9: 4A              LSR     A                   
FCCA: AA              TAX                         
FCCB: BD 0C FF        LDA     $FF0C,X             ; {}
FCCE: 18              CLC                         
FCCF: 79 1C FF        ADC     $FF1C,Y             ; {}
FCD2: 60              RTS                         
FCD3: A2 06           LDX     #$06                
FCD5: A5 C7           LDA     $C7                 ; {ram.mC7}
FCD7: 29 20           AND     #$20                
FCD9: F0 01           BEQ     $FCDC               ; {}
FCDB: CA              DEX                         
FCDC: 98              TYA                         
FCDD: 60              RTS                         
FCDE: 86 F4           STX     $F4                 ; {ram.mF4}
FCE0: B5 83           LDA     $83,X               ; {ram.m83}
FCE2: 10 07           BPL     $FCEB               ; {}
FCE4: C9 E0           CMP     #$E0                
FCE6: D0 03           BNE     $FCEB               ; {}
FCE8: A6 F5           LDX     $F5                 ; {ram.mF5}
FCEA: 60              RTS                         
FCEB: B5 A7           LDA     $A7,X               ; {ram.mA7}
FCED: A8              TAY                         
FCEE: 29 40           AND     #$40                
FCF0: D0 0E           BNE     $FD00               ; {}
FCF2: E8              INX                         
FCF3: 10 EB           BPL     $FCE0               ; {}
FCF5: 86 F6           STX     $F6                 ; {ram.mF6}
FCF7: 20 D8 FD        JSR     $FDD8               ; {}
FCFA: C6 F5           DEC     $F5                 ; {ram.mF5}
FCFC: A6 F6           LDX     $F6                 ; {ram.mF6}
FCFE: 10 E0           BPL     $FCE0               ; {}
FD00: B5 83           LDA     $83,X               ; {ram.m83}
FD02: 30 F1           BMI     $FCF5               ; {}
FD04: 98              TYA                         
FD05: 29 30           AND     #$30                
FD07: F0 0B           BEQ     $FD14               ; {}
FD09: C9 20           CMP     #$20                
FD0B: D0 03           BNE     $FD10               ; {}
FD0D: 4C B9 FD        JMP     $FDB9               ; {}
FD10: C9 30           CMP     #$30                
FD12: F0 E1           BEQ     $FCF5               ; {}
FD14: 20 D9 FA        JSR     $FAD9               ; {}
FD17: 29 8F           AND     #$8F                
FD19: 09 20           ORA     #$20                
FD1B: 95 A7           STA     $A7,X               ; {ram.mA7}
FD1D: B5 83           LDA     $83,X               ; {ram.m83}
FD1F: C9 53           CMP     #$53                
FD21: 90 0D           BCC     $FD30               ; {}
FD23: 20 6B FE        JSR     $FE6B               ; {}
FD26: B9 83 00        LDA     $0083,Y             ; {ram.m83}
FD29: 38              SEC                         
FD2A: E9 59           SBC     #$59                
FD2C: 95 83           STA     $83,X               ; {ram.m83}
FD2E: E6 F5           INC     $F5                 ; {ram.mF5}
FD30: 24 80           BIT     $80                 ; {ram.m80}
FD32: 30 BE           BMI     $FCF2               ; {}
FD34: 20 94 FE        JSR     $FE94               ; {}
FD37: B0 B9           BCS     $FCF2               ; {}
FD39: B5 83           LDA     $83,X               ; {ram.m83}
FD3B: 30 2F           BMI     $FD6C               ; {}
FD3D: C9 4F           CMP     #$4F                
FD3F: 90 2B           BCC     $FD6C               ; {}
FD41: 20 6B FE        JSR     $FE6B               ; {}
FD44: B5 A7           LDA     $A7,X               ; {ram.mA7}
FD46: 29 08           AND     #$08                
FD48: 85 F7           STA     $F7                 ; {ram.mF7}
FD4A: 20 D9 FA        JSR     $FAD9               ; {}
FD4D: 29 87           AND     #$87                
FD4F: 09 20           ORA     #$20                
FD51: 05 F7           ORA     $F7                 ; {ram.mF7}
FD53: 49 08           EOR     #$08                
FD55: 95 A7           STA     $A7,X               ; {ram.mA7}
FD57: B9 95 00        LDA     $0095,Y             ; {ram.m95}
FD5A: 95 95           STA     $95,X               ; {ram.m95}
FD5C: B9 83 00        LDA     $0083,Y             ; {ram.m83}
FD5F: 18              CLC                         
FD60: 69 0A           ADC     #$0A                
FD62: 38              SEC                         
FD63: E9 59           SBC     #$59                
FD65: 95 83           STA     $83,X               ; {ram.m83}
FD67: E6 F5           INC     $F5                 ; {ram.mF5}
FD69: 4C F2 FC        JMP     $FCF2               ; {}
FD6C: A5 F4           LDA     $F4                 ; {ram.mF4}
FD6E: 85 F7           STA     $F7                 ; {ram.mF7}
FD70: 86 F4           STX     $F4                 ; {ram.mF4}
FD72: A6 F5           LDX     $F5                 ; {ram.mF5}
FD74: 20 80 FE        JSR     $FE80               ; {}
FD77: A6 F4           LDX     $F4                 ; {ram.mF4}
FD79: E8              INX                         
FD7A: A5 F7           LDA     $F7                 ; {ram.mF7}
FD7C: 85 F4           STA     $F4                 ; {ram.mF4}
FD7E: E6 F5           INC     $F5                 ; {ram.mF5}
FD80: B5 A7           LDA     $A7,X               ; {ram.mA7}
FD82: 29 08           AND     #$08                
FD84: 85 F7           STA     $F7                 ; {ram.mF7}
FD86: 20 D9 FA        JSR     $FAD9               ; {}
FD89: 29 87           AND     #$87                
FD8B: 09 20           ORA     #$20                
FD8D: 05 F7           ORA     $F7                 ; {ram.mF7}
FD8F: 49 08           EOR     #$08                
FD91: 95 A7           STA     $A7,X               ; {ram.mA7}
FD93: B5 94           LDA     $94,X               ; {ram.m94}
FD95: 95 95           STA     $95,X               ; {ram.m95}
FD97: B5 82           LDA     $82,X               ; {ram.m82}
FD99: 18              CLC                         
FD9A: 69 0A           ADC     #$0A                
FD9C: C9 59           CMP     #$59                
FD9E: 95 83           STA     $83,X               ; {ram.m83}
FDA0: B0 07           BCS     $FDA9               ; {}
FDA2: C9 53           CMP     #$53                
FDA4: B0 03           BCS     $FDA9               ; {}
FDA6: 4C F2 FC        JMP     $FCF2               ; {}
FDA9: 20 6B FE        JSR     $FE6B               ; {}
FDAC: B9 83 00        LDA     $0083,Y             ; {ram.m83}
FDAF: 38              SEC                         
FDB0: E9 59           SBC     #$59                
FDB2: 95 83           STA     $83,X               ; {ram.m83}
FDB4: E6 F5           INC     $F5                 ; {ram.mF5}
FDB6: 4C F2 FC        JMP     $FCF2               ; {}
FDB9: 20 D9 FA        JSR     $FAD9               ; {}
FDBC: 29 8F           AND     #$8F                
FDBE: 09 30           ORA     #$30                
FDC0: 95 A7           STA     $A7,X               ; {ram.mA7}
FDC2: B5 83           LDA     $83,X               ; {ram.m83}
FDC4: C9 56           CMP     #$56                
FDC6: 90 0D           BCC     $FDD5               ; {}
FDC8: 20 6B FE        JSR     $FE6B               ; {}
FDCB: B9 83 00        LDA     $0083,Y             ; {ram.m83}
FDCE: 38              SEC                         
FDCF: E9 59           SBC     #$59                
FDD1: 95 83           STA     $83,X               ; {ram.m83}
FDD3: E6 F5           INC     $F5                 ; {ram.mF5}
FDD5: 4C F2 FC        JMP     $FCF2               ; {}
FDD8: B5 96           LDA     $96,X               ; {ram.m96}
FDDA: 95 95           STA     $95,X               ; {ram.m95}
FDDC: B5 A8           LDA     $A8,X               ; {ram.mA8}
FDDE: 95 A7           STA     $A7,X               ; {ram.mA7}
FDE0: B5 84           LDA     $84,X               ; {ram.m84}
FDE2: 95 83           STA     $83,X               ; {ram.m83}
FDE4: E8              INX                         
FDE5: C9 E0           CMP     #$E0                
FDE7: D0 EF           BNE     $FDD8               ; {}
FDE9: 60              RTS                         
FDEA: A9 00           LDA     #$00                
FDEC: 24 80           BIT     $80                 ; {ram.m80}
FDEE: 30 0C           BMI     $FDFC               ; {}
FDF0: A6 BD           LDX     $BD                 ; {ram.mBD}
FDF2: F0 08           BEQ     $FDFC               ; {}
FDF4: 09 40           ORA     #$40                
FDF6: E0 15           CPX     #$15                
FDF8: 90 02           BCC     $FDFC               ; {}
FDFA: 09 80           ORA     #$80                
FDFC: 85 F4           STA     $F4                 ; {ram.mF4}
FDFE: A2 00           LDX     #$00                
FE00: 20 0D FE        JSR     $FE0D               ; {}
FE03: 86 DC           STX     $DC                 ; {ram.mDC}
FE05: A2 09           LDX     #$09                
FE07: 20 0D FE        JSR     $FE0D               ; {}
FE0A: 86 DD           STX     $DD                 ; {ram.mDD}
FE0C: 60              RTS                         
FE0D: A9 01           LDA     #$01                
FE0F: 95 83           STA     $83,X               ; {ram.m83}
FE11: 20 94 FA        JSR     $FA94               ; {}
FE14: 95 95           STA     $95,X               ; {ram.m95}
FE16: 20 D9 FA        JSR     $FAD9               ; {}
FE19: 29 1F           AND     #$1F                
FE1B: 95 A7           STA     $A7,X               ; {ram.mA7}
FE1D: E8              INX                         
FE1E: 24 F4           BIT     $F4                 ; {ram.mF4}
FE20: 50 34           BVC     $FE56               ; {}
FE22: 30 08           BMI     $FE2C               ; {}
FE24: A9 15           LDA     #$15                
FE26: E0 09           CPX     #$09                
FE28: B0 19           BCS     $FE43               ; {}
FE2A: 90 15           BCC     $FE41               ; {}
FE2C: A9 15           LDA     #$15                
FE2E: 95 83           STA     $83,X               ; {ram.m83}
FE30: 20 D9 FA        JSR     $FAD9               ; {}
FE33: 29 E0           AND     #$E0                
FE35: 09 0A           ORA     #$0A                
FE37: 95 95           STA     $95,X               ; {ram.m95}
FE39: 20 D9 FA        JSR     $FAD9               ; {}
FE3C: 29 1F           AND     #$1F                
FE3E: 95 A7           STA     $A7,X               ; {ram.mA7}
FE40: E8              INX                         
FE41: A9 2A           LDA     #$2A                
FE43: 95 83           STA     $83,X               ; {ram.m83}
FE45: 20 D9 FA        JSR     $FAD9               ; {}
FE48: 29 E0           AND     #$E0                
FE4A: 09 0A           ORA     #$0A                
FE4C: 95 95           STA     $95,X               ; {ram.m95}
FE4E: 20 D9 FA        JSR     $FAD9               ; {}
FE51: 29 1F           AND     #$1F                
FE53: 95 A7           STA     $A7,X               ; {ram.mA7}
FE55: E8              INX                         
FE56: A9 3F           LDA     #$3F                
FE58: 95 83           STA     $83,X               ; {ram.m83}
FE5A: 20 94 FA        JSR     $FA94               ; {}
FE5D: 95 95           STA     $95,X               ; {ram.m95}
FE5F: 20 D9 FA        JSR     $FAD9               ; {}
FE62: 29 1F           AND     #$1F                
FE64: 95 A7           STA     $A7,X               ; {ram.mA7}
FE66: A9 E0           LDA     #$E0                
FE68: 95 84           STA     $84,X               ; {ram.m84}
FE6A: 60              RTS                         
FE6B: 86 F6           STX     $F6                 ; {ram.mF6}
FE6D: A6 F5           LDX     $F5                 ; {ram.mF5}
FE6F: 20 80 FE        JSR     $FE80               ; {}
FE72: A4 F6           LDY     $F6                 ; {ram.mF6}
FE74: C8              INY                         
FE75: B9 95 00        LDA     $0095,Y             ; {ram.m95}
FE78: 95 95           STA     $95,X               ; {ram.m95}
FE7A: B9 A7 00        LDA     $00A7,Y             ; {ram.mA7}
FE7D: 95 A7           STA     $A7,X               ; {ram.mA7}
FE7F: 60              RTS                         
FE80: E8              INX                         
FE81: B5 83           LDA     $83,X               ; {ram.m83}
FE83: 95 84           STA     $84,X               ; {ram.m84}
FE85: B5 95           LDA     $95,X               ; {ram.m95}
FE87: 95 96           STA     $96,X               ; {ram.m96}
FE89: B5 A7           LDA     $A7,X               ; {ram.mA7}
FE8B: 95 A8           STA     $A8,X               ; {ram.mA8}
FE8D: CA              DEX                         
FE8E: E4 F4           CPX     $F4                 ; {ram.mF4}
FE90: 10 EF           BPL     $FE81               ; {}
FE92: E8              INX                         
FE93: 60              RTS                         
FE94: A5 F5           LDA     $F5                 ; {ram.mF5}
FE96: C9 09           CMP     #$09                
FE98: B0 03           BCS     $FE9D               ; {}
FE9A: C9 06           CMP     #$06                
FE9C: 60              RTS                         
FE9D: C9 0F           CMP     #$0F                
FE9F: 60              RTS                         
FEA0: B5 83           LDA     $83,X               ; {ram.m83}
FEA2: A8              TAY                         
FEA3: C9 E0           CMP     #$E0                
FEA5: D0 01           BNE     $FEA8               ; {}
FEA7: 60              RTS                         
FEA8: B5 95           LDA     $95,X               ; {ram.m95}
FEAA: 29 0F           AND     #$0F                
FEAC: C9 0D           CMP     #$0D                
FEAE: F0 0B           BEQ     $FEBB               ; {}
FEB0: C9 0B           CMP     #$0B                
FEB2: F0 15           BEQ     $FEC9               ; {}
FEB4: C9 02           CMP     #$02                
FEB6: F0 11           BEQ     $FEC9               ; {}
FEB8: E8              INX                         
FEB9: 10 E5           BPL     $FEA0               ; {}
FEBB: 98              TYA                         
FEBC: 30 FA           BMI     $FEB8               ; {}
FEBE: C9 08           CMP     #$08                
FEC0: 90 F6           BCC     $FEB8               ; {}
FEC2: C9 40           CMP     #$40                
FEC4: B0 F2           BCS     $FEB8               ; {}
FEC6: C9 00           CMP     #$00                
FEC8: 60              RTS                         
FEC9: 98              TYA                         
FECA: C9 18           CMP     #$18                
FECC: 90 EA           BCC     $FEB8               ; {}
FECE: C9 38           CMP     #$38                
FED0: B0 E6           BCS     $FEB8               ; {}
FED2: C9 00           CMP     #$00                
FED4: 60              RTS                         
FED5: 60              RTS                         
FED6: 70 70           BVS     $FF48               ; {}
FED8: B0 90           BCS     $FE6A               ; {}
FEDA: B0 70           BCS     $FF4C               ; {}
FEDC: 70 80           BVS     $FE5E               ; {}
FEDE: 80                 
FEDF: 80                 
FEE0: 80                 
FEE1: 80                 
FEE2: 80                 
FEE3: 80                 
FEE4: 40              RTI                         
FEE5: 80                 
FEE6: 80                 
FEE7: 40              RTI                         
FEE8: 00              BRK                         
FEE9: 80                 
FEEA: 80                 
FEEB: 40              RTI                         
FEEC: 00              BRK                         
FEED: 64                 
FEEE: 00              BRK                         
FEEF: 66 67         ;ROR   $67                 ;
FEF1: 68              PLA                         
FEF2: 69 6A           ADC     #$6A                
FEF4: 6B                 
FEF5: 63                 
FEF6: 6D 00 32      ;ADC   $3200               ;
FEF9: 8A              TXA                         
FEFA: 82                 
FEFB: A3                 
FEFC: 84 85           STY     $85                 ; {ram.m85}
FEFE: 86 87           STX     $87                 ; {ram.m87}
FF00: 88              DEY                         
FF01: 89                 
FF02: 00              BRK                         
FF03: 8B                 
FF04: 06 04           ASL     $04                 ; {hard.CXM0FB}
FF06: 05 06           ORA     $06                 ; {hard.CXBLPF}
FF08: 07                 
FF09: 09 07           ORA     #$07                
FF0B: 05 06           ORA     $06                 ; {hard.CXBLPF}
FF0D: 05 04           ORA     $04                 ; {hard.CXM0FB}
FF0F: 03                 
FF10: 02                 
FF11: 01 00           ORA     ($00,X)             ; {hard.CXM0P}
FF13: 00              BRK                         
FF14: 0E 0D 0C      ;ASL   $0C0D               ;
FF17: 0B                 
FF18: 0A              ASL     A                   
FF19: 09 08           ORA     #$08                
FF1B: 07                 
FF1C: 00              BRK                         
FF1D: 00              BRK                         
FF1E: 55 00           EOR     $00,X               ; {hard.CXM0P}
FF20: 64                 
FF21: 0D 73 1C      ;ORA   $1C73               ;
FF24: 82                 
FF25: 2B                 
FF26: 91 3A           STA     ($3A),Y             
FF28: 00              BRK                         
FF29: 49 0E           EOR     #$0E                
FF2B: 0E 06 03      ;ASL   $0306               ;
FF2E: 04                 
FF2F: 04                 
FF30: 06 02           ASL     $02                 ; {hard.CXP0FB}
FF32: 02                 
FF33: 02                 
FF34: 24 0F           BIT     $0F                 ; 
FF36: 0F                 
FF37: 07                 
FF38: 03                 
FF39: 04                 
FF3A: 04                 
FF3B: 06 02           ASL     $02                 ; {hard.CXP0FB}
FF3D: 02                 
FF3E: 02                 
FF3F: 24 02           BIT     $02                 ; {hard.CXP0FB}
FF41: 02                 
FF42: 05 10           ORA     $10                 ; 
FF44: 00              BRK                         
FF45: 00              BRK                         
FF46: 20 00 00        JSR     $0000               ; {hard.CXM0P}
FF49: 00              BRK                         
FF4A: 00              BRK                         
FF4B: 00              BRK                         
FF4C: 01 00           ORA     ($00,X)             ; {hard.CXM0P}
FF4E: F1 F1           SBC     ($F1),Y             ; {ram.mF1}
FF50: F9 FC 4B        SBC     $4BFC,Y             
FF53: 4B                 
FF54: 53                 
FF55: 56 60           LSR     $60,X               
FF57: C1 80           CMP     ($80,X)             ; {ram.m80}
FF59: E1 C0           SBC     ($C0,X)             ; {ram.mC0}
FF5B: 60              RTS                         
FF5C: E0 40           CPX     #$40                
FF5E: 81 8B           STA     ($8B,X)             ; {ram.m8B}
FF60: A6 CF           LDX     $CF                 ; {ram.mCF}
FF62: 00              BRK                         
FF63: 31 5A           AND     ($5A),Y             
FF65: 75 7F           ADC     $7F,X               
FF67: 75 5A           ADC     $5A,X               
FF69: 31 00           AND     ($00),Y             ; {hard.CXM0P}
FF6B: CF                 
FF6C: A6 8B           LDX     $8B                 ; {ram.m8B}
FF6E: FC                 
FF6F: FD FD FF        SBC     $FFFD,X             ; {}
FF72: 00              BRK                         
FF73: 01 03           ORA     ($03,X)             ; {hard.CXP1FB}
FF75: 03                 
FF76: 04                 
FF77: 03                 
FF78: 03                 
FF79: 01 00           ORA     ($00,X)             ; {hard.CXM0P}
FF7B: FF                 
FF7C: FD FD 00        SBC     $00FD,X             ; {ram.mFD}
FF7F: 01 03           ORA     ($03,X)             ; {hard.CXP1FB}
FF81: 03                 
FF82: 04                 
FF83: 03                 
FF84: 03                 
FF85: 01 00           ORA     ($00,X)             ; {hard.CXM0P}
FF87: FF                 
FF88: FD FD FC        SBC     $FCFD,X             ; {}
FF8B: FD FD FF        SBC     $FFFD,X             ; {}

FF8E: A9 3C           LDA     #$3C                
FF90: 85 F7           STA     $F7                 ; {ram.mF7}
FF92: A9 D4           LDA     #$D4                
FF94: 85 F8           STA     $F8                 ; {ram.mF8}
FF96: 4C F0 FF        JMP     $FFF0               ; {code.SwitchToBank0} Bank switch to D43C


FF99: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  
FFA9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
FFB9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFC9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFD9: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFE9: 00 00 00 00 00 00 00    
```

# Switch to Bank 0

```code
SwitchToBank0:
; The destination address after the bank switch is in F7.
FFF0: 8D F8 FF        STA     $FFF8               ; {} Switch to bank 1 (goto DFF3)
FFF3: 6C F7 00        JMP     ($00F7)             ; {ram.mF7} Here after DFF0. Goto target address.
;
FFF6: 00 00 00 00 ; Padding   
```

# Vectors (Bank 1)

```code
Vectors1:
FFFA: DA F9       ; NMI vector to F9DA
FFFC: DA F9       ; Resset vector to F9DA
FFFE: DA F9       ; IRQ/BRK vector to F9DA
```

