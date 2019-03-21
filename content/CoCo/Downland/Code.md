![Code](downland.jpg)

# Downland Code

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

# Start

```code
C000: 12             NOP                     
C001: 1A 50          ORCC    #$50                           ; Turn off interrupts
C003: 10 CE 01 9F    LDS     #$019F                         ; Stack in low memory
C007: 8E 00 00       LDX     #$0000                         ; Clear ...
C00A: 6F 80          CLR     ,X+                            ; ... 16K ...
C00C: 8C 40 00       CMPX    #$4000                         ; ... of ...
C00F: 26 F9          BNE     $C00A                          ; RAM

C011: 86 7E          LDA     #$7E                           ; Set IRQ ...
C013: B7 01 0C       STA     $010C                          ; ... to ...
C016: 8E DC 4D       LDX     #$DC4D                         ; ... DC4D ...
C019: BF 01 0D       STX     $010D                          ; ... handler
           
C01C: 86 35          LDA     #$35                           ; Enable ...
C01E: B7 FF 03       STA     $FF03                          ; {hard:PIA0_CB} ... 60Hz interrupt

C021: 86 20          LDA     #$20                           ; Swap artifact colors ...
C023: B7 FF 98       STA     $FF98                          ; ... in CoCo3 Video Mode (??makes walls blue??)
C026: 86 FE          LDA     #$FE                           ; All columns OFF ...
C028: B7 FF 02       STA     $FF02                          ; {hard:PIA0_DB} ... except column 0
C02B: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} Read the rows
C02E: 84 10          ANDA    #$10                           ; Only keep row 5 (column 0, row 5 = "0")
C030: 26 0F          BNE     $C041                          ; 1 means NOT PRESSED ... use VDG Mode G6R
; ?? Is this for computers with the GME chip? Like COCO3?
C032: CC 00 09       LDD     #$0009                         ;
C035: FD FF B4       STD     $FFB4                          ; COCO3 low order red/green
C038: CC 24 3F       LDD     #$243F                         ;
C03B: FD FF B6       STD     $FFB6                          ; COCO3 low order blue/composite
C03E: 86 E8          LDA     #$E8                           ; If "0" is pressed E8 - VDG Mode G6C (2 bits per pixel)
C040: 8C 86 F8       CMPX    #$86F8                         ; Normally F8 - VDG Mode G6R (1 bit per pixels with color artifacts)
C043: 97 6A          STA     <$6A                           ; This is our VDG mode from now on

C045: BD C2 01       JSR     $C201                          ; {WaitForIRQ} Wait for an IRQ
C048: CC 1C 00       LDD     #$1C00                         ; Display memory ...
C04B: BD CD F7       JSR     $CDF7                          ; {SetDispMem} ... 1C00
C04E: BD CD E3       JSR     $CDE3                          ; {SetVDGMode} Set the graphics mode
C051: 4F             CLRA                    
C052: BD C1 F6       JSR     $C1F6                          ; 
C055: BD C2 17       JSR     $C217                          ; 
C058: B7 FF DE       STA     $FFDE                          ; {hard:mapType} Make sure we are not running in RAM (pirate copy)
C05B: 8E C0 00       LDX     #$C000          
C05E: 9F 61          STX     <$61            
C060: 9F 72          STX     <$72            
C062: 86 55          LDA     #$55            
C064: 97 71          STA     <$71            
C066: BD DB AD       JSR     $DBAD                          ; 
C069: 0C 51          INC     <$51            
C06B: 8E 03 6B       LDX     #$036B          
C06E: 86 0A          LDA     #$0A            
C070: 6F 80          CLR     ,X+             
C072: 4A             DECA                    
C073: 26 FB          BNE     $C070                          ; 
C075: BD DC C7       JSR     $DCC7                          ; 
C078: 86 01          LDA     #$01            
C07A: 97 3A          STA     <$3A            
C07C: BD D1 1A       JSR     $D11A                          ; 
C07F: 86 0A          LDA     #$0A            
C081: 97 39          STA     <$39            
C083: 86 55          LDA     #$55            
C085: 97 69          STA     <$69            
C087: BD CE 0B       JSR     $CE0B                          ; 
C08A: BD C2 01       JSR     $C201                          ; {WaitForIRQ} 
C08D: CC 1C 00       LDD     #$1C00                         ; Display memory ...
C090: BD CD F7       JSR     $CDF7                          ; {SetDispMem} ... 1C00
C093: BD CD E3       JSR     $CDE3                          ; {SetVDGMode} 
C096: BD CE 10       JSR     $CE10                          ; 
C099: 8E 04 00       LDX     #$0400          
C09C: 9F 4E          STX     <$4E            
C09E: CE CE C4       LDU     #$CEC4          
C0A1: BD D2 4E       JSR     $D24E                          ; 
C0A4: CE DA 19       LDU     #$DA19          
C0A7: 8E C2 3D       LDX     #$C23D          
C0AA: 86 0D          LDA     #$0D            
C0AC: 97 26          STA     <$26            
C0AE: 34 10          PSHS    X               
C0B0: AE 84          LDX     ,X              
C0B2: BD D8 E2       JSR     $D8E2                          ; 
C0B5: 35 10          PULS    X               
C0B7: 30 02          LEAX    2,X             
C0B9: 0A 26          DEC     <$26            
C0BB: 26 F1          BNE     $C0AE                          ; 
C0BD: CE 00 BB       LDU     #$00BB          
C0C0: BD C2 22       JSR     $C222                          ; 
C0C3: CE 00 BB       LDU     #$00BB          
C0C6: 8E 18 12       LDX     #$1812          
C0C9: BD DB 21       JSR     $DB21                          ; 
C0CC: BD D8 E2       JSR     $D8E2                          ; 
C0CF: CE 00 C3       LDU     #$00C3          
C0D2: BD C2 22       JSR     $C222                          ; 
C0D5: CE 00 C3       LDU     #$00C3          
C0D8: 8E 19 52       LDX     #$1952          
C0DB: BD DB 21       JSR     $DB21                          ; 
C0DE: BD D8 E2       JSR     $D8E2                          ; 
C0E1: CE 00 B3       LDU     #$00B3          
C0E4: 8E 16 CC       LDX     #$16CC          
C0E7: BD DB 21       JSR     $DB21                          ; 
C0EA: BD D8 E2       JSR     $D8E2                          ; 
C0ED: CC 04 00       LDD     #$0400                         ; Display memory ...
C0F0: BD CD F7       JSR     $CDF7                          ; {SetDispMem} ... 400
C0F3: 8E 04 00       LDX     #$0400                         ; Copy ...
C0F6: EC 84          LDD     ,X                             ; ... current ...
C0F8: ED 89 18 00    STD     $1800,X                        ; ... screen ...
C0FC: 30 02          LEAX    2,X                            ; ... to ...
C0FE: 8C 1C 00       CMPX    #$1C00                         ; ... drawing ...
C101: 26 F3          BNE     $C0F6                          ; ... screen
C103: 1C EF          ANDCC   #$EF                           ; Turn interrupts back on
C105: 96 51          LDA     <$51            
C107: 97 50          STA     <$50            
C109: 86 01          LDA     #$01            
C10B: 97 52          STA     <$52            
C10D: BD DC 39       JSR     $DC39                          ; 
C110: BD DC 66       JSR     $DC66                          ; 
C113: 96 15          LDA     <$15            
C115: 81 04          CMPA    #$04            
C117: 26 08          BNE     $C121                          ; 
C119: 86 01          LDA     #$01            
C11B: 97 50          STA     <$50            
C11D: 97 51          STA     <$51            
C11F: 20 0A          BRA     $C12B                          ; 
C121: 81 02          CMPA    #$02            
C123: 26 06          BNE     $C12B                          ; 
C125: 86 02          LDA     #$02            
C127: 97 50          STA     <$50            
C129: 97 51          STA     <$51            
C12B: 96 50          LDA     <$50            
C12D: C6 FF          LDB     #$FF            
C12F: 44             LSRA                    
C130: 27 08          BEQ     $C13A                          ; 
C132: 7F 13 64       CLR     $1364           
C135: F7 13 70       STB     $1370           
C138: 20 06          BRA     $C140                          ; 
C13A: F7 13 64       STB     $1364           
C13D: 7F 13 70       CLR     $1370           
C140: BD CF 53       JSR     $CF53                          ; 
C143: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} Check ...
C146: 85 01          BITA    #$01                           ; ... right joystick button
C148: 26 C3          BNE     $C10D                          ; Jump if button is pressed
C14A: C6 03          LDB     #$03            
C14C: D7 55          STB     <$55            
C14E: D7 56          STB     <$56            
C150: BD C2 0D       JSR     $C20D                          ; 
C153: 0F 3A          CLR     <$3A            
C155: 86 01          LDA     #$01            
C157: 97 52          STA     <$52            
C159: CE DA D2       LDU     #$DAD2          
C15C: DF 53          STU     <$53            
C15E: FC D2 72       LDD     $D272                          ; 
C161: DD 5E          STD     <$5E            
C163: 0F 60          CLR     <$60            
C165: BD CB A5       JSR     $CBA5                          ; 
C168: BD D1 1A       JSR     $D11A                          ; 
C16B: BD D1 4C       JSR     $D14C                          ; 
C16E: BD CE B6       JSR     $CEB6                          ; 
C171: BD CE CF       JSR     $CECF                          ; 
C174: BD CE FA       JSR     $CEFA                          ; 
C177: BD CC A3       JSR     $CCA3                          ; 
C17A: BD CC D3       JSR     $CCD3                          ; 
C17D: BD CE 68       JSR     $CE68                          ; 
C180: 10 8E 01 AA    LDY     #$01AA          
C184: BD C6 A9       JSR     $C6A9                          ; 

; Maybe the wait-for-start loop?
           
WaitStartLoop:
C187: 96 48          LDA     <$48            
C189: 27 09          BEQ     $C194                          ; 
C18B: 0F 48          CLR     <$48            
C18D: 10 8E 01 AA    LDY     #$01AA          
C191: BD D8 60       JSR     $D860                          ; 
C194: BD CC B1       JSR     $CCB1                          ; 
C197: BD C3 B3       JSR     $C3B3                          ; 
C19A: 96 49          LDA     <$49            
C19C: 27 09          BEQ     $C1A7                          ; 
C19E: 0F 49          CLR     <$49            
C1A0: 10 8E 01 BF    LDY     #$01BF          
C1A4: BD D8 60       JSR     $D860                          ; 
C1A7: 8E FF 00       LDX     #$FF00          
C1AA: 86 FB          LDA     #$FB            
C1AC: A7 02          STA     2,X             
C1AE: A6 84          LDA     ,X              
C1B0: 84 40          ANDA    #$40            
C1B2: 26 10          BNE     $C1C4                          ; 
C1B4: 34 01          PSHS    CC              
C1B6: 1A 50          ORCC    #$50            
C1B8: 86 FD          LDA     #$FD            
C1BA: A7 02          STA     2,X             
C1BC: E6 84          LDB     ,X              
C1BE: C4 40          ANDB    #$40            
C1C0: 26 F6          BNE     $C1B8                          ; 
C1C2: 35 01          PULS    CC              
C1C4: B6 01 A2       LDA     $01A2           
C1C7: 4A             DECA                    
C1C8: 26 0E          BNE     $C1D8                          ; 
C1CA: B6 01 A0       LDA     $01A0           
C1CD: 84 07          ANDA    #$07            
C1CF: 81 06          CMPA    #$06            
C1D1: 25 05          BCS     $C1D8                          ; 
C1D3: 86 2F          LDA     #$2F            
C1D5: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C1D8: BD CF 53       JSR     $CF53                          ; 
C1DB: 86 02          LDA     #$02            
C1DD: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C1E0: BD CA B6       JSR     $CAB6                          ; 
C1E3: BD CB C3       JSR     $CBC3                          ; 

C1E6: 96 14          LDA     <$14                           ; {ram:m0014} 
C1E8: 27 04          BEQ     $C1EE                          ; 
C1EA: 0F 14          CLR     <$14                           ; {ram:m0014} 
C1EC: 20 99          BRA     $C187                          ; {WaitStartLoop} 
C1EE: 8E 00 23       LDX     #$0023          
C1F1: BD DC 39       JSR     $DC39                          ; 
C1F4: 20 F0          BRA     $C1E6                          ; 
           
C1F6: 8E 7E 00       LDX     #$7E00          
C1F9: A7 80          STA     ,X+             
C1FB: 8C 80 00       CMPX    #$8000          
C1FE: 26 F9          BNE     $C1F9                          ; 
C200: 39             RTS                     

WaitForIRQ:
C201: 34 01          PSHS    CC                             ; Hold the interrupt mask
C203: 0F 14          CLR     <$14                           ; {ram:m0014} Clear the trigger
C205: 1C EF          ANDCC   #$EF                           ; Enable IRQ
C207: 96 14          LDA     <$14                           ; {ram:m0014} Has the interrupt service incremented the trigger?
C209: 27 FC          BEQ     $C207                          ; No ... keep waiting
C20B: 35 81          PULS    CC,PC                          ; Restore interrupt status and done

C20D: 8E 00 BB       LDX     #$00BB          
C210: 6F 80          CLR     ,X+             
C212: 8C 00 D3       CMPX    #$00D3          
C215: 26 F9          BNE     $C210                          ; 
C217: 86 FF          LDA     #$FF            
C219: 97 BA          STA     <$BA            
C21B: 97 C2          STA     <$C2            
C21D: 97 CA          STA     <$CA            
C21F: 97 D2          STA     <$D2            
C221: 39             RTS                     
C222: 8E 00 B3       LDX     #$00B3          
C225: 34 50          PSHS    U,X             
C227: A6 C0          LDA     ,U+             
C229: 2B 06          BMI     $C231                          ; 
C22B: A1 80          CMPA    ,X+             
C22D: 27 F8          BEQ     $C227                          ; 
C22F: 22 02          BHI     $C233                          ; 
C231: 35 D0          PULS    X,U,PC          
C233: 35 50          PULS    X,U             
C235: A6 C0          LDA     ,U+             
C237: 2B E8          BMI     $C221                          ; 
C239: A7 80          STA     ,X+             
C23B: 20 F8          BRA     $C235                          ; 
C23D: 07 C9          ASR     <$C9            
C23F: 09 0A          ROL     <$0A            
C241: 0A 47          DEC     <$47            
C243: 0B                                  
C244: 89 0C          ADCA    #$0C            
C246: C6 0E          LDB     #$0E            
C248: 0A 0F          DEC     <$0F            
C24A: 47             ASRA                    
C24B: 10                                  
C24C: 86 13          LDA     #$13            
C24E: 05                                  
C24F: 13             SYNC                    
C250: 11                                  
C251: 15                                  
C252: 8B 18          ADDA    #$18            
C254: 06 19          ROR     <$19            
C256: 46             RORA                    
C257: 35 20          PULS    Y               
C259: 10 9E 3D       LDY     <$3D            
C25C: 86 0A          LDA     #$0A            
C25E: 97 43          STA     <$43            
C260: 86 08          LDA     #$08            
C262: 97 44          STA     <$44            
C264: C6 05          LDB     #$05            
C266: A6 A4          LDA     ,Y              
C268: 94 52          ANDA    <$52            
C26A: 27 0D          BEQ     $C279                          ; 
C26C: A6 22          LDA     2,Y             
C26E: DD 41          STD     <$41            
C270: A6 23          LDA     3,Y             
C272: 97 42          STA     <$42            
C274: BD C3 7C       JSR     $C37C                          ; 
C277: 26 6B          BNE     $C2E4                          ; 
C279: 31 25          LEAY    5,Y             
C27B: 5A             DECB                    
C27C: 26 E8          BNE     $C266                          ; 
C27E: 10 8E 01 EF    LDY     #$01EF          
C282: 86 06          LDA     #$06            
C284: 97 43          STA     <$43            
C286: 86 04          LDA     #$04            
C288: 97 44          STA     <$44            
C28A: D6 3F          LDB     <$3F            
C28C: A6 A4          LDA     ,Y              
C28E: 27 13          BEQ     $C2A3                          ; 
C290: A6 23          LDA     3,Y             
C292: 97 41          STA     <$41            
C294: A6 25          LDA     5,Y             
C296: 97 42          STA     <$42            
C298: BD C3 7C       JSR     $C37C                          ; 
C29B: 27 06          BEQ     $C2A3                          ; 
C29D: A6 A4          LDA     ,Y              
C29F: 2B 02          BMI     $C2A3                          ; 
C2A1: 20 3A          BRA     $C2DD                          ; 
C2A3: 31 2D          LEAY    13,Y            
C2A5: 5A             DECB                    
C2A6: 26 E4          BNE     $C28C                          ; 
C2A8: 86 08          LDA     #$08            
C2AA: 97 43          STA     <$43            
C2AC: 86 08          LDA     #$08            
C2AE: 97 44          STA     <$44            
C2B0: B6 01 C3       LDA     $01C3           
C2B3: 97 41          STA     <$41            
C2B5: B6 01 C5       LDA     $01C5           
C2B8: 97 42          STA     <$42            
C2BA: BD C3 7C       JSR     $C37C                          ; 
C2BD: 26 1E          BNE     $C2DD                          ; 
C2BF: 86 06          LDA     #$06            
C2C1: 97 43          STA     <$43            
C2C3: 86 08          LDA     #$08            
C2C5: 97 44          STA     <$44            
C2C7: B6 01 D8       LDA     $01D8           
C2CA: 97 41          STA     <$41            
C2CC: B6 01 DA       LDA     $01DA           
C2CF: 97 42          STA     <$42            
C2D1: BD C3 7C       JSR     $C37C                          ; 
C2D4: 26 07          BNE     $C2DD                          ; 
C2D6: 10 8E 01 AA    LDY     #$01AA          
C2DA: 7E C4 8C       JMP     $C48C                          ; 
C2DD: 10 8E 01 AA    LDY     #$01AA          
C2E1: 7E C5 3C       JMP     $C53C                          ; 
C2E4: 96 52          LDA     <$52            
C2E6: 43             COMA                    
C2E7: A4 A4          ANDA    ,Y              
C2E9: A7 A4          STA     ,Y              
C2EB: E6 24          LDB     4,Y             
C2ED: 2B 2C          BMI     $C31B                          ; 
C2EF: 8E 3E C0       LDX     #$3EC0          
C2F2: 30 85          LEAX    B,X             
C2F4: A6 84          LDA     ,X              
C2F6: 9A 52          ORA     <$52            
C2F8: A7 84          STA     ,X              
C2FA: BD CC A7       JSR     $CCA7                          ; 
C2FD: E1 05          CMPB    5,X             
C2FF: 27 0A          BEQ     $C30B                          ; 
C301: 30 89 00 06    LEAX    $0006,X         
C305: A6 84          LDA     ,X              
C307: 26 F4          BNE     $C2FD                          ; 
C309: 20 10          BRA     $C31B                          ; 
C30B: CE 1C 00       LDU     #$1C00          
C30E: DF 4E          STU     <$4E            
C310: BD CD 81       JSR     $CD81                          ; 
C313: CE 04 00       LDU     #$0400          
C316: DF 4E          STU     <$4E            
C318: BD CD 81       JSR     $CD81                          ; 
C31B: DC 1B          LDD     <$1B            
C31D: BD DC 39       JSR     $DC39                          ; 
C320: C4 7F          ANDB    #$7F            
C322: A6 21          LDA     1,Y             
C324: 27 0E          BEQ     $C334                          ; 
C326: 4A             DECA                    
C327: 27 06          BEQ     $C32F                          ; 
C329: 4F             CLRA                    
C32A: C3 00 C8       ADDD    #$00C8          
C32D: 20 08          BRA     $C337                          ; 
C32F: C3 01 2C       ADDD    #$012C          
C332: 20 03          BRA     $C337                          ; 
C334: C3 01 90       ADDD    #$0190          
C337: 34 20          PSHS    Y               
C339: BD DB 0C       JSR     $DB0C                          ; 
C33C: 35 20          PULS    Y               
C33E: BD D1 42       JSR     $D142                          ; 
C341: D7 26          STB     <$26            
C343: 8D 0C          BSR     $C351                          ; 
C345: CC 12 80       LDD     #$1280          
C348: 8D 15          BSR     $C35F                          ; 
C34A: 10 8E 01 AA    LDY     #$01AA          
C34E: 7E D8 60       JMP     $D860                          ; 
C351: EC 89 18 00    LDD     $1800,X         
C355: ED 84          STD     ,X              
C357: 30 88 20       LEAX    $20,X           
C35A: 0A 26          DEC     <$26            
C35C: 26 F3          BNE     $C351                          ; 
C35E: 39             RTS                     
C35F: 97 4D          STA     <$4D            
C361: D7 26          STB     <$26            
C363: 86 FF          LDA     #$FF            
C365: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C368: 8D 0C          BSR     $C376                          ; 
C36A: 86 02          LDA     #$02            
C36C: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C36F: 8D 05          BSR     $C376                          ; 
C371: 0A 26          DEC     <$26            
C373: 26 EE          BNE     $C363                          ; 
C375: 39             RTS                     
C376: D6 4D          LDB     <$4D            
C378: 5A             DECB                    
C379: 26 FD          BNE     $C378                          ; 
C37B: 39             RTS                     
C37C: 8E 01 AA       LDX     #$01AA          
C37F: A6 04          LDA     4,X             
C381: 91 41          CMPA    <$41            
C383: 23 08          BLS     $C38D                          ; 
C385: 90 41          SUBA    <$41            
C387: 91 43          CMPA    <$43            
C389: 23 0A          BLS     $C395                          ; 
C38B: 20 20          BRA     $C3AD                          ; 
C38D: 96 41          LDA     <$41            
C38F: A0 04          SUBA    4,X             
C391: A1 1F          CMPA    -1,X            
C393: 22 18          BHI     $C3AD                          ; 
C395: A6 06          LDA     6,X             
C397: 91 42          CMPA    <$42            
C399: 23 08          BLS     $C3A3                          ; 
C39B: 90 42          SUBA    <$42            
C39D: 91 44          CMPA    <$44            
C39F: 23 0E          BLS     $C3AF                          ; 
C3A1: 20 0A          BRA     $C3AD                          ; 
C3A3: 96 42          LDA     <$42            
C3A5: A0 06          SUBA    6,X             
C3A7: 81 08          CMPA    #$08            
C3A9: 23 04          BLS     $C3AF                          ; 
C3AB: 20 00          BRA     $C3AD                          ; 
C3AD: 4F             CLRA                    
C3AE: 39             RTS                     
C3AF: 86 FF          LDA     #$FF            
C3B1: 39             RTS                     
C3B2: 39             RTS                     
C3B3: 10 8E 01 AA    LDY     #$01AA          
C3B7: A6 38          LDA     -8,Y            
C3B9: 4A             DECA                    
C3BA: 26 05          BNE     $C3C1                          ; 
C3BC: C6 3F          LDB     #$3F            
C3BE: F7 FF 20       STB     $FF20                          ; {hard:PIA1_DA} Sound
C3C1: A6 3B          LDA     -5,Y            
C3C3: 27 ED          BEQ     $C3B2                          ; 
C3C5: 81 01          CMPA    #$01            
C3C7: 10 27 00 C1    LBEQ    $00C1           
C3CB: 96 30          LDA     <$30            
C3CD: 10 26 01 7B    LBNE    $017B           
C3D1: A6 3E          LDA     -2,Y            
C3D3: 10 2B 02 E1    LBMI    $02E1           
C3D7: 10 26 00 BD    LBNE    $00BD           
C3DB: 6C 36          INC     -10,Y           
C3DD: CE 3B 80       LDU     #$3B80          
C3E0: A6 38          LDA     -8,Y            
C3E2: C6 3C          LDB     #$3C            
C3E4: 3D             MUL                     
C3E5: 33 CB          LEAU    D,U             
C3E7: A6 26          LDA     6,Y             
C3E9: 84 03          ANDA    #$03            
C3EB: C6 0F          LDB     #$0F            
C3ED: 3D             MUL                     
C3EE: 33 CB          LEAU    D,U             
C3F0: A6 38          LDA     -8,Y            
C3F2: 81 03          CMPA    #$03            
C3F4: 22 08          BHI     $C3FE                          ; 
C3F6: A6 3C          LDA     -4,Y            
C3F8: 26 04          BNE     $C3FE                          ; 
C3FA: 33 C9 01 68    LEAU    $0168,U         
C3FE: AE 2C          LDX     12,Y            
C400: 30 88 20       LEAX    $20,X           
C403: 34 20          PSHS    Y               
C405: 10 8E 00 74    LDY     #$0074          
C409: 86 05          LDA     #$05            
C40B: 97 26          STA     <$26            
C40D: 37 06          PULU    A,B             
C40F: A4 84          ANDA    ,X              
C411: AA 89 18 00    ORA     $1800,X         
C415: A7 A0          STA     ,Y+             
C417: E4 01          ANDB    1,X             
C419: EA 89 18 01    ORB     $1801,X         
C41D: E7 A0          STB     ,Y+             
C41F: 37 02          PULU    A               
C421: A4 02          ANDA    2,X             
C423: AA 89 18 02    ORA     $1802,X         
C427: A7 A0          STA     ,Y+             
C429: 30 88 60       LEAX    $60,X           
C42C: 0A 26          DEC     <$26            
C42E: 26 DD          BNE     $C40D                          ; 
C430: 35 20          PULS    Y               
C432: CE 34 00       LDU     #$3400          
C435: A6 38          LDA     -8,Y            
C437: C6 C0          LDB     #$C0            
C439: 3D             MUL                     
C43A: 33 CB          LEAU    D,U             
C43C: A6 26          LDA     6,Y             
C43E: 84 03          ANDA    #$03            
C440: C6 30          LDB     #$30            
C442: 3D             MUL                     
C443: 33 CB          LEAU    D,U             
C445: 33 43          LEAU    3,U             
C447: A6 38          LDA     -8,Y            
C449: 81 03          CMPA    #$03            
C44B: 22 08          BHI     $C455                          ; 
C44D: A6 3C          LDA     -4,Y            
C44F: 26 04          BNE     $C455                          ; 
C451: 33 C9 04 80    LEAU    $0480,U         
C455: AE 2C          LDX     12,Y            
C457: 30 89 18 20    LEAX    $1820,X         
C45B: 34 20          PSHS    Y               
C45D: 10 8E 00 74    LDY     #$0074          
C461: 86 05          LDA     #$05            
C463: 97 26          STA     <$26            
C465: 37 06          PULU    A,B             
C467: AA 84          ORA     ,X              
C469: A1 A0          CMPA    ,Y+             
C46B: 10 26 FD E8    LBNE    $FDE8           
C46F: EA 01          ORB     1,X             
C471: E1 A0          CMPB    ,Y+             
C473: 10 26 FD E0    LBNE    $FDE0           
C477: 37 02          PULU    A               
C479: AA 02          ORA     2,X             
C47B: A1 A0          CMPA    ,Y+             
C47D: 10 26 FD D6    LBNE    $FDD6           
C481: 30 88 60       LEAX    $60,X           
C484: 33 46          LEAU    6,U             
C486: 0A 26          DEC     <$26            
C488: 26 DB          BNE     $C465                          ; 
C48A: 35 20          PULS    Y               
C48C: 96 2C          LDA     <$2C            
C48E: 10 26 03 17    LBNE    $0317           
C492: A6 35          LDA     -11,Y           
C494: 10 26 00 94    LBNE    $0094           
C498: 8D 4D          BSR     $C4E7                          ; 
C49A: 30 89 02 00    LEAX    $0200,X         
C49E: CE C5 0D       LDU     #$C50D          
C4A1: EC C6          LDD     A,U             
C4A3: A4 89 18 00    ANDA    $1800,X         
C4A7: E4 89 18 01    ANDB    $1801,X         
C4AB: 10 93 1B       CMPD    <$1B            
C4AE: 27 0E          BEQ     $C4BE                          ; 
C4B0: 34 04          PSHS    B               
C4B2: BD CA 9B       JSR     $CA9B                          ; 
C4B5: 35 02          PULS    A               
C4B7: 26 73          BNE     $C52C                          ; 
C4B9: BD CA 9B       JSR     $CA9B                          ; 
C4BC: 26 6E          BNE     $C52C                          ; 
C4BE: 86 FF          LDA     #$FF            
C4C0: 97 2D          STA     <$2D            
C4C2: EC A4          LDD     ,Y              
C4C4: C3 00 06       ADDD    #$0006          
C4C7: 10 83 01 00    CMPD    #$0100          
C4CB: 23 05          BLS     $C4D2                          ; 
C4CD: 0F 2E          CLR     <$2E            
C4CF: CC 01 00       LDD     #$0100          
C4D2: ED A4          STD     ,Y              
C4D4: 96 2E          LDA     <$2E            
C4D6: 2B 2A          BMI     $C502                          ; 
C4D8: A6 3C          LDA     -4,Y            
C4DA: 2B 1B          BMI     $C4F7                          ; 
C4DC: EC 22          LDD     2,Y             
C4DE: C3 00 01       ADDD    #$0001          
C4E1: 2B 1D          BMI     $C500                          ; 
C4E3: DC 1B          LDD     <$1B            
C4E5: 20 19          BRA     $C500                          ; 
C4E7: 8E C5 09       LDX     #$C509          
C4EA: E6 26          LDB     6,Y             
C4EC: C4 03          ANDB    #$03            
C4EE: 1F 98          TFR     B,A             
C4F0: E6 85          LDB     B,X             
C4F2: AE 28          LDX     8,Y             
C4F4: 3A             ABX                     
C4F5: 48             LSLA                    
C4F6: 39             RTS                     
C4F7: EC 22          LDD     2,Y             
C4F9: C3 FF FF       ADDD    #$FFFF          
C4FC: 2A 02          BPL     $C500                          ; 
C4FE: DC 1B          LDD     <$1B            
C500: ED 22          STD     2,Y             
C502: A6 3E          LDA     -2,Y            
C504: 26 69          BNE     $C56F                          ; 
C506: 7E C7 83       JMP     $C783                          ; 
C509: 00 00          NEG     <$00            
C50B: 00 01          NEG     <$01            
C50D: 03 C0          COM     <$C0            
C50F: 00 F0          NEG     <$F0            
C511: 00 3C          NEG     <$3C            
C513: 0F 00          CLR     <$00            
C515: 3F             SWI                     
C516: F0 0F FC       SUBB    $0FFC           
C519: 03 FF          COM     <$FF            
C51B: FF C0 03       STU     $C003                          ; 
C51E: 00 00          NEG     <$00            
C520: C0 00          SUBB    #$00            
C522: 30 0C          LEAX    12,X            
C524: 00 DC          NEG     <$DC            
C526: 1B                                  
C527: ED A4          STD     ,Y              
C529: ED 22          STD     2,Y             
C52B: 39             RTS                     
C52C: 0F 2D          CLR     <$2D            
C52E: A6 3E          LDA     -2,Y            
C530: 26 3D          BNE     $C56F                          ; 
C532: EC A4          LDD     ,Y              
C534: 10 83 01 00    CMPD    #$0100          
C538: 10 26 01 DC    LBNE    $01DC           
C53C: 8D E7          BSR     $C525                          ; 
C53E: 6F 35          CLR     -11,Y           
C540: 0F 2C          CLR     <$2C            
C542: 0F 2F          CLR     <$2F            
C544: 96 2D          LDA     <$2D            
C546: 27 1C          BEQ     $C564                          ; 
C548: 86 32          LDA     #$32            
C54A: 97 30          STA     <$30            
C54C: 0A 30          DEC     <$30            
C54E: 27 14          BEQ     $C564                          ; 
C550: 96 30          LDA     <$30            
C552: 84 04          ANDA    #$04            
C554: 27 05          BEQ     $C55B                          ; 
C556: 86 FF          LDA     #$FF            
C558: A7 3C          STA     -4,Y            
C55A: 8C 6F 3C       CMPX    #$6F3C          
C55D: 86 02          LDA     #$02            
C55F: A7 38          STA     -8,Y            
C561: 7E C9 7F       JMP     $C97F                          ; 
C564: 86 0A          LDA     #$0A            
C566: A7 3D          STA     -3,Y            
C568: 86 02          LDA     #$02            
C56A: A7 3E          STA     -2,Y            
C56C: 7E C3 B2       JMP     $C3B2                          ; 
C56F: 96 2D          LDA     <$2D            
C571: 26 93          BNE     $C506                          ; 
C573: 8D B0          BSR     $C525                          ; 
C575: A6 3E          LDA     -2,Y            
C577: 4A             DECA                    
C578: 27 32          BEQ     $C5AC                          ; 
C57A: 8E 00 83       LDX     #$0083          
C57D: 86 30          LDA     #$30            
C57F: 6F 80          CLR     ,X+             
C581: 4A             DECA                    
C582: 26 FB          BNE     $C57F                          ; 
C584: 8E 00 98       LDX     #$0098          
C587: CE DE EF       LDU     #$DEEF          
C58A: 86 1B          LDA     #$1B            
C58C: E6 C0          LDB     ,U+             
C58E: E7 80          STB     ,X+             
C590: 4A             DECA                    
C591: 26 F9          BNE     $C58C                          ; 
C593: A6 26          LDA     6,Y             
C595: 84 03          ANDA    #$03            
C597: 27 07          BEQ     $C5A0                          ; 
C599: 97 26          STA     <$26            
C59B: C6 10          LDB     #$10            
C59D: BD CD C9       JSR     $CDC9                          ; 
C5A0: CC 25 08       LDD     #$2508          
C5A3: BD C3 5F       JSR     $C35F                          ; 
C5A6: CE 00 83       LDU     #$0083          
C5A9: BD C9 A2       JSR     $C9A2                          ; 
C5AC: 6A 3D          DEC     -3,Y            
C5AE: 10 26 FE 00    LBNE    $FE00           
C5B2: 6A 3E          DEC     -2,Y            
C5B4: 27 28          BEQ     $C5DE                          ; 
C5B6: 86 0C          LDA     #$0C            
C5B8: A7 3F          STA     -1,Y            
C5BA: 17 12 F8       LBSR    $12F8           
C5BD: 86 10          LDA     #$10            
C5BF: A7 3F          STA     -1,Y            
C5C1: 86 46          LDA     #$46            
C5C3: A7 3D          STA     -3,Y            
C5C5: 16 FD EA       LBRA    $FDEA           
C5C8: 8E C5 D2       LDX     #$C5D2          
C5CB: 96 52          LDA     <$52            
C5CD: 84 02          ANDA    #$02            
C5CF: AE 86          LDX     A,X             
C5D1: 39             RTS                     
C5D2: 00 55          NEG     <$55            
C5D4: 00 56          NEG     <$56            
C5D6: 00 57          NEG     <$57            
C5D8: 00 5C          NEG     <$5C            
C5DA: DA DA          ORB     <$DA            
C5DC: DA EF          ORB     <$EF            
C5DE: B6 01 CF       LDA     $01CF           
C5E1: 27 11          BEQ     $C5F4                          ; 
C5E3: BD CB B9       JSR     $CBB9                          ; 
C5E6: D6 39          LDB     <$39            
C5E8: 58             LSLB                    
C5E9: 3A             ABX                     
C5EA: CC 08 00       LDD     #$0800          
C5ED: ED 84          STD     ,X              
C5EF: 86 FF          LDA     #$FF            
C5F1: B7 01 CF       STA     $01CF           
C5F4: 8D D2          BSR     $C5C8                          ; 
C5F6: A6 84          LDA     ,X              
C5F8: 81 05          CMPA    #$05            
C5FA: 23 04          BLS     $C600                          ; 
C5FC: 86 05          LDA     #$05            
C5FE: A7 84          STA     ,X              
C600: 6A 84          DEC     ,X              
C602: 10 2B 16 06    LBMI    $1606           
C606: 34 20          PSHS    Y               
C608: 96 50          LDA     <$50            
C60A: 84 02          ANDA    #$02            
C60C: 10 27 00 95    LBEQ    $0095           
C610: 96 52          LDA     <$52            
C612: 84 02          ANDA    #$02            
C614: 26 0A          BNE     $C620                          ; 
C616: 0C 52          INC     <$52            
C618: CE DA D6       LDU     #$DAD6          
C61B: 8E 00 57       LDX     #$0057          
C61E: 20 08          BRA     $C628                          ; 
C620: 0A 52          DEC     <$52            
C622: CE DA D2       LDU     #$DAD2          
C625: 8E 00 5C       LDX     #$005C          
C628: DF 53          STU     <$53            
C62A: A6 24          LDA     4,Y             
C62C: E6 26          LDB     6,Y             
C62E: ED 02          STD     2,X             
C630: 96 39          LDA     <$39            
C632: A7 04          STA     4,X             
C634: BD CE 10       JSR     $CE10                          ; 
C637: CC 1C 00       LDD     #$1C00          
C63A: BD CD F7       JSR     $CDF7                          ; {SetDispMem} 
C63D: CE CE C4       LDU     #$CEC4          
C640: BD D2 4E       JSR     $D24E                          ; 
C643: 96 52          LDA     <$52            
C645: 84 02          ANDA    #$02            
C647: 8E C5 DA       LDX     #$C5DA          
C64A: EE 86          LDU     A,X             
C64C: 8E 0F 66       LDX     #$0F66          
C64F: BD D8 E2       JSR     $D8E2                          ; 
C652: BD C2 01       JSR     $C201                          ; {WaitForIRQ} 
C655: 1C EF          ANDCC   #$EF            
C657: CC 04 00       LDD     #$0400          
C65A: BD CD F7       JSR     $CDF7                          ; {SetDispMem} 
C65D: 8E 04 00       LDX     #$0400          
C660: EC 81          LDD     ,X++            
C662: ED 89 17 FE    STD     $17FE,X         
C666: 8C 1C 00       CMPX    #$1C00          
C669: 26 F5          BNE     $C660                          ; 
C66B: BD D1 1A       JSR     $D11A                          ; 
C66E: 86 0A          LDA     #$0A            
C670: 97 3F          STA     <$3F            
C672: 97 39          STA     <$39            
C674: BD CF 53       JSR     $CF53                          ; 
C677: 8E FF 00       LDX     #$FF00          
C67A: 86 FF          LDA     #$FF            
C67C: A7 02          STA     2,X             
C67E: A6 84          LDA     ,X              
C680: 95 52          BITA    <$52            
C682: 27 12          BEQ     $C696                          ; 
C684: 85 01          BITA    #$01            
C686: 27 EC          BEQ     $C674                          ; 
C688: 85 02          BITA    #$02            
C68A: 27 E8          BEQ     $C674                          ; 
C68C: 6F 02          CLR     2,X             
C68E: A6 84          LDA     ,X              
C690: 8A 83          ORA     #$83            
C692: 81 FF          CMPA    #$FF            
C694: 27 DE          BEQ     $C674                          ; 
C696: 8E C5 D6       LDX     #$C5D6          
C699: 96 52          LDA     <$52            
C69B: 84 02          ANDA    #$02            
C69D: AE 86          LDX     A,X             
C69F: 10 AE E4       LDY     ,S              
C6A2: BD CC D3       JSR     $CCD3                          ; 
C6A5: 35 20          PULS    Y               
C6A7: 6C 3B          INC     -5,Y            
C6A9: 86 28          LDA     #$28            
C6AB: A7 3D          STA     -3,Y            
C6AD: CC 01 90       LDD     #$0190          
C6B0: DD 4B          STD     <$4B            
C6B2: 86 FF          LDA     #$FF            
C6B4: A7 3E          STA     -2,Y            
C6B6: 6F 38          CLR     -8,Y            
C6B8: BD DC 66       JSR     $DC66                          ; 
C6BB: 96 15          LDA     <$15            
C6BD: 27 04          BEQ     $C6C3                          ; 
C6BF: DC 1B          LDD     <$1B            
C6C1: DD 4B          STD     <$4B            
C6C3: 4F             CLRA                    
C6C4: DC 4B          LDD     <$4B            
C6C6: 27 05          BEQ     $C6CD                          ; 
C6C8: 83 00 01       SUBD    #$0001          
C6CB: DD 4B          STD     <$4B            
C6CD: A6 3D          LDA     -3,Y            
C6CF: 27 03          BEQ     $C6D4                          ; 
C6D1: 4A             DECA                    
C6D2: A7 3D          STA     -3,Y            
C6D4: 26 5A          BNE     $C730                          ; 
C6D6: DC 4B          LDD     <$4B            
C6D8: 26 56          BNE     $C730                          ; 
C6DA: 34 20          PSHS    Y               
C6DC: 10 8E 01 E9    LDY     #$01E9          
C6E0: BD C5 C8       JSR     $C5C8                          ; 
C6E3: A6 84          LDA     ,X              
C6E5: E6 3B          LDB     -5,Y            
C6E7: 3D             MUL                     
C6E8: AE 22          LDX     2,Y             
C6EA: 30 8B          LEAX    D,X             
C6EC: A6 3F          LDA     -1,Y            
C6EE: 97 26          STA     <$26            
C6F0: DC 1B          LDD     <$1B            
C6F2: ED 84          STD     ,X              
C6F4: 30 88 20       LEAX    $20,X           
C6F7: 0A 26          DEC     <$26            
C6F9: 26 F7          BNE     $C6F2                          ; 
C6FB: 35 20          PULS    Y               
C6FD: 6F 3E          CLR     -2,Y            
C6FF: AE 28          LDX     8,Y             
C701: E6 3F          LDB     -1,Y            
C703: D7 26          STB     <$26            
C705: EC 89 18 00    LDD     $1800,X         
C709: ED 84          STD     ,X              
C70B: A6 89 18 02    LDA     $1802,X         
C70F: A7 02          STA     2,X             
C711: 30 88 20       LEAX    $20,X           
C714: 0A 26          DEC     <$26            
C716: 26 ED          BNE     $C705                          ; 
C718: A6 35          LDA     -11,Y           
C71A: 2B 18          BMI     $C734                          ; 
C71C: EC A4          LDD     ,Y              
C71E: 27 14          BEQ     $C734                          ; 
C720: 86 04          LDA     #$04            
C722: 97 2F          STA     <$2F            
C724: 6F 38          CLR     -8,Y            
C726: 0F 2E          CLR     <$2E            
C728: 86 7F          LDA     #$7F            
C72A: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C72D: 7E C7 BE       JMP     $C7BE                          ; 
C730: 4F             CLRA                    
C731: 7E C8 5F       JMP     $C85F                          ; 
C734: BD DC 66       JSR     $DC66                          ; 
C737: A6 35          LDA     -11,Y           
C739: 27 28          BEQ     $C763                          ; 
C73B: 81 01          CMPA    #$01            
C73D: 10 27 00 86    LBEQ    $0086           
C741: 96 15          LDA     <$15            
C743: 81 02          CMPA    #$02            
C745: 27 13          BEQ     $C75A                          ; 
C747: 81 04          CMPA    #$04            
C749: 27 08          BEQ     $C753                          ; 
C74B: 0F 2C          CLR     <$2C            
C74D: 0F 2F          CLR     <$2F            
C74F: 0F 2E          CLR     <$2E            
C751: 20 74          BRA     $C7C7                          ; 
C753: 6F 3C          CLR     -4,Y            
C755: CC FF CA       LDD     #$FFCA          
C758: 20 07          BRA     $C761                          ; 
C75A: 86 FF          LDA     #$FF            
C75C: A7 3C          STA     -4,Y            
C75E: CC 00 36       LDD     #$0036          
C761: ED 22          STD     2,Y             
C763: 96 52          LDA     <$52            
C765: B5 FF 00       BITA    $FF00                          ; {hard:PIA0_DA} 
C768: 26 5D          BNE     $C7C7                          ; 
C76A: 96 31          LDA     <$31            
C76C: 26 5B          BNE     $C7C9                          ; 
C76E: 0A 31          DEC     <$31            
C770: 96 2F          LDA     <$2F            
C772: 26 53          BNE     $C7C7                          ; 
C774: CC FF 61       LDD     #$FF61          
C777: ED A4          STD     ,Y              
C779: 86 28          LDA     #$28            
C77B: 97 2C          STA     <$2C            
C77D: 86 FF          LDA     #$FF            
C77F: 97 2E          STA     <$2E            
C781: 97 2D          STA     <$2D            
C783: 7E C8 6F       JMP     $C86F                          ; 
C786: E6 26          LDB     6,Y             
C788: A6 3C          LDA     -4,Y            
C78A: 27 04          BEQ     $C790                          ; 
C78C: CB 04          ADDB    #$04            
C78E: 20 02          BRA     $C792                          ; 
C790: C0 04          SUBB    #$04            
C792: E7 26          STB     6,Y             
C794: BD C5 25       JSR     $C525                          ; 
C797: 97 36          STA     <$36            
C799: A6 35          LDA     -11,Y           
C79B: 2B 05          BMI     $C7A2                          ; 
C79D: 6F 35          CLR     -11,Y           
C79F: 7E C8 79       JMP     $C879                          ; 
C7A2: 86 01          LDA     #$01            
C7A4: A7 35          STA     -11,Y           
C7A6: 7E C8 79       JMP     $C879                          ; 
C7A9: 96 2C          LDA     <$2C            
C7AB: 48             LSLA                    
C7AC: 8A 02          ORA     #$02            
C7AE: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C7B1: EC A4          LDD     ,Y              
C7B3: C3 00 03       ADDD    #$0003          
C7B6: ED A4          STD     ,Y              
C7B8: 0A 2C          DEC     <$2C            
C7BA: 10 26 00 BB    LBNE    $00BB           
C7BE: DC 1B          LDD     <$1B            
C7C0: ED A4          STD     ,Y              
C7C2: A7 35          STA     -11,Y           
C7C4: 7E C8 79       JMP     $C879                          ; 
C7C7: 0F 31          CLR     <$31            
C7C9: 96 15          LDA     <$15            
C7CB: 10 2B 00 8A    LBMI    $008A           
C7CF: 27 39          BEQ     $C80A                          ; 
C7D1: 81 02          CMPA    #$02            
C7D3: 25 28          BCS     $C7FD                          ; 
C7D5: 27 5E          BEQ     $C835                          ; 
C7D7: 81 03          CMPA    #$03            
C7D9: 27 42          BEQ     $C81D                          ; 
C7DB: A6 3C          LDA     -4,Y            
C7DD: 27 04          BEQ     $C7E3                          ; 
C7DF: 0F 36          CLR     <$36            
C7E1: 6F 3C          CLR     -4,Y            
C7E3: A6 35          LDA     -11,Y           
C7E5: 27 0F          BEQ     $C7F6                          ; 
C7E7: BD C5 25       JSR     $C525                          ; 
C7EA: 0C 36          INC     <$36            
C7EC: 96 36          LDA     <$36            
C7EE: 81 14          CMPA    #$14            
C7F0: 22 94          BHI     $C786                          ; 
C7F2: DC 1B          LDD     <$1B            
C7F4: 20 03          BRA     $C7F9                          ; 
C7F6: CC FF CA       LDD     #$FFCA          
C7F9: ED 22          STD     2,Y             
C7FB: 20 5C          BRA     $C859                          ; 
C7FD: 0F 36          CLR     <$36            
C7FF: A6 35          LDA     -11,Y           
C801: 2A 07          BPL     $C80A                          ; 
C803: CC FF C0       LDD     #$FFC0          
C806: ED A4          STD     ,Y              
C808: 20 1E          BRA     $C828                          ; 
C80A: 0F 36          CLR     <$36            
C80C: BD C5 25       JSR     $C525                          ; 
C80F: E6 35          LDB     -11,Y           
C811: 2A 4C          BPL     $C85F                          ; 
C813: A6 38          LDA     -8,Y            
C815: 81 03          CMPA    #$03            
C817: 22 02          BHI     $C81B                          ; 
C819: 86 04          LDA     #$04            
C81B: 20 14          BRA     $C831                          ; 
C81D: 0F 36          CLR     <$36            
C81F: A6 35          LDA     -11,Y           
C821: 2A E7          BPL     $C80A                          ; 
C823: CC 00 70       LDD     #$0070          
C826: ED A4          STD     ,Y              
C828: A6 36          LDA     -10,Y           
C82A: 44             LSRA                    
C82B: 44             LSRA                    
C82C: 44             LSRA                    
C82D: 84 01          ANDA    #$01            
C82F: 8B 04          ADDA    #$04            
C831: A7 38          STA     -8,Y            
C833: 20 44          BRA     $C879                          ; 
C835: A6 3C          LDA     -4,Y            
C837: 2B 06          BMI     $C83F                          ; 
C839: 0F 36          CLR     <$36            
C83B: 86 FF          LDA     #$FF            
C83D: A7 3C          STA     -4,Y            
C83F: A6 35          LDA     -11,Y           
C841: 27 11          BEQ     $C854                          ; 
C843: BD C5 25       JSR     $C525                          ; 
C846: 0C 36          INC     <$36            
C848: 96 36          LDA     <$36            
C84A: 81 14          CMPA    #$14            
C84C: 10 22 FF 36    LBHI    $FF36                          ; ?? WRONG. This is a relative offset -- not a destination
C850: DC 1B          LDD     <$1B            
C852: 20 03          BRA     $C857                          ; 
C854: CC 00 36       LDD     #$0036          
C857: ED 22          STD     2,Y             
C859: A6 36          LDA     -10,Y           
C85B: 44             LSRA                    
C85C: 44             LSRA                    
C85D: 84 03          ANDA    #$03            
C85F: E6 35          LDB     -11,Y           
C861: 27 0E          BEQ     $C871                          ; 
C863: 2A 0A          BPL     $C86F                          ; 
C865: A6 38          LDA     -8,Y            
C867: 81 03          CMPA    #$03            
C869: 22 06          BHI     $C871                          ; 
C86B: 86 05          LDA     #$05            
C86D: 20 02          BRA     $C871                          ; 
C86F: 86 02          LDA     #$02            
C871: A7 38          STA     -8,Y            
C873: D6 2F          LDB     <$2F            
C875: 27 02          BEQ     $C879                          ; 
C877: 0A 2F          DEC     <$2F            
C879: A6 35          LDA     -11,Y           
C87B: 81 01          CMPA    #$01            
C87D: 27 78          BEQ     $C8F7                          ; 
C87F: BD C4 E7       JSR     $C4E7                          ; 
C882: 30 89 01 00    LEAX    $0100,X         
C886: CE C5 1D       LDU     #$C51D          
C889: EC C6          LDD     A,U             
C88B: A4 89 18 00    ANDA    $1800,X         
C88F: E4 89 18 01    ANDB    $1801,X         
C893: 10 93 1B       CMPD    <$1B            
C896: 27 1D          BEQ     $C8B5                          ; 
C898: 34 04          PSHS    B               
C89A: 8D 1D          BSR     $C8B9                          ; 
C89C: 35 02          PULS    A               
C89E: 26 04          BNE     $C8A4                          ; 
C8A0: 8D 17          BSR     $C8B9                          ; 
C8A2: 27 11          BEQ     $C8B5                          ; 
C8A4: A6 35          LDA     -11,Y           
C8A6: 2B 1A          BMI     $C8C2                          ; 
C8A8: 86 FF          LDA     #$FF            
C8AA: A7 35          STA     -11,Y           
C8AC: BD C5 25       JSR     $C525                          ; 
C8AF: 0F 2C          CLR     <$2C            
C8B1: 0F 2E          CLR     <$2E            
C8B3: 20 0D          BRA     $C8C2                          ; 
C8B5: 6F 35          CLR     -11,Y           
C8B7: 20 3E          BRA     $C8F7                          ; 
C8B9: BD CA 9B       JSR     $CA9B                          ; 
C8BC: 96 4D          LDA     <$4D            
C8BE: 43             COMA                    
C8BF: 94 34          ANDA    <$34            
C8C1: 39             RTS                     
C8C2: 96 2C          LDA     <$2C            
C8C4: 26 31          BNE     $C8F7                          ; 
C8C6: EC A4          LDD     ,Y              
C8C8: 2A 2D          BPL     $C8F7                          ; 
C8CA: BD C4 E7       JSR     $C4E7                          ; 
C8CD: 30 89 00 E0    LEAX    $00E0,X         
C8D1: CE C5 1D       LDU     #$C51D          
C8D4: EC C6          LDD     A,U             
C8D6: A4 89 18 00    ANDA    $1800,X         
C8DA: E4 89 18 01    ANDB    $1801,X         
C8DE: 10 93 1B       CMPD    <$1B            
C8E1: 27 0C          BEQ     $C8EF                          ; 
C8E3: 34 04          PSHS    B               
C8E5: 8D D2          BSR     $C8B9                          ; 
C8E7: 35 02          PULS    A               
C8E9: 26 0C          BNE     $C8F7                          ; 
C8EB: 8D CC          BSR     $C8B9                          ; 
C8ED: 26 08          BNE     $C8F7                          ; 
C8EF: 86 04          LDA     #$04            
C8F1: A7 38          STA     -8,Y            
C8F3: DC 1B          LDD     <$1B            
C8F5: ED A4          STD     ,Y              
C8F7: EC 24          LDD     4,Y             
C8F9: E3 A4          ADDD    ,Y              
C8FB: ED 24          STD     4,Y             
C8FD: EC 26          LDD     6,Y             
C8FF: E3 22          ADDD    2,Y             
C901: ED 26          STD     6,Y             
C903: A6 35          LDA     -11,Y           
C905: 27 12          BEQ     $C919                          ; 
C907: 96 23          LDA     <$23            
C909: A1 24          CMPA    4,Y             
C90B: 27 0C          BEQ     $C919                          ; 
C90D: A6 36          LDA     -10,Y           
C90F: 84 07          ANDA    #$07            
C911: 48             LSLA                    
C912: 48             LSLA                    
C913: 48             LSLA                    
C914: 8A 1A          ORA     #$1A            
C916: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} Sound
C919: A6 24          LDA     4,Y             
C91B: 97 23          STA     <$23            
C91D: A6 35          LDA     -11,Y           
C91F: 26 59          BNE     $C97A                          ; 
C921: 8E C5 09       LDX     #$C509          
C924: E6 26          LDB     6,Y             
C926: C4 03          ANDB    #$03            
C928: 1F 98          TFR     B,A             
C92A: E6 85          LDB     B,X             
C92C: 34 06          PSHS    B,A             
C92E: BD D8 52       JSR     $D852                          ; 
C931: ED 28          STD     8,Y             
C933: 1F 01          TFR     D,X             
C935: 35 06          PULS    A,B             
C937: 30 89 01 E0    LEAX    $01E0,X         
C93B: 3A             ABX                     
C93C: 48             LSLA                    
C93D: CE C5 0D       LDU     #$C50D          
C940: EC C6          LDD     A,U             
C942: A4 89 18 00    ANDA    $1800,X         
C946: E4 89 18 01    ANDB    $1801,X         
C94A: 10 93 1B       CMPD    <$1B            
C94D: 27 30          BEQ     $C97F                          ; 
C94F: 34 04          PSHS    B               
C951: BD CA 9B       JSR     $CA9B                          ; 
C954: 35 02          PULS    A               
C956: 26 05          BNE     $C95D                          ; 
C958: BD CA 9B       JSR     $CA9B                          ; 
C95B: 27 22          BEQ     $C97F                          ; 
C95D: EC 26          LDD     6,Y             
C95F: A3 22          SUBD    2,Y             
C961: ED 26          STD     6,Y             
C963: 96 2C          LDA     <$2C            
C965: 26 04          BNE     $C96B                          ; 
C967: 6F 38          CLR     -8,Y            
C969: 20 0F          BRA     $C97A                          ; 
C96B: 86 01          LDA     #$01            
C96D: 97 2C          STA     <$2C            
C96F: EC 22          LDD     2,Y             
C971: 43             COMA                    
C972: 53             COMB                    
C973: C3 00 01       ADDD    #$0001          
C976: ED 22          STD     2,Y             
C978: 63 3C          COM     -4,Y            
C97A: BD D8 52       JSR     $D852                          ; 
C97D: ED 28          STD     8,Y             
C97F: CE 34 00       LDU     #$3400          
C982: A6 38          LDA     -8,Y            
C984: 81 03          CMPA    #$03            
C986: 22 08          BHI     $C990                          ; 
C988: A6 3C          LDA     -4,Y            
C98A: 26 04          BNE     $C990                          ; 
C98C: 33 C9 04 80    LEAU    $0480,U         
C990: A6 38          LDA     -8,Y            
C992: C6 C0          LDB     #$C0            
C994: 3D             MUL                     
C995: 33 CB          LEAU    D,U             
C997: DF 37          STU     <$37            
C999: A6 26          LDA     6,Y             
C99B: 84 03          ANDA    #$03            
C99D: C6 30          LDB     #$30            
C99F: 3D             MUL                     
C9A0: 33 CB          LEAU    D,U             
C9A2: EF 2A          STU     10,Y            
C9A4: 11 A3 2E       CMPU    14,Y            
C9A7: 26 10          BNE     $C9B9                          ; 
C9A9: A6 3E          LDA     -2,Y            
C9AB: 2B 0C          BMI     $C9B9                          ; 
C9AD: EE 28          LDU     8,Y             
C9AF: 11 A3 2C       CMPU    12,Y            
C9B2: 10 27 F9 FC    LBEQ    $F9FC           
C9B6: 0C 48          INC     <$48            
C9B8: 39             RTS                     
C9B9: A6 3E          LDA     -2,Y            
C9BB: 10 2E 00 D9    LBGT    $00D9           
C9BF: E6 3C          LDB     -4,Y            
C9C1: 34 20          PSHS    Y               
C9C3: 10 8E 01 E9    LDY     #$01E9          
C9C7: A7 3E          STA     -2,Y            
C9C9: E7 3C          STB     -4,Y            
C9CB: DE 37          LDU     <$37            
C9CD: EF A4          STU     ,Y              
C9CF: EE 22          LDU     2,Y             
C9D1: EF 24          STU     4,Y             
C9D3: BD C5 C8       JSR     $C5C8                          ; 
C9D6: A6 84          LDA     ,X              
C9D8: E6 3E          LDB     -2,Y            
C9DA: 2A 01          BPL     $C9DD                          ; 
C9DC: 4C             INCA                    
C9DD: A7 3D          STA     -3,Y            
C9DF: 20 02          BRA     $C9E3                          ; 
C9E1: 6A 3D          DEC     -3,Y            
C9E3: 10 27 00 AF    LBEQ    $00AF           
C9E7: AE 24          LDX     4,Y             
C9E9: EE A4          LDU     ,Y              
C9EB: A6 3F          LDA     -1,Y            
C9ED: 97 26          STA     <$26            
C9EF: A6 3E          LDA     -2,Y            
C9F1: 10 2A 00 87    LBPL    $0087           
C9F5: A6 3D          LDA     -3,Y            
C9F7: 81 01          CMPA    #$01            
C9F9: 10 26 00 7F    LBNE    $007F           
C9FD: CE 34 00       LDU     #$3400          
CA00: A6 3C          LDA     -4,Y            
CA02: 26 04          BNE     $CA08                          ; 
CA04: 33 C9 04 80    LEAU    $0480,U         
CA08: DF 45          STU     <$45            
CA0A: BD DC 39       JSR     $DC39                          ; 
CA0D: 1F 52          TFR     PC,Y            
CA0F: 31 A5          LEAY    B,Y             
CA11: EC C4          LDD     ,U              
CA13: 48             LSLA                    
CA14: 58             LSLB                    
CA15: AA C0          ORA     ,U+             
CA17: EA C0          ORB     ,U+             
CA19: A4 A0          ANDA    ,Y+             
CA1B: E4 A0          ANDB    ,Y+             
CA1D: ED 84          STD     ,X              
CA1F: A6 C4          LDA     ,U              
CA21: 48             LSLA                    
CA22: AA C0          ORA     ,U+             
CA24: A4 A0          ANDA    ,Y+             
CA26: A7 02          STA     2,X             
CA28: 30 88 20       LEAX    $20,X           
CA2B: 0A 26          DEC     <$26            
CA2D: 26 E2          BNE     $CA11                          ; 
CA2F: 10 8E 01 AA    LDY     #$01AA          
CA33: AE 28          LDX     8,Y             
CA35: AF 2C          STX     12,Y            
CA37: A6 3F          LDA     -1,Y            
CA39: 97 26          STA     <$26            
CA3B: DE 45          LDU     <$45            
CA3D: A6 26          LDA     6,Y             
CA3F: 84 03          ANDA    #$03            
CA41: C6 30          LDB     #$30            
CA43: 3D             MUL                     
CA44: 33 CB          LEAU    D,U             
CA46: 6F 2E          CLR     14,Y            
CA48: BD DC 39       JSR     $DC39                          ; 
CA4B: 1F 52          TFR     PC,Y            
CA4D: 31 A5          LEAY    B,Y             
CA4F: EC C4          LDD     ,U              
CA51: 48             LSLA                    
CA52: 58             LSLB                    
CA53: AA C0          ORA     ,U+             
CA55: EA C0          ORB     ,U+             
CA57: A4 A0          ANDA    ,Y+             
CA59: AA 89 18 00    ORA     $1800,X         
CA5D: E4 A0          ANDB    ,Y+             
CA5F: EA 89 18 01    ORB     $1801,X         
CA63: ED 84          STD     ,X              
CA65: A6 C4          LDA     ,U              
CA67: 48             LSLA                    
CA68: AA C0          ORA     ,U+             
CA6A: A4 A0          ANDA    ,Y+             
CA6C: AA 89 18 02    ORA     $1802,X         
CA70: A7 02          STA     2,X             
CA72: 30 88 20       LEAX    $20,X           
CA75: 0A 26          DEC     <$26            
CA77: 26 D6          BNE     $CA4F                          ; 
CA79: 35 20          PULS    Y               
CA7B: 39             RTS                     
CA7C: 37 06          PULU    A,B             
CA7E: ED 84          STD     ,X              
CA80: 37 02          PULU    A               
CA82: A7 02          STA     2,X             
CA84: 30 88 20       LEAX    $20,X           
CA87: 0A 26          DEC     <$26            
CA89: 26 F1          BNE     $CA7C                          ; 
CA8B: AE 24          LDX     4,Y             
CA8D: A6 3B          LDA     -5,Y            
CA8F: 30 86          LEAX    A,X             
CA91: AF 24          STX     4,Y             
CA93: 7E C9 E1       JMP     $C9E1                          ; 
CA96: 35 20          PULS    Y               
CA98: 0C 48          INC     <$48            
CA9A: 39             RTS                     
CA9B: 97 34          STA     <$34            
CA9D: 84 55          ANDA    #$55            
CA9F: 48             LSLA                    
CAA0: 97 35          STA     <$35            
CAA2: 96 34          LDA     <$34            
CAA4: 84 AA          ANDA    #$AA            
CAA6: 44             LSRA                    
CAA7: 9A 35          ORA     <$35            
CAA9: 98 34          EORA    <$34            
CAAB: 97 4D          STA     <$4D            
CAAD: 94 34          ANDA    <$34            
CAAF: 84 55          ANDA    #$55            
CAB1: 39             RTS                     
CAB2: 7E CE 75       JMP     $CE75                          ; 
CAB5: 39             RTS                     
CAB6: 10 8E 01 BF    LDY     #$01BF          
CABA: A6 3B          LDA     -5,Y            
CABC: 27 F4          BEQ     $CAB2                          ; 
CABE: 96 32          LDA     <$32            
CAC0: 2E 70          BGT     $CB32                          ; 
CAC2: 2B 5F          BMI     $CB23                          ; 
CAC4: 8E C5 09       LDX     #$C509          
CAC7: E6 26          LDB     6,Y             
CAC9: C4 03          ANDB    #$03            
CACB: 1F 98          TFR     B,A             
CACD: E6 85          LDB     B,X             
CACF: AE 28          LDX     8,Y             
CAD1: 30 89 01 00    LEAX    $0100,X         
CAD5: 3A             ABX                     
CAD6: 48             LSLA                    
CAD7: CE CB 10       LDU     #$CB10          
CADA: EC C6          LDD     A,U             
CADC: A4 89 18 00    ANDA    $1800,X         
CAE0: E4 89 18 01    ANDB    $1801,X         
CAE4: 10 93 1B       CMPD    <$1B            
CAE7: 27 0C          BEQ     $CAF5                          ; 
CAE9: 34 04          PSHS    B               
CAEB: 8D AE          BSR     $CA9B                          ; 
CAED: 35 02          PULS    A               
CAEF: 26 27          BNE     $CB18                          ; 
CAF1: 8D A8          BSR     $CA9B                          ; 
CAF3: 26 23          BNE     $CB18                          ; 
CAF5: EC A4          LDD     ,Y              
CAF7: C3 00 12       ADDD    #$0012          
CAFA: 10 83 01 00    CMPD    #$0100          
CAFE: 23 03          BLS     $CB03                          ; 
CB00: CC 01 00       LDD     #$0100          
CB03: ED A4          STD     ,Y              
CB05: A6 3E          LDA     -2,Y            
CB07: 81 0A          CMPA    #$0A            
CB09: 24 03          BCC     $CB0E                          ; 
CB0B: 4C             INCA                    
CB0C: A7 3E          STA     -2,Y            
CB0E: 20 31          BRA     $CB41                          ; 
CB10: 03 00          COM     <$00            
CB12: 00 C0          NEG     <$C0            
CB14: 00 30          NEG     <$30            
CB16: 0C 00          INC     <$00            
CB18: CC FF 00       LDD     #$FF00          
CB1B: ED A4          STD     ,Y              
CB1D: 86 FB          LDA     #$FB            
CB1F: 97 32          STA     <$32            
CB21: 20 6A          BRA     $CB8D                          ; 
CB23: 0C 32          INC     <$32            
CB25: 2B 66          BMI     $CB8D                          ; 
CB27: CC FF 00       LDD     #$FF00          
CB2A: ED A4          STD     ,Y              
CB2C: 86 0A          LDA     #$0A            
CB2E: 97 32          STA     <$32            
CB30: 20 0F          BRA     $CB41                          ; 
CB32: EC A4          LDD     ,Y              
CB34: C3 00 0A       ADDD    #$000A          
CB37: ED A4          STD     ,Y              
CB39: 0A 32          DEC     <$32            
CB3B: 26 04          BNE     $CB41                          ; 
CB3D: DC 1B          LDD     <$1B            
CB3F: ED A4          STD     ,Y              
CB41: EC 24          LDD     4,Y             
CB43: E3 A4          ADDD    ,Y              
CB45: ED 24          STD     4,Y             
CB47: EC 26          LDD     6,Y             
CB49: E3 22          ADDD    2,Y             
CB4B: ED 26          STD     6,Y             
CB4D: 8E C5 09       LDX     #$C509          
CB50: E6 26          LDB     6,Y             
CB52: C4 03          ANDB    #$03            
CB54: 1F 98          TFR     B,A             
CB56: E6 85          LDB     B,X             
CB58: 34 06          PSHS    B,A             
CB5A: BD D8 52       JSR     $D852                          ; 
CB5D: ED 28          STD     8,Y             
CB5F: 1F 01          TFR     D,X             
CB61: 35 06          PULS    A,B             
CB63: 30 89 00 A0    LEAX    $00A0,X         
CB67: 3A             ABX                     
CB68: 48             LSLA                    
CB69: CE C5 15       LDU     #$C515          
CB6C: EC C6          LDD     A,U             
CB6E: A4 89 18 00    ANDA    $1800,X         
CB72: E4 89 18 01    ANDB    $1801,X         
CB76: 10 93 1B       CMPD    <$1B            
CB79: 27 12          BEQ     $CB8D                          ; 
CB7B: 34 04          PSHS    B               
CB7D: BD CA 9B       JSR     $CA9B                          ; 
CB80: 35 02          PULS    A               
CB82: 26 05          BNE     $CB89                          ; 
CB84: BD CA 9B       JSR     $CA9B                          ; 
CB87: 27 04          BEQ     $CB8D                          ; 
CB89: 86 FF          LDA     #$FF            
CB8B: A7 3B          STA     -5,Y            
CB8D: CE 3D D8       LDU     #$3DD8          
CB90: 96 32          LDA     <$32            
CB92: 2A 03          BPL     $CB97                          ; 
CB94: 33 C8 60       LEAU    $60,U           
CB97: A6 26          LDA     6,Y             
CB99: 84 03          ANDA    #$03            
CB9B: C6 18          LDB     #$18            
CB9D: 3D             MUL                     
CB9E: 33 CB          LEAU    D,U             
CBA0: EF 2A          STU     10,Y            
CBA2: 0C 49          INC     <$49            
CBA4: 39             RTS                     
CBA5: 8D 12          BSR     $CBB9                          ; 
CBA7: C6 14          LDB     #$14            
CBA9: D7 26          STB     <$26            
CBAB: CC 10 00       LDD     #$1000          
CBAE: ED 81          STD     ,X++            
CBB0: 0A 26          DEC     <$26            
CBB2: 26 FA          BNE     $CBAE                          ; 
CBB4: 39             RTS                     
CBB5: 3E             RESET                   
CBB6: 98 3E          EORA    <$3E            
CBB8: AC                                  
CBB9: 8E CB B5       LDX     #$CBB5          
CBBC: 96 52          LDA     <$52            
CBBE: 84 02          ANDA    #$02            
CBC0: AE 86          LDX     A,X             
CBC2: 39             RTS                     
CBC3: D6 39          LDB     <$39            
CBC5: 58             LSLB                    
CBC6: 8D F1          BSR     $CBB9                          ; 
CBC8: EC 85          LDD     B,X             
CBCA: 8E 1B 14       LDX     #$1B14          
CBCD: BD DB 36       JSR     $DB36                          ; 
CBD0: 8D E7          BSR     $CBB9                          ; 
CBD2: 0F 26          CLR     <$26            
CBD4: D6 26          LDB     <$26            
CBD6: C1 0A          CMPB    #$0A            
CBD8: 27 1A          BEQ     $CBF4                          ; 
CBDA: D1 39          CMPB    <$39            
CBDC: 27 10          BEQ     $CBEE                          ; 
CBDE: EC 84          LDD     ,X              
CBE0: C3 00 01       ADDD    #$0001          
CBE3: 10 83 10 00    CMPD    #$1000          
CBE7: 23 03          BLS     $CBEC                          ; 
CBE9: CC 10 00       LDD     #$1000          
CBEC: ED 84          STD     ,X              
CBEE: 30 02          LEAX    2,X             
CBF0: 0C 26          INC     <$26            
CBF2: 20 E0          BRA     $CBD4                          ; 
CBF4: 10 8E 01 D4    LDY     #$01D4          
CBF8: A6 3B          LDA     -5,Y            
CBFA: 26 39          BNE     $CC35                          ; 
CBFC: B6 01 A8       LDA     $01A8           
CBFF: 2B 11          BMI     $CC12                          ; 
CC01: 8D B6          BSR     $CBB9                          ; 
CC03: D6 39          LDB     <$39            
CC05: 58             LSLB                    
CC06: 3A             ABX                     
CC07: EC 84          LDD     ,X              
CC09: 27 0A          BEQ     $CC15                          ; 
CC0B: 83 00 01       SUBD    #$0001          
CC0E: 27 03          BEQ     $CC13                          ; 
CC10: ED 84          STD     ,X              
CC12: 39             RTS                     
CC13: ED 84          STD     ,X              
CC15: CC 1A 23       LDD     #$1A23          
CC18: A7 24          STA     4,Y             
CC1A: E7 26          STB     6,Y             
CC1C: BD D8 52       JSR     $D852                          ; 
CC1F: ED 28          STD     8,Y             
CC21: 86 01          LDA     #$01            
CC23: A7 3B          STA     -5,Y            
CC25: 86 06          LDA     #$06            
CC27: A7 3F          STA     -1,Y            
CC29: 86 01          LDA     #$01            
CC2B: BD DC 39       JSR     $DC39                          ; 
CC2E: ED A4          STD     ,Y              
CC30: BD DC 39       JSR     $DC39                          ; 
CC33: ED 22          STD     2,Y             
CC35: 6C 3D          INC     -3,Y            
CC37: A6 3D          LDA     -3,Y            
CC39: 44             LSRA                    
CC3A: 44             LSRA                    
CC3B: 44             LSRA                    
CC3C: 84 01          ANDA    #$01            
CC3E: A7 3E          STA     -2,Y            
CC40: EC 24          LDD     4,Y             
CC42: E3 A4          ADDD    ,Y              
CC44: 81 10          CMPA    #$10            
CC46: 23 0A          BLS     $CC52                          ; 
CC48: 81 B1          CMPA    #$B1            
CC4A: 25 15          BCS     $CC61                          ; 
CC4C: EC A4          LDD     ,Y              
CC4E: 2B 0D          BMI     $CC5D                          ; 
CC50: 20 04          BRA     $CC56                          ; 
CC52: EC A4          LDD     ,Y              
CC54: 2A 07          BPL     $CC5D                          ; 
CC56: 43             COMA                    
CC57: 53             COMB                    
CC58: C3 00 01       ADDD    #$0001          
CC5B: ED A4          STD     ,Y              
CC5D: EC 24          LDD     4,Y             
CC5F: E3 A4          ADDD    ,Y              
CC61: ED 24          STD     4,Y             
CC63: EC 26          LDD     6,Y             
CC65: E3 22          ADDD    2,Y             
CC67: 81 07          CMPA    #$07            
CC69: 23 0A          BLS     $CC75                          ; 
CC6B: 81 73          CMPA    #$73            
CC6D: 25 15          BCS     $CC84                          ; 
CC6F: EC 22          LDD     2,Y             
CC71: 2B 0D          BMI     $CC80                          ; 
CC73: 20 04          BRA     $CC79                          ; 
CC75: EC 22          LDD     2,Y             
CC77: 2A 07          BPL     $CC80                          ; 
CC79: 43             COMA                    
CC7A: 53             COMB                    
CC7B: C3 00 01       ADDD    #$0001          
CC7E: ED 22          STD     2,Y             
CC80: EC 26          LDD     6,Y             
CC82: E3 22          ADDD    2,Y             
CC84: ED 26          STD     6,Y             
CC86: BD D8 52       JSR     $D852                          ; 
CC89: ED 28          STD     8,Y             
CC8B: CE 3E E2       LDU     #$3EE2          
CC8E: A6 3E          LDA     -2,Y            
CC90: 27 03          BEQ     $CC95                          ; 
CC92: 33 C8 48       LEAU    $48,U           
CC95: A6 26          LDA     6,Y             
CC97: 84 03          ANDA    #$03            
CC99: C6 12          LDB     #$12            
CC9B: 3D             MUL                     
CC9C: 33 CB          LEAU    D,U             
CC9E: EF 2A          STU     10,Y            
CCA0: 7E D8 60       JMP     $D860                          ; 
CCA3: 10 8E 01 AA    LDY     #$01AA          
CCA7: 9E 3B          LDX     <$3B            
CCA9: 96 39          LDA     <$39            
CCAB: 48             LSLA                    
CCAC: AE 86          LDX     A,X             
CCAE: 30 02          LEAX    2,X             
CCB0: 39             RTS                     
CCB1: BD CF 1D       JSR     $CF1D                          ; 
CCB4: 8D ED          BSR     $CCA3                          ; 
CCB6: A6 84          LDA     ,X              
CCB8: 27 F6          BEQ     $CCB0                          ; 
CCBA: E6 01          LDB     1,X             
CCBC: A1 24          CMPA    4,Y             
CCBE: 10 26 00 B8    LBNE    $00B8           
CCC2: E1 26          CMPB    6,Y             
CCC4: 10 26 00 B2    LBNE    $00B2           
CCC8: CE 3E C0       LDU     #$3EC0          
CCCB: A6 05          LDA     5,X             
CCCD: A6 C6          LDA     A,U             
CCCF: 94 52          ANDA    <$52            
CCD1: 27 DD          BEQ     $CCB0                          ; 
CCD3: A6 05          LDA     5,X             
CCD5: 81 21          CMPA    #$21            
CCD7: 26 12          BNE     $CCEB                          ; 
CCD9: 34 30          PSHS    Y,X             
CCDB: 0C 3A          INC     <$3A            
CCDD: BD D1 4C       JSR     $D14C                          ; 
CCE0: BD CE CF       JSR     $CECF                          ; 
CCE3: CC 27 10       LDD     #$2710          
CCE6: BD DB 0C       JSR     $DB0C                          ; 
CCE9: 35 30          PULS    X,Y             
CCEB: EC 02          LDD     2,X             
CCED: A7 24          STA     4,Y             
CCEF: E7 26          STB     6,Y             
CCF1: A6 04          LDA     4,X             
CCF3: 97 39          STA     <$39            
CCF5: 86 01          LDA     #$01            
CCF7: A7 3B          STA     -5,Y            
CCF9: BD C5 25       JSR     $C525                          ; 
CCFC: BD D1 1A       JSR     $D11A                          ; 
CCFF: 7F 01 BA       CLR     $01BA           
CD02: 0F 32          CLR     <$32            
CD04: 7F 01 CF       CLR     $01CF           
CD07: 9E 3B          LDX     <$3B            
CD09: 96 39          LDA     <$39            
CD0B: 48             LSLA                    
CD0C: EE 96          LDU     [A,X]           
CD0E: 8E 1C 00       LDX     #$1C00          
CD11: 9F 4E          STX     <$4E            
CD13: 17 00 F5       LBSR    $00F5           
CD16: BD D2 4E       JSR     $D24E                          ; 
CD19: 8D 8C          BSR     $CCA7                          ; 
CD1B: 10 8E 3E C0    LDY     #$3EC0          
CD1F: A6 05          LDA     5,X             
CD21: A6 A6          LDA     A,Y             
CD23: 94 52          ANDA    <$52            
CD25: 27 02          BEQ     $CD29                          ; 
CD27: 8D 58          BSR     $CD81                          ; 
CD29: 30 88 06       LEAX    $06,X           
CD2C: A6 84          LDA     ,X              
CD2E: 26 EF          BNE     $CD1F                          ; 
CD30: 8E 04 00       LDX     #$0400          
CD33: 9F 4E          STX     <$4E            
CD35: 17 00 E5       LBSR    $00E5           
CD38: BE 01 EB       LDX     $01EB           
CD3B: 30 1C          LEAX    -4,X            
CD3D: DE 53          LDU     <$53            
CD3F: BD D8 E2       JSR     $D8E2                          ; 
CD42: 96 39          LDA     <$39            
CD44: 27 17          BEQ     $CD5D                          ; 
CD46: 8E 03 6B       LDX     #$036B          
CD49: 96 39          LDA     <$39            
CD4B: 30 86          LEAX    A,X             
CD4D: A6 84          LDA     ,X              
CD4F: 94 52          ANDA    <$52            
CD51: 26 0A          BNE     $CD5D                          ; 
CD53: A6 84          LDA     ,X              
CD55: 9A 52          ORA     <$52            
CD57: A7 84          STA     ,X              
CD59: CC 03 E8       LDD     #$03E8          
CD5C: 8C DC 1B       CMPX    #$DC1B          
CD5F: BD DB 0C       JSR     $DB0C                          ; 
CD62: 8E 04 55       LDX     #$0455          
CD65: CE DB 04       LDU     #$DB04          
CD68: BD D8 E2       JSR     $D8E2                          ; 
CD6B: CE 00 D0       LDU     #$00D0          
CD6E: 86 24          LDA     #$24            
CD70: D6 39          LDB     <$39            
CD72: ED C4          STD     ,U              
CD74: BD D8 E2       JSR     $D8E2                          ; 
CD77: 7E CF 0F       JMP     $CF0F                          ; 
CD7A: 30 88 06       LEAX    $06,X           
CD7D: 7E CC B6       JMP     $CCB6                          ; 
CD80: 39             RTS                     
CD81: 34 50          PSHS    U,X             
CD83: EC 84          LDD     ,X              
CD85: 81 FF          CMPA    #$FF            
CD87: 27 3E          BEQ     $CDC7                          ; 
CD89: C1 40          CMPB    #$40            
CD8B: 25 03          BCS     $CD90                          ; 
CD8D: CB 07          ADDB    #$07            
CD8F: 8C C0 04       CMPX    #$C004          
CD92: 34 04          PSHS    B               
CD94: BD D8 56       JSR     $D856                          ; 
CD97: 1F 03          TFR     D,U             
CD99: 35 02          PULS    A               
CD9B: 84 03          ANDA    #$03            
CD9D: 97 26          STA     <$26            
CD9F: 34 40          PSHS    U               
CDA1: CE 00 83       LDU     #$0083          
CDA4: 8E DF 0A       LDX     #$DF0A          
CDA7: 86 10          LDA     #$10            
CDA9: 97 4D          STA     <$4D            
CDAB: EC 81          LDD     ,X++            
CDAD: ED C1          STD     ,U++            
CDAF: 6F C0          CLR     ,U+             
CDB1: 0A 4D          DEC     <$4D            
CDB3: 26 F6          BNE     $CDAB                          ; 
CDB5: 96 26          LDA     <$26            
CDB7: 27 29          BEQ     $CDE2                          ; 
CDB9: C6 10          LDB     #$10            
CDBB: 8D 0C          BSR     $CDC9                          ; 
CDBD: 35 40          PULS    U               
CDBF: 8E 00 83       LDX     #$0083          
CDC2: 86 10          LDA     #$10            
CDC4: BD D8 9B       JSR     $D89B                          ; 
CDC7: 35 D0          PULS    X,U,PC          
CDC9: 8E 00 83       LDX     #$0083          
CDCC: 96 26          LDA     <$26            
CDCE: 64 84          LSR     ,X              
CDD0: 66 01          ROR     1,X             
CDD2: 66 02          ROR     2,X             
CDD4: 64 84          LSR     ,X              
CDD6: 66 01          ROR     1,X             
CDD8: 66 02          ROR     2,X             
CDDA: 4A             DECA                    
CDDB: 26 F1          BNE     $CDCE                          ; 
CDDD: 30 03          LEAX    3,X             
CDDF: 5A             DECB                    
CDE0: 26 EA          BNE     $CDCC                          ; 
CDE2: 39             RTS                     

SetVDGMode:
CDE3: B6 FF 22       LDA     $FF22                          ; {hard:PIA1_DB} Current VDG settings
CDE6: 84 07          ANDA    #$07                           ; Clear out the top 5 bits (the VDG settings)
CDE8: 9A 6A          ORA     <$6A                           ; Set the desired ...
CDEA: B7 FF 22       STA     $FF22                          ; {hard:PIA1_DB} ... mode
CDED: B7 FF C0       STA     $FFC0                          ; {hard:dispMode} 
CDF0: B7 FF C3       STA     $FFC3                          ; {hard:dispMode} 
CDF3: B7 FF C5       STA     $FFC5                          ; {hard:dispMode} 
CDF6: 39             RTS                     

SetDispMem:
CDF7: 8E FF C6       LDX     #$FFC6                         ; Start of offset registers
CDFA: 44             LSRA                                   ; Only 7 bits -- discard the lowest
CDFB: C6 07          LDB     #$07                           ; 7 bits to set
CDFD: 44             LSRA                                   ; Test the bit
CDFE: 25 03          BCS     $CE03                          ; Bit is a one ... write to the SET register
CE00: A7 84          STA     ,X                             ; Write to the CLEAR register for the bit
CE02: 8C A7 01       CMPX    #$A701                         ; STA 1,X
CE05: 30 02          LEAX    2,X                            ; Next register pair in SAM
CE07: 5A             DECB                                   ; All done?
CE08: 26 F3          BNE     $CDFD                          ; No ... set all the bits
CE0A: 39             RTS                                    ; Done

CE0B: 8E 1C 00       LDX     #$1C00          
CE0E: 20 03          BRA     $CE13                          ; 
CE10: 8E 04 00       LDX     #$0400          
CE13: DC 1B          LDD     <$1B            
CE15: ED 81          STD     ,X++            
CE17: 8C 34 00       CMPX    #$3400          
CE1A: 26 F9          BNE     $CE15                          ; 
CE1C: 39             RTS                     
CE1D: 6F E2          CLR     ,-S             
CE1F: 8E 04 00       LDX     #$0400          
CE22: 1F 10          TFR     X,D             
CE24: C5 1F          BITB    #$1F            
CE26: 26 08          BNE     $CE30                          ; 
CE28: 10 8E 04 00    LDY     #$0400          
CE2C: 31 3F          LEAY    -1,Y            
CE2E: 26 FC          BNE     $CE2C                          ; 
CE30: C6 06          LDB     #$06            
CE32: A6 89 18 00    LDA     $1800,X         
CE36: A7 84          STA     ,X              
CE38: A6 E4          LDA     ,S              
CE3A: 26 05          BNE     $CE41                          ; 
CE3C: 86 55          LDA     #$55            
CE3E: A7 88 20       STA     $20,X           
CE41: 30 89 04 00    LEAX    $0400,X         
CE45: 34 04          PSHS    B               
CE47: 1F 10          TFR     X,D             
CE49: 8A 02          ORA     #$02            
CE4B: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
CE4E: 35 04          PULS    B               
CE50: 5A             DECB                    
CE51: 26 DF          BNE     $CE32                          ; 
CE53: 30 89 E8 01    LEAX    $E801,X         
CE57: 8C 07 E0       CMPX    #$07E0          
CE5A: 25 04          BCS     $CE60                          ; 
CE5C: 86 FF          LDA     #$FF            
CE5E: A7 E4          STA     ,S              
CE60: 8C 08 00       CMPX    #$0800          
CE63: 26 BD          BNE     $CE22                          ; 
CE65: 35 02          PULS    A               
CE67: 39             RTS                     
CE68: 10 8E 01 AA    LDY     #$01AA          
CE6C: 86 02          LDA     #$02            
CE6E: A7 3B          STA     -5,Y            
CE70: 86 10          LDA     #$10            
CE72: A7 3F          STA     -1,Y            
CE74: 39             RTS                     
CE75: 8E CE AC       LDX     #$CEAC          
CE78: A6 80          LDA     ,X+             
CE7A: 2B 2F          BMI     $CEAB                          ; 
CE7C: 91 39          CMPA    <$39            
CE7E: 26 F8          BNE     $CE78                          ; 
CE80: 10 8E 01 BF    LDY     #$01BF          
CE84: 8E 01 BA       LDX     #$01BA          
CE87: 6F 80          CLR     ,X+             
CE89: 8C 01 CF       CMPX    #$01CF          
CE8C: 26 F9          BNE     $CE87                          ; 
CE8E: 86 01          LDA     #$01            
CE90: A7 3B          STA     -5,Y            
CE92: 86 08          LDA     #$08            
CE94: A7 3F          STA     -1,Y            
CE96: CC FF A8       LDD     #$FFA8          
CE99: ED 22          STD     2,Y             
CE9B: DC 1B          LDD     <$1B            
CE9D: ED A4          STD     ,Y              
CE9F: CC 74 65       LDD     #$7465          
CEA2: A7 24          STA     4,Y             
CEA4: E7 26          STB     6,Y             
CEA6: BD D8 52       JSR     $D852                          ; 
CEA9: ED 28          STD     8,Y             
CEAB: 39             RTS                     
CEAC: 00 02          NEG     <$02            
CEAE: 05                                  
CEAF: 06 0A          ROR     <$0A            
CEB1: 0B                                  
CEB2: 0C 0D          INC     <$0D            
CEB4: 0E FF          JMP     <$FF            
CEB6: BD CE 10       JSR     $CE10                          ; 
CEB9: BD CD E3       JSR     $CDE3                          ; {SetVDGMode} Set the graphics mode
CEBC: 8E D2 5A       LDX     #$D25A          
CEBF: 9F 3B          STX     <$3B            
CEC1: 0F 39          CLR     <$39            
CEC3: 39             RTS                     

CEC4: 80 0C          SUBA    #$0C            
CEC6: 04 81          LSR     <$81            
CEC8: 0A 89          DEC     <$89            
CECA: 0E 87          JMP     <$87            
CECC: 0A 02          DEC     <$02            
CECE: FF C6 22       STU     $C622                          ; 
CED1: 8E 3E C0       LDX     #$3EC0          
CED4: 6F 80          CLR     ,X+             
CED6: 5A             DECB                    
CED7: 26 FB          BNE     $CED4                          ; 
CED9: 8E 3E C0       LDX     #$3EC0          
CEDC: CE CE EA       LDU     #$CEEA          
CEDF: C6 03          LDB     #$03            
CEE1: A6 C0          LDA     ,U+             
CEE3: 2B 04          BMI     $CEE9                          ; 
CEE5: E7 86          STB     A,X             
CEE7: 20 F8          BRA     $CEE1                          ; 
CEE9: 39             RTS                     
CEEA: 00 02          NEG     <$02            
CEEC: 04 05          LSR     <$05            
CEEE: 07 08          ASR     <$08            
CEF0: 09 0C          ROL     <$0C            
CEF2: 0D 0E          TST     <$0E            
CEF4: 0F 10          CLR     <$10            
CEF6: 11                                  
CEF7: 12             NOP                     
CEF8: 14                                  
CEF9: FF 10 8E       STU     $108E           
CEFC: 01                                  
CEFD: E9 CC 02       ADCB    $02,PC          
CF00: 14                                  
CF01: BD D8 56       JSR     $D856                          ; 
CF04: ED 22          STD     2,Y             
CF06: 86 07          LDA     #$07            
CF08: A7 3F          STA     -1,Y            
CF0A: 86 03          LDA     #$03            
CF0C: A7 3B          STA     -5,Y            
CF0E: 39             RTS                     
CF0F: 10 8E 02 71    LDY     #$0271          
CF13: 96 39          LDA     <$39            
CF15: C6 19          LDB     #$19            
CF17: 3D             MUL                     
CF18: 31 AB          LEAY    D,Y             
CF1A: 10 9F 3D       STY     <$3D            
CF1D: 86 05          LDA     #$05            
CF1F: 97 4D          STA     <$4D            
CF21: 10 9E 3D       LDY     <$3D            
CF24: A6 A4          LDA     ,Y              
CF26: 94 52          ANDA    <$52            
CF28: 27 12          BEQ     $CF3C                          ; 
CF2A: BD D1 42       JSR     $D142                          ; 
CF2D: 58             LSLB                    
CF2E: A6 21          LDA     1,Y             
CF30: 3D             MUL                     
CF31: CE DE B3       LDU     #$DEB3          
CF34: 33 CB          LEAU    D,U             
CF36: C6 0A          LDB     #$0A            
CF38: D7 26          STB     <$26            
CF3A: 8D 07          BSR     $CF43                          ; 
CF3C: 31 25          LEAY    5,Y             
CF3E: 0A 4D          DEC     <$4D            
CF40: 26 E2          BNE     $CF24                          ; 
CF42: 39             RTS                     
CF43: EC C1          LDD     ,U++            
CF45: AA 84          ORA     ,X              
CF47: EA 01          ORB     1,X             
CF49: ED 84          STD     ,X              
CF4B: 30 88 20       LEAX    $20,X           
CF4E: 0A 26          DEC     <$26            
CF50: 26 F1          BNE     $CF43                          ; 
CF52: 39             RTS                     
CF53: 10 8E 01 EF    LDY     #$01EF          
CF57: 96 40          LDA     <$40            
CF59: 27 02          BEQ     $CF5D                          ; 
CF5B: 31 2D          LEAY    13,Y            
CF5D: 03 40          COM     <$40            
CF5F: A6 A4          LDA     ,Y              
CF61: 27 4A          BEQ     $CFAD                          ; 
CF63: 2B 49          BMI     $CFAE                          ; 
CF65: 4A             DECA                    
CF66: 27 5C          BEQ     $CFC4                          ; 
CF68: AE 2A          LDX     10,Y            
CF6A: 30 89 18 C0    LEAX    $18C0,X         
CF6E: A6 84          LDA     ,X              
CF70: A4 2C          ANDA    12,Y            
CF72: BD CA 9B       JSR     $CA9B                          ; 
CF75: 26 4B          BNE     $CFC2                          ; 
CF77: A6 88 20       LDA     $20,X           
CF7A: A4 2C          ANDA    12,Y            
CF7C: BD CA 9B       JSR     $CA9B                          ; 
CF7F: 26 41          BNE     $CFC2                          ; 
CF81: EC 23          LDD     3,Y             
CF83: E3 21          ADDD    1,Y             
CF85: ED 23          STD     3,Y             
CF87: CC 02 00       LDD     #$0200          
CF8A: ED 21          STD     1,Y             
CF8C: A6 23          LDA     3,Y             
CF8E: E6 25          LDB     5,Y             
CF90: BD D8 56       JSR     $D856                          ; 
CF93: ED 28          STD     8,Y             
CF95: 17 00 9D       LBSR    $009D           
CF98: AE 28          LDX     8,Y             
CF9A: AF 2A          STX     10,Y            
CF9C: EE 26          LDU     6,Y             
CF9E: C6 06          LDB     #$06            
CFA0: D7 26          STB     <$26            
CFA2: 8D 9F          BSR     $CF43                          ; 
CFA4: 31 A8 1A       LEAY    $1A,Y           
CFA7: 10 8C 02 71    CMPY    #$0271          
CFAB: 25 B2          BCS     $CF5F                          ; 
CFAD: 39             RTS                     
CFAE: 6A A4          DEC     ,Y              
CFB0: A6 A4          LDA     ,Y              
CFB2: 84 02          ANDA    #$02            
CFB4: 27 05          BEQ     $CFBB                          ; 
CFB6: CC 00 80       LDD     #$0080          
CFB9: 20 03          BRA     $CFBE                          ; 
CFBB: CC FF 80       LDD     #$FF80          
CFBE: ED 21          STD     1,Y             
CFC0: 20 BF          BRA     $CF81                          ; 
CFC2: 8D 71          BSR     $D035                          ; 
CFC4: C6 A8          LDB     #$A8            
CFC6: E7 A4          STB     ,Y              
CFC8: 8E D0 5D       LDX     #$D05D          
CFCB: 96 39          LDA     <$39            
CFCD: 48             LSLA                    
CFCE: AE 86          LDX     A,X             
CFD0: 86 03          LDA     #$03            
CFD2: E6 80          LDB     ,X+             
CFD4: BD DC 1F       JSR     $DC1F                          ; 
CFD7: 3D             MUL                     
CFD8: 3A             ABX                     
CFD9: E6 84          LDB     ,X              
CFDB: BD DC 1F       JSR     $DC1F                          ; 
CFDE: 86 08          LDA     #$08            
CFE0: 3D             MUL                     
CFE1: EB 02          ADDB    2,X             
CFE3: 96 3A          LDA     <$3A            
CFE5: 81 03          CMPA    #$03            
CFE7: 25 02          BCS     $CFEB                          ; 
CFE9: C4 FE          ANDB    #$FE            
CFEB: A6 01          LDA     1,X             
CFED: A7 23          STA     3,Y             
CFEF: E7 25          STB     5,Y             
CFF1: 8B 06          ADDA    #$06            
CFF3: CB 04          ADDB    #$04            
CFF5: BD D8 56       JSR     $D856                          ; 
CFF8: 1F 01          TFR     D,X             
CFFA: A6 89 18 00    LDA     $1800,X         
CFFE: 8E D8 4A       LDX     #$D84A          
D001: E6 25          LDB     5,Y             
D003: C4 03          ANDB    #$03            
D005: A4 85          ANDA    B,X             
D007: BD C8 B9       JSR     $C8B9                          ; 
D00A: 27 02          BEQ     $D00E                          ; 
D00C: 6A 25          DEC     5,Y             
D00E: A6 23          LDA     3,Y             
D010: E6 25          LDB     5,Y             
D012: BD D8 56       JSR     $D856                          ; 
D015: ED 28          STD     8,Y             
D017: ED 2A          STD     10,Y            
D019: CE DF 2A       LDU     #$DF2A          
D01C: A6 25          LDA     5,Y             
D01E: 84 03          ANDA    #$03            
D020: 8E D0 31       LDX     #$D031          
D023: E6 86          LDB     A,X             
D025: E7 2C          STB     12,Y            
D027: C6 0C          LDB     #$0C            
D029: 3D             MUL                     
D02A: 33 CB          LEAU    D,U             
D02C: EF 26          STU     6,Y             
D02E: 16 FF 7D       LBRA    $FF7D           
D031: F0 3C 0F       SUBB    $3C0F           
D034: 03 AE          COM     <$AE            
D036: 2A EE          BPL     $D026                          ; 
D038: 26 86          BNE     $CFC0                          ; 
D03A: 06 97          ROR     <$97            
D03C: 26 A6          BNE     $CFE4                          ; 
D03E: C0 43          SUBB    #$43            
D040: A4 84          ANDA    ,X              
D042: AA 89 18 00    ORA     $1800,X         
D046: A7 84          STA     ,X              
D048: E6 C0          LDB     ,U+             
D04A: 27 09          BEQ     $D055                          ; 
D04C: 53             COMB                    
D04D: E4 01          ANDB    1,X             
D04F: EA 89 18 01    ORB     $1801,X         
D053: E7 01          STB     1,X             
D055: 30 88 20       LEAX    $20,X           
D058: 0A 26          DEC     <$26            
D05A: 26 E1          BNE     $D03D                          ; 
D05C: 39             RTS                     
D05D: D0 73          SUBB    <$73            
D05F: D0 89          SUBB    <$89            
D061: D0 9C          SUBB    <$9C            
D063: D0 AC          SUBB    <$AC            
D065: D0 BF          SUBB    <$BF            
D067: D0 CF          SUBB    <$CF            
D069: D0 DF          SUBB    <$DF            
D06B: D0 E6          SUBB    <$E6            
D06D: D0 FC          SUBB    <$FC            
D06F: D1 0C          CMPB    <$0C            
D071: D1 16          CMPB    <$16            
D073: 06 0C          ROR     <$0C            
D075: 11                                  
D076: 0F 09          CLR     <$09            
D078: 3E             RESET                   
D079: 27 01          BEQ     $D07C                          ; 
D07B: 6B                                  
D07C: 0F 05          CLR     <$05            
D07E: 6B                                  
D07F: 2F 01          BLE     $D082                          ; 
D081: 98 1F          EORA    <$1F            
D083: 01                                  
D084: 98 3F          EORA    <$3F            
D086: 01                                  
D087: 98 5F          EORA    <$5F            
D089: 05                                  
D08A: 05                                  
D08B: 11                                  
D08C: 0F 04          CLR     <$04            
D08E: 11                                  
D08F: 4F             CLRA                    
D090: 05                                  
D091: 3E             RESET                   
D092: 0F 01          CLR     <$01            
D094: 3E             RESET                   
D095: 4F             CLRA                    
D096: 01                                  
D097: 6B                                  
D098: 67 02          ASR     2,X             
D09A: 98 47          EORA    <$47            
D09C: 04 0C          LSR     <$0C            
D09E: 11                                  
D09F: 0F 02          CLR     <$02            
D0A1: 3E             RESET                   
D0A2: 0F 01          CLR     <$01            
D0A4: 3E             RESET                   
D0A5: 37 09          PULU    CC,DP           
D0A7: 6B                                  
D0A8: 27 04          BEQ     $D0AE                          ; 
D0AA: 98 0F          EORA    <$0F            
D0AC: 05                                  
D0AD: 0C 11          INC     <$11            
D0AF: 0F 03          CLR     <$03            
D0B1: 3E             RESET                   
D0B2: 0F 06          CLR     <$06            
D0B4: 3E             RESET                   
D0B5: 3F             SWI                     
D0B6: 03 6B          COM     <$6B            
D0B8: 0F 00          CLR     <$00            
D0BA: 98 0F          EORA    <$0F            
D0BC: 01                                  
D0BD: 98 2F          EORA    <$2F            
D0BF: 04 0C          LSR     <$0C            
D0C1: 11                                  
D0C2: 0F 01          CLR     <$01            
D0C4: 3E             RESET                   
D0C5: 0F 08          CLR     <$08            
D0C7: 4D             TSTA                    
D0C8: 1F 01          TFR     D,X             
D0CA: 98 2F          EORA    <$2F            
D0CC: 01                                  
D0CD: 98 57          EORA    <$57            
D0CF: 04 0C          LSR     <$0C            
D0D1: 11                                  
D0D2: 0F 01          CLR     <$01            
D0D4: 3E             RESET                   
D0D5: 67 0A          ASR     10,X            
D0D7: 6B                                  
D0D8: 1F 01          TFR     D,X             
D0DA: 98 0F          EORA    <$0F            
D0DC: 02                                  
D0DD: 98 47          EORA    <$47            
D0DF: 01                                  
D0E0: 0C 11          INC     <$11            
D0E2: 0F 09          CLR     <$09            
D0E4: 5C             INCB                    
D0E5: 27 06          BEQ     $D0ED                          ; 
D0E7: 05                                  
D0E8: 11                                  
D0E9: 0F 01          CLR     <$01            
D0EB: 20 3F          BRA     $D12C                          ; 
D0ED: 04 11          LSR     <$11            
D0EF: 4F             CLRA                    
D0F0: 00 5C          NEG     <$5C            
D0F2: 27 00          BEQ     $D0F4                          ; 
D0F4: 5C             INCB                    
D0F5: 57             ASRB                    
D0F6: 00 6B          NEG     <$6B            
D0F8: 2F 00          BLE     $D0FA                          ; 
D0FA: 6B                                  
D0FB: 4F             CLRA                    
D0FC: 04 0C          LSR     <$0C            
D0FE: 11                                  
D0FF: 0F 08          CLR     <$08            
D101: 3E             RESET                   
D102: 2F 0A          BLE     $D10E                          ; 
D104: 5C             INCB                    
D105: 0F 0A          CLR     <$0A            
D107: 7A 1F 0A       DEC     $1F0A           
D10A: 98 0F          EORA    <$0F            
D10C: 02                                  
D10D: 0C 11          INC     <$11            
D10F: 0F 03          CLR     <$03            
D111: 3E             RESET                   
D112: 0F 05          CLR     <$05            
D114: 5C             INCB                    
D115: 37 00          PULU    $00             
D117: 0C 11          INC     <$11            
D119: 0E 4F          JMP     <$4F            
D11B: C6 0A          LDB     #$0A            
D11D: 8D 18          BSR     $D137                          ; 
D11F: 96 3A          LDA     <$3A            
D121: 27 04          BEQ     $D127                          ; 
D123: C6 0A          LDB     #$0A            
D125: 20 09          BRA     $D130                          ; 
D127: D6 39          LDB     <$39            
D129: C1 05          CMPB    #$05            
D12B: 24 02          BCC     $D12F                          ; 
D12D: C6 05          LDB     #$05            
D12F: 5C             INCB                    
D130: D7 3F          STB     <$3F            
D132: 86 01          LDA     #$01            
D134: 8D 01          BSR     $D137                          ; 
D136: 39             RTS                     
D137: 8E 01 EF       LDX     #$01EF          
D13A: A7 84          STA     ,X              
D13C: 30 0D          LEAX    13,X            
D13E: 5A             DECB                    
D13F: 26 F9          BNE     $D13A                          ; 
D141: 39             RTS                     
D142: EC 22          LDD     2,Y             
D144: BD D8 56       JSR     $D856                          ; 
D147: 1F 01          TFR     D,X             
D149: C6 0A          LDB     #$0A            
D14B: 39             RTS                     
D14C: 86 FF          LDA     #$FF            
D14E: 8E 02 71       LDX     #$0271          
D151: C6 32          LDB     #$32            
D153: 6F 84          CLR     ,X              
D155: 6F 01          CLR     1,X             
D157: A7 04          STA     4,X             
D159: 30 05          LEAX    5,X             
D15B: 5A             DECB                    
D15C: 26 F5          BNE     $D153                          ; 
D15E: 8E 02 71       LDX     #$0271          
D161: CE D1 C2       LDU     #$D1C2          
D164: 96 3A          LDA     <$3A            
D166: 27 03          BEQ     $D16B                          ; 
D168: CE D1 D6       LDU     #$D1D6          
D16B: C6 0A          LDB     #$0A            
D16D: 86 02          LDA     #$02            
D16F: A7 01          STA     1,X             
D171: A7 06          STA     6,X             
D173: A6 C0          LDA     ,U+             
D175: A7 04          STA     4,X             
D177: A6 C0          LDA     ,U+             
D179: A7 09          STA     9,X             
D17B: 30 88 19       LEAX    $19,X           
D17E: 5A             DECB                    
D17F: 26 EC          BNE     $D16D                          ; 
D181: CE D1 EA       LDU     #$D1EA          
D184: C6 0A          LDB     #$0A            
D186: D7 26          STB     <$26            
D188: 8E 02 71       LDX     #$0271          
D18B: C6 05          LDB     #$05            
D18D: D7 4D          STB     <$4D            
D18F: 34 10          PSHS    X               
D191: D6 4D          LDB     <$4D            
D193: 5A             DECB                    
D194: 86 05          LDA     #$05            
D196: 3D             MUL                     
D197: 30 8B          LEAX    D,X             
D199: 86 03          LDA     #$03            
D19B: A7 84          STA     ,X              
D19D: D6 4D          LDB     <$4D            
D19F: 5A             DECB                    
D1A0: 1F 98          TFR     B,A             
D1A2: 48             LSLA                    
D1A3: EC C6          LDD     A,U             
D1A5: ED 02          STD     2,X             
D1A7: E6 01          LDB     1,X             
D1A9: 26 07          BNE     $D1B2                          ; 
D1AB: BD DC 39       JSR     $DC39                          ; 
D1AE: C4 01          ANDB    #$01            
D1B0: E7 01          STB     1,X             
D1B2: 35 10          PULS    X               
D1B4: 0A 4D          DEC     <$4D            
D1B6: 26 D7          BNE     $D18F                          ; 
D1B8: 30 88 19       LEAX    $19,X           
D1BB: 33 4A          LEAU    10,U            
D1BD: 0A 26          DEC     <$26            
D1BF: 26 CA          BNE     $D18B                          ; 
D1C1: 39             RTS                     
D1C2: 01                                  
D1C3: 03 1E          COM     <$1E            
D1C5: 1C 13          ANDCC   #$13            
D1C7: 06 0B          ROR     <$0B            
D1C9: 0A 15          DEC     <$15            
D1CB: 1A 16          ORCC    #$16            
D1CD: 17 18 19       LBSR    $1819           
D1D0: 1B                                  
D1D1: 21 1D          BRN     $D1F0                          ; 
D1D3: FF 1F 20       STU     $1F20           
D1D6: 01                                  
D1D7: 03 1E          COM     <$1E            
D1D9: 1C 06          ANDCC   #$06            
D1DB: 13             SYNC                    
D1DC: 0A 0B          DEC     <$0B            
D1DE: 15                                  
D1DF: 1A 17          ORCC    #$17            
D1E1: 16 19 18       LBRA    $1918           
D1E4: 21 1B          BRN     $D201                          ; 
D1E6: 1D             SEX                     
D1E7: FF 20 1F       STU     $201F           
D1EA: 3A             ABX                     
D1EB: 1C 69          ANDCC   #$69            
D1ED: 5C             INCB                    
D1EE: 65                                  
D1EF: 20 91          BRA     $D182                          ; 
D1F1: 30 91          LEAX    [,X++]          
D1F3: 50             NEGB                    
D1F4: 23 34          BLS     $D22A                          ; 
D1F6: 23 48          BLS     $D240                          ; 
D1F8: 38                                  
D1F9: 64                                  
D1FA: 97 3C          STA     <$3C            
D1FC: 97 5C          STA     <$5C            
D1FE: 3A             ABX                     
D1FF: 60 44          NEG     4,U             
D201: 1C 4D          ANDCC   #$4D            
D203: 34 69          PSHS    U,Y,DP,CC       
D205: 64 78          LSR     -8,S            
D207: 40             NEGA                    
D208: 41                                  
D209: 70 4B 24       NEG     $4B24           
D20C: 6C 50          INC     -16,U           
D20E: 6C 70          INC     -16,S           
D210: 9D 0C          JSR     <$0C            
D212: 3F             SWI                     
D213: 0C 6C          INC     <$6C            
D215: 0C 17          INC     <$17            
D217: 60 96          NEG     [A,X]           
D219: 3C 96          CWAI    $96             
D21B: 64 14          LSR     -12,X           
D21D: 6C 30          INC     -16,Y           
D21F: 04 4B          LSR     <$4B            
D221: 1C 5D          ANDCC   #$5D            
D223: 04 9B          LSR     <$9B            
D225: 50             NEGB                    
D226: 15                                  
D227: 18                                  
D228: 6A 6C          DEC     12,S            
D22A: 2B 40          BMI     $D26C                          ; 
D22C: 5F             CLRB                    
D22D: 18                                  
D22E: 93 34          SUBD    <$34            
D230: 30 0C          LEAX    12,X            
D232: 9B 44          ADDA    <$44            
D234: 2C 3C          BGE     $D272                          ; 
D236: 3D             MUL                     
D237: 6C 9B          INC     [D,X]           
D239: 2C 21          BGE     $D25C                          ; 
D23B: 38                                  
D23C: 34 20          PSHS    Y               
D23E: 40             NEGA                    
D23F: 60 5D          NEG     -3,U            
D241: 1C 7C          ANDCC   #$7C            
D243: 60 13          NEG     -13,X           
D245: 30 3D          LEAX    -3,Y            
D247: 38                                  
D248: 44             LSRA                    
D249: 18                                  
D24A: 96 38          LDA     <$38            
D24C: 96 60          LDA     <$60            
D24E: 86 01          LDA     #$01            
D250: 97 20          STA     <$20            
D252: CC 10 0F       LDD     #$100F          
D255: DD 21          STD     <$21            
D257: 7E D5 9E       JMP     $D59E                          ; 
D25A: D2 6E          SBCB    <$6E            
D25C: D2 7D          SBCB    <$7D            
D25E: D2 98          SBCB    <$98            
D260: D2 BF          SBCB    <$BF            
D262: D2 EC          SBCB    <$EC            
D264: D3 07          ADDD    <$07            
D266: D3 1C          ADDD    <$1C            
D268: D3 2B          ADDD    <$2B            
D26A: D3 3A          ADDD    <$3A            
D26C: D3 49          ADDD    <$49            
D26E: D3 5E          ADDD    <$5E            
D270: FF FF A5       STU     $FFA5           
D273: 70 00 00       NEG     $0000           
D276: 1E 72          EXG     $72             
D278: 87                                  
D279: 07 01          ASR     <$01            
D27B: 01                                  
D27C: 00 D3          NEG     <$D3            
D27E: A0                                  
D27F: 87                                  
D280: 05                                  
D281: 1E 70          EXG     $70             
D283: 00 02          NEG     <$02            
D285: 4B                                  
D286: 72                                  
D287: A5 07          BITA    7,X             
D289: 02                                  
D28A: 03 1E          COM     <$1E            
D28C: 72                                  
D28D: 78 07 02       LSL     $0702           
D290: 04 1E          LSR     <$1E            
D292: 05                                  
D293: 78 70 06       LSL     $7006           
D296: 1A 00          ORCC    #$00            
D298: D3 E4          ADDD    <$E4            
D29A: A5 05          BITA    5,X             
D29C: 4B                                  
D29D: 70 01 05       NEG     $0105           
D2A0: 78 05 1E       LSL     $051E           
D2A3: 70 01 06       NEG     $0106           
D2A6: 78 72 78       LSL     $7278           
D2A9: 07 03          ASR     <$03            
D2AB: 07 4B          ASR     <$4B            
D2AD: 72                                  
D2AE: 4B                                  
D2AF: 07 03          ASR     <$03            
D2B1: 13             SYNC                    
D2B2: 1E 72          EXG     $72             
D2B4: 1E 07          EXG     $07             
D2B6: 03 12          COM     <$12            
D2B8: 1E 05          EXG     $05             
D2BA: 87                                  
D2BB: 70 05 15       NEG     $0515           
D2BE: 00 D4          NEG     <$D4            
D2C0: 26 78          BNE     $D33A                          ; 
D2C2: 05                                  
D2C3: 78 70 02       LSL     $7002           
D2C6: 08 A5          ASL     <$A5            
D2C8: 72                                  
D2C9: A5 07          BITA    7,X             
D2CB: 04 09          LSR     <$09            
D2CD: 78 72 78       LSL     $7278           
D2D0: 07 04          ASR     <$04            
D2D2: 0A 4B          DEC     <$4B            
D2D4: 05                                  
D2D5: 4B                                  
D2D6: 70 02 14       NEG     $0214           
D2D9: 4B                                  
D2DA: 72                                  
D2DB: 4B                                  
D2DC: 07 04          ASR     <$04            
D2DE: 0B                                  
D2DF: 1E 05          EXG     $05             
D2E1: 1E 70          EXG     $70             
D2E3: 02                                  
D2E4: 11                                  
D2E5: 1E 72          EXG     $72             
D2E7: 1E 07          EXG     $07             
D2E9: 04 10          LSR     <$10            
D2EB: 00 D4          NEG     <$D4            
D2ED: 67 A5          ASR     B,Y             
D2EF: 05                                  
D2F0: A5 70          BITA    -16,S           
D2F2: 03 0C          COM     <$0C            
D2F4: 78 05 78       LSL     $0578           
D2F7: 70 03 0D       NEG     $030D           
D2FA: 4B                                  
D2FB: 05                                  
D2FC: 4B                                  
D2FD: 70 03 0E       NEG     $030E           
D300: 1E 05          EXG     $05             
D302: 1E 70          EXG     $70             
D304: 03 0F          COM     <$0F            
D306: 00 D4          NEG     <$D4            
D308: A2                                  
D309: 87                                  
D30A: 72                                  
D30B: 1E 07          EXG     $07             
D30D: 02                                  
D30E: 16 A5 05       LBRA    $A505           
D311: 3C 70          CWAI    $70             
D313: 06 17          ROR     <$17            
D315: 4B                                  
D316: 72                                  
D317: A5 07          BITA    7,X             
D319: 07 1A          ASR     <$1A            
D31B: 00 D4          NEG     <$D4            
D31D: D9 78          ADCB    <$78            
D31F: 72                                  
D320: 1E 07          EXG     $07             
D322: 01                                  
D323: 19             DAA                     
D324: 3C 72          CWAI    $72             
D326: A5 07          BITA    7,X             
D328: 05                                  
D329: 18                                  
D32A: 00 D4          NEG     <$D4            
D32C: F6 A5 05       LDB     $A505           
D32F: 4B                                  
D330: 70 05 1B       NEG     $051B           
D333: 4B                                  
D334: 72                                  
D335: A5 07          BITA    7,X             
D337: 08 1C          ASL     <$1C            
D339: 00 D5          NEG     <$D5            
D33B: 2F A5          BLE     $D2E2                          ; 
D33D: 05                                  
D33E: 4B                                  
D33F: 70 07 1D       NEG     $071D           
D342: 2D 72          BLT     $D3B6                          ; 
D344: 1E 07          EXG     $07             
D346: 09 1E          ROL     <$1E            
D348: 00 D5          NEG     <$D5            
D34A: 61                                  
D34B: 96 05          LDA     <$05            
D34D: A5 70          BITA    -16,S           
D34F: 08 20          ASL     <$20            
D351: 1E 05          EXG     $05             
D353: 2D 70          BLT     $D3C5                          ; 
D355: 08 1F          ASL     <$1F            
D357: A5 72          BITA    -14,S           
D359: A5 70          BITA    -16,S           
D35B: 00 21          NEG     <$21            
D35D: 00 0F          NEG     <$0F            
D35F: 80 06          SUBA    #$06            
D361: 0C 80          INC     <$80            
D363: 04 04          LSR     <$04            
D365: 0A 89          DEC     <$89            
D367: 0B                                  
D368: 03 80          COM     <$80            
D36A: 08 0F          ASL     <$0F            
D36C: 04 81          LSR     <$81            
D36E: 07 89          ASR     <$89            
D370: 0E 87          JMP     <$87            
D372: 04 02          LSR     <$02            
D374: 0F 19          CLR     <$19            
D376: 19             DAA                     
D377: 17 01 0C       LBSR    $010C           
D37A: 07 97          ASR     <$97            
D37C: 03 01          COM     <$01            
D37E: 0C 07          INC     <$07            
D380: 97 03          STA     <$03            
D382: 01                                  
D383: 0C 07          INC     <$07            
D385: 09 98          ROL     <$98            
D387: 03 09          COM     <$09            
D389: 98 03          EORA    <$03            
D38B: 09 18          ROL     <$18            
D38D: 1A 1A          ORCC    #$1A            
D38F: 05                                  
D390: 17 03 0D       LBSR    $030D           
D393: 80 03          SUBA    #$03            
D395: 0D 05          TST     <$05            
D397: 89 07          ADCA    #$07            
D399: 18                                  
D39A: 89 03          ADCA    #$03            
D39C: 87                                  
D39D: 04 02          LSR     <$02            
D39F: FF 80 05       STU     $8005           
D3A2: 04 17          LSR     <$17            
D3A4: 02                                  
D3A5: 00 00          NEG     <$00            
D3A7: 0D 00          TST     <$00            
D3A9: 04 0A          LSR     <$0A            
D3AB: 09 03          ROL     <$03            
D3AD: 01                                  
D3AE: 0A 89          DEC     <$89            
D3B0: 03 03          COM     <$03            
D3B2: 0F 04          CLR     <$04            
D3B4: 81 04          CMPA    #$04            
D3B6: 89 0A          ADCA    #$0A            
D3B8: 87                                  
D3B9: 06 09          ROR     <$09            
D3BB: 81 05          CMPA    #$05            
D3BD: 09 09          ROL     <$09            
D3BF: 07 09          ASR     <$09            
D3C1: 0B                                  
D3C2: 87                                  
D3C3: 04 02          LSR     <$02            
D3C5: 10                                  
D3C6: 80 03          SUBA    #$03            
D3C8: 12             NOP                     
D3C9: 04 81          LSR     <$81            
D3CB: 04 03          LSR     <$03            
D3CD: 00 00          NEG     <$00            
D3CF: 05                                  
D3D0: 09 07          ROL     <$07            
D3D2: 09 07          ROL     <$07            
D3D4: 09 07          ROL     <$07            
D3D6: 07 02          ASR     <$02            
D3D8: 0D 07          TST     <$07            
D3DA: 09 09          ROL     <$09            
D3DC: 07 18          ASR     <$18            
D3DE: 01                                  
D3DF: 89 07          ADCA    #$07            
D3E1: 0B                                  
D3E2: 02                                  
D3E3: FF 80 03       STU     $8003           
D3E6: 0C 80          INC     <$80            
D3E8: 04 0F          LSR     <$0F            
D3EA: 00 0D          NEG     <$0D            
D3EC: 00 04          NEG     <$04            
D3EE: 0A 09          DEC     <$09            
D3F0: 03 01          COM     <$01            
D3F2: 0A 89          DEC     <$89            
D3F4: 09 19          ROL     <$19            
D3F6: 00 0F          NEG     <$0F            
D3F8: 80 03          SUBA    #$03            
D3FA: 0C 00          INC     <$00            
D3FC: 00 04          NEG     <$04            
D3FE: 0A 09          DEC     <$09            
D400: 09 01          ROL     <$01            
D402: 09 09          ROL     <$09            
D404: 01                                  
D405: 09 09          ROL     <$09            
D407: 01                                  
D408: 89 08          ADCA    #$08            
D40A: 0B                                  
D40B: 02                                  
D40C: 80 04          SUBA    #$04            
D40E: 07 89          ASR     <$89            
D410: 05                                  
D411: 0B                                  
D412: 87                                  
D413: 03 02          COM     <$02            
D415: 0F 00          CLR     <$00            
D417: 04 01          LSR     <$01            
D419: 09 03          ROL     <$03            
D41B: 00 1A          NEG     <$1A            
D41D: 07 02          ASR     <$02            
D41F: 0C 05          INC     <$05            
D421: 89 08          ADCA    #$08            
D423: 0B                                  
D424: 02                                  
D425: FF 80 0C       STU     $800C           
D428: 04 0A          LSR     <$0A            
D42A: 89 0D          ADCA    #$0D            
D42C: 19             DAA                     
D42D: 80 03          SUBA    #$03            
D42F: 04 01          LSR     <$01            
D431: 09 09          ROL     <$09            
D433: 01                                  
D434: 0F 04          CLR     <$04            
D436: 01                                  
D437: 01                                  
D438: 00 87          NEG     <$87            
D43A: 05                                  
D43B: 02                                  
D43C: 12             NOP                     
D43D: 00 0D          NEG     <$0D            
D43F: 00 12          NEG     <$12            
D441: 00 04          NEG     <$04            
D443: 0A 09          DEC     <$09            
D445: 03 01          COM     <$01            
D447: 0A 09          DEC     <$09            
D449: 03 01          COM     <$01            
D44B: 0A 89          DEC     <$89            
D44D: 04 87          LSR     <$87            
D44F: 03 08          COM     <$08            
D451: 81 02          CMPA    #$02            
D453: 89 09          ADCA    #$09            
D455: 0B                                  
D456: 02                                  
D457: 05                                  
D458: 09 09          ROL     <$09            
D45A: 0B                                  
D45B: 02                                  
D45C: 00 07          NEG     <$07            
D45E: 09 09          ROL     <$09            
D460: 0B                                  
D461: 02                                  
D462: 1A 09          ORCC    #$09            
D464: 0B                                  
D465: 02                                  
D466: FF 80 0B       STU     $800B           
D469: 12             NOP                     
D46A: 04 81          LSR     <$81            
D46C: 0A 89          DEC     <$89            
D46E: 0E 0B          JMP     <$0B            
D470: 07 05          ASR     <$05            
D472: 09 0B          ROL     <$0B            
D474: 07 05          ASR     <$05            
D476: 09 0B          ROL     <$0B            
D478: 02                                  
D479: 00 04          NEG     <$04            
D47B: 11                                  
D47C: 00 14          NEG     <$14                           ; {ram:m0014} 
D47E: 96 04          LDA     <$04            
D480: 15                                  
D481: 98 06          EORA    <$06            
D483: 80 06          SUBA    #$06            
D485: 19             DAA                     
D486: 19             DAA                     
D487: 09 98          ROL     <$98            
D489: 04 09          LSR     <$09            
D48B: 81 03          CMPA    #$03            
D48D: 0C 87          INC     <$87            
D48F: 03 97          COM     <$97            
D491: 04 81          LSR     <$81            
D493: 03 0C          COM     <$0C            
D495: 87                                  
D496: 03 1A          COM     <$1A            
D498: 1A 07          ORCC    #$07            
D49A: 89 07          ADCA    #$07            
D49C: 07 89          ASR     <$89            
D49E: 04 0B          LSR     <$0B            
D4A0: 02                                  
D4A1: FF 12 80       STU     $1280           
D4A4: 07 0D          ASR     <$0D            
D4A6: 80 03          SUBA    #$03            
D4A8: 04 0A          LSR     <$0A            
D4AA: 89 03          ADCA    #$03            
D4AC: 03 00          COM     <$00            
D4AE: 04 0A          LSR     <$0A            
D4B0: 89 04          ADCA    #$04            
D4B2: 07 09          ASR     <$09            
D4B4: 07 09          ASR     <$09            
D4B6: 07 89          ASR     <$89            
D4B8: 05                                  
D4B9: 81 04          CMPA    #$04            
D4BB: 0D 00          TST     <$00            
D4BD: 0F 80          CLR     <$80            
D4BF: 07 04          ASR     <$04            
D4C1: 01                                  
D4C2: 0A 09          DEC     <$09            
D4C4: 09 07          ROL     <$07            
D4C6: 89 05          ADCA    #$05            
D4C8: 03 00          COM     <$00            
D4CA: 00 04          NEG     <$04            
D4CC: 01                                  
D4CD: 89 0B          ADCA    #$0B            
D4CF: 0B                                  
D4D0: 02                                  
D4D1: 00 07          NEG     <$07            
D4D3: 09 09          ROL     <$09            
D4D5: 87                                  
D4D6: 07 02          ASR     <$02            
D4D8: FF 13 80       STU     $1380           
D4DB: 09 0D          ROL     <$0D            
D4DD: 00 04          NEG     <$04            
D4DF: 01                                  
D4E0: 01                                  
D4E1: 0A 89          DEC     <$89            
D4E3: 0B                                  
D4E4: 03 80          COM     <$80            
D4E6: 07 10          ASR     <$10            
D4E8: 00 04          NEG     <$04            
D4EA: 01                                  
D4EB: 0A 09          DEC     <$09            
D4ED: 03 01          COM     <$01            
D4EF: 01                                  
D4F0: 89 0E          ADCA    #$0E            
D4F2: 87                                  
D4F3: 0A 02          DEC     <$02            
D4F5: FF 00 13       STU     $0013           
D4F8: 80 03          SUBA    #$03            
D4FA: 04 00          LSR     <$00            
D4FC: 02                                  
D4FD: 00 00          NEG     <$00            
D4FF: 13             SYNC                    
D500: 00 04          NEG     <$04            
D502: 81 03          CMPA    #$03            
D504: 0A 09          DEC     <$09            
D506: 03 81          COM     <$81            
D508: 05                                  
D509: 89 07          ADCA    #$07            
D50B: 07 07          ASR     <$07            
D50D: 05                                  
D50E: 07 02          ASR     <$02            
D510: 02                                  
D511: 07 07          ASR     <$07            
D513: 09 01          ROL     <$01            
D515: 09 01          ROL     <$01            
D517: 09 09          ROL     <$09            
D519: 07 09          ASR     <$09            
D51B: 07 09          ASR     <$09            
D51D: 01                                  
D51E: 01                                  
D51F: 84 03          ANDA    #$03            
D521: 08 01          ASL     <$01            
D523: 01                                  
D524: 89 06          ADCA    #$06            
D526: 87                                  
D527: 06 05          ROR     <$05            
D529: 09 0B          ROL     <$0B            
D52B: 87                                  
D52C: 02                                  
D52D: 02                                  
D52E: FF 14 96       STU     $1496           
D531: 09 15          ROL     <$15            
D533: 98 0B          EORA    <$0B            
D535: 0F 80          CLR     <$80            
D537: 09 0D          ROL     <$0D            
D539: 00 04          NEG     <$04            
D53B: 01                                  
D53C: 0A 89          DEC     <$89            
D53E: 09 86          ROL     <$86            
D540: 07 0E          ASR     <$0E            
D542: 04 81          LSR     <$81            
D544: 03 89          COM     <$89            
D546: 0B                                  
D547: 86 09          LDA     #$09            
D549: 0E 04          JMP     <$04            
D54B: 81 03          CMPA    #$03            
D54D: 89 0E          ADCA    #$0E            
D54F: 0B                                  
D550: 02                                  
D551: 86 0A          LDA     #$0A            
D553: 89 0B          ADCA    #$0B            
D555: 87                                  
D556: 03 02          COM     <$02            
D558: 0E 86          JMP     <$86            
D55A: 09 89          ROL     <$89            
D55C: 0B                                  
D55D: 87                                  
D55E: 04 02          LSR     <$02            
D560: FF 80 05       STU     $8005           
D563: 0D 00          TST     <$00            
D565: 0D 00          TST     <$00            
D567: 0D 00          TST     <$00            
D569: 12             NOP                     
D56A: 04 81          LSR     <$81            
D56C: 0A 89          DEC     <$89            
D56E: 0A 9A          DEC     <$9A            
D570: 03 05          COM     <$05            
D572: 09 09          ROL     <$09            
D574: 03 99          COM     <$99            
D576: 03 09          COM     <$09            
D578: 09 07          ROL     <$07            
D57A: 09 09          ROL     <$09            
D57C: 87                                  
D57D: 06 02          ROR     <$02            
D57F: 11                                  
D580: 00 00          NEG     <$00            
D582: 19             DAA                     
D583: 17 17 01       LBSR    $1701           
D586: 0D 07          TST     <$07            
D588: 17 01 0D       LBSR    $010D           
D58B: 07 17          ASR     <$17            
D58D: 01                                  
D58E: 0D 07          TST     <$07            
D590: 09 18          ROL     <$18            
D592: 09 18          ROL     <$18            
D594: 09 18          ROL     <$18            
D596: 18                                  
D597: 1A 05          ORCC    #$05            
D599: 89 05          ADCA    #$05            
D59B: 0B                                  
D59C: 02                                  
D59D: FF 8E D5       STU     $8ED5           
D5A0: BB A6 C0       ADDA    $A6C0           
D5A3: 2A 07          BPL     $D5AC                          ; 
D5A5: 4C             INCA                    
D5A6: 27 12          BEQ     $D5BA                          ; 
D5A8: 4A             DECA                    
D5A9: E6 C0          LDB     ,U+             
D5AB: 8C C6 01       CMPX    #$C601          
D5AE: 48             LSLA                    
D5AF: 34 56          PSHS    U,X,B,A         
D5B1: AD 96          JSR     [A,X]           
D5B3: 35 56          PULS    A,B,X,U         
D5B5: 5A             DECB                    
D5B6: 26 F7          BNE     $D5AF                          ; 
D5B8: 20 E7          BRA     $D5A1                          ; 
D5BA: 39             RTS                     
D5BB: D5 F1          BITB    <$F1            
D5BD: D6 06          LDB     <$06            
D5BF: D6 20          LDB     <$20            
D5C1: D6 3F          LDB     <$3F            
D5C3: D6 4E          LDB     <$4E            
D5C5: D6 5E          LDB     <$5E            
D5C7: D6 91          LDB     <$91            
D5C9: D6 01          LDB     <$01            
D5CB: D6 2F          LDB     <$2F            
D5CD: D6 9B          LDB     <$9B            
D5CF: D6 A4          LDB     <$A4            
D5D1: D6 AD          LDB     <$AD            
D5D3: D6 D4          LDB     <$D4            
D5D5: D6 E0          LDB     <$E0            
D5D7: D6 EC          LDB     <$EC            
D5D9: D6 F8          LDB     <$F8            
D5DB: D7 04          STB     <$04            
D5DD: D7 10          STB     <$10            
D5DF: D7 1C          STB     <$1C            
D5E1: D7 28          STB     <$28            
D5E3: D6 6D          LDB     <$6D            
D5E5: D6 7F          LDB     <$7F            
D5E7: D7 54          STB     <$54            
D5E9: D6 B6          LDB     <$B6            
D5EB: D6 C5          LDB     <$C5            
D5ED: D6 CA          LDB     <$CA            
D5EF: D6 CF          LDB     <$CF            
D5F1: CE D5 F7       LDU     #$D5F7          
D5F4: 7E D7 62       JMP     $D762                          ; 
D5F7: 03 80          COM     <$80            
D5F9: 04 00          LSR     <$00            
D5FB: 80 0A          SUBA    #$0A            
D5FD: 03 80          COM     <$80            
D5FF: 07 00          ASR     <$00            
D601: CE D6 16       LDU     #$D616          
D604: 20 03          BRA     $D609                          ; 
D606: CE D6 0C       LDU     #$D60C          
D609: 7E D7 62       JMP     $D762                          ; 
D60C: 03 40          COM     <$40            
D60E: 08 04          ASL     <$04            
D610: 40             NEGA                    
D611: 05                                  
D612: 03 00          COM     <$00            
D614: 05                                  
D615: 04 03          LSR     <$03            
D617: 00 05          NEG     <$05            
D619: 00 40          NEG     <$40            
D61B: 05                                  
D61C: 07 40          ASR     <$40            
D61E: 08 00          ASL     <$00            
D620: CE D6 25       LDU     #$D625          
D623: 20 0D          BRA     $D632                          ; 
D625: 03 00          COM     <$00            
D627: 04 07          LSR     <$07            
D629: 80 07          SUBA    #$07            
D62B: 00 FF          NEG     <$FF            
D62D: 07 00          ASR     <$00            
D62F: CE D6 35       LDU     #$D635          
D632: 7E D7 62       JMP     $D762                          ; 
D635: 03 FF          COM     <$FF            
D637: 07 04          ASR     <$04            
D639: 80 07          SUBA    #$07            
D63B: 04 00          LSR     <$00            
D63D: 04 03          LSR     <$03            
D63F: CE D6 44       LDU     #$D644          
D642: 20 0D          BRA     $D651                          ; 
D644: 03 80          COM     <$80            
D646: 06 03          ROR     <$03            
D648: 00 04          NEG     <$04            
D64A: 03 FF          COM     <$FF            
D64C: 08 03          ASL     <$03            
D64E: CE D6 54       LDU     #$D654          
D651: 7E D7 62       JMP     $D762                          ; 
D654: 03 80          COM     <$80            
D656: 06 03          ROR     <$03            
D658: FF 05 03       STU     $0503           
D65B: 80 07          SUBA    #$07            
D65D: 03 CE          COM     <$CE            
D65F: D6 63          LDB     <$63                           ; {ram:m0063} 
D661: 20 EE          BRA     $D651                          ; 
D663: 03 FF          COM     <$FF            
D665: 08 00          ASL     <$00            
D667: 00 05          NEG     <$05            
D669: 00 80          NEG     <$80            
D66B: 05                                  
D66C: 00 CE          NEG     <$CE            
D66E: D6 7B          LDB     <$7B            
D670: 86 03          LDA     #$03            
D672: 97 20          STA     <$20            
D674: 8D 1E          BSR     $D694                          ; 
D676: 86 01          LDA     #$01            
D678: 97 20          STA     <$20            
D67A: 39             RTS                     
D67B: 01                                  
D67C: FF 0A 03       STU     $0A03           
D67F: CE D6 8D       LDU     #$D68D          
D682: 86 03          LDA     #$03            
D684: 97 20          STA     <$20            
D686: 8D 0C          BSR     $D694                          ; 
D688: 86 01          LDA     #$01            
D68A: 97 20          STA     <$20            
D68C: 39             RTS                     
D68D: 01                                  
D68E: FF 0A 00       STU     $0A00           
D691: CE D6 97       LDU     #$D697          
D694: 7E D7 62       JMP     $D762                          ; 
D697: 01                                  
D698: 00 09          NEG     <$09            
D69A: 02                                  
D69B: CE D6 A0       LDU     #$D6A0          
D69E: 20 F4          BRA     $D694                          ; 
D6A0: 01                                  
D6A1: 00 09          NEG     <$09            
D6A3: 06 CE          ROR     <$CE            
D6A5: D6 A9          LDB     <$A9            
D6A7: 20 EB          BRA     $D694                          ; 
D6A9: 01                                  
D6AA: 00 10          NEG     <$10            
D6AC: 03 CE          COM     <$CE            
D6AE: D6 B2          LDB     <$B2            
D6B0: 20 E2          BRA     $D694                          ; 
D6B2: 01                                  
D6B3: 00 10          NEG     <$10            
D6B5: 00 CE          NEG     <$CE            
D6B7: D6 97          LDB     <$97            
D6B9: 86 FF          LDA     #$FF            
D6BB: 97 20          STA     <$20            
D6BD: BD D7 62       JSR     $D762                          ; 
D6C0: 86 01          LDA     #$01            
D6C2: 97 20          STA     <$20            
D6C4: 39             RTS                     
D6C5: CE D6 A0       LDU     #$D6A0          
D6C8: 20 EF          BRA     $D6B9                          ; 
D6CA: CE D6 A9       LDU     #$D6A9          
D6CD: 20 EA          BRA     $D6B9                          ; 
D6CF: CE D6 16       LDU     #$D616          
D6D2: 20 E5          BRA     $D6B9                          ; 
D6D4: 8E D6 D9       LDX     #$D6D9          
D6D7: 20 5B          BRA     $D734                          ; 
D6D9: 02                                  
D6DA: 00 07          NEG     <$07            
D6DC: 03 00          COM     <$00            
D6DE: 07 00          ASR     <$00            
D6E0: 8E D6 E5       LDX     #$D6E5          
D6E3: 20 4F          BRA     $D734                          ; 
D6E5: 02                                  
D6E6: 00 16          NEG     <$16            
D6E8: 03 00          COM     <$00            
D6EA: 16 00 8E       LBRA    $008E           
D6ED: D6 F1          LDB     <$F1            
D6EF: 20 43          BRA     $D734                          ; 
D6F1: 02                                  
D6F2: 00 25          NEG     <$25            
D6F4: 03 00          COM     <$00            
D6F6: 25 00          BCS     $D6F8                          ; 
D6F8: 8E D6 FD       LDX     #$D6FD          
D6FB: 20 37          BRA     $D734                          ; 
D6FD: 02                                  
D6FE: 00 34          NEG     <$34            
D700: 03 00          COM     <$00            
D702: 34 00          PSHS    $00             
D704: 8E D7 09       LDX     #$D709          
D707: 20 2B          BRA     $D734                          ; 
D709: 02                                  
D70A: 00 43          NEG     <$43            
D70C: 03 00          COM     <$00            
D70E: 43             COMA                    
D70F: 00 8E          NEG     <$8E            
D711: D7 15          STB     <$15            
D713: 20 1F          BRA     $D734                          ; 
D715: 02                                  
D716: 00 52          NEG     <$52            
D718: 03 00          COM     <$00            
D71A: 52                                  
D71B: 00 8E          NEG     <$8E            
D71D: D7 21          STB     <$21            
D71F: 20 13          BRA     $D734                          ; 
D721: 02                                  
D722: 00 61          NEG     <$61            
D724: 03 00          COM     <$00            
D726: 61                                  
D727: 00 8E          NEG     <$8E            
D729: D7 2D          STB     <$2D            
D72B: 20 07          BRA     $D734                          ; 
D72D: 02                                  
D72E: 00 8E          NEG     <$8E            
D730: 03 00          COM     <$00            
D732: 8E 00 34       LDX     #$0034          
D735: 10 CE D7 4C    LDS     #$D74C          
D739: 8D 27          BSR     $D762                          ; 
D73B: 86 03          LDA     #$03            
D73D: 97 20          STA     <$20            
D73F: 35 40          PULS    U               
D741: 8D 1F          BSR     $D762                          ; 
D743: CE D7 50       LDU     #$D750          
D746: 86 01          LDA     #$01            
D748: 97 20          STA     <$20            
D74A: 20 16          BRA     $D762                          ; 
D74C: 01                                  
D74D: FF 06 03       STU     $0603           
D750: 01                                  
D751: FF 06 00       STU     $0600           
D754: CE D6 97       LDU     #$D697          
D757: 86 03          LDA     #$03            
D759: 97 20          STA     <$20            
D75B: 8D 05          BSR     $D762                          ; 
D75D: 86 01          LDA     #$01            
D75F: 97 20          STA     <$20            
D761: 39             RTS                     
D762: A6 C0          LDA     ,U+             
D764: 97 24          STA     <$24            
D766: 0F 1E          CLR     <$1E            
D768: A6 C0          LDA     ,U+             
D76A: 97 1F          STA     <$1F            
D76C: A6 C0          LDA     ,U+             
D76E: 97 1D          STA     <$1D            
D770: A6 C0          LDA     ,U+             
D772: 48             LSLA                    
D773: 8E D7 7D       LDX     #$D77D          
D776: AD 96          JSR     [A,X]           
D778: 0A 24          DEC     <$24            
D77A: 26 EC          BNE     $D768                          ; 
D77C: 39             RTS                     
D77D: D7 8D          STB     <$8D            
D77F: D7 94          STB     <$94            
D781: D7 9D          STB     <$9D            
D783: D7 A4          STB     <$A4            
D785: D7 AB          STB     <$AB            
D787: D7 B4          STB     <$B4            
D789: D7 BB          STB     <$BB            
D78B: D7 C4          STB     <$C4            
D78D: 8E D7 FF       LDX     #$D7FF          
D790: 0F 25          CLR     <$25            
D792: 20 52          BRA     $D7E6                          ; 
D794: 8E D8 04       LDX     #$D804          
D797: 86 FF          LDA     #$FF            
D799: 97 25          STA     <$25            
D79B: 20 30          BRA     $D7CD                          ; 
D79D: 8E D8 09       LDX     #$D809          
D7A0: 0F 25          CLR     <$25            
D7A2: 20 29          BRA     $D7CD                          ; 
D7A4: 8E D8 0E       LDX     #$D80E          
D7A7: 0F 25          CLR     <$25            
D7A9: 20 3B          BRA     $D7E6                          ; 
D7AB: 8E D8 13       LDX     #$D813          
D7AE: 86 FF          LDA     #$FF            
D7B0: 97 25          STA     <$25            
D7B2: 20 32          BRA     $D7E6                          ; 
D7B4: 8E D8 18       LDX     #$D818          
D7B7: 0F 25          CLR     <$25            
D7B9: 20 12          BRA     $D7CD                          ; 
D7BB: 8E D8 1D       LDX     #$D81D          
D7BE: 86 FF          LDA     #$FF            
D7C0: 97 25          STA     <$25            
D7C2: 20 09          BRA     $D7CD                          ; 
D7C4: 8E D8 22       LDX     #$D822          
D7C7: 86 FF          LDA     #$FF            
D7C9: 97 25          STA     <$25            
D7CB: 20 19          BRA     $D7E6                          ; 
D7CD: 96 21          LDA     <$21            
D7CF: D6 1D          LDB     <$1D            
D7D1: 27 12          BEQ     $D7E5                          ; 
D7D3: D6 25          LDB     <$25            
D7D5: 34 56          PSHS    U,X,B,A         
D7D7: 8D 4E          BSR     $D827                          ; 
D7D9: 35 56          PULS    A,B,X,U         
D7DB: 0A 1D          DEC     <$1D            
D7DD: 27 06          BEQ     $D7E5                          ; 
D7DF: AD 84          JSR     ,X              
D7E1: 97 21          STA     <$21            
D7E3: 20 F0          BRA     $D7D5                          ; 
D7E5: 39             RTS                     
D7E6: 96 22          LDA     <$22            
D7E8: D6 1D          LDB     <$1D            
D7EA: 27 12          BEQ     $D7FE                          ; 
D7EC: D6 25          LDB     <$25            
D7EE: 34 56          PSHS    U,X,B,A         
D7F0: 8D 35          BSR     $D827                          ; 
D7F2: 35 56          PULS    A,B,X,U         
D7F4: 0A 1D          DEC     <$1D            
D7F6: 27 06          BEQ     $D7FE                          ; 
D7F8: AD 84          JSR     ,X              
D7FA: 97 22          STA     <$22            
D7FC: 20 F0          BRA     $D7EE                          ; 
D7FE: 39             RTS                     
D7FF: 0A 21          DEC     <$21            
D801: D3 1E          ADDD    <$1E            
D803: 39             RTS                     
D804: 0C 22          INC     <$22            
D806: 93 1E          SUBD    <$1E            
D808: 39             RTS                     
D809: 0C 22          INC     <$22            
D80B: D3 1E          ADDD    <$1E            
D80D: 39             RTS                     
D80E: 0C 21          INC     <$21            
D810: D3 1E          ADDD    <$1E            
D812: 39             RTS                     
D813: 0C 21          INC     <$21            
D815: 93 1E          SUBD    <$1E            
D817: 39             RTS                     
D818: 0A 22          DEC     <$22            
D81A: D3 1E          ADDD    <$1E            
D81C: 39             RTS                     
D81D: 0A 22          DEC     <$22            
D81F: 93 1E          SUBD    <$1E            
D821: 39             RTS                     
D822: 0A 21          DEC     <$21            
D824: 93 1E          SUBD    <$1E            
D826: 39             RTS                     
D827: DC 21          LDD     <$21            
D829: 8D 2B          BSR     $D856                          ; 
D82B: 1F 02          TFR     D,Y             
D82D: D6 22          LDB     <$22            
D82F: C4 03          ANDB    #$03            
D831: CE D8 4A       LDU     #$D84A          
D834: 30 44          LEAX    4,U             
D836: 96 20          LDA     <$20            
D838: 2B 0F          BMI     $D849                          ; 
D83A: A6 86          LDA     A,X             
D83C: A4 C5          ANDA    B,U             
D83E: A7 E2          STA     ,-S             
D840: A6 C5          LDA     B,U             
D842: 43             COMA                    
D843: A4 A4          ANDA    ,Y              
D845: AA E0          ORA     ,S+             
D847: A7 A4          STA     ,Y              
D849: 39             RTS                     
D84A: C0 30          SUBB    #$30            
D84C: 0C 03          INC     <$03            
D84E: 00 55          NEG     <$55            
D850: AA FF A6 24    ORA     [$A624]         
D854: E6 26          LDB     6,Y             
D856: 58             LSLB                    
D857: 44             LSRA                    
D858: 56             RORB                    
D859: 44             LSRA                    
D85A: 56             RORB                    
D85B: 44             LSRA                    
D85C: 56             RORB                    
D85D: D3 4E          ADDD    <$4E            
D85F: 39             RTS                     
D860: A6 3B          LDA     -5,Y            
D862: 27 4E          BEQ     $D8B2                          ; 
D864: 2B 4D          BMI     $D8B3                          ; 
D866: 4A             DECA                    
D867: 27 03          BEQ     $D86C                          ; 
D869: 8D 4A          BSR     $D8B5                          ; 
D86B: 8C 6C 3B       CMPX    #$6C3B          
D86E: 10 8C 01 AA    CMPY    #$01AA          
D872: 26 1D          BNE     $D891                          ; 
D874: A6 35          LDA     -11,Y           
D876: 27 19          BEQ     $D891                          ; 
D878: E6 26          LDB     6,Y             
D87A: CB 03          ADDB    #$03            
D87C: A6 24          LDA     4,Y             
D87E: DD 21          STD     <$21            
D880: 0F 20          CLR     <$20            
D882: DC 1B          LDD     <$1B            
D884: DD 1E          STD     <$1E            
D886: 86 0C          LDA     #$0C            
D888: 97 1D          STA     <$1D            
D88A: BD D7 A4       JSR     $D7A4                          ; 
D88D: 10 8E 01 AA    LDY     #$01AA          
D891: EE 28          LDU     8,Y             
D893: EF 2C          STU     12,Y            
D895: AE 2A          LDX     10,Y            
D897: AF 2E          STX     14,Y            
D899: A6 3F          LDA     -1,Y            
D89B: 97 26          STA     <$26            
D89D: EC C4          LDD     ,U              
D89F: AA 80          ORA     ,X+             
D8A1: EA 80          ORB     ,X+             
D8A3: ED C4          STD     ,U              
D8A5: A6 42          LDA     2,U             
D8A7: AA 80          ORA     ,X+             
D8A9: A7 42          STA     2,U             
D8AB: 33 C8 20       LEAU    $20,U           
D8AE: 0A 26          DEC     <$26            
D8B0: 26 EB          BNE     $D89D                          ; 
D8B2: 39             RTS                     
D8B3: 6F 3B          CLR     -5,Y            
D8B5: EE 2C          LDU     12,Y            
D8B7: AE 2E          LDX     14,Y            
D8B9: A6 3F          LDA     -1,Y            
D8BB: 97 26          STA     <$26            
D8BD: EC 81          LDD     ,X++            
D8BF: 43             COMA                    
D8C0: A4 C4          ANDA    ,U              
D8C2: AA C9 18 00    ORA     $1800,U         
D8C6: 53             COMB                    
D8C7: E4 41          ANDB    1,U             
D8C9: EA C9 18 01    ORB     $1801,U         
D8CD: ED C4          STD     ,U              
D8CF: A6 80          LDA     ,X+             
D8D1: 43             COMA                    
D8D2: A4 42          ANDA    2,U             
D8D4: AA C9 18 02    ORA     $1802,U         
D8D8: A7 42          STA     2,U             
D8DA: 33 C8 20       LEAU    $20,U           
D8DD: 0A 26          DEC     <$26            
D8DF: 26 DC          BNE     $D8BD                          ; 
D8E1: 39             RTS                     
D8E2: 10 8E D9 08    LDY     #$D908          
D8E6: C6 07          LDB     #$07            
D8E8: A6 C0          LDA     ,U+             
D8EA: 2B 1B          BMI     $D907                          ; 
D8EC: 3D             MUL                     
D8ED: 31 AB          LEAY    D,Y             
D8EF: C6 07          LDB     #$07            
D8F1: A6 A0          LDA     ,Y+             
D8F3: 94 69          ANDA    <$69            
D8F5: AA 89 18 00    ORA     $1800,X         
D8F9: A7 84          STA     ,X              
D8FB: 30 88 20       LEAX    $20,X           
D8FE: 5A             DECB                    
D8FF: 26 F0          BNE     $D8F1                          ; 
D901: 30 89 FF 21    LEAX    $FF21,X         
D905: 20 DB          BRA     $D8E2                          ; 
D907: 39             RTS                     
D908: 30 CC CC       LEAX    $CC,PC          
D90B: CC CC CC       LDD     #$CCCC          
D90E: 30 30          LEAX    -16,Y           
D910: F0 30 30       SUBB    $3030           
D913: 30 30          LEAX    -16,Y           
D915: FC 30 CC       LDD     $30CC           
D918: 0C 30          INC     <$30            
D91A: 30 C0          LEAX    ,U+             
D91C: FC 30 CC       LDD     $30CC           
D91F: 0C 3C          INC     <$3C            
D921: 0C CC          INC     <$CC            
D923: 30 0C          LEAX    12,X            
D925: 3C CC          CWAI    $CC             
D927: FC 0C 0C       LDD     $0C0C           
D92A: 0C FC          INC     <$FC            
D92C: C0 C0          SUBB    #$C0            
D92E: FC 0C CC       LDD     $0CCC           
D931: 30 30          LEAX    -16,Y           
D933: CC C0 F0       LDD     #$C0F0          
D936: CC CC 30       LDD     #$CC30          
D939: FC 0C 30       LDD     $0C30           
D93C: 30 30          LEAX    -16,Y           
D93E: C0 C0          SUBB    #$C0            
D940: 30 CC CC       LEAX    $CC,PC          
D943: 30 CC CC       LEAX    $CC,PC          
D946: 30 30          LEAX    -16,Y           
D948: CC CC 3C       LDD     #$CC3C          
D94B: 0C CC          INC     <$CC            
D94D: 30 30          LEAX    -16,Y           
D94F: CC CC FC       LDD     #$CCFC          
D952: CC CC CC       LDD     #$CCCC          
D955: F0 CC CC       SUBB    $CCCC                          ; 
D958: F0 CC CC       SUBB    $CCCC                          ; 
D95B: F0 30 CC       SUBB    $30CC           
D95E: C0 C0          SUBB    #$C0            
D960: C0 CC          SUBB    #$CC            
D962: 30                                  
D963: F0 CC CC       SUBB    $CCCC                          ; 
D966: CC CC CC       LDD     #$CCCC          
D969: F0 FC C0       SUBB    $FCC0           
D96C: C0 F0          SUBB    #$F0            
D96E: C0 C0          SUBB    #$C0            
D970: FC FC C0       LDD     $FCC0           
D973: C0 F0          SUBB    #$F0            
D975: C0 C0          SUBB    #$C0            
D977: C0 30          SUBB    #$30            
D979: CC C0 3C       LDD     #$C03C          
D97C: CC CC 30       LDD     #$CC30          
D97F: CC CC CC       LDD     #$CCCC          
D982: FC CC CC       LDD     $CCCC                          ; 
D985: CC FC 30       LDD     #$FC30          
D988: 30 30          LEAX    -16,Y           
D98A: 30 30          LEAX    -16,Y           
D98C: FC 0C 0C       LDD     $0C0C           
D98F: 0C 0C          INC     <$0C            
D991: 0C CC          INC     <$CC            
D993: 30 CC CC       LEAX    $CC,PC          
D996: F0 C0 F0       SUBB    $C0F0                          ; 
D999: CC CC C0       LDD     #$CCC0          
D99C: C0 C0          SUBB    #$C0            
D99E: C0 C0          SUBB    #$C0            
D9A0: C0 FC          SUBB    #$FC            
D9A2: CC FC FC       LDD     #$FCFC          
D9A5: CC CC CC       LDD     #$CCCC          
D9A8: CC CC CC       LDD     #$CCCC          
D9AB: F0 FC FC       SUBB    $FCFC           
D9AE: CC CC 30       LDD     #$CC30          
D9B1: CC CC CC       LDD     #$CCCC          
D9B4: CC CC 30       LDD     #$CC30          
D9B7: F0 CC CC       SUBB    $CCCC                          ; 
D9BA: F0 C0 C0       SUBB    $C0C0                          ; 
D9BD: C0 30          SUBB    #$30            
D9BF: CC CC CC       LDD     #$CCCC          
D9C2: CC FC 3C       LDD     #$FC3C          
D9C5: F0 CC CC       SUBB    $CCCC                          ; 
D9C8: F0 F0 CC       SUBB    $F0CC           
D9CB: CC 30 CC       LDD     #$30CC          
D9CE: C0 30          SUBB    #$30            
D9D0: 0C CC          INC     <$CC            
D9D2: 30 FC 30       LEAX    [$30,PC]        
D9D5: 30 30          LEAX    -16,Y           
D9D7: 30 30          LEAX    -16,Y           
D9D9: 30 CC CC       LEAX    $CC,PC          
D9DC: CC CC CC       LDD     #$CCCC          
D9DF: CC 30 CC       LDD     #$30CC          
D9E2: CC CC CC       LDD     #$CCCC          
D9E5: CC 30 30       LDD     #$3030          
D9E8: CC CC CC       LDD     #$CCCC          
D9EB: CC FC FC       LDD     #$FCFC          
D9EE: CC CC CC       LDD     #$CCCC          
D9F1: 30 30          LEAX    -16,Y           
D9F3: 30 CC CC       LEAX    $CC,PC          
D9F6: CC CC CC       LDD     #$CCCC          
D9F9: 30 30          LEAX    -16,Y           
D9FB: 30 30          LEAX    -16,Y           
D9FD: FC 0C 30       LDD     $0C30           
DA00: 30 30          LEAX    -16,Y           
DA02: C0 FC          SUBB    #$FC            
DA04: 00 00          NEG     <$00            
DA06: 00 00          NEG     <$00            
DA08: 00 00          NEG     <$00            
DA0A: 00 00          NEG     <$00            
DA0C: C0 C0          SUBB    #$C0            
DA0E: 00 C0          NEG     <$C0            
DA10: C0 00          SUBB    #$00            
DA12: 00 00          NEG     <$00            
DA14: 00 00          NEG     <$00            
DA16: 00 30          NEG     <$30            
DA18: 30 0D          LEAX    13,X            
DA1A: 18                                  
DA1B: 20 17          BRA     $DA34                          ; 
DA1D: 15                                  
DA1E: 0A 17          DEC     <$17            
DA20: 0D 24          TST     <$24            
DA22: 1F 01          TFR     D,X             
DA24: 26 01          BNE     $DA27                          ; 
DA26: FF 20 1B       STU     $201B           
DA29: 12             NOP                     
DA2A: 1D             SEX                     
DA2B: 1D             SEX                     
DA2C: 0E 17          JMP     <$17            
DA2E: 24 0B          BCC     $DA3B                          ; 
DA30: 22 25          BHI     $DA57                          ; 
DA32: FF 16 12       STU     $1612           
DA35: 0C 11          INC     <$11            
DA37: 0A 0E          DEC     <$0E            
DA39: 15                                  
DA3A: 24 0A          BCC     $DA46                          ; 
DA3C: 12             NOP                     
DA3D: 0C 11          INC     <$11            
DA3F: 15                                  
DA40: 16 0A 22       LBRA    $0A22           
DA43: 1B                                  
DA44: FF 0C 18       STU     $0C18           
DA47: 19             DAA                     
DA48: 22 1B          BHI     $DA65                          ; 
DA4A: 12             NOP                     
DA4B: 10                                  
DA4C: 11                                  
DA4D: 1D             SEX                     
DA4E: 24 01          BCC     $DA51                          ; 
DA50: 09 08          ROL     <$08            
DA52: 03 FF          COM     <$FF            
DA54: 1C 19          ANDCC   #$19            
DA56: 0E 0C          JMP     <$0C            
DA58: 1D             SEX                     
DA59: 1B                                  
DA5A: 0A 15          DEC     <$15            
DA5C: 24 0A          BCC     $DA68                          ; 
DA5E: 1C 1C          ANDCC   #$1C            
DA60: 18                                  
DA61: 0C 12          INC     <$12            
DA63: 0A 1D          DEC     <$1D            
DA65: 0E 1C          JMP     <$1C            
DA67: FF 15 12       STU     $1512           
DA6A: 0C 0E          INC     <$0E            
DA6C: 17 1C 0E       LBSR    $1C0E           
DA6F: 0D 24          TST     <$24            
DA71: 1D             SEX                     
DA72: 18                                  
DA73: 24 FF          BCC     $DA74                          ; 
DA75: 1D             SEX                     
DA76: 0A 17          DEC     <$17            
DA78: 0D 22          TST     <$22            
DA7A: 24 0C          BCC     $DA88                          ; 
DA7C: 18                                  
DA7D: 1B                                  
DA7E: 19             DAA                     
DA7F: 18                                  
DA80: 1B                                  
DA81: 0A 1D          DEC     <$1D            
DA83: 12             NOP                     
DA84: 18                                  
DA85: 17 FF 0A       LBSR    $FF0A           
DA88: 15                                  
DA89: 15                                  
DA8A: 24 1B          BCC     $DAA7                          ; 
DA8C: 12             NOP                     
DA8D: 10                                  
DA8E: 11                                  
DA8F: 1D             SEX                     
DA90: 1C 24          ANDCC   #$24            
DA92: 1B                                  
DA93: 0E 1C          JMP     <$1C            
DA95: 0E 1B          JMP     <$1B            
DA97: 1F 0E          TFR     D,?             
DA99: 0D FF          TST     <$FF            
DA9B: 18                                  
DA9C: 17 0E 24       LBSR    $0E24           
DA9F: 19             DAA                     
DAA0: 15                                  
DAA1: 0A 22          DEC     <$22            
DAA3: 0E 1B          JMP     <$1B            
DAA5: FF 1D 20       STU     $1D20           
DAA8: 18                                  
DAA9: 24 19          BCC     $DAC4                          ; 
DAAB: 15                                  
DAAC: 0A 22          DEC     <$22            
DAAE: 0E 1B          JMP     <$1B            
DAB0: FF 11 12       STU     $1112           
DAB3: 10                                  
DAB4: 11                                  
DAB5: 24 1C          BCC     $DAD3                          ; 
DAB7: 0C 18          INC     <$18            
DAB9: 1B                                  
DABA: 0E FF          JMP     <$FF            
DABC: 19             DAA                     
DABD: 15                                  
DABE: 0A 22          DEC     <$22            
DAC0: 0E 1B          JMP     <$1B            
DAC2: 24 18          BCC     $DADC                          ; 
DAC4: 17 0E FF       LBSR    $0EFF           
DAC7: 19             DAA                     
DAC8: 15                                  
DAC9: 0A 22          DEC     <$22            
DACB: 0E 1B          JMP     <$1B            
DACD: 24 1D          BCC     $DAEC                          ; 
DACF: 20 18          BRA     $DAE9                          ; 
DAD1: FF 19 15       STU     $1915           
DAD4: 01                                  
DAD5: FF 19 15       STU     $1915           
DAD8: 02                                  
DAD9: FF 10 0E       STU     $100E           
DADC: 1D             SEX                     
DADD: 24 1B          BCC     $DAFA                          ; 
DADF: 0E 0A          JMP     <$0A            
DAE1: 0D 22          TST     <$22            
DAE3: 24 19          BCC     $DAFE                          ; 
DAE5: 15                                  
DAE6: 0A 22          DEC     <$22            
DAE8: 0E 1B          JMP     <$1B            
DAEA: 24 18          BCC     $DB04                          ; 
DAEC: 17 0E FF       LBSR    $0EFF           
DAEF: 10                                  
DAF0: 0E 1D          JMP     <$1D            
DAF2: 24 1B          BCC     $DB0F                          ; 
DAF4: 0E 0A          JMP     <$0A            
DAF6: 0D 22          TST     <$22            
DAF8: 24 19          BCC     $DB13                          ; 
DAFA: 15                                  
DAFB: 0A 22          DEC     <$22            
DAFD: 0E 1B          JMP     <$1B            
DAFF: 24 1D          BCC     $DB1E                          ; 
DB01: 20 18          BRA     $DB1B                          ; 
DB03: FF 0C 11       STU     $0C11           
DB06: 0A 16          DEC     <$16            
DB08: 0B                                  
DB09: 0E 1B          JMP     <$1B            
DB0B: FF 8D 47       STU     $8D47           

DB0E: CE DB 32       LDU     #$DB32          
DB11: 96 52          LDA     <$52            
DB13: 84 02          ANDA    #$02            
DB15: EE C6          LDU     A,U             
DB17: 8D 79          BSR     $DB92                          ; 
DB19: 8E 1B 03       LDX     #$1B03          
DB1C: 8D 03          BSR     $DB21                          ; 
DB1E: 7E D8 E2       JMP     $D8E2                          ; 
DB21: A6 C4          LDA     ,U              
DB23: 2B 08          BMI     $DB2D                          ; 
DB25: 26 0A          BNE     $DB31                          ; 
DB27: 33 41          LEAU    1,U             
DB29: 30 01          LEAX    1,X             
DB2B: 20 F4          BRA     $DB21                          ; 
DB2D: 33 5F          LEAU    -1,U            
DB2F: 30 1F          LEAX    -1,X            
DB31: 39             RTS                     

DB32: 00 BB          NEG     <$BB            
DB34: 00 C3          NEG     <$C3            
DB36: 34 10          PSHS    X               
DB38: 8D 1B          BSR     $DB55                          ; 
DB3A: 35 10          PULS    X               
DB3C: CE 00 CB       LDU     #$00CB          
DB3F: 8D 03          BSR     $DB44                          ; 
DB41: 7E D8 E2       JMP     $D8E2                          ; 
DB44: 1F 32          TFR     U,Y             
DB46: A6 A0          LDA     ,Y+             
DB48: 2B 08          BMI     $DB52                          ; 
DB4A: 26 08          BNE     $DB54                          ; 
DB4C: 86 24          LDA     #$24            
DB4E: A7 3F          STA     -1,Y            
DB50: 20 F4          BRA     $DB46                          ; 
DB52: 6F 3E          CLR     -2,Y            
DB54: 39             RTS                     

DB55: DD 6E          STD     <$6E            
DB57: C6 07          LDB     #$07            
DB59: 8E 00 CB       LDX     #$00CB          
DB5C: 6F 80          CLR     ,X+             
DB5E: 5A             DECB                    
DB5F: 26 FB          BNE     $DB5C                          ; 
DB61: 8E 00 CD       LDX     #$00CD          
DB64: CC 27 10       LDD     #$2710          
DB67: 8D 14          BSR     $DB7D                          ; 
DB69: CC 03 E8       LDD     #$03E8          
DB6C: 8D 0F          BSR     $DB7D                          ; 
DB6E: CC 00 64       LDD     #$0064          
DB71: 8D 0A          BSR     $DB7D                          ; 
DB73: CC 00 0A       LDD     #$000A          
DB76: 8D 05          BSR     $DB7D                          ; 
DB78: D6 6F          LDB     <$6F            
DB7A: E7 84          STB     ,X              
DB7C: 39             RTS                     

DB7D: 0F 6B          CLR     <$6B            
DB7F: DD 6C          STD     <$6C            
DB81: DC 6E          LDD     <$6E            
DB83: DD 6E          STD     <$6E            
DB85: 93 6C          SUBD    <$6C            
DB87: 25 04          BCS     $DB8D                          ; 
DB89: 0C 6B          INC     <$6B            
DB8B: 20 F6          BRA     $DB83                          ; 
DB8D: 96 6B          LDA     <$6B            
DB8F: A7 80          STA     ,X+             
DB91: 39             RTS                     

DB92: 5F             CLRB                    
DB93: 8E 00 D2       LDX     #$00D2          
DB96: 33 47          LEAU    7,U             
DB98: A6 C2          LDA     ,-U             
DB9A: CB F0          ADDB    #$F0            
DB9C: A9 82          ADCA    ,-X             
DB9E: 19             DAA                     
DB9F: 1F 89          TFR     A,B             
DBA1: 84 0F          ANDA    #$0F            
DBA3: A7 C4          STA     ,U              
DBA5: 8C 00 CB       CMPX    #$00CB          
DBA8: 26 EE          BNE     $DB98                          ; 
DBAA: CB F0          ADDB    #$F0            
DBAC: 39             RTS                     

DBAD: CE DB C1       LDU     #$DBC1          
DBB0: EC C1          LDD     ,U++            
DBB2: 2B 0C          BMI     $DBC0                          ; A=FF ... end of the table
DBB4: AE C1          LDX     ,U++            
DBB6: 10 AE C1       LDY     ,U++            
DBB9: 8D 1F          BSR     $DBDA                          ; 
DBBB: 4A             DECA                    
DBBC: 26 FB          BNE     $DBB9                          ; 
DBBE: 20 F0          BRA     $DBB0                          ; 
DBC0: 39             RTS                     

DBC1: 0A 10           
DBC3: DC D7           
DBC5: 34 00
            
DBC7: 0A 05          
DBC9: DE 17          
DBCB: 3B 80
 
DBCD: 02 08 
DBDF: DE 7B                                  
DBD1: 3D D8
 
DBD3: 02 06 
DBD5: DE 9B 
DBD7: 3E E2
       
DBD9: FF      ; End of list 

DBDA: 34 46          PSHS    U,B,A         
DBDC: 4F             CLRA                    
DBDD: ED E3          STD     ,--S            
DBDF: 34 16          PSHS    X,B,A           
DBE1: 6F 22          CLR     2,Y             
DBE3: EC 81          LDD     ,X++            
DBE5: 6D 64          TST     4,S             
DBE7: 27 0C          BEQ     $DBF5                          ; 
DBE9: 44             LSRA                    
DBEA: 56             RORB                    
DBEB: 66 22          ROR     2,Y             
DBED: 44             LSRA                    
DBEE: 56             RORB                    
DBEF: 66 22          ROR     2,Y             
DBF1: 6A 64          DEC     4,S             
DBF3: 20 F0          BRA     $DBE5                          ; 
DBF5: ED A4          STD     ,Y              
DBF7: 31 23          LEAY    3,Y             
DBF9: A6 E4          LDA     ,S              
DBFB: A7 64          STA     4,S             
DBFD: 6A 65          DEC     5,S             
DBFF: 26 E0          BNE     $DBE1                          ; 
DC01: 35 56          PULS    A,B,X,U         
DC03: 4C             INCA                    
DC04: 81 04          CMPA    #$04            
DC06: 26 D5          BNE     $DBDD                          ; 
DC08: 58             LSLB                    
DC09: 3A             ABX                     
DC0A: 35 C6          PULS    A,B,U,PC        
DC0C: 35 10          PULS    X               
DC0E: 96 50          LDA     <$50            
DC10: 84 02          ANDA    #$02            
DC12: 10 27 E4 55    LBEQ    $E455           
DC16: 0A 50          DEC     <$50            
DC18: 1F 20          TFR     Y,D             
DC1A: 34 16          PSHS    X,B,A           
DC1C: 7E C6 10       JMP     $C610                          ; 
DC1F: 34 12          PSHS    X,A             
DC21: 4F             CLRA                    
DC22: DD 64          STD     <$64            
DC24: 43             COMA                    
DC25: 59             ROLB                    
DC26: 25 05          BCS     $DC2D                          ; 
DC28: 43             COMA                    
DC29: 06 64          ROR     <$64            
DC2B: 20 F8          BRA     $DC25                          ; 
DC2D: 03 64          COM     <$64            
DC2F: 8D 08          BSR     $DC39                          ; 
DC31: D4 64          ANDB    <$64            
DC33: D1 65          CMPB    <$65            
DC35: 22 F8          BHI     $DC2F                          ; 
DC37: 35 92          PULS    A,X,PC          
DC39: 34 10          PSHS    X               
DC3B: 9E 61          LDX     <$61            
DC3D: 30 01          LEAX    1,X             
DC3F: 8C DF 5A       CMPX    #$DF5A          
DC42: 25 03          BCS     $DC47                          ; 
DC44: 8E C0 00       LDX     #$C000          
DC47: 9F 61          STX     <$61            
DC49: E6 84          LDB     ,X              
DC4B: 35 90          PULS    X,PC            
```

