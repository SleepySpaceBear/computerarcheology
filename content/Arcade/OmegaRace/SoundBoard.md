![Sound Board](ORace.jpg)

# Sound Board

>>> cpu Z80

>>> binary roms/sound.k5

>>> memoryTable hard 

[Hardware Info](SoundHardware.md)

>>> memoryTable ram 

[RAM Usage](SoundRAMUse.md)

```code
; Commands:
;    0 - reset sound CPU
;    7 - beep used in diagnostics

0000: F3              DI                          ; Interrupts off
0001: ED 56           IM      1                   ; All interrupts go to RST 38
0003: 31 FC 13        LD      SP,$13FC            ; Stack pointer almost to top of RAM
0006: FD 21 00 10     LD      IY,$1000            
000A: 01 FF 03        LD      BC,$03FF            ; 400 bytes (1K) to clear
000D: 11 01 10        LD      DE,$1001            ; Destination is 1 ...
0010: 21 00 10        LD      HL,$1000            ; ... past source
0013: 36 00           LD      (HL),$00            ; Move 0 ...
0015: ED B0           LDIR                        ; ... through all RAM
0017: 01 1F 00        LD      BC,$001F            
001A: 11 31 10        LD      DE,$1031            
001D: 21 30 10        LD      HL,$1030            
0020: 36 FF           LD      (HL),$FF            
0022: ED B0           LDIR                        
0024: 21 FF FF        LD      HL,$FFFF            
0027: 22 C0 11        LD      ($11C0),HL          ; {ram.m11C0}
002A: 01 5A 00        LD      BC,$005A            
002D: 11 C2 11        LD      DE,$11C2            
0030: 21 C0 11        LD      HL,$11C0            
0033: ED B0           LDIR                        
0035: 18 50           JR      $87                 ; {}

0037: 4E              LD      C,(HL)              

0038: 08              EX      AF,AF'              ; Hold flags and A
0039: D9              EXX                         ; Hold everything else
003A: DB 00           IN      A,($00)             ; {hard.SOUNDCMD} Get the command
003C: E6 7F           AND     $7F                 ; Command is not zero ...
003E: 20 03           JR      NZ,$43              ; {} ... handle it
0040: C3 00 00        JP      $0000               ; {} Command 0 ... restart
0043: FE 17           CP      $17                 ; Invalid command?
0045: 30 3B           JR      NC,$82              ; {} Greater than $16 ... ignore it
0047: FD BE 03        CP      (IY+$03)            
004A: 28 36           JR      Z,$82               ; {}
004C: 4F              LD      C,A                 
004D: CB 21           SLA     C                   
004F: 06 00           LD      B,$00               
0051: 21 C0 11        LD      HL,$11C0            
0054: 09              ADD     HL,BC               
0055: 09              ADD     HL,BC               
0056: EB              EX      DE,HL               
0057: 21 4A 02        LD      HL,$024A            
005A: 09              ADD     HL,BC               
005B: 09              ADD     HL,BC               
005C: 01 04 00        LD      BC,$0004            
005F: ED B0           LDIR                        
0061: 2B              DEC     HL                  
0062: 56              LD      D,(HL)              
0063: 2B              DEC     HL                  
0064: 18 16           JR      $7C                 ; {}
0066: F5              PUSH    AF                  
0067: E5              PUSH    HL                  
0068: 21 00 00        LD      HL,$0000            
006B: 39              ADD     HL,SP               
006C: 3E 13           LD      A,$13               
006E: BC              CP      H                   
006F: 20 FE           JR      NZ,$6F              ; {}
0071: E1              POP     HL                  
0072: 3A 00 10        LD      A,($1000)           ; {ram.m1000}
0075: 3C              INC     A                   
0076: 32 00 10        LD      ($1000),A           ; {ram.m1000}
0079: F1              POP     AF                  
007A: ED 45           RETN                        
007C: 5E              LD      E,(HL)              
007D: 3E 00           LD      A,$00               
007F: 12              LD      (DE),A              
0080: 13              INC     DE                  
0081: 12              LD      (DE),A              
0082: D9              EXX                         ; Restore registers
0083: 08              EX      AF,AF'              ; Restore flags and A
0084: FB              EI                          ; Interrupts back on
0085: ED 4D           RETI                        ; Return from interrupt

; Initialization continues here
0087: FD 36 17 3F     LD      (IY+$17),$3F        
008B: FD 36 27 3F     LD      (IY+$27),$3F        
008F: FB              EI                          ; Now taking commands from main board

; Main loop
0090: 3A 00 10        LD      A,($1000)           ; {ram.m1000}
0093: FD BE 01        CP      (IY+$01)            
0096: 28 F8           JR      Z,$90               ; {}
0098: 32 01 10        LD      ($1001),A           ; {ram.m1001}
009B: 06 17           LD      B,$17               
009D: 21 C1 11        LD      HL,$11C1            
00A0: FD 36 03 18     LD      (IY+$03),$18        
00A4: FD 36 02 00     LD      (IY+$02),$00        
00A8: CB 7E           BIT     7,(HL)              
00AA: CC E7 00        CALL    Z,$00E7             ; {}
00AD: 23              INC     HL                  
00AE: 23              INC     HL                  
00AF: 23              INC     HL                  
00B0: 23              INC     HL                  
00B1: FD 34 02        INC     (IY+$02)            ; 
00B4: 10 F2           DJNZ    $A8                 ; {}
;
; Copy RAM mirror to AY registers (if needed). Note that this mirror does not allow
; for re-writing a value to an AY register in case there is a write-trigger on the
; register.
;            
00B6: 06 20           LD      B,$20               ; 16 registers per chip, 2 chips
00B8: 0E 00           LD      C,$00               ; MSB of counter is 0
00BA: DD 21 10 10     LD      IX,$1010            ; NEW and CURRENT values of registers mirrored in memory
;
00BE: DD 7E 00        LD      A,(IX+$00)          ; Get the requested value
00C1: DD BE 20        CP      (IX+$20)            ; Is it the same as the current value?
00C4: 28 19           JR      Z,$DF               ; {} Yes ... nothing to do
00C6: DD 77 20        LD      (IX+$20),A          ; This is now the current value
00C9: 79              LD      A,C                 ; Register number
00CA: E6 0F           AND     $0F                 ; Each chip has 0-F
00CC: B9              CP      C                   ; 0-F ... 1st chip?
00CD: 20 09           JR      NZ,$D8              ; {} No ... send to 2nd chip
00CF: D3 00           OUT     ($00),A             ; {hard.AY0ADDRESS} Write the register address (chip 1)
00D1: DD 7E 20        LD      A,(IX+$20)          ; Write ...
00D4: D3 01           OUT     ($01),A             ; {hard.AY0VALUE} ... the value (chip 1)
00D6: 18 07           JR      $DF                 ; {} Skip 2nd chip logic
;
00D8: D3 02           OUT     ($02),A             ; {hard.AY1ADDRESS} Write the register address (chip 2)
00DA: DD 7E 20        LD      A,(IX+$20)          ; Write ...
00DD: D3 03           OUT     ($03),A             ; {hard.AY1VALUE} ... the value (chip 2)
;
00DF: 0C              INC     C                   ; Next register
00E0: DD 23           INC     IX                  ; Next pointer in memory
00E2: 10 DA           DJNZ    $BE                 ; {} Do all registers
00E4: C3 90 00        JP      $0090               ; {} Back to main loop


00E7: C5              PUSH    BC                  
00E8: E5              PUSH    HL                  
00E9: F3              DI                          
00EA: 3A 02 10        LD      A,($1002)           ; {ram.m1002}
00ED: 32 03 10        LD      ($1003),A           ; {ram.m1003}
00F0: 2B              DEC     HL                  
00F1: 5E              LD      E,(HL)              
00F2: 23              INC     HL                  
00F3: 56              LD      D,(HL)              
00F4: CB FE           SET     7,(HL)              
00F6: E5              PUSH    HL                  
00F7: 23              INC     HL                  
00F8: 4E              LD      C,(HL)              
00F9: 23              INC     HL                  
00FA: 46              LD      B,(HL)              
00FB: FB              EI                          
00FC: 0A              LD      A,(BC)              
00FD: B7              OR      A                   
00FE: EB              EX      DE,HL               
00FF: 28 08           JR      Z,$109              ; {}
0101: 3D              DEC     A                   
0102: 02              LD      (BC),A              
0103: C2 36 02        JP      NZ,$0236            ; {}
0106: 18 01           JR      $109                ; {}
0108: 23              INC     HL                  
0109: 7E              LD      A,(HL)              
010A: FE F0           CP      $F0                 
010C: D2 81 01        JP      NC,$0181            ; {}
010F: DD 21 10 10     LD      IX,$1010            ; AY Register mirror
0113: E6 1F           AND     $1F                 ; Only 32 registers
0115: 5F              LD      E,A                 ; Register ...
0116: 16 00           LD      D,$00               ; ... to DE
0118: DD 19           ADD     IX,DE               ; Offset IX to register mirror
011A: 7E              LD      A,(HL)              
011B: 23              INC     HL                  
011C: E6 E0           AND     $E0                 
011E: FE 00           CP      $00                 
0120: 28 17           JR      Z,$139              ; {}
0122: FE 20           CP      $20                 
0124: 28 24           JR      Z,$14A              ; {}
0126: FE 40           CP      $40                 
0128: 28 2B           JR      Z,$155              ; {}
012A: FE 60           CP      $60                 
012C: 28 30           JR      Z,$15E              ; {}
012E: FE 80           CP      $80                 
0130: 28 35           JR      Z,$167              ; {}
0132: FE A0           CP      $A0                 
0134: 28 3A           JR      Z,$170              ; {}
0136: C3 35 02        JP      $0235               ; {}
0139: 7E              LD      A,(HL)              
013A: DD 77 00        LD      (IX+$00),A          
013D: 7B              LD      A,E                 
013E: E6 0F           AND     $0F                 
0140: FE 0D           CP      $0D                 
0142: 20 C4           JR      NZ,$108             ; {}
0144: DD 36 20 FF     LD      (IX+$20),$FF        
0148: 18 BE           JR      $108                ; {}
014A: 7E              LD      A,(HL)              
014B: DD 77 00        LD      (IX+$00),A          
014E: 23              INC     HL                  
014F: 7E              LD      A,(HL)              
0150: DD 77 01        LD      (IX+$01),A          
0153: 18 B3           JR      $108                ; {}
0155: 7E              LD      A,(HL)              
0156: DD B6 00        OR      (IX+$00)            
0159: DD 77 00        LD      (IX+$00),A          
015C: 18 AA           JR      $108                ; {}
015E: DD 7E 00        LD      A,(IX+$00)          
0161: A6              AND     (HL)                
0162: DD 77 00        LD      (IX+$00),A          
0165: 18 A1           JR      $108                ; {}
0167: DD 7E 00        LD      A,(IX+$00)          
016A: 86              ADD     A,(HL)              
016B: DD 77 00        LD      (IX+$00),A          
016E: 18 98           JR      $108                ; {}
0170: DD 7E 00        LD      A,(IX+$00)          
0173: 86              ADD     A,(HL)              
0174: DD 77 00        LD      (IX+$00),A          
0177: 23              INC     HL                  
0178: DD 7E 01        LD      A,(IX+$01)          
017B: 8E              ADC     A,(HL)              
017C: DD 77 01        LD      (IX+$01),A          
017F: 18 87           JR      $108                ; {}
0181: 23              INC     HL                  
0182: FE F1           CP      $F1                 
0184: 28 19           JR      Z,$19F              ; {}
0186: FE F2           CP      $F2                 
0188: 28 1A           JR      Z,$1A4              ; {}
018A: FE F3           CP      $F3                 
018C: 28 35           JR      Z,$1C3              ; {}
018E: FE F4           CP      $F4                 
0190: 28 61           JR      Z,$1F3              ; {}
0192: FE F5           CP      $F5                 
0194: CA 19 02        JP      Z,$0219             ; {}
0197: FE F6           CP      $F6                 
0199: CA 2A 02        JP      Z,$022A             ; {}
019C: C3 31 02        JP      $0231               ; {}
019F: 7E              LD      A,(HL)              
01A0: 02              LD      (BC),A              
01A1: C3 35 02        JP      $0235               ; {}
01A4: C5              PUSH    BC                  
01A5: 03              INC     BC                  
01A6: 0A              LD      A,(BC)              
01A7: 3C              INC     A                   
01A8: 02              LD      (BC),A              
01A9: 03              INC     BC                  
01AA: 3D              DEC     A                   
01AB: 28 06           JR      Z,$1B3              ; {}
01AD: 03              INC     BC                  
01AE: 03              INC     BC                  
01AF: 03              INC     BC                  
01B0: 03              INC     BC                  
01B1: 18 F7           JR      $1AA                ; {}
01B3: 7E              LD      A,(HL)              
01B4: 02              LD      (BC),A              
01B5: 23              INC     HL                  
01B6: 03              INC     BC                  
01B7: 7E              LD      A,(HL)              
01B8: 02              LD      (BC),A              
01B9: 03              INC     BC                  
01BA: 7D              LD      A,L                 
01BB: 02              LD      (BC),A              
01BC: 03              INC     BC                  
01BD: 7C              LD      A,H                 
01BE: 02              LD      (BC),A              
01BF: C1              POP     BC                  
01C0: C3 08 01        JP      $0108               ; {}
01C3: C5              PUSH    BC                  
01C4: 03              INC     BC                  
01C5: 0A              LD      A,(BC)              
01C6: 03              INC     BC                  
01C7: 3D              DEC     A                   
01C8: 28 06           JR      Z,$1D0              ; {}
01CA: 03              INC     BC                  
01CB: 03              INC     BC                  
01CC: 03              INC     BC                  
01CD: 03              INC     BC                  
01CE: 18 F7           JR      $1C7                ; {}
01D0: 0A              LD      A,(BC)              
01D1: 03              INC     BC                  
01D2: 5F              LD      E,A                 
01D3: 0A              LD      A,(BC)              
01D4: 57              LD      D,A                 
01D5: 1B              DEC     DE                  
01D6: 7A              LD      A,D                 
01D7: 02              LD      (BC),A              
01D8: 0B              DEC     BC                  
01D9: 7B              LD      A,E                 
01DA: 02              LD      (BC),A              
01DB: B2              OR      D                   
01DC: 28 0B           JR      Z,$1E9              ; {}
01DE: 03              INC     BC                  
01DF: 03              INC     BC                  
01E0: 0A              LD      A,(BC)              
01E1: 6F              LD      L,A                 
01E2: 03              INC     BC                  
01E3: 0A              LD      A,(BC)              
01E4: 67              LD      H,A                 
01E5: C1              POP     BC                  
01E6: C3 08 01        JP      $0108               ; {}
01E9: 2B              DEC     HL                  
01EA: C1              POP     BC                  
01EB: 03              INC     BC                  
01EC: 0A              LD      A,(BC)              
01ED: 3D              DEC     A                   
01EE: 02              LD      (BC),A              
01EF: 0B              DEC     BC                  
01F0: C3 08 01        JP      $0108               ; {}
01F3: 7E              LD      A,(HL)              
01F4: C5              PUSH    BC                  
01F5: E5              PUSH    HL                  
01F6: 4F              LD      C,A                 
01F7: CB 21           SLA     C                   
01F9: 06 00           LD      B,$00               
01FB: 21 C0 11        LD      HL,$11C0            
01FE: 09              ADD     HL,BC               
01FF: 09              ADD     HL,BC               
0200: EB              EX      DE,HL               
0201: 21 4A 02        LD      HL,$024A            
0204: 09              ADD     HL,BC               
0205: 09              ADD     HL,BC               
0206: 01 04 00        LD      BC,$0004            
0209: ED B0           LDIR                        
020B: 2B              DEC     HL                  
020C: 56              LD      D,(HL)              
020D: 2B              DEC     HL                  
020E: 5E              LD      E,(HL)              
020F: 3E 00           LD      A,$00               
0211: 12              LD      (DE),A              
0212: 13              INC     DE                  
0213: 12              LD      (DE),A              
0214: E1              POP     HL                  
0215: C1              POP     BC                  
0216: C3 08 01        JP      $0108               ; {}
0219: 5E              LD      E,(HL)              
021A: E5              PUSH    HL                  
021B: CB 23           SLA     E                   
021D: 16 00           LD      D,$00               
021F: 21 C1 11        LD      HL,$11C1            
0222: 19              ADD     HL,DE               
0223: 19              ADD     HL,DE               
0224: CB FE           SET     7,(HL)              
0226: E1              POP     HL                  
0227: C3 08 01        JP      $0108               ; {}
022A: 5E              LD      E,(HL)              
022B: 23              INC     HL                  
022C: 56              LD      D,(HL)              
022D: 19              ADD     HL,DE               
022E: C3 08 01        JP      $0108               ; {}
0231: CB FC           SET     7,H                 
0233: 18 00           JR      $235                ; {}
0235: 23              INC     HL                  
0236: D1              POP     DE                  
0237: 1A              LD      A,(DE)              
0238: CB 7F           BIT     7,A                 
023A: 28 07           JR      Z,$243              ; {}
023C: 7C              LD      A,H                 
023D: F3              DI                          
023E: 12              LD      (DE),A              
023F: 1B              DEC     DE                  
0240: 7D              LD      A,L                 
0241: 12              LD      (DE),A              
0242: FB              EI                          
0243: FD 36 03 18     LD      (IY+$03),$18        
0247: E1              POP     HL                  
0248: C1              POP     BC                  
0249: C9              RET                         
024A: B4              OR      H                   
024B: 07              RLCA                        
024C: 70              LD      (HL),B              
024D: 10 59           DJNZ    $2A8                ; {}
024F: 07              RLCA                        
0250: 80              ADD     A,B                 
0251: 10 67           DJNZ    $2BA                ; {}
0253: 04              INC     B                   
0254: 90              SUB     B                   
0255: 10 46           DJNZ    $29D                ; {}
0257: 04              INC     B                   
0258: A0              AND     B                   
0259: 10 49           DJNZ    $2A4                ; {}
025B: 05              DEC     B                   
025C: B0              OR      B                   
025D: 10 59           DJNZ    $2B8                ; {}
025F: 06 C0           LD      B,$C0               
0261: 10 A7           DJNZ    $20A                ; {}
0263: 06 D0           LD      B,$D0               
0265: 10 2E           DJNZ    $295                ; {}
0267: 07              RLCA                        
0268: E0              RET     PO                  
0269: 10 F7           DJNZ    $262                ; {}
026B: 04              INC     B                   
026C: F0              RET     P                   
026D: 10 28           DJNZ    $297                ; {}
026F: 04              INC     B                   
0270: 00              NOP                         
0271: 11 3F 04        LD      DE,$043F            
0274: 10 11           DJNZ    $287                ; {}
0276: E6 02           AND     $02                 
0278: 20 11           JR      NZ,$28B             ; {}
027A: 28 03           JR      Z,$27F              ; {}
027C: 30 11           JR      NC,$28F             ; {}
027E: 6A              LD      L,D                 
027F: 03              INC     BC                  
0280: 40              LD      B,B                 
0281: 11 AC 03        LD      DE,$03AC            
0284: 50              LD      D,B                 
0285: 11 EE 03        LD      DE,$03EE            
0288: 60              LD      H,B                 
0289: 11 8F 04        LD      DE,$048F            
028C: 70              LD      (HL),B              
028D: 11 B5 04        LD      DE,$04B5            
0290: 80              ADD     A,B                 
0291: 11 CE 04        LD      DE,$04CE            
0294: 90              SUB     B                   
0295: 11 2A 05        LD      DE,$052A            
0298: A0              AND     B                   
0299: 11 12 05        LD      DE,$0512            
029C: B0              OR      B                   
029D: 11 D1 02        LD      DE,$02D1            
02A0: 60              LD      H,B                 
02A1: 10 A6           DJNZ    $249                ; {}
02A3: 02              LD      (BC),A              
02A4: 50              LD      D,B                 
02A5: 10 67           DJNZ    $30E                ; {}
02A7: FE 20           CP      $20                 
02A9: 33              INC     SP                  
02AA: 00              NOP                         
02AB: 08              EX      AF,AF'              
02AC: 0F              RRCA                        
02AD: F2 F4 01        JP      P,$01F4             ; {}
02B0: A0              AND     B                   
02B1: 01 00 F1        LD      BC,$F100            
02B4: 00              NOP                         
02B5: F3              DI                          
02B6: 47              LD      B,A                 
02B7: 01 F1 63        LD      BC,$63F1            
02BA: 77              LD      (HL),A              
02BB: FE 30           CP      $30                 
02BD: 33              INC     SP                  
02BE: 00              NOP                         
02BF: 18 0F           JR      $2D0                ; {}
02C1: F2 F4 01        JP      P,$01F4             ; {}
02C4: B0              OR      B                   
02C5: 01 00 F1        LD      BC,$F100            
02C8: 00              NOP                         
02C9: F3              DI                          
02CA: 57              LD      D,A                 
02CB: 01 F1 63        LD      BC,$63F1            
02CE: F6 D5           OR      $D5                 
02D0: FF              RST     0X38                
02D1: F5              PUSH    AF                  
02D2: 10 F5           DJNZ    $2C9                ; {}
02D4: 02              LD      (BC),A              
02D5: F1              POP     AF                  
02D6: 09              ADD     HL,BC               
02D7: F2 04 00        JP      P,$0004             ; {}
02DA: F4 10 F1        CALL    P,$F110             ; 
02DD: 1E F5           LD      E,$F5               
02DF: 10 F1           DJNZ    $2D2                ; {}
02E1: 08              EX      AF,AF'              
02E2: F3              DI                          
02E3: F4 10 FF        CALL    P,$FF10             ; 
02E6: F5              PUSH    AF                  
02E7: 0C              INC     C                   
02E8: F5              PUSH    AF                  
02E9: 0D              DEC     C                   
02EA: F5              PUSH    AF                  
02EB: 0E F5           LD      C,$F5               
02ED: 0F              RRCA                        
02EE: 77              LD      (HL),A              
02EF: FE 30           CP      $30                 
02F1: F6 02           OR      $02                 
02F3: 18 0B           JR      $300                ; {}
02F5: F1              POP     AF                  
02F6: 14              INC     D                   
02F7: 18 00           JR      $2F9                ; {}
02F9: F1              POP     AF                  
02FA: 02              LD      (BC),A              
02FB: F1              POP     AF                  
02FC: 7F              LD      A,A                 
02FD: 30 7E           JR      NC,$37D             ; {}
02FF: 02              LD      (BC),A              
0300: 18 0C           JR      $30E                ; {}
0302: F1              POP     AF                  
0303: 14              INC     D                   
0304: 18 00           JR      $306                ; {}
0306: F1              POP     AF                  
0307: 02              LD      (BC),A              
0308: F1              POP     AF                  
0309: 7F              LD      A,A                 
030A: 30 5A           JR      NC,$366             ; {}
030C: 02              LD      (BC),A              
030D: 18 0D           JR      $31C                ; {}
030F: F1              POP     AF                  
0310: 14              INC     D                   
0311: 18 00           JR      $313                ; {}
0313: F1              POP     AF                  
0314: 02              LD      (BC),A              
0315: F1              POP     AF                  
0316: 7F              LD      A,A                 
0317: 30 7E           JR      NC,$397             ; {}
0319: 02              LD      (BC),A              
031A: 18 0C           JR      $328                ; {}
031C: F1              POP     AF                  
031D: 14              INC     D                   
031E: 18 00           JR      $320                ; {}
0320: F1              POP     AF                  
0321: 02              LD      (BC),A              
0322: F1              POP     AF                  
0323: 7F              LD      A,A                 
0324: F6 C7           OR      $C7                 
0326: FF              RST     0X38                
0327: FF              RST     0X38                
0328: F5              PUSH    AF                  
0329: 0B              DEC     BC                  
032A: F5              PUSH    AF                  
032B: 0D              DEC     C                   
032C: F5              PUSH    AF                  
032D: 0E F5           LD      C,$F5               
032F: 0F              RRCA                        
0330: 77              LD      (HL),A              
0331: FE 30           CP      $30                 
0333: F6 02           OR      $02                 
0335: 18 0B           JR      $342                ; {}
0337: F1              POP     AF                  
0338: 14              INC     D                   
0339: 18 00           JR      $33B                ; {}
033B: F1              POP     AF                  
033C: 02              LD      (BC),A              
033D: F1              POP     AF                  
033E: 5F              LD      E,A                 
033F: 30 7E           JR      NC,$3BF             ; {}
0341: 02              LD      (BC),A              
0342: 18 0C           JR      $350                ; {}
0344: F1              POP     AF                  
0345: 14              INC     D                   
0346: 18 00           JR      $348                ; {}
0348: F1              POP     AF                  
0349: 02              LD      (BC),A              
034A: F1              POP     AF                  
034B: 5F              LD      E,A                 
034C: 30 5A           JR      NC,$3A8             ; {}
034E: 02              LD      (BC),A              
034F: 18 0D           JR      $35E                ; {}
0351: F1              POP     AF                  
0352: 14              INC     D                   
0353: 18 00           JR      $355                ; {}
0355: F1              POP     AF                  
0356: 02              LD      (BC),A              
0357: F1              POP     AF                  
0358: 5F              LD      E,A                 
0359: 30 7E           JR      NC,$3D9             ; {}
035B: 02              LD      (BC),A              
035C: 18 0C           JR      $36A                ; {}
035E: F1              POP     AF                  
035F: 14              INC     D                   
0360: 18 00           JR      $362                ; {}
0362: F1              POP     AF                  
0363: 02              LD      (BC),A              
0364: F1              POP     AF                  
0365: 5F              LD      E,A                 
0366: F6 C7           OR      $C7                 
0368: FF              RST     0X38                
0369: FF              RST     0X38                
036A: F5              PUSH    AF                  
036B: 0C              INC     C                   
036C: F5              PUSH    AF                  
036D: 0B              DEC     BC                  
036E: F5              PUSH    AF                  
036F: 0E F5           LD      C,$F5               
0371: 0F              RRCA                        
0372: 77              LD      (HL),A              
0373: FE 30           CP      $30                 
0375: F6 02           OR      $02                 
0377: 18 0C           JR      $385                ; {}
0379: F1              POP     AF                  
037A: 14              INC     D                   
037B: 18 00           JR      $37D                ; {}
037D: F1              POP     AF                  
037E: 02              LD      (BC),A              
037F: F1              POP     AF                  
0380: 2F              CPL                         
0381: 30 7E           JR      NC,$401             ; {}
0383: 02              LD      (BC),A              
0384: 18 0D           JR      $393                ; {}
0386: F1              POP     AF                  
0387: 14              INC     D                   
0388: 18 00           JR      $38A                ; {}
038A: F1              POP     AF                  
038B: 02              LD      (BC),A              
038C: F1              POP     AF                  
038D: 2F              CPL                         
038E: 30 5A           JR      NC,$3EA             ; {}
0390: 02              LD      (BC),A              
0391: 18 0E           JR      $3A1                ; {}
0393: F1              POP     AF                  
0394: 14              INC     D                   
0395: 18 00           JR      $397                ; {}
0397: F1              POP     AF                  
0398: 02              LD      (BC),A              
0399: F1              POP     AF                  
039A: 2F              CPL                         
039B: 30 7E           JR      NC,$41B             ; {}
039D: 02              LD      (BC),A              
039E: 18 0D           JR      $3AD                ; {}
03A0: F1              POP     AF                  
03A1: 14              INC     D                   
03A2: 18 00           JR      $3A4                ; {}
03A4: F1              POP     AF                  
03A5: 02              LD      (BC),A              
03A6: F1              POP     AF                  
03A7: 2F              CPL                         
03A8: F6 C7           OR      $C7                 
03AA: FF              RST     0X38                
03AB: FF              RST     0X38                
03AC: F5              PUSH    AF                  
03AD: 0D              DEC     C                   
03AE: F5              PUSH    AF                  
03AF: 0B              DEC     BC                  
03B0: F5              PUSH    AF                  
03B1: 0C              INC     C                   
03B2: F5              PUSH    AF                  
03B3: 0F              RRCA                        
03B4: 77              LD      (HL),A              
03B5: FE 30           CP      $30                 
03B7: F6 02           OR      $02                 
03B9: 18 0C           JR      $3C7                ; {}
03BB: F1              POP     AF                  
03BC: 14              INC     D                   
03BD: 18 00           JR      $3BF                ; {}
03BF: F1              POP     AF                  
03C0: 02              LD      (BC),A              
03C1: F1              POP     AF                  
03C2: 17              RLA                         
03C3: 30 7E           JR      NC,$443             ; {}
03C5: 02              LD      (BC),A              
03C6: 18 0D           JR      $3D5                ; {}
03C8: F1              POP     AF                  
03C9: 14              INC     D                   
03CA: 18 00           JR      $3CC                ; {}
03CC: F1              POP     AF                  
03CD: 02              LD      (BC),A              
03CE: F1              POP     AF                  
03CF: 19              ADD     HL,DE               
03D0: 30 5A           JR      NC,$42C             ; {}
03D2: 02              LD      (BC),A              
03D3: 18 0E           JR      $3E3                ; {}
03D5: F1              POP     AF                  
03D6: 14              INC     D                   
03D7: 18 00           JR      $3D9                ; {}
03D9: F1              POP     AF                  
03DA: 02              LD      (BC),A              
03DB: F1              POP     AF                  
03DC: 17              RLA                         
03DD: 30 7E           JR      NC,$45D             ; {}
03DF: 02              LD      (BC),A              
03E0: 18 0D           JR      $3EF                ; {}
03E2: F1              POP     AF                  
03E3: 14              INC     D                   
03E4: 18 00           JR      $3E6                ; {}
03E6: F1              POP     AF                  
03E7: 02              LD      (BC),A              
03E8: F1              POP     AF                  
03E9: 17              RLA                         
03EA: F6 C7           OR      $C7                 
03EC: FF              RST     0X38                
03ED: FF              RST     0X38                
03EE: F5              PUSH    AF                  
03EF: 0E F5           LD      C,$F5               
03F1: 0B              DEC     BC                  
03F2: F5              PUSH    AF                  
03F3: 0C              INC     C                   
03F4: F5              PUSH    AF                  
03F5: 0D              DEC     C                   
03F6: 77              LD      (HL),A              
03F7: FE 30           CP      $30                 
03F9: A6              AND     (HL)                
03FA: 02              LD      (BC),A              
03FB: 18 0D           JR      $40A                ; {}
03FD: F1              POP     AF                  
03FE: 14              INC     D                   
03FF: 18 00           JR      $401                ; {}
0401: F1              POP     AF                  
0402: 02              LD      (BC),A              
0403: 30 1E           JR      NC,$423             ; {}
0405: 02              LD      (BC),A              
0406: 18 0E           JR      $416                ; {}
0408: F1              POP     AF                  
0409: 14              INC     D                   
040A: 18 00           JR      $40C                ; {}
040C: F1              POP     AF                  
040D: 02              LD      (BC),A              
040E: 30 FA           JR      NC,$40A             ; {}
0410: 01 18 0F        LD      BC,$0F18            
0413: F1              POP     AF                  
0414: 14              INC     D                   
0415: 18 00           JR      $417                ; {}
0417: F1              POP     AF                  
0418: 02              LD      (BC),A              
0419: 30 7E           JR      NC,$499             ; {}
041B: 02              LD      (BC),A              
041C: 18 0E           JR      $42C                ; {}
041E: F1              POP     AF                  
041F: 14              INC     D                   
0420: 18 00           JR      $422                ; {}
0422: F1              POP     AF                  
0423: 02              LD      (BC),A              
0424: F6 CF           OR      $CF                 
0426: FF              RST     0X38                
0427: FF              RST     0X38                
0428: 1A              LD      A,(DE)              
0429: 0F              RRCA                        
042A: F2 07 00        JP      P,$0007             ; {}
042D: 16 1F           LD      D,$1F               
042F: 77              LD      (HL),A              
0430: DF              RST     0X18                
0431: 9A              SBC     D                   
0432: FF              RST     0X38                
0433: F1              POP     AF                  
0434: 02              LD      (BC),A              
0435: F3              DI                          
0436: F2 0A 00        JP      P,$000A             ; {}
0439: 96              SUB     (HL)                
043A: FD
043B: F1              POP     AF                  
043C: 03              INC     BC                  
043D: F3              DI                          
043E: FF              RST     0X38                
043F: F5              PUSH    AF                  
0440: 09              ADD     HL,BC               
0441: 1A              LD      A,(DE)              
0442: 00              NOP                         
0443: 57              LD      D,A                 
0444: 20 FF           JR      NZ,$445             ; {}
0446: F5              PUSH    AF                  
0447: 11 32 50        LD      DE,$5032            
044A: 00              NOP                         
044B: 19              ADD     HL,DE               
044C: 0F              RRCA                        
044D: F2 06 00        JP      P,$0006             ; {}
0450: F2 02 00        JP      P,$0002             ; {}
0453: 57              LD      D,A                 
0454: 10 77           DJNZ    $4CD                ; {}
0456: FD
0457: 99              SBC     C                   
0458: FF              RST     0X38                
0459: F1              POP     AF                  
045A: 06 F3           LD      B,$F3               
045C: B2              OR      D                   
045D: F0              RET     P                   
045E: FF              RST     0X38                
045F: F3              DI                          
0460: 57              LD      D,A                 
0461: 02              LD      (BC),A              
0462: 12              LD      (DE),A              
0463: 00              NOP                         
0464: 19              ADD     HL,DE               
0465: 00              NOP                         
0466: FF              RST     0X38                
0467: F5              PUSH    AF                  
0468: 10 F5           DJNZ    $45F                ; {}
046A: 15              DEC     D                   
046B: 22 38 02        LD      ($0238),HL          ; {}
046E: 09              ADD     HL,BC               
046F: 0F              RRCA                        
0470: F2 07 00        JP      P,$0007             ; {}
0473: F2 06 00        JP      P,$0006             ; {}
0476: 67              LD      H,A                 
0477: FD
0478: A2              AND     D                   
0479: F0              RET     P                   
047A: FF              RST     0X38                
047B: F1              POP     AF                  
047C: 02              LD      (BC),A              
047D: F3              DI                          
047E: F2 06 00        JP      P,$0006             ; {}
0481: A2              AND     D                   
0482: 10 00           DJNZ    $484                ; {}
0484: F1              POP     AF                  
0485: 02              LD      (BC),A              
0486: F3              DI                          
0487: 89              ADC     A,C                 
0488: FE F3           CP      $F3                 
048A: 47              LD      B,A                 
048B: 02              LD      (BC),A              
048C: 09              ADD     HL,BC               
048D: 00              NOP                         
048E: FF              RST     0X38                
048F: F5              PUSH    AF                  
0490: 02              LD      (BC),A              
0491: 22 6F 00        LD      ($006F),HL          ; {}
0494: 09              ADD     HL,BC               
0495: 0F              RRCA                        
0496: F2 07 00        JP      P,$0007             ; {}
0499: F2 06 00        JP      P,$0006             ; {}
049C: 67              LD      H,A                 
049D: FD
049E: A2              AND     D                   
049F: F0              RET     P                   
04A0: FF              RST     0X38                
04A1: F1              POP     AF                  
04A2: 02              LD      (BC),A              
04A3: F3              DI                          
04A4: F2 06 00        JP      P,$0006             ; {}
04A7: A2              AND     D                   
04A8: 10 00           DJNZ    $4AA                ; {}
04AA: F1              POP     AF                  
04AB: 02              LD      (BC),A              
04AC: F3              DI                          
04AD: 89              ADC     A,C                 
04AE: FE F3           CP      $F3                 
04B0: 47              LD      B,A                 
04B1: 02              LD      (BC),A              
04B2: 09              ADD     HL,BC               
04B3: 00              NOP                         
04B4: FF              RST     0X38                
04B5: F5              PUSH    AF                  
04B6: 03              INC     BC                  
04B7: 16 00           LD      D,$00               
04B9: 57              LD      D,A                 
04BA: 02              LD      (BC),A              
04BB: 77              LD      (HL),A              
04BC: EF              RST     0X28                
04BD: 19              ADD     HL,DE               
04BE: 00              NOP                         
04BF: F2 0F 00        JP      P,$000F             ; {}
04C2: 96              SUB     (HL)                
04C3: FE 99           CP      $99                 
04C5: 01 F1 04        LD      BC,$04F1            
04C8: F3              DI                          
04C9: 19              ADD     HL,DE               
04CA: 00              NOP                         
04CB: 57              LD      D,A                 
04CC: 10 FF           DJNZ    $4CD                ; {}
04CE: F5              PUSH    AF                  
04CF: 07              RLCA                        
04D0: 67              LD      H,A                 
04D1: FE 20           CP      $20                 
04D3: EF              RST     0X28                
04D4: 00              NOP                         
04D5: 08              EX      AF,AF'              
04D6: 0B              DEC     BC                  
04D7: F1              POP     AF                  
04D8: 11 20 5F        LD      DE,$5F20            
04DB: 00              NOP                         
04DC: F1              POP     AF                  
04DD: 11 20 7F        LD      DE,$7F20            
04E0: 00              NOP                         
04E1: F1              POP     AF                  
04E2: 11 20 47        LD      DE,$4720            
04E5: 00              NOP                         
04E6: F1              POP     AF                  
04E7: 11 20 BE        LD      DE,$BE20            
04EA: 00              NOP                         
04EB: F1              POP     AF                  
04EC: 11 20 77        LD      DE,$7720            
04EF: 00              NOP                         
04F0: F1              POP     AF                  
04F1: 11 08 00        LD      DE,$0008            
04F4: 47              LD      B,A                 
04F5: 01 FF 24        LD      BC,$24FF            
04F8: 00              NOP                         
04F9: 01 0A 0D        LD      BC,$0D0A            
04FC: 67              LD      H,A                 
04FD: FB              EI                          
04FE: F2 06 00        JP      P,$0006             ; {}
0501: F2 01 00        JP      P,$0001             ; {}
0504: 8A              ADC     A,D                 
0505: FF              RST     0X38                
0506: F1              POP     AF                  
0507: 07              RLCA                        
0508: F3              DI                          
0509: A4              AND     H                   
050A: F0              RET     P                   
050B: FF              RST     0X38                
050C: F3              DI                          
050D: 47              LD      B,A                 
050E: 04              INC     B                   
050F: 0A              LD      A,(BC)              
0510: 00              NOP                         
0511: FF              RST     0X38                
0512: F4 00 F1        CALL    P,$F100             ; 
0515: 05              DEC     B                   
0516: 30 3F           JR      NC,$557             ; {}
0518: 00              NOP                         
0519: 77              LD      (HL),A              
051A: FE F2           CP      $F2                 
051C: 10 00           DJNZ    $51E                ; {}
051E: 18 0F           JR      $52F                ; {}
0520: F1              POP     AF                  
0521: 10 18           DJNZ    $53B                ; {}
0523: 00              NOP                         
0524: F1              POP     AF                  
0525: 0A              LD      A,(BC)              
0526: F3              DI                          
0527: 57              LD      D,A                 
0528: 01 FF F4        LD      BC,$F4FF            
052B: 00              NOP                         
052C: F1              POP     AF                  
052D: 01 F2 08        LD      BC,$08F2            
0530: 00              NOP                         
0531: 20 7F           JR      NZ,$5B2             ; {}
0533: 00              NOP                         
0534: F2 3C 00        JP      P,$003C             ; {}
0537: 67              LD      H,A                 
0538: FE 08           CP      $08                 
053A: 0F              RRCA                        
053B: A0              AND     B                   
053C: FF              RST     0X38                
053D: FF              RST     0X38                
053E: F1              POP     AF                  
053F: 01 F3 F1        LD      BC,$F1F3            
0542: 09              ADD     HL,BC               
0543: F3              DI                          
0544: 47              LD      B,A                 
0545: 01 08 00        LD      BC,$0008            
0548: FF              RST     0X38                
0549: F5              PUSH    AF                  
054A: 14              INC     D                   
054B: 67              LD      H,A                 
054C: FD
054D: 67              LD      H,A                 
054E: FB              EI                          
054F: 77              LD      (HL),A              
0550: FE 30           CP      $30                 
0552: 47              LD      B,A                 
0553: 00              NOP                         
0554: 18 0A           JR      $560                ; {}
0556: F1              POP     AF                  
0557: 14              INC     D                   
0558: 18 00           JR      $55A                ; {}
055A: F1              POP     AF                  
055B: 02              LD      (BC),A              
055C: 30 43           JR      NC,$5A1             ; {}
055E: 00              NOP                         
055F: 18 0A           JR      $56B                ; {}
0561: F1              POP     AF                  
0562: 14              INC     D                   
0563: 18 00           JR      $565                ; {}
0565: F1              POP     AF                  
0566: 02              LD      (BC),A              
0567: 30 47           JR      NC,$5B0             ; {}
0569: 00              NOP                         
056A: 18 0A           JR      $576                ; {}
056C: F1              POP     AF                  
056D: 14              INC     D                   
056E: 18 00           JR      $570                ; {}
0570: F1              POP     AF                  
0571: 02              LD      (BC),A              
0572: 30 43           JR      NC,$5B7             ; {}
0574: 00              NOP                         
0575: 18 0A           JR      $581                ; {}
0577: F1              POP     AF                  
0578: 14              INC     D                   
0579: 18 00           JR      $57B                ; {}
057B: F1              POP     AF                  
057C: 02              LD      (BC),A              
057D: F4 05 F4        CALL    P,$F405             ; 
0580: 06 30           LD      B,$30               
0582: 3C              INC     A                   
0583: 00              NOP                         
0584: 18 0A           JR      $590                ; {}
0586: F1              POP     AF                  
0587: 44              LD      B,H                 
0588: 18 00           JR      $58A                ; {}
058A: F1              POP     AF                  
058B: 02              LD      (BC),A              
058C: 30 59           JR      NC,$5E7             ; {}
058E: 00              NOP                         
058F: 18 0A           JR      $59B                ; {}
0591: F1              POP     AF                  
0592: 8C              ADC     A,H                 
0593: 18 00           JR      $595                ; {}
0595: F1              POP     AF                  
0596: 02              LD      (BC),A              
0597: 30 47           JR      NC,$5E0             ; {}
0599: 00              NOP                         
059A: 18 0A           JR      $5A6                ; {}
059C: F1              POP     AF                  
059D: 14              INC     D                   
059E: 18 00           JR      $5A0                ; {}
05A0: F1              POP     AF                  
05A1: 02              LD      (BC),A              
05A2: 30 43           JR      NC,$5E7             ; {}
05A4: 00              NOP                         
05A5: 18 0A           JR      $5B1                ; {}
05A7: F1              POP     AF                  
05A8: 14              INC     D                   
05A9: 18 00           JR      $5AB                ; {}
05AB: F1              POP     AF                  
05AC: 02              LD      (BC),A              
05AD: 30 47           JR      NC,$5F6             ; {}
05AF: 00              NOP                         
05B0: 18 0A           JR      $5BC                ; {}
05B2: F1              POP     AF                  
05B3: 14              INC     D                   
05B4: 18 00           JR      $5B6                ; {}
05B6: F1              POP     AF                  
05B7: 02              LD      (BC),A              
05B8: 30 43           JR      NC,$5FD             ; {}
05BA: 00              NOP                         
05BB: 18 0A           JR      $5C7                ; {}
05BD: F1              POP     AF                  
05BE: 14              INC     D                   
05BF: 18 00           JR      $5C1                ; {}
05C1: F1              POP     AF                  
05C2: 02              LD      (BC),A              
05C3: 30 3C           JR      NC,$601             ; {}
05C5: 00              NOP                         
05C6: 18 0A           JR      $5D2                ; {}
05C8: F1              POP     AF                  
05C9: 44              LD      B,H                 
05CA: 18 00           JR      $5CC                ; {}
05CC: F1              POP     AF                  
05CD: 02              LD      (BC),A              
05CE: 30 59           JR      NC,$629             ; {}
05D0: 00              NOP                         
05D1: 18 0A           JR      $5DD                ; {}
05D3: F1              POP     AF                  
05D4: 8C              ADC     A,H                 
05D5: 18 00           JR      $5D7                ; {}
05D7: F1              POP     AF                  
05D8: 02              LD      (BC),A              
05D9: 30 47           JR      NC,$622             ; {}
05DB: 00              NOP                         
05DC: 18 0A           JR      $5E8                ; {}
05DE: F1              POP     AF                  
05DF: 14              INC     D                   
05E0: 18 00           JR      $5E2                ; {}
05E2: F1              POP     AF                  
05E3: 02              LD      (BC),A              
05E4: 30 43           JR      NC,$629             ; {}
05E6: 00              NOP                         
05E7: 18 0A           JR      $5F3                ; {}
05E9: F1              POP     AF                  
05EA: 14              INC     D                   
05EB: 18 00           JR      $5ED                ; {}
05ED: F1              POP     AF                  
05EE: 02              LD      (BC),A              
05EF: 30 47           JR      NC,$638             ; {}
05F1: 00              NOP                         
05F2: 18 0A           JR      $5FE                ; {}
05F4: F1              POP     AF                  
05F5: 14              INC     D                   
05F6: 18 00           JR      $5F8                ; {}
05F8: F1              POP     AF                  
05F9: 02              LD      (BC),A              
05FA: 30 43           JR      NC,$63F             ; {}
05FC: 00              NOP                         
05FD: 18 0A           JR      $609                ; {}
05FF: F1              POP     AF                  
0600: 14              INC     D                   
0601: 18 00           JR      $603                ; {}
0603: F1              POP     AF                  
0604: 02              LD      (BC),A              
0605: 30 3C           JR      NC,$643             ; {}
0607: 00              NOP                         
0608: 18 0A           JR      $614                ; {}
060A: F1              POP     AF                  
060B: 44              LD      B,H                 
060C: 18 00           JR      $60E                ; {}
060E: F1              POP     AF                  
060F: 02              LD      (BC),A              
0610: 30 59           JR      NC,$66B             ; {}
0612: 00              NOP                         
0613: 18 0A           JR      $61F                ; {}
0615: F1              POP     AF                  
0616: 8C              ADC     A,H                 
0617: 18 00           JR      $619                ; {}
0619: F1              POP     AF                  
061A: 02              LD      (BC),A              
061B: 30 47           JR      NC,$664             ; {}
061D: 00              NOP                         
061E: 18 0A           JR      $62A                ; {}
0620: F1              POP     AF                  
0621: 14              INC     D                   
0622: 18 00           JR      $624                ; {}
0624: F1              POP     AF                  
0625: 02              LD      (BC),A              
0626: 30 43           JR      NC,$66B             ; {}
0628: 00              NOP                         
0629: 18 0A           JR      $635                ; {}
062B: F1              POP     AF                  
062C: 14              INC     D                   
062D: 18 00           JR      $62F                ; {}
062F: F1              POP     AF                  
0630: 02              LD      (BC),A              
0631: 30 47           JR      NC,$67A             ; {}
0633: 00              NOP                         
0634: 18 0A           JR      $640                ; {}
0636: F1              POP     AF                  
0637: 14              INC     D                   
0638: 18 00           JR      $63A                ; {}
063A: F1              POP     AF                  
063B: 02              LD      (BC),A              
063C: 30 43           JR      NC,$681             ; {}
063E: 00              NOP                         
063F: 18 0A           JR      $64B                ; {}
0641: F1              POP     AF                  
0642: 14              INC     D                   
0643: 18 00           JR      $645                ; {}
0645: F1              POP     AF                  
0646: 02              LD      (BC),A              
0647: 30 50           JR      NC,$699             ; {}
0649: 00              NOP                         
064A: 18 0A           JR      $656                ; {}
064C: F1              POP     AF                  
064D: D4 18 00        CALL    NC,$0018            ; {}
0650: F1              POP     AF                  
0651: 02              LD      (BC),A              
0652: 47              LD      B,A                 
0653: 02              LD      (BC),A              
0654: 47              LD      B,A                 
0655: 04              INC     B                   
0656: 57              LD      D,A                 
0657: 01 FF 22        LD      BC,$22FF            
065A: 1C              INC     E                   
065B: 01 09 07        LD      BC,$0709            
065E: F1              POP     AF                  
065F: D4 09 00        CALL    NC,$0009            ; {}
0662: F1              POP     AF                  
0663: 02              LD      (BC),A              
0664: 22 EF 00        LD      ($00EF),HL          ; {}
0667: 09              ADD     HL,BC               
0668: 07              RLCA                        
0669: F1              POP     AF                  
066A: 5C              LD      E,H                 
066B: 09              ADD     HL,BC               
066C: 00              NOP                         
066D: F1              POP     AF                  
066E: 02              LD      (BC),A              
066F: 22 1C 01        LD      ($011C),HL          ; {}
0672: 09              ADD     HL,BC               
0673: 07              RLCA                        
0674: F1              POP     AF                  
0675: D4 09 00        CALL    NC,$0009            ; {}
0678: F1              POP     AF                  
0679: 02              LD      (BC),A              
067A: 22 EF 00        LD      ($00EF),HL          ; {}
067D: 09              ADD     HL,BC               
067E: 07              RLCA                        
067F: F1              POP     AF                  
0680: 5C              LD      E,H                 
0681: 09              ADD     HL,BC               
0682: 00              NOP                         
0683: F1              POP     AF                  
0684: 02              LD      (BC),A              
0685: 22 1C 01        LD      ($011C),HL          ; {}
0688: 09              ADD     HL,BC               
0689: 07              RLCA                        
068A: F1              POP     AF                  
068B: 44              LD      B,H                 
068C: 09              ADD     HL,BC               
068D: 00              NOP                         
068E: F1              POP     AF                  
068F: 02              LD      (BC),A              
0690: 22 66 01        LD      ($0166),HL          ; {}
0693: 09              ADD     HL,BC               
0694: 07              RLCA                        
0695: F1              POP     AF                  
0696: BC              CP      H                   
0697: 09              ADD     HL,BC               
0698: 00              NOP                         
0699: F1              POP     AF                  
069A: 02              LD      (BC),A              
069B: 22 7B 01        LD      ($017B),HL          ; {}
069E: 09              ADD     HL,BC               
069F: 07              RLCA                        
06A0: F1              POP     AF                  
06A1: F8              RET     M                   
06A2: 09              ADD     HL,BC               
06A3: 00              NOP                         
06A4: F1              POP     AF                  
06A5: 02              LD      (BC),A              
06A6: FF              RST     0X38                
06A7: 24              INC     H                   
06A8: 66              LD      H,(HL)              
06A9: 01 0A 09        LD      BC,$090A            
06AC: F1              POP     AF                  
06AD: 44              LD      B,H                 
06AE: 0A              LD      A,(BC)              
06AF: 00              NOP                         
06B0: F1              POP     AF                  
06B1: 02              LD      (BC),A              
06B2: 24              INC     H                   
06B3: DE 01           SBC     $01                 
06B5: 0A              LD      A,(BC)              
06B6: 09              ADD     HL,BC               
06B7: F1              POP     AF                  
06B8: 8C              ADC     A,H                 
06B9: 0A              LD      A,(BC)              
06BA: 00              NOP                         
06BB: F1              POP     AF                  
06BC: 02              LD      (BC),A              
06BD: 24              INC     H                   
06BE: 3F              CCF                         
06BF: 01 0A 09        LD      BC,$090A            
06C2: F1              POP     AF                  
06C3: 2C              INC     L                   
06C4: 0A              LD      A,(BC)              
06C5: 00              NOP                         
06C6: F1              POP     AF                  
06C7: 02              LD      (BC),A              
06C8: 24              INC     H                   
06C9: 7B              LD      A,E                 
06CA: 01 0A 09        LD      BC,$090A            
06CD: F1              POP     AF                  
06CE: 2C              INC     L                   
06CF: 0A              LD      A,(BC)              
06D0: 00              NOP                         
06D1: F1              POP     AF                  
06D2: 02              LD      (BC),A              
06D3: 24              INC     H                   
06D4: 66              LD      H,(HL)              
06D5: 01 0A 09        LD      BC,$090A            
06D8: F1              POP     AF                  
06D9: 44              LD      B,H                 
06DA: 0A              LD      A,(BC)              
06DB: 00              NOP                         
06DC: F1              POP     AF                  
06DD: 02              LD      (BC),A              
06DE: 24              INC     H                   
06DF: DE 01           SBC     $01                 
06E1: 0A              LD      A,(BC)              
06E2: 09              ADD     HL,BC               
06E3: F1              POP     AF                  
06E4: 8C              ADC     A,H                 
06E5: 0A              LD      A,(BC)              
06E6: 00              NOP                         
06E7: F1              POP     AF                  
06E8: 02              LD      (BC),A              
06E9: 24              INC     H                   
06EA: 3F              CCF                         
06EB: 01 0A 09        LD      BC,$090A            
06EE: F1              POP     AF                  
06EF: 2C              INC     L                   
06F0: 0A              LD      A,(BC)              
06F1: 00              NOP                         
06F2: F1              POP     AF                  
06F3: 02              LD      (BC),A              
06F4: 24              INC     H                   
06F5: 7B              LD      A,E                 
06F6: 01 0A 09        LD      BC,$090A            
06F9: F1              POP     AF                  
06FA: 2C              INC     L                   
06FB: 0A              LD      A,(BC)              
06FC: 00              NOP                         
06FD: F1              POP     AF                  
06FE: 02              LD      (BC),A              
06FF: 24              INC     H                   
0700: 66              LD      H,(HL)              
0701: 01 0A 09        LD      BC,$090A            
0704: F1              POP     AF                  
0705: 44              LD      B,H                 
0706: 0A              LD      A,(BC)              
0707: 00              NOP                         
0708: F1              POP     AF                  
0709: 02              LD      (BC),A              
070A: 24              INC     H                   
070B: 38 02           JR      C,$70F              ; {}
070D: 0A              LD      A,(BC)              
070E: 09              ADD     HL,BC               
070F: F1              POP     AF                  
0710: 8C              ADC     A,H                 
0711: 0A              LD      A,(BC)              
0712: 00              NOP                         
0713: F1              POP     AF                  
0714: 02              LD      (BC),A              
0715: 24              INC     H                   
0716: DE 01           SBC     $01                 
0718: 0A              LD      A,(BC)              
0719: 09              ADD     HL,BC               
071A: F1              POP     AF                  
071B: 44              LD      B,H                 
071C: 0A              LD      A,(BC)              
071D: 00              NOP                         
071E: F1              POP     AF                  
071F: 02              LD      (BC),A              
0720: F1              POP     AF                  
0721: 13              INC     DE                  
0722: 24              INC     H                   
0723: DE 01           SBC     $01                 
0725: 0A              LD      A,(BC)              
0726: 09              ADD     HL,BC               
0727: F1              POP     AF                  
0728: D4 0A 00        CALL    NC,$000A            ; {}
072B: F1              POP     AF                  
072C: 02              LD      (BC),A              
072D: FF              RST     0X38                
072E: F5              PUSH    AF                  
072F: 12              LD      (DE),A              
0730: 00              NOP                         
0731: 25              DEC     H                   
0732: 01 00 F2        LD      BC,$F200            
0735: 04              INC     B                   
0736: 00              NOP                         
0737: 67              LD      H,A                 
0738: FE 08           CP      $08                 
073A: 0B              DEC     BC                  
073B: 80              ADD     A,B                 
073C: 10 F1           DJNZ    $72F                ; {}
073E: 01 80 FE        LD      BC,$FE80            
0741: F1              POP     AF                  
0742: 04              INC     B                   
0743: F3              DI                          
0744: 00              NOP                         
0745: 25              DEC     H                   
0746: 01 00 F2        LD      BC,$F200            
0749: 0C              INC     C                   
074A: 00              NOP                         
074B: 80              ADD     A,B                 
074C: 10 F1           DJNZ    $73F                ; {}
074E: 01 80 FE        LD      BC,$FE80            
0751: F1              POP     AF                  
0752: 04              INC     B                   
0753: F3              DI                          
0754: 47              LD      B,A                 
0755: 01 08 00        LD      BC,$0008            
0758: FF              RST     0X38                
0759: 07              RLCA                        
075A: 3F              CCF                         
075B: 17              RLA                         
075C: 3F              CCF                         
075D: 06 1F           LD      B,$1F               
075F: 16 1F           LD      D,$1F               
0761: 2B              DEC     HL                  
0762: 00              NOP                         
0763: 02              LD      (BC),A              
0764: 3B              DEC     SP                  
0765: 00              NOP                         
0766: 02              LD      (BC),A              
0767: 08              EX      AF,AF'              
0768: 00              NOP                         
0769: 18 00           JR      $76B                ; {}
076B: 0A              LD      A,(BC)              
076C: 00              NOP                         
076D: 1A              LD      A,(DE)              
076E: 00              NOP                         
076F: 09              ADD     HL,BC               
0770: 10 19           DJNZ    $78B                ; {}
0772: 10 67           DJNZ    $7DB                ; {}
0774: EF              RST     0X28                
0775: 77              LD      (HL),A              
0776: EF              RST     0X28                
0777: 0D              DEC     C                   
0778: 00              NOP                         
0779: 1D              DEC     E                   
077A: 00              NOP                         
077B: F1              POP     AF                  
077C: 13              INC     DE                  
077D: 09              ADD     HL,BC               
077E: 00              NOP                         
077F: 19              ADD     HL,DE               
0780: 00              NOP                         
0781: 08              EX      AF,AF'              
0782: 10 18           DJNZ    $79C                ; {}
0784: 10 47           DJNZ    $7CD                ; {}
0786: 10 57           DJNZ    $7DF                ; {}
0788: 10 67           DJNZ    $7F1                ; {}
078A: F7              RST     0X30                
078B: 77              LD      (HL),A              
078C: F7              RST     0X30                
078D: 0D              DEC     C                   
078E: 00              NOP                         
078F: 1D              DEC     E                   
0790: 00              NOP                         
0791: F1              POP     AF                  
0792: 13              INC     DE                  
0793: 08              EX      AF,AF'              
0794: 00              NOP                         
0795: 18 00           JR      $797                ; {}
0797: 09              ADD     HL,BC               
0798: 10 19           DJNZ    $7B3                ; {}
079A: 10 47           DJNZ    $7E3                ; {}
079C: 08              EX      AF,AF'              
079D: 57              LD      D,A                 
079E: 08              EX      AF,AF'              
079F: 67              LD      H,A                 
07A0: EF              RST     0X28                
07A1: 77              LD      (HL),A              
07A2: EF              RST     0X28                
07A3: 2B              DEC     HL                  
07A4: 00              NOP                         
07A5: 20 3B           JR      NZ,$7E2             ; {}
07A7: 00              NOP                         
07A8: 20 0D           JR      NZ,$7B7             ; {}
07AA: 00              NOP                         
07AB: 1D              DEC     E                   
07AC: 00              NOP                         
07AD: F1              POP     AF                  
07AE: C7              RST     0X00                
07AF: F1              POP     AF                  
07B0: C7              RST     0X00                
07B1: F4 00 FF        CALL    P,$FF00             ; 
07B4: F5              PUSH    AF                  
07B5: 01 F5 16        LD      BC,$16F5            
07B8: F5              PUSH    AF                  
07B9: 15              DEC     D                   
07BA: F5              PUSH    AF                  
07BB: 02              LD      (BC),A              
07BC: F5              PUSH    AF                  
07BD: 03              INC     BC                  
07BE: F5              PUSH    AF                  
07BF: 04              INC     B                   
07C0: F5              PUSH    AF                  
07C1: 05              DEC     B                   
07C2: F5              PUSH    AF                  
07C3: 06 F5           LD      B,$F5               
07C5: 07              RLCA                        
07C6: F5              PUSH    AF                  
07C7: 08              EX      AF,AF'              
07C8: F5              PUSH    AF                  
07C9: 09              ADD     HL,BC               
07CA: F5              PUSH    AF                  
07CB: 0B              DEC     BC                  
07CC: F5              PUSH    AF                  
07CD: 0C              INC     C                   
07CE: F5              PUSH    AF                  
07CF: 0D              DEC     C                   
07D0: F5              PUSH    AF                  
07D1: 0E F5           LD      C,$F5               
07D3: 0F              RRCA                        
07D4: F5              PUSH    AF                  
07D5: 10 F5           DJNZ    $7CC                ; {}
07D7: 11 F5 12        LD      DE,$12F5            
07DA: 20 00           JR      NZ,$7DC             ; {}
07DC: 00              NOP                         
07DD: 22 00 00        LD      ($0000),HL          ; {}
07E0: 24              INC     H                   
07E1: 00              NOP                         
07E2: 00              NOP                         
07E3: 26 00           LD      H,$00               
07E5: 3F              CCF                         
07E6: 28 00           JR      Z,$7E8              ; {}
07E8: 00              NOP                         
07E9: 2A 00 00        LD      HL,($0000)          ; {}
07EC: 2C              INC     L                   
07ED: 00              NOP                         
07EE: 00              NOP                         
07EF: 30 00           JR      NC,$7F1             ; {}
07F1: 00              NOP                         
07F2: 32 00 00        LD      ($0000),A           ; {}
07F5: 34              INC     (HL)                
07F6: 00              NOP                         
07F7: 00              NOP                         
07F8: 36 00           LD      (HL),$00            
07FA: 3F              CCF                         
07FB: 38 00           JR      C,$7FD              ; {}
07FD: 00              NOP                         
07FE: 3A 00 
```

