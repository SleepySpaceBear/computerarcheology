![Defender Bank 1](Defender.jpg)

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

# Bank1 

(write 1 to $D000)

```plainCode
;Small jump table
C000: 7E C0 06      JMP   $C006              ;
C003: 7E CC AD      JMP   $CCAD              ;

; in jump table
C006: BD D0 7C      JSR   $D07C              ;
C009: 86 FF         LDA   #$FF               ;
C00B: 97 BA         STA   <$BA               ;
C00D: BD E0 52      JSR   $E052              ;
C010: 96 37         LDA   <$37               ;
C012: B7 A1 83      STA   $A183              ;
C015: 4F            CLRA                     ;
C016: B7 A1 84      STA   $A184              ;
C019: B7 A1 78      STA   $A178              ;
C01C: 96 B7         LDA   <$B7               ;
C01E: 10 27 06 55   LBEQ  $C677              ;
C022: 8E C8 F4      LDX   #$C8F4             ;
C025: 86 00         LDA   #$00               ;
C027: BD D0 55      JSR   $D055              ;
C02A: 10 8E A1 C2   LDY   #$A1C2             ;
C02E: 86 01         LDA   #$01               ;
C030: 97 06         STA   <$06               ;
C032: 10 BF A1 7B   STY   $A17B              ;
C036: 8E B2 B4      LDX   #$B2B4             ;
C039: BD C1 47      JSR   $C147              ;
C03C: 10 24 00 EA   LBCC  $C12A              ;
C040: 7C A1 78      INC   $A178              ;
C043: BD F5 D1      JSR   VidMemClr          ;
C046: 96 06         LDA   <$06               ;
C048: 4A            DECA                     ;
C049: 26 05         BNE   $C050              ;
C04B: BD D8 DC      JSR   $D8DC              ;
C04E: 20 03         BRA   $C053              ;
C050: BD D8 EA      JSR   $D8EA              ;
C053: C6 85         LDB   #$85               ;
C055: D7 27         STB   <$27               ;
C057: 86 3E         LDA   #$3E               ;
C059: 8E B2 60      LDX   #$B260             ;
C05C: BD C1 47      JSR   $C147              ;
C05F: 24 02         BCC   $C063              ;
C061: 86 3D         LDA   #$3D               ;
C063: 8E CC 02      LDX   #$CC02             ;sound board I/O address
C066: C6 3F         LDB   #$3F               ;sending an interrupt to the sound board
C068: BD FF D4      JSR   WriteIOPortX       ;
C06B: C6 24         LDB   #$24               ;send sound code $24(36)
C06D: BD FF D4      JSR   WriteIOPortX       ;
C070: 5A            DECB                     ;time delay loop
C071: 26 FD         BNE   $C070              ;
C073: C6 3F         LDB   #$3F               ;send interrupt
C075: BD FF D4      JSR   WriteIOPortX       ;
C078: 1F 89         TFR   A,B                ;send $3E or $3D according to C flag result from Subr$C147
C07A: BD FF D4      JSR   WriteIOPortX       ;
C07D: CE C0 ED      LDU   #$C0ED             ;
C080: 96 06         LDA   <$06               ;
C082: 48            ASLA                     ;
C083: 33 C6         LEAU  A,U                ;
C085: 8E 3E 38      LDX   #$3E38             ;
C088: BD FF CE      JSR   CallOtherPageX     ;
C08B: C0 02                                  ;   $C002         ;
C08D: 02                                     ;page #2
C08E: CE C0 FD      LDU   #$C0FD             ;
C091: 8E 14 58      LDX   #$1458             ;
C094: BD FF CE      JSR   CallOtherPageX     ;
C097: C0 02                                  ;   $C002         ;
C099: 02                                     ;page #2
C09A: CC 41 2F      LDD   #$412F             ;
C09D: DD 00         STD   <$00               ;
C09F: 86 40         LDA   #$40               ;
C0A1: DD 02         STD   <$02               ;
C0A3: DD 04         STD   <$04               ;
C0A5: BD C1 58      JSR   $C158              ;
C0A8: 86 28         LDA   #$28               ;
C0AA: B7 A1 7D      STA   $A17D              ;
C0AD: 8E C1 DC      LDX   #$C1DC             ;
C0B0: 86 00         LDA   #$00               ;
C0B2: BD D0 55      JSR   $D055              ;
C0B5: 8E C1 E7      LDX   #$C1E7             ;
C0B8: 86 00         LDA   #$00               ;
C0BA: BD D0 55      JSR   $D055              ;
C0BD: 8E C1 FA      LDX   #$C1FA             ;
C0C0: 86 00         LDA   #$00               ;
C0C2: BD D0 55      JSR   $D055              ;
C0C5: 7F A1 7A      CLR   $A17A              ;
C0C8: BD C1 6B      JSR   $C16B              ;
C0CB: 4F            CLRA                     ;
C0CC: B7 A1 86      STA   $A186              ;
C0CF: B7 A1 85      STA   $A185              ;
C0D2: 86 01         LDA   #$01               ;
C0D4: 8E C0 DA      LDX   #$C0DA             ;
C0D7: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C0DA: 96 7B         LDA   <$7B               ;
C0DC: 85 01         BITA  #$01               ;
C0DE: 26 14         BNE   $C0F4              ;
C0E0: 7D A1 7D      TST   $A17D              ;
C0E3: 27 29         BEQ   $C10E              ;
C0E5: 7C A1 86      INC   $A186              ;
C0E8: B6 A1 86      LDA   $A186              ;
C0EB: 81 05         CMPA  #$05               ;
C0ED: 26 E3         BNE   $C0D2              ;
C0EF: B7 A1 85      STA   $A185              ;
C0F2: 20 DE         BRA   $C0D2              ;
C0F4: 7F A1 86      CLR   $A186              ;
C0F7: 7D A1 85      TST   $A185              ;
C0FA: 27 D6         BEQ   $C0D2              ;
C0FC: 86 14         LDA   #$14               ;
C0FE: B7 A1 7D      STA   $A17D              ;
C101: 7C A1 7A      INC   $A17A              ;
C104: BD C1 6B      JSR   $C16B              ;
C107: B6 A1 7A      LDA   $A17A              ;
C10A: 81 03         CMPA  #$03               ;
C10C: 26 BD         BNE   $C0CB              ;
C10E: BD D0 7C      JSR   $D07C              ;
C111: 8E B2 A8      LDX   #$B2A8             ;
C114: CE B2 54      LDU   #$B254             ;
C117: BD C1 94      JSR   $C194              ;
C11A: 8E C4 71      LDX   #$C471             ;
C11D: 8D 28         BSR   $C147              ;
C11F: 24 09         BCC   $C12A              ;
C121: 8E C4 65      LDX   #$C465             ;
C124: CE C4 11      LDU   #$C411             ;
C127: BD C1 94      JSR   $C194              ;
C12A: 10 8E A1 FF   LDY   #$A1FF             ;
C12E: 96 06         LDA   <$06               ;
C130: 4C            INCA                     ;
C131: 81 03         CMPA  #$03               ;
C133: 10 26 FE F9   LBNE  $C030              ;
C137: 7D A1 78      TST   $A178              ;
C13A: 26 08         BNE   $C144              ;
C13C: 86 FF         LDA   #$FF               ;
C13E: 8E C1 44      LDX   #$C144             ;
C141: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C144: 7E C2 63      JMP   $C263              ;



;SUBRTN
C147: 34 16         PSHS  X,B,A              ;
C149: BD F8 38      JSR   SRAMWordRd         ;
C14C: 10 A3 21      CMPD  1,Y                ;
C14F: 26 05         BNE   $C156              ;
C151: BD F8 22      JSR   RdSRAMbyte         ;
C154: A1 23         CMPA  3,Y                ;
C156: 35 96         PULS  A,B,X,PC           ;

;SUBRTN
C158: 8E 46 AC      LDX   #$46AC             ;
C15B: CC 14 08      LDD   #$1408             ;
C15E: BD F5 C7      JSR   ScrnBlkClr         ;
C161: CE C0 FF      LDU   #$C0FF             ;
C164: BD FF CE      JSR   CallOtherPageX     ;
C167: C0 02                                  ;   $C002         ;
C169: 02                                     ;page #2
C16A: 39            RTS                      ;

;SUBRTN
C16B: 7F A1 62      CLR   $A162              ;
C16E: 8E 45 B7      LDX   #$45B7             ;
C171: CE 11 11      LDU   #$1111             ;
C174: B6 A1 62      LDA   $A162              ;
C177: B1 A1 7A      CMPA  $A17A              ;
C17A: 26 03         BNE   $C17F              ;
C17C: CE DD DD      LDU   #$DDDD             ;
C17F: CC 04 00      LDD   #$0400             ;
C182: EF 8B         STU   D,X                ;
C184: 4A            DECA                     ;
C185: 26 FB         BNE   $C182              ;
C187: 7C A1 62      INC   $A162              ;
C18A: 30 89 08 00   LEAX  $0800,X            ;
C18E: 8C 5D B7      CMPX  #$5DB7             ;
C191: 26 DE         BNE   $C171              ;
C193: 39            RTS                      ;

;SUBRTN
C194: FF A1 64      STU   $A164              ;
C197: 10 BE A1 7B   LDY   $A17B              ;
C19B: 8D AA         BSR   $C147              ;
C19D: 24 09         BCC   $C1A8              ;
C19F: 8D 24         BSR   $C1C5              ;
C1A1: 30 14         LEAX  -12,X              ;
C1A3: BC A1 64      CMPX  $A164              ;
C1A6: 22 F3         BHI   $C19B              ;
C1A8: 30 0C         LEAX  12,X               ;
C1AA: EC 21         LDD   1,Y                ;
C1AC: BD F8 64      JSR   SRAMWordWr         ;
C1AF: A6 23         LDA   3,Y                ;
C1B1: BD F8 4E      JSR   WrSRAMbyte         ;
C1B4: CE A0 00      LDU   #$A000             ;
C1B7: A6 C4         LDA   ,U                 ;
C1B9: BD F8 4E      JSR   WrSRAMbyte         ;
C1BC: 33 42         LEAU  2,U                ;
C1BE: 11 83 A0 06   CMPU  #$A006             ;
C1C2: 26 F3         BNE   $C1B7              ;
C1C4: 39            RTS                      ;

;SUBRTN
C1C5: 34 10         PSHS  X                  ;
C1C7: BD F8 38      JSR   SRAMWordRd         ;
C1CA: 30 08         LEAX  8,X                ;
C1CC: BD F8 64      JSR   SRAMWordWr         ;
C1CF: 30 88 E8      LEAX  $-18,X             ;
C1D2: AC E4         CMPX  ,S                 ;
C1D4: 27 04         BEQ   $C1DA              ;
C1D6: 30 0C         LEAX  12,X               ;
C1D8: 20 ED         BRA   $C1C7              ;
C1DA: 35 90         PULS  X,PC               ;
C1DC: 7A A1 7D      DEC   $A17D              ;
C1DF: 86 3C         LDA   #$3C               ;
C1E1: 8E C1 DC      LDX   #$C1DC             ;
C1E4: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C1E7: 96 33         LDA   <$33               ;
C1E9: 26 04         BNE   $C1EF              ;
C1EB: 96 27         LDA   <$27               ;
C1ED: 20 01         BRA   $C1F0              ;
C1EF: 4F            CLRA                     ;
C1F0: 97 33         STA   <$33               ;
C1F2: 86 0F         LDA   #$0F               ;
C1F4: 8E C1 E7      LDX   #$C1E7             ;
C1F7: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C1FA: 7F A1 79      CLR   $A179              ;
C1FD: 96 7B         LDA   <$7B               ;
C1FF: 85 80         BITA  #$80               ;
C201: 27 04         BEQ   $C207              ;
C203: 86 FF         LDA   #$FF               ;
C205: 20 0F         BRA   $C216              ;
C207: 96 7D         LDA   <$7D               ;
C209: 85 01         BITA  #$01               ;
C20B: 27 04         BEQ   $C211              ;
C20D: 86 01         LDA   #$01               ;
C20F: 20 05         BRA   $C216              ;
C211: 7F A1 79      CLR   $A179              ;
C214: 20 34         BRA   $C24A              ;
C216: B1 A1 79      CMPA  $A179              ;
C219: 26 37         BNE   $C252              ;
C21B: 7A A1 7F      DEC   $A17F              ;
C21E: 26 2A         BNE   $C24A              ;
C220: 8E A0 00      LDX   #$A000             ;
C223: F6 A1 7A      LDB   $A17A              ;
C226: 58            ASLB                     ;
C227: 3A            ABX                      ;
C228: A6 84         LDA   ,X                 ;
C22A: BB A1 79      ADDA  $A179              ;
C22D: 81 3F         CMPA  #$3F               ;
C22F: 26 02         BNE   $C233              ;
C231: 86 5A         LDA   #$5A               ;
C233: 81 5B         CMPA  #$5B               ;
C235: 26 02         BNE   $C239              ;
C237: 86 40         LDA   #$40               ;
C239: A7 84         STA   ,X                 ;
C23B: BD C1 58      JSR   $C158              ;
C23E: B6 A1 7E      LDA   $A17E              ;
C241: 44            LSRA                     ;
C242: 8B 05         ADDA  #$05               ;
C244: B7 A1 7E      STA   $A17E              ;
C247: B7 A1 7F      STA   $A17F              ;
C24A: 86 01         LDA   #$01               ;
C24C: 8E C1 FD      LDX   #$C1FD             ;
C24F: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C252: B7 A1 79      STA   $A179              ;
C255: 86 37         LDA   #$37               ;
C257: B7 A1 7E      STA   $A17E              ;
C25A: 86 03         LDA   #$03               ;
C25C: B7 A1 7F      STA   $A17F              ;
C25F: 20 E9         BRA   $C24A              ;
C261: DE FF         LDU   <$FF               ;
C263: 7F A1 62      CLR   $A162              ;
C266: BD D0 7C      JSR   $D07C              ;
C269: BD C8 6F      JSR   $C86F              ;
C26C: BD F5 D1      JSR   VidMemClr          ;
C26F: BD D8 DC      JSR   $D8DC              ;
C272: 0F 27         CLR   <$27               ;
C274: 8E C8 F4      LDX   #$C8F4             ;
C277: 86 00         LDA   #$00               ;
C279: BD D0 55      JSR   $D055              ;
C27C: BD C9 36      JSR   $C936              ;
C27F: CE C1 01      LDU   #$C101             ;
C282: 8E 38 54      LDX   #$3854             ;
C285: BD FF CE      JSR   CallOtherPageX     ;
C288: C0 02                                  ;   $C002          ;
C28A: 02                                     ;page #2
C28B: CE 11 11      LDU   #$1111             ;
C28E: 8E 1E 7B      LDX   #$1E7B             ;
C291: CC 5F 00      LDD   #$5F00             ;
C294: EF 8B         STU   D,X                ;
C296: 81 41         CMPA  #$41               ;
C298: 26 02         BNE   $C29C              ;
C29A: 86 1F         LDA   #$1F               ;
C29C: 4A            DECA                     ;
C29D: 2A F5         BPL   $C294              ;
C29F: 86 2F         LDA   #$2F               ;
C2A1: 97 07         STA   <$07               ;
C2A3: 97 0B         STA   <$0B               ;
C2A5: 97 12         STA   <$12               ;
C2A7: CE C1 03      LDU   #$C103             ;
C2AA: 8E 18 86      LDX   #$1886             ;
C2AD: BF A1 81      STX   $A181              ;
C2B0: 8E B2 60      LDX   #$B260             ;
C2B3: BF A1 64      STX   $A164              ;
C2B6: 8D 4E         BSR   $C306              ;
C2B8: 8E 59 86      LDX   #$5986             ;
C2BB: BF A1 81      STX   $A181              ;
C2BE: 8E C4 1D      LDX   #$C41D             ;
C2C1: BF A1 64      STX   $A164              ;
C2C4: 8D 40         BSR   $C306              ;
C2C6: 86 3F         LDA   #$3F               ;
C2C8: 97 32         STA   <$32               ;
C2CA: 10 8E B3 00   LDY   #$B300             ;
C2CE: CC 3C 18      LDD   #$3C18             ;
C2D1: ED A4         STD   ,Y                 ;
C2D3: CC B4 12      LDD   #$B412             ;
C2D6: ED 22         STD   2,Y                ;
C2D8: CC 30 38      LDD   #$3038             ;
C2DB: BD F5 22      JSR   $F522              ;
C2DE: 8E E7 82      LDX   #$E782             ;
C2E1: 86 00         LDA   #$00               ;
C2E3: BD D0 55      JSR   $D055              ;
C2E6: 86 3C         LDA   #$3C               ;
C2E8: B7 A1 7D      STA   $A17D              ;
C2EB: 7D A1 84      TST   $A184              ;
C2EE: 26 14         BNE   $C304              ;
C2F0: 7D A1 62      TST   $A162              ;
C2F3: 10 26 FF 6C   LBNE  $C263              ;
C2F7: 7A A1 7D      DEC   $A17D              ;
C2FA: 27 08         BEQ   $C304              ;
C2FC: 86 0A         LDA   #$0A               ;
C2FE: 8E C2 EB      LDX   #$C2EB             ;
C301: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C304: 20 4B         BRA   $C351              ;

;SUBRTN
C306: 86 31         LDA   #$31               ;
C308: 97 06         STA   <$06               ;
C30A: 4F            CLRA                     ;
C30B: 10 8E A0 0C   LDY   #$A00C             ;
C30F: BE A1 64      LDX   $A164              ;
C312: BD FF D7      JSR   ReadIOPortX        ;
C315: 30 01         LEAX  1,X                ;
C317: C4 0F         ANDB  #$0F               ;
C319: 26 07         BNE   $C322              ;
C31B: 4D            TSTA                     ;
C31C: 26 04         BNE   $C322              ;
C31E: C6 40         LDB   #$40               ;
C320: 20 03         BRA   $C325              ;
C322: 4C            INCA                     ;
C323: CB 30         ADDB  #$30               ;
C325: E7 A0         STB   ,Y+                ;
C327: 10 8C A0 12   CMPY  #$A012             ;
C32B: 26 E5         BNE   $C312              ;
C32D: BD F8 38      JSR   SRAMWordRd         ;
C330: DD 08         STD   <$08               ;
C332: BD F8 22      JSR   RdSRAMbyte         ;
C335: 97 0A         STA   <$0A               ;
C337: BF A1 64      STX   $A164              ;
C33A: BE A1 81      LDX   $A181              ;
C33D: BD FF CE      JSR   CallOtherPageX     ;
C340: C0 02                                  ;   $C002          ;
C342: 02                                     ;page #2
C343: 30 0A         LEAX  10,X               ;
C345: BF A1 81      STX   $A181              ;
C348: 0C 06         INC   <$06               ;
C34A: 96 06         LDA   <$06               ;
C34C: 81 39         CMPA  #$39               ;
C34E: 26 BA         BNE   $C30A              ;
C350: 39            RTS                      ;

C351: BD D0 7C      JSR   $D07C              ;
C354: BD C4 3C      JSR   $C43C              ;
C357: 86 D9         LDA   #$D9               ;
C359: 97 BA         STA   <$BA               ;
C35B: BD C9 36      JSR   $C936              ;
C35E: 8E C8 F4      LDX   #$C8F4             ;
C361: 86 00         LDA   #$00               ;
C363: BD D0 55      JSR   $D055              ;
C366: BD D6 BC      JSR   $D6BC              ;
C369: 8E CC 63      LDX   #$CC63             ;
C36C: BF A1 96      STX   $A196              ;
C36F: 8E E7 82      LDX   #$E782             ;
C372: 86 00         LDA   #$00               ;
C374: BD D0 55      JSR   $D055              ;
C377: 8E F4 64      LDX   #$F464             ;
C37A: 86 00         LDA   #$00               ;
C37C: BD D0 55      JSR   $D055              ;
C37F: 8E F4 3D      LDX   #$F43D             ;
C382: 86 00         LDA   #$00               ;
C384: BD D0 55      JSR   $D055              ;
C387: 8E E9 E3      LDX   #$E9E3             ;
C38A: 86 00         LDA   #$00               ;
C38C: BD D0 55      JSR   $D055              ;
C38F: 8E C6 4F      LDX   #$C64F             ;
C392: 86 00         LDA   #$00               ;
C394: BD D0 55      JSR   $D055              ;
C397: BD D0 AD      JSR   $D0AD              ;
C39A: CC 00 00      LDD   #$0000             ;
C39D: ED 0E         STD   14,X               ;
C39F: ED 88 10      STD   $10,X              ;
C3A2: CC 1E 00      LDD   #$1E00             ;
C3A5: ED 0A         STD   10,X               ;
C3A7: CC DB 00      LDD   #$DB00             ;
C3AA: ED 0C         STD   12,X               ;
C3AC: CC F9 01      LDD   #$F901             ;
C3AF: ED 02         STD   2,X                ;
C3B1: 9F 65         STX   <$65               ;
C3B3: CC 66 66      LDD   #$6666             ;
C3B6: ED 88 12      STD   $12,X              ;
C3B9: BF A1 89      STX   $A189              ;
C3BC: BD D0 AD      JSR   $D0AD              ;
C3BF: CC 00 00      LDD   #$0000             ;
C3C2: ED 0E         STD   14,X               ;
C3C4: ED 88 10      STD   $10,X              ;
C3C7: CC 08 00      LDD   #$0800             ;
C3CA: ED 0A         STD   10,X               ;
C3CC: CC 50 00      LDD   #$5000             ;
C3CF: ED 0C         STD   12,X               ;
C3D1: CC F9 C1      LDD   #$F9C1             ;
C3D4: ED 02         STD   2,X                ;
C3D6: 9F 65         STX   <$65               ;
C3D8: CC 00 00      LDD   #$0000             ;
C3DB: ED 88 12      STD   $12,X              ;
C3DE: BF A1 8B      STX   $A18B              ;
C3E1: BD D0 AD      JSR   $D0AD              ;
C3E4: CC F9 85      LDD   #$F985             ;
C3E7: ED 02         STD   2,X                ;
C3E9: CC 1D A0      LDD   #$1DA0             ;
C3EC: ED 0A         STD   10,X               ;
C3EE: CC 40 00      LDD   #$4000             ;
C3F1: ED 0C         STD   12,X               ;
C3F3: CC 00 A0      LDD   #$00A0             ;
C3F6: ED 88 10      STD   $10,X              ;
C3F9: CC 00 00      LDD   #$0000             ;
C3FC: ED 0E         STD   14,X               ;
C3FE: CC 44 33      LDD   #$4433             ;
C401: ED 88 12      STD   $12,X              ;
C404: BD FC 60      JSR   $FC60              ;"JSR  $FC69" would have been faster
C407: BF A1 8D      STX   $A18D              ;
C40A: 86 E6         LDA   #$E6               ;
C40C: 8E C4 12      LDX   #$C412             ;
C40F: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C412: CC FF 50      LDD   #$FF50             ;
C415: BE A1 8D      LDX   $A18D              ;
C418: ED 88 10      STD   $10,X              ;
C41B: BE A1 89      LDX   $A189              ;
C41E: ED 88 10      STD   $10,X              ;
C421: 86 A0         LDA   #$A0               ;
C423: 8E C4 29      LDX   #$C429             ;
C426: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C429: 8E C5 F5      LDX   #$C5F5             ;
C42C: 86 00         LDA   #$00               ;
C42E: BD D0 55      JSR   $D055              ;
C431: BF A1 87      STX   $A187              ;
C434: 86 15         LDA   #$15               ;
C436: 8E C4 75      LDX   #$C475             ;
C439: 7E F4 BE      JMP   InsEventLnkPgSav   ;

;SUBRTN
C43C: 86 FF         LDA   #$FF               ;
C43E: 97 BA         STA   <$BA               ;
C440: BD D8 05      JSR   $D805              ;
C443: BD F5 D1      JSR   VidMemClr          ;
C446: CC 00 00      LDD   #$0000             ;
C449: DD 20         STD   <$20               ;
C44B: DD 22         STD   <$22               ;
C44D: BD FF CE      JSR   CallOtherPageX     ;
C450: F4 FA                                  ;   $F4FA
C452: 00                                     ;page #0?
C453: BD D7 F5      JSR   $D7F5              ;
C456: 86 DB         LDA   #$DB               ;
C458: 97 BA         STA   <$BA               ;
C45A: 8E 10 30      LDX   #$1030             ;
C45D: 9F BF         STX   <$BF               ;
C45F: 39            RTS                      ;

;SUBRTN
C460: BE A1 87      LDX   $A187              ;
C463: FE A1 94      LDU   $A194              ;
C466: 4F            CLRA                     ;
C467: A7 C4         STA   ,U                 ;
C469: 33 C9 01 00   LEAU  $0100,U            ;
C46D: 11 A3 07      CMPU  7,X                ;
C470: 23 F5         BLS   $C467              ;
C472: 7E D0 15      JMP   $D015              ;
C475: 8D E9         BSR   $C460              ;
C477: BE A1 8D      LDX   $A18D              ;
C47A: BD D0 C7      JSR   $D0C7              ;
C47D: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
C480: BE A1 8B      LDX   $A18B              ;
C483: CC 00 40      LDD   #$0040             ;
C486: ED 0E         STD   14,X               ;
C488: CC 00 D4      LDD   #$00D4             ;
C48B: ED 88 10      STD   $10,X              ;
C48E: 86 2D         LDA   #$2D               ;
C490: B7 A1 8F      STA   $A18F              ;
C493: BE A1 89      LDX   $A189              ;
C496: CC 00 00      LDD   #$0000             ;
C499: ED 88 10      STD   $10,X              ;
C49C: BE A1 89      LDX   $A189              ;
C49F: EC 88 10      LDD   $10,X              ;
C4A2: C3 00 08      ADDD  #$0008             ;
C4A5: ED 88 10      STD   $10,X              ;
C4A8: 7A A1 8F      DEC   $A18F              ;
C4AB: 27 08         BEQ   $C4B5              ;
C4AD: 86 02         LDA   #$02               ;
C4AF: 8E C4 9C      LDX   #$C49C             ;
C4B2: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C4B5: BD D0 AD      JSR   $D0AD              ;
C4B8: CC 00 00      LDD   #$0000             ;
C4BB: ED 0E         STD   14,X               ;
C4BD: ED 88 10      STD   $10,X              ;
C4C0: CC 1D FF      LDD   #$1DFF             ;
C4C3: ED 0A         STD   10,X               ;
C4C5: CC 90 00      LDD   #$9000             ;
C4C8: ED 0C         STD   12,X               ;
C4CA: CC F9 E7      LDD   #$F9E7             ;
C4CD: ED 02         STD   2,X                ;
C4CF: 9F 65         STX   <$65               ;
C4D1: CC 00 00      LDD   #$0000             ;
C4D4: ED 88 12      STD   $12,X              ;
C4D7: BF A1 90      STX   $A190              ;
C4DA: CC 00 00      LDD   #$0000             ;
C4DD: CE 00 C0      LDU   #$00C0             ;
C4E0: BE A1 8B      LDX   $A18B              ;
C4E3: ED 0E         STD   14,X               ;
C4E5: EF 88 10      STU   $10,X              ;
C4E8: BE A1 89      LDX   $A189              ;
C4EB: CC 1E 80      LDD   #$1E80             ;
C4EE: ED 0A         STD   10,X               ;
C4F0: CC A2 E0      LDD   #$A2E0             ;
C4F3: ED 0C         STD   12,X               ;
C4F5: EF 88 10      STU   $10,X              ;
C4F8: 86 50         LDA   #$50               ;
C4FA: 8E C5 00      LDX   #$C500             ;
C4FD: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C500: BE A1 90      LDX   $A190              ;
C503: CC E0 00      LDD   #$E000             ;
C506: ED 0C         STD   12,X               ;
C508: CC 1C 00      LDD   #$1C00             ;
C50B: ED 0A         STD   10,X               ;
C50D: BE A1 89      LDX   $A189              ;
C510: CC 00 00      LDD   #$0000             ;
C513: ED 88 10      STD   $10,X              ;
C516: BE A1 8B      LDX   $A18B              ;
C519: CC F9 CB      LDD   #$F9CB             ;
C51C: ED 02         STD   2,X                ;
C51E: CC FF C0      LDD   #$FFC0             ;
C521: ED 0E         STD   14,X               ;
C523: CC FE 80      LDD   #$FE80             ;
C526: ED 88 10      STD   $10,X              ;
C529: 86 60         LDA   #$60               ;
C52B: 8E C5 31      LDX   #$C531             ;
C52E: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C531: BE A1 8B      LDX   $A18B              ;
C534: CC F9 C1      LDD   #$F9C1             ;
C537: ED 02         STD   2,X                ;
C539: CC 00 00      LDD   #$0000             ;
C53C: ED 0E         STD   14,X               ;
C53E: ED 88 10      STD   $10,X              ;
C541: BE A1 90      LDX   $A190              ;
C544: EC 04         LDD   4,X                ;
C546: BD D0 C7      JSR   $D0C7              ;
C549: BD D3 50      JSR   $D350              ;
C54C: CE CC 7D      LDU   #$CC7D             ;
C54F: BD D0 AD      JSR   $D0AD              ;
C552: EC C9 00 0C   LDD   $000C,U            ;
C556: ED 02         STD   2,X                ;
C558: EC C9 00 24   LDD   $0024,U            ;
C55C: ED 88 12      STD   $12,X              ;
C55F: CC 1F 00      LDD   #$1F00             ;
C562: ED 0A         STD   10,X               ;
C564: CC A0 00      LDD   #$A000             ;
C567: ED 0C         STD   12,X               ;
C569: CC FF 40      LDD   #$FF40             ;
C56C: ED 88 10      STD   $10,X              ;
C56F: CC 00 00      LDD   #$0000             ;
C572: ED 0E         STD   14,X               ;
C574: BD FC 60      JSR   $FC60              ;"JSR  $FC69" would have been faster
C577: FF A1 92      STU   $A192              ;
C57A: BF A1 8D      STX   $A18D              ;
C57D: 86 5F         LDA   #$5F               ;
C57F: 8E C5 85      LDX   #$C585             ;
C582: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C585: 8E C5 F5      LDX   #$C5F5             ;
C588: 86 00         LDA   #$00               ;
C58A: BD D0 55      JSR   $D055              ;
C58D: BF A1 87      STX   $A187              ;
C590: 86 17         LDA   #$17               ;
C592: 8E C5 98      LDX   #$C598             ;
C595: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C598: BD C4 60      JSR   $C460              ;
C59B: BE A1 8D      LDX   $A18D              ;
C59E: BD D0 C7      JSR   $D0C7              ;
C5A1: BD D0 AD      JSR   $D0AD              ;
C5A4: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
C5A7: FE A1 92      LDU   $A192              ;
C5AA: EC C9 00 18   LDD   $0018,U            ;
C5AE: ED 0A         STD   10,X               ;
C5B0: EC C1         LDD   ,U++               ;
C5B2: ED 0C         STD   12,X               ;
C5B4: CC 00 00      LDD   #$0000             ;
C5B7: ED 88 10      STD   $10,X              ;
C5BA: ED 0E         STD   14,X               ;
C5BC: BD FC 60      JSR   $FC60              ;"JSR  $FC69" would have been faster
C5BF: FF A1 92      STU   $A192              ;
C5C2: 86 20         LDA   #$20               ;
C5C4: 8E C5 CA      LDX   #$C5CA             ;
C5C7: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C5CA: BE A1 96      LDX   $A196              ;
C5CD: 30 02         LEAX  2,X                ;
C5CF: BF A1 96      STX   $A196              ;
C5D2: 86 20         LDA   #$20               ;
C5D4: 8E C5 DA      LDX   #$C5DA             ;
C5D7: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C5DA: FE A1 92      LDU   $A192              ;
C5DD: 11 83 CC 89   CMPU  #$CC89             ;
C5E1: 10 26 FF 6A   LBNE  $C54F              ;
C5E5: 86 FF         LDA   #$FF               ;
C5E7: 8E C5 ED      LDX   #$C5ED             ;
C5EA: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C5ED: 86 FF         LDA   #$FF               ;
C5EF: 8E C6 77      LDX   #$C677             ;
C5F2: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C5F5: BE A1 8B      LDX   $A18B              ;
C5F8: AE 04         LDX   4,X                ;
C5FA: 30 89 07 04   LEAX  $0704,X            ;
C5FE: AF 47         STX   7,U                ;
C600: AF 49         STX   9,U                ;
C602: BF A1 94      STX   $A194              ;
C605: 86 04         LDA   #$04               ;
C607: AE 47         LDX   7,U                ;
C609: C6 11         LDB   #$11               ;
C60B: E7 84         STB   ,X                 ;
C60D: 30 89 01 00   LEAX  $0100,X            ;
C611: 4A            DECA                     ;
C612: 26 F7         BNE   $C60B              ;
C614: C6 99         LDB   #$99               ;
C616: E7 84         STB   ,X                 ;
C618: AF 47         STX   7,U                ;
C61A: 10 9E A4      LDY   <$A4               ;
C61D: 10 8C A1 5F   CMPY  #$A15F             ;
C621: 25 04         BCS   $C627              ;
C623: 10 8E A1 42   LDY   #$A142             ;
C627: AE 49         LDX   9,U                ;
C629: 86 03         LDA   #$03               ;
C62B: E6 A0         LDB   ,Y+                ;
C62D: E7 84         STB   ,X                 ;
C62F: 30 89 01 00   LEAX  $0100,X            ;
C633: 4A            DECA                     ;
C634: 26 F5         BNE   $C62B              ;
C636: 10 9F A4      STY   <$A4               ;
C639: AF 49         STX   9,U                ;
C63B: BE A1 94      LDX   $A194              ;
C63E: 6F 84         CLR   ,X                 ;
C640: 30 89 01 00   LEAX  $0100,X            ;
C644: BF A1 94      STX   $A194              ;
C647: 86 01         LDA   #$01               ;
C649: 8E C6 05      LDX   #$C605             ;
C64C: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C64F: 10 8E CC 61   LDY   #$CC61             ;
C653: EE A9 00 0E   LDU   $000E,Y            ;
C657: AE A1         LDX   ,Y++               ;
C659: BD FF CE      JSR   CallOtherPageX     ;
C65C: C0 02                                  ;   $C002         ;
C65E: 02                                     ;page #2
C65F: 10 BF A1 98   STY   $A198              ;
C663: 86 06         LDA   #$06               ;
C665: 8E C6 6B      LDX   #$C66B             ;
C668: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C66B: 10 BE A1 98   LDY   $A198              ;
C66F: 10 BC A1 96   CMPY  $A196              ;
C673: 26 DE         BNE   $C653              ;
C675: 20 D8         BRA   $C64F              ;
C677: BD D0 7C      JSR   $D07C              ;
C67A: 7F A1 84      CLR   $A184              ;
C67D: 86 FB         LDA   #$FB               ;
C67F: 97 BA         STA   <$BA               ;
C681: BD F5 D1      JSR   VidMemClr          ;
C684: 0F 52         CLR   <$52               ;
C686: CC FF FF      LDD   #$FFFF             ;
C689: DD 59         STD   <$59               ;
C68B: 8E E7 82      LDX   #$E782             ;
C68E: 86 00         LDA   #$00               ;
C690: BD D0 55      JSR   $D055              ;
C693: 8E F4 3D      LDX   #$F43D             ;
C696: 86 00         LDA   #$00               ;
C698: BD D0 55      JSR   $D055              ;
C69B: 86 3F         LDA   #$3F               ;
C69D: 97 32         STA   <$32               ;
C69F: 7E C6 A2      JMP   $C6A2              ;what is this? a longer NOP?
C6A2: BD C8 6F      JSR   $C86F              ;
C6A5: 86 03         LDA   #$03               ;
C6A7: B7 A1 6A      STA   $A16A              ;
C6AA: 8E C9 41      LDX   #$C941             ;
C6AD: BF A1 6B      STX   $A16B              ;
C6B0: B6 A1 6A      LDA   $A16A              ;
C6B3: B7 A1 63      STA   $A163              ;
C6B6: 10 BE A1 6B   LDY   $A16B              ;
C6BA: A6 A0         LDA   ,Y+                ;
C6BC: 81 AA         CMPA  #$AA               ;
C6BE: 23 0E         BLS   $C6CE              ;
C6C0: 43            COMA                     ;
C6C1: 27 F7         BEQ   $C6BA              ;
C6C3: 4A            DECA                     ;
C6C4: 26 4B         BNE   $C711              ;
C6C6: EC A1         LDD   ,Y++               ;
C6C8: FD A1 66      STD   $A166              ;
C6CB: 4F            CLRA                     ;
C6CC: 20 18         BRA   $C6E6              ;
C6CE: 48            ASLA                     ;
C6CF: 24 03         BCC   $C6D4              ;
C6D1: 7A A1 66      DEC   $A166              ;
C6D4: 48            ASLA                     ;
C6D5: 24 03         BCC   $C6DA              ;
C6D7: 7C A1 66      INC   $A166              ;
C6DA: 48            ASLA                     ;
C6DB: 24 03         BCC   $C6E0              ;
C6DD: 7A A1 67      DEC   $A167              ;
C6E0: 48            ASLA                     ;
C6E1: 24 03         BCC   $C6E6              ;
C6E3: 7C A1 67      INC   $A167              ;
C6E6: B7 A1 62      STA   $A162              ;
C6E9: FC A1 66      LDD   $A166              ;
C6EC: 44            LSRA                     ;
C6ED: 1F 01         TFR   D,X                ;
C6EF: E6 84         LDB   ,X                 ;
C6F1: 25 04         BCS   $C6F7              ;
C6F3: CA F0         ORB   #$F0               ;
C6F5: 20 02         BRA   $C6F9              ;
C6F7: CA 0F         ORB   #$0F               ;
C6F9: E7 84         STB   ,X                 ;
C6FB: B6 A1 62      LDA   $A162              ;
C6FE: 26 CE         BNE   $C6CE              ;
C700: 7A A1 63      DEC   $A163              ;
C703: 26 B5         BNE   $C6BA              ;
C705: 10 BF A1 6B   STY   $A16B              ;
C709: 86 02         LDA   #$02               ;
C70B: 8E C6 B0      LDX   #$C6B0             ;
C70E: BD F4 BE      JSR   InsEventLnkPgSav   ;
C711: BF A1 68      STX   $A168              ;
C714: 86 03         LDA   #$03               ;
C716: B1 A1 6A      CMPA  $A16A              ;
C719: 26 0D         BNE   $C728              ;
C71B: 86 0A         LDA   #$0A               ;
C71D: B7 A1 6A      STA   $A16A              ;
C720: 8E C7 30      LDX   #$C730             ;
C723: 86 00         LDA   #$00               ;
C725: BD D0 55      JSR   $D055              ;
C728: 8E C9 41      LDX   #$C941             ;
C72B: BF A1 6B      STX   $A16B              ;
C72E: 20 80         BRA   $C6B0              ;
C730: 8E C7 4C      LDX   #$C74C             ;
C733: 86 00         LDA   #$00               ;
C735: BD D0 55      JSR   $D055              ;
C738: 8E 32 58      LDX   #$3258             ;
C73B: CE C0 ED      LDU   #$C0ED             ;
C73E: BD FF CE      JSR   CallOtherPageX     ;
C741: C0 02                                  ;   $C002          ;
C743: 02                                     ;page #2
C744: 86 05         LDA   #$05               ;
C746: 8E C7 38      LDX   #$C738             ;
C749: BD F4 BE      JSR   InsEventLnkPgSav   ;
C74C: 86 30         LDA   #$30               ;
C74E: 8E C7 54      LDX   #$C754             ;
C751: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C754: CC B3 D6      LDD   #$B3D6             ;
C757: FD A1 6D      STD   $A16D              ;
C75A: CC B4 12      LDD   #$B412             ;
C75D: FD A1 6F      STD   $A16F              ;
C760: CC 00 00      LDD   #$0000             ;
C763: DD 20         STD   <$20               ;
C765: CC 0C 00      LDD   #$0C00             ;
C768: FD A1 71      STD   $A171              ;
C76B: CC B3 04      LDD   #$B304             ;
C76E: FD A1 73      STD   $A173              ;
C771: BE A1 73      LDX   $A173              ;
C774: 10 BE A1 6D   LDY   $A16D              ;
C778: CC 04 0C      LDD   #$040C             ;
C77B: ED A4         STD   ,Y                 ;
C77D: FC A1 6F      LDD   $A16F              ;
C780: ED 22         STD   2,Y                ;
C782: C3 00 60      ADDD  #$0060             ;
C785: FD A1 6F      STD   $A16F              ;
C788: 10 AF 02      STY   2,X                ;
C78B: FC A1 71      LDD   $A171              ;
C78E: ED 0A         STD   10,X               ;
C790: C3 01 00      ADDD  #$0100             ;
C793: FD A1 71      STD   $A171              ;
C796: CC 98 00      LDD   #$9800             ;
C799: ED 0C         STD   12,X               ;
C79B: BD FC 60      JSR   $FC60              ;"JSR  $FC69" would have been faster
C79E: 30 0E         LEAX  14,X               ;
C7A0: BF A1 73      STX   $A173              ;
C7A3: 31 24         LEAY  4,Y                ;
C7A5: 10 BF A1 6D   STY   $A16D              ;
C7A9: 10 8C B4 12   CMPY  #$B412             ;
C7AD: 26 C2         BNE   $C771              ;
C7AF: 86 2E         LDA   #$2E               ;
C7B1: 8E C7 B7      LDX   #$C7B7             ;
C7B4: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C7B7: 8E B3 00      LDX   #$B300             ;
C7BA: CC 3C 18      LDD   #$3C18             ;
C7BD: ED 84         STD   ,X                 ;
C7BF: CC B4 12      LDD   #$B412             ;
C7C2: ED 02         STD   2,X                ;
C7C4: 8E C8 48      LDX   #$C848             ;
C7C7: 86 00         LDA   #$00               ;
C7C9: BD D0 55      JSR   $D055              ;
C7CC: 86 28         LDA   #$28               ;
C7CE: 8E C7 D4      LDX   #$C7D4             ;
C7D1: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C7D4: 8E F4 64      LDX   #$F464             ;
C7D7: 86 00         LDA   #$00               ;
C7D9: BD D0 55      JSR   $D055              ;
C7DC: FE A1 68      LDU   $A168              ;
C7DF: 10 8E CC 11   LDY   #$CC11             ;
C7E3: 8E 3B D0      LDX   #$3BD0             ;
C7E6: EC A1         LDD   ,Y++               ;
C7E8: FD A1 64      STD   $A164              ;
C7EB: 86 01         LDA   #$01               ;
C7ED: 5F            CLRB                     ;
C7EE: B5 A1 64      BITA  $A164              ;
C7F1: 27 02         BEQ   $C7F5              ;
C7F3: C6 10         LDB   #$10               ;
C7F5: B5 A1 65      BITA  $A165              ;
C7F8: 27 02         BEQ   $C7FC              ;
C7FA: CA 01         ORB   #$01               ;
C7FC: E7 80         STB   ,X+                ;
C7FE: 48            ASLA                     ;
C7FF: 26 EC         BNE   $C7ED              ;
C801: 30 89 00 F8   LEAX  $00F8,X            ;
C805: 10 8C CC 61   CMPY  #$CC61             ;
C809: 26 DB         BNE   $C7E6              ;
C80B: 8E A0 26      LDX   #$A026             ;
C80E: F6 C6 F8      LDB   $C6F8              ;
C811: A6 85         LDA   B,X                ;
C813: 43            COMA                     ;
C814: 84 07         ANDA  #$07               ;
C816: 26 08         BNE   $C820              ;
C818: 8E 80 18      LDX   #$8018             ;
C81B: CC 20 A0      LDD   #$20A0             ;
C81E: EF 8B         STU   D,X                ;
C820: 86 01         LDA   #$01               ;
C822: 97 B7         STA   <$B7               ;
C824: 8E C8 F4      LDX   #$C8F4             ;
C827: 86 00         LDA   #$00               ;
C829: BD D0 55      JSR   $D055              ;
C82C: 86 3C         LDA   #$3C               ;
C82E: B7 A1 7D      STA   $A17D              ;
C831: 7D A1 84      TST   $A184              ;
C834: 10 26 FB 19   LBNE  $C351              ;
C838: 7A A1 7D      DEC   $A17D              ;
C83B: 27 08         BEQ   $C845              ;
C83D: 86 0A         LDA   #$0A               ;
C83F: 8E C8 31      LDX   #$C831             ;
C842: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C845: 7E C2 63      JMP   $C263              ;
C848: 10 8E B3 00   LDY   #$B300             ;
C84C: CC 30 90      LDD   #$3090             ;
C84F: BD F5 22      JSR   $F522              ;
C852: 7D 9C 00      TST   $9C00              ;
C855: 26 10         BNE   $C867              ;
C857: 7D 9C 40      TST   $9C40              ;
C85A: 26 0B         BNE   $C867              ;
C85C: 8E C9 21      LDX   #$C921             ;
C85F: 86 00         LDA   #$00               ;
C861: BD D0 55      JSR   $D055              ;
C864: 7E D0 0A      JMP   $D00A              ;
C867: 86 01         LDA   #$01               ;
C869: 8E C8 48      LDX   #$C848             ;
C86C: 7E F4 BE      JMP   InsEventLnkPgSav   ;

C86F: 8E B4 12      LDX   #$B412             ;
C872: 10 8E CA A0   LDY   #$CAA0             ;
C876: 4F            CLRA                     ;
C877: B7 A1 77      STA   $A177              ;
C87A: B7 A1 76      STA   $A176              ;
C87D: A6 A4         LDA   ,Y                 ;
C87F: 44            LSRA                     ;
C880: 44            LSRA                     ;
C881: 44            LSRA                     ;
C882: 44            LSRA                     ;
C883: 8D 0C         BSR   $C891              ;
C885: A6 A0         LDA   ,Y+                ;
C887: 84 0F         ANDA  #$0F               ;
C889: 8D 06         BSR   $C891              ;
C88B: 10 8C CC 0E   CMPY  #$CC0E             ;
C88F: 26 EC         BNE   $C87D              ;

;SUBRTN
C891: 85 0C         BITA  #$0C               ;
C893: 26 09         BNE   $C89E              ;
C895: BB A1 76      ADDA  $A176              ;
C898: 48            ASLA                     ;
C899: 48            ASLA                     ;
C89A: B7 A1 76      STA   $A176              ;
C89D: 39            RTS                      ;
C89E: 34 02         PSHS  A                  ;
C8A0: 84 03         ANDA  #$03               ;
C8A2: BB A1 76      ADDA  $A176              ;
C8A5: B7 A1 76      STA   $A176              ;
C8A8: 35 02         PULS  A                  ;
C8AA: 84 0C         ANDA  #$0C               ;
C8AC: 44            LSRA                     ;
C8AD: 44            LSRA                     ;
C8AE: CE CC 0D      LDU   #$CC0D             ;
C8B1: E6 C6         LDB   A,U                ;
C8B3: F7 A1 75      STB   $A175              ;
C8B6: 8C B9 B2      CMPX  #$B9B2             ;
C8B9: 25 04         BCS   $C8BF              ;
C8BB: 30 89 FA 61   LEAX  $-59F,X            ;
C8BF: B6 A1 77      LDA   $A177              ;
C8C2: 27 14         BEQ   $C8D8              ;
C8C4: A6 84         LDA   ,X                 ;
C8C6: 84 F0         ANDA  #$F0               ;
C8C8: A7 84         STA   ,X                 ;
C8CA: B6 A1 75      LDA   $A175              ;
C8CD: 84 0F         ANDA  #$0F               ;
C8CF: AA 84         ORA   ,X                 ;
C8D1: A7 84         STA   ,X                 ;
C8D3: B6 A1 75      LDA   $A175              ;
C8D6: 20 0D         BRA   $C8E5              ;
C8D8: 73 A1 77      COM   $A177              ;
C8DB: B6 A1 75      LDA   $A175              ;
C8DE: A7 84         STA   ,X                 ;
C8E0: 7A A1 76      DEC   $A176              ;
C8E3: 2B 0B         BMI   $C8F0              ;
C8E5: 30 88 18      LEAX  $18,X              ;
C8E8: 7A A1 76      DEC   $A176              ;
C8EB: 2A F1         BPL   $C8DE              ;
C8ED: 7F A1 77      CLR   $A177              ;
C8F0: 7F A1 76      CLR   $A176              ;
C8F3: 39            RTS                      ;
C8F4: D6 37         LDB   <$37               ;
C8F6: 27 21         BEQ   $C919              ;
C8F8: F1 A1 83      CMPB  $A183              ;
C8FB: 23 06         BLS   $C903              ;
C8FD: F7 A1 83      STB   $A183              ;
C900: 7C A1 84      INC   $A184              ;
C903: CE C0 E9      LDU   #$C0E9             ;
C906: 8E 28 E5      LDX   #$28E5             ;
C909: BD FF CE      JSR   CallOtherPageX     ;
C90C: C0 02                                  ;   $C002         ;
C90E: 02                                     ;page #2
C90F: 4F            CLRA                     ;
C910: 8E 48 E5      LDX   #$48E5             ;
C913: BD FF CE      JSR   CallOtherPageX     ;
C916: C0 0E                                  ;   $C00E         ;
C918: 02                                     ;page #2
C919: 86 10         LDA   #$10               ;
C91B: 8E C8 F4      LDX   #$C8F4             ;
C91E: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C921: 86 FF         LDA   #$FF               ;
C923: B7 A1 6A      STA   $A16A              ;
C926: 86 02         LDA   #$02               ;
C928: 8E C9 2E      LDX   #$C92E             ;
C92B: 7E F4 BE      JMP   InsEventLnkPgSav   ;
C92E: 86 0A         LDA   #$0A               ;
C930: B7 A1 6A      STA   $A16A              ;
C933: 7E D0 0A      JMP   $D00A              ;



;SUBRTN
C936: 96 8C         LDA   <$8C               ;
C938: 27 06         BEQ   $C940              ;
C93A: BD D3 DB      JSR   $D3DB              ;
C93D: 4A            DECA                     ;
C93E: 20 F8         BRA   $C938              ;
C940: 39            RTS                      ;

Data??

C941: FE 74 40      LDU   $7440              ;
C944: 11 
C945: 11 
C946: 85 81         BITA  #$81               ;
C948: 81 81         CMPA  #$81               ;
C94A: 88 82         EORA  #$82               ;
C94C: 82 22         SBCA  #$22               ;
C94E: 24 22         BCC   $C972              ;
C950: 42 
C951: 24 24         BCC   $C977              ;
C953: 24 44         BCC   $C999              ;
C955: 24 44         BCC   $C99B              ;
C957: 49            ROLA                     ;
C958: 44            LSRA                     ;
C959: 94 41         ANDA  <$41               ;
C95B: 88 14         EORA  #$14               ;
C95D: 41 
C95E: 88 14         EORA  #$14               ;
C960: 41 
C961: 88 94         EORA  #$94               ;
C963: 41 
C964: 88 94         EORA  #$94               ;
C966: 49            ROLA                     ;
C967: 88 14         EORA  #$14               ;
C969: 98 58         EORA  <$58               ;
C96B: 94 98         ANDA  <$98               ;
C96D: 18 
C96E: 94 46         ANDA  <$46               ;
C970: 66 62         ROR   2,S                ;
C972: 42 
C973: 42 
C974: 42 
C975: 42 
C976: 25 24         BCS   $C99C              ;
C978: 24 68         BCC   $C9E2              ;
C97A: 24 24         BCC   $C9A0              ;
C97C: 24 26         BCC   $C9A4              ;
C97E: 11 
C97F: 18 
C980: 18 
C981: 58            ASLB                     ;
C982: 18 
C983: 58            ASLB                     ;
C984: 81 44         CMPA  #$44               ;
C986: 98 81         EORA  <$81               ;
C988: 44            LSRA                     ;
C989: 98 81         EORA  <$81               ;
C98B: 44            LSRA                     ;
C98C: 98 14         EORA  <$14               ;
C98E: 94 94         ANDA  <$94               ;
C990: 16 22 24      LBRA  $EBB7              ;
C993: 24 A4         BCC   $C939              ;
C995: 24 A4         BCC   $C93B              ;
C997: 24 24         BCC   $C9BD              ;
C999: 24 24         BCC   $C9BF              ;
C99B: 24 FE         BCC   $C99B              ;
C99D: 81 4A         CMPA  #$4A               ;
C99F: 42 
C9A0: 42 
C9A1: 42 
C9A2: 42 
C9A3: 44            LSRA                     ;
C9A4: 99 99         ADCA  <$99               ;
C9A6: 41 
C9A7: 88 14         EORA  #$14               ;
C9A9: 41 
C9AA: 88 14         EORA  #$14               ;
C9AC: 46            RORA                     ;
C9AD: 24 24         BCC   $C9D3              ;
C9AF: 24 24         BCC   $C9D5              ;
C9B1: 24 24         BCC   $C9D7              ;
C9B3: A4 24         ANDA  4,Y                ;
C9B5: 24 A4         BCC   $C95B              ;
C9B7: 22 42         BHI   $C9FB              ;
C9B9: 4A            DECA                     ;
C9BA: 42 
C9BB: 42 
C9BC: 44            LSRA                     ;
C9BD: 99 19         ADCA  <$19               ;
C9BF: 91 19         CMPA  <$19               ;
C9C1: 91 91         CMPA  <$91               ;
C9C3: 81 81         CMPA  #$81               ;
C9C5: 41 
C9C6: 81 49         CMPA  #$49               ;
C9C8: 46            RORA                     ;
C9C9: 42 
C9CA: 42 
C9CB: 42 
C9CC: 42 
C9CD: 42 
C9CE: 42 
C9CF: 24 22         BCC   $C9F3              ;
C9D1: 42 
C9D2: 62 
C9D3: 62 
C9D4: 42 
C9D5: 24 49         BCC   $CA20              ;
C9D7: 19            DAA                      ;
C9D8: 91 91         CMPA  <$91               ;
C9DA: 91 91         CMPA  <$91               ;
C9DC: 91 85         CMPA  <$85               ;
C9DE: 88 14         EORA  #$14               ;
C9E0: 94 14         ANDA  <$14               ;
C9E2: 24 24         BCC   $CA08              ;
C9E4: 24 24         BCC   $CA0A              ;
C9E6: 24 24         BCC   $CA0C              ;
C9E8: A4 24         ANDA  4,Y                ;
C9EA: 24 41         BCC   $CA2D              ;
C9EC: 81 81         CMPA  #$81               ;
C9EE: 18 
C9EF: 18 
C9F0: 94 41         ANDA  <$41               ;
C9F2: 88 14         EORA  #$14               ;
C9F4: 14 
C9F5: 24 42         BCC   $CA39              ;
C9F7: 24 24         BCC   $CA1D              ;
C9F9: 24 24         BCC   $CA1F              ;
C9FB: 24 24         BCC   $CA21              ;
C9FD: 24 44         BCC   $CA43              ;
C9FF: 98 18         EORA  <$18               ;
CA01: 18 
CA02: 18 
CA03: 58            ASLB                     ;
CA04: 89 44         ADCA  #$44               ;
CA06: 18 
CA07: 85 14         BITA  #$14               ;
CA09: 24 14         BCC   $CA1F              ;
CA0B: 24 A4         BCC   $C9B1              ;
CA0D: 24 24         BCC   $CA33              ;
CA0F: 24 A4         BCC   $C9B5              ;
CA11: 24 28         BCC   $CA3B              ;
CA13: 24 44         BCC   $CA59              ;
CA15: 18 
CA16: 19            DAA                      ;
CA17: 19            DAA                      ;
CA18: 81 41         CMPA  #$41               ;
CA1A: 81 14         CMPA  #$14               ;
CA1C: 24 24         BCC   $CA42              ;
CA1E: 24 24         BCC   $CA44              ;
CA20: 22 42         BHI   $CA64              ;
CA22: 42 
CA23: 64 41         LSR   1,U                ;
CA25: 85 81         BITA  #$81               ;
CA27: 81 18         CMPA  #$18               ;
CA29: 19            DAA                      ;
CA2A: 41 
CA2B: 89 44         ADCA  #$44               ;
CA2D: 42 
CA2E: 22 42         BHI   $CA72              ;
CA30: 24 24         BCC   $CA56              ;
CA32: 24 24         BCC   $CA58              ;
CA34: 24 44         BCC   $CA7A              ;
CA36: 18 
CA37: 14 
CA38: 98 11         EORA  <$11               ;
CA3A: 81 81         CMPA  #$81               ;
CA3C: 41 
CA3D: 89 44         ADCA  #$44               ;
CA3F: 42 
CA40: 22 42         BHI   $CA84              ;
CA42: 24 24         BCC   $CA68              ;
CA44: 24 24         BCC   $CA6A              ;
CA46: 24 44         BCC   $CA8C              ;
CA48: 18 
CA49: 94 41         ANDA  <$41               ;
CA4B: 88 89         EORA  #$89               ;
CA4D: 44            LSRA                     ;
CA4E: 49            ROLA                     ;
CA4F: 88 14         EORA  #$14               ;
CA51: 41 
CA52: 88 14         EORA  #$14               ;
CA54: 14 
CA55: 24 24         BCC   $CA7B              ;
CA57: 24 26         BCC   $CA7F              ;
CA59: 62 
CA5A: 66 26         ROR   6,Y                ;
CA5C: 24 18         BCC   $CA76              ;
CA5E: 91 91         CMPA  <$91               ;
CA60: 19            DAA                      ;
CA61: 18 
CA62: 14 
CA63: 18 
CA64: 14 
CA65: 14 
CA66: 24 14         BCC   $CA7C              ;
CA68: 2A 45         BPL   $CAAF              ;
CA6A: 24 68         BCC   $CAD4              ;
CA6C: 88 24         EORA  #$24               ;
CA6E: 44            LSRA                     ;
CA6F: 42 
CA70: 18 
CA71: A8 82         EORA  ,-X                ;
CA73: 44            LSRA                     ;
CA74: A8 22         EORA  2,Y                ;
CA76: 20 FE         BRA   $CA76              ;
CA78: 87 
CA79: 40            NEGA                     ;
CA7A: 44            LSRA                     ;
CA7B: 11 
CA7C: 88 24         EORA  #$24               ;
CA7E: FE 9A 3F      LDU   $9A3F              ;
CA81: 44            LSRA                     ;
CA82: 11 
CA83: 88 24         EORA  #$24               ;
CA85: FE C1 3F      LDU   $C13F              ;
CA88: 44            LSRA                     ;
CA89: 44            LSRA                     ;
CA8A: 44            LSRA                     ;
CA8B: 11 
CA8C: 11 
CA8D: 11 
CA8E: 11 
CA8F: 88 88         EORA  #$88               ;
CA91: 88 22         EORA  #$22               ;
CA93: 22 22         BHI   $CAB7              ;
CA95: 20 FE         BRA   $CA95              ;
CA97: C3 45 22      ADDD  #$4522             ;
CA9A: 22 44         BHI   $CAE0              ;
CA9C: 11 
CA9D: 81 50         CMPA  #$50               ;
CA9F: FD 10 D1      STD   $10D1              ;
CAA2: BD 29 C2      JSR   $29C2              ;
CAA5: 9C 29         CMPX  <$29               ;
CAA7: CB EA         ADDB  #$EA               ;
CAA9: C2 8C         SBCB  #$8C               ;
CAAB: 29 C2         BVS   $CA6F              ;
CAAD: 81 0D         CMPA  #$0D               ;
CAAF: 10 
CAB0: C2 8D         SBCB  #$8D               ;
CAB2: 29 C2         BVS   $CA76              ;
CAB4: 9C 29         CMPX  <$29               ;
CAB6: CB EA         ADDB  #$EA               ;
CAB8: 42 
CAB9: 94 29         ANDA  <$29               ;
CABB: 42 
CABC: 81 0C         CMPA  #$0C               ;
CABE: 3F            SWI                      ;
CABF: 29 C2         BVS   $CA83              ;
CAC1: 94 C2         ANDA  <$C2               ;
CAC3: 9C 29         CMPX  <$29               ;
CAC5: C1 8D         CMPB  #$8D               ;
CAC7: A4 29         ANDA  9,Y                ;
CAC9: 42 
CACA: 94 29         ANDA  <$29               ;
CACC: 3F            SWI                      ;
CACD: 3E            RESET                    ;
CACE: 29 42         BVS   $CB12              ;
CAD0: A4 29         ANDA  9,Y                ;
CAD2: 4C            INCA                     ;
CAD3: 29 C1         BVS   $CA96              ;
CAD5: 8D A4         BSR   $CA7B              ;
CAD7: 2A 42         BPL   $CB1B              ;
CAD9: 94 29         ANDA  <$29               ;
CADB: 3E            RESET                    ;
CADC: 3D            MUL                      ;
CADD: B6 B4 A2      LDA   $B4A2              ;
CAE0: 4A            DECA                     ;
CAE1: 17 CA 16      LBSR  $94FA              ;
CAE4: C1 9C         CMPB  #$9C               ;
CAE6: B4 A7 A4      ANDA  $A7A4              ;
CAE9: B1 7A 7A      CMPA  $7A7A              ;
CAEC: 3D            MUL                      ;
CAED: 3C B6         CWAI  $B6                ;
CAEF: B4 B1 71      ANDA  $B171              ;
CAF2: 81 6B         CMPA  #$6B               ;
CAF4: 16 C1 AC      LBRA  $8CA3              ;
CAF7: A4 B6         ANDA  [A,Y]              ;
CAF9: B4 A2 4A      ANDA  $A24A              ;
CAFC: 6B 
CAFD: 3C 2F         CWAI  $2F                ;
CAFF: B6 B4 29      LDA   $B429              ;
CB02: 62 
CB03: 85 C2         BITA  #$C2               ;
CB05: 85 C1         BITA  #$C1               ;
CB07: AC A4         CMPX  ,Y                 ;
CB09: B6 B4 28      LDA   $B428              ;
CB0C: 62 
CB0D: A2 
CB0E: F2 EB 61      SBCB  $EB61              ;
CB11: 84 29         ANDA  #$29               ;
CB13: 62 
CB14: 8E 28 E2      LDX   #$28E2             ;
CB17: A4 
CB18: B7 B4 28      STA   $B428              ;
CB1B: 62 
CB1C: A2 E2         SBCA  ,-S                ;
CB1E: DB 7B         ADDB  <$7B               ;
CB20: 42 
CB21: 96 28         LDA   <$28               ;
CB23: 4E 
CB24: 28 E2         BVC   $CB08              ;
CB26: B4 B6 B4      ANDA  $B6B4              ;
CB29: 29 62         BVS   $CB8D              ;
CB2B: 92 E2         SBCA  <$E2               ;
CB2D: CB 7B         ADDB  #$7B               ;
CB2F: 52 
CB30: 96 28         LDA   <$28               ;
CB32: 4E 
CB33: 28 EB         BVC   $CB20              ;
CB35: 41 
CB36: A4 
CB37: B7 B4 28      STA   $B428              ;
CB3A: 62 
CB3B: 92 E1         SBCA  <$E1               ;
CB3D: FB 7B 5B      ADDB  $7B5B              ;
CB40: 24 B1         BCC   $CAF3              ;
CB42: 6D 18         TST   -8,X               ;
CB44: 14 
CB45: EB 51         ADDB  -15,U              ;
CB47: 94 B7         ANDA  <$B7               ;
CB49: B4 18 17      ANDA  $1817              ;
CB4C: 29 2D         BVS   $CB7B              ;
CB4E: 1E B1         EXG   DP,X               ;
CB50: 4B 
CB51: 4B 
CB52: 25 B1         BCS   $CB05              ;
CB54: 6D B1         TST   [,Y++]             ;
CB56: 5E 
CB57: B5 1A 4B      BITA  $1A4B              ;
CB5A: 61 
CB5B: 84 B2         ANDA  #$B2               ;
CB5D: 4B 
CB5E: 41 
CB5F: 82 C1         SBCA  #$C1               ;
CB61: DB 14         ADDB  <$14               ;
CB63: B5 18 17      BITA  $1817              ;
CB66: 18 
CB67: 16 D1 81      LBRA  $9CEB              ;
CB6A: 4E 
CB6B: B6 19 4B      LDA   $194B              ;
CB6E: 61 
CB6F: 84 18         ANDA  #$18               ;
CB71: 24 B4         BCC   $CB27              ;
CB73: 18 
CB74: 1F 1C         TFR   X,?                ;
CB76: 38 
CB77: 53            COMB                     ;
CB78: 84 B1         ANDA  #$B1               ;
CB7A: 6E 2B         JMP   11,Y               ;
CB7C: CB 61         ADDB  #$61               ;
CB7E: 94 38         ANDA  <$38               ;
CB80: 42 
CB81: B4 18 41      ANDA  $1841              ;
CB84: 81 EF         CMPA  #$EF               ;
CB86: 39            RTS                      ;

CB87: 43            COMA                     ;
CB88: 85 B1         BITA  #$B1               ;
CB8A: 6E 2B         JMP   11,Y               ;
CB8C: CB 71         ADDB  #$71               ;
CB8E: 84 38         ANDA  #$38               ;
CB90: 43            COMA                     ;
CB91: 84 B6         ANDA  #$B6               ;
CB93: 18 
CB94: 1C E3         ANDCC #$E3               ;
CB96: 95 38         BITA  <$38               ;
CB98: 41 
CB99: 81 6D         CMPA  #$6D               ;
CB9B: 38 
CB9C: CB C6         ADDB  #$C6               ;
CB9E: 19            DAA                      ;
CB9F: 42 
CBA0: B5 38 4B      BITA  $384B              ;
CBA3: 61 
CBA4: 8F 
CBA5: D3 95         ADDD  <$95               ;
CBA7: 38 
CBA8: 5B 
CBA9: 51 
CBAA: F3 8C BD      ADDD  $8CBD              ;
CBAD: 61 
CBAE: 84 2A         ANDA  #$2A               ;
CBB0: 63 85         COM   B,X                ;
CBB2: B6 18 ED      LDA   $18ED              ;
CBB5: 38 
CBB6: 53            COMB                     ;
CBB7: 94 18         ANDA  <$18               ;
CBB9: 51 
CBBA: F3 8C BD      ADDD  $8CBD              ;
CBBD: 7B 
CBBE: 42 
CBBF: 91 42         CMPA  <$42               ;
CBC1: B5 18 7B      BITA  $187B              ;
CBC4: DC 21         LDD   <$21               ;
CBC6: 51 
CBC7: F3 4C 7E      ADDD  $4C7E              ;
CBCA: 30 6C         LEAX  12,S               ;
CBCC: C2 14         SBCB  #$14               ;
CBCE: 2C 34         BGE   $CC04              ;
CBD0: C7 
CBD1: E1 07         CMPB  7,X                ;
CBD3: C1 35         CMPB  #$35               ;
CBD5: CC 21 42      LDD   #$2142             ;
CBD8: C3 4C 7F      ADDD  #$4C7F             ;
CBDB: 10 
CBDC: 6C 13         INC   -13,X              ;
CBDE: 5C            INCB                     ;
CBDF: C1 35         CMPB  #$35               ;
CBE1: C1 52         CMPB  #$52               ;
CBE3: C3 4C 7F      ADDD  #$4C7F             ;
CBE6: 15 
CBE7: C2 7D         SBCB  #$7D               ;
CBE9: 34 C1         PSHS  PC,U,CC            ;
CBEB: 5C            INCB                     ;
CBEC: 17 CC 36      LBSR  $9825              ;
CBEF: C3 5C 14      ADDD  #$5C14             ;
CBF2: 2D 34         BLT   $CC28              ;
CBF4: C7 
CBF5: 1C 14         ANDCC #$14               ;
CBF7: C2 6E         SBCB  #$6E               ;
CBF9: 34 D1         PSHS  PC,U,X,CC          ;
CBFB: 4E 
CBFC: 15 
CBFD: CC 36 C3      LDD   #$36C3             ;
CC00: 5C            INCB                     ;
CC01: 14 
CC02: 2D 34         BLT   $CC38              ;
CC04: C7 
CC05: 1C 14         ANDCC #$14               ;
CC07: C2 51         SBCB  #$51               ;
CC09: C2 7D         SBCB  #$7D               ;
CC0B: 14 
CC0C: F1 4C 22      CMPB  $4C22              ;
CC0F: CC 00 3E      LDD   #$003E             ;
CC12: 41 
CC13: 41 
CC14: 22 00         BHI   $CC16              ;
CC16: 3E            RESET                    ;
CC17: 41 
CC18: 41 
CC19: 3E            RESET                    ;
CC1A: 00 7F         NEG   <$7F               ;
CC1C: 09 09         ROL   <$09               ;
CC1E: 06 00         ROR   <$00               ;
CC20: 03 04         COM   <$04               ;
CC22: 78 04 03      ASL   $0403              ;
CC25: 00 7F         NEG   <$7F               ;
CC27: 09 19         ROL   <$19               ;
CC29: 66 00         ROR   0,X                ;
CC2B: 41 
CC2C: 7F 41 00      CLR   $4100              ;
CC2F: 3E            RESET                    ;
CC30: 41 
CC31: 49            ROLA                     ;
CC32: 3A            ABX                      ;
CC33: 00 7F         NEG   <$7F               ;
CC35: 08 08         LSL   <$08               ;
CC37: 7F 00 01      CLR   $0001              ;
CC3A: 01 
CC3B: 7F 01 01      CLR   $0101              ;
CC3E: 00 1C         NEG   <$1C               ;
CC40: 22 5D         BHI   $CC9F              ;
CC42: 63 55         COM   -11,U              ;
CC44: 22 1C         BHI   $CC62              ;
CC46: 22 7F         BHI   $CCC7              ;
CC48: 4B 
CC49: 45 
CC4A: 22 1C         BHI   $CC68              ;
CC4C: 00 00         NEG   <$00               ;
CC4E: 00 42         NEG   <$42               ;
CC50: 7F 40 00      CLR   $4000              ;
CC53: 26 49         BNE   $CC9E              ;
CC55: 49            ROLA                     ;
CC56: 3E            RESET                    ;
CC57: 00 36         NEG   <$36               ;
CC59: 49            ROLA                     ;
CC5A: 49            ROLA                     ;
CC5B: 36 00         PSHU                     ;
CC5D: 3E            RESET                    ;
CC5E: 41 
CC5F: 41 
CC60: 3E            RESET                    ;
CC61: 43            COMA                     ;
CC62: 30 1C         LEAX  -4,X               ;
CC64: 70 3C 70      NEG   $3C70              ;
CC67: 5F            CLRB                     ;
CC68: 70 1C A8      NEG   $1CA8              ;
CC6B: 40            NEGA                     ;
CC6C: A8 5C         EORA  -4,U               ;
CC6E: A8 C0         EORA  ,U+                ;
CC70: EB C0         ADDB  ,U+                ;
CC72: DD C0         STD   <$C0               ;
CC74: DF C0         STU   <$C0               ;
CC76: E7 C0         STB   ,U+                ;
CC78: E3 C0         ADDD  ,U+                ;
CC7A: E1 C0         CMPB  ,U+                ;
CC7C: E5 60         BITB  0,S                ;
CC7E: 00 60         NEG   <$60               ;
CC80: 00 62         NEG   <$62               ;
CC82: 00 98         NEG   <$98               ;
CC84: 00 98         NEG   <$98               ;
CC86: 00 9A         NEG   <$9A               ;
CC88: 00 F9         NEG   <$F9               ;
CC8A: 85 F8         BITA  #$F8               ;
CC8C: CE F9 A3      LDU   #$F9A3             ;
CC8F: F9 29 F8      ADCB  $29F8              ;
CC92: F7 F9 7B      STB   $F97B              ;
CC95: 09 00         ROL   <$00               ;
CC97: 11 
CC98: 00 19         NEG   <$19               ;
CC9A: 80 09         SUBA  #$09               ;
CC9C: 60 11         NEG   -15,X              ;
CC9E: 60 19         NEG   -7,X               ;
CCA0: E0 44         SUBB  4,U                ;
CCA2: 33 CC 33      LEAU  $33,PC             ;
CCA5: 33 33         LEAU  -13,Y              ;
CCA7: 88 88         EORA  #$88               ;
CCA9: CC CC 24      LDD   #$CC24             ;
CCAC: 24 



; in jump table
CCAD: CE 00 00      LDU   #$0000             ;
CCB0: C6 08         LDB   #$08               ;
CCB2: 8E B0 5D      LDX   #$B05D             ;
CCB5: EF 94         STU   [,X]               ;
CCB7: EF 98 02      STU   [$02,X]            ;
CCBA: EF 98 04      STU   [$04,X]            ;
CCBD: EF 98 06      STU   [$06,X]            ;
CCC0: 3A            ABX                      ;
CCC1: 9C 97         CMPX  <$97               ;
CCC3: 25 F0         BCS   $CCB5              ;
CCC5: AE 9F A0 97   LDX   [$A097]            ;
CCC9: 27 08         BEQ   $CCD3              ;
CCCB: EF 84         STU   ,X                 ;
CCCD: 6F 02         CLR   2,X                ;
CCCF: EF 89 FF 00   STU   $-100,X            ;
CCD3: DC 20         LDD   <$20               ;
CCD5: 83 6D 40      SUBD  #$6D40             ;
CCD8: DD 73         STD   <$73               ;
CCDA: 44            LSRA                     ;A = A/4
CCDB: 44            LSRA                     ;
CCDC: CE CD 69      LDU   #$CD69             ;
CCDF: C6 03         LDB   #$03               ;
CCE1: 3D            MUL                      ;
CCE2: 33 CB         LEAU  D,U                ;
CCE4: 96 BA         LDA   <$BA               ;
CCE6: 85 02         BITA  #$02               ;
CCE8: 26 22         BNE   $CD0C              ;
CCEA: 86 30         LDA   #$30               ;
CCEC: 10 8E B1 25   LDY   #$B125             ;
CCF0: 8E 00 00      LDX   #$0000             ;
CCF3: AF B4         STX   [,Y]               ;
CCF5: 37 14         PULU  B,X                ;
CCF7: ED A4         STD   ,Y                 ;
CCF9: AF B1         STX   [,Y++]             ;
CCFB: 4C            INCA                     ;
CCFC: 8E 00 00      LDX   #$0000             ;
CCFF: AF B4         STX   [,Y]               ;
CD01: 37 14         PULU  B,X                ;
CD03: ED A4         STD   ,Y                 ;
CD05: AF B1         STX   [,Y++]             ;
CD07: 4C            INCA                     ;
CD08: 81 70         CMPA  #$70               ;
CD0A: 26 E4         BNE   $CCF0              ;
CD0C: 8E 4C 09      LDX   #$4C09             ;
CD0F: CC 90 90      LDD   #$9090             ;
CD12: ED 84         STD   ,X                 ;
CD14: ED 88 1D      STD   $1D,X              ;
CD17: 8E 53 09      LDX   #$5309             ;
CD1A: CC 09 09      LDD   #$0909             ;
CD1D: ED 84         STD   ,X                 ;
CD1F: ED 88 1D      STD   $1D,X              ;
CD22: 8E A0 65      LDX   #$A065             ;
CD25: CE B0 5D      LDU   #$B05D             ;
CD28: 8D 3A         BSR   $CD64              ;
CD2A: 8E A0 6B      LDX   #$A06B             ;
CD2D: 8D 35         BSR   $CD64              ;
CD2F: DF 97         STU   <$97               ;
CD31: DC BF         LDD   <$BF               ;
CD33: 44            LSRA                     ;
CD34: 44            LSRA                     ;
CD35: 44            LSRA                     ;
CD36: 44            LSRA                     ;
CD37: 54            LSRB                     ;
CD38: 54            LSRB                     ;
CD39: 54            LSRB                     ;
CD3A: C3 4B 07      ADDD  #$4B07             ;
CD3D: ED C4         STD   ,U                 ;
CD3F: AE C4         LDX   ,U                 ;
CD41: CC 90 99      LDD   #$9099             ;
CD44: ED 84         STD   ,X                 ;
CD46: A7 02         STA   2,X                ;
CD48: 86 09         LDA   #$09               ;
CD4A: A7 89 FF 01   STA   -255,X             ;
CD4E: 39            RTS                      ;



CD4F: EC 0A         LDD   10,X               ;
CD51: 93 73         SUBD  <$73               ;
CD53: 44            LSRA                     ;
CD54: 44            LSRA                     ;
CD55: E6 0C         LDB   12,X               ;
CD57: 54            LSRB                     ;
CD58: 54            LSRB                     ;
CD59: 54            LSRB                     ;
CD5A: C3 30 07      ADDD  #$3007             ;
CD5D: ED C4         STD   ,U                 ;
CD5F: EC 88 12      LDD   $12,X              ;
CD62: ED D1         STD   [,U++]             ;

;SUBRTN
CD64: AE 84         LDX   ,X                 ;
CD66: 26 E7         BNE   $CD4F              ;
CD68: 39            RTS                      ;

Data

CD69: 25 70 07
CD6C: 26 77 00
CD6F: 26 07 70
CD72: 24 07 70
CD75: 23 07 70
CD78: 23 70 07
CD7B: 24 07 70
CD7E: 25 70 07
CD81: 26 77 00
CD84: 25 07 70
CD87: 24 07 70
CD8A: 23 07 70
CD8D: 21 07 70
CD90: 22 70 07
CD93: 24 77 00
CD96: 24 70 07
CD99: 26 77 00
CD9C: 26 77 00
CD9F: 25 77 00
CDA2: 25 70 07
CDA5: 26 77 00
CDA8: 24 07 70
CDAB: 23 70 07
CDAE: 25 77 00
CDB1: 26 70 07
CDB4: 26 77 00
CDB7: 26 77 00
CDBA: 25 07 70
CDBD: 23 07 70
CDC0: 22 07 70
CDC3: 21 77 00
CDC6: 21 70 07
CDC9: 23 70 07
CDCC: 25 70 07
CDCF: 25 07 70
CDD2: 25 77 00
CDD5: 25 77 00
CDD8: 24 77 00
CDDB: 22 07 70
CDDE: 20 07 70
CDE1: 1E 07 70
CDE4: 1C 07 70
CDE7: 1D 70 07
CDEA: 1F 70 07
CDED: 21 70 07
CDF0: 22 70 07
CDF3: 24 70 07
CDF6: 26 70 07
CDF9: 26 77 00
CDFC: 26 77 00
CDFF: 26 77 00
CE02: 26 77 00
CE05: 26 77 00
CE08: 25 77 00
CE0B: 25 70 07
CE0E: 26 77 00
CE11: 24 07 70
CE14: 23 77 00
CE17: 24 77 00
CE1A: 22 07 70
CE1D: 23 70 07
CE20: 22 07 70
CE23: 21 70 07
CE26: 23 70 07

CE29: 25 70 07
CE2C: 26 77 00
CE2F: 26 07 70
CE32: 24 07 70
CE35: 23 07 70
CE38: 23 70 07
CE3B: 24 07 70
CE3E: 25 70 07
CE41: 26 77 00
CE44: 25 07 70
CE47: 24 07 70
CE4A: 23 07 70
CE4D: 21 07 70
CE50: 22 70 07
CE53: 24 77 00
CE56: 24 70 07
CE59: 26 77 00
CE5C: 26 77 00
CD5F: 25 77 00
CD62: 25 70 07
CD65: 26 77 00
CD58: 24 07 70
CE6B: 23 70 07
CE6E: 25 77 00
CE71: 26 70 07
CE74: 26 77 00
CE77: 26 77 00
CE7A: 25 07 70
CE7D: 23 07 70
CE80: 22 07 70
CE83: 21 77 00
CE86: 21 70 07
CE89: 23 70 07
CE8C: 25 70 07
CE8F: 25 07 70
CE92: 25 77 00
CE95: 25 77 00
CE98: 24 77 00
CE9B: 22 07 70
CE9E: 20 07 70
CEA1: 1E 07 70
CEA4: 1C 07 70
CEA7: 1D 70 07
CEAA: 1F 70 07
CEAD: 21 70 07
CEB0: 22 70 07
CEB3: 24 70 07
CEB6: 26 70 07
CEB9: 26 77 00
CEBC: 26 77 00
CEBF: 26 77 00
CEC2: 26 77 00
CEC5: 26 77 00
CEC8: 25 77 00
CECB: 25 70 07
CECE: 26 77 00
CED1: 24 07 70
CED4: 23 77 00
CED7: 24 77 00
CEDA: 22 07 70
CEDD: 23 70 07
CEE0: 22 07 70
CEE3: 21 70 07
CEE6: 23 70 07
CEE9: 80            
CEEA: 00 00         NEG   <$00               ;
CEEC: 30 00         LEAX  0,X                ;
CEEE: 30 00         LEAX  0,X                ;
CEF0: 00 00         NEG   <$00               ;
CEF2: 00 00         NEG   <$00               ;
CEF4: 03 00         COM   <$00               ;
CEF6: 00 00         NEG   <$00               ;
CEF8: 00 00         NEG   <$00               ;
CEFA: 96 00         LDA   <$00               ;
CEFC: 00 00         NEG   <$00               ;
CEFE: 00 FE         NEG   <$FE               ;
CF00: C3 00 00      ADDD  #$0000             ;
CF03: 00 00         NEG   <$00               ;
CF05: D6 66         LDB   <$66               ;
CF07: 00 00         NEG   <$00               ;
CF09: 00 00         NEG   <$00               ;
CF0B: 66 66         ROR   6,S                ;
CF0D: 39            RTS                      ;

CF0E: 00 06         NEG   <$06               ;
CF10: 66 66         ROR   6,S                ;
CF12: 88 68         EORA  #$68               ;
CF14: 66 66         ROR   6,S                ;
CF16: 66 88 88      ROR   $-78,X             ;
CF19: 88 00         EORA  #$00               ;
CF1B: 60 63         NEG   3,S                ;
CF1D: 30 63         LEAX  3,S                ;
CF1F: 00 06         NEG   <$06               ;
CF21: 26 68         BNE   $CF8B              ;
CF23: 28 60         BVC   $CF85              ;
CF25: 66 66         ROR   6,S                ;
CF27: 86 00         LDA   #$00               ;
CF29: 00 66         NEG   <$66               ;
CF2B: 66 00         ROR   0,X                ;
CF2D: 00 ED         NEG   <$ED               ;
CF2F: 66 00         ROR   0,X                ;
CF31: 00 00         NEG   <$00               ;
CF33: 63 
CF34: 90 09         SUBA  <$09               ;
CF36: 90 99         SUBA  <$99               ;
CF38: 99 99         ADCA  <$99               ;
CF3A: 90 CC         SUBA  <$CC               ;
CF3C: 90 11         SUBA  <$11               ;
CF3E: 00 11         NEG   <$11               ;
CF40: 10 
CF41: 11 
CF42: 00 10         NEG   <$10               ;
CF44: 10 
CF45: 10 
CF46: 00 10         NEG   <$10               ;
CF48: 00 11         NEG   <$11               ;
CF4A: 10 
CF4B: 11 
CF4C: 00 11         NEG   <$11               ;
CF4E: 00 10         NEG   <$10               ;
CF50: 00 10         NEG   <$10               ;
CF52: 10 
CF53: 10 
CF54: 00 11         NEG   <$11               ;
CF56: 10 
CF57: 10 
CF58: 10 
CF59: 11 
CF5A: 00 10         NEG   <$10               ;
CF5C: 10 
CF5D: 10 
CF5E: 10 
CF5F: 10 
CF60: 00 01         NEG   <$01               ;
CF62: 00 01         NEG   <$01               ;
CF64: 01 
CF65: 01 
CF66: 00 11         NEG   <$11               ;
CF68: 01 
CF69: 11 
CF6A: 00 11         NEG   <$11               ;
CF6C: 00 01         NEG   <$01               ;
CF6E: 01 
CF6F: 01 
CF70: 00 01         NEG   <$01               ;
CF72: 00 11         NEG   <$11               ;
CF74: 00 11         NEG   <$11               ;
CF76: 01 
CF77: 11 
CF78: 00 01         NEG   <$01               ;
CF7A: 01 
CF7B: 01 
CF7C: 01 
CF7D: 01 
CF7E: 00 11         NEG   <$11               ;
CF80: 01 
CF81: 01 
CF82: 01 
CF83: 11 
CF84: 00 FF         NEG   <$FF               ;
CF86: F0 FF 00      SUBB  $FF00              ;
CF89: FF 00 F0      STU   $00F0              ;
CF8C: 00 F0         NEG   <$F0               ;
CF8E: F0 F0 00      SUBB  $F000              ;
CF91: EE E0         LDU   ,S+                ;
CF93: E0 E0         SUBB  ,S+                ;
CF95: EE 00         LDU   0,X                ;
CF97: E0 E0         SUBB  ,S+                ;
CF99: E0 E0         SUBB  ,S+                ;
CF9B: E0 00         SUBB  0,X                ;
CF9D: DD D0         STD   <$D0               ;
CF9F: D0 D0         SUBB  <$D0               ;
CFA1: DD 00         STD   <$00               ;
CFA3: D0 D0         SUBB  <$D0               ;
CFA5: D0 D0         SUBB  <$D0               ;
CFA7: D0 00         SUBB  <$00               ;
CFA9: 0F 0F         CLR   <$0F               ;
CFAB: 0F 00         CLR   <$00               ;
CFAD: 0F 00         CLR   <$00               ;
CFAF: FF 00 FF      STU   $00FF              ;
CFB2: 0F FF         CLR   <$FF               ;
CFB4: 00 0E         NEG   <$0E               ;
CFB6: 0E 0E         JMP   <$0E               ;
CFB8: 0E 0E         JMP   <$0E               ;
CFBA: 00 EE         NEG   <$EE               ;
CFBC: 0E 0E         JMP   <$0E               ;
CFBE: 0E EE         JMP   <$EE               ;
CFC0: 00 0D         NEG   <$0D               ;
CFC2: 0D 0D         TST   <$0D               ;
CFC4: 0D 0D         TST   <$0D               ;
CFC6: 00 DD         NEG   <$DD               ;
CFC8: 0D 0D         TST   <$0D               ;
CFCA: 0D DD         TST   <$DD               ;
CFCC: 00 1C         NEG   <$1C               ;
CFCE: 0D 7F         TST   <$7F               ;
CFD0: E7 70         STB   -16,S              ;
CFD2: 00 0F         NEG   <$0F               ;
CFD4: 71 
CFD5: 71 
CFD6: 07 DC         ASR   <$DC               ;
CFD8: 77 7C 0D      ASR   $7C0D              ;
CFDB: 71 
CFDC: C7 
CFDD: 77 DE 07      ASR   $DE07              ;
CFE0: 71 
CFE1: 17 17 DE      LBSR  $E7C2              ;
CFE4: F7 71 17      STB   $7117              ;
CFE7: 71 
CFE8: 7C DE F0      INC   $DEF0              ;
CFEB: 07 77         ASR   <$77               ;
CFED: C7 
CFEE: 71 
CFEF: 17 70 70      LBSR  $14062             ;
CFF2: 7C D7 77      INC   $D777              ;
CFF5: 77 70 01      ASR   $7001              ;
CFF8: CD 
CFF9: FF D7 70      STU   $D770              ;
CFFC: F0 00 00      SUBB  $0000              ;
CFFF: 00 
```