# IRQ Handler

```code
IRQHandler:
DC4D: B6 FF 02       LDA     $FF02                          ; {hard:PIA0_DB} 
DC50: 0C 14          INC     <$14                           ; {ram:m0014} 
DC52: 0C 63          INC     <$63                           ; {ram:m0063} 
DC54: 3B             RTI
                     
DC55: CE FF 01       LDU     #$FF01          
DC58: 8D 00          BSR     $DC5A                          ; 
DC5A: A6 C4          LDA     ,U              
DC5C: 84 F7          ANDA    #$F7            
DC5E: 54             LSRB                    
DC5F: 24 02          BCC     $DC63                          ; 
DC61: 8A 08          ORA     #$08            
DC63: A7 C1          STA     ,U++            
DC65: 39             RTS                     
DC66: 8D 66          BSR     $DCCE                          ; 
DC68: 8E 00 14       LDX     #$0014          
DC6B: C6 01          LDB     #$01            
DC6D: D7 10          STB     <$10            
DC6F: 96 52          LDA     <$52            
DC71: 84 02          ANDA    #$02            
DC73: 34 02          PSHS    A               
DC75: EB E0          ADDB    ,S+             
DC77: 8D DC          BSR     $DC55                          ; 
DC79: CC 40 80       LDD     #$4080          
DC7C: 97 11          STA     <$11            
DC7E: CA 02          ORB     #$02            
DC80: F7 FF 20       STB     $FF20                          ; {hard:PIA1_DA} 
DC83: C8 02          EORB    #$02            
DC85: B6 FF 00       LDA     $FF00                          ; {hard:PIA0_DA} 
DC88: 2B 03          BMI     $DC8D                          ; 
DC8A: D0 11          SUBB    <$11            
DC8C: 8C DB 11       CMPX    #$DB11          
DC8F: 96 11          LDA     <$11            
DC91: 44             LSRA                    
DC92: 81 01          CMPA    #$01            
DC94: 26 E6          BNE     $DC7C                          ; 
DC96: E7 82          STB     ,-X             
DC98: D6 10          LDB     <$10            
DC9A: 5A             DECB                    
DC9B: 2A D0          BPL     $DC6D                          ; 
DC9D: EC 84          LDD     ,X              
DC9F: 0F 15          CLR     <$15            
DCA1: 54             LSRB                    
DCA2: 54             LSRB                    
DCA3: 27 07          BEQ     $DCAC                          ; 
DCA5: C1 3F          CMPB    #$3F            
DCA7: 26 07          BNE     $DCB0                          ; 
DCA9: C6 03          LDB     #$03            
DCAB: 8C C6 01       CMPX    #$C601          
DCAE: D7 15          STB     <$15            
DCB0: 44             LSRA                    
DCB1: 44             LSRA                    
DCB2: 27 07          BEQ     $DCBB                          ; 
DCB4: 81 3F          CMPA    #$3F            
DCB6: 26 07          BNE     $DCBF                          ; 
DCB8: 86 02          LDA     #$02            
DCBA: 8C 86 04       CMPX    #$8604          
DCBD: 97 15          STA     <$15            
DCBF: 86 02          LDA     #$02            
DCC1: B7 FF 20       STA     $FF20                          ; {hard:PIA1_DA} 
DCC4: 5F             CLRB                    
DCC5: 8D 8E          BSR     $DC55                          ; 
DCC7: B6 FF 23       LDA     $FF23                          ; {hard:PIA1_CB} 
DCCA: 8A 08          ORA     #$08            
DCCC: 20 05          BRA     $DCD3                          ; 
DCCE: B6 FF 23       LDA     $FF23                          ; {hard:PIA1_CB} 
DCD1: 84 F7          ANDA    #$F7            
DCD3: B7 FF 23       STA     $FF23                          ; {hard:PIA1_CB} 
DCD6: 39             RTS                     



DCD7: 0A 80          DEC     <$80            
DCD9: 2A A0          BPL     $DC7B                          ; 
DCDB: 15                                  
DCDC: C0 2D          SUBB    #$2D            
DCDE: A0 2D          SUBA    13,Y            
DCE0: D0 17          SUBB    <$17            
DCE2: A0 0F          SUBA    15,X            
DCE4: E0 1A          SUBB    -6,X            
DCE6: 80 1A          SUBA    #$1A            
DCE8: C0 1A          SUBB    #$1A            
DCEA: 80 1F          SUBA    #$1F            
DCEC: 80 0F          SUBA    #$0F            
DCEE: 80 0A          SUBA    #$0A            
DCF0: C0 0A          SUBB    #$0A            
DCF2: 80 0F          SUBA    #$0F            
DCF4: C0 0F          SUBB    #$0F            
DCF6: E0 0A          SUBB    10,X            
DCF8: 80 2A          SUBA    #$2A            
DCFA: A0 15          SUBA    -11,X           
DCFC: C0 2D          SUBB    #$2D            
DCFE: A0 2D          SUBA    13,Y            
DD00: D0 17          SUBB    <$17            
DD02: A0 0F          SUBA    15,X            
DD04: E0 0A          SUBB    10,X            
DD06: 80 3A          SUBA    #$3A            
DD08: D8 7A          EORB    <$7A            
DD0A: F8 6A F8       EORB    $6AF8           
DD0D: 0A A8          DEC     <$A8            
DD0F: 0A A8          DEC     <$A8            
DD11: 2A 38          BPL     $DD4B                          ; 
DD13: 6A 38          DEC     -8,Y            
DD15: 60 00          NEG     0,X             
DD17: 00 00          NEG     <$00            
DD19: 0A 80          DEC     <$80            
DD1B: 2A A0          BPL     $DCBD                          ; 
DD1D: 15                                  
DD1E: C0 2D          SUBB    #$2D            
DD20: A0 2D          SUBA    13,Y            
DD22: D0 17          SUBB    <$17            
DD24: A0 0F          SUBA    15,X            
DD26: E6                                  
DD27: FA FE FA       ORB     $FEFA           
DD2A: FE 0A A0       LDU     $0AA0           
DD2D: 0A AA          DEC     <$AA            
DD2F: 3A             ABX                     
DD30: AE 6A          LDX     10,S            
DD32: 0E 60          JMP     <$60            
DD34: 00 00          NEG     <$00            
DD36: 00 0A          NEG     <$0A            
DD38: 80 2A          SUBA    #$2A            
DD3A: A0 15          SUBA    -11,X           
DD3C: C0 2D          SUBB    #$2D            
DD3E: A0 2D          SUBA    13,Y            
DD40: D0 17          SUBB    <$17            
DD42: A0 0F          SUBA    15,X            
DD44: E0 0A          SUBB    10,X            
DD46: 80 7A          SUBA    #$7A            
DD48: D8 7A          EORB    <$7A            
DD4A: F8 6A F0       EORB    $6AF0           
DD4D: 0A A0          DEC     <$A0            
DD4F: 6A A0          DEC     ,Y+             
DD51: 68 50          ASL     -16,U           
DD53: 60 70          NEG     -16,S           
DD55: 00 38          NEG     <$38            
DD57: 0A C0          DEC     <$C0            
DD59: 1A B0          ORCC    #$B0            
DD5B: 15                                  
DD5C: 58             LSLB                    
DD5D: 35 58          PULS    DP,X,U          
DD5F: 35 58          PULS    DP,X,U          
DD61: 15                                  
DD62: 58             LSLB                    
DD63: 35 B8          PULS    DP,X,Y,PC       
DD65: 6A                                  
DD66: B0 EA A0       SUBA    $EAA0           
DD69: 6A A0          DEC     ,Y+             
DD6B: 2A A0          BPL     $DD0D                          ; 
DD6D: 2A A0          BPL     $DD0F                          ; 
DD6F: 28 A0          BVC     $DD11                          ; 
DD71: 1C A0          ANDCC   #$A0            
DD73: 00 A0          NEG     <$A0            
DD75: 01                                  
DD76: C0 1A          SUBB    #$1A            
DD78: 80 6A          SUBA    #$6A            
DD7A: C0 D5          SUBB    #$D5            
DD7C: 40             NEGA                    
DD7D: D5 60          BITB    <$60            
DD7F: D5 60          BITB    <$60            
DD81: D5 40          BITB    <$40            
DD83: EA E0          ORB     ,S+             
DD85: 6A                                  
DD86: B0 2A B8       SUBA    $2AB8           
DD89: 2A B0          BPL     $DD3B                          ; 
DD8B: 2A A0          BPL     $DD2D                          ; 
DD8D: 2A A0          BPL     $DD2F                          ; 
DD8F: 28 A0          BVC     $DD31                          ; 
DD91: 29 C0          BVS     $DD53                          ; 
DD93: 28 00          BVC     $DD95                          ; 
DD95: 1C 00          ANDCC   #$00            
DD97: 02                                  
DD98: A0 0A          SUBA    10,X            
DD9A: A8 07          EORA    7,X             
DD9C: 50             NEGB                    
DD9D: 0B                                  
DD9E: 68 17          ASL     -9,X            
DDA0: 68 0B          ASL     11,X            
DDA2: D0 0F          SUBB    <$0F            
DDA4: E0 02          SUBB    2,X             
DDA6: B0 06 B0       SUBA    $06B0           
DDA9: 02                                  
DDAA: B0 03 F0       SUBA    $03F0           
DDAD: 03 E0          COM     <$E0            
DDAF: 06 A0          ROR     <$A0            
DDB1: 02                                  
DDB2: A0 07          SUBA    7,X             
DDB4: E0 0F          SUBB    15,X            
DDB6: E0 02          SUBB    2,X             
DDB8: A0 0A          SUBA    10,X            
DDBA: A8 07          EORA    7,X             
DDBC: 50             NEGB                    
DDBD: 0B                                  
DDBE: 68 17          ASL     -9,X            
DDC0: 68 0B          ASL     11,X            
DDC2: D0 0F          SUBB    <$0F            
DDC4: F0 02 A0       SUBB    $02A0           
DDC7: 1A BC          ORCC    #$BC            
DDC9: 1E B7          EXG     $B7             
DDCB: 1E A6          EXG     $A6             
DDCD: 0A A0          DEC     <$A0            
DDCF: 0A A0          DEC     <$A0            
DDD1: 1C AE          ANDCC   #$AE            
DDD3: 1C AE          ANDCC   #$AE            
DDD5: 00 06          NEG     <$06            
DDD7: 00 00          NEG     <$00            
DDD9: 02                                  
DDDA: A0 0A          SUBA    10,X            
DDDC: A8 07          EORA    7,X             
DDDE: 50             NEGB                    
DDDF: 0B                                  
DDE0: 68 17          ASL     -9,X            
DDE2: 68 0B          ASL     11,X            
DDE4: D0 6F          SUBB    <$6F            
DDE6: E0 7E          SUBB    -2,S            
DDE8: BF 7E BF       STX     $7EBF           
DDEB: 0A A0          DEC     <$A0            
DDED: 6A A0          DEC     ,Y+             
DDEF: 7A AE 78       DEC     $AE78           
DDF2: AE 00          LDX     0,X             
DDF4: 06 00          ROR     <$00            
DDF6: 00 02          NEG     <$02            
DDF8: A0 0A          SUBA    10,X            
DDFA: A8 07          EORA    7,X             
DDFC: 50             NEGB                    
DDFD: 0B                                  
DDFE: 68 17          ASL     -9,X            
DE00: 68 0B          ASL     11,X            
DE02: D0 0F          SUBB    <$0F            
DE04: E0 02          SUBB    2,X             
DE06: A0 1A          SUBA    -6,X            
DE08: BE 1E BE       LDX     $1EBE           
DE0B: 1E A6          EXG     $A6             
DE0D: 0A A0          DEC     <$A0            
DE0F: 0A AE          DEC     <$AE            
DE11: 08 AE          ASL     <$AE            
DE13: 1C 06          ANDCC   #$06            
DE15: 1C 00          ANDCC   #$00            
DE17: 3F             SWI                     
DE18: F0 3F F0       SUBB    $3FF0           
DE1B: 3F             SWI                     
DE1C: C0 3F          SUBB    #$3F            
DE1E: C0 0F          SUBB    #$0F            
DE20: C0 3F          SUBB    #$3F            
DE22: F0 3F F0       SUBB    $3FF0           
DE25: 0F C0          CLR     <$C0            
DE27: 6F F8 3F       CLR     [$3F,S]         
DE2A: 38                                  
DE2B: 0F C0          CLR     <$C0            
DE2D: 3F             SWI                     
DE2E: F0 0F F6       SUBB    $0FF6           
DE31: 0F F0          CLR     <$F0            
DE33: 7F 0E 3F       CLR     $0E3F           
DE36: F0 3F F0       SUBB    $3FF0           
DE39: 0F C0          CLR     <$C0            
DE3B: 6F                                  
DE3C: F0 6C 70       SUBB    $6C70           
DE3F: 3F             SWI                     
DE40: F0 3F FC       SUBB    $3FFC           
DE43: FF F0 3F       STU     $F03F           
DE46: F0 3C F0       SUBB    $3CF0           
DE49: FF C0 FF       STU     $C0FF                          ; 
DE4C: F0 FF F0       SUBB    $FFF0                          ; {hard:vector6809} 
DE4F: 3F             SWI                     
DE50: F0 3F C0       SUBB    $3FC0           
DE53: 0F FC          CLR     <$FC            
DE55: 1F F8          TFR     ?,A             
DE57: 03 F0          COM     <$F0            
DE59: 03 F0          COM     <$F0            
DE5B: 03 F0          COM     <$F0            
DE5D: 0F F8          CLR     <$F8            
DE5F: 1F F8          TFR     ?,A             
DE61: 03 F0          COM     <$F0            
DE63: 1F F6          TFR     ?,?             
DE65: 1C FE          ANDCC   #$FE            
DE67: 03 F0          COM     <$F0            
DE69: 0F F8          CLR     <$F8            
DE6B: 6F                                  
DE6C: F0 0F F0       SUBB    $0FF0           
DE6F: 7C FE 0F       INC     $FE0F           
DE72: F8 1F F8       EORB    $1FF8           
DE75: 03 F0          COM     <$F0            
DE77: 1F F6          TFR     ?,?             
DE79: 0C FE          INC     <$FE            
DE7B: 01                                  
DE7C: 00 05          NEG     <$05            
DE7E: 40             NEGA                    
DE7F: 0D 60          TST     <$60            
DE81: 15                                  
DE82: 50             NEGB                    
DE83: 15                                  
DE84: 50             NEGB                    
DE85: 0D 60          TST     <$60            
DE87: 05                                  
DE88: 40             NEGA                    
DE89: 01                                  
DE8A: 00 00          NEG     <$00            
DE8C: 00 00          NEG     <$00            
DE8E: 00 05          NEG     <$05            
DE90: 40             NEGA                    
DE91: 35 58          PULS    DP,X,U          
DE93: 55                                  
DE94: 54             LSRB                    
DE95: 55                                  
DE96: 54             LSRB                    
DE97: 35 58          PULS    DP,X,U          
DE99: 05                                  
DE9A: 40             NEGA                    
DE9B: C1 83          CMPB    #$83            
DE9D: F3 CF 3F       ADDD    $CF3F                          ; 
DEA0: FC 0F F0       LDD     $0FF0           
DEA3: 03 C0          COM     <$C0            
DEA5: 01                                  
DEA6: 80 01          SUBA    #$01            
DEA8: 80 03          SUBA    #$03            
DEAA: C0 0F          SUBB    #$0F            
DEAC: F0 3F FC       SUBB    $3FFC           
DEAF: F3 CF C1       ADDD    $CFC1                          ; 
DEB2: 83 11 10       SUBD    #$1110          
DEB5: 1E E4          EXG     $E4             
DEB7: 0A D8          DEC     <$D8            
DEB9: 07 F0          ASR     <$F0            
DEBB: 0D 6C          TST     <$6C            
DEBD: 1A B2          ORCC    #$B2            
DEBF: 3A             ABX                     
DEC0: B8 3A B8       EORA    $3AB8           
DEC3: 3A             ABX                     
DEC4: B8 1F F0       EORA    $1FF0           
DEC7: 02                                  
DEC8: 80 2A          SUBA    #$2A            
DECA: A8                                  
DECB: AA                                  
DECC: AA                                  
DECD: AA                                  
DECE: AA 2A          ORA     10,Y            
DED0: A8 2A          EORA    10,Y            
DED2: A8 0A          EORA    10,X            
DED4: A0 0A          SUBA    10,X            
DED6: A0 02          SUBA    2,X             
DED8: 80 02          SUBA    #$02            
DEDA: 80 00          SUBA    #$00            
DEDC: 00 20          NEG     <$20            
DEDE: 00 28          NEG     <$28            
DEE0: 00 88          NEG     <$88            
DEE2: 00 8B          NEG     <$8B            
DEE4: 55                                  
DEE5: 8A AA          ORA     #$AA            
DEE7: 8B 55          ADDA    #$55            
DEE9: 88 33          EORA    #$33            
DEEB: 28 33          BVC     $DF20                          ; 
DEED: 20 00          BRA     $DEEF                          ; 
DEEF: 04 00          LSR     <$00            
DEF1: 00 03          NEG     <$03            
DEF3: 07 00          ASR     <$00            
DEF5: 31 06          LEAY    6,X             
DEF7: 00 18          NEG     <$18            
DEF9: 04 C0          LSR     <$C0            
DEFB: 09 50          ROL     <$50            
DEFD: 80 05          SUBA    #$05            
DEFF: 54             LSRB                    
DF00: 00 16          NEG     <$16            
DF02: 5C             INCB                    
DF03: 00 39          NEG     <$39            
DF05: 55                                  
DF06: 00 DA          NEG     <$DA            
DF08: AB C0          ADDA    ,U+             
DF0A: 2A 80          BPL     $DE8C                          ; 
DF0C: AA A0          ORA     ,Y+             
DF0E: AF A0          STX     ,Y+             
DF10: B5 E0 AF       BITA    $E0AF           
DF13: A0                                  
DF14: AA A0          ORA     ,Y+             
DF16: A5 A0          BITA    ,Y+             
DF18: 9A 60          ORA     <$60            
DF1A: 9A 60          ORA     <$60            
DF1C: A5 A0          BITA    ,Y+             
DF1E: AA A0          ORA     ,Y+             
DF20: AA A0          ORA     ,Y+             
DF22: AA A0          ORA     ,Y+             
DF24: AA A0          ORA     ,Y+             
DF26: AA A0          ORA     ,Y+             
DF28: AA A0          ORA     ,Y+             
DF2A: 00 00          NEG     <$00            
DF2C: 40             NEGA                    
DF2D: 00 60          NEG     <$60            
DF2F: 00 F0          NEG     <$F0            
DF31: 00 F0          NEG     <$F0            
DF33: 00 60          NEG     <$60            
DF35: 00 00          NEG     <$00            
DF37: 00 10          NEG     <$10            
DF39: 00 18          NEG     <$18            
DF3B: 00 3C          NEG     <$3C            
DF3D: 00 3C          NEG     <$3C            
DF3F: 00 18          NEG     <$18            
DF41: 00 00          NEG     <$00            
DF43: 00 04          NEG     <$04            
DF45: 00 06          NEG     <$06            
DF47: 00 0F          NEG     <$0F            
DF49: 00 0F          NEG     <$0F            
DF4B: 00 06          NEG     <$06            
DF4D: 00 00          NEG     <$00            
DF4F: 00 01          NEG     <$01            
DF51: 00 01          NEG     <$01            
DF53: 80 03          SUBA    #$03            
DF55: C0 03          SUBB    #$03            
DF57: C0 01          SUBB    #$01            
DF59: 80 00          SUBA    #$00            
DF5B: FE 01 FF       LDU     $01FF           
DF5E: 01                                  
DF5F: FF 00 FE       STU     $00FE           
DF62: 00 FE          NEG     <$FE            
DF64: 01                                  
DF65: FF 01 FF       STU     $01FF           
DF68: 00 FE          NEG     <$FE            
DF6A: 00 FE          NEG     <$FE            
DF6C: 01                                  
DF6D: FF 01 FF       STU     $01FF           
DF70: 00 FE          NEG     <$FE            
DF72: 00 FE          NEG     <$FE            
DF74: 01                                  
DF75: FF 01 FF       STU     $01FF           
DF78: 00 FE          NEG     <$FE            
DF7A: 00 FE          NEG     <$FE            
DF7C: 01                                  
DF7D: FF 01 FF       STU     $01FF           
DF80: 00 FE          NEG     <$FE            
DF82: 00 FE          NEG     <$FE            
DF84: 01                                  
DF85: FF 01 FF       STU     $01FF           
DF88: 00 FE          NEG     <$FE            
DF8A: 00 FE          NEG     <$FE            
DF8C: 01                                  
DF8D: FF 01 FF       STU     $01FF           
DF90: 00 FE          NEG     <$FE            
DF92: 00 FE          NEG     <$FE            
DF94: 01                                  
DF95: FF 01 FF       STU     $01FF           
DF98: 00 FE          NEG     <$FE            
DF9A: 00 FE          NEG     <$FE            
DF9C: 01                                  
DF9D: FF 01 FF       STU     $01FF           
DFA0: 00 FE          NEG     <$FE            
DFA2: 00 FE          NEG     <$FE            
DFA4: 01                                  
DFA5: FF 01 FF       STU     $01FF           
DFA8: 00 FE          NEG     <$FE            
DFAA: 00 FE          NEG     <$FE            
DFAC: 01                                  
DFAD: FF 01 FF       STU     $01FF           
DFB0: 00 FE          NEG     <$FE            
DFB2: 00 FE          NEG     <$FE            
DFB4: 01                                  
DFB5: FF 01 FF       STU     $01FF           
DFB8: 00 FE          NEG     <$FE            
DFBA: 00 FE          NEG     <$FE            
DFBC: 01                                  
DFBD: FF 01 FF       STU     $01FF           
DFC0: 00 FE          NEG     <$FE            
DFC2: 00 FE          NEG     <$FE            
DFC4: 01                                  
DFC5: FF 01 FF       STU     $01FF           
DFC8: 00 FE          NEG     <$FE            
DFCA: 00 FE          NEG     <$FE            
DFCC: 01                                  
DFCD: FF 01 FF       STU     $01FF           
DFD0: 00 FE          NEG     <$FE            
DFD2: 00 FE          NEG     <$FE            
DFD4: 01                                  
DFD5: FF 01 FF       STU     $01FF           
DFD8: 00 FE          NEG     <$FE            
DFDA: 00 FE          NEG     <$FE            
DFDC: 01                                  
DFDD: FF 01 FF       STU     $01FF           
DFE0: 00 FE          NEG     <$FE            
DFE2: 00 FE          NEG     <$FE            
DFE4: 01                                  
DFE5: FF 01 FF       STU     $01FF           
DFE8: 00 FE          NEG     <$FE            
DFEA: 00 FE          NEG     <$FE            
DFEC: 01                                  
DFED: FF 01 FF       STU     $01FF           
DFF0: 00 FE          NEG     <$FE            
DFF2: 00 FE          NEG     <$FE            
DFF4: 01                                  
DFF5: FF 01 FF       STU     $01FF           
DFF8: 00 FE          NEG     <$FE            
DFFA: 00 FE          NEG     <$FE            
DFFC: 01                                  
DFFD: FF F7 FF       STU     $F7FF           
```
