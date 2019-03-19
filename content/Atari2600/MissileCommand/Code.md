![Missile Command](A2600MissileCommand.jpg)

# Missile Command

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

; 86 P0
; 87 P1 
; 88 M0 ?? Positions of the five objects F016 below
; 89 M1
; 90 Ball (cursor)

; A1 !0 position-rountine only does object number X

F000: 4C 3F F0      JMP   $F03F       ;{Init}
        
F003: A2 04         LDX   #$04                ; Count to -1 ... FIVE objects

F005: A9 02         LDA   #$02                
F007: E0 02         CPX   #$02                ; 
F009: B0 0A         BCS   $F015               ;
F00B: A9 01         LDA   #$01                
F00D: A4 A1         LDY   $A1                 ;
F00F: C0 F0         CPY   #$F0                
F011: D0 02         BNE   $F015               ;
F013: A9 FC         LDA   #$FC                
F015: 18            CLC                       
F016: 75 86         ADC   $86,X               
F018: A0 02         LDY   #$02                
F01A: 38            SEC                       
F01B: C8            INY                       
F01C: E9 0F         SBC   #$0F                
F01E: B0 FB         BCS   $F01B               ;
F020: 49 FF         EOR   #$FF                
F022: E9 06         SBC   #$06                
F024: 0A            ASL   A                   
F025: 0A            ASL   A                   
F026: 0A            ASL   A                   
F027: 0A            ASL   A                   
F028: 85 02         STA   $02                 ;{-2_WSYNC} Wait for end of line ;*WSYNC:lots 
F02A: 88            DEY                       ; Delay ...
F02B: 10 FD         BPL   $F02A               ; ... in Y
F02D: 95 10         STA   $10,X               ; RESx (M0, BL, M1, P0, P1) ;* RESM0:lots RESBL:lots RESM1:lots RESP0:lots RESP1:lots 
F02F: 95 20         STA   $20,X               ; HMMx (M0, BL, M1, P0, P1) ;* HMP0:lots HMP1:lots HMM1:lots HMBL:lots HMM0:lots 
F031: A5 A1         LDA   $A1                 ; Only moving one object?
F033: D0 03         BNE   $F038               ; Yes ... skip the other objects
F035: CA            DEX                       ; Do all ...
F036: 10 CD         BPL   $F005               ; ... 5 objects
F038: 85 02         STA   $02                 ;{-2_WSYNC} Wait a line ;*WSYNC:lots 
F03A: 85 2A         STA   $2A                 ;{-2_HMOVE} Move all the object ;*HMOVE:lots 
F03C: 85 02         STA   $02                 ;{-2_WSYNC} Wait another line ;*WSYNC:lots 
F03E: 60            RTS                       ; Done

# Init

Init:
F03F: 78            SEI                       ; Disable interrupts
F040: D8            CLD                       ; Binary mode (not BCD)
F041: A2 00         LDX   #$00                ; All port A pins ...
F043: 8E 81 02      STX   $0281               ;{-2_SWACNT} ... are inputs ;*SWACNT:1 
F046: 8A            TXA                       ; Clear ...
F047: 95 00         STA   $00,X               ; ... all ...  
F049: E8            INX                       ; ... TIA ...
F04A: D0 FB         BNE   $F047               ; ... registers and RAM
F04C: CA            DEX                       ; FF
F04D: 9A            TXS                       ; Stack pointer to FF (top of ram)
F04E: A9 87         LDA   #$87                
F050: 85 DB         STA   $DB                 ; ?? TODO ram usage report
F052: A9 01         LDA   #$01                
F054: 85 E9         STA   $E9                 ;

# VBLANK

