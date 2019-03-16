![Defender Bank 3](Defender.jpg)

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

# Bank3

(write 3 to $D000)

```plainCode
;Jump table
C000: 7E C0 76      JMP   $C076              ;
C003: 7E C0 9C      JMP   $C09C              ;
C006: 7E C0 B8      JMP   $C0B8              ;
C009: 7E C0 FC      JMP   $C0FC              ;
C00C: 7E CB E6      JMP   $CBE6              ;
C00F: 7E CB E0      JMP   $CBE0              ;
C012: 7E CC 2C      JMP   $CC2C              ;
C015: 7E CC 20      JMP   $CC20              ;
C018: 7E CC 26      JMP   $CC26              ;
C01B: 7E CC AF      JMP   $CCAF              ;
C01E: 7E CB AF      JMP   $CBAF              ;
C021: 7E C7 99      JMP   $C799              ;
C024: 7E C1 27      JMP   $C127              ;
C027: 7E C1 46      JMP   $C146              ;
C02A: 7E C2 3D      JMP   $C23D              ;
C02D: 7E C2 C3      JMP   $C2C3              ;
C030: 7E C4 06      JMP   $C406              ;
C033: 7E CC C1      JMP   $CCC1              ;
WriteIOPortX3
C036: 7E FF D4      JMP   WriteIOPortX       ;
ReadIOPortX3
C039: 7E FF D7      JMP   ReadIOPortX        ;



;SUBRTN  called 24 times from within this ROM
C03C: BD FF CE      JSR   CallOtherPageX         ;
C03F: C0 02                                  ;   $C002         ;subroutine address goes to $CAA7
C041: 02                                     ;   2             ;ROM page #
C042: 39            RTS                      ;

;it follows the pattern, but nothing uses it? seems unlikely?
C043: BD FF CE      JSR   CallOtherPageX         ;
C046: C0 05                                  ;   $C005         ;subroutine address goes to $CAB2
C048: 02                                     ;   2             ;ROM page # 
C049: 39            RTS                      ;

;SUBRTN  called 4 times from within this ROM
C04A: BD FF CE      JSR   CallOtherPageX         ;
C04D: C0 0E                                  ;   $C00E         ;subroutine address goes to $CBC1
C04F: 02                                     ;   2             ;ROM page #
C050: 39            RTS                      ;

;SUBRTN  called 1 time from within this ROM
C051: BD FF CE      JSR   CallOtherPageX         ;
C054: C0 11                                  ;   $C011         ;subroutine address goes to $CBCC
C056: 02                                     ;   2             ;ROM page # 
C057: 39            RTS                      ;

;SUBRTN  called 1 time from within this ROM
C058: BD FF CE      JSR   CallOtherPageX         ;
C05B: C0 1A                                  ;   $C01A         ;subroutine address goes to $CA79
C05D: 02                                     ;   2             ;ROM page # 
C05E: 39            RTS                      ;

;SUBRTN  called 1 time from within this ROM
C05F: BD FF CE      JSR   CallOtherPageX         ;
C062: C0 1D                                  ;   $C01D         ;subroutine address goes to $CA81
C064: 02                                     ;   2             ;ROM page # 
C065: 39            RTS                      ;

;SUBRTN  called 1 time from within this ROM
C066: BD FF CE      JSR   CallOtherPageX         ;
C069: C0 20                                  ;   $C020         ;subroutine address goes to $CA51
C06B: 02                                     ;   2             ;ROM page # 
C06C: 39            RTS                      ;

;SUBRTN  called 16 times from within this ROM
C06D: BD FF CE      JSR   CallOtherPageX         ;
C070: C0 23                                  ;   $C023         ;subroutine address goes to $CA58
C072: 02                                     ;   2             ;ROM page # 
C073: 39            RTS                      ;



C074: D9 FF         ADCB  <$FF               ;


;SUBRTN  in jump table
C076: BD CA 2A      JSR   $CA2A              ;clear the video memory
C079: C6 7A         LDB   #$7A               ;
C07B: BD C7 93      JSR   $C793              ;write $7A to $C001 (2nd color register)
C07E: CE C0 69      LDU   #$C069             ;"INITIAL TESTS INDICATE UNIT OK" message
C081: 8E 28 70      LDX   #$2870             ;
C084: BD C0 3C      JSR   $C03C              ;
C087: CE C0 6B      LDU   #$C06B             ;
C08A: 8E 40 90      LDX   #$4090             ;
C08D: BD C0 3C      JSR   $C03C              ;
C090: C6 0F         LDB   #$0F               ;
C092: BD CA C8      JSR   $CAC8              ;
C095: 10 8E 0B B8   LDY   #$0BB8             ;
C099: 7E CA 44      JMP   $CA44              ;

;SUBRTN  in jump table
C09C: BD CA 2A      JSR   $CA2A              ;
C09F: C6 57         LDB   #$57               ;
C0A1: BD C7 93      JSR   $C793              ;
C0A4: CE C0 69      LDU   #$C069             ;
C0A7: 8E 28 70      LDX   #$2870             ;
C0AA: BD C0 3C      JSR   $C03C              ;
C0AD: CE C0 73      LDU   #$C073             ;
C0B0: 8E 38 90      LDX   #$3890             ;
C0B3: BD C0 3C      JSR   $C03C              ;
C0B6: 20 29         BRA   $C0E1              ;

;SUBRTN  in jump table
C0B8: BD CA 2A      JSR   $CA2A              ;
C0BB: C6 57         LDB   #$57               ;
C0BD: BD C7 93      JSR   $C793              ;
C0C0: CE C0 69      LDU   #$C069             ;
C0C3: 8E 28 60      LDX   #$2860             ;
C0C6: BD C0 3C      JSR   $C03C              ;
C0C9: CE C0 71      LDU   #$C071             ;
C0CC: 8E 38 80      LDX   #$3880             ;
C0CF: BD C0 3C      JSR   $C03C              ;
C0D2: 1F B8         TFR   DP,A               ;
C0D4: 81 9E         CMPA  #$9E               ;
C0D6: 27 09         BEQ   $C0E1              ;
C0D8: CE C0 73      LDU   #$C073             ;
C0DB: 8E 38 A0      LDX   #$38A0             ;
C0DE: BD C0 3C      JSR   $C03C              ;
C0E1: 10 8E 0B B8   LDY   #$0BB8             ;
C0E5: BD CA 57      JSR   $CA57              ;
C0E8: 8E CC 00      LDX   #$CC00             ;
C0EB: BD C0 39      JSR   ReadIOPortX3       ;
C0EE: C5 02         BITB  #$02               ;
C0F0: 27 05         BEQ   $C0F7              ;
C0F2: 54            LSRB                     ;
C0F3: 25 06         BCS   $C0FB              ;
C0F5: 20 4F         BRA   $C146              ;
C0F7: 31 3F         LEAY  -1,Y               ;
C0F9: 26 EA         BNE   $C0E5              ;
C0FB: 39            RTS                      ;
;in jump table
C0FC: 1C EF         ANDCC #$EF               ;
C0FE: 8E C4 7F      LDX   #$C47F             ;
C101: BD FF A4      JSR   SRAMByteRdX        ;
C104: C1 5A         CMPB  #$5A               ;
C106: 26 36         BNE   $C13E              ;
C108: 8E C4 00      LDX   #$C400             ;
C10B: BD C0 39      JSR   ReadIOPortX3       ;
C10E: C4 0F         ANDB  #$0F               ;
C110: 26 01         BNE   $C113              ;
C112: 39            RTS                      ;
C113: 5F            CLRB                     ;
C114: BD C0 36      JSR   WriteIOPortX3      ;
C117: 8E C4 7D      LDX   #$C47D             ;
C11A: BD FF A4      JSR   SRAMByteRdX        ;
C11D: 4F            CLRA                     ;
C11E: 30 1E         LEAX  -2,X               ;
C120: BD FF AA      JSR   WrSRAMbyteX        ;
C123: C1 15         CMPB  #$15               ;
C125: 26 04         BNE   $C12B              ;
;can't find anything that calls it, but it is in the jump table
C127: 1C 7F         ANDCC #$7F               ;
C129: 20 1B         BRA   $C146              ;
C12B: C1 25         CMPB  #$25               ;
C12D: 26 03         BNE   $C132              ;
C12F: 7E CC AF      JMP   $CCAF              ;
C132: C1 35         CMPB  #$35               ;
C134: 26 03         BNE   $C139              ;
C136: 7E CB BF      JMP   $CBBF              ;
C139: C1 45         CMPB  #$45               ;
C13B: 27 01         BEQ   $C13E              ;
C13D: 39            RTS                      ;
C13E: 32 62         LEAS  2,S                ;bypassing a return address?
C140: BD CB CF      JSR   $CBCF              ;
C143: 7E C7 99      JMP   $C799              ;
;in jump table
C146: 1A 10         ORCC  #$10               ;
C148: BD CA 2A      JSR   $CA2A              ;
C14B: BD FF BF      JSR   $FFBF              ;
C14E: 34 40         PSHS  U                  ;
C150: FE FF 9F      LDU   $FF9F              ;
C153: 33 C8 18      LEAU  $18,U              ;
C156: DF 43         STU   <$43               ;
C158: 35 40         PULS  U                  ;
C15A: 11 93 43      CMPU  <$43               ;
C15D: 27 70         BEQ   $C1CF              ;
C15F: DF 5B         STU   <$5B               ;
C161: C6 08         LDB   #$08               ;
C163: BD CA AA      JSR   $CAAA              ;
C166: C6 57         LDB   #$57               ;
C168: BD C7 93      JSR   $C793              ;
C16B: CE C0 71      LDU   #$C071             ;
C16E: 8E 38 60      LDX   #$3860             ;
C171: BD C0 3C      JSR   $C03C              ;
C174: 10 8E C0 35   LDY   #$C035             ;
C178: BD C0 6D      JSR   $C06D              ;
C17B: CC 42 66      LDD   #$4266             ;
C17E: DD 4A         STD   <$4A               ;
C180: 9E 4A         LDX   <$4A               ;
C182: 30 0A         LEAX  10,X               ;
C184: 9F 4A         STX   <$4A               ;
C186: CE C0 6D      LDU   #$C06D             ;
C189: BD C0 3C      JSR   $C03C              ;
C18C: FE FF 9F      LDU   $FF9F              ;
C18F: DF 43         STU   <$43               ;
C191: DE 5B         LDU   <$5B               ;
C193: DC 5B         LDD   <$5B               ;
C195: 93 43         SUBD  <$43               ;
C197: 54            LSRB                     ;
C198: 25 02         BCS   $C19C              ;
C19A: 33 41         LEAU  1,U                ;
C19C: 5C            INCB                     ;
C19D: D7 3A         STB   <$3A               ;
C19F: BD CB 23      JSR   $CB23              ;
C1A2: 9E 50         LDX   <$50               ;
C1A4: BD C0 4A      JSR   $C04A              ;
C1A7: BD CA 69      JSR   $CA69              ;
C1AA: BD FF C2      JSR   $FFC2              ;
C1AD: DF 5B         STU   <$5B               ;
C1AF: FE FF 9F      LDU   $FF9F              ;
C1B2: 33 C8 18      LEAU  $18,U              ;
C1B5: 11 93 5B      CMPU  <$5B               ;
C1B8: 26 C6         BNE   $C180              ;
C1BA: BD CA 0E      JSR   $CA0E              ;
C1BD: 0D 49         TST   <$49               ;
C1BF: 26 30         BNE   $C1F1              ;
C1C1: D6 3A         LDB   <$3A               ;
C1C3: BD CA AA      JSR   $CAAA              ;
C1C6: 10 8E C0 39   LDY   #ReadIOPortX3      ;
C1CA: BD C0 6D      JSR   $C06D              ;
C1CD: 20 1F         BRA   $C1EE              ;
C1CF: 1F A9         TFR   CCR,B              ;
C1D1: 5D            TSTB                     ;
C1D2: 2A 3E         BPL   $C212              ;
C1D4: C6 7A         LDB   #$7A               ;
C1D6: BD C7 93      JSR   $C793              ;
C1D9: CE C0 77      LDU   #$C077             ;
C1DC: 8E 38 80      LDX   #$3880             ;
C1DF: BD C0 3C      JSR   $C03C              ;
C1E2: 10 8E C0 39   LDY   #ReadIOPortX3      ;
C1E6: BD C0 6D      JSR   $C06D              ;
C1E9: C6 08         LDB   #$08               ;
C1EB: BD CA C8      JSR   $CAC8              ;
C1EE: BD CA 39      JSR   $CA39              ;
C1F1: BD CA 2A      JSR   $CA2A              ;
C1F4: 5F            CLRB                     ;
C1F5: BD CA AA      JSR   $CAAA              ;
C1F8: BD C7 91      JSR   $C791              ;
C1FB: CE C0 79      LDU   #$C079             ;
C1FE: 8E 40 80      LDX   #$4080             ;
C201: BD C0 3C      JSR   $C03C              ;
C204: 10 8E C0 3D   LDY   #$C03D             ;
C208: BD C0 6D      JSR   $C06D              ;
C20B: 10 8E 13 88   LDY   #$1388             ;
C20F: BD CA 44      JSR   $CA44              ;
C212: BD CA 57      JSR   $CA57              ;
C215: 0D 49         TST   <$49               ;
C217: 10 26 00 D7   LBNE  $C2F2              ;
C21B: 0D 47         TST   <$47               ;
C21D: 26 F3         BNE   $C212              ;
C21F: 8E C0 00      LDX   #$C000             ;
C222: C6 C0         LDB   #$C0               ;
C224: BD C0 36      JSR   WriteIOPortX3      ;
C227: 86 B5         LDA   #$B5               ;
C229: 3D            MUL                      ;
C22A: 1E 89         EXG   A,B                ;
C22C: 30 01         LEAX  1,X                ;
C22E: 8C C0 10      CMPX  #$C010             ;
C231: 26 F1         BNE   $C224              ;
C233: CC 00 00      LDD   #$0000             ;
C236: 10 8E 00 0A   LDY   #$000A             ;
C23A: 7E FF C5      JMP   RAMTestX           ;RAM test
;in jump table
C23D: 1F 20         TFR   Y,D                ;
C23F: E8 82         EORB  ,-X                ;
C241: A8 82         EORA  ,-X                ;
C243: DD 41         STD   <$41               ;
C245: 9F 43         STX   <$43               ;
C247: BD CA F9      JSR   BlkOutClrRegs      ;
C24A: BD FF BC      JSR   VidMemClrX         ;
C24D: BD CA E4      JSR   $CAE4              ;
C250: BD CA 69      JSR   $CA69              ;
C253: C6 04         LDB   #$04               ;
C255: BD CA AA      JSR   $CAAA              ;
C258: C6 57         LDB   #$57               ;
C25A: BD C7 93      JSR   $C793              ;
C25D: CE C0 73      LDU   #$C073             ;
C260: 8E 38 70      LDX   #$3870             ;
C263: BD C0 3C      JSR   $C03C              ;
C266: 10 8E C0 41   LDY   #$C041             ;
C26A: BD C0 6D      JSR   $C06D              ;
C26D: DC 41         LDD   <$41               ;
C26F: 4D            TSTA                     ;
C270: 26 02         BNE   $C274              ;
C272: 1F 98         TFR   B,A                ;
C274: 5F            CLRB                     ;
C275: 5C            INCB                     ;
C276: 44            LSRA                     ;
C277: 24 FC         BCC   $C275              ;
C279: D7 3A         STB   <$3A               ;
C27B: DC 43         LDD   <$43               ;
C27D: 80 03         SUBA  #$03               ;
C27F: 24 FC         BCC   $C27D              ;
C281: 8B 04         ADDA  #$04               ;
C283: 97 3B         STA   <$3B               ;
C285: CE C0 6F      LDU   #$C06F             ;
C288: 8E 42 90      LDX   #$4290             ;
C28B: BD C0 3C      JSR   $C03C              ;
C28E: D6 3B         LDB   <$3B               ;
C290: 58            ASLB                     ;
C291: 58            ASLB                     ;
C292: 58            ASLB                     ;
C293: 58            ASLB                     ;
C294: DB 3A         ADDB  <$3A               ;
C296: 4F            CLRA                     ;
C297: 9E 50         LDX   <$50               ;
C299: BD C0 4A      JSR   $C04A              ;
C29C: BD CA 0E      JSR   $CA0E              ;
C29F: 0D 49         TST   <$49               ;
C2A1: 26 4F         BNE   $C2F2              ;
C2A3: 96 3B         LDA   <$3B               ;
C2A5: C6 10         LDB   #$10               ;
C2A7: 54            LSRB                     ;
C2A8: 4A            DECA                     ;
C2A9: 26 FC         BNE   $C2A7              ;
C2AB: BD CA AA      JSR   $CAAA              ;
C2AE: BD CA 0E      JSR   $CA0E              ;
C2B1: 0D 49         TST   <$49               ;
C2B3: 26 3D         BNE   $C2F2              ;
C2B5: D6 3A         LDB   <$3A               ;
C2B7: BD CA AA      JSR   $CAAA              ;
C2BA: 10 8E C0 45   LDY   #$C045             ;
C2BE: BD C0 6D      JSR   $C06D              ;
C2C1: 20 2C         BRA   $C2EF              ;
;in jump table
C2C3: BD CA F9      JSR   BlkOutClrRegs      ;
C2C6: BD FF BC      JSR   VidMemClrX         ;
C2C9: BD CA E4      JSR   $CAE4              ;
C2CC: BD CA 69      JSR   $CA69              ;
C2CF: 10 8C 00 0A   CMPY  #$000A             ;
C2D3: 27 1D         BEQ   $C2F2              ;
C2D5: C6 7A         LDB   #$7A               ;
C2D7: BD C7 93      JSR   $C793              ;
C2DA: CE C0 7B      LDU   #$C07B             ;
C2DD: 8E 28 80      LDX   #$2880             ;
C2E0: BD C0 3C      JSR   $C03C              ;
C2E3: 10 8E C0 45   LDY   #$C045             ;
C2E7: BD C0 6D      JSR   $C06D              ;
C2EA: C6 04         LDB   #$04               ;
C2EC: BD CA C8      JSR   $CAC8              ;
C2EF: BD CA 39      JSR   $CA39              ;
C2F2: BD CA 2A      JSR   $CA2A              ;
C2F5: 1F B8         TFR   DP,A               ;
C2F7: 81 A2         CMPA  #$A2               ;
C2F9: 26 1D         BNE   $C318              ;
C2FB: C6 02         LDB   #$02               ;
C2FD: BD CA AA      JSR   $CAAA              ;
C300: C6 57         LDB   #$57               ;
C302: BD C7 93      JSR   $C793              ;
C305: CE C0 81      LDU   #$C081             ;
C308: 8E 28 80      LDX   #$2880             ;
C30B: BD C0 3C      JSR   $C03C              ;
C30E: 10 8E C0 49   LDY   #$C049             ;
C312: BD C0 6D      JSR   $C06D              ;
C315: 7E C3 BB      JMP   $C3BB              ;
C318: 8B 03         ADDA  #$03               ;
C31A: 5F            CLRB                     ;
C31B: DD 41         STD   <$41               ;
C31D: DE 41         LDU   <$41               ;
C31F: 8E C4 00      LDX   #$C400             ;
C322: BD C0 39      JSR   ReadIOPortX3       ;
C325: E7 C0         STB   ,U+                ;
C327: 30 01         LEAX  1,X                ;
C329: 8C C5 00      CMPX  #$C500             ;
C32C: 26 F4         BNE   $C322              ;
C32E: CC 00 10      LDD   #$0010             ;
C331: D7 3A         STB   <$3A               ;
C333: 4F            CLRA                     ;
C334: 8E C4 00      LDX   #$C400             ;
C337: D6 3A         LDB   <$3A               ;
C339: BD C0 36      JSR   WriteIOPortX3      ;
C33C: 30 01         LEAX  1,X                ;
C33E: 5C            INCB                     ;
C33F: D1 3A         CMPB  <$3A               ;
C341: 26 F6         BNE   $C339              ;
C343: 8E C4 00      LDX   #$C400             ;
C346: 4C            INCA                     ;
C347: BD C0 39      JSR   ReadIOPortX3       ;
C34A: D7 3B         STB   <$3B               ;
C34C: 30 01         LEAX  1,X                ;
C34E: BD C0 39      JSR   ReadIOPortX3       ;
C351: D0 3B         SUBB  <$3B               ;
C353: 5A            DECB                     ;
C354: C4 0F         ANDB  #$0F               ;
C356: 26 0E         BNE   $C366              ;
C358: 4C            INCA                     ;
C359: 26 EC         BNE   $C347              ;
C35B: BD CA 69      JSR   $CA69              ;
C35E: 0D 49         TST   <$49               ;
C360: 26 04         BNE   $C366              ;
C362: 0A 3A         DEC   <$3A               ;
C364: 26 CE         BNE   $C334              ;
C366: DE 41         LDU   <$41               ;
C368: 8E C4 00      LDX   #$C400             ;
C36B: E6 C0         LDB   ,U+                ;
C36D: BD C0 36      JSR   WriteIOPortX3      ;
C370: 30 01         LEAX  1,X                ;
C372: 8C C5 00      CMPX  #$C500             ;
C375: 26 F4         BNE   $C36B              ;
C377: 0D 49         TST   <$49               ;
C379: 26 43         BNE   $C3BE              ;
C37B: 96 3A         LDA   <$3A               ;
C37D: 27 22         BEQ   $C3A1              ;
C37F: C6 02         LDB   #$02               ;
C381: BD CA AA      JSR   $CAAA              ;
C384: C6 57         LDB   #$57               ;
C386: BD C7 93      JSR   $C793              ;
C389: BD CA 69      JSR   $CA69              ;
C38C: CE C0 7D      LDU   #$C07D             ;
C38F: 8E 30 80      LDX   #$3080             ;
C392: BD C0 3C      JSR   $C03C              ;
C395: BD CA 69      JSR   $CA69              ;
C398: 10 8E C0 49   LDY   #$C049             ;
C39C: BD C0 6D      JSR   $C06D              ;
C39F: 20 1A         BRA   $C3BB              ;
C3A1: C6 7A         LDB   #$7A               ;
C3A3: BD C7 93      JSR   $C793              ;
C3A6: CE C0 7F      LDU   #$C07F             ;
C3A9: 8E 38 80      LDX   #$3880             ;
C3AC: BD C0 3C      JSR   $C03C              ;
C3AF: 10 8E C0 49   LDY   #$C049             ;
C3B3: BD C0 6D      JSR   $C06D              ;
C3B6: C6 02         LDB   #$02               ;
C3B8: BD CA C8      JSR   $CAC8              ;
C3BB: BD CA 39      JSR   $CA39              ;
C3BE: BD CA 2A      JSR   $CA2A              ;
C3C1: C6 01         LDB   #$01               ;
C3C3: BD CA AA      JSR   $CAAA              ;
C3C6: BD C7 91      JSR   $C791              ;
C3C9: CE C0 83      LDU   #$C083             ;
C3CC: 8E 38 80      LDX   #$3880             ;
C3CF: BD C0 3C      JSR   $C03C              ;
C3D2: 10 8E C0 4D   LDY   #$C04D             ;
C3D6: BD C0 6D      JSR   $C06D              ;
C3D9: 10 8E 13 88   LDY   #$1388             ;
C3DD: BD CA 44      JSR   $CA44              ;
C3E0: BD CB 67      JSR   $CB67              ;
C3E3: 10 8E 07 D0   LDY   #$07D0             ;
C3E7: CE C9 D8      LDU   #$C9D8             ;
C3EA: E6 C0         LDB   ,U+                ;
C3EC: 8E C0 00      LDX   #$C000             ;
C3EF: BD C0 36      JSR   WriteIOPortX3      ;
C3F2: 30 01         LEAX  1,X                ;
C3F4: 8C C0 10      CMPX  #$C010             ;
C3F7: 26 F6         BNE   $C3EF              ;
C3F9: BD CA 44      JSR   $CA44              ;
C3FC: 11 83 C9 E0   CMPU  #$C9E0             ;
C400: 26 E8         BNE   $C3EA              ;
C402: 0D 49         TST   <$49               ;
C404: 27 E1         BEQ   $C3E7              ;
;in jump table
C406: BD CA 2A      JSR   $CA2A              ;
C409: 5F            CLRB                     ;
C40A: D7 41         STB   <$41               ;
C40C: D7 42         STB   <$42               ;
C40E: BD CA AA      JSR   $CAAA              ;
C411: BD C7 91      JSR   $C791              ;
C414: CE C0 85      LDU   #$C085             ;
C417: 8E 40 78      LDX   #$4078             ;
C41A: BD C0 3C      JSR   $C03C              ;
C41D: 10 8E C0 55   LDY   #$C055             ;
C421: BD C0 6D      JSR   $C06D              ;
C424: 10 8E 00 01   LDY   #$0001             ;
C428: CE C9 F0      LDU   #$C9F0             ;
C42B: 4F            CLRA                     ;
C42C: 8E CC 00      LDX   #$CC00             ;
C42F: BD C0 39      JSR   ReadIOPortX3       ;
C432: C5 01         BITB  #$01               ;
C434: 26 09         BNE   $C43F              ;
C436: C5 02         BITB  #$02               ;
C438: 26 15         BNE   $C44F              ;
C43A: BD CA 57      JSR   $CA57              ;
C43D: 20 ED         BRA   $C42C              ;
C43F: BD CA 44      JSR   $CA44              ;
C442: 4C            INCA                     ;
C443: A1 C4         CMPA  ,U                 ;
C445: 26 04         BNE   $C44B              ;
C447: 33 41         LEAU  1,U                ;
C449: 20 F7         BRA   $C442              ;
C44B: 97 3A         STA   <$3A               ;
C44D: 88 3F         EORA  #$3F               ;
C44F: C6 13         LDB   #$13               ;
C451: BD CB 0B      JSR   $CB0B              ;
C454: 0D 49         TST   <$49               ;
C456: 26 2E         BNE   $C486              ;
C458: D6 3A         LDB   <$3A               ;
C45A: BD CB 0B      JSR   $CB0B              ;
C45D: 10 8E 03 E8   LDY   #$03E8             ;
C461: DC 41         LDD   <$41               ;
C463: 8E 5A 8C      LDX   #$5A8C             ;
C466: BD C0 51      JSR   $C051              ;
C469: D6 3A         LDB   <$3A               ;
C46B: BD CB 23      JSR   $CB23              ;
C46E: 4F            CLRA                     ;
C46F: DD 41         STD   <$41               ;
C471: 8E 5A 8C      LDX   #$5A8C             ;
C474: BD C0 4A      JSR   $C04A              ;
C477: 96 3A         LDA   <$3A               ;
C479: 81 1F         CMPA  #$1F               ;
C47B: 26 AF         BNE   $C42C              ;
C47D: 1F A9         TFR   CCR,B              ;
C47F: 5D            TSTB                     ;
C480: 10 2A 01 01   LBPL  $C585              ;
C484: 20 A2         BRA   $C428              ;

C486: BD CA 2A      JSR   $CA2A              ;
C489: BD C7 91      JSR   $C791              ;
C48C: CE C0 87      LDU   #$C087             ;
C48F: 8E 38 20      LDX   #$3820             ;
C492: BD C0 3C      JSR   $C03C              ;
C495: 10 8E C0 59   LDY   #$C059             ;
C499: BD C0 6D      JSR   $C06D              ;
C49C: 1F B8         TFR   DP,A               ;
C49E: C6 62         LDB   #$62               ;
C4A0: DD 41         STD   <$41               ;
C4A2: CB 26         ADDB  #$26               ;
C4A4: 1F 01         TFR   D,X                ;
C4A6: 86 FF         LDA   #$FF               ;
C4A8: A7 82         STA   ,-X                ;
C4AA: 9C 41         CMPX  <$41               ;
C4AC: 26 FA         BNE   $C4A8              ;
C4AE: 0F 5D         CLR   <$5D               ;
C4B0: 0F 5E         CLR   <$5E               ;
C4B2: 0F 5F         CLR   <$5F               ;
C4B4: 0F 60         CLR   <$60               ;
C4B6: 0F 61         CLR   <$61               ;
C4B8: 86 01         LDA   #$01               ;
C4BA: 97 3C         STA   <$3C               ;
C4BC: 8E CC 00      LDX   #$CC00             ;
C4BF: DE 41         LDU   <$41               ;
C4C1: 33 5B         LEAU  -5,U               ;
C4C3: 4F            CLRA                     ;
C4C4: BD C0 39      JSR   ReadIOPortX3       ;
C4C7: 8C CC 06      CMPX  #$CC06             ;
C4CA: 26 02         BNE   $C4CE              ;
C4CC: C4 7F         ANDB  #$7F               ;
C4CE: 81 18         CMPA  #$18               ;
C4D0: 26 02         BNE   $C4D4              ;
C4D2: C4 CF         ANDB  #$CF               ;
C4D4: D7 3A         STB   <$3A               ;
C4D6: E8 C0         EORB  ,U+                ;
C4D8: 26 38         BNE   $C512              ;
C4DA: 8B 08         ADDA  #$08               ;
C4DC: 30 02         LEAX  2,X                ;
C4DE: 8C CC 02      CMPX  #$CC02             ;
C4E1: 27 F9         BEQ   $C4DC              ;
C4E3: 8C CC 08      CMPX  #$CC08             ;
C4E6: 26 DC         BNE   $C4C4              ;
C4E8: 81 28         CMPA  #$28               ;
C4EA: 27 15         BEQ   $C501              ;
C4EC: 30 1E         LEAX  -2,X               ;
C4EE: BD C0 39      JSR   ReadIOPortX3       ;
C4F1: 5D            TSTB                     ;
C4F2: 2A 0D         BPL   $C501              ;
C4F4: C6 34         LDB   #$34               ;
C4F6: 30 01         LEAX  1,X                ;
C4F8: BD C0 36      JSR   WriteIOPortX3      ;
C4FB: 30 1D         LEAX  -3,X               ;
C4FD: 0C 3C         INC   <$3C               ;
C4FF: 20 C3         BRA   $C4C4              ;
C501: C6 3C         LDB   #$3C               ;
C503: 8E CC 07      LDX   #$CC07             ;
C506: BD C0 36      JSR   WriteIOPortX3      ;
C509: BD CA 69      JSR   $CA69              ;
C50C: 0D 49         TST   <$49               ;
C50E: 27 A8         BEQ   $C4B8              ;
C510: 20 73         BRA   $C585              ;
C512: D7 3B         STB   <$3B               ;
C514: C6 01         LDB   #$01               ;
C516: D5 3B         BITB  <$3B               ;
C518: 26 04         BNE   $C51E              ;
C51A: 4C            INCA                     ;
C51B: 58            ASLB                     ;
C51C: 20 F8         BRA   $C516              ;
C51E: 9E 41         LDX   <$41               ;
C520: D5 3A         BITB  <$3A               ;
C522: 26 14         BNE   $C538              ;
C524: E8 C2         EORB  ,-U                ;
C526: E7 C4         STB   ,U                 ;
C528: A1 80         CMPA  ,X+                ;
C52A: 26 FC         BNE   $C528              ;
C52C: 63 82         COM   ,-X                ;
C52E: 8D 3C         BSR   $C56C              ;
C530: CC 38 08      LDD   #$3808             ;
C533: BD FF B9      JSR   ScrnBlkClrX        ;
C536: 20 C9         BRA   $C501              ;
C538: E8 C2         EORB  ,-U                ;
C53A: E7 C4         STB   ,U                 ;
C53C: C6 08         LDB   #$08               ;
C53E: BD CB 0B      JSR   $CB0B              ;
C541: 6D 80         TST   ,X+                ;
C543: 2A FC         BPL   $C541              ;
C545: A7 82         STA   ,-X                ;
C547: 34 02         PSHS  A                  ;
C549: 8D 21         BSR   $C56C              ;
C54B: BD C0 3C      JSR   $C03C              ;
C54E: 35 02         PULS  A                  ;
C550: 81 08         CMPA  #$08               ;
C552: 25 AD         BCS   $C501              ;
C554: 44            LSRA                     ;
C555: 81 06         CMPA  #$06               ;
C557: 27 A8         BEQ   $C501              ;
C559: 8E CC 06      LDX   #$CC06             ;
C55C: BD C0 39      JSR   ReadIOPortX3       ;
C55F: 5D            TSTB                     ;
C560: 2A 9F         BPL   $C501              ;
C562: 9E 50         LDX   <$50               ;
C564: 4F            CLRA                     ;
C565: D6 3C         LDB   <$3C               ;
C567: BD C0 4A      JSR   $C04A              ;
C56A: 20 95         BRA   $C501              ;

;SUBRTN
C56C: CE C0 8B      LDU   #$C08B             ;
C56F: 81 18         CMPA  #$18               ;
C571: 25 02         BCS   $C575              ;
C573: 80 10         SUBA  #$10               ;
C575: 48            ASLA                     ;
C576: 33 C6         LEAU  A,U                ;
C578: 1F 10         TFR   X,D                ;
C57A: 93 41         SUBD  <$41               ;
C57C: 86 0A         LDA   #$0A               ;
C57E: 3D            MUL                      ;
C57F: C3 38 30      ADDD  #$3830             ;
C582: 1F 01         TFR   D,X                ;
C584: 39            RTS                      ;

C585: BD CA 2A      JSR   $CA2A              ;
C588: BD C7 91      JSR   $C791              ;
C58B: CE C0 89      LDU   #$C089             ;
C58E: 8E 28 80      LDX   #$2880             ;
C591: BD C0 3C      JSR   $C03C              ;
C594: 10 8E C0 5D   LDY   #$C05D             ;
C598: BD C0 6D      JSR   $C06D              ;
C59B: 8E CC 00      LDX   #$CC00             ;
C59E: CE C9 F4      LDU   #$C9F4             ;load vector table address
C5A1: BD C0 39      JSR   ReadIOPortX3       ;
C5A4: C5 01         BITB  #$01               ;
C5A6: 27 14         BEQ   $C5BC              ;
C5A8: 10 8E 13 88   LDY   #$1388             ;
C5AC: BD CA 44      JSR   $CA44              ;
C5AF: 0D 49         TST   <$49               ;
C5B1: 10 26 01 E4   LBNE  $C799              ;
C5B5: BD C0 39      JSR   ReadIOPortX3       ;
C5B8: C5 01         BITB  #$01               ;
C5BA: 26 09         BNE   $C5C5              ;
C5BC: BD CA 0E      JSR   $CA0E              ;
C5BF: 0D 49         TST   <$49               ;
C5C1: 10 26 01 D4   LBNE  $C799              ;
C5C5: 34 70         PSHS  U,Y,X              ;
C5C7: AD D4         JSR   [,U]               ;
C5C9: 35 70         PULS  X,Y,U              ;
C5CB: 33 42         LEAU  2,U                ;
C5CD: 11 83 C9 FE   CMPU  #$C9FE             ;
C5D1: 26 CE         BNE   $C5A1              ;
C5D3: 10 8E 13 88   LDY   #$1388             ;
C5D7: BD CA 44      JSR   $CA44              ;
C5DA: 1F A9         TFR   CCR,B              ;
C5DC: 5D            TSTB                     ;
C5DD: 10 2A FB 65   LBPL  $C146              ;
C5E1: 20 BB         BRA   $C59E              ;

;possible vector address
C5E3: BD CA 69      JSR   $CA69              ;
C5E6: BD FF BC      JSR   VidMemClrX         ;
C5E9: BD CA F9      JSR   BlkOutClrRegs      ;
C5EC: 8E C0 01      LDX   #$C001             ;
C5EF: C6 FF         LDB   #$FF               ;
C5F1: BD C0 36      JSR   WriteIOPortX3      ;
C5F4: 8E C0 02      LDX   #$C002             ;
C5F7: C6 C0         LDB   #$C0               ;
C5F9: BD C0 36      JSR   WriteIOPortX3      ;
C5FC: 8E C0 03      LDX   #$C003             ;
C5FF: C6 38         LDB   #$38               ;
C601: BD C0 36      JSR   WriteIOPortX3      ;
C604: 8E C0 04      LDX   #$C004             ;
C607: C6 07         LDB   #$07               ;
C609: BD C0 36      JSR   WriteIOPortX3      ;
C60C: BD CA 69      JSR   $CA69              ;
C60F: 10 8E C6 F7   LDY   #$C6F7             ;
C613: CC 01 01      LDD   #$0101             ;
C616: AE A4         LDX   ,Y                 ;
C618: ED 81         STD   ,X++               ;
C61A: AC 22         CMPX  2,Y                ;
C61C: 26 FA         BNE   $C618              ;
C61E: 31 24         LEAY  4,Y                ;
C620: 10 8C C7 1F   CMPY  #$C71F             ;
C624: 26 F0         BNE   $C616              ;
C626: BD CA 69      JSR   $CA69              ;
C629: 86 11         LDA   #$11               ;
C62B: 10 8E C6 D7   LDY   #$C6D7             ;
C62F: AE A4         LDX   ,Y                 ;
C631: 9F 45         STX   <$45               ;
C633: A7 84         STA   ,X                 ;
C635: 0C 45         INC   <$45               ;
C637: 9E 45         LDX   <$45               ;
C639: AC 22         CMPX  2,Y                ;
C63B: 26 F6         BNE   $C633              ;
C63D: 31 24         LEAY  4,Y                ;
C63F: 10 8C C6 F7   CMPY  #$C6F7             ;
C643: 26 EA         BNE   $C62F              ;
C645: BD CA 69      JSR   $CA69              ;
C648: 10 8E C7 1F   LDY   #$C71F             ;
C64C: AE A4         LDX   ,Y                 ;
C64E: 9F 45         STX   <$45               ;
C650: A6 24         LDA   4,Y                ;
C652: A7 84         STA   ,X                 ;
C654: 0C 45         INC   <$45               ;
C656: 9E 45         LDX   <$45               ;
C658: AC 22         CMPX  2,Y                ;
C65A: 26 F6         BNE   $C652              ;
C65C: 31 25         LEAY  5,Y                ;
C65E: 10 8C C7 5B   CMPY  #$C75B             ;
C662: 26 E8         BNE   $C64C              ;
C664: BD CA 69      JSR   $CA69              ;
C667: 10 8E C7 5B   LDY   #$C75B             ;
C66B: AE A4         LDX   ,Y                 ;
C66D: A6 24         LDA   4,Y                ;
C66F: A7 80         STA   ,X+                ;
C671: AC 22         CMPX  2,Y                ;
C673: 26 FA         BNE   $C66F              ;
C675: 31 25         LEAY  5,Y                ;
C677: 10 8C C7 6F   CMPY  #$C76F             ;
C67B: 26 EE         BNE   $C66B              ;
C67D: BD CA 69      JSR   $CA69              ;
C680: 86 21         LDA   #$21               ;
C682: B7 46 7E      STA   $467E              ;
C685: 86 20         LDA   #$20               ;
C687: B7 96 7E      STA   $967E              ;
C68A: 8E 4E 0A      LDX   #$4E0A             ;
C68D: A6 84         LDA   ,X                 ;
C68F: 84 F0         ANDA  #$F0               ;
C691: 8A 02         ORA   #$02               ;
C693: A7 80         STA   ,X+                ;
C695: 8C 4E 6D      CMPX  #$4E6D             ;
C698: 26 F3         BNE   $C68D              ;
C69A: 8E 4E 90      LDX   #$4E90             ;
C69D: A6 84         LDA   ,X                 ;
C69F: 84 F0         ANDA  #$F0               ;
C6A1: 8A 02         ORA   #$02               ;
C6A3: A7 80         STA   ,X+                ;
C6A5: 8C 4E F3      CMPX  #$4EF3             ;
C6A8: 26 F3         BNE   $C69D              ;
C6AA: BD CA 69      JSR   $CA69              ;
C6AD: 8E 0E 18      LDX   #$0E18             ;
C6B0: 9F 45         STX   <$45               ;
C6B2: 9E 45         LDX   <$45               ;
C6B4: A6 84         LDA   ,X                 ;
C6B6: 84 F0         ANDA  #$F0               ;
C6B8: 8A 01         ORA   #$01               ;
C6BA: A7 84         STA   ,X                 ;
C6BC: D6 46         LDB   <$46               ;
C6BE: CB 22         ADDB  #$22               ;
C6C0: 25 04         BCS   $C6C6              ;
C6C2: D7 46         STB   <$46               ;
C6C4: 20 EC         BRA   $C6B2              ;
C6C6: C6 18         LDB   #$18               ;
C6C8: D7 46         STB   <$46               ;
C6CA: D6 45         LDB   <$45               ;
C6CC: CB 10         ADDB  #$10               ;
C6CE: D7 45         STB   <$45               ;
C6D0: C1 9E         CMPB  #$9E               ;
C6D2: 26 DE         BNE   $C6B2              ;
C6D4: 7E CA 69      JMP   $CA69              ;a jump to this subroutine means this will return somewhere else



;data table
C6D7: 07 07         ASR   <$07               ;
C6D9: 97 07         STA   <$07               ;
C6DB: 07 29         ASR   <$29               ;
C6DD: 97 29         STA   <$29               ;
C6DF: 07 4B         ASR   <$4B               ;
C6E1: 97 4B         STA   <$4B               ;
C6E3: 07 6D         ASR   <$6D               ;
C6E5: 97 6D         STA   <$6D               ;
C6E7: 07 8F         ASR   <$8F               ;
C6E9: 97 8F         STA   <$8F               ;
C6EB: 07 B1         ASR   <$B1               ;
C6ED: 97 B1         STA   <$B1               ;
C6EF: 07 D3         ASR   <$D3               ;
C6F1: 97 D3         STA   <$D3               ;
C6F3: 07 F5         ASR   <$F5               ;
C6F5: 97 F5         STA   <$F5               ;
C6F7: 06 07         ROR   <$07               ;
C6F9: 06 F5         ROR   <$F5               ;
C6FB: 16 07 16      LBRA  $CE14              ;
C6FE: F5 26 07      BITB  $2607              ;
C701: 26 F5         BNE   $C6F8              ;
C703: 36 07         PSHU  B,A,CC             ;
C705: 36 F5         PSHU  PC,S,Y,X,B,CC      ;
C707: 46            RORA                     ;
C708: 07 46         ASR   <$46               ;
C70A: F5 56 07      BITB  $5607              ;
C70D: 56            RORB                     ;
C70E: F5 66 07      BITB  $6607              ;
C711: 66 F5         ROR   [B,S]              ;
C713: 76 07 76      ROR   $0776              ;
C716: F5 86 07      BITB  $8607              ;
C719: 86 F5         LDA   #$F5               ;
C71B: 96 07         LDA   <$07               ;
C71D: 96 F5         LDA   <$F5               ;

data in 5 byte packets

C71F: 48            ASLA                     ;
C720: 05 
C721: 55 
C722: 05 
C723: 44            LSRA                     ;
C724: 48            ASLA                     ;
C725: 06 55         ROR   <$55               ;
C727: 06 44         ROR   <$44               ;
C729: 48            ASLA                     ;
C72A: 07 55         ASR   <$55               ;
C72C: 07 00         ASR   <$00               ;
C72E: 48            ASLA                     ;
C72F: 08 55         LSL   <$55               ;
C731: 08 33         LSL   <$33               ;
C733: 48            ASLA                     ;
C734: 09 55         ROL   <$55               ;
C736: 09 33         ROL   <$33               ;
C738: 48            ASLA                     ;

C739: F3 55 F3      ADDD  $55F3              ;
C73C: 33 48         LEAU  8,U                ;

C73E: F4 55 F4      ANDB  $55F4              ;
C741: 33 48         LEAU  8,U                ;

C743: F5 55 F5      BITB  $55F5              ;
C746: 00 48         NEG   <$48               ;

C748: F6 55 F6      LDB   $55F6              ;
C74B: 44            LSRA                     ;
C74C: 48            ASLA                     ;

C74D: F7 55 F7      STB   $55F7              ;
C750: 44            LSRA                     ;
C751: 07 

C752: 7E 46         RORA                     ;
C754: 7E 22 57      JMP   $2257              ;

C757: 7E 96 7E      JMP   $967E              ;
C75A: 22 05         BHI   $C761              ;

C75C: 6F 05         CLR   5,X                ;
C75E: 8E 04 06      LDX   #$0406             ;
C761: 6F 06         CLR   6,X                ;
C763: 8E 30 96      LDX   #$3096             ;
C766: 6F 96         CLR   [A,X]              ;
C768: 8E 00 97      LDX   #$0097             ;
C76B: 6F 
C76C: 97 8E         STA   <$8E               ;
C76E: 34

4 of 5 vectors located at $C9F4-$C9FD are in this block. The first one in the table is elsewhere, at $C5E3

;possible vector address
C76F: BD FF BC      JSR   VidMemClrX         ;
C772: C6 05         LDB   #$05
C774: 8E C0 00      LDX   #$C000             ;
C777: 8D 03         BSR   $C77C              ;
C779: 8E C0 0C      LDX   #$C00C             ;
C77C: 7E C0 36      JMP   WriteIOPortX3      ;we want this to return elsewhere so we call it with a JMP instead of BSR, LBSR, or JSR

;possible vector address
C77F: C6 28         LDB   #$28               ;
C781: 20 F1         BRA   $C774              ;
;possible vector address
C783: C6 80         LDB   #$80               ;
C785: 20 ED         BRA   $C774              ;
;possible vector address
C787: 10 8E C9 FE   LDY   #$C9FE             ;
C78B: BD CA 97      JSR   $CA97              ;
C78E: 7E CB 3B      JMP   $CB3B              ;



;SUBRTN    6 times in this ROM
C791: C6 A5         LDB   #$A5               ;
;SUBRTN    9 times in this ROM
C793: 8E C0 01      LDX   #$C001             ;
C796: 7E C0 36      JMP   WriteIOPortX3      ;we want this to return elsewhere so we call it with a JMP instead of BSR, LBSR, or JSR



;4 times in this ROM, in jump table
C799: BD CA 69      JSR   $CA69              ;
C79C: BD CA 2A      JSR   $CA2A              ;
C79F: 8D F0         BSR   $C791              ;
C7A1: CE C0 D7      LDU   #$C0D7             ;
C7A4: 8E 28 20      LDX   #$2820             ;
C7A7: BD CA 69      JSR   $CA69              ;
C7AA: BD C0 3C      JSR   $C03C              ;
C7AD: 10 8E C0 61   LDY   #$C061             ;
C7B1: BD C0 6D      JSR   $C06D              ;
C7B4: 10 8E 05 DC   LDY   #$05DC             ;
C7B8: BD CA 44      JSR   $CA44              ;
C7BB: 0D 49         TST   <$49               ;
C7BD: 26 60         BNE   $C81F              ;
C7BF: 0F 3C         CLR   <$3C               ;
C7C1: 86 01         LDA   #$01               ;
C7C3: 97 3B         STA   <$3B               ;
C7C5: 32 E8 E0      LEAS  $-20,S             ;
C7C8: BD FF BC      JSR   VidMemClrX         ;
C7CB: CE C0 D7      LDU   #$C0D7             ;
C7CE: 8E 28 20      LDX   #$2820             ;
C7D1: BD CA 69      JSR   $CA69              ;
C7D4: BD C0 3C      JSR   $C03C              ;
C7D7: 0F 3A         CLR   <$3A               ;
C7D9: 10 8E C0 65   LDY   #$C065             ;
C7DD: BD C0 66      JSR   $C066              ;
C7E0: BD CA 69      JSR   $CA69              ;
C7E3: 86 20         LDA   #$20               ;
C7E5: 1F 89         TFR   A,B                ;
C7E7: 5A            DECB                     ;
C7E8: 30 E4         LEAX  ,S                 ;
C7EA: A7 80         STA   ,X+                ;
C7EC: 5A            DECB                     ;
C7ED: 26 FB         BNE   $C7EA              ;
C7EF: 86 2F         LDA   #$2F               ;
C7F1: A7 80         STA   ,X+                ;
C7F3: 30 E4         LEAX  ,S                 ;
C7F5: BD CA 57      JSR   $CA57              ;
C7F8: 8E CC 00      LDX   #$CC00             ;
C7FB: BD C0 39      JSR   ReadIOPortX3       ;
C7FE: C5 02         BITB  #$02               ;
C800: 27 23         BEQ   $C825              ;
C802: C5 01         BITB  #$01               ;
C804: 26 0C         BNE   $C812              ;
C806: 0C 3B         INC   <$3B               ;
C808: 0A 3C         DEC   <$3C               ;
C80A: 2A 19         BPL   $C825              ;
C80C: C6 1B         LDB   #$1B               ;
C80E: D7 3C         STB   <$3C               ;
C810: 20 13         BRA   $C825              ;
C812: 0C 3C         INC   <$3C               ;
C814: 0C 3B         INC   <$3B               ;
C816: 86 1C         LDA   #$1C               ;
C818: 91 3C         CMPA  <$3C               ;
C81A: 26 09         BNE   $C825              ;
C81C: 32 E8 20      LEAS  $20,S              ;
C81F: BD CA 69      JSR   $CA69              ;
C822: 7E FF C8      JMP   $FFC8              ;
C825: BD C9 7A      JSR   $C97A              ;
C828: 0D 3B         TST   <$3B               ;
C82A: 27 C9         BEQ   $C7F5              ;
C82C: D6 3C         LDB   <$3C               ;
C82E: C1 09         CMPB  #$09               ;
C830: 26 25         BNE   $C857              ;
C832: 8E C4 87      LDX   #$C487             ;
C835: BD FF A4      JSR   SRAMByteRdX        ;
C838: 5D            TSTB                     ;
C839: 27 1C         BEQ   $C857              ;
C83B: C1 08         CMPB  #$08               ;
C83D: 22 05         BHI   $C844              ;
C83F: BD CB 99      JSR   $CB99              ;
C842: 20 13         BRA   $C857              ;
C844: 8E C4 87      LDX   #$C487             ;
C847: 34 10         PSHS  X                  ;
C849: C6 01         LDB   #$01               ;
C84B: BD FF AD      JSR   SRAMByteWrX        ;
C84E: BD CB 99      JSR   $CB99              ;
C851: 5F            CLRB                     ;
C852: 35 10         PULS  X                  ;
C854: BD FF AD      JSR   SRAMByteWrX        ;
C857: 8D 38         BSR   $C891              ;
C859: 96 3A         LDA   <$3A               ;
C85B: 81 06         CMPA  #$06               ;
C85D: 27 0E         BEQ   $C86D              ;
C85F: 4D            TSTA                     ;
C860: 26 04         BNE   $C866              ;
C862: 86 64         LDA   #$64               ;
C864: 20 02         BRA   $C868              ;
C866: 86 06         LDA   #$06               ;
C868: 97 3A         STA   <$3A               ;
C86A: 4C            INCA                     ;
C86B: C6 FF         LDB   #$FF               ;
C86D: BD CA 57      JSR   $CA57              ;
C870: 4A            DECA                     ;
C871: 27 19         BEQ   $C88C              ;
C873: 8E CC 00      LDX   #$CC00             ;
C876: 34 04         PSHS  B                  ;
C878: BD C0 39      JSR   ReadIOPortX3       ;
C87B: C5 0A         BITB  #$0A               ;
C87D: 26 04         BNE   $C883              ;
C87F: 1C FE         ANDCC #$FE               ;
C881: 20 02         BRA   $C885              ;
C883: 1A 01         ORCC  #$01               ;
C885: 35 04         PULS  B                  ;
C887: 56            RORB                     ;
C888: 26 E3         BNE   $C86D              ;
C88A: 0F 3A         CLR   <$3A               ;
C88C: 0F 3B         CLR   <$3B               ;
C88E: 7E C7 F5      JMP   $C7F5              ;

;SUBRTN
C891: 31 62         LEAY  2,S                ;
C893: 8E 10 80      LDX   #$1080             ;
C896: BD C0 58      JSR   $C058              ;
C899: BD C9 1F      JSR   $C91F              ;
C89C: 96 3C         LDA   <$3C               ;
C89E: 4C            INCA                     ;
C89F: BD C9 02      JSR   $C902              ;
C8A2: BD C9 10      JSR   $C910              ;
C8A5: ED 84         STD   ,X                 ;
C8A7: D6 3C         LDB   <$3C               ;
C8A9: 58            ASLB                     ;
C8AA: 58            ASLB                     ;
C8AB: 8E CC D6      LDX   #$CCD6             ;
C8AE: 3A            ABX                      ;
C8AF: 10 AE 84      LDY   ,X                 ;
C8B2: EE 02         LDU   2,X                ;
C8B4: 30 6E         LEAX  14,S               ;
C8B6: A6 A0         LDA   ,Y+                ;
C8B8: 81 2F         CMPA  #$2F               ;
C8BA: 27 04         BEQ   $C8C0              ;
C8BC: A7 80         STA   ,X+                ;
C8BE: 20 F6         BRA   $C8B6              ;
C8C0: 1F 30         TFR   U,D                ;
C8C2: 33 62         LEAU  2,S                ;
C8C4: 8E C4 00      LDX   #$C400             ;
C8C7: 3A            ABX                      ;
C8C8: BD FF A4      JSR   SRAMByteRdX        ;
C8CB: 34 06         PSHS  B,A                ;
C8CD: D6 3C         LDB   <$3C               ;
C8CF: 5C            INCB                     ;
C8D0: C1 07         CMPB  #$07               ;
C8D2: 22 13         BHI   $C8E7              ;
C8D4: 35 06         PULS  A,B                ;
C8D6: 1F 98         TFR   B,A                ;
C8D8: BD C9 10      JSR   $C910              ;
C8DB: ED 47         STD   7,U                ;
C8DD: BD FF A1      JSR   RdSRAMbyteX        ;
C8E0: BD C9 10      JSR   $C910              ;
C8E3: ED 49         STD   9,U                ;
C8E5: 20 13         BRA   $C8FA              ;
C8E7: C1 08         CMPB  #$08               ;
C8E9: 26 09         BNE   $C8F4              ;
C8EB: CC 30 30      LDD   #$3030             ;
C8EE: ED 49         STD   9,U                ;
C8F0: 33 5E         LEAU  -2,U               ;
C8F2: 20 E0         BRA   $C8D4              ;
C8F4: 35 06         PULS  A,B                ;
C8F6: 1F 98         TFR   B,A                ;
C8F8: 20 E6         BRA   $C8E0              ;
C8FA: 8E 10 80      LDX   #$1080             ;
C8FD: 31 62         LEAY  2,S                ;
C8FF: 7E C0 5F      JMP   $C05F              ;

;SUBRTN
C902: 34 04         PSHS  B                  ;
C904: 1F 89         TFR   A,B                ;
C906: 86 99         LDA   #$99               ;
C908: 8B 01         ADDA  #$01               ;
C90A: 19            DAA                      ;
C90B: 5A            DECB                     ;
C90C: 2A FA         BPL   $C908              ;
C90E: 35 84         PULS  B,PC               ;

;SUBRTN
C910: 1F 89         TFR   A,B                ;
C912: 84 F0         ANDA  #$F0               ;
C914: 44            LSRA                     ;
C915: 44            LSRA                     ;
C916: 44            LSRA                     ;
C917: 44            LSRA                     ;
C918: 8B 30         ADDA  #$30               ;
C91A: C4 0F         ANDB  #$0F               ;
C91C: CB 30         ADDB  #$30               ;
C91E: 39            RTS                      ;

;SUBTRN
C91F: 86 20         LDA   #$20               ;
C921: 1F 89         TFR   A,B                ;
C923: 5A            DECB                     ;
C924: 30 64         LEAX  4,S                ;
C926: A7 80         STA   ,X+                ;
C928: 5A            DECB                     ;
C929: 26 FB         BNE   $C926              ;
C92B: 86 2F         LDA   #$2F               ;
C92D: A7 80         STA   ,X+                ;
C92F: 30 64         LEAX  4,S                ;
C931: 39            RTS                      ;

C932: 8C C4 81      CMPX  #$C481             ;
C935: 26 1A         BNE   $C951              ;
C937: BD FF A7      JSR   SRAMWordRdX        ;
C93A: 30 1C         LEAX  -4,X               ;
C93C: 1E 89         EXG   A,B                ;
C93E: 8B 10         ADDA  #$10               ;
C940: 19            DAA                      ;
C941: 24 07         BCC   $C94A              ;
C943: 1E 89         EXG   A,B                ;
C945: 8B 01         ADDA  #$01               ;
C947: 19            DAA                      ;
C948: 1E 89         EXG   A,B                ;
C94A: 1E 89         EXG   A,B                ;
C94C: 0C 3B         INC   <$3B               ;
C94E: 7E FF B0      JMP   $FFB0              ;
C951: BD FF A1      JSR   RdSRAMbyteX        ;
C954: 8B 01         ADDA  #$01               ;
C956: 19            DAA                      ;
C957: 30 1E         LEAX  -2,X               ;
C959: 0C 3B         INC   <$3B               ;
C95B: 7E FF AA      JMP   WrSRAMbyteX        ;
C95E: 8C C4 81      CMPX  #$C481             ;
C961: 26 10         BNE   $C973              ;
C963: BD FF A7      JSR   SRAMWordRdX        ;
C966: 30 1C         LEAX  -4,X               ;
C968: 1E 89         EXG   A,B                ;
C96A: 8B 90         ADDA  #$90               ;
C96C: 19            DAA                      ;
C96D: 1E 89         EXG   A,B                ;
C96F: 89 99         ADCA  #$99               ;
C971: 20 D4         BRA   $C947              ;
C973: BD FF A1      JSR   RdSRAMbyteX        ;
C976: 8B 99         ADDA  #$99               ;
C978: 20 DC         BRA   $C956              ;
C97A: D6 3C         LDB   <$3C               ;
C97C: 5C            INCB                     ;
C97D: C1 07         CMPB  #$07               ;
C97F: 22 01         BHI   $C982              ;
C981: 39            RTS                      ;
C982: C1 09         CMPB  #$09               ;
C984: 23 11         BLS   $C997              ;
C986: C1 10         CMPB  #$10               ;
C988: 22 0D         BHI   $C997              ;
C98A: C1 0A         CMPB  #$0A               ;
C98C: 27 09         BEQ   $C997              ;
C98E: 8E C4 87      LDX   #$C487             ;
C991: BD FF A1      JSR   RdSRAMbyteX        ;
C994: 4D            TSTA                     ;
C995: 26 EA         BNE   $C981              ;
C997: 5A            DECB                     ;
C998: 58            ASLB                     ;
C999: 58            ASLB                     ;
C99A: 8E CC D6      LDX   #$CCD6             ;
C99D: 3A            ABX                      ;
C99E: E6 03         LDB   3,X                ;
C9A0: 8E C4 00      LDX   #$C400             ;
C9A3: 3A            ABX                      ;
C9A4: 34 10         PSHS  X                  ;
C9A6: BD CA 57      JSR   $CA57              ;
C9A9: 8E CC 00      LDX   #$CC00             ;
C9AC: BD C0 39      JSR   ReadIOPortX3       ;
C9AF: C5 02         BITB  #$02               ;
C9B1: 27 02         BEQ   $C9B5              ;
C9B3: 35 90         PULS  X,PC               ;
C9B5: C5 08         BITB  #$08               ;
C9B7: 26 04         BNE   $C9BD              ;
C9B9: 0F 3A         CLR   <$3A               ;
C9BB: 20 E9         BRA   $C9A6              ;
C9BD: 35 10         PULS  X                  ;
C9BF: 8C C4 7D      CMPX  #$C47D             ;
C9C2: 26 0C         BNE   $C9D0              ;
C9C4: 34 14         PSHS  X,B                ;
C9C6: 8E C4 00      LDX   #$C400             ;
C9C9: C6 01         LDB   #$01               ;
C9CB: BD C0 36      JSR   WriteIOPortX3      ;
C9CE: 35 14         PULS  B,X                ;
C9D0: 54            LSRB                     ;
C9D1: 10 25 FF 5D   LBCS  $C932              ;
C9D5: 7E C9 5E      JMP   $C95E              ;



C9D8: 02 
C9D9: 03 04         COM   <$04               ;
C9DB: 10 
C9DC: 18 
C9DD: 20 40         BRA   $CA1F              ;
C9DF: 80 00         SUBA  #$00               ;
C9E1: FF 11 EE      STU   $11EE              ;
C9E4: 22 DD         BHI   $C9C3              ;
C9E6: 33 CC 44      LEAU  $44,PC             ;
C9E9: BB 55 AA      ADDA  $55AA              ;
C9EC: 66 99 77 88   ROR   [$7788,X]          ;
C9F0: 13            SYNC                     ;
C9F1: 1B 
C9F2: 1C 00         ANDCC #$00               ;

vector table???

C9F4: C5 E3 
C9F6: C7 6F 
C9F8: C7 7F
C9FA: C7 83
C9FC: C7 87 



C9FE: 05 
C9FF: 05 
CA00: 28 28         BVC   $CA2A              ;
CA02: 80 80         SUBA  #$80               ;
CA04: 00 00         NEG   <$00               ;
CA06: AD AD 2D 2D   JSR   $2D2D,PC           ;
CA0A: A8 A8 85      EORA  $-7B,Y             ;
CA0D: 85 8E         BITA  #$8E               ;
CA0F: CC 00 10      LDD   #$0010             ;
CA12: 8E 00 64      LDX   #$0064             ;
CA15: BD CA 44      JSR   $CA44              ;
CA18: BD C0 39      JSR   ReadIOPortX3       ;
CA1B: C5 02         BITB  #$02               ;
CA1D: 26 F6         BNE   $CA15              ;
CA1F: BD CA 44      JSR   $CA44              ;
CA22: BD C0 39      JSR   ReadIOPortX3       ;
CA25: C5 02         BITB  #$02               ;
CA27: 27 F6         BEQ   $CA1F              ;
CA29: 39            RTS                      ;



;SUBRTN  12 times in this ROM
CA2A: BD FF BC      JSR   VidMemClrX         ;$F5D1 subr, clears video memory, ~76.2mS
CA2D: 8D 3A         BSR   $CA69              ;
CA2F: BD CA F9      JSR   BlkOutClrRegs      ;all color registers are changed to black
CA32: 0A 49         DEC   <$49               ;
CA34: 2A 02         BPL   $CA38              ;
CA36: 0F 49         CLR   <$49               ;
CA38: 39            RTS                      ;



;SUBRTN   3 times in this ROM
CA39: 10 8E 00 01   LDY   #$0001             ;
CA3D: 8D 05         BSR   $CA44              ;
CA3F: 0D 49         TST   <$49               ;
CA41: 27 FA         BEQ   $CA3D              ;
CA43: 39            RTS                      ;



;SUBRTN  14 times in this ROM
CA44: 34 23         PSHS  Y,A,CC             ;
CA46: 8D 21         BSR   $CA69              ;
CA48: 0D 49         TST   <$49               ;
CA4A: 26 09         BNE   $CA55              ;
CA4C: 86 B2         LDA   #$B2               ;
CA4E: 4A            DECA                     ;
CA4F: 26 FD         BNE   $CA4E              ;
CA51: 31 3F         LEAY  -1,Y               ;
CA53: 26 F1         BNE   $CA46              ;
CA55: 35 A3         PULS  CC,A,Y,PC          ;



;SUBRTN   8 times in this ROM
CA57: 34 24         PSHS  Y,B                ;
CA59: D6 49         LDB   <$49               ;
CA5B: 0F 49         CLR   <$49               ;
CA5D: 10 8E 00 0A   LDY   #$000A             ;
CA61: 8D E1         BSR   $CA44              ;
CA63: DB 49         ADDB  <$49               ;
CA65: D7 49         STB   <$49               ;
CA67: 35 A4         PULS  B,Y,PC             ;



;SUBRTN  24 times in this ROM
CA69: 34 15         PSHS  X,B,CC             ;
CA6B: C6 38         LDB   #$38               ;watchdog clear byte
CA6D: 8E C3 FC      LDX   #$C3FC             ;watchdog address
CA70: BD C0 36      JSR   WriteIOPortX3      ;$F7DB, clear the watchdog
CA73: 8E CC 00      LDX   #$CC00             ;ROM board PIA address
CA76: BD C0 39      JSR   ReadIOPortX3       ;$F7F1, read from coin door port
CA79: 53            COMB                     ;toggle all bit values
CA7A: C4 03         ANDB  #$03               ;mask for "auto/manual" and "advance" switchs
CA7C: 27 02         BEQ   $CA80              ;if they're both active (0's after the COMB) leave the C flag alone
CA7E: 1C FE         ANDCC #$FE               ;clear C flag
CA80: D6 47         LDB   <$47               ;
CA82: 56            RORB                     ;
CA83: D7 47         STB   <$47               ;
CA85: 26 02         BNE   $CA89              ;
CA87: D7 48         STB   <$48               ;
CA89: 53            COMB                     ;
CA8A: 26 09         BNE   $CA95              ;
CA8C: D6 48         LDB   <$48               ;
CA8E: 26 05         BNE   $CA95              ;
CA90: 53            COMB                     ;
CA91: D7 48         STB   <$48               ;
CA93: 0C 49         INC   <$49               ;
CA95: 35 95         PULS  CC,B,X,PC          ;



;SUBRTN   1 time in this ROM
CA97: 34 34         PSHS  Y,X,B              ;
CA99: 8E C0 00      LDX   #$C000             ;
CA9C: E6 A0         LDB   ,Y+                ;
CA9E: BD C0 36      JSR   WriteIOPortX3      ;
CAA1: 30 01         LEAX  1,X                ;
CAA3: 8C C0 10      CMPX  #$C010             ;
CAA6: 26 F4         BNE   $CA9C              ;
CAA8: 35 B4         PULS  B,X,Y,PC           ;



;SUBRTN   12 times in this ROM
CAAA: 34 14         PSHS  X,B                ;
CAAC: 54            LSRB                     ;
CAAD: 56            RORB                     ;
CAAE: 56            RORB                     ;
CAAF: 56            RORB                     ;
CAB0: 2A 01         BPL   $CAB3              ;
CAB2: 5C            INCB                     ;
CAB3: 56            RORB                     ;
CAB4: 56            RORB                     ;
CAB5: 8E CC 00      LDX   #$CC00             ;
CAB8: BD C0 36      JSR   WriteIOPortX3      ;LEDs 1&2 activity, appears to be random?
CABB: 58            ASLB                     ;
CABC: 58            ASLB                     ;
CABD: 58            ASLB                     ;
CABE: CA 3F         ORB   #$3F               ;
CAC0: 8E CC 02      LDX   #$CC02             ;
CAC3: BD C0 36      JSR   WriteIOPortX3      ;send an interrupt to the 6802 on the sound board
CAC6: 35 94         PULS  B,X,PC             ;



;SUBRTN   4 times in this ROM
CAC8: 34 26         PSHS  Y,B,A              ;
CACA: 86 02         LDA   #$02               ;
CACC: 10 8E 01 F4   LDY   #$01F4             ;
CAD0: BD CA AA      JSR   $CAAA              ;
CAD3: BD CA 44      JSR   $CA44              ;
CAD6: 5F            CLRB                     ;
CAD7: BD CA AA      JSR   $CAAA              ;
CADA: BD CA 44      JSR   $CA44              ;
CADD: E6 61         LDB   1,S                ;
CADF: 4A            DECA                     ;
CAE0: 26 EE         BNE   $CAD0              ;
CAE2: 35 26         PULS  A,B,Y              ;



;SUBRTN   2 times in this ROM
CAE4: 34 06         PSHS  B,A                ;
CAE6: 0F 52         CLR   <$52               ;
CAE8: 0F 49         CLR   <$49               ;
CAEA: 86 01         LDA   #$01               ;
CAEC: 97 48         STA   <$48               ;
CAEE: 86 03         LDA   #$03               ;
CAF0: 97 36         STA   <$36               ;
CAF2: CC FF FF      LDD   #$FFFF             ;
CAF5: DD 59         STD   <$59               ;
CAF7: 35 86         PULS  A,B,PC             ;

Clears all 16 color registers to zero(black)

BlkOutClrRegs    ;SUBRTN
CAF9: 34 14         PSHS  X,B                ;
CAFB: 5F            CLRB                     ;a zero to write to the color register
CAFC: 8E C0 00      LDX   #$C000             ;the first color register address
CAFF: BD C0 36      JSR   WriteIOPortX3      ;write it
CB02: 30 01         LEAX  1,X                ;go to next color register
CB04: 8C C0 10      CMPX  #$C010             ;are we done?
CB07: 26 F6         BNE   $CAFF              ;go back around if not
CB09: 35 94         PULS  B,X,PC             ;done, restore regs and return



;SUBRTN  3 times in this ROM
CB0B: 34 14         PSHS  X,B                ;
CB0D: 53            COMB                     ;
CB0E: C4 3F         ANDB  #$3F               ;
CB10: 8E CC 02      LDX   #$CC02             ;
CB13: BD C0 36      JSR   WriteIOPortX3      ;
CB16: BD CA 57      JSR   $CA57              ;
CB19: C6 3F         LDB   #$3F               ;
CB1B: BD C0 36      JSR   WriteIOPortX3      ;
CB1E: BD CA 57      JSR   $CA57              ;
CB21: 35 94         PULS  B,X,PC             ;



;SUBRTN   2 times in this ROM
CB23: 34 02         PSHS  A                  ;
CB25: 1F 98         TFR   B,A                ;
CB27: 84 0F         ANDA  #$0F               ;
CB29: 8B 00         ADDA  #$00               ;
CB2B: 19            DAA                      ;
CB2C: C4 F0         ANDB  #$F0               ;
CB2E: 27 07         BEQ   $CB37              ;
CB30: 8B 16         ADDA  #$16               ;
CB32: 19            DAA                      ;
CB33: C0 10         SUBB  #$10               ;
CB35: 20 F7         BRA   $CB2E              ;
CB37: 1F 89         TFR   A,B                ;
CB39: 35 82         PULS  A,PC               ;



;not a subroutine in this ROM, but obviously it is made to return from a subroutine
CB3B: 34 16         PSHS  X,B,A              ;
CB3D: CC 00 00      LDD   #$0000             ;
CB40: 8E 00 00      LDX   #$0000             ;
CB43: 9F 3D         STX   <$3D               ;
CB45: 30 89 0F 00   LEAX  $0F00,X            ;
CB49: ED 83         STD   ,--X               ;
CB4B: 9C 3D         CMPX  <$3D               ;
CB4D: 26 FA         BNE   $CB49              ;
CB4F: 30 89 09 00   LEAX  $0900,X            ;
CB53: 4D            TSTA                     ;
CB54: 26 03         BNE   $CB59              ;
CB56: 8E 0F 00      LDX   #$0F00             ;
CB59: BD CA 69      JSR   $CA69              ;
CB5C: 0D 49         TST   <$49               ;
CB5E: 26 05         BNE   $CB65              ;
CB60: C3 11 11      ADDD  #$1111             ;
CB63: 24 DE         BCC   $CB43              ;
CB65: 35 96         PULS  A,B,X,PC           ;



;SUBRTN   1 time in this ROM
CB67: BD CA F9      JSR   BlkOutClrRegs      ;
CB6A: 8E 00 00      LDX   #$0000             ;
CB6D: 10 8E C9 E0   LDY   #$C9E0             ;
CB71: 9F 3D         STX   <$3D               ;
CB73: 30 89 0F 00   LEAX  $0F00,X            ;
CB77: A6 A0         LDA   ,Y+                ;
CB79: 1F 89         TFR   A,B                ;
CB7B: ED 83         STD   ,--X               ;
CB7D: 9C 3D         CMPX  <$3D               ;
CB7F: 26 FA         BNE   $CB7B              ;
CB81: 30 89 09 00   LEAX  $0900,X            ;
CB85: 4D            TSTA                     ;
CB86: 26 03         BNE   $CB8B              ;
CB88: 8E 0F 00      LDX   #$0F00             ;
CB8B: BD CA 69      JSR   $CA69              ;
CB8E: 0D 49         TST   <$49               ;
CB90: 26 06         BNE   $CB98              ;
CB92: 10 8C C9 F0   CMPY  #$C9F0             ;
CB96: 26 D9         BNE   $CB71              ;
CB98: 39            RTS                      ;



;SUBRTN   2 times in this ROM
CB99: 8E C4 87      LDX   #$C487             ;
CB9C: BD FF AD      JSR   SRAMByteWrX        ;
CB9F: 58            ASLB                     ;2 * B
CBA0: 34 04         PSHS  B                  ;save that on stack
CBA2: 58            ASLB                     ;4 * B
CBA3: EB E0         ADDB  ,S+                ;add stack and move past it for 6 * B
CBA5: 8E CF 10      LDX   #$CF10             ;data table address
CBA8: 3A            ABX                      ;set pointer to data packet we want
CBA9: 10 8E C4 89   LDY   #$C489             ;
CBAD: C6 06         LDB   #$06               ;

;SUBRTN   3 times in this ROM, in jump table
CBAF: 34 02         PSHS  A                  ;
CBB1: A6 80         LDA   ,X+                ;
CBB3: 1E 12         EXG   X,Y                ;
CBB5: BD FF AA      JSR   WrSRAMbyteX        ;
CBB8: 1E 12         EXG   X,Y                ;
CBBA: 5A            DECB                     ;
CBBB: 26 F4         BNE   $CBB1              ;
CBBD: 35 82         PULS  A,PC               ;



CBBF: C6 0E         LDB   #$0E               ;
CBC1: 20 01         BRA   $CBC4              ;

;SUBRTN   1 times in this ROM
CBC3: 5F            CLRB                     ;
CBC4: 8E C4 00      LDX   #$C400             ;
CBC7: 4F            CLRA                     ;
CBC8: BD FF AA      JSR   WrSRAMbyteX        ;$F84E in Fixed bank
CBCB: 5A            DECB                     ;
CBCC: 26 FA         BNE   $CBC8              ;
CBCE: 39            RTS                      ;



;SUBRTN   1 times in this ROM
CBCF: 34 36         PSHS  Y,X,B,A            ;
CBD1: 8D F0         BSR   $CBC3              ;
CBD3: 8E CE CF      LDX   #$CECF             ;
CBD6: 10 8E C4 1D   LDY   #$C41D             ;
CBDA: C6 47         LDB   #$47               ;
CBDC: 8D D1         BSR   $CBAF              ;
CBDE: 35 B6         PULS  A,B,X,Y,PC         ;



;SUBRTN   2 times in this ROM, in jump table
CBE0: 34 16         PSHS  X,B,A              ;
CBE2: 86 01         LDA   #$01               ;
CBE4: 20 02         BRA   $CBE8              ;

;SUBRTN   2 times in this ROM, in jump table
CBE6: 34 16         PSHS  X,B,A              ;
CBE8: C4 07         ANDB  #$07               ;
CBEA: 27 1F         BEQ   $CC0B              ;
CBEC: 58            ASLB                     ;
CBED: 58            ASLB                     ;
CBEE: 8E C3 FD      LDX   #$C3FD             ;
CBF1: 3A            ABX                      ;
CBF2: BD FF A4      JSR   SRAMByteRdX        ;
CBF5: 34 04         PSHS  B                  ;
CBF7: BD FF A4      JSR   SRAMByteRdX        ;
CBFA: 34 04         PSHS  B                  ;
CBFC: AB E0         ADDA  ,S+                ;
CBFE: 19            DAA                      ;
CBFF: 1E 89         EXG   A,B                ;
CC01: 35 02         PULS  A                  ;
CC03: 89 00         ADCA  #$00               ;
CC05: 19            DAA                      ;
CC06: 30 1C         LEAX  -4,X               ;
CC08: BD FF B0      JSR   $FFB0              ;
CC0B: 35 96         PULS  A,B,X,PC           ;



;SUBRTN
CC0D: 34 12         PSHS  X,A                ;
CC0F: 9B 37         ADDA  <$37               ;
CC11: 19            DAA                      ;
CC12: 24 02         BCC   $CC16              ;
CC14: 86 99         LDA   #$99               ;
CC16: 97 37         STA   <$37               ;
CC18: 8E C4 7D      LDX   #$C47D             ;
CC1B: BD FF AA      JSR   WrSRAMbyteX        ;
CC1E: 35 92         PULS  A,X,PC             ;



;in jump table
CC20: 34 16         PSHS  X,B,A              ;
CC22: C6 03         LDB   #$03               ;
CC24: 20 0A         BRA   $CC30              ;
;in jump table
CC26: 34 16         PSHS  X,B,A              ;
CC28: C6 02         LDB   #$02               ;
CC2A: 20 04         BRA   $CC30              ;
;in jump table
CC2C: 34 16         PSHS  X,B,A              ;
CC2E: C6 01         LDB   #$01               ;
CC30: BD CB E0      JSR   $CBE0              ;
CC33: 58            ASLB                     ;
CC34: 8E C4 87      LDX   #$C487             ;
CC37: 3A            ABX                      ;
CC38: BD FF A4      JSR   SRAMByteRdX        ;
CC3B: 8D 62         BSR   $CC9F              ;
CC3D: 96 39         LDA   <$39               ;
CC3F: 34 04         PSHS  B                  ;
CC41: AB E4         ADDA  ,S                 ;
CC43: 97 39         STA   <$39               ;
CC45: 96 38         LDA   <$38               ;
CC47: AB E0         ADDA  ,S+                ;
CC49: 97 38         STA   <$38               ;
CC4B: 8E C4 93      LDX   #$C493             ;
CC4E: BD FF A4      JSR   SRAMByteRdX        ;
CC51: 8D 4C         BSR   $CC9F              ;
CC53: 34 04         PSHS  B                  ;
CC55: A1 E0         CMPA  ,S+                ;
CC57: 24 02         BCC   $CC5B              ;
CC59: 35 96         PULS  A,B,X,PC           ;
CC5B: 8E C4 8F      LDX   #$C48F             ;
CC5E: BD FF A4      JSR   SRAMByteRdX        ;
CC61: 8D 3C         BSR   $CC9F              ;
CC63: 8D 24         BSR   $CC89              ;
CC65: 34 02         PSHS  A                  ;
CC67: D7 38         STB   <$38               ;
CC69: 8E C4 91      LDX   #$C491             ;
CC6C: BD FF A4      JSR   SRAMByteRdX        ;
CC6F: 96 39         LDA   <$39               ;
CC71: 8D 2C         BSR   $CC9F              ;
CC73: 8D 14         BSR   $CC89              ;
CC75: 4D            TSTA                     ;
CC76: 27 04         BEQ   $CC7C              ;
CC78: 0F 38         CLR   <$38               ;
CC7A: 0F 39         CLR   <$39               ;
CC7C: AB E0         ADDA  ,S+                ;
CC7E: 19            DAA                      ;
CC7F: C6 04         LDB   #$04               ;
CC81: BD CB E6      JSR   $CBE6              ;
CC84: BD CC 0D      JSR   $CC0D              ;
CC87: 35 96         PULS  A,B,X,PC           ;



CC89: 34 04         PSHS  B                  ;
CC8B: 5D            TSTB                     ;
CC8C: 26 03         BNE   $CC91              ;
CC8E: 4F            CLRA                     ;
CC8F: 35 84         PULS  B,PC               ;
CC91: 1E 89         EXG   A,B                ;
CC93: 86 99         LDA   #$99               ;
CC95: 8B 01         ADDA  #$01               ;
CC97: 19            DAA                      ;
CC98: E0 E4         SUBB  ,S                 ;
CC9A: 24 F9         BCC   $CC95              ;
CC9C: EB E0         ADDB  ,S+                ;
CC9E: 39            RTS                      ;



CC9F: 34 02         PSHS  A                  ;
CCA1: 1E 89         EXG   A,B                ;
CCA3: 5F            CLRB                     ;
CCA4: 4D            TSTA                     ;
CCA5: 26 02         BNE   $CCA9              ;
CCA7: 35 82         PULS  A,PC               ;
CCA9: 8B 99         ADDA  #$99               ;
CCAB: 19            DAA                      ;
CCAC: 5C            INCB                     ;
CCAD: 20 F5         BRA   $CCA4              ;



;in jump table
CCAF: 34 36         PSHS  Y,X,B,A            ;
CCB1: 8E CE CF      LDX   #$CECF             ;
CCB4: 10 8E C4 1D   LDY   #$C41D             ;
CCB8: C6 30         LDB   #$30               ;
CCBA: BD CB AF      JSR   $CBAF              ;
CCBD: 8D 02         BSR   $CCC1              ;
CCBF: 35 B6         PULS  A,B,X,Y,PC         ;



;in jump table
CCC1: 34 36         PSHS  Y,X,B,A            ;
CCC3: 10 8E CE CF   LDY   #$CECF             ;
CCC7: 8E B2 60      LDX   #$B260             ;
CCCA: C6 30         LDB   #$30               ;
CCCC: A6 A0         LDA   ,Y+                ;
CCCE: BD FF AA      JSR   WrSRAMbyteX        ;
CCD1: 5A            DECB                     ;
CCD2: 26 F8         BNE   $CCCC              ;
CCD4: 35 B6         PULS  A,B,X,Y,PC         ;



CCD6: CD 46                                  ;'COINS LEFT'
CCD8: 00 01                                  ;
CCDA: CD 51                                  ;'COINS CENTER'
CCDC: 00 05                                  ;
CCDE: CD 5E                                  ;'COINS RIGHT'
CCE0: 00 09                                  ;
CCE2: CD 6A                                  ;'TOTAL PAID'
CCE4: 00 0D                                  ;
CCE6: CD 75                                  ;'SHIPS WON'
CCE8: 00 11                                  ;
CCEA: CD 7F                                  ;'TOTAL TIME'
CCEC: 00 15                                  ;
CCEE: CD 8A                                  ;'TOTAL SHIPS'
CCF0: 00 19                                  ;
CCF2: CD 96                                  ;'BONUS SHIP LEVEL'
CCF4: 00 81                                  ;
CCF6: CD A7                                  ;'NUMBER OF SHIPS'
CCF8: 00 85                                  ;
CCFA: CD B7                                  ;'COINAGE SELECT'
CCFC: 00 87                                  ;
CCFE: CD C6                                  ;'LEFT COIN MULT'
CD00: 00 89                                  ;
CD02: CD D5                                  ;'CENTER COIN MULT'
CD04: 00 8B                                  ;
CD06: CD E6                                  ;'RIGHT COIN MULT'
CD08: 00 8D                                  ;
CD0A: CD F6                                  ;'COINS FOR CREDIT'
CD0C: 00 8F                                  ;
CD0E: CE 07                                  ;'COINS FOR BONUS'
CD10: 00 91                                  ;
CD12: CE 17                                  ;'MINIMUM COINS'
CD14: 00 93                                  ;
CD16: CE 25                                  ;'FREE PLAY'
CD18: 00 95                                  ;
CD1A: CE 2F                                  ;'GAME ADJUST 1'
CD1C: 00 97                                  ;
CD1E: CE 3D                                  ;'GAME ADJUST 2'
CD20: 00 99                                  ;
CD22: CE 4B                                  ;'GAME ADJUST 3'
CD24: 00 9B                                  ;
CD26: CE 59                                  ;'GAME ADJUST 4'
CD28: 00 9D                                  ;
CD2A: CE 67                                  ;'GAME ADJUST 5'
CD2C: 00 9F                                  ;
CD2E: CE 75                                  ;'GAME ADJUST 6'
CD30: 00 A1                                  ;
CD32: CE 83                                  ;'GAME ADJUST 7'
CD34: 00 A3                                  ;
CD36: CE 91                                  ;'GAME ADJUST 8'
CD38: 00 A5                                  ;
CD3A: CE 9F                                  ;'GAME ADJUST 9'
CD3C: 00 A7                                  ;
CD3E: CE AD                                  ;'GAME ADJUST 10'
CD40: 00 A9                                  ;
CD42: CE BC                                  ;'SPECIAL FUNCTION'
CD44: 00 7D                                  ;

More Defender vocabulary

CD46: 43 4F 49 4E                            ; 'COINS LEFT/'
CD4A: 53 20 4C 45 
CD4E: 46 54 2F 

CD51: 43 4F 49 4E                            ; 'COINS CENTER/'
CD55: 53 20 43 45 
CD59: 4E 54 45 52 
CD5D: 2F 

CD5E: 43 4F 49 4E                            ; 'COINS RIGHT/'
CD62: 53 20 52 49
CD66: 47 48 54 2F 

CD6A: 54 4F 54 41                            ; 'TOTAL PAID/'
CD6E: 4C 20 50 41 
CD72: 49 44 2F 


CD75: 53 48 49 50                            ; 'SHIPS WON/'
CD79: 53 20 57 4F
CD7D: 4E 2F 

CD7F: 54 4F 54 41                            ; 'TOTAL TIME/'
CD83: 4C 20 54 49
CD87: 4D 45 2F 


CD8A: 54 4F 54 41                            ; 'TOTAL SHIPS/'
CD8E: 4C 20 53 48
CD92: 49 50 53 2F

CD96: 42 4F 4E 55                            ; 'BONUS SHIP LEVEL/'
CD9A: 53 20 53 48
CD9E: 49 50 20 4C
CDA2: 45 56 45 4C
CDA6: 2F

CDA7: 4E 55 4D 42                            ; 'NUMBER OF SHIPS/'
CDAB: 45 52 20 4F
CDAF: 46 20 53 48
CDB3: 49 50 53 2F

CDB7: 43 4F 49 4E                            ; 'COINAGE SELECT/'
CDBB: 41 47 45 20
CDBF: 53 45 4C 45 
CDC3: 43 54 2F

CDC6: 4C 45 46 54                            ; 'LEFT COIN MULT/'
CDCA: 20 43 4F 49
CDCE: 4E 20 4D 55 
CDD2: 4C 54 2F

CDD5: 43 45 4E 54                            ; 'CENTER COIN MULT/'
CDD9: 45 52 20 43
CDDD: 4F 49 4E 20
CDE1: 4D 55 4C 54
CDE5: 2F

CDE6: 52 49 47 48                            ; 'RIGHT COIN MULT/'
CDEA: 54 20 43 4F 
CDEE: 49 4E 20 4D 
CDF2: 55 4C 54 2F

CDF6: 43 4F 49 4E                            ; 'COINS FOR CREDIT/'
CDFA: 53 20 46 4F 
CDFE: 52 20 43 52 
CE02: 45 44 49 54
CE06: 2F

CE07: 43 4F 49 4E                            ; 'COINS FOR BONUS/'
CE0B: 53 20 46 4F
CE0F: 52 20 42 4F
CE13: 4E 55 53 2F

CE17: 4D 49 4E 49                            ; 'MINIMUM COINS/'
CE1B: 4D 55 4D 20
CE1F: 43 4F 49 4E 
CE23: 53 2F

CE25: 46 52 45 45                            ; 'FREE PLAY/'
CE29: 20 50 4C 41 
CE2D: 59 2F 

CE2F: 47 41 4D 45                            ; 'GAME ADJUST 1/'
CE33: 20 41 44 4A
CE37: 55 53 54 20
CE3B: 31 2F 

CE3D: 47 41 4D 45                            ; 'GAME ADJUST 2/'
CE41: 20 41 44 4A 
CE45: 55 53 54 20
CE49: 32 2F 

CE4B: 47 41 4D 45                            ; 'GAME ADJUST 3/'
CE4F: 20 41 44 4A
CE53: 55 53 54 20
CE57: 33 2F

CE59: 47 41 4D 45                            ; 'GAME ADJUST 4/'
CE5D: 20 41 44 4A 
CE61: 55 53 54 20
CE65: 34 2F

CE67: 47 41 4D 45                            ; 'GAME ADJUST 5/'
CE6B: 20 41 44 4A 
CE6F: 55 53 54 20
CE73: 35 2F

CE75: 47 41 4D 45                            ; 'GAME ADJUST 6/'
CE79: 20 41 44 4A
CE7D: 55 53 54 20
CE81: 36 2F

CE83: 47 41 4D 45                            ; 'GAME ADJUST 7/'
CE87: 20 41 44 4A
CE8B: 55 53 54 20
CE8F: 37 2F

CE91: 47 41 4D 45                            ; 'GAME ADJUST 8/'
CE95: 20 41 44 4A
CE99: 55 53 54 20
CE9D: 38 2F

CE9F: 47 41 4D 45                            ; 'GAME ADJUST 9/'
CEA3: 20 41 44 4A
CEA7: 55 53 54 20
CEAB: 39 2F

CEAD: 47 41 4D 45                            ; 'GAME ADJUST 10/'
CEB1: 20 41 44 4A 
CEB5: 55 53 54 20
CEB9: 31 30 2F

CEBC: 53 50 45 43                            ; 'SPECIAL FUNCTION/'
CEC0: 49 41 4C 20
CEC4: 46 55 4E 43 
CEC8: 54 49 4F 4E 
CECC: 2F



CECD: FF
CECE: FF 02 12      STU   $0212              ;
CED1: 70 44 52      NEG   $4452              ;
CED4: 4A            DECA                     ;
CED5: 01 
CED6: 83 15 53      SUBD  #$1553             ;
CED9: 41 
CEDA: 4D            TSTA                     ;
CEDB: 01 
CEDC: 59            ROLB                     ;
CEDD: 20 4C         BRA   $CF2B              ;
CEDF: 45 
CEE0: 44            LSRA                     ;
CEE1: 01 
CEE2: 42 
CEE3: 85 50         BITA  #$50               ;
CEE5: 47            ASRA                     ;
CEE6: 44            LSRA                     ;
CEE7: 01 
CEE8: 25 20         BCS   $CF0A              ;
CEEA: 43            COMA                     ;
CEEB: 52 
CEEC: 42 
CEED: 01 
CEEE: 10 
CEEF: 35 4D         PULS  CC,B,DP,U          ;
CEF1: 52 
CEF2: 53            COMB                     ;
CEF3: 00 82         NEG   <$82               ;
CEF5: 65 
CEF6: 53            COMB                     ;
CEF7: 53            COMB                     ;
CEF8: 52 
CEF9: 00 60         NEG   <$60               ;
CEFB: 10 
CEFC: 54            LSRB                     ;
CEFD: 4D            TSTA                     ;
CEFE: 48            ASLA                     ;
CEFF: 00 5A         NEG   <$5A               ;
CF01: 01 
CF02: 00 03         NEG   <$03               ;
CF04: 03 01         COM   <$01               ;
CF06: 04 01         LSR   <$01               ;
CF08: 01 
CF09: 00 00         NEG   <$00               ;
CF0B: 00 05         NEG   <$05               ;
CF0D: 15 
CF0E: 01 
CF0F: 05 

CF10: 00 00         NEG   <$00               ;
CF12: 00 00         NEG   <$00               ;
CF14: 00 00         NEG   <$00               ;
CF16: 01 
CF17: 04 01         LSR   <$01               ;
CF19: 02 
CF1A: 04 00         LSR   <$00               ;
CF1C: 06 00         ROR   <$00               ;
CF1E: 01 
CF1F: 01 
CF20: 00 00         NEG   <$00               ;
CF22: 01 
CF23: 04 01         LSR   <$01               ;
CF25: 01 
CF26: 00 00         NEG   <$00               ;
CF28: 01 
CF29: 16 06 02      LBRA  $D52E              ;
CF2C: 00 00         NEG   <$00               ;
CF2E: 01 
CF2F: 04 01         LSR   <$01               ;
CF31: 02 
CF32: 00 00         NEG   <$00               ;
CF34: 01 
CF35: 00 04         NEG   <$04               ;
CF37: 01 
CF38: 00 00         NEG   <$00               ;
CF3A: 01 
CF3B: 00 02         NEG   <$02               ;
CF3D: 01 
CF3E: 00 00         NEG   <$00               ;
CF40: 01 
CF41: 00 02         NEG   <$02               ;
CF43: 02 
CF44: 00 00         NEG   <$00               ;
CF46: 43            COMA                     ;
CF47: 4F            CLRA                     ;
CF48: 50            NEGB                     ;
CF49: 59            ROLB                     ;
CF4A: 52 
CF4B: 49            ROLA                     ;
CF4C: 47            ASRA                     ;
CF4D: 48            ASLA                     ;
CF4E: 54            LSRB                     ;
CF4F: 20 31         BRA   $CF82              ;
CF51: 39            RTS                      ;
CF52: 38 
CF53: 30 20         LEAX  0,Y                ;
CF55: 2D 20         BLT   $CF77              ;
CF57: 57            ASRB                     ;
CF58: 49            ROLA                     ;
CF59: 4C            INCA                     ;
CF5A: 4C            INCA                     ;
CF5B: 49            ROLA                     ;
CF5C: 41 
CF5D: 4D            TSTA                     ;
CF5E: 53            COMB                     ;
CF5F: 20 45         BRA   $CFA6              ;
CF61: 4C            INCA                     ;
CF62: 45 
CF63: 43            COMA                     ;
CF64: 54            LSRB                     ;
CF65: 52 
CF66: 4F            CLRA                     ;
CF67: 4E 
CF68: 49            ROLA                     ;
CF69: 43            COMA                     ;
CF6A: 53            COMB                     ;
CF6B: 00 00         NEG   <$00               ;
CF6D: 00 00         NEG   <$00               ;
CF6F: 00 00         NEG   <$00               ;
CF71: 00 00         NEG   <$00               ;
CF73: 00 00         NEG   <$00               ;
CF75: 00 00         NEG   <$00               ;
CF77: 00 00         NEG   <$00               ;
CF79: 00 00         NEG   <$00               ;
CF7B: 00 00         NEG   <$00               ;
CF7D: 00 00         NEG   <$00               ;
CF7F: 00 00         NEG   <$00               ;
CF81: 00 00         NEG   <$00               ;
CF83: 00 00         NEG   <$00               ;
CF85: 00 00         NEG   <$00               ;
CF87: 00 00         NEG   <$00               ;
CF89: 00 00         NEG   <$00               ;
CF8B: 00 00         NEG   <$00               ;
CF8D: 00 00         NEG   <$00               ;
CF8F: 00 00         NEG   <$00               ;
CF91: 00 00         NEG   <$00               ;
CF93: 00 00         NEG   <$00               ;
CF95: 00 00         NEG   <$00               ;
CF97: 00 00         NEG   <$00               ;
CF99: 00 00         NEG   <$00               ;
CF9B: 00 00         NEG   <$00               ;
CF9D: 00 00         NEG   <$00               ;
CF9F: 00 00         NEG   <$00               ;
CFA1: 00 00         NEG   <$00               ;
CFA3: 00 00         NEG   <$00               ;
CFA5: 00 00         NEG   <$00               ;
CFA7: 00 00         NEG   <$00               ;
CFA9: 00 00         NEG   <$00               ;
CFAB: 00 00         NEG   <$00               ;
CFAD: 00 00         NEG   <$00               ;
CFAF: 00 00         NEG   <$00               ;
CFB1: 00 00         NEG   <$00               ;
CFB3: 00 00         NEG   <$00               ;
CFB5: 00 00         NEG   <$00               ;
CFB7: 00 00         NEG   <$00               ;
CFB9: 00 00         NEG   <$00               ;
CFBB: 00 00         NEG   <$00               ;
CFBD: 00 00         NEG   <$00               ;
CFBF: 00 00         NEG   <$00               ;
CFC1: 00 00         NEG   <$00               ;
CFC3: 00 00         NEG   <$00               ;
CFC5: 00 00         NEG   <$00               ;
CFC7: 00 00         NEG   <$00               ;
CFC9: 00 00         NEG   <$00               ;
CFCB: 00 00         NEG   <$00               ;
CFCD: 00 00         NEG   <$00               ;
CFCF: 00 00         NEG   <$00               ;
CFD1: 00 00         NEG   <$00               ;
CFD3: 00 00         NEG   <$00               ;
CFD5: 00 00         NEG   <$00               ;
CFD7: 00 00         NEG   <$00               ;
CFD9: 00 00         NEG   <$00               ;
CFDB: 00 00         NEG   <$00               ;
CFDD: 00 00         NEG   <$00               ;
CFDF: 00 00         NEG   <$00               ;
CFE1: 00 00         NEG   <$00               ;
CFE3: 00 00         NEG   <$00               ;
CFE5: 00 00         NEG   <$00               ;
CFE7: 00 00         NEG   <$00               ;
CFE9: 00 00         NEG   <$00               ;
CFEB: 00 00         NEG   <$00               ;
CFED: 00 00         NEG   <$00               ;
CFEF: 00 4A         NEG   <$4A               ;
CFF1: 00 00         NEG   <$00               ;
CFF3: 00 00         NEG   <$00               ;
CFF5: 00 00         NEG   <$00               ;
CFF7: 00 00         NEG   <$00               ;
CFF9: 00 00         NEG   <$00               ;
CFFB: 00 00         NEG   <$00               ;
CFFD: 00 00         NEG   <$00               ;
CFFF: 00 
```     