; VBLANK begins
F056: A9 02         LDA   #$02                ; Start ...
F058: 85 01         STA   $01                 ;{-2_VBLANK} ... the VBLANK    ;VBLANK:32,263
F05A: 85 00         STA   $00                 ;{-2_VSYNC} And VSYNC         ;VSYNC:32,263
F05C: 85 02         STA   $02                 ;{-2_WSYNC} Hold VSYNC ...    ;WSYNC:1
F05E: 85 02         STA   $02                 ;{-2_WSYNC} ... for three ... ;WSYNC:2
F060: 85 02         STA   $02                 ;{-2_WSYNC} ... scanlines     ;WSYNC:3
F062: A9 00         LDA   #$00                ; Turn off ...
F064: 85 00         STA   $00                 ;{-2_VSYNC} ... VSYNC         ;VSYNC:4
F066: A9 30         LDA   #$30                ; Set timer to 48*64 = 3072 machine ...
F068: 8D 96 02      STA   $0296               ;{-2_TIM64T} ... cycles 3072/(228/3) = 40 scanlines ;TIM64T:4
F06B: E6 80         INC   $80                 ;
F06D: D0 10         BNE   $F07F               ;
F06F: E6 E8         INC   $E8                 ;
F071: A5 DB         LDA   $DB                 ;
F073: 10 0A         BPL   $F07F               ;
F075: A5 F8         LDA   $F8                 ;
F077: 10 06         BPL   $F07F               ;
F079: A5 F5         LDA   $F5                 ;
F07B: 49 01         EOR   #$01                
F07D: 85 F5         STA   $F5                 ;
F07F: A5 DC         LDA   $DC                 ;
F081: F0 07         BEQ   $F08A               ;
F083: C6 DC         DEC   $DC                 ;
F085: D0 03         BNE   $F08A               ;
F087: 20 AF FC      JSR   $FCAF               ;
F08A: 24 DB         BIT   $DB                 ;
F08C: 10 04         BPL   $F092               ;
F08E: A9 FF         LDA   #$FF                
F090: 85 DE         STA   $DE                 ;
F092: A5 DE         LDA   $DE                 ;
F094: C9 E8         CMP   #$E8                
F096: D0 2D         BNE   $F0C5               ;
F098: A5 E0         LDA   $E0                 ;
F09A: D0 1C         BNE   $F0B8               ;
F09C: A9 07         LDA   #$07                
F09E: 85 E0         STA   $E0                 ;
F0A0: A5 DD         LDA   $DD                 ;
F0A2: D0 07         BNE   $F0AB               ;
F0A4: 20 AF FC      JSR   $FCAF               ;
F0A7: A5 DD         LDA   $DD                 ;
F0A9: F0 10         BEQ   $F0BB               ;
F0AB: A9 04         LDA   #$04                
F0AD: 85 DF         STA   $DF                 ;
F0AF: C6 DD         DEC   $DD                 ;
F0B1: A9 05         LDA   #$05                
F0B3: A0 00         LDY   #$00                
F0B5: 20 CB FC      JSR   $FCCB               ;
F0B8: 4C 32 F1      JMP   $F132               ;
F0BB: A9 E0         LDA   #$E0                
F0BD: 85 DE         STA   $DE                 ;
F0BF: A9 00         LDA   #$00                
F0C1: 85 DF         STA   $DF                 ;
F0C3: 85 E0         STA   $E0                 ;
F0C5: A5 DE         LDA   $DE                 ;
F0C7: C9 E0         CMP   #$E0                
F0C9: D0 41         BNE   $F10C               ;
F0CB: A5 80         LDA   $80                 ;
F0CD: 29 0F         AND   #$0F                
F0CF: D0 61         BNE   $F132               ;
F0D1: A6 E0         LDX   $E0                 ;
F0D3: E0 06         CPX   #$06                
F0D5: F0 23         BEQ   $F0FA               ;
F0D7: BC 18 FE      LDY   $FE18,X             
F0DA: B9 A9 00      LDA   $00A9,Y             
F0DD: C9 38         CMP   #$38                
F0DF: F0 03         BEQ   $F0E4               ;
F0E1: E8            INX                       
F0E2: D0 EF         BNE   $F0D3               ;
F0E4: AD 79 FF      LDA   $FF79               ;
F0E7: 99 A9 00      STA   $00A9,Y             
F0EA: E8            INX                       
F0EB: 86 E0         STX   $E0                 ;
F0ED: A9 00         LDA   #$00                
F0EF: A0 01         LDY   #$01                
F0F1: 20 CB FC      JSR   $FCCB               ;
F0F4: A9 05         LDA   #$05                
F0F6: 85 DF         STA   $DF                 ;
F0F8: D0 38         BNE   $F132               ;
F0FA: A9 A8         LDA   #$A8                
F0FC: 85 DE         STA   $DE                 ;
F0FE: A9 04         LDA   #$04                
F100: 85 E0         STA   $E0                 ;
F102: A9 01         LDA   #$01                
F104: 85 DF         STA   $DF                 ;
F106: 20 96 FD      JSR   $FD96               ;
F109: 4C D6 F4      JMP   $F4D6               ;
F10C: A5 DF         LDA   $DF                 ;
F10E: C9 06         CMP   #$06                
F110: F0 20         BEQ   $F132               ;
F112: 24 DE         BIT   $DE                 ;
F114: 10 1C         BPL   $F132               ;
F116: A5 80         LDA   $80                 ;
F118: 29 03         AND   #$03                
F11A: D0 16         BNE   $F132               ;
F11C: C6 DE         DEC   $DE                 ;
F11E: 30 03         BMI   $F123               ;
F120: 4C D8 F1      JMP   $F1D8               ;
F123: A5 DE         LDA   $DE                 ;
F125: C9 A0         CMP   #$A0                
F127: D0 09         BNE   $F132               ;
F129: A9 32         LDA   #$32                
F12B: 85 90         STA   $90                 ;
F12D: 85 8E         STA   $8E                 ;
F12F: 20 16 FD      JSR   $FD16               ;
F132: 24 DB         BIT   $DB                 ;
F134: 50 11         BVC   $F147               ;
F136: AD 82 02      LDA   $0282               ;{-2_SWCHB}SWCHB:5,4,6 
F139: 29 03         AND   #$03                
F13B: F0 03         BEQ   $F140               ;
F13D: 4A            LSR   A                   
F13E: 90 03         BCC   $F143               ;
F140: 4C 10 F2      JMP   $F210               ;
F143: A9 00         LDA   #$00                
F145: 85 DB         STA   $DB                 ;
F147: A9 38         LDA   #$38                
F149: A0 FF         LDY   #$FF                
F14B: A2 0A         LDX   #$0A                
F14D: 95 A9         STA   $A9,X               
F14F: 94 AA         STY   $AA,X               
F151: 94 CC         STY   $CC,X               
F153: CA            DEX                       
F154: CA            DEX                       
F155: 10 F6         BPL   $F14D               ;
F157: C8            INY                       
F158: A2 05         LDX   #$05                
F15A: 94 EF         STY   $EF,X               
F15C: CA            DEX                       
F15D: 10 FB         BPL   $F15A               ;
F15F: 84 ED         STY   $ED                 ;
F161: 84 F5         STY   $F5                 ;
F163: 84 FB         STY   $FB                 ;
F165: 84 F6         STY   $F6                 ;
F167: 84 F7         STY   $F7                 ;
F169: A4 E9         LDY   $E9                 ;
F16B: B9 94 FE      LDA   $FE94,Y             
F16E: A2 3F         LDX   #$3F                
F170: 86 EC         STX   $EC                 ;
F172: C0 18         CPY   #$18                
F174: 90 12         BCC   $F188               ;
F176: 98            TYA                       
F177: F8            SED                       
F178: 38            SEC                       
F179: E9 17         SBC   #$17                
F17B: A8            TAY                       
F17C: D8            CLD                       
F17D: B9 94 FE      LDA   $FE94,Y             
F180: 86 ED         STX   $ED                 ;
F182: 09 80         ORA   #$80                
F184: A2 01         LDX   #$01                
F186: 86 F5         STX   $F5                 ;
F188: 85 F8         STA   $F8                 ;
F18A: C0 17         CPY   #$17                
F18C: D0 04         BNE   $F192               ;
F18E: A0 40         LDY   #$40                
F190: 84 FB         STY   $FB                 ;
F192: 29 0E         AND   #$0E                
F194: AA            TAX                       
F195: CA            DEX                       
F196: 86 E7         STX   $E7                 ;
F198: A9 54         LDA   #$54                
F19A: 85 93         STA   $93                 ;
F19C: 85 94         STA   $94                 ;
F19E: A5 DB         LDA   $DB                 ;
F1A0: 09 40         ORA   #$40                
F1A2: 85 DB         STA   $DB                 ;
F1A4: 24 DB         BIT   $DB                 ;
F1A6: 30 2D         BMI   $F1D5               ;
F1A8: A9 32         LDA   #$32                
F1AA: 85 8E         STA   $8E                 ;
F1AC: 85 90         STA   $90                 ;
F1AE: A2 01         LDX   #$01                
F1B0: 86 DF         STX   $DF                 ;
F1B2: A2 04         LDX   #$04                
F1B4: 86 E0         STX   $E0                 ;
F1B6: A9 13         LDA   #$13                
F1B8: 24 FB         BIT   $FB                 ;
F1BA: 50 02         BVC   $F1BE               ;
F1BC: A9 FB         LDA   #$FB                
F1BE: A4 E7         LDY   $E7                 ;
F1C0: C8            INY                       
F1C1: 18            CLC                       
F1C2: 69 0D         ADC   #$0D                
F1C4: 88            DEY                       
F1C5: 10 FA         BPL   $F1C1               ;
F1C7: 85 9B         STA   $9B                 ;
F1C9: A9 B0         LDA   #$B0                
F1CB: 85 DE         STA   $DE                 ;
F1CD: A5 80         LDA   $80                 ;
F1CF: 09 02         ORA   #$02                
F1D1: 85 D8         STA   $D8                 ;
F1D3: 85 D9         STA   $D9                 ;
F1D5: 4C 10 F2      JMP   $F210               ;
F1D8: A0 0F         LDY   #$0F                
F1DA: A5 E7         LDA   $E7                 ;
F1DC: C9 10         CMP   #$10                
F1DE: B0 01         BCS   $F1E1               ;
F1E0: A8            TAY                       
F1E1: B9 6C FE      LDA   $FE6C,Y             
F1E4: 24 FB         BIT   $FB                 ;
F1E6: 50 01         BVC   $F1E9               ;
F1E8: 4A            LSR   A                   
F1E9: 85 DE         STA   $DE                 ;
F1EB: B9 7E FE      LDA   $FE7E,Y             
F1EE: 85 EB         STA   $EB                 ;
F1F0: A9 0A         LDA   #$0A                
F1F2: 85 DD         STA   $DD                 ;
F1F4: A9 4F         LDA   #$4F                
F1F6: A0 01         LDY   #$01                
F1F8: A2 02         LDX   #$02                
F1FA: 95 C4         STA   $C4,X               
F1FC: 94 C7         STY   $C7,X               
F1FE: 94 B5         STY   $B5,X               
F200: D6 B5         DEC   $B5,X               
F202: CA            DEX                       
F203: 10 F5         BPL   $F1FA               ;
F205: 86 91         STX   $91                 ;
F207: 86 92         STX   $92                 ;
F209: E8            INX                       
F20A: 86 DF         STX   $DF                 ;
F20C: A9 40         LDA   #$40                
F20E: 85 DB         STA   $DB                 ;
F210: A0 1F         LDY   #$1F                
F212: AD 82 02      LDA   $0282               ;{-2_SWCHB}SWCHB:8,5,6 
F215: 29 03         AND   #$03                
F217: D0 02         BNE   $F21B               ;
F219: A0 07         LDY   #$07                
F21B: 84 DA         STY   $DA                 ;
F21D: AD 82 02      LDA   $0282               ;{-2_SWCHB}SWCHB:8,5,6 
F220: 4A            LSR   A                   
F221: 4A            LSR   A                   
F222: A9 FF         LDA   #$FF                
F224: 90 04         BCC   $F22A               ;
F226: 85 EA         STA   $EA                 ;
F228: D0 2D         BNE   $F257               ;
F22A: 85 DB         STA   $DB                 ;
F22C: A5 EA         LDA   $EA                 ;
F22E: 30 06         BMI   $F236               ;
F230: 45 80         EOR   $80                 ;
F232: 25 DA         AND   $DA                 ;
F234: D0 21         BNE   $F257               ;
F236: A5 80         LDA   $80                 ;
F238: 25 DA         AND   $DA                 ;
F23A: 85 EA         STA   $EA                 ;
F23C: F8            SED                       
F23D: 18            CLC                       
F23E: A5 E9         LDA   $E9                 ;
F240: 69 01         ADC   #$01                
F242: C9 35         CMP   #$35                
F244: D0 02         BNE   $F248               ;
F246: A9 01         LDA   #$01                
F248: 85 E9         STA   $E9                 ;
F24A: D8            CLD                       
F24B: A9 00         LDA   #$00                
F24D: 85 DF         STA   $DF                 ;
F24F: 85 E8         STA   $E8                 ;
F251: 85 E7         STA   $E7                 ;
F253: 85 8E         STA   $8E                 ;
F255: 85 90         STA   $90                 ;
F257: 24 FB         BIT   $FB                 ;
F259: 10 03         BPL   $F25E               ;
F25B: 4C D6 F4      JMP   $F4D6               ;
F25E: 20 92 FC      JSR   $FC92               ;
F261: A6 F5         LDX   $F5                 ;
F263: B5 3C         LDA   $3C,X               ;INPT4:9,6,7 
F265: 10 09         BPL   $F270               ;
F267: A5 A2         LDA   $A2                 ;
F269: 29 F7         AND   #$F7                
F26B: 85 A2         STA   $A2                 ;
F26D: 4C ED F2      JMP   $F2ED               ;
F270: A5 A2         LDA   $A2                 ;
F272: 29 08         AND   #$08                
F274: D0 77         BNE   $F2ED               ;
F276: A2 02         LDX   #$02                
F278: B5 B5         LDA   $B5,X               
F27A: 10 13         BPL   $F28F               ;
F27C: CA            DEX                       
F27D: 10 F9         BPL   $F278               ;
F27F: A5 DF         LDA   $DF                 ;
F281: 29 0F         AND   #$0F                
F283: D0 68         BNE   $F2ED               ;
F285: 85 E0         STA   $E0                 ;
F287: A5 DF         LDA   $DF                 ;
F289: 09 02         ORA   #$02                
F28B: 85 DF         STA   $DF                 ;
F28D: D0 5E         BNE   $F2ED               ;
F28F: A9 08         LDA   #$08                
F291: 05 A2         ORA   $A2                 ;
F293: 85 A2         STA   $A2                 ;
F295: A5 DE         LDA   $DE                 ;
F297: 30 54         BMI   $F2ED               ;
F299: A5 DD         LDA   $DD                 ;
F29B: F0 E2         BEQ   $F27F               ;
F29D: C6 DD         DEC   $DD                 ;
F29F: D0 03         BNE   $F2A4               ;
F2A1: 20 AF FC      JSR   $FCAF               ;
F2A4: A5 DF         LDA   $DF                 ;
F2A6: C9 20         CMP   #$20                
F2A8: B0 0A         BCS   $F2B4               ;
F2AA: 29 0F         AND   #$0F                
F2AC: 09 10         ORA   #$10                
F2AE: 85 DF         STA   $DF                 ;
F2B0: A9 0A         LDA   #$0A                
F2B2: 85 E1         STA   $E1                 ;
F2B4: A9 4F         LDA   #$4F                
F2B6: 38            SEC                       
F2B7: E5 90         SBC   $90                 ;
F2B9: B0 06         BCS   $F2C1               ;
F2BB: F6 C4         INC   $C4,X               
F2BD: 49 FF         EOR   #$FF                
F2BF: 69 01         ADC   #$01                
F2C1: 85 82         STA   $82                 ;
F2C3: A5 8E         LDA   $8E                 ;
F2C5: 38            SEC                       
F2C6: E9 01         SBC   #$01                
F2C8: C5 82         CMP   $82                 ;
F2CA: 90 09         BCC   $F2D5               ;
F2CC: 85 83         STA   $83                 ;
F2CE: A9 C0         LDA   #$C0                
F2D0: 95 B5         STA   $B5,X               
F2D2: 4C DF F2      JMP   $F2DF               ;
F2D5: A4 82         LDY   $82                 ;
F2D7: 85 82         STA   $82                 ;
F2D9: 84 83         STY   $83                 ;
F2DB: A9 80         LDA   #$80                
F2DD: 95 B5         STA   $B5,X               
F2DF: A5 83         LDA   $83                 ;
F2E1: 95 B8         STA   $B8,X               
F2E3: 95 BB         STA   $BB,X               
F2E5: A5 82         LDA   $82                 ;
F2E7: 95 BE         STA   $BE,X               
F2E9: A9 00         LDA   #$00                
F2EB: 95 C1         STA   $C1,X               
F2ED: AD 82 02      LDA   $0282               ;{-2_SWCHB}SWCHB:9,6,7,8 
F2F0: 0A            ASL   A                   
F2F1: A6 F5         LDX   $F5                 ;
F2F3: D0 01         BNE   $F2F6               ;
F2F5: 0A            ASL   A                   
F2F6: A0 02         LDY   #$02                
F2F8: 90 01         BCC   $F2FB               ;
F2FA: 88            DEY                       
F2FB: 84 DA         STY   $DA                 ;
F2FD: A2 02         LDX   #$02                
F2FF: B5 B5         LDA   $B5,X               
F301: 30 03         BMI   $F306               ;
F303: 4C 89 F3      JMP   $F389               ;
F306: 29 20         AND   #$20                
F308: D0 F9         BNE   $F303               ;
F30A: B5 C1         LDA   $C1,X               
F30C: 18            CLC                       
F30D: 75 BE         ADC   $BE,X               
F30F: 95 C1         STA   $C1,X               
F311: D5 BB         CMP   $BB,X               
F313: 90 2B         BCC   $F340               ;
F315: F5 BB         SBC   $BB,X               
F317: 95 C1         STA   $C1,X               
F319: B5 B5         LDA   $B5,X               
F31B: 29 40         AND   #$40                
F31D: D0 0A         BNE   $F329               ;
F31F: B5 C7         LDA   $C7,X               
F321: 18            CLC                       
F322: 65 DA         ADC   $DA                 ;
F324: 95 C7         STA   $C7,X               
F326: 4C 40 F3      JMP   $F340               ;
F329: A9 4F         LDA   #$4F                
F32B: D5 C4         CMP   $C4,X               
F32D: B0 0A         BCS   $F339               ;
F32F: B5 C4         LDA   $C4,X               
F331: 18            CLC                       
F332: 65 DA         ADC   $DA                 ;
F334: 95 C4         STA   $C4,X               
F336: 4C 40 F3      JMP   $F340               ;
F339: B5 C4         LDA   $C4,X               
F33B: 38            SEC                       
F33C: E5 DA         SBC   $DA                 ;
F33E: 95 C4         STA   $C4,X               
F340: B5 B5         LDA   $B5,X               
F342: 29 40         AND   #$40                
F344: F0 0A         BEQ   $F350               ;
F346: B5 C7         LDA   $C7,X               
F348: 18            CLC                       
F349: 65 DA         ADC   $DA                 ;
F34B: 95 C7         STA   $C7,X               
F34D: 4C 67 F3      JMP   $F367               ;
F350: A9 4F         LDA   #$4F                
F352: D5 C4         CMP   $C4,X               
F354: B0 0A         BCS   $F360               ;
F356: B5 C4         LDA   $C4,X               
F358: 18            CLC                       
F359: 65 DA         ADC   $DA                 ;
F35B: 95 C4         STA   $C4,X               
F35D: 4C 67 F3      JMP   $F367               ;
F360: B5 C4         LDA   $C4,X               
F362: 38            SEC                       
F363: E5 DA         SBC   $DA                 ;
F365: 95 C4         STA   $C4,X               
F367: B5 B8         LDA   $B8,X               
F369: 38            SEC                       
F36A: E5 DA         SBC   $DA                 ;
F36C: 95 B8         STA   $B8,X               
F36E: 90 02         BCC   $F372               ;
F370: D0 17         BNE   $F389               ;
F372: A9 20         LDA   #$20                
F374: 15 B5         ORA   $B5,X               
F376: 95 B5         STA   $B5,X               
F378: A0 00         LDY   #$00                
F37A: 94 9E         STY   $9E,X               
F37C: B5 C4         LDA   $C4,X               
F37E: 38            SEC                       
F37F: E9 04         SBC   #$04                
F381: 95 A6         STA   $A6,X               
F383: B5 C7         LDA   $C7,X               
F385: E9 04         SBC   #$04                
F387: 95 A3         STA   $A3,X               
F389: CA            DEX                       
F38A: 30 03         BMI   $F38F               ;
F38C: 4C FF F2      JMP   $F2FF               ;
F38F: A6 CA         LDX   $CA                 ;
F391: A0 54         LDY   #$54                
F393: B5 C4         LDA   $C4,X               
F395: 85 89         STA   $89                 ;
F397: B5 B5         LDA   $B5,X               
F399: 29 20         AND   #$20                
F39B: D0 02         BNE   $F39F               ;
F39D: B4 C7         LDY   $C7,X               
F39F: 84 84         STY   $84                 ;
F3A1: A5 DE         LDA   $DE                 ;
F3A3: 10 07         BPL   $F3AC               ;
F3A5: C9 A0         CMP   #$A0                
F3A7: 90 03         BCC   $F3AC               ;
F3A9: 4C 31 F4      JMP   $F431               ;
F3AC: AD 80 02      LDA   $0280               ;{-2_SWCHA}SWCHA:lots 
F3AF: A4 F5         LDY   $F5                 ;
F3B1: F0 05         BEQ   $F3B8               ;
F3B3: 88            DEY                       
F3B4: 0A            ASL   A                   
F3B5: 0A            ASL   A                   
F3B6: 0A            ASL   A                   
F3B7: 0A            ASL   A                   
F3B8: 85 DA         STA   $DA                 ;
F3BA: 24 FB         BIT   $FB                 ;
F3BC: 50 04         BVC   $F3C2               ;
F3BE: A0 04         LDY   #$04                
F3C0: D0 07         BNE   $F3C9               ;
F3C2: A5 F8         LDA   $F8                 ;
F3C4: 4A            LSR   A                   
F3C5: 90 02         BCC   $F3C9               ;
F3C7: A0 02         LDY   #$02                
F3C9: A5 8F         LDA   $8F                 ;
F3CB: 26 DA         ROL   $DA                 ;
F3CD: B0 0C         BCS   $F3DB               ;
F3CF: 79 AB FE      ADC   $FEAB,Y             
F3D2: 85 8F         STA   $8F                 ;
F3D4: A5 90         LDA   $90                 ;
F3D6: 79 AC FE      ADC   $FEAC,Y             
F3D9: 85 90         STA   $90                 ;
F3DB: 26 DA         ROL   $DA                 ;
F3DD: B0 0F         BCS   $F3EE               ;
F3DF: 38            SEC                       
F3E0: A5 8F         LDA   $8F                 ;
F3E2: F9 AB FE      SBC   $FEAB,Y             
F3E5: 85 8F         STA   $8F                 ;
F3E7: A5 90         LDA   $90                 ;
F3E9: F9 AC FE      SBC   $FEAC,Y             
F3EC: 85 90         STA   $90                 ;
F3EE: A5 8D         LDA   $8D                 ;
F3F0: 26 DA         ROL   $DA                 ;
F3F2: B0 0D         BCS   $F401               ;
F3F4: 38            SEC                       
F3F5: F9 AB FE      SBC   $FEAB,Y             
F3F8: 85 8D         STA   $8D                 ;
F3FA: A5 8E         LDA   $8E                 ;
F3FC: F9 AC FE      SBC   $FEAC,Y             
F3FF: 85 8E         STA   $8E                 ;
F401: 26 DA         ROL   $DA                 ;
F403: B0 0C         BCS   $F411               ;
F405: 79 AB FE      ADC   $FEAB,Y             
F408: 85 8D         STA   $8D                 ;
F40A: A5 8E         LDA   $8E                 ;
F40C: 79 AC FE      ADC   $FEAC,Y             
F40F: 85 8E         STA   $8E                 ;
F411: A0 97         LDY   #$97                
F413: C4 90         CPY   $90                 ;
F415: B0 02         BCS   $F419               ;
F417: 84 90         STY   $90                 ;
F419: A0 09         LDY   #$09                
F41B: C4 90         CPY   $90                 ;
F41D: 90 02         BCC   $F421               ;
F41F: 84 90         STY   $90                 ;
F421: A0 0A         LDY   #$0A                
F423: C4 8E         CPY   $8E                 ;
F425: 90 02         BCC   $F429               ;
F427: 84 8E         STY   $8E                 ;
F429: A0 53         LDY   #$53                
F42B: C4 8E         CPY   $8E                 ;
F42D: B0 02         BCS   $F431               ;
F42F: 84 8E         STY   $8E                 ;
F431: A5 90         LDA   $90                 ;
F433: 85 8A         STA   $8A                 ;
F435: A5 8E         LDA   $8E                 ;
F437: 85 85         STA   $85                 ;
F439: A4 92         LDY   $92                 ;
F43B: A5 98         LDA   $98                 ;
F43D: 29 02         AND   #$02                
F43F: F0 04         BEQ   $F445               ;
F441: 98            TYA                       
F442: 09 10         ORA   #$10                
F444: A8            TAY                       
F445: A5 91         LDA   $91                 ;
F447: 84 91         STY   $91                 ;
F449: 85 92         STA   $92                 ;
F44B: A5 93         LDA   $93                 ;
F44D: A4 94         LDY   $94                 ;
F44F: 84 93         STY   $93                 ;
F451: 85 94         STA   $94                 ;
F453: A5 97         LDA   $97                 ;
F455: A4 98         LDY   $98                 ;
F457: 84 97         STY   $97                 ;
F459: 85 98         STA   $98                 ;
F45B: A5 95         LDA   $95                 ;
F45D: A4 96         LDY   $96                 ;
F45F: 84 95         STY   $95                 ;
F461: 85 96         STA   $96                 ;
F463: A5 9A         LDA   $9A                 ;
F465: 85 88         STA   $88                 ;
F467: A4 99         LDY   $99                 ;
F469: 84 9A         STY   $9A                 ;
F46B: 85 99         STA   $99                 ;
F46D: A5 91         LDA   $91                 ;
F46F: C9 FF         CMP   #$FF                
F471: D0 31         BNE   $F4A4               ;
F473: A2 0A         LDX   #$0A                
F475: B5 A9         LDA   $A9,X               
F477: C9 38         CMP   #$38                
F479: F0 0B         BEQ   $F486               ;
F47B: CA            DEX                       
F47C: CA            DEX                       
F47D: 10 F6         BPL   $F475               ;
F47F: A5 D8         LDA   $D8                 ;
F481: 29 07         AND   #$07                
F483: 4C A2 F4      JMP   $F4A2               ;
F486: A5 D8         LDA   $D8                 ;
F488: 29 07         AND   #$07                
F48A: C9 06         CMP   #$06                
F48C: B0 14         BCS   $F4A2               ;
F48E: 0A            ASL   A                   
F48F: AA            TAX                       
F490: B5 A9         LDA   $A9,X               
F492: C9 38         CMP   #$38                
F494: F0 0A         BEQ   $F4A0               ;
F496: E8            INX                       
F497: E8            INX                       
F498: E0 0C         CPX   #$0C                
F49A: D0 F4         BNE   $F490               ;
F49C: A2 00         LDX   #$00                
F49E: F0 F0         BEQ   $F490               ;
F4A0: 8A            TXA                       
F4A1: 4A            LSR   A                   
F4A2: 85 95         STA   $95                 ;
F4A4: A5 80         LDA   $80                 ;
F4A6: 29 01         AND   #$01                
F4A8: AA            TAX                       
F4A9: B5 9C         LDA   $9C,X               
F4AB: 18            CLC                       
F4AC: 65 9B         ADC   $9B                 ;
F4AE: 95 9C         STA   $9C,X               
F4B0: 90 24         BCC   $F4D6               ;
F4B2: A5 93         LDA   $93                 ;
F4B4: C9 54         CMP   #$54                
F4B6: F0 1E         BEQ   $F4D6               ;
F4B8: A5 97         LDA   $97                 ;
F4BA: 29 02         AND   #$02                
F4BC: F0 16         BEQ   $F4D4               ;
F4BE: 24 F8         BIT   $F8                 ;
F4C0: 50 12         BVC   $F4D4               ;
F4C2: A5 80         LDA   $80                 ;
F4C4: 29 01         AND   #$01                
F4C6: AA            TAX                       
F4C7: B5 F9         LDA   $F9,X               
F4C9: F0 09         BEQ   $F4D4               ;
F4CB: E6 93         INC   $93                 ;
F4CD: E6 93         INC   $93                 ;
F4CF: D6 F9         DEC   $F9,X               
F4D1: 4C D6 F4      JMP   $F4D6               ;
F4D4: C6 93         DEC   $93                 ;
F4D6: A6 CA         LDX   $CA                 ;
F4D8: CA            DEX                       
F4D9: 10 02         BPL   $F4DD               ;
F4DB: A2 02         LDX   #$02                
F4DD: 86 CA         STX   $CA                 ;
F4DF: A5 80         LDA   $80                 ;
F4E1: 29 0F         AND   #$0F                
F4E3: 85 DA         STA   $DA                 ;
F4E5: 0A            ASL   A                   
F4E6: 0A            ASL   A                   
F4E7: 0A            ASL   A                   
F4E8: 0A            ASL   A                   
F4E9: 05 DA         ORA   $DA                 ;
F4EB: 85 D7         STA   $D7                 ;
F4ED: A0 30         LDY   #$30                
F4EF: B5 B5         LDA   $B5,X               
F4F1: 29 20         AND   #$20                
F4F3: F0 06         BEQ   $F4FB               ;
F4F5: B5 9E         LDA   $9E,X               
F4F7: AA            TAX                       
F4F8: BC 00 FF      LDY   $FF00,X             
F4FB: 84 8B         STY   $8B                 ;
F4FD: A9 FF         LDA   #$FF                
F4FF: 85 8C         STA   $8C                 ;
F501: A5 A2         LDA   $A2                 ;
F503: 29 7F         AND   #$7F                
F505: 85 A2         STA   $A2                 ;
F507: A0 10         LDY   #$10                
F509: A9 F8         LDA   #$F8                
F50B: E0 04         CPX   #$04                
F50D: 90 0E         BCC   $F51D               ;
F50F: E0 0C         CPX   #$0C                
F511: B0 0A         BCS   $F51D               ;
F513: A5 A2         LDA   $A2                 ;
F515: 09 80         ORA   #$80                
F517: 85 A2         STA   $A2                 ;
F519: A9 F0         LDA   #$F0                
F51B: A0 15         LDY   #$15                
F51D: 85 A1         STA   $A1                 ;
F51F: 84 EE         STY   $EE                 ;
F521: A6 CA         LDX   $CA                 ;
F523: B5 A3         LDA   $A3,X               
F525: 24 A2         BIT   $A2                 ;
F527: 10 03         BPL   $F52C               ;
F529: 18            CLC                       
F52A: 69 FC         ADC   #$FC                
F52C: 85 83         STA   $83                 ;
F52E: A5 80         LDA   $80                 ;
F530: 29 07         AND   #$07                
F532: D0 19         BNE   $F54D               ;
F534: A2 02         LDX   #$02                
F536: F6 9E         INC   $9E,X               
F538: B5 9E         LDA   $9E,X               
F53A: C9 10         CMP   #$10                
F53C: D0 0C         BNE   $F54A               ;
F53E: A9 00         LDA   #$00                
F540: 95 B5         STA   $B5,X               
F542: A9 4F         LDA   #$4F                
F544: 95 C4         STA   $C4,X               
F546: A9 01         LDA   #$01                
F548: 95 C7         STA   $C7,X               
F54A: CA            DEX                       
F54B: 10 E9         BPL   $F536               ;
F54D: A2 0A         LDX   #$0A                
F54F: B5 A9         LDA   $A9,X               
F551: C9 38         CMP   #$38                
F553: F0 16         BEQ   $F56B               ;
F555: CD 79 FF      CMP   $FF79               ;
F558: F0 11         BEQ   $F56B               ;
F55A: C9 B1         CMP   #$B1                
F55C: F0 0D         BEQ   $F56B               ;
F55E: A5 80         LDA   $80                 ;
F560: 29 0F         AND   #$0F                
F562: D0 07         BNE   $F56B               ;
F564: B5 A9         LDA   $A9,X               
F566: 18            CLC                       
F567: 69 09         ADC   #$09                
F569: 95 A9         STA   $A9,X               
F56B: CA            DEX                       
F56C: CA            DEX                       
F56D: 10 E0         BPL   $F54F               ;
F56F: A9 38         LDA   #$38                
F571: 85 86         STA   $86                 ;
F573: A9 40         LDA   #$40                
F575: 85 87         STA   $87                 ;
F577: A5 A1         LDA   $A1                 ;
F579: 85 DA         STA   $DA                 ;
F57B: A9 00         LDA   #$00                
F57D: 85 A1         STA   $A1                 ;
F57F: 20 03 F0      JSR   $F003               ;
F582: A5 DA         LDA   $DA                 ;
F584: 85 A1         STA   $A1                 ;
F586: A2 00         LDX   #$00                
F588: A5 DF         LDA   $DF                 ;
F58A: 29 0F         AND   #$0F                
F58C: 0A            ASL   A                   
F58D: A8            TAY                       
F58E: B9 98 F5      LDA   $F598,Y             
F591: 48            PHA                       
F592: B9 97 F5      LDA   $F597,Y             
F595: 48            PHA                       
F596: 60            RTS                       
F597: 54            
F598: F6 3E         INC   $3E,X               
F59A: F6 F7         INC   $F7,X               
F59C: F5 DF         SBC   $DF,X               
F59E: F5 C6         SBC   $C6,X               
F5A0: F5 CD         SBC   $CD,X               
F5A2: F5 A6         SBC   $A6,X               
F5A4: F5 16         SBC   $16,X               
F5A6: F6 A5         INC   $A5,X               
F5A8: E0 29         CPX   #$29                
F5AA: 03            
F5AB: D0 06         BNE   $F5B3               ;
F5AD: A5 D8         LDA   $D8                 ;
F5AF: 29 07         AND   #$07                
F5B1: 85 E1         STA   $E1                 ;
F5B3: A0 0C         LDY   #$0C                
F5B5: A2 08         LDX   #$08                
F5B7: A5 E1         LDA   $E1                 ;
F5B9: C6 E0         DEC   $E0                 ;
F5BB: D0 57         BNE   $F614               ;
F5BD: A9 01         LDA   #$01                
F5BF: 85 DF         STA   $DF                 ;
F5C1: A9 04         LDA   #$04                
F5C3: 85 E0         STA   $E0                 ;
F5C5: D0 4D         BNE   $F614               ;
F5C7: C6 E0         DEC   $E0                 ;
F5C9: A5 E0         LDA   $E0                 ;
F5CB: 4C D8 F5      JMP   $F5D8               ;
F5CE: A5 80         LDA   $80                 ;
F5D0: 29 0F         AND   #$0F                
F5D2: C9 03         CMP   #$03                
F5D4: B0 3E         BCS   $F614               ;
F5D6: 49 07         EOR   #$07                
F5D8: 0A            ASL   A                   
F5D9: AA            TAX                       
F5DA: A0 08         LDY   #$08                
F5DC: A9 18         LDA   #$18                
F5DE: D0 34         BNE   $F614               ;
F5E0: A5 80         LDA   $80                 ;
F5E2: A6 E0         LDX   $E0                 ;
F5E4: 29 1F         AND   #$1F                
F5E6: D0 06         BNE   $F5EE               ;
F5E8: E0 0E         CPX   #$0E                
F5EA: F0 02         BEQ   $F5EE               ;
F5EC: E6 E0         INC   $E0                 ;
F5EE: A5 80         LDA   $80                 ;
F5F0: 29 03         AND   #$03                
F5F2: 09 08         ORA   #$08                
F5F4: A0 05         LDY   #$05                
F5F6: D0 5D         BNE   $F655               ;
F5F8: A4 E0         LDY   $E0                 ;
F5FA: B9 51 FE      LDA   $FE51,Y             
F5FD: A2 08         LDX   #$08                
F5FF: C8            INY                       
F600: 84 E0         STY   $E0                 ;
F602: C0 08         CPY   #$08                
F604: F0 04         BEQ   $F60A               ;
F606: A0 05         LDY   #$05                
F608: D0 0A         BNE   $F614               ;
F60A: A5 DF         LDA   $DF                 ;
F60C: 29 F0         AND   #$F0                
F60E: 85 DF         STA   $DF                 ;
F610: A2 00         LDX   #$00                
F612: 86 E0         STX   $E0                 ;
F614: 4C 55 F6      JMP   $F655               ;
F617: A0 08         LDY   #$08                
F619: 84 15         STY   $15                 ;{-2_AUDC0}
F61B: A5 80         LDA   $80                 ;
F61D: 29 0F         AND   #$0F                
F61F: D0 12         BNE   $F633               ;
F621: E6 E0         INC   $E0                 ;
F623: A5 E0         LDA   $E0                 ;
F625: C9 10         CMP   #$10                
F627: D0 0A         BNE   $F633               ;
F629: A9 30         LDA   #$30                
F62B: 85 DF         STA   $DF                 ;
F62D: A2 50         LDX   #$50                
F62F: 86 E1         STX   $E1                 ;
F631: F0 22         BEQ   $F655               ;
F633: A6 E0         LDX   $E0                 ;
F635: 86 19         STX   $19                 ;{-2_AUDV0}
F637: 8A            TXA                       
F638: 85 17         STA   $17                 ;{-2_AUDF0}
F63A: 49 FF         EOR   #$FF                
F63C: 4C D0 F6      JMP   $F6D0               ;
F63F: A5 DE         LDA   $DE                 ;
F641: C9 A0         CMP   #$A0                
F643: B0 10         BCS   $F655               ;
F645: A6 E0         LDX   $E0                 ;
F647: 8A            TXA                       
F648: E8            INX                       
F649: E0 14         CPX   #$14                
F64B: D0 02         BNE   $F64F               ;
F64D: A2 04         LDX   #$04                
F64F: 86 E0         STX   $E0                 ;
F651: A0 0C         LDY   #$0C                
F653: A2 08         LDX   #$08                
F655: 86 19         STX   $19                 ;{-2_AUDV0}AUDV0:lots 
F657: 84 15         STY   $15                 ;{-2_AUDC0}AUDC0:lots 
F659: 85 17         STA   $17                 ;{-2_AUDF0}AUDF0:lots 
F65B: A2 00         LDX   #$00                
F65D: A5 DF         LDA   $DF                 ;
F65F: 29 F0         AND   #$F0                
F661: C9 10         CMP   #$10                
F663: F0 2A         BEQ   $F68F               ;
F665: C9 20         CMP   #$20                
F667: F0 51         BEQ   $F6BA               ;
F669: C9 30         CMP   #$30                
F66B: B0 03         BCS   $F670               ;
F66D: 4C D0 F6      JMP   $F6D0               ;
F670: C6 E1         DEC   $E1                 ;
F672: F0 2D         BEQ   $F6A1               ;
F674: A5 E1         LDA   $E1                 ;
F676: 29 70         AND   #$70                
F678: 4A            LSR   A                   
F679: 4A            LSR   A                   
F67A: 4A            LSR   A                   
F67B: 4A            LSR   A                   
F67C: A8            TAY                       
F67D: BE 8A F6      LDX   $F68A,Y             
F680: A0 08         LDY   #$08                
F682: A5 E1         LDA   $E1                 ;
F684: 29 0F         AND   #$0F                
F686: 09 10         ORA   #$10                
F688: D0 46         BNE   $F6D0               ;
F68A: 02            
F68B: 04            
F68C: 06 08         ASL   $08                 ;
F68E: 0E A0 08      ASL   $08A0               ;
F691: A2 06         LDX   #$06                
F693: A5 80         LDA   $80                 ;
F695: 29 03         AND   #$03                
F697: D0 04         BNE   $F69D               ;
F699: C6 E1         DEC   $E1                 ;
F69B: F0 04         BEQ   $F6A1               ;
F69D: A5 E1         LDA   $E1                 ;
F69F: D0 2F         BNE   $F6D0               ;
F6A1: A5 DF         LDA   $DF                 ;
F6A3: 29 0F         AND   #$0F                
F6A5: 85 DF         STA   $DF                 ;
F6A7: 24 FB         BIT   $FB                 ;
F6A9: 10 0C         BPL   $F6B7               ;
F6AB: A9 C3         LDA   #$C3                
F6AD: 85 DB         STA   $DB                 ;
F6AF: A9 00         LDA   #$00                
F6B1: 85 FB         STA   $FB                 ;
F6B3: 85 E7         STA   $E7                 ;
F6B5: 85 E8         STA   $E8                 ;
F6B7: 4C D0 F6      JMP   $F6D0               ;
F6BA: A4 E1         LDY   $E1                 ;
F6BC: BE 59 FE      LDX   $FE59,Y             
F6BF: A5 80         LDA   $80                 ;
F6C1: 29 07         AND   #$07                
F6C3: D0 07         BNE   $F6CC               ;
F6C5: C8            INY                       
F6C6: 84 E1         STY   $E1                 ;
F6C8: C0 10         CPY   #$10                
F6CA: F0 D5         BEQ   $F6A1               ;
F6CC: A9 1F         LDA   #$1F                
F6CE: A0 08         LDY   #$08                
F6D0: 86 1A         STX   $1A                 ;{-2_AUDV1}AUDV1:lots 
F6D2: 84 16         STY   $16                 ;{-2_AUDC1}AUDC1:lots 
F6D4: 85 18         STA   $18                 ;{-2_AUDF1}AUDF1:lots 
F6D6: A0 00         LDY   #$00                
F6D8: A2 0F         LDX   #$0F                
F6DA: AD 82 02      LDA   $0282               ;{-2_SWCHB}SWCHB:lots 
F6DD: 29 08         AND   #$08                
F6DF: F0 02         BEQ   $F6E3               ;
F6E1: A2 FF         LDX   #$FF                
F6E3: 24 DB         BIT   $DB                 ;
F6E5: 10 06         BPL   $F6ED               ;
F6E7: 8A            TXA                       
F6E8: 29 F7         AND   #$F7                
F6EA: AA            TAX                       
F6EB: A0 FF         LDY   #$FF                
F6ED: 86 86         STX   $86                 ;
F6EF: 98            TYA                       
F6F0: 25 E8         AND   $E8                 ;
F6F2: 85 DA         STA   $DA                 ;
F6F4: A2 00         LDX   #$00                
F6F6: A0 00         LDY   #$00                
F6F8: A5 E7         LDA   $E7                 ;
F6FA: C9 FF         CMP   #$FF                
F6FC: F0 0B         BEQ   $F709               ;
F6FE: 29 0E         AND   #$0E                
F700: 4A            LSR   A                   
F701: 85 82         STA   $82                 ;
F703: 0A            ASL   A                   
F704: 0A            ASL   A                   
F705: 18            CLC                       
F706: 65 82         ADC   $82                 ;
F708: A8            TAY                       
F709: B9 BA FE      LDA   $FEBA,Y             
F70C: 45 DA         EOR   $DA                 ;
F70E: 25 86         AND   $86                 ;
F710: 95 E2         STA   $E2,X               
F712: E8            INX                       
F713: C8            INY                       
F714: E0 05         CPX   #$05                
F716: D0 F1         BNE   $F709               ;
F718: 24 FB         BIT   $FB                 ;
F71A: 30 14         BMI   $F730               ;
F71C: A4 DF         LDY   $DF                 ;
F71E: C0 30         CPY   #$30                
F720: 90 0E         BCC   $F730               ;
F722: A5 E1         LDA   $E1                 ;
F724: 25 86         AND   $86                 ;
F726: C0 40         CPY   #$40                
F728: 90 04         BCC   $F72E               ;
F72A: 85 E2         STA   $E2                 ;
F72C: B0 02         BCS   $F730               ;
F72E: 85 E5         STA   $E5                 ;
F730: A6 F5         LDX   $F5                 ;
F732: A5 DB         LDA   $DB                 ;
F734: 29 04         AND   #$04                
F736: F0 10         BEQ   $F748               ;
F738: A5 E9         LDA   $E9                 ;
F73A: 95 F3         STA   $F3,X               
F73C: A0 00         LDY   #$00                
F73E: 94 F1         STY   $F1,X               
F740: C8            INY                       
F741: C9 18         CMP   #$18                
F743: 90 01         BCC   $F746               ;
F745: C8            INY                       
F746: 94 EF         STY   $EF,X               
F748: B5 F3         LDA   $F3,X               
F74A: 20 8F FD      JSR   $FD8F               ;
F74D: A8            TAY                       
F74E: B9 ED FE      LDA   $FEED,Y             
F751: 85 CB         STA   $CB                 ;
F753: B5 F3         LDA   $F3,X               
F755: 29 0F         AND   #$0F                
F757: A8            TAY                       
F758: B9 ED FE      LDA   $FEED,Y             
F75B: 85 CD         STA   $CD                 ;
F75D: B5 F1         LDA   $F1,X               
F75F: 20 8F FD      JSR   $FD8F               ;
F762: A8            TAY                       
F763: B9 ED FE      LDA   $FEED,Y             
F766: 85 CF         STA   $CF                 ;
F768: B5 F1         LDA   $F1,X               
F76A: 29 0F         AND   #$0F                
F76C: A8            TAY                       
F76D: B9 ED FE      LDA   $FEED,Y             
F770: 85 D1         STA   $D1                 ;
F772: B5 EF         LDA   $EF,X               
F774: 20 8F FD      JSR   $FD8F               ;
F777: A8            TAY                       
F778: B9 ED FE      LDA   $FEED,Y             
F77B: 85 D3         STA   $D3                 ;
F77D: B5 EF         LDA   $EF,X               
F77F: 29 0F         AND   #$0F                
F781: A8            TAY                       
F782: B9 ED FE      LDA   $FEED,Y             
F785: 85 D5         STA   $D5                 ;
F787: A2 00         LDX   #$00                
F789: A0 30         LDY   #$30                
F78B: B5 CB         LDA   $CB,X               
F78D: C9 88         CMP   #$88                
F78F: D0 08         BNE   $F799               ;
F791: 94 CB         STY   $CB,X               
F793: E8            INX                       
F794: E8            INX                       
F795: E0 0A         CPX   #$0A                
F797: D0 F2         BNE   $F78B               ;
F799: A5 DB         LDA   $DB                 ;
F79B: 29 04         AND   #$04                
F79D: F0 06         BEQ   $F7A5               ;
F79F: 84 D1         STY   $D1                 ;
F7A1: 84 CF         STY   $CF                 ;
F7A3: 84 D3         STY   $D3                 ;
F7A5: A5 D7         LDA   $D7                 ;
F7A7: 25 86         AND   $86                 ;
F7A9: 85 D7         STA   $D7                 ;
F7AB: 24 FB         BIT   $FB                 ;
F7AD: 10 0C         BPL   $F7BB               ;
F7AF: A5 DF         LDA   $DF                 ;
F7B1: C9 30         CMP   #$30                
F7B3: D0 06         BNE   $F7BB               ;
F7B5: A5 E1         LDA   $E1                 ;
F7B7: 25 86         AND   $86                 ;
F7B9: 85 E4         STA   $E4                 ;
F7BB: A5 E6         LDA   $E6                 ;
F7BD: 45 DA         EOR   $DA                 ;
F7BF: 25 86         AND   $86                 ;
F7C1: 85 06         STA   $06                 ;{-2_COLUP0}COLUP0:lots 
F7C3: 85 07         STA   $07                 ;{-2_COLUP1}COLUP1:lots 
F7C5: A9 03         LDA   #$03                
F7C7: 85 05         STA   $05                 ;{-2_NUSIZ1}NUSIZ1:lots 
F7C9: 85 25         STA   $25                 ;{-2_VDELP0}VDELP0:lots 
F7CB: 85 26         STA   $26                 ;{-2_VDELP1}VDELP1:lots 
F7CD: A5 E4         LDA   $E4                 ;
F7CF: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:lots 

F7D1: AD 84 02      LDA   $0284               ;{-2_INTIM} Wait for end of ... ;INTIM:lots 
F7D4: D0 FB         BNE   $F7D1               ; ... VBLANK

; End of VBLANK
F7D6: 85 02         STA   $02                 ;{-2_WSYNC} Wait for end of 1st line ;WSYNC:43 
F7D8: 85 01         STA   $01                 ;{-2_VBLANK} Turn off VBLANK ;VBLANK:44 
F7DA: 85 81         STA   $81                 ;
F7DC: 85 22         STA   $22                 ;{-2_HMM0}HMM0:44 
F7DE: 85 23         STA   $23                 ;{-2_HMM1}HMM1:44 
F7E0: 85 24         STA   $24                 ;{-2_HMBL}HMBL:44 
F7E2: A9 06         LDA   #$06                
F7E4: 85 DA         STA   $DA                 ;
F7E6: A4 DA         LDY   $DA                 ;
F7E8: B1 CB         LDA   ($CB),Y             
F7EA: 85 1B         STA   $1B                 ;{-2_GRP0}GRP0:lots 
F7EC: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:lots 
F7EE: B1 CD         LDA   ($CD),Y             
F7F0: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:lots 
F7F2: B1 CF         LDA   ($CF),Y             
F7F4: 85 1B         STA   $1B                 ;{-2_GRP0}GRP0:lots 
F7F6: B1 D1         LDA   ($D1),Y             
F7F8: 85 82         STA   $82                 ;
F7FA: B1 D3         LDA   ($D3),Y             
F7FC: AA            TAX                       
F7FD: B1 D5         LDA   ($D5),Y             
F7FF: A8            TAY                       
F800: A5 82         LDA   $82                 ;
F802: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:lots 
F804: 86 1B         STX   $1B                 ;{-2_GRP0}GRP0:lots 
F806: 84 1C         STY   $1C                 ;{-2_GRP1}GRP1:lots 
F808: 84 1B         STY   $1B                 ;{-2_GRP0}GRP0:lots 
F80A: C6 DA         DEC   $DA                 ;
F80C: 10 D8         BPL   $F7E6               ;
F80E: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:51 
F810: A0 00         LDY   #$00                
F812: 84 25         STY   $25                 ;{-2_VDELP0}VDELP0:52 
F814: 84 26         STY   $26                 ;{-2_VDELP1}VDELP1:52 
F816: 84 1B         STY   $1B                 ;{-2_GRP0}GRP0:52 
F818: 84 1C         STY   $1C                 ;{-2_GRP1}GRP1:52 
F81A: A0 21         LDY   #$21                
F81C: 84 0A         STY   $0A                 ;{-2_CTRLPF}CTRLPF:52 
F81E: A5 80         LDA   $80                 ;
F820: 29 0F         AND   #$0F                
F822: 85 08         STA   $08                 ;{-2_COLUPF}COLUPF:52 
F824: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:52 
F826: A5 E3         LDA   $E3                 ;
F828: 85 06         STA   $06                 ;{-2_COLUP0}COLUP0:53 
F82A: A5 E4         LDA   $E4                 ;
F82C: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:53 
F82E: A5 D7         LDA   $D7                 ;
F830: 85 07         STA   $07                 ;{-2_COLUP1}COLUP1:53 
F832: A4 E6         LDY   $E6                 ;
F834: A5 97         LDA   $97                 ;
F836: 29 02         AND   #$02                
F838: D0 09         BNE   $F843               ;
F83A: A8            TAY                       
F83B: A5 80         LDA   $80                 ;
F83D: 29 08         AND   #$08                
F83F: D0 02         BNE   $F843               ;
F841: A0 0F         LDY   #$0F                
F843: 98            TYA                       
F844: 25 86         AND   $86                 ;
F846: 85 D7         STA   $D7                 ;
F848: A6 CA         LDX   $CA                 ;
F84A: B5 A6         LDA   $A6,X               
F84C: 85 87         STA   $87                 ;

F84E: A5 91         LDA   $91                 ;
F850: 85 04         STA   $04                 ;{-2_NUSIZ0}NUSIZ0:53 
F852: A5 EE         LDA   $EE                 ;
F854: 85 05         STA   $05                 ;{-2_NUSIZ1}NUSIZ1:53 
F856: A2 01         LDX   #$01                
F858: A9 36         LDA   #$36                
F85A: 8D 95 02      STA   $0295               ;{-2_TIM8T}TIM8T:53 
F85D: 20 05 F0      JSR   $F005               ;
F860: A9 00         LDA   #$00                
F862: 85 21         STA   $21                 ;{-2_HMP1}HMP1:57,58 
F864: AD 84 02      LDA   $0284               ;{-2_INTIM}INTIM:57,58,59 
F867: D0 FB         BNE   $F864               ;
F869: A2 53         LDX   #$53                
F86B: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:lots 
F86D: 85 2A         STA   $2A                 ;{-2_HMOVE}HMOVE:lots 
F86F: A9 02         LDA   #$02                
F871: E4 93         CPX   $93                 ;
F873: D0 06         BNE   $F87B               ;
F875: A4 D7         LDY   $D7                 ;
F877: 84 06         STY   $06                 ;{-2_COLUP0}COLUP0:lots 
F879: D0 08         BNE   $F883               ;
F87B: 24 97         BIT   $97                 ;
F87D: D0 02         BNE   $F881               ;
F87F: B0 02         BCS   $F883               ;
F881: A9 00         LDA   #$00                
F883: 85 1D         STA   $1D                 ;{-2_ENAM0}ENAM0:lots 
F885: A5 81         LDA   $81                 ;
F887: 18            CLC                       
F888: 65 95         ADC   $95                 ;
F88A: 85 81         STA   $81                 ;
F88C: A0 00         LDY   #$00                
F88E: 90 02         BCC   $F892               ;
F890: A4 97         LDY   $97                 ;
F892: 84 22         STY   $22                 ;{-2_HMM0}HMM0:lots 
F894: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:lots 
F896: A9 00         LDA   #$00                
F898: E4 85         CPX   $85                 ;
F89A: D0 02         BNE   $F89E               ;
F89C: A9 02         LDA   #$02                
F89E: 85 1F         STA   $1F                 ;{-2_ENABL}ENABL:lots 
F8A0: 8A            TXA                       
F8A1: 38            SEC                       
F8A2: E5 83         SBC   $83                 ;
F8A4: A8            TAY                       
F8A5: 24 A2         BIT   $A2                 ;
F8A7: 10 03         BPL   $F8AC               ;
F8A9: 4A            LSR   A                   
F8AA: A8            TAY                       
F8AB: 0A            ASL   A                   
F8AC: 25 A1         AND   $A1                 ;
F8AE: D0 05         BNE   $F8B5               ;
F8B0: B1 8B         LDA   ($8B),Y             
F8B2: 4C B7 F8      JMP   $F8B7               ;
F8B5: A9 00         LDA   #$00                
F8B7: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:lots 
F8B9: A9 00         LDA   #$00                
F8BB: E4 84         CPX   $84                 ;
F8BD: D0 02         BNE   $F8C1               ;
F8BF: A9 02         LDA   #$02                
F8C1: 85 1E         STA   $1E                 ;{-2_ENAM1}ENAM1:lots 
F8C3: CA            DEX                       
F8C4: D0 A5         BNE   $F86B               ;
F8C6: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:225 
F8C8: A2 02         LDX   #$02                
F8CA: A5 84         LDA   $84                 ;
F8CC: C9 01         CMP   #$01                
F8CE: F0 05         BEQ   $F8D5               ;
F8D0: A2 00         LDX   #$00                
F8D2: 4C D7 F8      JMP   $F8D7               ;
F8D5: EA            NOP                       
F8D6: EA            NOP                       
F8D7: 86 1E         STX   $1E                 ;{-2_ENAM1}ENAM1:226 
F8D9: A9 00         LDA   #$00                
F8DB: 85 1D         STA   $1D                 ;{-2_ENAM0}ENAM0:226 
F8DD: 85 1D         STA   $1D                 ;{-2_ENAM0}ENAM0:226 
F8DF: 85 10         STA   $10                 ;{-2_RESP0}RESP0:226 
F8E1: A5 E5         LDA   $E5                 ;
F8E3: 85 08         STA   $08                 ;{-2_COLUPF}COLUPF:226 
F8E5: A5 E2         LDA   $E2                 ;
F8E7: 85 06         STA   $06                 ;{-2_COLUP0}COLUP0:226 
F8E9: 85 07         STA   $07                 ;{-2_COLUP1}COLUP1:226 
F8EB: 85 07         STA   $07                 ;{-2_COLUP1}COLUP1:226 
F8ED: A0 08         LDY   #$08                
F8EF: A9 30         LDA   #$30                
F8F1: A2 84         LDX   #$84                
F8F3: 85 11         STA   $11                 ;{-2_RESP1}RESP1:226 
F8F5: 84 1E         STY   $1E                 ;{-2_ENAM1}ENAM1:226 
F8F7: 85 0D         STA   $0D                 ;{-2_PF0}PF0:226 
F8F9: A9 03         LDA   #$03                
F8FB: 85 04         STA   $04                 ;{-2_NUSIZ0}NUSIZ0:226 
F8FD: 85 05         STA   $05                 ;{-2_NUSIZ1}NUSIZ1:226 
F8FF: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:lots 
F901: B9 7F FF      LDA   $FF7F,Y             
F904: 85 0F         STA   $0F                 ;{-2_PF2}PF2:lots 
F906: B1 AD         LDA   ($AD),Y             
F908: AA            TAX                       
F909: B1 A9         LDA   ($A9),Y             
F90B: 85 1B         STA   $1B                 ;{-2_GRP0}GRP0:lots 
F90D: B1 AB         LDA   ($AB),Y             
F90F: EA            NOP                       
F910: 85 1B         STA   $1B                 ;{-2_GRP0}GRP0:lots 
F912: A5 10         LDA   $10                 ;CXM0P:lots 
F914: 86 1B         STX   $1B                 ;{-2_GRP0}GRP0:lots 
F916: B1 B3         LDA   ($B3),Y             
F918: AA            TAX                       
F919: B1 AF         LDA   ($AF),Y             
F91B: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:lots 
F91D: B1 B1         LDA   ($B1),Y             
F91F: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:lots 
F921: EA            NOP                       
F922: 86 1C         STX   $1C                 ;{-2_GRP1}GRP1:lots 
F924: 88            DEY                       
F925: 10 D8         BPL   $F8FF               ;
F927: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:235 
F929: A9 05         LDA   #$05                
F92B: 85 05         STA   $05                 ;{-2_NUSIZ1}NUSIZ1:236 
F92D: A5 E5         LDA   $E5                 ;
F92F: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:236 
F931: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:236 
F933: A9 00         LDA   #$00                
F935: 85 0F         STA   $0F                 ;{-2_PF2}PF2:236 
F937: 85 0D         STA   $0D                 ;{-2_PF0}PF0:236 
F939: 85 1B         STA   $1B                 ;{-2_GRP0}GRP0:236 
F93B: A4 DD         LDY   $DD                 ;
F93D: B9 E2 FE      LDA   $FEE2,Y             
F940: 85 8B         STA   $8B                 ;
F942: A9 FF         LDA   #$FF                
F944: 85 8C         STA   $8C                 ;
F946: A0 03         LDY   #$03                
F948: 85 11         STA   $11                 ;{-2_RESP1}RESP1:236 
F94A: A5 E4         LDA   $E4                 ;
F94C: 85 07         STA   $07                 ;{-2_COLUP1}COLUP1:236 
F94E: 85 08         STA   $08                 ;{-2_COLUPF}COLUPF:236 
F950: A5 DB         LDA   $DB                 ;
F952: 29 03         AND   #$03                
F954: AA            TAX                       
F955: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:236,237,238,239 
F957: B1 8B         LDA   ($8B),Y             
F959: 85 1C         STA   $1C                 ;{-2_GRP1}GRP1:237,238,239,240 
F95B: BD 7C FE      LDA   $FE7C,X             
F95E: 85 0D         STA   $0D                 ;{-2_PF0}PF0:237,238,239,240 
F960: 20 8F FD      JSR   $FD8F               ;
F963: 85 0D         STA   $0D                 ;{-2_PF0}PF0:237,238,239,240 
F965: 88            DEY                       
F966: 10 ED         BPL   $F955               ;
F968: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:240 
F96A: A5 E5         LDA   $E5                 ;
F96C: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:241 
F96E: A9 1A         LDA   #$1A                
F970: 8D 96 02      STA   $0296               ;{-2_TIM64T}TIM64T:241 
F973: C8            INY                       
F974: 84 1C         STY   $1C                 ;{-2_GRP1}GRP1:241 
F976: A5 91         LDA   $91                 ;
F978: C9 FF         CMP   #$FF                
F97A: D0 15         BNE   $F991               ;
F97C: 24 DE         BIT   $DE                 ;
F97E: 30 11         BMI   $F991               ;
F980: 20 81 FA      JSR   $FA81               ;
F983: 90 09         BCC   $F98E               ;
F985: A5 94         LDA   $94                 ;
F987: C9 54         CMP   #$54                
F989: D0 03         BNE   $F98E               ;
F98B: 20 F4 FC      JSR   $FCF4               ;
F98E: 4C 6F FA      JMP   $FA6F               ;
F991: A4 93         LDY   $93                 ;
F993: D0 06         BNE   $F99B               ;
F995: 20 B2 FB      JSR   $FBB2               ;
F998: 4C 6F FA      JMP   $FA6F               ;
F99B: 29 07         AND   #$07                
F99D: AA            TAX                       
F99E: BD EE FD      LDA   $FDEE,X             
F9A1: 85 88         STA   $88                 ;
F9A3: BC F6 FD      LDY   $FDF6,X             
F9A6: B9 1E FE      LDA   $FE1E,Y             
F9A9: 85 8B         STA   $8B                 ;
F9AB: B9 1F FE      LDA   $FE1F,Y             
F9AE: 85 8C         STA   $8C                 ;
F9B0: A9 53         LDA   #$53                
F9B2: 38            SEC                       
F9B3: E5 93         SBC   $93                 ;
F9B5: 85 81         STA   $81                 ;
F9B7: A5 95         LDA   $95                 ;
F9B9: 85 DA         STA   $DA                 ;
F9BB: 20 78 FC      JSR   $FC78               ;
F9BE: A4 88         LDY   $88                 ;
F9C0: A5 99         LDA   $99                 ;
F9C2: 18            CLC                       
F9C3: 71 8B         ADC   ($8B),Y             
F9C5: A4 93         LDY   $93                 ;
F9C7: 84 83         STY   $83                 ;
F9C9: A4 97         LDY   $97                 ;
F9CB: C0 F0         CPY   #$F0                
F9CD: 90 06         BCC   $F9D5               ;
F9CF: 18            CLC                       
F9D0: 65 87         ADC   $87                 ;
F9D2: 4C D8 F9      JMP   $F9D8               ;
F9D5: 38            SEC                       
F9D6: E5 87         SBC   $87                 ;
F9D8: 85 82         STA   $82                 ;
F9DA: A6 CA         LDX   $CA                 ;
F9DC: B5 B5         LDA   $B5,X               
F9DE: 29 20         AND   #$20                
F9E0: F0 39         BEQ   $FA1B               ;
F9E2: B4 C7         LDY   $C7,X               
F9E4: B5 C4         LDA   $C4,X               
F9E6: AA            TAX                       
F9E7: 20 4C FC      JSR   $FC4C               ;
F9EA: 85 82         STA   $82                 ;
F9EC: A6 CA         LDX   $CA                 ;
F9EE: B4 9E         LDY   $9E,X               
F9F0: A5 97         LDA   $97                 ;
F9F2: 29 02         AND   #$02                
F9F4: F0 1E         BEQ   $FA14               ;
F9F6: 24 F8         BIT   $F8                 ;
F9F8: 50 1A         BVC   $FA14               ;
F9FA: B9 DF FD      LDA   $FDDF,Y             
F9FD: C5 82         CMP   $82                 ;
F9FF: 90 1A         BCC   $FA1B               ;
FA01: A5 82         LDA   $82                 ;
FA03: C9 03         CMP   #$03                
FA05: 90 17         BCC   $FA1E               ;
FA07: A5 80         LDA   $80                 ;
FA09: 29 01         AND   #$01                
FA0B: AA            TAX                       
FA0C: A9 02         LDA   #$02                
FA0E: 95 F9         STA   $F9,X               
FA10: D0 09         BNE   $FA1B               ;
FA12: 90 07         BCC   $FA1B               ;
FA14: B9 DF FD      LDA   $FDDF,Y             
FA17: C5 82         CMP   $82                 ;
FA19: B0 03         BCS   $FA1E               ;
FA1B: 4C 68 FA      JMP   $FA68               ;
FA1E: A0 00         LDY   #$00                
FA20: A5 97         LDA   $97                 ;
FA22: 29 02         AND   #$02                
FA24: F0 01         BEQ   $FA27               ;
FA26: C8            INY                       
FA27: A9 25         LDA   #$25                
FA29: 20 CB FC      JSR   $FCCB               ;
FA2C: A5 DF         LDA   $DF                 ;
FA2E: C9 30         CMP   #$30                
FA30: B0 0A         BCS   $FA3C               ;
FA32: 29 0F         AND   #$0F                
FA34: 09 20         ORA   #$20                
FA36: 85 DF         STA   $DF                 ;
FA38: A9 00         LDA   #$00                
FA3A: 85 E1         STA   $E1                 ;
FA3C: A5 8B         LDA   $8B                 ;
FA3E: 18            CLC                       
FA3F: 69 0D         ADC   #$0D                
FA41: 85 8B         STA   $8B                 ;
FA43: A4 88         LDY   $88                 ;
FA45: B1 8B         LDA   ($8B),Y             
FA47: 85 91         STA   $91                 ;
FA49: C9 FF         CMP   #$FF                
FA4B: D0 06         BNE   $FA53               ;
FA4D: A9 55         LDA   #$55                
FA4F: 85 93         STA   $93                 ;
FA51: D0 1C         BNE   $FA6F               ;
FA53: A5 8B         LDA   $8B                 ;
FA55: 18            CLC                       
FA56: 69 0D         ADC   #$0D                
FA58: 85 8B         STA   $8B                 ;
FA5A: A5 99         LDA   $99                 ;
FA5C: 18            CLC                       
FA5D: 71 8B         ADC   ($8B),Y             
FA5F: 85 99         STA   $99                 ;
FA61: A5 8B         LDA   $8B                 ;
FA63: 38            SEC                       
FA64: E9 1A         SBC   #$1A                
FA66: 85 8B         STA   $8B                 ;
FA68: C6 88         DEC   $88                 ;
FA6A: 30 03         BMI   $FA6F               ;
FA6C: 4C BE F9      JMP   $F9BE               ;
FA6F: AD 84 02      LDA   $0284               ;{-2_INTIM}INTIM:lots 
FA72: D0 FB         BNE   $FA6F               ;
FA74: A9 02         LDA   #$02                
FA76: 85 02         STA   $02                 ;{-2_WSYNC}WSYNC:262 
FA78: 85 01         STA   $01                 ;{-2_VBLANK}VBLANK:263 
FA7A: A9 00         LDA   #$00                
FA7C: 85 09         STA   $09                 ;{-2_COLUBK}COLUBK:263 
FA7E: 4C 56 F0      JMP   $F056               ;
FA81: A0 00         LDY   #$00                
FA83: A5 97         LDA   $97                 ;
FA85: 29 02         AND   #$02                
FA87: F0 0C         BEQ   $FA95               ;
FA89: A5 98         LDA   $98                 ;
FA8B: 29 02         AND   #$02                
FA8D: D0 06         BNE   $FA95               ;
FA8F: A5 DF         LDA   $DF                 ;
FA91: 29 F0         AND   #$F0                
FA93: 85 DF         STA   $DF                 ;
FA95: 84 97         STY   $97                 ;
FA97: 24 DE         BIT   $DE                 ;
FA99: 30 08         BMI   $FAA3               ;
FA9B: A5 DE         LDA   $DE                 ;
FA9D: D0 26         BNE   $FAC5               ;
FA9F: A5 EB         LDA   $EB                 ;
FAA1: D0 06         BNE   $FAA9               ;
FAA3: A9 54         LDA   #$54                
FAA5: 85 93         STA   $93                 ;
FAA7: 38            SEC                       
FAA8: 60            RTS                       
FAA9: A0 02         LDY   #$02                
FAAB: 84 E0         STY   $E0                 ;
FAAD: A0 FF         LDY   #$FF                
FAAF: 84 97         STY   $97                 ;
FAB1: A5 80         LDA   $80                 ;
FAB3: 29 01         AND   #$01                
FAB5: AA            TAX                       
FAB6: C8            INY                       
FAB7: 94 F9         STY   $F9,X               
FAB9: C6 EB         DEC   $EB                 ;
FABB: A5 DF         LDA   $DF                 ;
FABD: 29 F0         AND   #$F0                
FABF: 09 03         ORA   #$03                
FAC1: 85 DF         STA   $DF                 ;
FAC3: D0 0A         BNE   $FACF               ;
FAC5: A5 D8         LDA   $D8                 ;
FAC7: 29 18         AND   #$18                
FAC9: D0 04         BNE   $FACF               ;
FACB: A5 EB         LDA   $EB                 ;
FACD: D0 DA         BNE   $FAA9               ;
FACF: A4 95         LDY   $95                 ;
FAD1: B9 05 FE      LDA   $FE05,Y             
FAD4: 85 82         STA   $82                 ;
FAD6: 24 97         BIT   $97                 ;
FAD8: 30 11         BMI   $FAEB               ;
FADA: A5 DE         LDA   $DE                 ;
FADC: C9 04         CMP   #$04                
FADE: B0 07         BCS   $FAE7               ;
FAE0: A8            TAY                       
FAE1: B9 15 FE      LDA   $FE15,Y             
FAE4: 4C FA FA      JMP   $FAFA               ;
FAE7: C0 06         CPY   #$06                
FAE9: 90 04         BCC   $FAEF               ;
FAEB: A9 00         LDA   #$00                
FAED: F0 0B         BEQ   $FAFA               ;
FAEF: A5 D8         LDA   $D8                 ;
FAF1: 4A            LSR   A                   
FAF2: 4A            LSR   A                   
FAF3: 4A            LSR   A                   
FAF4: 29 07         AND   #$07                
FAF6: A8            TAY                       
FAF7: B9 0D FE      LDA   $FE0D,Y             
FAFA: A8            TAY                       
FAFB: 85 91         STA   $91                 ;
FAFD: B9 FD FD      LDA   $FDFD,Y             
FB00: 85 83         STA   $83                 ;
FB02: A5 D8         LDA   $D8                 ;
FB04: C9 A0         CMP   #$A0                
FB06: 90 01         BCC   $FB09               ;
FB08: 4A            LSR   A                   
FB09: 18            CLC                       
FB0A: 65 83         ADC   $83                 ;
FB0C: C9 A0         CMP   #$A0                
FB0E: 90 01         BCC   $FB11               ;
FB10: 4A            LSR   A                   
FB11: 38            SEC                       
FB12: E5 83         SBC   $83                 ;
FB14: 85 99         STA   $99                 ;
FB16: C5 82         CMP   $82                 ;
FB18: B0 34         BCS   $FB4E               ;
FB1A: 18            CLC                       
FB1B: 65 83         ADC   $83                 ;
FB1D: C5 82         CMP   $82                 ;
FB1F: 90 29         BCC   $FB4A               ;
FB21: A5 82         LDA   $82                 ;
FB23: 18            CLC                       
FB24: 65 83         ADC   $83                 ;
FB26: C9 A0         CMP   #$A0                
FB28: B0 0A         BCS   $FB34               ;
FB2A: A5 83         LDA   $83                 ;
FB2C: 4A            LSR   A                   
FB2D: 18            CLC                       
FB2E: 65 99         ADC   $99                 ;
FB30: C5 82         CMP   $82                 ;
FB32: B0 0F         BCS   $FB43               ;
FB34: A5 82         LDA   $82                 ;
FB36: C5 83         CMP   $83                 ;
FB38: 90 09         BCC   $FB43               ;
FB3A: A2 10         LDX   #$10                
FB3C: A5 83         LDA   $83                 ;
FB3E: 18            CLC                       
FB3F: 65 99         ADC   $99                 ;
FB41: D0 0F         BNE   $FB52               ;
FB43: A2 F0         LDX   #$F0                
FB45: A5 99         LDA   $99                 ;
FB47: 4C 52 FB      JMP   $FB52               ;
FB4A: A2 F0         LDX   #$F0                
FB4C: D0 EE         BNE   $FB3C               ;
FB4E: A2 10         LDX   #$10                
FB50: A5 99         LDA   $99                 ;
FB52: 86 DA         STX   $DA                 ;
FB54: AA            TAX                       
FB55: A5 97         LDA   $97                 ;
FB57: 29 02         AND   #$02                
FB59: 05 DA         ORA   $DA                 ;
FB5B: 85 97         STA   $97                 ;
FB5D: 8A            TXA                       
FB5E: A0 53         LDY   #$53                
FB60: 84 93         STY   $93                 ;
FB62: 38            SEC                       
FB63: E5 82         SBC   $82                 ;
FB65: B0 04         BCS   $FB6B               ;
FB67: 49 FF         EOR   #$FF                
FB69: 69 01         ADC   #$01                
FB6B: 84 81         STY   $81                 ;
FB6D: 20 7E FB      JSR   $FB7E               ;
FB70: 86 87         STX   $87                 ;
FB72: A2 00         LDX   #$00                
FB74: 85 DA         STA   $DA                 ;
FB76: 20 82 FB      JSR   $FB82               ;
FB79: 86 86         STX   $86                 ;
FB7B: 4C 9C FB      JMP   $FB9C               ;
FB7E: 85 DA         STA   $DA                 ;
FB80: A9 00         LDA   #$00                
FB82: A0 07         LDY   #$07                
FB84: 26 DA         ROL   $DA                 ;
FB86: 2A            ROL   A                   
FB87: B0 0E         BCS   $FB97               ;
FB89: C5 81         CMP   $81                 ;
FB8B: 90 02         BCC   $FB8F               ;
FB8D: E5 81         SBC   $81                 ;
FB8F: 88            DEY                       
FB90: 10 F2         BPL   $FB84               ;
FB92: 26 DA         ROL   $DA                 ;
FB94: A6 DA         LDX   $DA                 ;
FB96: 60            RTS                       
FB97: E5 81         SBC   $81                 ;
FB99: 38            SEC                       
FB9A: B0 F3         BCS   $FB8F               ;
FB9C: A5 86         LDA   $86                 ;
FB9E: 85 95         STA   $95                 ;
FBA0: A5 97         LDA   $97                 ;
FBA2: 29 02         AND   #$02                
FBA4: D0 0A         BNE   $FBB0               ;
FBA6: A4 91         LDY   $91                 ;
FBA8: A5 DE         LDA   $DE                 ;
FBAA: 18            CLC                       
FBAB: F9 EE FD      SBC   $FDEE,Y             
FBAE: 85 DE         STA   $DE                 ;
FBB0: 18            CLC                       
FBB1: 60            RTS                       
FBB2: A5 91         LDA   $91                 ;
FBB4: 29 07         AND   #$07                
FBB6: A8            TAY                       
FBB7: B9 EE FD      LDA   $FDEE,Y             
FBBA: 85 82         STA   $82                 ;
FBBC: B9 F6 FD      LDA   $FDF6,Y             
FBBF: A8            TAY                       
FBC0: B9 1E FE      LDA   $FE1E,Y             
FBC3: 85 8B         STA   $8B                 ;
FBC5: B9 1F FE      LDA   $FE1F,Y             
FBC8: 85 8C         STA   $8C                 ;
FBCA: A9 53         LDA   #$53                
FBCC: 85 81         STA   $81                 ;
FBCE: A5 95         LDA   $95                 ;
FBD0: 85 DA         STA   $DA                 ;
FBD2: 20 78 FC      JSR   $FC78               ;
FBD5: A4 82         LDY   $82                 ;
FBD7: A5 99         LDA   $99                 ;
FBD9: 18            CLC                       
FBDA: 71 8B         ADC   ($8B),Y             
FBDC: A6 97         LDX   $97                 ;
FBDE: E0 F0         CPX   #$F0                
FBE0: B0 06         BCS   $FBE8               ;
FBE2: 38            SEC                       
FBE3: E5 87         SBC   $87                 ;
FBE5: 4C EB FB      JMP   $FBEB               ;
FBE8: 18            CLC                       
FBE9: 65 87         ADC   $87                 ;
FBEB: 85 81         STA   $81                 ;
FBED: A0 00         LDY   #$00                
FBEF: B9 05 FE      LDA   $FE05,Y             
FBF2: 38            SEC                       
FBF3: E9 04         SBC   #$04                
FBF5: C5 81         CMP   $81                 ;
FBF7: B0 06         BCS   $FBFF               ;
FBF9: 69 08         ADC   #$08                
FBFB: C5 81         CMP   $81                 ;
FBFD: B0 08         BCS   $FC07               ;
FBFF: C8            INY                       
FC00: C0 07         CPY   #$07                
FC02: D0 EB         BNE   $FBEF               ;
FC04: 4C 3F FC      JMP   $FC3F               ;
FC07: C0 06         CPY   #$06                
FC09: D0 16         BNE   $FC21               ;
FC0B: A9 20         LDA   #$20                
FC0D: 85 DC         STA   $DC                 ;
FC0F: A5 DF         LDA   $DF                 ;
FC11: 29 0F         AND   #$0F                
FC13: 09 30         ORA   #$30                
FC15: 85 DF         STA   $DF                 ;
FC17: A9 50         LDA   #$50                
FC19: 85 E1         STA   $E1                 ;
FC1B: A9 00         LDA   #$00                
FC1D: 85 DD         STA   $DD                 ;
FC1F: F0 1E         BEQ   $FC3F               ;
FC21: 98            TYA                       
FC22: 0A            ASL   A                   
FC23: AA            TAX                       
FC24: AC 7D FF      LDY   $FF7D               ;
FC27: B5 A9         LDA   $A9,X               
FC29: CD 79 FF      CMP   $FF79               ;
FC2C: F0 0F         BEQ   $FC3D               ;
FC2E: AC 7B FF      LDY   $FF7B               ;
FC31: A5 DF         LDA   $DF                 ;
FC33: 29 0F         AND   #$0F                
FC35: 09 40         ORA   #$40                
FC37: 85 DF         STA   $DF                 ;
FC39: A9 50         LDA   #$50                
FC3B: 85 E1         STA   $E1                 ;
FC3D: 94 A9         STY   $A9,X               
FC3F: C6 82         DEC   $82                 ;
FC41: 10 92         BPL   $FBD5               ;
FC43: A9 FF         LDA   #$FF                
FC45: 85 91         STA   $91                 ;
FC47: A9 55         LDA   #$55                
FC49: 85 93         STA   $93                 ;
FC4B: 60            RTS                       
FC4C: 8A            TXA                       
FC4D: 38            SEC                       
FC4E: E5 82         SBC   $82                 ;
FC50: B0 04         BCS   $FC56               ;
FC52: 49 FF         EOR   #$FF                
FC54: 69 01         ADC   #$01                
FC56: 85 82         STA   $82                 ;
FC58: 98            TYA                       
FC59: 38            SEC                       
FC5A: E5 83         SBC   $83                 ;
FC5C: B0 04         BCS   $FC62               ;
FC5E: 49 FF         EOR   #$FF                
FC60: 69 01         ADC   #$01                
FC62: C5 82         CMP   $82                 ;
FC64: 90 05         BCC   $FC6B               ;
FC66: A6 82         LDX   $82                 ;
FC68: 85 82         STA   $82                 ;
FC6A: 8A            TXA                       
FC6B: 4A            LSR   A                   
FC6C: 4A            LSR   A                   
FC6D: 85 83         STA   $83                 ;
FC6F: 0A            ASL   A                   
FC70: 18            CLC                       
FC71: 65 83         ADC   $83                 ;
FC73: 4A            LSR   A                   
FC74: 18            CLC                       
FC75: 65 82         ADC   $82                 ;
FC77: 60            RTS                       
FC78: A9 00         LDA   #$00                
FC7A: 85 87         STA   $87                 ;
FC7C: A2 08         LDX   #$08                
FC7E: 0A            ASL   A                   
FC7F: 26 87         ROL   $87                 ;
FC81: 06 81         ASL   $81                 ;
FC83: 90 07         BCC   $FC8C               ;
FC85: 18            CLC                       
FC86: 65 DA         ADC   $DA                 ;
FC88: 90 02         BCC   $FC8C               ;
FC8A: E6 87         INC   $87                 ;
FC8C: CA            DEX                       
FC8D: D0 EF         BNE   $FC7E               ;
FC8F: 85 86         STA   $86                 ;
FC91: 60            RTS                       
FC92: 06 D8         ASL   $D8                 ;
FC94: 26 D9         ROL   $D9                 ;
FC96: 10 02         BPL   $FC9A               ;
FC98: E6 D8         INC   $D8                 ;
FC9A: A5 D8         LDA   $D8                 ;
FC9C: 2C AE FC      BIT   $FCAE               ;
FC9F: F0 04         BEQ   $FCA5               ;
FCA1: 49 01         EOR   #$01                
FCA3: 85 D8         STA   $D8                 ;
FCA5: 05 D9         ORA   $D9                 ;
FCA7: D0 02         BNE   $FCAB               ;
FCA9: E6 D8         INC   $D8                 ;
FCAB: A5 D8         LDA   $D8                 ;
FCAD: 60            RTS                       
FCAE: 02            
FCAF: A0 01         LDY   #$01                
FCB1: A5 DB         LDA   $DB                 ;
FCB3: 29 03         AND   #$03                
FCB5: F0 0A         BEQ   $FCC1               ;
FCB7: C9 01         CMP   #$01                
FCB9: F0 05         BEQ   $FCC0               ;
FCBB: A9 00         LDA   #$00                
FCBD: 85 DD         STA   $DD                 ;
FCBF: 60            RTS                       
FCC0: C8            INY                       
FCC1: 98            TYA                       
FCC2: 05 DB         ORA   $DB                 ;
FCC4: 85 DB         STA   $DB                 ;
FCC6: A9 0A         LDA   #$0A                
FCC8: 85 DD         STA   $DD                 ;
FCCA: 60            RTS                       
FCCB: 85 DA         STA   $DA                 ;
FCCD: A2 05         LDX   #$05                
FCCF: A5 E7         LDA   $E7                 ;
FCD1: C9 0C         CMP   #$0C                
FCD3: B0 02         BCS   $FCD7               ;
FCD5: 4A            LSR   A                   
FCD6: AA            TAX                       
FCD7: 86 82         STX   $82                 ;
FCD9: A6 F5         LDX   $F5                 ;
FCDB: A5 DA         LDA   $DA                 ;
FCDD: F8            SED                       
FCDE: 18            CLC                       
FCDF: 75 EF         ADC   $EF,X               
FCE1: 95 EF         STA   $EF,X               
FCE3: 98            TYA                       
FCE4: 75 F1         ADC   $F1,X               
FCE6: 95 F1         STA   $F1,X               
FCE8: A9 00         LDA   #$00                
FCEA: 75 F3         ADC   $F3,X               
FCEC: 95 F3         STA   $F3,X               
FCEE: D8            CLD                       
FCEF: C6 82         DEC   $82                 ;
FCF1: 10 E6         BPL   $FCD9               ;
FCF3: 60            RTS                       
FCF4: A2 00         LDX   #$00                
FCF6: 8A            TXA                       
FCF7: B4 A9         LDY   $A9,X               
FCF9: 38            SEC                       
FCFA: C0 38         CPY   #$38                
FCFC: F0 01         BEQ   $FCFF               ;
FCFE: 18            CLC                       
FCFF: 2A            ROL   A                   
FD00: E8            INX                       
FD01: E8            INX                       
FD02: E0 0C         CPX   #$0C                
FD04: D0 F1         BNE   $FCF7               ;
FD06: A6 F5         LDX   $F5                 ;
FD08: 95 EC         STA   $EC,X               
FD0A: A2 FF         LDX   #$FF                
FD0C: 86 DE         STX   $DE                 ;
FD0E: E8            INX                       
FD0F: 86 90         STX   $90                 ;
FD11: 86 8E         STX   $8E                 ;
FD13: 86 E0         STX   $E0                 ;
FD15: 60            RTS                       
FD16: 24 F8         BIT   $F8                 ;
FD18: 30 20         BMI   $FD3A               ;
FD1A: A5 EC         LDA   $EC                 ;
FD1C: D0 45         BNE   $FD63               ;
FD1E: A9 07         LDA   #$07                
FD20: 85 DF         STA   $DF                 ;
FD22: A2 FF         LDX   #$FF                
FD24: 86 FB         STX   $FB                 ;
FD26: A5 E9         LDA   $E9                 ;
FD28: C9 13         CMP   #$13                
FD2A: D0 DE         BNE   $FD0A               ;
FD2C: A5 F1         LDA   $F1                 ;
FD2E: 05 F3         ORA   $F3                 ;
FD30: D0 D8         BNE   $FD0A               ;
FD32: A9 B1         LDA   #$B1                
FD34: 85 B3         STA   $B3                 ;
FD36: C6 B4         DEC   $B4                 ;
FD38: D0 D0         BNE   $FD0A               ;
FD3A: A6 F5         LDX   $F5                 ;
FD3C: B5 EC         LDA   $EC,X               
FD3E: D0 0D         BNE   $FD4D               ;
FD40: 8A            TXA                       
FD41: 49 01         EOR   #$01                
FD43: AA            TAX                       
FD44: B5 EC         LDA   $EC,X               
FD46: F0 D6         BEQ   $FD1E               ;
FD48: 86 F5         STX   $F5                 ;
FD4A: 4C 63 FD      JMP   $FD63               ;
FD4D: 8A            TXA                       
FD4E: 49 01         EOR   #$01                
FD50: AA            TAX                       
FD51: B5 EC         LDA   $EC,X               
FD53: F0 05         BEQ   $FD5A               ;
FD55: 86 F5         STX   $F5                 ;
FD57: 4C 63 FD      JMP   $FD63               ;
FD5A: 8A            TXA                       
FD5B: 49 01         EOR   #$01                
FD5D: 85 F5         STA   $F5                 ;
FD5F: AA            TAX                       
FD60: 4C 67 FD      JMP   $FD67               ;
FD63: A6 F5         LDX   $F5                 ;
FD65: D0 15         BNE   $FD7C               ;
FD67: E6 E7         INC   $E7                 ;
FD69: A5 E7         LDA   $E7                 ;
FD6B: C9 10         CMP   #$10                
FD6D: B0 0D         BCS   $FD7C               ;
FD6F: A5 9B         LDA   $9B                 ;
FD71: 18            CLC                       
FD72: 69 08         ADC   #$08                
FD74: 24 FB         BIT   $FB                 ;
FD76: 70 02         BVS   $FD7A               ;
FD78: 69 05         ADC   #$05                
FD7A: 85 9B         STA   $9B                 ;
FD7C: B5 EC         LDA   $EC,X               
FD7E: A2 0A         LDX   #$0A                
FD80: 4A            LSR   A                   
FD81: A0 38         LDY   #$38                
FD83: B0 03         BCS   $FD88               ;
FD85: AC 79 FF      LDY   $FF79               ;
FD88: 94 A9         STY   $A9,X               
FD8A: CA            DEX                       
FD8B: CA            DEX                       
FD8C: 10 F2         BPL   $FD80               ;
FD8E: 60            RTS                       
FD8F: 29 F0         AND   #$F0                
FD91: 4A            LSR   A                   
FD92: 4A            LSR   A                   
FD93: 4A            LSR   A                   
FD94: 4A            LSR   A                   
FD95: 60            RTS                       
FD96: A6 F5         LDX   $F5                 ;
FD98: B5 F3         LDA   $F3,X               
FD9A: D5 F6         CMP   $F6,X               
FD9C: F0 40         BEQ   $FDDE               ;
FD9E: B5 EC         LDA   $EC,X               
FDA0: C9 3F         CMP   #$3F                
FDA2: F0 3A         BEQ   $FDDE               ;
FDA4: A9 06         LDA   #$06                
FDA6: 85 DF         STA   $DF                 ;
FDA8: A9 A0         LDA   #$A0                
FDAA: 85 E0         STA   $E0                 ;
FDAC: A5 D8         LDA   $D8                 ;
FDAE: 29 07         AND   #$07                
FDB0: C9 06         CMP   #$06                
FDB2: 90 02         BCC   $FDB6               ;
FDB4: E9 04         SBC   #$04                
FDB6: A8            TAY                       
FDB7: B9 8E FE      LDA   $FE8E,Y             
FDBA: 85 DA         STA   $DA                 ;
FDBC: A5 DA         LDA   $DA                 ;
FDBE: 35 EC         AND   $EC,X               
FDC0: F0 0A         BEQ   $FDCC               ;
FDC2: 46 DA         LSR   $DA                 ;
FDC4: 90 F6         BCC   $FDBC               ;
FDC6: A9 20         LDA   #$20                
FDC8: 85 DA         STA   $DA                 ;
FDCA: D0 F0         BNE   $FDBC               ;
FDCC: B5 EC         LDA   $EC,X               
FDCE: 05 DA         ORA   $DA                 ;
FDD0: 95 EC         STA   $EC,X               
FDD2: B5 F6         LDA   $F6,X               
FDD4: F8            SED                       
FDD5: 18            CLC                       
FDD6: 69 01         ADC   #$01                
FDD8: D8            CLD                       
FDD9: 95 F6         STA   $F6,X               
FDDB: 4C 96 FD      JMP   $FD96               ;
FDDE: 60            RTS                       
FDDF: 01 02         ORA   ($02,X)             
FDE1: 03            
FDE2: 04            
FDE3: 02            
FDE4: 04            
FDE5: 06 08         ASL   $08                 ;
FDE7: 06 04         ASL   $04                 ;
FDE9: 02            
FDEA: 04            
FDEB: 03            
FDEC: 02            
FDED: 01 00         ORA   ($00,X)             
FDEF: 01 01         ORA   ($01,X)             
FDF1: 02            
FDF2: 01 00         ORA   ($00,X)             
FDF4: 02            
FDF5: 01 00         ORA   ($00,X)             
FDF7: 02            
FDF8: 06 04         ASL   $04                 ;
FDFA: 0A            ASL   A                   
FDFB: 00            BRK                       
FDFC: 08            PHP                       
FDFD: 00            BRK                       
FDFE: 10 20         BPL   $FE20               ;
FE00: 20 40 00      JSR   $0040               ;
FE03: 40            RTI                       
FE04: 00            BRK                       
FE05: 18            CLC                       
FE06: 28            PLP                       
FE07: 38            SEC                       
FE08: 6A            ROR   A                   
FE09: 7A            
FE0A: 8A            TXA                       
FE0B: 50 50         BVC   $FE5D               ;
FE0D: 00            BRK                       
FE0E: 01 02         ORA   ($02,X)             
FE10: 03            
FE11: 04            
FE12: 00            BRK                       
FE13: 06 04         ASL   $04                 ;
FE15: 00            BRK                       
FE16: 00            BRK                       
FE17: 02            
FE18: 06 08         ASL   $08                 ;
FE1A: 04            
FE1B: 00            BRK                       
FE1C: 02            
FE1D: 0A            ASL   A                   
FE1E: 2A            ROL   A                   
FE1F: FE 2B FE      INC   $FE2B,X             
FE22: 2D FE 30      AND   $30FE               ;
FE25: FE 32 FE      INC   $FE32,X             
FE28: 35 FE         AND   $FE,X               
FE2A: 00            BRK                       
FE2B: 00            BRK                       
FE2C: 10 00         BPL   $FE2E               ;
FE2E: 10 20         BPL   $FE50               ;
FE30: 00            BRK                       
FE31: 20 00 20      JSR   $2000               ;
FE34: 40            RTI                       
FE35: 00            BRK                       
FE36: 40            RTI                       
FE37: FF            
FE38: 00            BRK                       
FE39: 00            BRK                       
FE3A: 01 02         ORA   ($02,X)             
FE3C: 01 00         ORA   ($00,X)             
FE3E: 00            BRK                       
FE3F: 02            
FE40: 04            
FE41: 02            
FE42: 00            BRK                       
FE43: 00            BRK                       
FE44: 00            BRK                       
FE45: 10 00         BPL   $FE47               ;
FE47: 10 00         BPL   $FE49               ;
FE49: 00            BRK                       
FE4A: 20 00 20      JSR   $2000               ;
FE4D: 00            BRK                       
FE4E: 00            BRK                       
FE4F: 40            RTI                       
FE50: 00            BRK                       
FE51: 0C            
FE52: 0A            ASL   A                   
FE53: 08            PHP                       
FE54: 06 04         ASL   $04                 ;
FE56: 02            
FE57: 00            BRK                       
FE58: 00            BRK                       
FE59: 0F            
FE5A: 0C            
FE5B: 0A            ASL   A                   
FE5C: 08            PHP                       
FE5D: 0A            ASL   A                   
FE5E: 08            PHP                       
FE5F: 08            PHP                       
FE60: 06 04         ASL   $04                 ;
FE62: 04            
FE63: 08            PHP                       
FE64: 08            PHP                       
FE65: 06 04         ASL   $04                 ;
FE67: 02            
FE68: 13            
FE69: 14            
FE6A: 15 16         ORA   $16,X               
FE6C: 0C            
FE6D: 0F            
FE6E: 12            
FE6F: 0C            
FE70: 10 0E         BPL   $FE80               ;
FE72: 11 0A         ORA   ($0A),Y             
FE74: 0D 10 13      ORA   $1310               ;
FE77: 0C            
FE78: 0E 10 12      ASL   $1210               ;
FE7B: 14            
FE7C: A0 80         LDY   #$80                
FE7E: 00            BRK                       
FE7F: 00            BRK                       
FE80: 00            BRK                       
FE81: 00            BRK                       
FE82: 00            BRK                       
FE83: 01 01         ORA   ($01,X)             
FE85: 02            
FE86: 03            
FE87: 04            
FE88: 04            
FE89: 05 05         ORA   $05                 ;
FE8B: 06 06         ASL   $06                 ;
FE8D: 07            
FE8E: 20 10 08      JSR   $0810               ;
FE91: 04            
FE92: 02            
FE93: 01 00         ORA   ($00,X)             
FE95: 00            BRK                       
FE96: 01 40         ORA   ($40,X)             
FE98: 41 06         EOR   ($06,X)             
FE9A: 07            
FE9B: 46 47         LSR   $47                 ;
FE9D: 0A            ASL   A                   
FE9E: 00            BRK                       
FE9F: 00            BRK                       
FEA0: 00            BRK                       
FEA1: 00            BRK                       
FEA2: 00            BRK                       
FEA3: 00            BRK                       
FEA4: 0B            
FEA5: 4A            LSR   A                   
FEA6: 4B            
FEA7: 0E 0F 4E      ASL   $4E0F               ;
FEAA: 4F            
FEAB: 00            BRK                       
FEAC: 01 80         ORA   ($80,X)             
FEAE: 01 80         ORA   ($80,X)             
FEB0: 00            BRK                       
FEB1: 98            TYA                       
FEB2: A8            TAY                       
FEB3: C8            INY                       
FEB4: AE 98 98      LDX   $9898               ;
FEB7: EF            
FEB8: 00            BRK                       
FEB9: 00            BRK                       
FEBA: 84 48         STY   $48                 ;
FEBC: 00            BRK                       
FEBD: 24 47         BIT   $47                 ;
FEBF: 84 CE         STY   $CE                 ;
FEC1: 00            BRK                       
FEC2: D8            CLD                       
FEC3: 0E DA 48      ASL   $48DA               ;
FEC6: 00            BRK                       
FEC7: 84 88         STY   $88                 ;
FEC9: 8A            TXA                       
FECA: 1A            
FECB: 00            BRK                       
FECC: 44            
FECD: 24 28         BIT   $28                 ;
FECF: 4C 84 DA      JMP   $DA84               ;
FED2: DA            
FED3: 88            DEY                       
FED4: 0E C4 00      ASL   $00C4               ;
FED7: 0E 1A 0E      ASL   $0E1A               ;
FEDA: 74            
FEDB: C8            INY                       
FEDC: CA            DEX                       
FEDD: 44            
FEDE: 00            BRK                       
FEDF: 1A            
FEE0: C8            INY                       
FEE1: 44            
FEE2: 30 F2         BMI   $FED6               ;
FEE4: EE EA E6      INC   $E6EA               ;
FEE7: E2            
FEE8: DE DA D6      DEC   $D6DA,X             
FEEB: D2            
FEEC: CE 88 8F      DEC   $8F88               ;
FEEF: 96 9D         STX   $9D,Y               
FEF1: A4 AB         LDY   $AB                 ;
FEF3: B2            
FEF4: B9 C0 C7      LDA   $C7C0,Y             
FEF7: 00            BRK                       
FEF8: 00            BRK                       
FEF9: 00            BRK                       
FEFA: 00            BRK                       
FEFB: 00            BRK                       
FEFC: 00            BRK                       
FEFD: 00            BRK                       
FEFE: 00            BRK                       
FEFF: 00            BRK                       
FF00: 10 18         BPL   $FF1A               ;
FF02: 20 28 10      JSR   $1028               ;
FF05: 18            CLC                       
FF06: 20 28 28      JSR   $2828               ;
FF09: 20 18 10      JSR   $1018               ;
FF0C: 28            PLP                       
FF0D: 20 18 10      JSR   $1018               ;
FF10: 00            BRK                       
FF11: 00            BRK                       
FF12: 00            BRK                       
FF13: 18            CLC                       
FF14: 18            CLC                       
FF15: 00            BRK                       
FF16: 00            BRK                       
FF17: 00            BRK                       
FF18: 00            BRK                       
FF19: 00            BRK                       
FF1A: 18            CLC                       
FF1B: 3C            
FF1C: 3C            
FF1D: 18            CLC                       
FF1E: 00            BRK                       
FF1F: 00            BRK                       
FF20: 00            BRK                       
FF21: 18            CLC                       
FF22: 3C            
FF23: 7E 7E 3C      ROR   $3C7E,X             
FF26: 18            CLC                       
FF27: 00            BRK                       
FF28: 18            CLC                       
FF29: 3C            
FF2A: 7E FF FF      ROR   $FFFF,X             
FF2D: 7E 3C 18      ROR   $183C,X             
FF30: 00            BRK                       
FF31: 00            BRK                       
FF32: 00            BRK                       
FF33: 00            BRK                       
FF34: 00            BRK                       
FF35: 00            BRK                       
FF36: 00            BRK                       
FF37: 00            BRK                       
FF38: FF            
FF39: FF            
FF3A: FF            
FF3B: 7E 7E 76      ROR   $767E,X             
FF3E: 36 26         ROL   $26,X               
FF40: 22            
FF41: 38            SEC                       
FF42: FF            
FF43: FF            
FF44: FF            
FF45: FF            
FF46: 7E 7E 76      ROR   $767E,X             
FF49: 36 26         ROL   $26,X               
FF4B: 22            
FF4C: FF            
FF4D: FF            
FF4E: FF            
FF4F: 7E FF FF      ROR   $FFFF,X             
FF52: 7E 7E 00      ROR   $007E,X             
FF55: FF            
FF56: FF            
FF57: 3C            
FF58: 3C            
FF59: FF            
FF5A: FF            
FF5B: 7E 00 00      ROR   $0000,X             
FF5E: FF            
FF5F: 18            CLC                       
FF60: 18            CLC                       
FF61: 18            CLC                       
FF62: DB            
FF63: FF            
FF64: FF            
FF65: 7E 00 FF      ROR   $FF00,X             
FF68: 18            CLC                       
FF69: 18            CLC                       
FF6A: 18            CLC                       
FF6B: 18            CLC                       
FF6C: 00            BRK                       
FF6D: 81 C3         STA   ($C3,X)             
FF6F: 7E FF 6D      ROR   $6DFF,X             
FF72: 00            BRK                       
FF73: 00            BRK                       
FF74: 00            BRK                       
FF75: 00            BRK                       
FF76: 00            BRK                       
FF77: 00            BRK                       
FF78: 00            BRK                       
FF79: 70 FF         BVS   $FF7A               ;
FF7B: 43            
FF7C: FF            
FF7D: 55 FF         EOR   $FF,X               
FF7F: E0 E0         CPX   #$E0                
FF81: E0 C0         CPX   #$C0                
FF83: C0 C0         CPY   #$C0                
FF85: 80            
FF86: 80            
FF87: 80            
FF88: 7C            
FF89: C6 E6         DEC   $E6                 ;
FF8B: D6 CE         DEC   $CE,X               
FF8D: C6 7C         DEC   $7C                 ;
FF8F: FC            
FF90: 30 30         BMI   $FFC2               ;
FF92: 30 30         BMI   $FFC4               ;
FF94: 70 30         BVS   $FFC6               ;
FF96: FE E0 78      INC   $78E0,X             
FF99: 3C            
FF9A: 0E C6 7C      ASL   $7CC6               ;
FF9D: 7C            
FF9E: C6 06         DEC   $06                 ;
FFA0: 3C            
FFA1: 18            CLC                       
FFA2: 0C            
FFA3: 7E 0C 0C      ROR   $0C0C,X             
FFA6: FE CC 6C      INC   $6CCC,X             
FFA9: 3C            
FFAA: 1C            
FFAB: 7C            
FFAC: C6 06         DEC   $06                 ;
FFAE: 06 FC         ASL   $FC                 ;
FFB0: C0 FC         CPY   #$FC                
FFB2: 7C            
FFB3: C6 C6         DEC   $C6                 ;
FFB5: FC            
FFB6: C0 60         CPY   #$60                
FFB8: 3C            
FFB9: 30 30         BMI   $FFEB               ;
FFBB: 30 18         BMI   $FFD5               ;
FFBD: 0C            
FFBE: C6 FE         DEC   $FE                 ;
FFC0: 7C            
FFC1: C6 C6         DEC   $C6                 ;
FFC3: 7C            
FFC4: C6 C6         DEC   $C6                 ;
FFC6: 7C            
FFC7: 78            SEI                       
FFC8: 0C            
FFC9: 06 7E         ASL   $7E                 ;
FFCB: C6 C6         DEC   $C6                 ;
FFCD: 7C            
FFCE: AA            TAX                       
FFCF: 54            
FFD0: 28            PLP                       
FFD1: 10 A8         BPL   $FF7B               ;
FFD3: 54            
FFD4: 28            PLP                       
FFD5: 10 A0         BPL   $FF77               ;
FFD7: 54            
FFD8: 28            PLP                       
FFD9: 10 80         BPL   $FF5B               ;
FFDB: 54            
FFDC: 28            PLP                       
FFDD: 10 00         BPL   $FFDF               ;
FFDF: 54            
FFE0: 28            PLP                       
FFE1: 10 00         BPL   $FFE3               ;
FFE3: 50 28         BVC   $1000D              ;
FFE5: 10 00         BPL   $FFE7               ;
FFE7: 40            RTI                       
FFE8: 28            PLP                       
FFE9: 10 00         BPL   $FFEB               ;
FFEB: 00            BRK                       
FFEC: 28            PLP                       
FFED: 10 00         BPL   $FFEF               ;
FFEF: 00            BRK                       
FFF0: 20 10 00      JSR   $0010               ;
FFF3: 00            BRK                       
FFF4: 00            BRK                       
FFF5: 10 00         BPL   $FFF7               ;
FFF7: 00            BRK                       
FFF8: 00            BRK                       
FFF9: 00            BRK                       
FFFA: 00            BRK                       

# Vectors 

Same as ET ... the vector bytes look swapped here

FFFB: F0 00         BEQ   $FFFD               ;
FFFD: F0 00         BEQ   $FFFF               ;
FFFF: F0 FF         BEQ   $10000              ;
