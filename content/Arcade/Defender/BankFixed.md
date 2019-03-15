![Fixed Bank](Defender.jpg)

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

# Fixed Bank

I have no idea what this first byte is. I now have a theory regarding this, though. 
I believe this must be set to yield a value of $80 when a checksum is done on this ROM.

```code
D000: 4A            DECA                     ;

This routine seems to be some sort of chain. Each link has 
at least 6 bytes. There are some indications that the chain
links are larger. The U register points to the link and the word
at ,U has the address of the next link. The word at 2,U is a
jump address to go back to when this link "matures". The byte 
at 4,U is a counter to determine when the current link has 
matured. The byte at 5,U is unknown, but is used in at least
one location. A pointer to the current link is kept in <$63.
Some routines appear to access larger ofsets in this structure.
The routine at $F4BE accesses a word value at 13,U and a byte
value at 12,U. It has not, however, been established that the U register is pointing
to one of these links when it is used with these values.

Some of the destinations/counts from this chain: $D499/$A, $D93A/$F, $DA1F/$80, $DA32/$60, [[BR]]
  $DABC/2, $DA7C/2, $DAB8/2, $DB15/$60, $DB48/$28, $DCEA/$F, [[BR]]
  $DE66/4, $DE79/$80, $E5CB/1, $E638/1, $E784/2, $E8AE/2, $E8BC/5, [[BR]]
  $E900/2, $E90C/$A, $E91A/$A, $E936/$F, $E9AC/$28, $E9BF/4, [[BR]]
  $E9EE/2, $E9FC/2, $E9E3/4, $EAB4/6, $EC2A/3, $ECC9/2, $EE44/2, $EEB2/$32, [[BR]]
  $EFF6/6, $F074/1, $F0E6/4, $F101/1, $F15E/3, $F216/4, $F24C/1, [[BR]]
  $F2F7/1, $F44A/6, $F472/3, $F464/6, $F4B0/8, $F493/$C, $F4CC/1

InsertEventLink:
D001: DE 63         LDU   <$63               ;get the current event chain link address pointer
D003: A7 44         STA   4,U                ;store count for this link in the chain
D005: AF 42         STX   2,U                ;store action address for this link
D007: 7E E8 56      JMP   Ticker             ;

D00A: 9E 63         LDX   <$63               ;
D00C: 8D 07         BSR   $D015              ;
D00E: 33 84         LEAU  ,X                 ;
D010: 7E E8 56      JMP   Ticker             ;

D013: AE 06         LDX   6,X                ;load alternate event chain address?

D015: 34 46         PSHS  U,B,A              ;
D017: CE A0 5F      LDU   #$A05F             ;load the 1st link in the event chain into U register
D01A: AC C4         CMPX  ,U                 ;looking for the link preceding the one that X is pointing to?
D01C: 26 18         BNE   $D036              ;if this isn't it then go to next one
D01E: EC 84         LDD   ,X                 ;get addr of link beyond the next one
D020: ED C4         STD   ,U                 ;make that the next one in the chain, we're eliminating the next link in the chain
D022: A6 06         LDA   6,X                ;
D024: 27 06         BEQ   $D02C              ;
D026: DC 69         LDD   <$69               ;??? $A069 ???
D028: 9F 69         STX   <$69               ;???
D02A: 20 04         BRA   $D030              ;
D02C: DC 61         LDD   <$61               ;??? $A061 ???
D02E: 9F 61         STX   <$61               ;???
D030: ED 84         STD   ,X                 ;
D032: 30 C4         LEAX  ,U                 ;
D034: 35 C6         PULS  A,B,U,PC           ;
D036: EE C4         LDU   ,U                 ;go to next link in the chain
D038: 26 E0         BNE   $D01A              ;



This looks like a deliberate attempt to confuse anyone who might be wanting to know how the Defender game program works. Who might that be? :)

;SUBRTN
D03A: 12            NOP                      ;WHY?
D03B: 7E D7 38      JMP   $D738              ;A: screwy code in subroutine at $D03E
;why the NOP? Probably just filler. 


;SUBRTN
D03E: 34 62         PSHS  U,Y,A              ;
D040: DE 69         LDU   <$69               ;
D042: 26 01         BNE   $D045              ;jumping into the middle of the next instruction?
D044: BD D0 3A      JSR   $D03A              ;"JSR $D738"
   ;This is the part that I think is a deliberate attempt to confuse people like me.
   ;I think this screwy business here is the reason the subroutine at $D03A is necessary
   ; No, this is common in 6809.
   $D045          ;hate it when this happens
;D045: D0 3A         SUBB  <$3A          ;
D047: 10 AE C4      LDY   ,U                 ;
D04A: 10 9F 69      STY   <$69               ;
D04D: 86 01         LDA   #$01               ;
D04F: A7 46         STA   6,U                ;
D051: A6 E4         LDA   ,S                 ;
D053: 20 11         BRA   $D066              ;


;SUBRTN
D055: 34 62         PSHS  U,Y,A              ;
D057: DE 61         LDU   <$61               ;??? don't know what this variable is yet
D059: 26 03         BNE   $D05E              ;
D05B: BD D0 3A      JSR   $D03A              ;
D05E: 10 AE C4      LDY   ,U                 ;
D061: 10 9F 61      STY   <$61               ;???
D064: 6F 46         CLR   6,U                ;??? 
D066: AF 42         STX   2,U                ;set event manager address
D068: A7 45         STA   5,U                ;???
D06A: 86 01         LDA   #$01               ;
D06C: A7 44         STA   4,U                ;set the event count to a 1
D06E: AE 9F A0 63   LDX   [$A063]            ;this would be the address pointed to by <$63, the current link in the event chain
D072: EF 9F A0 63   STU   [$A063]            ;
D076: AF C4         STX   ,U                 ;
D078: 30 C4         LEAX  ,U                 ;
D07A: 35 E2         PULS  A,Y,U,PC           ;




;SUBRTN
D07C: 34 12         PSHS  X,A                ;
D07E: 8E A0 5F      LDX   #$A05F             ;load the 1st link in the event chain into X register
D081: AE 84         LDX   ,X                 ;if this link is zero, presumably this would mean it is the last link?
D083: 27 0E         BEQ   $D093              ;if zero, leave
D085: 9C 63         CMPX  <$63               ;is this the current link?
D087: 27 F8         BEQ   $D081              ;if so, let's go to the next one
D089: A6 05         LDA   5,X                ;get value in 6th byte of link
D08B: 81 02         CMPA  #$02               ;if it's a 2 then go on to next link
D08D: 27 F2         BEQ   $D081              ;
D08F: 8D 84         BSR   $D015              ;otherwise, X=addr of next link, A=6th byte of this link
D091: 20 EE         BRA   $D081              ;on return we go to the next link
D093: 35 92         PULS  A,X,PC             ;finally hit the last link, so we return



;SUBRTN
D095: 8D 16         BSR   $D0AD              ;
D097: 34 66         PSHS  U,Y,B,A            ;
D099: EF 06         STU   6,X                ;
D09B: EE 66         LDU   6,S                ;
D09D: 37 26         PULU  A,B,Y              ;
D09F: ED 02         STD   2,X                ;
D0A1: 10 AF 08      STY   8,X                ;
D0A4: 37 06         PULU  A,B                ;
D0A6: ED 88 12      STD   $12,X              ;
D0A9: EF 66         STU   6,S                ;
D0AB: 35 E6         PULS  A,B,Y,U,PC         ;



;SUBRTN
D0AD: 34 46         PSHS  U,B,A              ;
D0AF: 9E 67         LDX   <$67               ;
D0B1: 26 03         BNE   $D0B6              ;
D0B3: BD D0 3A      JSR   $D03A              ;Why not just "JSR   $D738"?
D0B6: EC 84         LDD   ,X                 ;
D0B8: DD 67         STD   <$67               ;
D0BA: DC 65         LDD   <$65               ;
D0BC: ED 84         STD   ,X                 ;
D0BE: 4F            CLRA                     ;
D0BF: 5F            CLRB                     ;
D0C0: ED 04         STD   4,X                ;


// What if $14 is a memory address we are indexing off of? We need a way to tell the compiler to look for $14
D0C2: A7 88 14      STA   $14,X              ; @@ The "@@" the the hint that "$14 is an address"


D0C5: 35 C6         PULS  A,B,U,PC           ;



;SUBRTN
D0C7: 34 70         PSHS  U,Y,X              ;
D0C9: CE A0 65      LDU   #$A065             ;
D0CC: AC C4         CMPX  ,U                 ;
D0CE: 26 10         BNE   $D0E0              ;
D0D0: 10 AE D4      LDY   [,U]               ;
D0D3: 10 AF C4      STY   ,U                 ;
D0D6: 10 9E 67      LDY   <$67               ;
D0D9: 9F 67         STX   <$67               ;
D0DB: 10 AF 84      STY   ,X                 ;
D0DE: 35 F0         PULS  X,Y,U,PC           ;
D0E0: EE C4         LDU   ,U                 ;
D0E2: 26 E8         BNE   $D0CC              ;
D0E4: CE A0 6B      LDU   #$A06B             ;
D0E7: AC C4         CMPX  ,U                 ;
D0E9: 27 E5         BEQ   $D0D0              ;
D0EB: EE C4         LDU   ,U                 ;
D0ED: 26 F8         BNE   $D0E7              ;
D0EF: BD D0 3A      JSR   $D03A              ;Why not just "JSR   $D738"?

;SUBRTN
D0F2: 34 70         PSHS  U,Y,X              ;
D0F4: CE A0 6D      LDU   #$A06D             ;
D0F7: 20 EE         BRA   $D0E7              ;



;entry point via vector
D0F9: 34 18         PSHS  X,DP               ;saving the X and DP regs
D0FB: 10 DF 77      STS   <$77               ;save the system stack in $A077(DP=$A0)
D0FE: 24 02         BCC   $D102              ;if carry is clear Y reg is already set to value we want
D100: 31 22         LEAY  2,Y                ;move to next word with Y reg
D102: 10 EE 22      LDS   2,Y                ;load the source address
D105: CB 08         ADDB  #$08               ;calc source address start point
D107: 1F 03         TFR   D,U                ;put it in the source(user) stack reg
D109: 20 4E         BRA   $D159              ;go move 16 bytes using the two stack registers

;entry point via vector
D10B: 34 18         PSHS  X,DP               ;saving the X and DP regs
D10D: CB 08         ADDB  #$08               ;calc source address start point
D10F: 1F 03         TFR   D,U                ;put it in the source(user) stack reg
D111: CC 00 00      LDD   #$0000             ;clear all the registers we will be using
D114: 8E 00 00      LDX   #$0000             ;
D117: 31 84         LEAY  ,X                 ;
D119: 1F 8B         TFR   A,DP               ;
D11B: 1C 00         ANDCC #$00               ;
D11D: 20 6A         BRA   $D189              ;go clear 16 bytes

;entry via vector
D11F: 34 18         PSHS  X,DP               ;saving the X and DP regs
D121: CB 08         ADDB  #$08               ;
D123: 1F 03         TFR   D,U                ;
D125: CC 00 00      LDD   #$0000             ;clear all the registers we will be using
D128: 8E 00 00      LDX   #$0000             ;
D12B: 31 84         LEAY  ,X                 ;
D12D: 1F 8B         TFR   A,DP               ;
D12F: 1C 00         ANDCC #$00               ;enable interrupts?
D131: 36 3F         PSHU  Y,X,DP,B,A,CC      ;clear 8 bytes
D133: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D137: 20 44         BRA   $D17D              ;go clear another 32 bytes

;entry via vector
D139: 34 18         PSHS  X,DP               ;saving the X and DP regs
D13B: 10 DF 77      STS   <$77               ;save the system stack in $A077(DP=$A0)
D13E: 24 02         BCC   $D142              ;
D140: 31 22         LEAY  2,Y                ;
D142: 10 EE 22      LDS   2,Y                ;
D145: CB 08         ADDB  #$08               ;
D147: 1F 03         TFR   D,U                ;
;move 32 bytes
D149: 35 3F         PULS  CC,A,B,DP,X,Y      ;
D14B: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D14D: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D151: 35 3F         PULS  CC,A,B,DP,X,Y      ;
D153: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D155: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D159: 35 3F         PULS  CC,A,B,DP,X,Y      ;
D15B: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D15D: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D161: 35 3F         PULS  CC,A,B,DP,X,Y      ;
D163: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D165: 10 FE A0 77   LDS   $A077              ;restore stack via extended address because the DP is pointing to the wrong spot right now.
D169: 35 98         PULS  DP,X,PC            ;restore and return

;entry via one of several vectors
D16B: 34 18         PSHS  X,DP               ;saving the X and DP regs
D16D: CB 08         ADDB  #$08               ;
D16F: 1F 03         TFR   D,U                ;
D171: CC 00 00      LDD   #$0000             ;
D174: 8E 00 00      LDX   #$0000             ;
D177: 31 84         LEAY  ,X                 ;
D179: 1F 8B         TFR   A,DP               ;
D17B: 1C 00         ANDCC #$00               ;
;clear 32 bytes
D17D: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D17F: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D183: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D185: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D189: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D18B: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D18F: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D191: 35 98         PULS  DP,X,PC            ;restore and return

;entry via vector
D193: 34 18         PSHS  X,DP               ;saving the X and DP regs
D195: 10 DF 77      STS   <$77               ;
D198: 24 02         BCC   $D19C              ;
D19A: 31 22         LEAY  2,Y                ;
D19C: 10 EE 22      LDS   2,Y                ;
D19F: CB 08         ADDB  #$08               ;
D1A1: 1F 03         TFR   D,U                ;
D1A3: 35 3F         PULS  CC,A,B,DP,X,Y      ;move 8 bytes
D1A5: 36 3F         PSHU  Y,X,DP,B,A,CC      ;
D1A7: 33 C9 01 08   LEAU  $0108,U            ;move to next line of display?
D1AB: 20 9C         BRA   $D149              ;go move 32 more bytes



;entry via vector
D1AD: 24 02         BCC   $D1B1              ;
D1AF: 31 22         LEAY  2,Y                ;
D1B1: 10 AE 22      LDY   2,Y                ;
D1B4: 1F 03         TFR   D,U                ;
D1B6: EC A4         LDD   ,Y                 ;
D1B8: ED C4         STD   ,U                 ;
D1BA: EC 22         LDD   2,Y                ;
D1BC: ED 42         STD   2,U                ;
D1BE: EC 24         LDD   4,Y                ;
D1C0: ED C9 01 00   STD   $0100,U            ;
D1C4: EC 26         LDD   6,Y                ;
D1C6: ED C9 01 02   STD   $0102,U            ;
D1CA: EC 28         LDD   8,Y                ;
D1CC: ED C9 02 00   STD   $0200,U            ;
D1D0: EC 2A         LDD   10,Y               ;
D1D2: ED C9 02 02   STD   $0202,U            ;
D1D6: 39            RTS                      ;



;entry via vector
D1D7: 1F 03         TFR   D,U                ;
D1D9: CC 00 00      LDD   #$0000             ;
D1DC: ED C4         STD   ,U                 ;
D1DE: ED 42         STD   2,U                ;
D1E0: ED C9 01 00   STD   $0100,U            ;
D1E4: ED C9 01 02   STD   $0102,U            ;
D1E8: ED C9 02 00   STD   $0200,U            ;
D1EC: ED C9 02 02   STD   $0202,U            ;
D1F0: 39            RTS                      ;



;entry via vector
D1F1: 24 02         BCC   $D1F5              ;
D1F3: 31 22         LEAY  2,Y                ;
D1F5: 10 AE 22      LDY   2,Y                ;
D1F8: 1F 03         TFR   D,U                ;
D1FA: EC A4         LDD   ,Y                 ;
D1FC: ED C4         STD   ,U                 ;
D1FE: EC 22         LDD   2,Y                ;
D200: A7 42         STA   2,U                ;
D202: E7 C9 01 00   STB   $0100,U            ;
D206: EC 24         LDD   4,Y                ;
D208: ED C9 01 01   STD   $0101,U            ;
D20C: 39            RTS                      ;



D20D: 1F 03         TFR   D,U                ;
D20F: CC 00 00      LDD   #$0000             ;
D212: ED C4         STD   ,U                 ;
D214: A7 42         STA   2,U                ;
D216: ED C9 01 00   STD   $0100,U            ;
D21A: A7 C9 01 02   STA   $0102,U            ;
D21E: 39            RTS                      ;



;called via vector
D21F: 34 56         PSHS  U,X,B,A            ;
D221: 10 DF 77      STS   <$77               ;
D224: 24 02         BCC   $D228              ;
D226: 31 22         LEAY  2,Y                ;
D228: 10 EE 22      LDS   2,Y                ;
D22B: CB 04         ADDB  #$04               ;
D22D: 1F 03         TFR   D,U                ;
D22F: 35 16         PULS  A,B,X              ;
D231: 36 16         PSHU  X,B,A              ;
D233: 33 C9 01 04   LEAU  $0104,U            ;
D237: 35 16         PULS  A,B,X              ;
D239: 36 16         PSHU  X,B,A              ;
D23B: 33 C9 01 04   LEAU  $0104,U            ;
D23F: 35 16         PULS  A,B,X              ;
D241: 36 16         PSHU  X,B,A              ;
D243: 33 C9 01 04   LEAU  $0104,U            ;
D247: 35 16         PULS  A,B,X              ;
D249: 36 16         PSHU  X,B,A              ;
D24B: 33 C9 01 04   LEAU  $0104,U            ;
D24F: 35 16         PULS  A,B,X              ;
D251: 36 16         PSHU  X,B,A              ;
D253: 33 C9 01 04   LEAU  $0104,U            ;
D257: 35 16         PULS  A,B,X              ;
D259: 36 16         PSHU  X,B,A              ;
D25B: 10 DE 77      LDS   <$77               ;
D25E: 35 D6         PULS  A,B,X,U,PC         ;



;called via vector
D260: 34 56         PSHS  U,X,B,A            ;
D262: CB 04         ADDB  #$04               ;
D264: 1F 03         TFR   D,U                ;
D266: CC 00 00      LDD   #$0000             ;
D269: 8E 00 00      LDX   #$0000             ;
D26C: 36 16         PSHU  X,B,A              ;
D26E: 33 C9 01 04   LEAU  $0104,U            ;
D272: 36 16         PSHU  X,B,A              ;
D274: 33 C9 01 04   LEAU  $0104,U            ;
D278: 36 16         PSHU  X,B,A              ;
D27A: 33 C9 01 04   LEAU  $0104,U            ;
D27E: 36 16         PSHU  X,B,A              ;
D280: 33 C9 01 04   LEAU  $0104,U            ;
D284: 36 16         PSHU  X,B,A              ;
D286: 33 C9 01 04   LEAU  $0104,U            ;
D28A: 36 16         PSHU  X,B,A              ;
D28C: 35 D6         PULS  A,B,X,U,PC         ;



;called via vector, also from one subroutine via a JMP 
D28E: 34 10         PSHS  X                  ;
D290: 10 DF 77      STS   <$77               ;
D293: 24 02         BCC   $D297              ;
D295: 31 22         LEAY  2,Y                ;
D297: 10 EE 22      LDS   2,Y                ;
D29A: CB 06         ADDB  #$06               ;
D29C: 1F 03         TFR   D,U                ;
D29E: 35 36         PULS  A,B,X,Y            ;
D2A0: 36 36         PSHU  Y,X,B,A            ;
D2A2: 33 C9 01 06   LEAU  $0106,U            ;
D2A6: 35 36         PULS  A,B,X,Y            ;
D2A8: 36 36         PSHU  Y,X,B,A            ;
D2AA: 33 C9 01 06   LEAU  $0106,U            ;
D2AE: 35 36         PULS  A,B,X,Y            ;
D2B0: 36 36         PSHU  Y,X,B,A            ;
D2B2: 33 C9 01 06   LEAU  $0106,U            ;
D2B6: 35 36         PULS  A,B,X,Y            ;
D2B8: 36 36         PSHU  Y,X,B,A            ;
D2BA: 33 C9 01 06   LEAU  $0106,U            ;
D2BE: 35 36         PULS  A,B,X,Y            ;
D2C0: 36 36         PSHU  Y,X,B,A            ;
D2C2: 33 C9 01 06   LEAU  $0106,U            ;
D2C6: 35 36         PULS  A,B,X,Y            ;
D2C8: 36 36         PSHU  Y,X,B,A            ;
D2CA: 33 C9 01 06   LEAU  $0106,U            ;
D2CE: 35 36         PULS  A,B,X,Y            ;
D2D0: 36 36         PSHU  Y,X,B,A            ;
D2D2: 33 C9 01 06   LEAU  $0106,U            ;
D2D6: 35 36         PULS  A,B,X,Y            ;
D2D8: 36 36         PSHU  Y,X,B,A            ;
D2DA: 10 DE 77      LDS   <$77               ;
D2DD: 35 90         PULS  X,PC               ;



;located in possible jump table at $F9D1-$F9D4??
D2DF: 34 10         PSHS  X                  ;
D2E1: CB 06         ADDB  #$06               ;
D2E3: 1F 03         TFR   D,U                ;
D2E5: CC 00 00      LDD   #$0000             ;
D2E8: 8E 00 00      LDX   #$0000             ;
D2EB: 31 84         LEAY  ,X                 ;
D2ED: 36 36         PSHU  Y,X,B,A            ;
D2EF: 33 C9 01 06   LEAU  $0106,U            ;
D2F3: 36 36         PSHU  Y,X,B,A            ;
D2F5: 33 C9 01 06   LEAU  $0106,U            ;
D2F9: 36 36         PSHU  Y,X,B,A            ;
D2FB: 33 C9 01 06   LEAU  $0106,U            ;
D2FF: 36 36         PSHU  Y,X,B,A            ;
D301: 33 C9 01 06   LEAU  $0106,U            ;
D305: 36 36         PSHU  Y,X,B,A            ;
D307: 33 C9 01 06   LEAU  $0106,U            ;
D30B: 36 36         PSHU  Y,X,B,A            ;
D30D: 33 C9 01 06   LEAU  $0106,U            ;
D311: 36 36         PSHU  Y,X,B,A            ;
D313: 33 C9 01 06   LEAU  $0106,U            ;
D317: 36 36         PSHU  Y,X,B,A            ;
D319: 35 90         PULS  X,PC               ;


No JMP, JSR, BRA, vector, etc. leads us to these two sections of code, so far.


;how do we get here?
D31B: 34 10         PSHS  X                  ;
D31D: 10 DF 77      STS   <$77               ;
D320: 24 02         BCC   $D324              ;
D322: 31 22         LEAY  2,Y                ;
D324: 10 EE 22      LDS   2,Y                ;
D327: CB 06         ADDB  #$06               ;
D329: 1F 03         TFR   D,U                ;
D32B: 20 89         BRA   $D2B6              ;

;how do we get here?
D32D: 34 10         PSHS  X                  ;
D32F: CB 06         ADDB  #$06               ;
D331: 1F 03         TFR   D,U                ;
D333: CC 00 00      LDD   #$0000             ;
D336: 8E 00 00      LDX   #$0000             ;
D339: 31 84         LEAY  ,X                 ;
D33B: 20 C2         BRA   $D2FF              ;



;called via vector
D33D: 34 10         PSHS  X                  ;
D33F: 10 DF 77      STS   <$77               ;
D342: 24 02         BCC   $D346              ;
D344: 31 22         LEAY  2,Y                ;
D346: 10 EE 22      LDS   2,Y                ;
D349: CB 06         ADDB  #$06               ;
D34B: 1F 03         TFR   D,U                ;
D34D: 7E D2 AE      JMP   $D2AE              ;

;called via vector
D350: 34 10         PSHS  X                  ;
D352: CB 06         ADDB  #$06               ;
D354: 1F 03         TFR   D,U                ;
D356: CC 00 00      LDD   #$0000             ;
D359: 8E 00 00      LDX   #$0000             ;
D35C: 31 84         LEAY  ,X                 ;
D35E: 20 99         BRA   $D2F9              ;





;SUBRTN
D360: 34 76         PSHS  U,Y,X,B,A          ;
D362: 1A 01         ORCC  #$01               ;
D364: 09 8A         ROL   <$8A               ;
D366: 44            LSRA                     ;
D367: 34 02         PSHS  A                  ;
D369: 86 00         LDA   #$00               ;
D36B: 24 08         BCC   $D375              ;
D36D: 58            ASLB                     ;
D36E: 49            ROLA                     ;
D36F: 58            ASLB                     ;
D370: 49            ROLA                     ;
D371: 58            ASLB                     ;
D372: 49            ROLA                     ;
D373: 58            ASLB                     ;
D374: 49            ROLA                     ;
D375: BD D6 FE      JSR   $D6FE              ;
D378: DD 73         STD   <$73               ;
D37A: C6 03         LDB   #$03               ;
D37C: E0 E0         SUBB  ,S+                ;
D37E: A6 85         LDA   B,X                ;
D380: 9B 74         ADDA  <$74               ;
D382: 19            DAA                      ;
D383: A7 85         STA   B,X                ;
D385: 5A            DECB                     ;
D386: 2B 0E         BMI   $D396              ;
D388: A6 85         LDA   B,X                ;
D38A: 99 73         ADCA  <$73               ;
D38C: 19            DAA                      ;
D38D: A7 85         STA   B,X                ;
D38F: 86 00         LDA   #$00               ;
D391: 97 73         STA   <$73               ;
D393: 5A            DECB                     ;
D394: 2A F2         BPL   $D388              ;
D396: DC AB         LDD   <$AB               ;
D398: 27 2B         BEQ   $D3C5              ;
D39A: 30 01         LEAX  1,X                ;
D39C: 31 03         LEAY  3,X                ;



[http://donhodges.com/defenders_extra_life_bonanza.htm Defender's Extra Life Bonanza][[br]]

D39E: 8D 2A         BSR   $D3CA              ;
D3A0: 25 23         BCS   $D3C5              ;
D3A2: A6 21         LDA   1,Y                ;
D3A4: 9B AC         ADDA  <$AC               ;
D3A6: 19            DAA                      ;
D3A7: A7 21         STA   1,Y                ;
D3A9: A6 A4         LDA   ,Y                 ;
D3AB: 99 AB         ADCA  <$AB               ;
D3AD: 19            DAA                      ;
D3AE: A7 A4         STA   ,Y                 ;
D3B0: 6C 06         INC   6,X                ;
D3B2: 6C 08         INC   8,X                ;
D3B4: BD D6 29      JSR   $D629              ;update # of lives on screen? (Don Hodges)
D3B7: BD D6 80      JSR   $D680              ;update # of smart bombs on screen? (Don Hodges)
D3BA: CC D4 B0      LDD   #$D4B0             ;extra life sound? (Don Hodges)
D3BD: BD D5 4D      JSR   $D54D              ;play the sound? (Don Hodges)
D3C0: C6 05         LDB   #$05               ;
D3C2: BD F5 1C      JSR   $F51C              ;
D3C5: 8D 12         BSR   $D3D9              ;
D3C7: 35 76         PULS  A,B,X,Y,U          ;could have put ,PC on here for faster execution of return
D3C9: 39            RTS                      ;why didn't they? they plainly know this



;SUBRTN
D3CA: 34 06         PSHS  B,A                ;
D3CC: EC 84         LDD   ,X                 ;Load D with MSW of SCORE (Don Hodges w/ correction)
D3CE: 10 A3 A4      CMPD  ,Y                 ;Compare with MSW of NEXT (Don Hodges)
D3D1: 26 04         BNE   $D3D7              ;
D3D3: A6 02         LDA   2,X                ;
D3D5: A1 22         CMPA  2,Y                ;
D3D7: 35 86         PULS  A,B,PC             ;



;SUBRTN
D3D9: 96 8B         LDA   <$8B               ;


;SUBRTN
D3DB: 34 02         PSHS  A                  ;
D3DD: 4A            DECA                     ;
D3DE: 26 08         BNE   $D3E8              ;
D3E0: 8E 0F 1C      LDX   #$0F1C             ;
D3E3: CE A1 C3      LDU   #$A1C3             ;
D3E6: 20 06         BRA   $D3EE              ;
D3E8: 8E 71 1C      LDX   #$711C             ;
D3EB: CE A2 00      LDU   #$A200             ;
D3EE: 0F 73         CLR   <$73               ;
D3F0: C6 06         LDB   #$06               ;
D3F2: 96 36         LDA   <$36               ;get current page #
D3F4: 34 02         PSHS  A                  ;save current page # to stack
D3F6: 86 02         LDA   #$02               ;
D3F8: 97 36         STA   <$36               ;change to page 2
D3FA: B7 D0 00      STA   $D000              ;set page # to 2
D3FD: A6 C0         LDA   ,U+                ;
D3FF: 10 BE C0 00   LDY   $C000              ;
D403: C5 01         BITB  #$01               ;
D405: 26 06         BNE   $D40D              ;
D407: 33 5F         LEAU  -1,U               ;
D409: 44            LSRA                     ;
D40A: 44            LSRA                     ;
D40B: 44            LSRA                     ;
D40C: 44            LSRA                     ;
D40D: 84 0F         ANDA  #$0F               ;
D40F: 26 0F         BNE   $D420              ;
D411: C1 02         CMPB  #$02               ;
D413: 23 0B         BLS   $D420              ;
D415: 0D 73         TST   <$73               ;
D417: 26 07         BNE   $D420              ;
D419: 1E 10         EXG   X,D                ;
D41B: BD F5 7B      JSR   ScrnBlkClrP2       ;
D41E: 20 0B         BRA   $D42B              ;
D420: 0C 73         INC   <$73               ;
D422: 48            ASLA                     ;
D423: 48            ASLA                     ;
D424: 31 A6         LEAY  A,Y                ;
D426: 1E 10         EXG   X,D                ;
D428: BD F5 22      JSR   DrawChar           ;
D42B: 1E 10         EXG   X,D                ;
D42D: 30 89 04 00   LEAX  $0400,X            ;
D431: 5A            DECB                     ;
D432: 26 C9         BNE   $D3FD              ;loop
D434: 35 02         PULS  A                  ;restore previous page # from value on stack
D436: 97 36         STA   <$36               ;
D438: B7 D0 00      STA   $D000              ;
D43B: 35 82         PULS  A,PC               ;



;entry via vector
D43D: 96 BA         LDA   <$BA               ;
D43F: 2A 2A         BPL   $D46B              ;
D441: BD F5 07      JSR   ROMPg3             ;
D444: BD C0 33      JSR   $C033              ;
D447: 7C A1 62      INC   $A162              ;
D44A: 20 1F         BRA   $D46B              ;
;entry via vector
D44C: 96 BA         LDA   <$BA               ;
D44E: 2A 1B         BPL   $D46B              ;
D450: 1A 90         ORCC  #$90               ;
D452: 7F D0 00      CLR   $D000              ;I/O page, but making no effort to be able to 
return to previous page after I/O is concluded. Possibly because we already know that we 
want it to be page 3
D455: 86 04         LDA   #$04               ;
D457: B7 CC 03      STA   $CC03              ;
D45A: B6 CC 02      LDA   $CC02              ;
D45D: BD F5 07      JSR   ROMPg3             ;
D460: 96 79         LDA   <$79               ;
D462: 44            LSRA                     ;
D463: 25 03         BCS   $D468              ;
D465: 7E C0 27      JMP   $C027              ;
D468: 7E C0 21      JMP   $C021              ;
D46B: 7E D0 0A      JMP   $D00A              ;

;entry via vector
D46E: 8E A0 7F      LDX   #$A07F             ;
D471: C6 12         LDB   #$12               ;
D473: 20 0C         BRA   $D481              ;

;entry via vector
D475: 8E A0 80      LDX   #$A080             ;
D478: C6 15         LDB   #$15               ;
D47A: 20 05         BRA   $D481              ;

;entry via vector
D47C: 8E A0 81      LDX   #$A081             ;
D47F: C6 18         LDB   #$18               ;
D481: 96 7E         LDA   <$7E               ;
D483: 26 E6         BNE   $D46B              ;
D485: A6 84         LDA   ,X                 ;
D487: 26 E2         BNE   $D46B              ;
D489: 86 16         LDA   #$16               ;
D48B: A7 84         STA   ,X                 ;
D48D: 86 C0         LDA   #$C0               ;
D48F: ED 49         STD   9,U                ;
D491: 86 0A         LDA   #$0A               ;load InsertEventLink event count
D493: 8E D4 99      LDX   #$D499             ;load jump point for event return
D496: 7E D0 01      JMP   InsertEventLink    ;

;service entry on InsertEventLink event link
D499: 96 7E         LDA   <$7E               ;
D49B: 26 CE         BNE   $D46B              ;
D49D: CC D4 AB      LDD   #$D4AB             ;loading data address
D4A0: BD D5 4D      JSR   $D54D              ;
D4A3: BD F5 07      JSR   ROMPg3             ;
D4A6: AD D8 09      JSR   [$09,U]            ;
D4A9: 20 C0         BRA   $D46B              ;



      DATA
This appears to be a series of data packets terminated by a zero byte. Most packets are 5 bytes in length. I can't account for all of them being used, yet.

; I
D4AB: FF 01 18 19 00
; I
D4B0: FF 01 20 1E 00
; I
D4B5: F0 02 08 11 01 
D4BA: 20 17 00
; I
D4BD: F0 01 40 0A 00
; I
D4C2: F0 01 10 0B 00
; I
D4C7: E8 01 04 14 02 
D4CC: 06 11 02 0A 17 
D4D1: 00
; I
D4D2: E8 06 04 11 01 
D4D7: 10 17 00
; I
D4DA: E0 03 0A 08 00
; I
D4DF: E0 01 18 1F 00
; I  
D4E4: E0 01 18 11 00
; I
D4E9: D8 01 10 1A 00

D4EE: D0 01 30 15 00 

D4F3: D0 01 10 05 00

D4F8: D0 01 08 17 00 
; I
D4FD: D0 01 08 07 00 

D502: D0 01 0A 01 00 

D507: D0 01 0A 06 00
; I
D50C: D0 01 10 0B 00
; I
D511: C8 0A 01 0E 00 
; I
D516: C0 01 08 07 00
; I
D51B: C0 01 30 14 00 

D520: C0 01 20 18 00
; I
D525: C0 01 08 03 00
; I
D52A: C0 01 30 09 00
; I
D52F: C0 01 08 03 00
; I
D534: C0 01 18 0C 00 

This looks more like a sound output routine than $D54D. 

;SUBRTN
D539: 34 07         PSHS  B,A,CC             ;
D53B: 1A FF         ORCC  #$FF               ;setting all the flags?
D53D: 7F D0 00      CLR   $D000              ;switch to I/O page, not saving the current page #
D540: 86 3F         LDA   #$3F               ;load interrupt code
D542: B7 CC 02      STA   $CC02              ;send interrupt to the sound processor
D545: 53            COMB                     ;complemented sound code? I wonder why?
D546: C4 3F         ANDB  #$3F               ;mask out the two most significant bits
D548: F7 CC 02      STB   $CC02              ;send sound code
D54B: 35 87         PULS  CC,A,B,PC          ;


Play a sound routine? (Don Hodges) \\
I don't know what this routine actually does, but I am now certain that it does not actually access the sound board. Could this initiate a process that causes another routine to send out a sound? Perhaps, but I've yet to find that process. For now, I believe it is an error to call this a sound routine. \\

Called from 22 locations in this ROM \\
Address  / D reg contents \\
  D3BD   /   D4B0 \\
  D4A0   /   D4AB \\
  D846   /   D4C2 or D4BD \\
  DA5C   /   D4B5 \\
  E547   /   D4E4 \\
  E59C   /   D51B \\
  E8D5   /   D4D2 \\
  EAD2   /   D52F \\
  EC14   /   D516 \\
  ECAA   /   D534 \\
  ED8E   /   D4E4 \\
  EDA4   /   D4DA \\
  EE35   /   D4E4 \\
  EE5F   /   D4C7 \\
  EF11   /   D525 \\
  F0DE   /   D50C \\
  FOFE   /   D511 \\
  F1D5   /   D52A \\
  F1FE   /   D4E9 \\
  F297   /   D4DF \\
  F42F   /   ???? \\
  FCAF   /   FFDD  via the jump table at $FFDA \\
  FFDA   /   ???? \\ \\

ROM #   /  Address   /  D reg contents

strange that there is no looping in here. I expected \\
a search for the NULL byte. \\ \\


;SUBRTN  
D54D: 34 17         PSHS  X,B,A,CC           ;
D54F: 0F AD         CLR   <$AD               ;
D551: 1F 01         TFR   D,X                ;put data address in X reg
D553: A6 84         LDA   ,X                 ;load byte from packet
D555: 91 B2         CMPA  <$B2               ;is it less than contents of <$B2
D557: 25 0D         BCS   $D566              ;if so, then get out of here
D559: 97 B2         STA   <$B2               ;if more, or equal, replace <$B2 with this value
D55B: 30 1E         LEAX  -2,X               ;huh? moving to end of previous packet?
D55D: 1A 10         ORCC  #$10               ;no interrupt please, must be important
D55F: 9F B0         STX   <$B0               ;store that?
D561: CC 01 01      LDD   #$0101             ;
D564: DD B3         STD   <$B3               ;then make <$B3 a known value of $101(257)
D566: 35 97         PULS  CC,A,B,X,PC        ;



;SUBRTN
D568: 96 B3         LDA   <$B3               ;
D56A: 27 14         BEQ   $D580              ;
D56C: 0A B3         DEC   <$B3               ;
D56E: 26 38         BNE   $D5A8              ;
D570: 9E B0         LDX   <$B0               ;
D572: 0A B4         DEC   <$B4               ;
D574: 26 2C         BNE   $D5A2              ;
D576: 30 03         LEAX  3,X                ;
D578: 9F B0         STX   <$B0               ;
D57A: A6 84         LDA   ,X                 ;
D57C: 26 22         BNE   $D5A0              ;
D57E: 97 B2         STA   <$B2               ;
D580: 96 7B         LDA   <$7B               ;
D582: 85 02         BITA  #$02               ;
D584: 26 0A         BNE   $D590              ;
D586: 96 AD         LDA   <$AD               ;
D588: 27 1E         BEQ   $D5A8              ;
D58A: 0F AD         CLR   <$AD               ;
D58C: C6 0F         LDB   #$0F               ;
D58E: 20 16         BRA   $D5A6              ;
D590: 96 AD         LDA   <$AD               ;
D592: 26 14         BNE   $D5A8              ;
D594: 96 BA         LDA   <$BA               ;
D596: 85 98         BITA  #$98               ;
D598: 26 0E         BNE   $D5A8              ;
D59A: C6 16         LDB   #$16               ;
D59C: D7 AD         STB   <$AD               ;
D59E: 20 06         BRA   $D5A6              ;
D5A0: 97 B4         STA   <$B4               ;
D5A2: EC 01         LDD   1,X                ;
D5A4: 97 B3         STA   <$B3               ;
D5A6: 8D 91         BSR   $D539              ;
D5A8: B6 CC 01      LDA   $CC01              ;
D5AB: 85 40         BITA  #$40               ;
D5AD: 27 04         BEQ   $D5B3              ;
D5AF: 86 3C         LDA   #$3C               ;
D5B1: 97 7E         STA   <$7E               ;
D5B3: 96 7E         LDA   <$7E               ;
D5B5: 27 02         BEQ   $D5B9              ;
D5B7: 0A 7E         DEC   <$7E               ;
D5B9: 96 7F         LDA   <$7F               ;
D5BB: 27 02         BEQ   $D5BF              ;
D5BD: 0A 7F         DEC   <$7F               ;
D5BF: 96 81         LDA   <$81               ;
D5C1: 27 02         BEQ   $D5C5              ;
D5C3: 0A 81         DEC   <$81               ;
D5C5: 96 80         LDA   <$80               ;
D5C7: 27 02         BEQ   $D5CB              ;
D5C9: 0A 80         DEC   <$80               ;
D5CB: 96 7B         LDA   <$7B               ;
D5CD: 9A 7C         ORA   <$7C               ;
D5CF: 43            COMA                     ;
D5D0: D6 7B         LDB   <$7B               ;
D5D2: D7 7C         STB   <$7C               ;
D5D4: F6 CC 04      LDB   $CC04              ;
D5D7: D7 7B         STB   <$7B               ;
D5D9: F6 CC 06      LDB   $CC06              ;
D5DC: D7 7D         STB   <$7D               ;
D5DE: 94 7B         ANDA  <$7B               ;
D5E0: 27 1B         BEQ   $D5FD              ;
D5E2: CE F8 82      LDU   #$F882             ;



;SUBRTN
D5E5: 5F            CLRB                     ;
D5E6: CB 04         ADDB  #$04               ;
D5E8: 44            LSRA                     ;
D5E9: 24 FB         BCC   $D5E6              ;
D5EB: 33 C5         LEAU  B,U                ;
D5ED: 37 16         PULU  A,B,X              ;
D5EF: DE 82         LDU   <$82               ;
D5F1: 26 05         BNE   $D5F8              ;
D5F3: DD 82         STD   <$82               ;
D5F5: 9F 84         STX   <$84               ;
D5F7: 39            RTS                      ;
D5F8: DD 86         STD   <$86               ;
D5FA: 9F 88         STX   <$88               ;
D5FC: 39            RTS                      ;



;SUBRTN
D5FD: 96 79         LDA   <$79               ;
D5FF: 9A 7A         ORA   <$7A               ;
D601: 43            COMA                     ;
D602: D6 79         LDB   <$79               ;
D604: D7 7A         STB   <$7A               ;
D606: F6 CC 00      LDB   PIA_addr_base      ;
D609: C4 3F         ANDB  #$3F               ;
D60B: D7 79         STB   <$79               ;
D60D: 95 79         BITA  <$79               ;
D60F: 27 17         BEQ   $D628              ;
D611: 8E 00 78      LDX   #$0078             ;
D614: 30 1F         LEAX  -1,X               ;
D616: 26 FC         BNE   $D614              ;
D618: F6 CC 00      LDB   PIA_addr_base      ;
D61B: D4 79         ANDB  <$79               ;
D61D: D7 79         STB   <$79               ;
D61F: 94 79         ANDA  <$79               ;
D621: 27 05         BEQ   $D628              ;
D623: CE F8 A2      LDU   #$F8A2             ;
D626: 8D BD         BSR   $D5E5              ;
D628: 39            RTS                      ;



;SUBRTN
D629: 34 76         PSHS  U,Y,X,B,A          ;
D62B: 8E 0F 14      LDX   #$0F14             ;player 1 lives start position?
D62E: B6 A1 C9      LDA   $A1C9              ;get # of lives for player 1
D631: 8D 0F         BSR   $D642              ;Go paint in player 1's reserve ships
D633: 96 8C         LDA   <$8C               ;
D635: 4A            DECA                     ;
D636: 27 08         BEQ   $D640              ;
D638: 8E 71 14      LDX   #$7114             ;player 2 lives start position?
D63B: B6 A2 06      LDA   $A206              ;get # of lives for player 2
D63E: 8D 02         BSR   $D642              ;Go paint in player 2's reserve ships
D640: 35 F6         PULS  A,B,X,Y,U,PC       ;



;SUBRTN
D642: 81 05         CMPA  #$05               ;
D644: 23 02         BLS   $D648              ;
D646: 86 05         LDA   #$05               ;only 5 lives allowed
D648: 34 02         PSHS  A                  ;
D64A: CC 20 06      LDD   #$2006             ;32 sets, 6 bytes each
D64D: BD F5 C7      JSR   ScrnBlkClr         ;Go clear the area out
D650: A6 E4         LDA   ,S                 ;How many extra lives do we have?
D652: 27 0F         BEQ   $D663              ;if zero, we're done here
D654: 10 8E F9 D5   LDY   #$F9D5             ;
D658: 1F 10         TFR   X,D                ;
D65A: BD F5 22      JSR   DrawChar           ;
D65D: 8B 06         ADDA  #$06               ;
D65F: 6A E4         DEC   ,S                 ;
D661: 26 F7         BNE   $D65A              ;
D663: 35 82         PULS  A,PC               ;



;SUBRTN
D665: 34 76         PSHS  U,Y,X,B,A          ;
D667: CC 40 20      LDD   #$4020             ;
D66A: 8E 30 08      LDX   #$3008             ;
D66D: BD F5 C7      JSR   ScrnBlkClr         ;
D670: 8D 4A         BSR   $D6BC              ;
D672: 8D B5         BSR   $D629              ;
D674: 8D 0A         BSR   $D680              ;
D676: 96 8C         LDA   <$8C               ;
D678: BD D3 DB      JSR   $D3DB              ;
D67B: 4A            DECA                     ;
D67C: 26 FA         BNE   $D678              ;
D67E: 35 F6         PULS  A,B,X,Y,U,PC       ;



;SUBRTN
D680: 34 76         PSHS  U,Y,X,B,A          ;
D682: 8E 29 1B      LDX   #$291B             ;
D685: B6 A1 CB      LDA   $A1CB              ;
D688: 8D 0F         BSR   $D699              ;
D68A: 96 8C         LDA   <$8C               ;
D68C: 4A            DECA                     ;
D68D: 27 08         BEQ   $D697              ;
D68F: 8E 8B 1B      LDX   #$8B1B             ;
D692: B6 A2 08      LDA   $A208              ;
D695: 8D 02         BSR   $D699              ;
D697: 35 F6         PULS  A,B,X,Y,U,PC       ;



;SUBRTN
D699: 81 03         CMPA  #$03               ;
D69B: 23 02         BLS   $D69F              ;
D69D: 86 03         LDA   #$03               ;
D69F: 34 02         PSHS  A                  ;
D6A1: CC 03 0B      LDD   #$030B             ;
D6A4: BD F5 C7      JSR   ScrnBlkClr         ;
D6A7: A6 E4         LDA   ,S                 ;
D6A9: 27 0F         BEQ   $D6BA              ;
D6AB: 10 8E F9 D9   LDY   #$F9D9             ;
D6AF: 1F 10         TFR   X,D                ;
D6B1: BD F5 22      JSR   DrawChar           ;
D6B4: CB 04         ADDB  #$04               ;
D6B6: 6A E4         DEC   ,S                 ;
D6B8: 26 F7         BNE   $D6B1              ;
D6BA: 35 82         PULS  A,PC               ;



;SUBRTN
D6BC: CC 55 55      LDD   #$5555             ;
D6BF: 8E 00 28      LDX   #$0028             ;
D6C2: ED 84         STD   ,X                 ;
D6C4: 30 89 01 00   LEAX  $0100,X            ;
D6C8: 8C 9C 00      CMPX  #$9C00             ;
D6CB: 25 F5         BCS   $D6C2              ;
D6CD: 8E 2F 08      LDX   #$2F08             ;
D6D0: ED 89 41 00   STD   $4100,X            ;
D6D4: ED 81         STD   ,X++               ;
D6D6: 8C 2F 28      CMPX  #$2F28             ;
D6D9: 26 F5         BNE   $D6D0              ;
D6DB: 8E 2F 07      LDX   #$2F07             ;
D6DE: A7 84         STA   ,X                 ;
D6E0: 30 89 01 00   LEAX  $0100,X            ;
D6E4: 8C 71 07      CMPX  #$7107             ;
D6E7: 26 F5         BNE   $D6DE              ;
D6E9: 8E 4C 07      LDX   #$4C07             ;
D6EC: CC 99 99      LDD   #$9999             ;
D6EF: ED 84         STD   ,X                 ;
D6F1: ED 88 21      STD   $21,X              ;
D6F4: 30 89 01 00   LEAX  $0100,X            ;
D6F8: 8C 54 07      CMPX  #$5407             ;
D6FB: 26 F2         BNE   $D6EF              ;
D6FD: 39            RTS                      ;



;SUBRTN
D6FE: 34 02         PSHS  A                  ;
D700: 96 8B         LDA   <$8B               ;
D702: 8E A1 C2      LDX   #$A1C2             ;
D705: 4A            DECA                     ;
D706: 27 03         BEQ   $D70B              ;
D708: 8E A1 FF      LDX   #$A1FF             ;
D70B: 35 82         PULS  A,PC               ;


;SUBRTN
D70D: 34 02         PSHS  A                  ;
D70F: 20 F1         BRA   $D702              ;



;SUBRTN
D711: 34 04         PSHS  B                  ;
D713: D6 DF         LDB   <$DF               ;
D715: 86 03         LDA   #$03               ;
D717: 3D            MUL                      ;
D718: CB 11         ADDB  #$11               ;
D71A: 96 E1         LDA   <$E1               ;
D71C: 44            LSRA                     ;
D71D: 44            LSRA                     ;
D71E: 44            LSRA                     ;
D71F: 98 E1         EORA  <$E1               ;
D721: 44            LSRA                     ;
D722: 06 E0         ROR   <$E0               ;
D724: 06 E1         ROR   <$E1               ;
D726: DB E1         ADDB  <$E1               ;
D728: D9 E0         ADCB  <$E0               ;
D72A: D7 DF         STB   <$DF               ;
D72C: 96 DF         LDA   <$DF               ;
D72E: 35 84         PULS  B,PC               ;

Data for setting up the PIAs

;DATA
D730: C0 FF 00 00                            ;   $C0,$FF,0,0   ;DDR values
D736: 14 05 34 3E                            ;   $14,5,$34,$3E ;CR values



;SUBRTN
D738: 1A FF         ORCC  #$FF               ;Set all flags?
D73A: 10 CE BF FF   LDS   #$BFFF             ;Initialize system stack address
D73E: 86 A0         LDA   #$A0               ;
D740: 1F 8B         TFR   A,DP               ;direct page will be at $A000 - $A0FF
D742: 7F D0 00      CLR   $D000              ;switch to the I/O page
D745: C6 04         LDB   #$04               ;loop counter setup
D747: CE CC 00      LDU   #PIA_addr_base     ;
D74A: 8E D7 30      LDX   #$D730             ;Constant data for setting up the PIA's
D74D: 6F 41         CLR   1,U                ;go to data direction register please
D74F: A6 80         LDA   ,X+                ;get data direction setting for this port
D751: A7 C1         STA   ,U++               ;set DDR
D753: A6 03         LDA   3,X                ;get control reg setting for this port
D755: A7 5F         STA   -1,U               ;set CR
D757: 5A            DECB                     ;decrement the count
D758: 26 F3         BNE   $D74D              ;loop if not done
D75A: BD F5 D1      JSR   VidMemClr          ;clear the video memory
D75D: 8E 9C 00      LDX   #$9C00             ;clear the rest of RAM
D760: 6F 80         CLR   ,X+                ;
D762: C6 38         LDB   #$38               ;
D764: F7 C3 FC      STB   $C3FC              ;reset watchdog
D767: 8C C0 00      CMPX  #$C000             ;
D76A: 26 F4         BNE   $D760              ;
D76C: 7F CC 00      CLR   PIA_addr_base      ;
D76F: 7F CC 02      CLR   $CC02              ;
D772: 8E C4 7D      LDX   #$C47D             ;
D775: BD F8 3A      JSR   SRAMByteRd         ;
D778: 1F 98         TFR   B,A                ;
D77A: 81 20         CMPA  #$20               ;
D77C: 22 06         BHI   $D784              ;
D77E: 84 0F         ANDA  #$0F               ;
D780: 81 09         CMPA  #$09               ;
D782: 23 01         BLS   $D785              ;
D784: 5F            CLRB                     ;
D785: D7 37         STB   <$37               ;
D787: CC A5 5A      LDD   #$A55A             ;
D78A: DD E0         STD   <$E0               ;
D78C: CC FF 70      LDD   #$FF70             ;
D78F: DD A1         STD   <$A1               ;
D791: 0F A3         CLR   <$A3               ;
D793: C6 FF         LDB   #$FF               ;
D795: DD 79         STD   <$79               ;
D797: BD D8 DC      JSR   $D8DC              ;
D79A: BD F5 07      JSR   ROMPg3             ;
D79D: BD C0 33      JSR   $C033              ;
D7A0: 8D 24         BSR   $D7C6              ;
D7A2: 8D 12         BSR   $D7B6              ;
D7A4: BD F8 00      JSR   $F800              ;clear <$49,<$52, put 3 in <$36,<$48, put $FFFF in <$59
D7A7: 8E D8 25      LDX   #$D825             ;
D7AA: 86 01         LDA   #$01               ;
D7AC: BD D0 55      JSR   $D055              ;
D7AF: 03 BA         COM   <$BA               ;
D7B1: 1C 00         ANDCC #$00               ;
D7B3: 7E E7 BE      JMP   $E7BE              ;



;SUBRTN
D7B6: 8D 3D         BSR   $D7F5              ;
D7B8: BD E6 9F      JSR   $E69F              ;
D7BB: BD E0 52      JSR   $E052              ;
D7BE: 8D 45         BSR   $D805              ;
D7C0: BD E5 4B      JSR   $E54B              ;
D7C3: 7E E1 49      JMP   $E149              ;



;SUBRTN
D7C6: 34 16         PSHS  X,B,A              ;
D7C8: 4F            CLRA                     ;
D7C9: 5F            CLRB                     ;
D7CA: 8E AA C5      LDX   #$AAC5             ;
D7CD: 9F 61         STX   <$61               ;
D7CF: 30 0F         LEAX  15,X               ;
D7D1: AF 11         STX   -15,X              ;
D7D3: 8C AF 1B      CMPX  #$AF1B             ;
D7D6: 26 F7         BNE   $D7CF              ;
D7D8: ED 84         STD   ,X                 ;
D7DA: DD 5F         STD   <$5F               ;
D7DC: 8E AF 2A      LDX   #$AF2A             ;
D7DF: 9F 69         STX   <$69               ;
D7E1: 30 88 17      LEAX  $17,X              ;
D7E4: AF 88 E9      STX   $-17,X             ;
D7E7: 8C AF 86      CMPX  #$AF86             ;
D7EA: 26 F5         BNE   $D7E1              ;
D7EC: ED 84         STD   ,X                 ;
D7EE: 8E A0 5F      LDX   #$A05F             ;
D7F1: 9F 63         STX   <$63               ;reset event chain to initial entry
D7F3: 35 96         PULS  A,B,X,PC           ;



;SUBRTN
D7F5: 8E F8 BE      LDX   #$F8BE             ;
D7F8: CE A0 26      LDU   #$A026             ;
D7FB: C6 10         LDB   #$10               ;
D7FD: A6 80         LDA   ,X+                ;
D7FF: A7 C0         STA   ,U+                ;
D801: 5A            DECB                     ;
D802: 26 F9         BNE   $D7FD              ;
D804: 39            RTS                      ;



;SUBRTN
D805: 34 17         PSHS  X,B,A,CC           ;
D807: 1A FF         ORCC  #$FF               ;
D809: 8E A2 3C      LDX   #$A23C             ;
D80C: 9F 67         STX   <$67               ;
D80E: 30 88 17      LEAX  $17,X              ;
D811: AF 88 E9      STX   $-17,X             ;
D814: 8C AA AE      CMPX  #$AAAE             ;
D817: 26 F5         BNE   $D80E              ;
D819: 4F            CLRA                     ;
D81A: 5F            CLRB                     ;
D81B: ED 84         STD   ,X                 ;
D81D: DD 6B         STD   <$6B               ;
D81F: DD 65         STD   <$65               ;
D821: DD 6D         STD   <$6D               ;
D823: 35 97         PULS  CC,A,B,X,PC        ;



D825: BD F5 0B      JSR   ROMPg1             ;page 1
D828: 7E C0 00      JMP   $C000              ;go to $C006 in bank 1



;SUBRTN
D82B: 8E C4 95      LDX   #$C495             ;
D82E: BD F8 22      JSR   RdSRAMbyte         ;
D831: 4A            DECA                     ;
D832: 26 04         BNE   $D838              ;
D834: 86 02         LDA   #$02               ;
D836: 97 37         STA   <$37               ;
D838: 39            RTS                      ;



D839: 96 BA         LDA   <$BA               ;
D83B: 2A 0E         BPL   $D84B              ;
D83D: 8D EC         BSR   $D82B              ;
D83F: 96 37         LDA   <$37               ;
D841: 27 08         BEQ   $D84B              ;
D843: CC D4 BD      LDD   #$D4BD             ;
D846: BD D5 4D      JSR   $D54D              ;
D849: 8D 16         BSR   $D861              ;
D84B: 7E D0 0A      JMP   $D00A              ;
D84E: 96 BA         LDA   <$BA               ;
D850: 2A F9         BPL   $D84B              ;
D852: 8D D7         BSR   $D82B              ;
D854: 96 37         LDA   <$37               ;
D856: 81 02         CMPA  #$02               ;
D858: 25 F1         BCS   $D84B              ;
D85A: 8D 05         BSR   $D861              ;
D85C: CC D4 C2      LDD   #$D4C2             ;
D85F: 20 E5         BRA   $D846              ;



;SUBRTN
D861: 0F 38         CLR   <$38               ;
D863: 12            NOP                      ;
D864: 96 B7         LDA   <$B7               ;
D866: 27 73         BEQ   $D8DB              ;
D868: 96 BA         LDA   <$BA               ;
D86A: 2A 58         BPL   $D8C4              ;
D86C: BD D0 7C      JSR   $D07C              ;
D86F: BD F5 D1      JSR   VidMemClr          ;
D872: 86 7F         LDA   #$7F               ;
D874: 97 BA         STA   <$BA               ;
D876: 86 01         LDA   #$01               ;
D878: 97 8B         STA   <$8B               ;
D87A: 97 25         STA   <$25               ;
D87C: 0F 8C         CLR   <$8C               ;
D87E: 8E A1 C2      LDX   #$A1C2             ;
D881: 6F 80         CLR   ,X+                ;
D883: 8C A2 3C      CMPX  #$A23C             ;
D886: 26 F9         BNE   $D881              ;
D888: 8E C4 85      LDX   #$C485             ;
D88B: BD F8 22      JSR   RdSRAMbyte         ;
D88E: 84 0F         ANDA  #$0F               ;
D890: B7 A1 C9      STA   $A1C9              ;
D893: C6 0A         LDB   #$0A               ;
D895: FD A1 CB      STD   $A1CB              ;
D898: 0F 39         CLR   <$39               ;
D89A: 12            NOP                      ;
D89B: 8E A1 C2      LDX   #$A1C2             ;
D89E: BD DE 7C      JSR   $DE7C              ;
D8A1: 8E C4 81      LDX   #$C481             ;
D8A4: BD F8 38      JSR   SRAMWordRd         ;
D8A7: DD AB         STD   <$AB               ;
D8A9: FD A1 C6      STD   $A1C6              ;
D8AC: 7F A1 C8      CLR   $A1C8              ;
D8AF: 8E A1 C2      LDX   #$A1C2             ;
D8B2: A6 80         LDA   ,X+                ;
D8B4: A7 88 3C      STA   $3C,X              ;
D8B7: 8C A1 FF      CMPX  #$A1FF             ;
D8BA: 26 F6         BNE   $D8B2              ;
D8BC: 8E D9 19      LDX   #$D919             ;
D8BF: 86 00         LDA   #$00               ;
D8C1: BD D0 55      JSR   $D055              ;
D8C4: 0C 8C         INC   <$8C               ;
D8C6: 96 37         LDA   <$37               ;
D8C8: 8B 99         ADDA  #$99               ;
D8CA: 19            DAA                      ;
D8CB: 97 37         STA   <$37               ;
D8CD: 8E C4 7D      LDX   #$C47D             ;
D8D0: BD F8 4E      JSR   WrSRAMbyte         ;
D8D3: 96 8C         LDA   <$8C               ;
D8D5: 4A            DECA                     ;
D8D6: 27 03         BEQ   $D8DB              ;
D8D8: BD D6 65      JSR   $D665              ;
D8DB: 39            RTS                      ;



;SUBRTN
D8DC: 34 12         PSHS  X,A                ;
D8DE: 96 36         LDA   <$36               ;
D8E0: 34 02         PSHS  A                  ;save page #
D8E2: 8E DF 17      LDX   #$DF17             ;
D8E5: CC 38 3C      LDD   #$383C             ;a $38 to clear the watchdog and $3C for PIA#2
D8E8: 20 15         BRA   $D8FF              ;

;SUBRTN
D8EA: 34 12         PSHS  X,A                ;
D8EC: 96 36         LDA   <$36               ;
D8EE: 34 02         PSHS  A                  ;save page #
D8F0: 4F            CLRA                     ;
D8F1: BD F5 0D      JSR   SwtchPgNum         ;
D8F4: B6 CC 06      LDA   $CC06              ;
D8F7: 2A E9         BPL   $D8E2              ;
D8F9: 8E DF C3      LDX   #$DFC3             ;
D8FC: CC 39 34      LDD   #$3934             ;a $39 to clear the watchdog and $34 for PIA#2
D8FF: 9F 90         STX   <$90               ;storing JMP value
D901: 0F 36         CLR   <$36               ;
D903: 7F D0 00      CLR   $D000              ;
D906: F7 CC 07      STB   $CC07              ;set CB2 of second PIA to appropriate value
D909: B7 C3 FC      STA   $C3FC              ;reset watchdog
D90C: 86 7E         LDA   #$7E               ;this a JMP instruction 
D90E: 97 8F         STA   <$8F               ;placed in front of the stored address at <$90
D910: 35 02         PULS  A                  ;
D912: 97 36         STA   <$36               ;
D914: B7 D0 00      STA   $D000              ;restore page #
D917: 35 92         PULS  A,X,PC             ;



D919: C6 07         LDB   #$07               ;
D91B: BD F5 1C      JSR   $F51C              ;
D91E: BD D7 B6      JSR   $D7B6              ;
D921: BD D0 7C      JSR   $D07C              ;
D924: 86 7F         LDA   #$7F               ;
D926: 97 BA         STA   <$BA               ;
D928: 9E 63         LDX   <$63               ;
D92A: 9C 5F         CMPX  <$5F               ;
D92C: 26 04         BNE   $D932              ;
D92E: AE 84         LDX   ,X                 ;
D930: 27 10         BEQ   $D942              ;
D932: 86 0F         LDA   #$0F               ;load InsertEventLink event count
D934: 8E D9 3A      LDX   #$D93A             ;load jump point for event return
D937: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
D93A: 96 7F         LDA   <$7F               ;
D93C: 9A 80         ORA   <$80               ;
D93E: 9A 7F         ORA   <$7F               ;
D940: 26 F0         BNE   $D932              ;
D942: BD D7 C6      JSR   $D7C6              ;
D945: 8E D9 50      LDX   #$D950             ;
D948: 86 00         LDA   #$00               ;
D94A: BD D0 55      JSR   $D055              ;
D94D: 7E E7 BE      JMP   $E7BE              ;

D950: 4F            CLRA                     ;
D951: BD F5 0D      JSR   SwtchPgNum         ;
D954: B6 CC 06      LDA   $CC06              ;
D957: 2A 15         BPL   $D96E              ;
D959: BD F5 D1      JSR   VidMemClr          ;
D95C: 96 8B         LDA   <$8B               ;
D95E: 4A            DECA                     ;
D95F: 26 05         BNE   $D966              ;
D961: BD D8 DC      JSR   $D8DC              ;
D964: 20 02         BRA   $D968              ;
D966: 8D 82         BSR   $D8EA              ;
D968: 86 FF         LDA   #$FF               ;
D96A: 97 7B         STA   <$7B               ;
D96C: 97 7C         STA   <$7C               ;
D96E: 4F            CLRA                     ;
D96F: 5F            CLRB                     ;
D970: DD 20         STD   <$20               ;
D972: DD 22         STD   <$22               ;
D974: BD F4 FF      JSR   ROMPg7             ;
D977: BD C0 06      JSR   $C006              ;
D97A: BD C0 00      JSR   $C000              ;
D97D: BD F5 F1      JSR   ClrVidMem          ;
D980: CC 03 00      LDD   #$0300             ;
D983: DD BD         STD   <$BD               ;
D985: DD BB         STD   <$BB               ;
D987: 0F AD         CLR   <$AD               ;
D989: 0F B5         CLR   <$B5               ;
D98B: 0F 8A         CLR   <$8A               ;
D98D: 0F AF         CLR   <$AF               ;
D98F: 0F 9A         CLR   <$9A               ;
D991: 0F 99         CLR   <$99               ;
D993: 8E A1 1A      LDX   #$A11A             ;
D996: 9F 9B         STX   <$9B               ;
D998: BD D6 FE      JSR   $D6FE              ;
D99B: 9F 8D         STX   <$8D               ;
D99D: A6 08         LDA   8,X                ;
D99F: 84 07         ANDA  #$07               ;
D9A1: CE DB 53      LDU   #$DB53             ;
D9A4: A6 C6         LDA   A,U                ;
D9A6: 97 2B         STA   <$2B               ;
D9A8: 6A 07         DEC   7,X                ;
D9AA: BD D6 65      JSR   $D665              ;
D9AD: CC 20 80      LDD   #$2080             ;
D9B0: DD C1         STD   <$C1               ;
D9B2: DD BF         STD   <$BF               ;
D9B4: CC 20 00      LDD   #$2000             ;
D9B7: DD C3         STD   <$C3               ;
D9B9: CC 08 00      LDD   #$0800             ;
D9BC: D3 20         ADDD  <$20               ;
D9BE: DD CC         STD   <$CC               ;
D9C0: CC 80 00      LDD   #$8000             ;
D9C3: DD C5         STD   <$C5               ;
D9C5: 4F            CLRA                     ;
D9C6: 5F            CLRB                     ;
D9C7: DD C7         STD   <$C7               ;
D9C9: 97 C9         STA   <$C9               ;
D9CB: DD CA         STD   <$CA               ;
D9CD: 8E E9 E3      LDX   #$E9E3             ;
D9D0: 86 00         LDA   #$00               ;
D9D2: BD D0 55      JSR   $D055              ;
D9D5: 8E E7 82      LDX   #$E782             ;
D9D8: 86 00         LDA   #$00               ;
D9DA: BD D0 55      JSR   $D055              ;
D9DD: 8E F4 93      LDX   #$F493             ;
D9E0: 86 00         LDA   #$00               ;
D9E2: BD D0 55      JSR   $D055              ;
D9E5: 8E E9 BF      LDX   #$E9BF             ;
D9E8: 86 00         LDA   #$00               ;
D9EA: BD D0 55      JSR   $D055              ;
D9ED: 8E F4 64      LDX   #$F464             ;
D9F0: 86 00         LDA   #$00               ;
D9F2: BD D0 55      JSR   $D055              ;
D9F5: 8E F4 3D      LDX   #$F43D             ;
D9F8: 86 00         LDA   #$00               ;
D9FA: BD D0 55      JSR   $D055              ;
D9FD: 96 25         LDA   <$25               ;
D9FF: 27 1E         BEQ   $DA1F              ;
DA01: D6 8C         LDB   <$8C               ;
DA03: 5A            DECB                     ;
DA04: 27 19         BEQ   $DA1F              ;
DA06: CE C0 EF      LDU   #$C0EF             ;
DA09: 96 8B         LDA   <$8B               ;
DA0B: 4A            DECA                     ;
DA0C: 27 03         BEQ   $DA11              ;
DA0E: CE C0 F1      LDU   #$C0F1             ;
DA11: 8E 3C 80      LDX   #$3C80             ;
DA14: BD F5 13      JSR   $F513              ;
DA17: 86 80         LDA   #$80               ;load InsertEventLink event count
DA19: 8E DA 1F      LDX   #$DA1F             ;load jump point for event return
DA1C: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
DA1F: BD F5 F1      JSR   ClrVidMem          ;
DA22: C6 05         LDB   #$05               ;
DA24: 9E 8D         LDX   <$8D               ;
DA26: A6 0A         LDA   10,X               ;
DA28: 8D 15         BSR   $DA3F              ;
DA2A: 86 60         LDA   #$60               ;load InsertEventLink event count
DA2C: 8E DA 32      LDX   #$DA32             ;load jump point for event return
DA2F: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
DA32: BD DC 1E      JSR   $DC1E              ;
DA35: 8D 05         BSR   $DA3C              ;
DA37: 0F 25         CLR   <$25               ;
DA39: 7E DC D9      JMP   $DCD9              ;



;SUBRTN
DA3C: 5F            CLRB                     ;
;SUBRTN
DA3D: 96 FA         LDA   <$FA               ;
;SUBRTN
DA3F: 26 02         BNE   $DA43              ;
DA41: CA 02         ORB   #$02               ;
DA43: D7 BA         STB   <$BA               ;if value in <$FA is not zero, we clear <$BA, otherwise put a 2 in there
DA45: 39            RTS                      ;



DA46: C6 58         LDB   #$58               ;
DA48: 8D F3         BSR   $DA3D              ;
DA4A: DC 20         LDD   <$20               ;
DA4C: DD 22         STD   <$22               ;
DA4E: 9E BF         LDX   <$BF               ;
DA50: CC 08 06      LDD   #$0806             ;
DA53: BD F5 C7      JSR   ScrnBlkClr         ;
DA56: BD DB B6      JSR   $DBB6              ;
DA59: CC D4 B5      LDD   #$D4B5             ;
DA5C: BD D5 4D      JSR   $D54D              ;
DA5F: 10 8E F9 C1   LDY   #$F9C1             ;
DA63: 96 BB         LDA   <$BB               ;
DA65: 2A 04         BPL   $DA6B              ;
DA67: 10 8E F9 CB   LDY   #$F9CB             ;
DA6B: 8E DB 4B      LDX   #$DB4B             ;
DA6E: AF 47         STX   7,U                ;
DA70: CE AF DD      LDU   #$AFDD             ;
DA73: BD DB 5C      JSR   $DB5C              ;
DA76: 1F 31         TFR   U,X                ;
DA78: DE 63         LDU   <$63               ;
DA7A: AF 4B         STX   11,U               ;
;service entry on InsertEventLink event link
DA7C: DC C1         LDD   <$C1               ;
DA7E: 10 AE 4B      LDY   11,U               ;
DA81: BD F5 7B      JSR   ScrnBlkClrP2       ;
DA84: 86 02         LDA   #$02               ;load InsertEventLink event count
DA86: 8E DA 8C      LDX   #$DA8C             ;load jump point for event return
DA89: 7E D0 01      JMP   InsertEventLink    ;
;service entry on InsertEventLink event link
DA8C: DC C1         LDD   <$C1               ;
DA8E: 10 AE 4B      LDY   11,U               ;
DA91: BD F5 22      JSR   DrawChar           ;
DA94: AE 47         LDX   7,U                ;
DA96: A6 80         LDA   ,X+                ;
DA98: 27 0E         BEQ   $DAA8              ;
DA9A: 97 31         STA   <$31               ;
DA9C: 0F 26         CLR   <$26               ;
DA9E: AF 47         STX   7,U                ;
DAA0: 86 02         LDA   #$02               ;load InsertEventLink event count
DAA2: 8E DA 7C      LDX   #$DA7C             ;load jump point for event return
DAA5: 7E D0 01      JMP   InsertEventLink    ;
DAA8: 86 7F         LDA   #$7F               ;
DAAA: 97 BA         STA   <$BA               ;
DAAC: 86 FF         LDA   #$FF               ;
DAAE: 97 26         STA   <$26               ;
DAB0: 86 02         LDA   #$02               ;load InsertEventLink event count
DAB2: 8E DA B8      LDX   #$DAB8             ;load jump point for event return
DAB5: 7E D0 01      JMP   InsertEventLink    ;
;service entry on InsertEventLink event link
DAB8: 0F 26         CLR   <$26               ;
DABA: BD D0 7C      JSR   $D07C              ;
DABD: 9E C1         LDX   <$C1               ;
DABF: 30 89 04 03   LEAX  $0403,X            ;
DAC3: BD F4 FF      JSR   ROMPg7             ;
DAC6: BD C0 0E      JSR   $C00E              ;$C5D0 of bank 7
DAC9: BD D3 D9      JSR   $D3D9              ;
DACC: 0F B3         CLR   <$B3               ;
DACE: C6 13         LDB   #$13               ;
DAD0: BD D5 39      JSR   $D539              ;play sound $13
DAD3: BD DD AE      JSR   $DDAE              ;
DAD6: 26 06         BNE   $DADE              ;
DAD8: BD DD EC      JSR   $DDEC              ;
DADB: BD F5 F1      JSR   ClrVidMem          ;
DADE: 96 8B         LDA   <$8B               ;
DAE0: 9E 8D         LDX   <$8D               ;
DAE2: E6 07         LDB   7,X                ;
DAE4: 26 2F         BNE   $DB15              ;
DAE6: D6 8C         LDB   <$8C               ;
DAE8: 5A            DECB                     ;
DAE9: 27 41         BEQ   $DB2C              ;
DAEB: 88 03         EORA  #$03               ;
DAED: BD D7 0D      JSR   $D70D              ;
DAF0: E6 07         LDB   7,X                ;
DAF2: 27 38         BEQ   $DB2C              ;
DAF4: CE C0 EF      LDU   #$C0EF             ;
DAF7: 81 02         CMPA  #$02               ;
DAF9: 27 03         BEQ   $DAFE              ;
DAFB: CE C0 F1      LDU   #$C0F1             ;
DAFE: 8E 3C 78      LDX   #$3C78             ;
DB01: BD F5 13      JSR   $F513              ;
DB04: CE C0 75      LDU   #$C075             ;
DB07: 8E 3E 88      LDX   #$3E88             ;
DB0A: BD F5 13      JSR   $F513              ;
DB0D: 86 60         LDA   #$60               ;load InsertEventLink event count
DB0F: 8E DB 15      LDX   #$DB15             ;load jump point for event return
DB12: 7E D0 01      JMP   InsertEventLink    ;
;service entry on InsertEventLink event link
DB15: 96 8B         LDA   <$8B               ;
DB17: 4C            INCA                     ;
DB18: 91 8C         CMPA  <$8C               ;
DB1A: 23 02         BLS   $DB1E              ;
DB1C: 86 01         LDA   #$01               ;
DB1E: BD D7 0D      JSR   $D70D              ;
DB21: E6 07         LDB   7,X                ;
DB23: 27 F2         BEQ   $DB17              ;
DB25: 97 8B         STA   <$8B               ;
DB27: 0C 25         INC   <$25               ;
DB29: 7E D9 19      JMP   $D919              ;
DB2C: CE C0 75      LDU   #$C075             ;
DB2F: 8E 3E 80      LDX   #$3E80             ;
DB32: 86 FF         LDA   #$FF               ;
DB34: 97 BA         STA   <$BA               ;
DB36: BD F5 13      JSR   $F513              ;
DB39: 0F B3         CLR   <$B3               ;
DB3B: C6 13         LDB   #$13               ;
DB3D: BD D5 39      JSR   $D539              ;send sound code $13 to sound board
DB40: 86 28         LDA   #$28               ;load InsertEventLink event count
DB42: 8E DB 48      LDX   #$DB48             ;load jump point for event return
DB45: 7E D0 01      JMP   InsertEventLink    ;


;service entry on InsertEventLink event link
DB48: 7E D8 25      JMP   $D825              ;

;out of sync here?
DB4B: 07 07         ASR   <$07               ;
DB4D: 07 0F         ASR   <$0F               ;
DB4F: 3F            SWI                      ;
DB50: 7F FF FF      CLR   $FFFF              ;
DB53: 00 81         NEG   <$81               ;
DB55: 28 07         BVC   $DB5E              ;
DB57: 16 2F 84      LBRA  $0ADE              ;
DB5A: 15 
DB5B: 00
;got out of sync somewhere back there

;SUBRTN
DB5C: 34 56         PSHS  U,X,B,A            ;
DB5E: BD F5 03      JSR   ROMPg2             ;
DB61: EC A4         LDD   ,Y                 ;
DB63: ED C4         STD   ,U                 ;
DB65: 3D            MUL                      ;
DB66: 30 4A         LEAX  10,U               ;
DB68: AF 42         STX   2,U                ;
DB6A: 30 8B         LEAX  D,X                ;
DB6C: AF 44         STX   4,U                ;
DB6E: 34 10         PSHS  X                  ;
DB70: 30 8B         LEAX  D,X                ;
DB72: 34 10         PSHS  X                  ;
DB74: EC 26         LDD   6,Y                ;
DB76: ED 46         STD   6,U                ;
DB78: EC 28         LDD   8,Y                ;
DB7A: ED 48         STD   8,U                ;
DB7C: AE 22         LDX   2,Y                ;
DB7E: 33 4A         LEAU  10,U               ;
DB80: 8D 0E         BSR   $DB90              ;
DB82: AE 24         LDX   4,Y                ;
DB84: EE 62         LDU   2,S                ;
DB86: EC E4         LDD   ,S                 ;
DB88: ED 62         STD   2,S                ;
DB8A: 8D 04         BSR   $DB90              ;
DB8C: 32 64         LEAS  4,S                ;
DB8E: 35 D6         PULS  A,B,X,U,PC         ;


;SUBRTN
DB90: EC 81         LDD   ,X++               ;
DB92: 85 F0         BITA  #$F0               ;
DB94: 27 02         BEQ   $DB98              ;
DB96: 8A F0         ORA   #$F0               ;
DB98: 85 0F         BITA  #$0F               ;
DB9A: 27 02         BEQ   $DBA4              ;
DB9C: 8A 0F         ORA   #$0F               ;
DB9E: C5 F0         BITB  #$F0               ;
DBA0: 27 02         BEQ   $DBA4              ;
DBA2: CA F0         ORB   #$F0               ;
DBA4: C5 0F         BITB  #$0F               ;
DBA6: 27 02         BEQ   $DBAA              ;
DBA8: CA 0F         ORB   #$0F               ;
DBAA: 84 BB         ANDA  #$BB               ;
DBAC: C4 BB         ANDB  #$BB               ;
DBAE: ED C1         STD   ,U++               ;
DBB0: 11 A3 64      CMPU  4,S                ;
DBB3: 25 DB         BCS   $DB90              ;
DBB5: 39            RTS                      ;


;SUBRTN
DBB6: 34 56         PSHS  U,X,B,A            ;
DBB8: DE 8D         LDU   <$8D               ;
DBBA: 33 4A         LEAU  10,U               ;
DBBC: 86 33         LDA   #$33               ;
DBBE: 6F C0         CLR   ,U+                ;
DBC0: 4A            DECA                     ;
DBC1: 26 FB         BNE   $DBBE              ;
DBC3: DE 8D         LDU   <$8D               ;
DBC5: 96 FA         LDA   <$FA               ;
DBC7: A7 4A         STA   10,U               ;
DBC9: 33 4B         LEAU  11,U               ;
DBCB: 8E A0 FB      LDX   #$A0FB             ;
DBCE: A6 80         LDA   ,X+                ;
DBD0: 8C A1 00      CMPX  #$A100             ;
DBD3: 22 03         BHI   $DBD8              ;
DBD5: AB 88 16      ADDA  $16,X              ;
DBD8: A7 C0         STA   ,U+                ;
DBDA: 8C A1 12      CMPX  #$A112             ;
DBDD: 26 EF         BNE   $DBCE              ;
DBDF: 35 D6         PULS  A,B,X,U,PC         ;

;SUBRTN
DBE1: 34 06         PSHS  B,A                ;
DBE3: 97 74         STA   <$74               ;
DBE5: BD D0 95      JSR   $D095              ;
DBE8: F9 01 ED      ADCB  $01ED              ;
DBEB: 70 66 66      NEG   $6666              ;
DBEE: BD D7 11      JSR   $D711              ;
DBF1: DC E0         LDD   <$E0               ;
DBF3: 84 1F         ANDA  #$1F               ;
DBF5: AB 61         ADDA  1,S                ;
DBF7: ED 0A         STD   10,X               ;
DBF9: 54            LSRB                     ;
DBFA: 24 05         BCC   $DC01              ;
DBFC: CC F9 15      LDD   #$F915             ;
DBFF: ED 02         STD   2,X                ;
DC01: 86 E0         LDA   #$E0               ;
DC03: A7 0C         STA   12,X               ;
DC05: 86 10         LDA   #$10               ;
DC07: A7 88 14      STA   $14,X              ;
DC0A: 4F            CLRA                     ;
DC0B: 5F            CLRB                     ;
DC0C: ED 88 10      STD   $10,X              ;
DC0F: ED 0E         STD   14,X               ;
DC11: ED 06         STD   6,X                ;
DC13: 9F 65         STX   <$65               ;
DC15: AF A1         STX   ,Y++               ;
DC17: 0A 74         DEC   <$74               ;
DC19: 26 CA         BNE   $DBE5              ;
DC1B: 35 86         PULS  A,B,PC             ;


;out of sync?
DC1D: 0C
;SUBRTN
DC1E: 8E EC C9      LDX   #$ECC9             ;
DC21: 86 00         LDA   #$0                ;
DC23: BD D0 55      JSR   $D055              ;
DC26: CE A1 1A      LDU   #$A11A             ;
DC29: 31 C4         LEAY  ,U                 ;
DC2B: EF 07         STU   7,X                ;
DC2D: 6F C0         CLR   ,U+                ;
DC2F: 11 83 A1 42   CMPU  #$A142             ;
DC33: 26 F8         BNE   $DC2D              ;
DC35: DE 8D         LDU   <$8D               ;
DC37: A6 4A         LDA   10,U               ;
DC39: 97 FA         STA   <$FA               ;
DC3B: 27 20         BEQ   $DC5D              ;
DC3D: 81 07         CMPA  #$07               ;
DC3F: 23 10         BLS   $DC51              ;
DC41: 44            LSRA                     ;
DC42: 44            LSRA                     ;
DC43: 5F            CLRB                     ;
DC44: 8D 9B         BSR   $DBE1              ;
DC46: CB 40         ADDB  #$40               ;
DC48: 26 FA         BNE   $DC44              ;
DC4A: 48            ASLA                     ;
DC4B: 48            ASLA                     ;
DC4C: 40            NEGA                     ;
DC4D: AB 4A         ADDA  10,U               ;
DC4F: 27 0C         BEQ   $DC5D              ;
DC51: 97 73         STA   <$73               ;
DC53: D6 E0         LDB   <$E0               ;
DC55: 86 01         LDA   #$01               ;
DC57: 8D 88         BSR   $DBE1              ;
DC59: 0A 73         DEC   <$73               ;
DC5B: 26 F6         BNE   $DC53              ;
DC5D: DE 8D         LDU   <$8D               ;
DC5F: 33 4B         LEAU  11,U               ;
DC61: 8E A0 FB      LDX   #$A0FB             ;
DC64: A6 C0         LDA   ,U+                ;
DC66: A7 80         STA   ,X+                ;
DC68: 8C A1 12      CMPX  #$A112             ;
DC6B: 26 F7         BNE   $DC64              ;
DC6D: 8E A1 12      LDX   #$A112             ;
DC70: 6F 80         CLR   ,X+                ;
DC72: 8C A1 1A      CMPX  #$A11A             ;
DC75: 26 F9         BNE   $DC70              ;
DC77: BD D0 AD      JSR   $D0AD              ;
DC7A: 96 DF         LDA   <$DF               ;
DC7C: 44            LSRA                     ;
DC7D: 8B 2A         ADDA  #$2A               ;
DC7F: A7 0C         STA   12,X               ;
DC81: BD D7 11      JSR   $D711              ;
DC84: 84 3F         ANDA  #$3F               ;
DC86: 8B 80         ADDA  #$80               ;
DC88: D3 20         ADDD  <$20               ;
DC8A: ED 0A         STD   10,X               ;
DC8C: 96 FF         LDA   <$FF               ;
DC8E: 27 19         BEQ   $DCA9              ;
DC90: 81 06         CMPA  #$06               ;
DC92: 23 02         BLS   $DC96              ;
DC94: 86 06         LDA   #$06               ;
DC96: 31 84         LEAY  ,X                 ;
DC98: BD EB 9E      JSR   $EB9E              ;
DC9B: 9E 67         LDX   <$67               ;
DC9D: AF A4         STX   ,Y                 ;
DC9F: 10 9F 67      STY   <$67               ;
DCA2: 40            NEGA                     ;
DCA3: 9B FF         ADDA  <$FF               ;
DCA5: 97 FF         STA   <$FF               ;
DCA7: 26 CE         BNE   $DC77              ;
DCA9: 96 FE         LDA   <$FE               ;
DCAB: 27 05         BEQ   $DCB2              ;
DCAD: BD EF 15      JSR   $EF15              ;
DCB0: 0F FE         CLR   <$FE               ;
DCB2: 96 FD         LDA   <$FD               ;
DCB4: B7 A1 14      STA   $A114              ;
DCB7: 27 05         BEQ   $DCBE              ;
DCB9: 0F FD         CLR   <$FD               ;
DCBB: BD EB 36      JSR   $EB36              ;
DCBE: 96 FC         LDA   <$FC               ;
DCC0: B7 A1 13      STA   $A113              ;
DCC3: 27 13         BEQ   $DCD8              ;
DCC5: 81 03         CMPA  #$03               ;
DCC7: 23 02         BLS   $DCCB              ;
DCC9: 86 03         LDA   #$03               ;
DCCB: 34 02         PSHS  A                  ;
DCCD: BD F2 9D      JSR   $F29D              ;
DCD0: 96 FC         LDA   <$FC               ;
DCD2: A0 E0         SUBA  ,S+                ;
DCD4: 97 FC         STA   <$FC               ;
DCD6: 26 ED         BNE   $DCC5              ;
DCD8: 39            RTS                      ;

DCD9: DE 63         LDU   <$63               ;
DCDB: 86 28         LDA   #$28               ;
DCDD: A7 47         STA   7,U                ;
DCDF: B6 A1 0F      LDA   $A10F              ;
DCE2: B7 A1 18      STA   $A118              ;
DCE5: 86 01         LDA   #$01               ;
DCE7: B7 A1 17      STA   $A117              ;
;service entry on InsertEventLink event link
DCEA: 96 BA         LDA   <$BA               ;
DCEC: 85 08         BITA  #$08               ;
DCEE: 26 7C         BNE   $DD6C              ;
DCF0: BD DD AE      JSR   $DDAE              ;
DCF3: 26 14         BNE   $DD09              ;
DCF5: 86 77         LDA   #$77               ;
DCF7: 97 BA         STA   <$BA               ;
DCF9: BD D0 7C      JSR   $D07C              ;
DCFC: BD DB B6      JSR   $DBB6              ;
DCFF: BD DD EC      JSR   $DDEC              ;
DD02: 9E 8D         LDX   <$8D               ;
DD04: 6C 07         INC   7,X                ;
DD06: 7E D9 1E      JMP   $D91E              ;
DD09: 81 08         CMPA  #$08               ;
DD0B: 22 12         BHI   $DD1F              ;
DD0D: F6 A1 0F      LDB   $A10F              ;
DD10: 54            LSRB                     ;
DD11: 81 03         CMPA  #$03               ;
DD13: 22 01         BHI   $DD16              ;
DD15: 54            LSRB                     ;
DD16: 5C            INCB                     ;
DD17: F1 A1 18      CMPB  $A118              ;
DD1A: 24 03         BCC   $DD1F              ;
DD1C: F7 A1 18      STB   $A118              ;
DD1F: 7A A1 18      DEC   $A118              ;
DD22: 26 1C         BNE   $DD40              ;
DD24: 81 04         CMPA  #$04               ;
DD26: B6 A1 0F      LDA   $A10F              ;
DD29: 24 05         BCC   $DD30              ;
DD2B: 44            LSRA                     ;
DD2C: 44            LSRA                     ;
DD2D: BD DD 9E      JSR   $DD9E              ;
DD30: B7 A1 18      STA   $A118              ;
DD33: B6 A1 19      LDA   $A119              ;
DD36: 81 0C         CMPA  #$0C               ;
DD38: 24 06         BCC   $DD40              ;
DD3A: BD EA 80      JSR   $EA80              ;
DD3D: 7C A1 19      INC   $A119              ;
DD40: 7A A1 17      DEC   $A117              ;
DD43: 27 05         BEQ   $DD4A              ;
DD45: B6 A1 12      LDA   $A112              ;
DD48: 26 22         BNE   $DD6C              ;
DD4A: B6 A1 00      LDA   $A100              ;
DD4D: B7 A1 17      STA   $A117              ;
DD50: 96 FB         LDA   <$FB               ;
DD52: 27 18         BEQ   $DD6C              ;
DD54: B6 A1 12      LDA   $A112              ;
DD57: 81 08         CMPA  #$08               ;
DD59: 24 11         BCC   $DD6C              ;
DD5B: B6 A1 01      LDA   $A101              ;
DD5E: 91 FB         CMPA  <$FB               ;
DD60: 23 02         BLS   $DD64              ;
DD62: 96 FB         LDA   <$FB               ;
DD64: BD EF 9C      JSR   $EF9C              ;
DD67: 40            NEGA                     ;
DD68: 9B FB         ADDA  <$FB               ;
DD6A: 97 FB         STA   <$FB               ;
DD6C: 96 AE         LDA   <$AE               ;
DD6E: 81 10         CMPA  #$10               ;
DD70: 24 02         BCC   $DD74              ;
DD72: 0C AE         INC   <$AE               ;
DD74: 96 24         LDA   <$24               ;
DD76: 4C            INCA                     ;
DD77: 81 F0         CMPA  #$F0               ;
DD79: 23 06         BLS   $DD81              ;
DD7B: C6 06         LDB   #$06               ;
DD7D: BD F5 1C      JSR   $F51C              ;
DD80: 4F            CLRA                     ;
DD81: 97 24         STA   <$24               ;
DD83: DE 63         LDU   <$63               ;
DD85: 6A 47         DEC   7,U                ;
DD87: 26 0D         BNE   $DD96              ;
DD89: C6 02         LDB   #$02               ;
DD8B: 10 8E A0 FB   LDY   #$A0FB             ;
DD8F: BD DE EC      JSR   $DEEC              ;
DD92: 86 28         LDA   #$28               ;
DD94: A7 47         STA   7,U                ;
DD96: 86 0F         LDA   #$0F               ;load InsertEventLink event count
DD98: 8E DC EA      LDX   #$DCEA             ;load jump point for event return
DD9B: 7E D0 01      JMP   InsertEventLink    ;


;SUBRTN
DD9E: 34 02         PSHS  A                  ;
DDA0: BD D7 11      JSR   $D711              ;
DDA3: A1 E4         CMPA  ,S                 ;
DDA5: 23 03         BLS   $DDAA              ;
DDA7: 44            LSRA                     ;
DDA8: 20 F9         BRA   $DDA3              ;
DDAA: 4C            INCA                     ;
DDAB: 32 61         LEAS  1,S                ;
DDAD: 39            RTS                      ;

;SUBRTN
DDAE: B6 A1 12      LDA   $A112              ;
DDB1: 9B FB         ADDA  <$FB               ;
DDB3: BB A1 13      ADDA  $A113              ;
DDB6: BB A1 14      ADDA  $A114              ;
DDB9: BB A1 16      ADDA  $A116              ;
DDBC: BB A1 15      ADDA  $A115              ;
DDBF: 9B FE         ADDA  <$FE               ;
DDC1: 39            RTS                      ;

;SUBRTN
DDC2: 34 04         PSHS  B                  ;
DDC4: 5F            CLRB                     ;
DDC5: 81 10         CMPA  #$10               ;
DDC7: 25 06         BCS   $DDCF              ;
DDC9: CB 0A         ADDB  #$0A               ;
DDCB: 80 10         SUBA  #$10               ;
DDCD: 20 F6         BRA   $DDC5              ;
DDCF: 34 04         PSHS  B                  ;
DDD1: AB E0         ADDA  ,S+                ;
DDD3: 35 84         PULS  B,PC               ;

;SUBRTN
DDD5: 34 04         PSHS  B                  ;
DDD7: 1F 89         TFR   A,B                ;
DDD9: 4F            CLRA                     ;
DDDA: C1 0A         CMPB  #$0A               ;
DDDC: 25 07         BCS   $DDE5              ;
DDDE: 8B 10         ADDA  #$10               ;
DDE0: 19            DAA                      ;
DDE1: C0 0A         SUBB  #$0A               ;
DDE3: 20 F5         BRA   $DDDA              ;
DDE5: 34 04         PSHS  B                  ;
DDE7: AB E0         ADDA  ,S+                ;
DDE9: 19            DAA                      ;
DDEA: 35 84         PULS  B,PC               ;

;SUBRTN
DDEC: 0F 26         CLR   <$26               ;
DDEE: DE 63         LDU   <$63               ;
DDF0: 35 10         PULS  X                  ;
DDF2: AF 4D         STX   13,U               ;
DDF4: BD F5 F1      JSR   ClrVidMem          ;
DDF7: CE C0 F9      LDU   #$C0F9             ;
DDFA: 8E 38 50      LDX   #$3850             ;
DDFD: BD F5 13      JSR   $F513              ;
DE00: 9E 8D         LDX   <$8D               ;
DE02: A6 08         LDA   8,X                ;
DE04: 8D CF         BSR   $DDD5              ;
DE06: 1F 89         TFR   A,B                ;
DE08: 4F            CLRA                     ;
DE09: 9E 50         LDX   <$50               ;
DE0B: BD C0 0E      JSR   $C00E              ;probable bank 2, address $CBC1, or bank 7, address $C5D0
DE0E: 8E 3D 60      LDX   #$3D60             ;
DE11: CE C0 FB      LDU   #$C0FB             ;
DE14: BD F5 13      JSR   $F513              ;
DE17: CE C0 F3      LDU   #$C0F3             ;
DE1A: 8E 3C 90      LDX   #$3C90             ;
DE1D: BD F5 13      JSR   $F513              ;
DE20: 9E 8D         LDX   <$8D               ;
DE22: 5F            CLRB                     ;
DE23: A6 08         LDA   8,X                ;
DE25: 81 05         CMPA  #$05               ;
DE27: 23 02         BLS   $DE2B              ;
DE29: 86 05         LDA   #$05               ;
DE2B: 9E 50         LDX   <$50               ;
DE2D: BD C0 0E      JSR   $C00E              ;probable bank 2, address $CBC1, or bank 7, address $C5D0
DE30: DE 63         LDU   <$63               ;
DE32: 8E 3C A0      LDX   #$3CA0             ;
DE35: 96 FA         LDA   <$FA               ;
DE37: A7 49         STA   9,U                ;
DE39: 27 31         BEQ   $DE6C              ;
DE3B: 1F 10         TFR   X,D                ;
DE3D: 10 8E F9 15   LDY   #$F915             ;
DE41: BD F5 22      JSR   DrawChar           ;
DE44: 30 89 04 00   LEAX  $0400,X            ;
DE48: 86 01         LDA   #$01               ;
DE4A: 10 9E 8D      LDY   <$8D               ;
DE4D: E6 28         LDB   8,Y                ;
DE4F: C1 05         CMPB  #$05               ;
DE51: 25 02         BCS   $DE55              ;
DE53: C6 05         LDB   #$05               ;
DE55: 58            ASLB                     ;
DE56: 58            ASLB                     ;
DE57: 58            ASLB                     ;
DE58: 58            ASLB                     ;
DE59: BD D3 60      JSR   $D360              ;
DE5C: AF 47         STX   7,U                ;
DE5E: 86 04         LDA   #$04               ;load InsertEventLink event count
DE60: 8E DE 66      LDX   #$DE66             ;load jump point for event return
DE63: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
DE66: AE 47         LDX   7,U                ;
DE68: 6A 49         DEC   9,U                ;
DE6A: 26 CF         BNE   $DE3B              ;
DE6C: 9E 8D         LDX   <$8D               ;
DE6E: BD DE 7C      JSR   $DE7C              ;
DE71: 86 80         LDA   #$80               ;load InsertEventLink event count
DE73: 8E DE 79      LDX   #$DE79             ;load jump point for event return
DE76: 7E D0 01      JMP   InsertEventLink    ;
;service entry on InsertEventLink event link
DE79: 6E D8 0D      JMP   [$0D,U]            ;


;SUBRTN
DE7C: 34 56         PSHS  U,X,B,A            ;
DE7E: 6C 08         INC   8,X                ;
DE80: 8E C4 9D      LDX   #$C49D             ;
DE83: BD F8 22      JSR   RdSRAMbyte         ;
DE86: 97 73         STA   <$73               ;
DE88: AE 62         LDX   2,S                ;
DE8A: 4D            TSTA                     ;
DE8B: 27 0C         BEQ   $DE99              ;
DE8D: A6 08         LDA   8,X                ;
DE8F: 90 73         SUBA  <$73               ;
DE91: 25 06         BCS   $DE99              ;
DE93: 26 FA         BNE   $DE8F              ;
DE95: 86 0A         LDA   #$0A               ;
DE97: A7 0A         STA   10,X               ;
DE99: BD F4 FF      JSR   ROMPg7             ;
DE9C: A6 08         LDA   8,X                ;
DE9E: 34 02         PSHS  A                  ;
DEA0: 81 04         CMPA  #$04               ;
DEA2: 23 02         BLS   $DEA6              ;
DEA4: 86 04         LDA   #$04               ;
DEA6: FE C0 11      LDU   $C011              ;
DEA9: 8B 03         ADDA  #$03               ;
DEAB: 30 0B         LEAX  11,X               ;
DEAD: E6 C6         LDB   A,U                ;
DEAF: E7 80         STB   ,X+                ;
DEB1: 33 48         LEAU  8,U                ;
DEB3: 11 B3 C0 13   CMPU  $C013              ;
DEB7: 26 F4         BNE   $DEAD              ;
DEB9: 35 02         PULS  A                  ;
DEBB: 80 04         SUBA  #$04               ;
DEBD: 24 01         BCC   $DEC0              ;
DEBF: 4F            CLRA                     ;
DEC0: 97 73         STA   <$73               ;
DEC2: 8E C4 97      LDX   #$C497             ;
DEC5: BD F8 38      JSR   SRAMWordRd         ;
DEC8: BD DD C2      JSR   $DDC2              ;
DECB: 9B 73         ADDA  <$73               ;
DECD: 97 73         STA   <$73               ;
DECF: 27 19         BEQ   $DEEA              ;
DED1: 1F 98         TFR   B,A                ;
DED3: BD DD C2      JSR   $DDC2              ;
DED6: 91 73         CMPA  <$73               ;
DED8: 24 02         BCC   $DEDC              ;
DEDA: 97 73         STA   <$73               ;
DEDC: 96 73         LDA   <$73               ;
DEDE: C6 03         LDB   #$03               ;
DEE0: BD D6 FE      JSR   $D6FE              ;
DEE3: 31 0B         LEAY  11,X               ;
DEE5: 8D 05         BSR   $DEEC              ;
DEE7: 4A            DECA                     ;
DEE8: 26 F4         BNE   $DEDE              ;
DEEA: 35 D6         PULS  A,B,X,U,PC         ;

;SUBRTN
DEEC: 34 32         PSHS  Y,X,A              ;
DEEE: BD F4 FF      JSR   ROMPg7             ;
DEF1: BE C0 11      LDX   $C011              ;
DEF4: A6 85         LDA   B,X                ;
DEF6: 2B 0A         BMI   $DF02              ;
DEF8: AB A4         ADDA  ,Y                 ;
DEFA: 25 10         BCS   $DF0C              ;
DEFC: A1 84         CMPA  ,X                 ;
DEFE: 22 0C         BHI   $DF0C              ;
DF00: 20 08         BRA   $DF0A              ;
DF02: AB A4         ADDA  ,Y                 ;
DF04: 24 06         BCC   $DF0C              ;
DF06: A1 01         CMPA  1,X                ;
DF08: 25 02         BCS   $DF0C              ;
DF0A: A7 A4         STA   ,Y                 ;
DF0C: 31 21         LEAY  1,Y                ;
DF0E: 30 08         LEAX  8,X                ;
DF10: BC C0 13      CMPX  $C013              ;
DF13: 26 DF         BNE   $DEF4              ;
DF15: 35 B2         PULS  A,X,Y,PC           ;

IRQ handlers. 

;one of two possible routines for handling an IRQ. The other one is at $DFC3
DF17: 7F D0 00      CLR   $D000              ;
DF1A: 86 A0         LDA   #$A0               ;need to handle the possibility of the DP having been changed from $A0
DF1C: 1F 8B         TFR   A,DP               ;to some other possible DP value
DF1E: 86 04         LDA   #$04               ;
DF20: B7 CC 03      STA   $CC03              ;
DF23: B6 CC 02      LDA   $CC02              ;
DF26: B6 C8 00      LDA   $C800              ;
DF29: 81 80         CMPA  #$80               ;
DF2B: 25 30         BCS   $DF5D              ;
DF2D: 96 92         LDA   <$92               ;
DF2F: 26 7B         BNE   $DFAC              ;go to return from interrupt
DF31: 0C 92         INC   <$92               ;
DF33: BD D5 68      JSR   $D568              ;
DF36: BD E2 63      JSR   $E263              ;
DF39: BD E0 7E      JSR   $E07E              ;
DF3C: B6 C8 00      LDA   $C800              ;
DF3F: 80 08         SUBA  #$08               ;
DF41: 81 A8         CMPA  #$A8               ;
DF43: 23 02         BLS   $DF47              ;
DF45: 86 A8         LDA   #$A8               ;
DF47: 97 A2         STA   <$A2               ;
DF49: 86 02         LDA   #$02               ;
DF4B: B7 D0 00      STA   $D000              ;
DF4E: DC A2         LDD   <$A2               ;
DF50: BD E3 9F      JSR   $E39F              ;
DF53: DC A2         LDD   <$A2               ;
DF55: BD E2 13      JSR   $E213              ;
DF58: BD E4 53      JSR   $E453              ;
DF5B: 20 4F         BRA   $DFAC              ;go to return from interrupt
DF5D: D6 92         LDB   <$92               ;
DF5F: 27 4B         BEQ   $DFAC              ;go to return from interrupt
DF61: 0F 92         CLR   <$92               ;
DF63: 0C 5D         INC   <$5D               ;
DF65: C6 38         LDB   #$38               ;
DF67: F7 C3 FC      STB   $C3FC              ;reset watchdog
DF6A: 81 08         CMPA  #$08               ;
DF6C: 22 1B         BHI   $DF89              ;
DF6E: CE C0 10      LDU   #$C010             ;
DF71: DC 30         LDD   <$30               ;
DF73: 9E 32         LDX   <$32               ;
DF75: 10 9E 34      LDY   <$34               ;
DF78: 36 36         PSHU  Y,X,B,A            ;
DF7A: DC 2A         LDD   <$2A               ;
DF7C: 9E 2C         LDX   <$2C               ;
DF7E: 10 9E 2E      LDY   <$2E               ;
DF81: 36 36         PSHU  Y,X,B,A            ;
DF83: DC 26         LDD   <$26               ;
DF85: 9E 28         LDX   <$28               ;
DF87: 36 16         PSHU  X,B,A              ;
DF89: BD D5 FD      JSR   $D5FD              ;
DF8C: 86 07         LDA   #$07               ;
DF8E: B7 D0 00      STA   $D000              ;
DF91: 96 BA         LDA   <$BA               ;
DF93: 85 02         BITA  #$02               ;
DF95: 26 03         BNE   $DF9A              ;
DF97: BD C0 03      JSR   $C003              ;
DF9A: 86 02         LDA   #$02               ;
DF9C: B7 D0 00      STA   $D000              ;
DF9F: DC A1         LDD   <$A1               ;
DFA1: BD E2 13      JSR   $E213              ;
DFA4: DC A1         LDD   <$A1               ;
DFA6: BD E3 9F      JSR   $E39F              ;
DFA9: BD E3 76      JSR   $E376              ;
DFAC: 1A FF         ORCC  #$FF               ;
DFAE: 7F D0 00      CLR   $D000              ;
DFB1: 86 05         LDA   #$05               ;
DFB3: B7 CC 03      STA   $CC03              ;
DFB6: 96 36         LDA   <$36               ;
DFB8: B7 D0 00      STA   $D000              ;
DFBB: A6 E4         LDA   ,S                 ;
DFBD: 84 6F         ANDA  #$6F               ;
DFBF: A7 E4         STA   ,S                 ;
DFC1: 35 FF         PULS  CC,A,B,DP,X,Y,U,PC  ;return from interrupt

;one of two possible routines for handling an IRQ. The other one is at $DF17
DFC3: 7F D0 00      CLR   $D000              ;
DFC6: 86 A0         LDA   #$A0               ;Putting the direct page at $A000-$A0FF
DFC8: 1F 8B         TFR   A,DP               ;

DFCA: 86 04         LDA   #$04 

DFCC: B7 CC 03      STA   $CC03              ;
DFCF: B6 CC 02      LDA   $CC02              ;
DFD2: B6 C8 00      LDA   $C800              ;
DFD5: 81 58         CMPA  #$58               ;
DFD7: 25 2C         BCS   $E005              ;
DFD9: D6 92         LDB   <$92               ;
DFDB: 26 CF         BNE   $DFAC              ;go to return from interrupt
DFDD: 0C 92         INC   <$92               ;
DFDF: 43            COMA                     ;
DFE0: 12            NOP                      ;
DFE1: 97 A2         STA   <$A2               ;
DFE3: BD D5 FD      JSR   $D5FD              ;
DFE6: 86 07         LDA   #$07               ;switch to bank 7
DFE8: B7 D0 00      STA   $D000              ;
DFEB: 96 BA         LDA   <$BA               ;
DFED: 85 02         BITA  #$02               ;
DFEF: 26 03         BNE   $DFF4              ;
DFF1: BD C0 03      JSR   $C003              ;
DFF4: 86 02         LDA   #$02               ;
DFF6: B7 D0 00      STA   $D000              ;
DFF9: DC A1         LDD   <$A1               ;
DFFB: BD E2 13      JSR   $E213              ;
DFFE: DC A1         LDD   <$A1               ;
E000: BD E3 9F      JSR   $E39F              ;
E003: 20 A7         BRA   $DFAC              ;go to return from interrupt
E005: D6 92         LDB   <$92               ;
E007: 27 A3         BEQ   $DFAC              ;go to return from interrupt
E009: 0F 92         CLR   <$92               ;
E00B: 0C 5D         INC   <$5D               ;
E00D: C6 39         LDB   #$39               ;
E00F: F7 C3 FC      STB   $C3FC              ;reset watchdog
E012: 81 04         CMPA  #$04               ;
E014: 22 1B         BHI   $E031              ;
E016: CE C0 10      LDU   #$C010             ;
E019: DC 30         LDD   <$30               ;
E01B: 9E 32         LDX   <$32               ;
E01D: 10 9E 34      LDY   <$34               ;
E020: 36 36         PSHU  Y,X,B,A            ;
E022: DC 2A         LDD   <$2A               ;
E024: 9E 2C         LDX   <$2C               ;
E026: 10 9E 2E      LDY   <$2E               ;
E029: 36 36         PSHU  Y,X,B,A            ;
E02B: DC 26         LDD   <$26               ;
E02D: 9E 28         LDX   <$28               ;
E02F: 36 16         PSHU  X,B,A              ;
E031: BD D5 68      JSR   $D568              ;
E034: BD E2 63      JSR   $E263              ;
E037: BD E0 7E      JSR   $E07E              ;
E03A: 86 02         LDA   #$02               ;
E03C: B7 D0 00      STA   $D000              ;
E03F: DC A2         LDD   <$A2               ;
E041: BD E2 13      JSR   $E213              ;
E044: DC A2         LDD   <$A2               ;
E046: BD E3 9F      JSR   $E39F              ;
E049: BD E4 53      JSR   $E453              ;
E04C: BD E3 76      JSR   $E376              ;
E04F: 7E DF AC      JMP   $DFAC              ;go to return from interrupt



;SUBRTN
E052: 8E AF 9D      LDX   #$AF9D             ;
E055: C6 10         LDB   #$10               ;
E057: D7 AE         STB   <$AE               ;
E059: 5F            CLRB                     ;
E05A: BD D7 11      JSR   $D711              ;
E05D: 81 9C         CMPA  #$9C               ;
E05F: 24 F9         BCC   $E05A              ;
E061: A7 84         STA   ,X                 ;
E063: BD D7 11      JSR   $D711              ;
E066: 81 A8         CMPA  #$A8               ;
E068: 22 F9         BHI   $E063              ;
E06A: 81 2A         CMPA  #$2A               ;
E06C: 23 F5         BLS   $E063              ;
E06E: A7 01         STA   1,X                ;
E070: E7 02         STB   2,X                ;
E072: CB 11         ADDB  #$11               ;
E074: C4 77         ANDB  #$77               ;
E076: 30 04         LEAX  4,X                ;
E078: 8C AF DD      CMPX  #$AFDD             ;
E07B: 26 DD         BNE   $E05A              ;
E07D: 39            RTS                      ;

;SUBRTN
E07E: 96 BA         LDA   <$BA               ;
E080: 85 20         BITA  #$20               ;
E082: 26 F9         BNE   $E07D              ;
E084: 8E AF 9D      LDX   #$AF9D             ;
E087: DC 20         LDD   <$20               ;
E089: C4 80         ANDB  #$80               ;
E08B: DD 6F         STD   <$6F               ;
E08D: DC 22         LDD   <$22               ;
E08F: C4 80         ANDB  #$80               ;
E091: 93 6F         SUBD  <$6F               ;
E093: 58            ASLB                     ;
E094: 49            ROLA                     ;
E095: 97 6F         STA   <$6F               ;
E097: C6 F0         LDB   #$F0               ;
E099: 96 21         LDA   <$21               ;
E09B: 85 40         BITA  #$40               ;
E09D: 26 01         BNE   $E0A0              ;
E09F: 53            COMB                     ;
E0A0: D7 71         STB   <$71               ;
E0A2: 4F            CLRA                     ;
E0A3: A7 94         STA   [,X]               ;
E0A5: A7 98 04      STA   [$04,X]            ;
E0A8: A7 98 08      STA   [$08,X]            ;
E0AB: A7 98 0C      STA   [$0C,X]            ;
E0AE: A7 98 10      STA   [$10,X]            ;
E0B1: A7 98 14      STA   [$14,X]            ;
E0B4: A7 98 18      STA   [$18,X]            ;
E0B7: A7 98 1C      STA   [$1C,X]            ;
E0BA: A7 98 20      STA   [$20,X]            ;
E0BD: A7 98 24      STA   [$24,X]            ;
E0C0: A7 98 28      STA   [$28,X]            ;
E0C3: A7 98 2C      STA   [$2C,X]            ;
E0C6: A7 98 30      STA   [$30,X]            ;
E0C9: A7 98 34      STA   [$34,X]            ;
E0CC: A7 98 38      STA   [$38,X]            ;
E0CF: A7 98 3C      STA   [$3C,X]            ;
E0D2: D6 AE         LDB   <$AE               ;
E0D4: A6 84         LDA   ,X                 ;
E0D6: 9B 6F         ADDA  <$6F               ;
E0D8: 81 9C         CMPA  #$9C               ;
E0DA: 25 0A         BCS   $E0E6              ;
E0DC: 81 C0         CMPA  #$C0               ;
E0DE: 23 04         BLS   $E0E4              ;
E0E0: 86 9B         LDA   #$9B               ;
E0E2: 20 02         BRA   $E0E6              ;
E0E4: 86 00         LDA   #$00               ;
E0E6: A7 84         STA   ,X                 ;
E0E8: A6 02         LDA   2,X                ;
E0EA: 94 71         ANDA  <$71               ;
E0EC: A7 98 00      STA   [$00,X]            ;
E0EF: 30 04         LEAX  4,X                ;
E0F1: 5A            DECB                     ;
E0F2: 26 E0         BNE   $E0D4              ;
E0F4: D6 DF         LDB   <$DF               ;
E0F6: C4 3C         ANDB  #$3C               ;
E0F8: 8E AF 9D      LDX   #$AF9D             ;
E0FB: 3A            ABX                      ;
E0FC: A6 02         LDA   2,X                ;
E0FE: 8B 11         ADDA  #$11               ;
E100: 84 77         ANDA  #$77               ;
E102: A7 02         STA   2,X                ;
E104: 96 DF         LDA   <$DF               ;
E106: 85 01         BITA  #$01               ;
E108: 26 3E         BNE   $E148              ;
E10A: 81 98         CMPA  #$98               ;
E10C: 25 24         BCS   $E132              ;
E10E: CE A1 02      LDU   #$A102             ;
E111: 33 C8 B6      LEAU  $-4A,U             ;
E114: EE C4         LDU   ,U                 ;
E116: 11 83 62 45   CMPU  #$6245             ;
E11A: 27 14         BEQ   $E130              ;
E11C: 0D BA         TST   <$BA               ;
E11E: 2B 10         BMI   $E130              ;
E120: 81 A0         CMPA  #$A0               ;
E122: 25 0C         BCS   $E130              ;
E124: 81 A1         CMPA  #$A1               ;
E126: 24 08         BCC   $E130              ;
E128: D6 E1         LDB   <$E1               ;
E12A: 1F 01         TFR   D,X                ;
E12C: D6 E0         LDB   <$E0               ;
E12E: E7 84         STB   ,X                 ;
E130: 80 84         SUBA  #$84               ;
E132: 6F 98 00      CLR   [$00,X]            ;
E135: A7 84         STA   ,X                 ;
E137: 96 BA         LDA   <$BA               ;
E139: 85 02         BITA  #$02               ;
E13B: 27 0B         BEQ   $E148              ;
E13D: 96 E1         LDA   <$E1               ;
E13F: 84 3F         ANDA  #$3F               ;
E141: C6 03         LDB   #$03               ;
E143: 3D            MUL                      ;
E144: CB 2A         ADDB  #$2A               ;
E146: E7 01         STB   1,X                ;
E148: 39            RTS                      ;
E149: 8E A1 62      LDX   #$A162             ;
E14C: 9F 9F         STX   <$9F               ;
E14E: BD D7 11      JSR   $D711              ;
E151: A7 88 20      STA   $20,X              ;
E154: A7 80         STA   ,X+                ;
E156: 8C A1 83      CMPX  #$A183             ;
E159: 26 F3         BNE   $E14E              ;
E15B: 39            RTS                      ;

;SUBRTN
E15C: 9E 9F         LDX   <$9F               ;
E15E: DE BF         LDU   <$BF               ;
E160: 33 C9 FF 01   LEAU  $-FF,U             ;
E164: EC 84         LDD   ,X                 ;
E166: ED C4         STD   ,U                 ;
E168: A6 05         LDA   5,X                ;
E16A: E6 09         LDB   9,X                ;
E16C: ED 42         STD   2,U                ;
E16E: A6 0C         LDA   12,X               ;
E170: A7 44         STA   4,U                ;
E172: 96 7B         LDA   <$7B               ;
E174: 85 02         BITA  #$02               ;
E176: 27 22         BEQ   $E19A              ;
E178: A6 03         LDA   3,X                ;
E17A: E6 06         LDB   6,X                ;
E17C: ED C9 FF 01   STD   $-FF,U             ;
E180: A6 0A         LDA   10,X               ;
E182: A7 C9 FF 03   STA   $-FD,U             ;
E186: A6 04         LDA   4,X                ;
E188: E6 07         LDB   7,X                ;
E18A: ED C9 FE 01   STD   $-1FF,U            ;
E18E: A6 0B         LDA   11,X               ;
E190: A7 C9 FE 03   STA   $-1FD,U            ;
E194: A6 08         LDA   8,X                ;
E196: A7 C9 FD 02   STA   $-2FE,U            ;
E19A: 39            RTS                      ;



E19B: DE 9F         LDU   <$9F               ;
E19D: 9E BF         LDX   <$BF               ;
E19F: 30 89 08 01   LEAX  $0801,X            ;
E1A3: 37 26         PULU  A,B,Y              ;
E1A5: ED 84         STD   ,X                 ;
E1A7: 10 AF 02      STY   2,X                ;
E1AA: 37 26         PULU  A,B,Y              ;
E1AC: A7 04         STA   4,X                ;
E1AE: 96 7B         LDA   <$7B               ;
E1B0: 85 02         BITA  #$02               ;
E1B2: 27 18         BEQ   $E1CC              ;
E1B4: E7 89 01 01   STB   $0101,X            ;
E1B8: 10 AF 89 01 02  STY   $0102,X          ;
E1BD: 37 26         PULU  A,B,Y              ;
E1BF: 10 AF 89 02 01  STY   $0201,X          ;
E1C4: A7 89 02 03   STA   $0203,X            ;
E1C8: E7 89 03 02   STB   $0302,X            ;
E1CC: 39            RTS                      ;



;SUBRTN
E1CD: DE BF         LDU   <$BF               ;
E1CF: 5F            CLRB                     ;
E1D0: 8E 00 00      LDX   #$0000             ;
E1D3: 31 84         LEAY  ,X                 ;
E1D5: 33 C9 08 06   LEAU  $0806,U            ;
E1D9: 36 34         PSHU  Y,X,B              ;
E1DB: AF C9 01 01   STX   $0101,U            ;
E1DF: E7 C9 01 03   STB   $0103,U            ;
E1E3: AF C9 02 01   STX   $0201,U            ;
E1E7: E7 C9 02 03   STB   $0203,U            ;
E1EB: E7 C9 03 02   STB   $0302,U            ;
E1EF: 39            RTS                      ;



;SUBRTN
E1F0: DE BF         LDU   <$BF               ;
E1F2: 5F            CLRB                     ;
E1F3: 8E 00 00      LDX   #$0000             ;
E1F6: 31 84         LEAY  ,X                 ;
E1F8: 33 C9 FF 06   LEAU  $-FA,U             ;
E1FC: 36 34         PSHU  Y,X,B              ;
E1FE: AF C9 FF 01   STX   $-FF,U             ;
E202: E7 C9 FF 03   STB   $-FD,U             ;
E206: AF C9 FE 01   STX   $-1FF,U            ;
E20A: E7 C9 FE 03   STB   $-1FD,U            ;
E20E: E7 C9 FD 02   STB   $-2FE,U            ;
E212: 39            RTS                      ;



;SUBRTN
E213: 97 77         STA   <$77               ;
E215: 96 BA         LDA   <$BA               ;
E217: 85 10         BITA  #$10               ;
E219: 26 28         BNE   $E243              ;
E21B: 96 77         LDA   <$77               ;
E21D: 91 C0         CMPA  <$C0               ;
E21F: 23 22         BLS   $E243              ;
E221: D1 C0         CMPB  <$C0               ;
E223: 22 1E         BHI   $E243              ;
E225: 96 BD         LDA   <$BD               ;
E227: 2B 08         BMI   $E231              ;
E229: BD E2 5E      JSR   $E25E              ;
E22C: BD E1 F0      JSR   $E1F0              ;
E22F: 20 06         BRA   $E237              ;
E231: BD E2 5E      JSR   $E25E              ;
E234: BD E1 CD      JSR   $E1CD              ;
E237: DC BB         LDD   <$BB               ;
E239: DD BD         STD   <$BD               ;
E23B: 2B 07         BMI   $E244              ;
E23D: BD E2 4A      JSR   $E24A              ;
E240: BD E1 5C      JSR   $E15C              ;
E243: 39            RTS                      ;
E244: BD E2 58      JSR   $E258              ;
E247: 7E E1 9B      JMP   $E19B              ;



;SUBRTN
E24A: 10 8E F9 C1   LDY   #$F9C1             ;
E24E: 96 C4         LDA   <$C4               ;
E250: 48            ASLA                     ;
E251: DC C1         LDD   <$C1               ;
E253: DD BF         STD   <$BF               ;
E255: 7E D2 8E      JMP   $D28E              ;
;SUBRTN
E258: 10 8E F9 CB   LDY   #$F9CB             ;
E25C: 20 F0         BRA   $E24E              ;

;SUBRTN
E25E: DC BF         LDD   <$BF               ;
E260: 7E D2 DF      JMP   $D2DF              ;
E263: 96 BA         LDA   <$BA               ;
E265: 85 40         BITA  #$40               ;
E267: 10 26 01 0A   LBNE  $E375              ;
E26B: 0F 6F         CLR   <$6F               ;
E26D: DC C7         LDD   <$C7               ;
E26F: 43            COMA                     ;
E270: 53            COMB                     ;
E271: C3 00 01      ADDD  #$0001             ;
E274: 2A 02         BPL   $E278              ;
E276: 03 6F         COM   <$6F               ;
E278: 58            ASLB                     ;
E279: 49            ROLA                     ;
E27A: 58            ASLB                     ;
E27B: 49            ROLA                     ;
E27C: D3 C8         ADDD  <$C8               ;
E27E: DD C8         STD   <$C8               ;
E280: 96 6F         LDA   <$6F               ;
E282: 99 C7         ADCA  <$C7               ;
E284: 97 C7         STA   <$C7               ;
E286: DC C7         LDD   <$C7               ;
E288: 96 7B         LDA   <$7B               ;
E28A: 85 02         BITA  #$02               ;
E28C: 27 12         BEQ   $E2A0              ;
E28E: 0F 6F         CLR   <$6F               ;
E290: DC BD         LDD   <$BD               ;
E292: 2A 02         BPL   $E296              ;
E294: 03 6F         COM   <$6F               ;
E296: D3 C8         ADDD  <$C8               ;
E298: DD C8         STD   <$C8               ;
E29A: 96 6F         LDA   <$6F               ;
E29C: 99 C7         ADCA  <$C7               ;
E29E: 97 C7         STA   <$C7               ;
E2A0: DC C7         LDD   <$C7               ;
E2A2: 47            ASRA                     ;
E2A3: 56            RORB                     ;
E2A4: 47            ASRA                     ;
E2A5: 56            RORB                     ;
E2A6: 4F            CLRA                     ;
E2A7: 57            ASRB                     ;
E2A8: 46            RORA                     ;
E2A9: 97 94         STA   <$94               ;
E2AB: D7 93         STB   <$93               ;
E2AD: 96 BD         LDA   <$BD               ;
E2AF: 2B 07         BMI   $E2B8              ;
E2B1: 86 20         LDA   #$20               ;
E2B3: 5D            TSTB                     ;
E2B4: 2B 07         BMI   $E2BD              ;
E2B6: 20 09         BRA   $E2C1              ;
E2B8: 86 70         LDA   #$70               ;
E2BA: 5D            TSTB                     ;
E2BB: 2B 04         BMI   $E2C1              ;
E2BD: 0F 94         CLR   <$94               ;
E2BF: 0F 93         CLR   <$93               ;
E2C1: D6 94         LDB   <$94               ;
E2C3: 9B 93         ADDA  <$93               ;
E2C5: 97 93         STA   <$93               ;
E2C7: 93 C3         SUBD  <$C3               ;
E2C9: 27 26         BEQ   $E2F1              ;
E2CB: 25 12         BCS   $E2DF              ;
E2CD: 10 83 01 00   CMPD  #$0100             ;
E2D1: 23 1E         BLS   $E2F1              ;
E2D3: CC 00 40      LDD   #$0040             ;
E2D6: DD 95         STD   <$95               ;
E2D8: CC 01 00      LDD   #$0100             ;
E2DB: D3 C3         ADDD  <$C3               ;
E2DD: 20 18         BRA   $E2F7              ;
E2DF: 10 83 FF 00   CMPD  #$FF00             ;
E2E3: 2E 0C         BGT   $E2F1              ;
E2E5: CC FF C0      LDD   #$FFC0             ;
E2E8: DD 95         STD   <$95               ;
E2EA: CC FF 00      LDD   #$FF00             ;
E2ED: D3 C3         ADDD  <$C3               ;
E2EF: 20 06         BRA   $E2F7              ;
E2F1: 4F            CLRA                     ;
E2F2: 5F            CLRB                     ;
E2F3: DD 95         STD   <$95               ;
E2F5: DC 93         LDD   <$93               ;
E2F7: DD C3         STD   <$C3               ;
E2F9: 97 C1         STA   <$C1               ;
E2FB: DC 20         LDD   <$20               ;
E2FD: DD 22         STD   <$22               ;
E2FF: DC C7         LDD   <$C7               ;
E301: 10 83 01 00   CMPD  #$0100             ;
E305: 2D 03         BLT   $E30A              ;
E307: CC 01 00      LDD   #$0100             ;
E30A: 10 83 FF 00   CMPD  #$FF00             ;
E30E: 2E 03         BGT   $E313              ;
E310: CC FF 00      LDD   #$FF00             ;
E313: DD C7         STD   <$C7               ;
E315: D3 20         ADDD  <$20               ;
E317: 93 95         SUBD  <$95               ;
E319: DD 20         STD   <$20               ;
E31B: DC C3         LDD   <$C3               ;
E31D: 44            LSRA                     ;
E31E: 56            RORB                     ;
E31F: 44            LSRA                     ;
E320: 56            RORB                     ;
E321: C4 E0         ANDB  #$E0               ;
E323: D3 20         ADDD  <$20               ;
E325: DD CC         STD   <$CC               ;
E327: D6 C5         LDB   <$C5               ;
E329: 96 7D         LDA   <$7D               ;
E32B: 44            LSRA                     ;
E32C: 25 09         BCS   $E337              ;
E32E: 96 7B         LDA   <$7B               ;
E330: 2B 20         BMI   $E352              ;
E332: CC 00 00      LDD   #$0000             ;
E335: 20 36         BRA   $E36D              ;
E337: C1 2B         CMPB  #$2B               ;
E339: 23 3A         BLS   $E375              ;
E33B: DC CA         LDD   <$CA               ;
E33D: 2A 0E         BPL   $E34D              ;
E33F: C3 FF F8      ADDD  #$FFF8             ;
E342: 10 83 FE 00   CMPD  #$FE00             ;
E346: 2C 25         BGE   $E36D              ;
E348: CC FE 00      LDD   #$FE00             ;
E34B: 20 20         BRA   $E36D              ;
E34D: CC FF 00      LDD   #$FF00             ;
E350: 20 1B         BRA   $E36D              ;
E352: C1 EE         CMPB  #$EE               ;
E354: 24 1F         BCC   $E375              ;
E356: DC CA         LDD   <$CA               ;
E358: 2F 0E         BLE   $E368              ;
E35A: C3 00 08      ADDD  #$0008             ;
E35D: 10 83 02 00   CMPD  #$0200             ;
E361: 23 0A         BLS   $E36D              ;
E363: CC 02 00      LDD   #$0200             ;
E366: 20 05         BRA   $E36D              ;
E368: CC 01 00      LDD   #$0100             ;
E36B: 20 00         BRA   $E36D              ;
E36D: DD CA         STD   <$CA               ;
E36F: D3 C5         ADDD  <$C5               ;
E371: DD C5         STD   <$C5               ;
E373: 97 C2         STA   <$C2               ;
E375: 39            RTS                      ;



;SUBRTN
E376: 96 BA         LDA   <$BA               ;
E378: 85 20         BITA  #$20               ;
E37A: 26 22         BNE   $E39E              ;
E37C: 8E A0 65      LDX   #$A065             ;
E37F: 20 19         BRA   $E39A              ;
E381: EC 0A         LDD   10,X               ;
E383: E3 0E         ADDD  14,X               ;
E385: ED 0A         STD   10,X               ;
E387: EC 0C         LDD   12,X               ;
E389: E3 88 10      ADDD  $10,X              ;
E38C: 81 2A         CMPA  #$2A               ;
E38E: 24 02         BCC   $E392              ;
E390: 86 F0         LDA   #$F0               ;
E392: 81 F0         CMPA  #$F0               ;
E394: 23 02         BLS   $E398              ;
E396: 86 2A         LDA   #$2A               ;
E398: ED 0C         STD   12,X               ;
E39A: AE 84         LDX   ,X                 ;
E39C: 26 E3         BNE   $E381              ;
E39E: 39            RTS                      ;



E39F: 34 06         PSHS  B,A                ;
E3A1: 96 BA         LDA   <$BA               ;
E3A3: 85 20         BITA  #$20               ;
E3A5: 26 4A         BNE   $E3F1              ;
E3A7: 8E A0 65      LDX   #$A065             ;
E3AA: 20 41         BRA   $E3ED              ;
E3AC: EC 04         LDD   4,X                ;
E3AE: 27 12         BEQ   $E3C2              ;
E3B0: E1 E4         CMPB  ,S                 ;
E3B2: 22 39         BHI   $E3ED              ;
E3B4: E1 61         CMPB  1,S                ;
E3B6: 23 35         BLS   $E3ED              ;
E3B8: 10 AE 02      LDY   2,X                ;
E3BB: AD B8 08      JSR   [$08,Y]            ;
E3BE: 4F            CLRA                     ;
E3BF: 5F            CLRB                     ;
E3C0: ED 04         STD   4,X                ;
E3C2: E6 0C         LDB   12,X               ;
E3C4: E1 E4         CMPB  ,S                 ;
E3C6: 22 25         BHI   $E3ED              ;
E3C8: E1 61         CMPB  1,S                ;
E3CA: 23 21         BLS   $E3ED              ;
E3CC: EC 0A         LDD   10,X               ;
E3CE: 93 20         SUBD  <$20               ;
E3D0: 10 83 25 80   CMPD  #$2580             ;
E3D4: 24 17         BCC   $E3ED              ;
E3D6: 10 AE 02      LDY   2,X                ;
E3D9: 58            ASLB                     ;
E3DA: 49            ROLA                     ;
E3DB: 58            ASLB                     ;
E3DC: 49            ROLA                     ;
E3DD: AB A4         ADDA  ,Y                 ;
E3DF: 81 9C         CMPA  #$9C               ;
E3E1: 22 0A         BHI   $E3ED              ;
E3E3: A0 A4         SUBA  ,Y                 ;
E3E5: 58            ASLB                     ;
E3E6: E6 0C         LDB   12,X               ;
E3E8: ED 04         STD   4,X                ;
E3EA: AD B8 06      JSR   [$06,Y]            ;
E3ED: AE 84         LDX   ,X                 ;
E3EF: 26 BB         BNE   $E3AC              ;
E3F1: 35 86         PULS  A,B,PC             ;



;SUBRTN
E3F3: 34 66         PSHS  U,Y,B,A            ;
E3F5: 96 99         LDA   <$99               ;
E3F7: 81 14         CMPA  #$14               ;
E3F9: 24 4F         BCC   $E44A              ;
E3FB: EC 0A         LDD   10,X               ;
E3FD: 93 20         SUBD  <$20               ;
E3FF: 10 83 25 80   CMPD  #$2580             ;
E403: 24 45         BCC   $E44A              ;
E405: 58            ASLB                     ;
E406: 49            ROLA                     ;
E407: 58            ASLB                     ;
E408: 49            ROLA                     ;
E409: E6 0C         LDB   12,X               ;
E40B: C1 2A         CMPB  #$2A               ;
E40D: 23 3B         BLS   $E44A              ;
E40F: 9E 67         LDX   <$67               ;
E411: 27 37         BEQ   $E44A              ;
E413: ED 04         STD   4,X                ;
E415: ED 0A         STD   10,X               ;
E417: 1E 89         EXG   A,B                ;
E419: ED 0C         STD   12,X               ;
E41B: EF 06         STU   6,X                ;
E41D: 4F            CLRA                     ;
E41E: 5F            CLRB                     ;
E41F: ED 0E         STD   14,X               ;
E421: ED 88 10      STD   $10,X              ;
E424: EE 66         LDU   6,S                ;
E426: 37 26         PULU  A,B,Y              ;
E428: ED 88 12      STD   $12,X              ;
E42B: 10 AF 02      STY   2,X                ;
E42E: 37 06         PULU  A,B                ;
E430: EF 66         STU   6,S                ;
E432: ED 08         STD   8,X                ;
E434: 86 14         LDA   #$14               ;
E436: A7 88 15      STA   $15,X              ;
E439: A7 88 16      STA   $16,X              ;
E43C: EC 84         LDD   ,X                 ;
E43E: DD 67         STD   <$67               ;
E440: DC 6D         LDD   <$6D               ;
E442: ED 84         STD   ,X                 ;
E444: 0C 99         INC   <$99               ;
E446: 9F 6D         STX   <$6D               ;
E448: 35 E6         PULS  A,B,Y,U,PC         ;
E44A: EE 66         LDU   6,S                ;
E44C: 33 46         LEAU  6,U                ;
E44E: EF 66         STU   6,S                ;
E450: 4F            CLRA                     ;
E451: 35 E6         PULS  A,B,Y,U,PC         ;



;SUBRTN
E453: 96 BA         LDA   <$BA               ;
E455: 85 20         BITA  #$20               ;
E457: 26 3E         BNE   $E497              ;
E459: DC 20         LDD   <$20               ;
E45B: C4 E0         ANDB  #$E0               ;
E45D: DD 9D         STD   <$9D               ;
E45F: DC 22         LDD   <$22               ;
E461: C4 E0         ANDB  #$E0               ;
E463: 93 9D         SUBD  <$9D               ;
E465: 58            ASLB                     ;
E466: 49            ROLA                     ;
E467: 58            ASLB                     ;
E468: 49            ROLA                     ;
E469: DD 9D         STD   <$9D               ;
E46B: 8E A0 6D      LDX   #$A06D             ;
E46E: 20 23         BRA   $E493              ;
E470: 10 AE 04      LDY   4,X                ;
E473: EC 88 10      LDD   $10,X              ;
E476: E3 0C         ADDD  12,X               ;
E478: 81 2A         CMPA  #$2A               ;
E47A: 23 4A         BLS   $E4C6              ;
E47C: ED 0C         STD   12,X               ;
E47E: EC 0E         LDD   14,X               ;
E480: D3 9D         ADDD  <$9D               ;
E482: E3 0A         ADDD  10,X               ;
E484: 81 98         CMPA  #$98               ;
E486: 24 3E         BCC   $E4C6              ;
E488: ED 0A         STD   10,X               ;
E48A: E6 0C         LDB   12,X               ;
E48C: ED 04         STD   4,X                ;
E48E: EE 04         LDU   4,X                ;
E490: 6E 98 12      JMP   [$12,X]            ;
E493: AE 84         LDX   ,X                 ;
E495: 26 D9         BNE   $E470              ;
E497: 39            RTS                      ;

;this block here doesn't have any entry points that I can find, yet.
E498: DE A6         LDU   <$A6               ;
E49A: E6 0B         LDB   11,X               ;
E49C: 2A 02         BPL   $E4A0              ;
E49E: 33 46         LEAU  6,U                ;
E4A0: CC 00 00      LDD   #$0000             ;
E4A3: ED A4         STD   ,Y                 ;
E4A5: A7 22         STA   2,Y                ;
E4A7: ED A9 01 00   STD   $0100,Y            ;
E4AB: A7 A9 01 02   STA   $0102,Y            ;
E4AF: 10 AE 04      LDY   4,X                ;
E4B2: EC C4         LDD   ,U                 ;
E4B4: ED A4         STD   ,Y                 ;
E4B6: EC 42         LDD   2,U                ;
E4B8: A7 22         STA   2,Y                ;
E4BA: E7 A9 01 00   STB   $0100,Y            ;
E4BE: EC 44         LDD   4,U                ;
E4C0: ED A9 01 01   STD   $0101,Y            ;
E4C4: 20 CD         BRA   $E493              ;

E4C6: 4F            CLRA                     ;
E4C7: 5F            CLRB                     ;
E4C8: A7 88 16      STA   $16,X              ;
E4CB: ED A4         STD   ,Y                 ;
E4CD: A7 22         STA   2,Y                ;
E4CF: ED A9 01 00   STD   $0100,Y            ;
E4D3: A7 A9 01 02   STA   $0102,Y            ;
E4D7: 20 BA         BRA   $E493              ;
E4D9: DE A8         LDU   <$A8               ;
E4DB: E6 0B         LDB   11,X               ;
E4DD: 58            ASLB                     ;
E4DE: CC 00 00      LDD   #$0000             ;
E4E1: ED A4         STD   ,Y                 ;
E4E3: A7 22         STA   2,Y                ;
E4E5: ED A9 01 00   STD   $0100,Y            ;
E4E9: A7 A9 01 02   STA   $0102,Y            ;
E4ED: 10 AE 04      LDY   4,X                ;
E4F0: 25 15         BCS   $E507              ;
E4F2: EC C4         LDD   ,U                 ;
E4F4: 84 0F         ANDA  #$0F               ;
E4F6: ED A4         STD   ,Y                 ;
E4F8: EC 42         LDD   2,U                ;
E4FA: 84 0F         ANDA  #$0F               ;
E4FC: A7 22         STA   2,Y                ;
E4FE: C4 F0         ANDB  #$F0               ;
E500: E7 A9 01 01   STB   $0101,Y            ;
E504: 7E E4 93      JMP   $E493              ;
E507: EC C4         LDD   ,U                 ;
E509: C4 0F         ANDB  #$0F               ;
E50B: E7 21         STB   1,Y                ;
E50D: 84 F0         ANDA  #$F0               ;
E50F: A7 A9 01 02   STA   $0102,Y            ;
E513: EC 42         LDD   2,U                ;
E515: 84 F0         ANDA  #$F0               ;
E517: ED A9 01 00   STD   $0100,Y            ;
E51B: 7E E4 93      JMP   $E493              ;
E51E: CC 00 25      LDD   #$0025             ;
E521: BD D3 60      JSR   $D360              ;
E524: 0A 99         DEC   <$99               ;
E526: BD D0 F2      JSR   $D0F2              ;
E529: BD F3 FE      JSR   $F3FE              ;
E52C: EC 0A         LDD   10,X               ;
E52E: 44            LSRA                     ;
E52F: 56            RORB                     ;
E530: 44            LSRA                     ;
E531: 56            RORB                     ;
E532: D3 20         ADDD  <$20               ;
E534: ED 0A         STD   10,X               ;
E536: A6 0C         LDA   12,X               ;
E538: 80 02         SUBA  #$02               ;
E53A: A7 0C         STA   12,X               ;
E53C: CC F9 51      LDD   #$F951             ;
E53F: ED 02         STD   2,X                ;
E541: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
E544: CC D4 E4      LDD   #$D4E4             ;
E547: 7E D5 4D      JMP   $D54D              ;
E54A: 5E 



;SUBRTN
E54B: 8E A1 A2      LDX   #$A1A2             ;
E54E: 9F A8         STX   <$A8               ;
E550: C6 0A         LDB   #$0A               ;
E552: BD D7 11      JSR   $D711              ;
E555: 2B 02         BMI   $E559              ;
E557: C6 09         LDB   #$09               ;
E559: 44            LSRA                     ;
E55A: 25 04         BCS   $E560              ;
E55C: CB A0         ADDB  #$A0               ;
E55E: 20 02         BRA   $E562              ;
E560: CB 90         ADDB  #$90               ;
E562: E7 80         STB   ,X+                ;
E564: 8C A1 C2      CMPX  #$A1C2             ;
E567: 26 E7         BNE   $E550              ;
E569: 39            RTS                      ;



;SUBRTN
E56A: 8E A0 6D      LDX   #$A06D             ;
E56D: 20 1B         BRA   $E58A              ;
E56F: A6 88 16      LDA   $16,X              ;
E572: 27 05         BEQ   $E579              ;
E574: 6A 88 15      DEC   $15,X              ;
E577: 26 11         BNE   $E58A              ;
E579: EE 84         LDU   ,X                 ;
E57B: EF A4         STU   ,Y                 ;
E57D: DE 67         LDU   <$67               ;
E57F: EF 84         STU   ,X                 ;
E581: 9F 67         STX   <$67               ;
E583: BD F3 FE      JSR   $F3FE              ;
E586: 0A 99         DEC   <$99               ;
E588: 30 A4         LEAX  ,Y                 ;
E58A: 31 84         LEAY  ,X                 ;
E58C: AE 84         LDX   ,X                 ;
E58E: 26 DF         BNE   $E56F              ;
E590: 39            RTS                      ;

Unable to find the entry point in this next routine?

E591: 96 B5         LDA   <$B5               ;
E593: 81 04         CMPA  #$04               ;
E595: 24 11         BCC   $E5A8              ;
E597: 0C B5         INC   <$B5               ;
E599: CC D5 1B      LDD   #$D51B             ;
E59C: BD D5 4D      JSR   $D54D              ;
E59F: 9E C1         LDX   <$C1               ;
E5A1: 96 BB         LDA   <$BB               ;
E5A3: 2A 1C         BPL   $E5C1              ;
E5A5: 7E E6 30      JMP   $E630              ;
E5A8: 7E D0 0A      JMP   $D00A              ;


;SUBRTN
E5AB: 34 46         PSHS  U,B,A              ;
E5AD: 86 02         LDA   #$02               ;
E5AF: 97 36         STA   <$36               ;
E5B1: B7 D0 00      STA   $D000              ;
E5B4: 35 06         PULS  A,B                ;
E5B6: 12            NOP                      ;
E5B7: 12            NOP                      ;
E5B8: 12            NOP                      ;
E5B9: CE F9 6F      LDU   #$F96F             ;
E5BC: BD E6 BA      JSR   $E6BA              ;
E5BF: 35 C0         PULS  U,PC               ;


E5C1: 30 89 07 04   LEAX  $0704,X            ;
E5C5: AF 47         STX   7,U                ;
E5C7: AF 49         STX   9,U                ;
E5C9: AF 4B         STX   11,U               ;
;service entry on InsertEventLink event link
E5CB: 96 BA         LDA   <$BA               ;
E5CD: 85 40         BITA  #$40               ;
E5CF: 26 50         BNE   $E621              ;
E5D1: 86 04         LDA   #$04               ;
E5D3: AE 47         LDX   7,U                ;
E5D5: C6 11         LDB   #$11               ;
E5D7: 8C 98 00      CMPX  #$9800             ;
E5DA: 24 45         BCC   $E621              ;
E5DC: E7 84         STB   ,X                 ;
E5DE: 30 89 01 00   LEAX  $0100,X            ;
E5E2: 4A            DECA                     ;
E5E3: 26 F7         BNE   $E5DC              ;
E5E5: C6 99         LDB   #$99               ;
E5E7: E7 84         STB   ,X                 ;
E5E9: AF 47         STX   7,U                ;
E5EB: 10 9E A4      LDY   <$A4               ;
E5EE: 10 8C A1 5F   CMPY  #$A15F             ;
E5F2: 25 04         BCS   $E5F8              ;
E5F4: 10 8E A1 42   LDY   #$A142             ;
E5F8: AE 49         LDX   9,U                ;
E5FA: 86 03         LDA   #$03               ;
E5FC: E6 A0         LDB   ,Y+                ;
E5FE: E7 84         STB   ,X                 ;
E600: 30 89 01 00   LEAX  $0100,X            ;
E604: 4A            DECA                     ;
E605: 26 F5         BNE   $E5FC              ;
E607: 10 9F A4      STY   <$A4               ;
E60A: AF 49         STX   9,U                ;
E60C: 6F D8 0B      CLR   [$0B,U]            ;
E60F: 6C 4B         INC   11,U               ;
E611: EC 47         LDD   7,U                ;
E613: 80 06         SUBA  #$06               ;
E615: 8D 94         BSR   $E5AB              ;
E617: 26 08         BNE   $E621              ;
E619: 86 01         LDA   #$01               ;load InsertEventLink event count
E61B: 8E E5 CB      LDX   #$E5CB             ;load jump point for event return
E61E: 7E D0 01      JMP   InsertEventLink         ;
E621: AE 4B         LDX   11,U               ;
E623: 4F            CLRA                     ;
E624: A7 84         STA   ,X                 ;
E626: 30 89 01 00   LEAX  $0100,X            ;
E62A: AC 47         CMPX  7,U                ;
E62C: 23 F6         BLS   $E624              ;
E62E: 20 6A         BRA   $E69A              ;
E630: 30 04         LEAX  4,X                ;
E632: AF 47         STX   7,U                ;
E634: AF 49         STX   9,U                ;
E636: AF 4B         STX   11,U               ;
;service entry on InsertEventLink event link
E638: 96 BA         LDA   <$BA               ;
E63A: 85 40         BITA  #$40               ;
E63C: 26 4F         BNE   $E68D              ;
E63E: 86 04         LDA   #$04               ;
E640: AE 47         LDX   7,U                ;
E642: C6 11         LDB   #$11               ;
E644: 8C 05 00      CMPX  #$0500             ;
E647: 23 44         BLS   $E68D              ;
E649: E7 84         STB   ,X                 ;
E64B: 30 89 FF 00   LEAX  $-100,X            ;
E64F: 4A            DECA                     ;
E650: 26 F7         BNE   $E649              ;
E652: C6 99         LDB   #$99               ;
E654: E7 84         STB   ,X                 ;
E656: AF 47         STX   7,U                ;
E658: 10 9E A4      LDY   <$A4               ;
E65B: 10 8C A1 5F   CMPY  #$A15F             ;
E65F: 25 04         BCS   $E665              ;
E661: 10 8E A1 42   LDY   #$A142             ;
E665: AE 49         LDX   9,U                ;
E667: 86 03         LDA   #$03               ;
E669: E6 A0         LDB   ,Y+                ;
E66B: E7 84         STB   ,X                 ;
E66D: 30 89 FF 00   LEAX  $-100,X            ;
E671: 4A            DECA                     ;
E672: 26 F5         BNE   $E669              ;
E674: 10 9F A4      STY   <$A4               ;
E677: AF 49         STX   9,U                ;
E679: 6F D8 0B      CLR   [$0B,U]            ;
E67C: 6A 4B         DEC   11,U               ;
E67E: EC 47         LDD   7,U                ;
E680: BD E5 AB      JSR   $E5AB              ;
E683: 26 08         BNE   $E68D              ;
E685: 86 01         LDA   #$01               ;load InsertEventLink event count
E687: 8E E6 38      LDX   #$E638             ;load jump point for event return
E68A: 7E D0 01      JMP   InsertEventLink         ;
E68D: AE 4B         LDX   11,U               ;
E68F: 4F            CLRA                     ;
E690: A7 84         STA   ,X                 ;
E692: 30 89 FF 00   LEAX  $-100,X            ;
E696: AC 47         CMPX  7,U                ;
E698: 24 F6         BCC   $E690              ;
E69A: 0A B5         DEC   <$B5               ;
E69C: 7E D0 0A      JMP   $D00A              ;
;SUBRTN
E69F: 8E A1 42      LDX   #$A142             ;
E6A2: 9F A4         STX   <$A4               ;
E6A4: BD D7 11      JSR   $D711              ;
E6A7: 5F            CLRB                     ;
E6A8: 44            LSRA                     ;
E6A9: 24 02         BCC   $E6AD              ;
E6AB: CB 01         ADDB  #$01               ;
E6AD: 44            LSRA                     ;
E6AE: 24 02         BCC   $E6B2              ;
E6B0: CB 10         ADDB  #$10               ;
E6B2: E7 80         STB   ,X+                ;
E6B4: 8C A1 62      CMPX  #$A162             ;
E6B7: 26 EB         BNE   $E6A4              ;
E6B9: 39            RTS                      ;


;SUBRTN
E6BA: 8E A0 65      LDX   #$A065             ;


;SUBRTN
E6BD: DD D6         STD   <$D6               ;
E6BF: E3 C4         ADDD  ,U                 ;
E6C1: DD D8         STD   <$D8               ;
E6C3: 20 17         BRA   $E6DC              ;
E6C5: EC 04         LDD   4,X                ;
E6C7: 27 13         BEQ   $E6DC              ;
E6C9: 91 D8         CMPA  <$D8               ;
E6CB: 24 0F         BCC   $E6DC              ;
E6CD: D1 D9         CMPB  <$D9               ;
E6CF: 24 0B         BCC   $E6DC              ;
E6D1: E3 98 02      ADDD  [$02,X]            ;
E6D4: 91 D6         CMPA  <$D6               ;
E6D6: 23 04         BLS   $E6DC              ;
E6D8: D1 D7         CMPB  <$D7               ;
E6DA: 22 05         BHI   $E6E1              ;
E6DC: AE 84         LDX   ,X                 ;
E6DE: 26 E5         BNE   $E6C5              ;
E6E0: 39            RTS                      ;
E6E1: DF DC         STU   <$DC               ;
E6E3: 10 AE 02      LDY   2,X                ;
E6E6: A3 A4         SUBD  ,Y                 ;
E6E8: DD 73         STD   <$73               ;
E6EA: 4F            CLRA                     ;
E6EB: 5F            CLRB                     ;
E6EC: DD D0         STD   <$D0               ;
E6EE: DD D2         STD   <$D2               ;
E6F0: DC 73         LDD   <$73               ;
E6F2: D0 D7         SUBB  <$D7               ;
E6F4: 22 05         BHI   $E6FB              ;
E6F6: 50            NEGB                     ;
E6F7: D7 D1         STB   <$D1               ;
E6F9: 20 02         BRA   $E6FD              ;
E6FB: D7 D3         STB   <$D3               ;
E6FD: 90 D6         SUBA  <$D6               ;
E6FF: 22 05         BHI   $E706              ;
E701: 40            NEGA                     ;
E702: 97 D0         STA   <$D0               ;
E704: 20 02         BRA   $E708              ;
E706: 97 D2         STA   <$D2               ;
E708: DC 73         LDD   <$73               ;
E70A: E3 A4         ADDD  ,Y                 ;
E70C: D0 D9         SUBB  <$D9               ;
E70E: 22 01         BHI   $E711              ;
E710: 5F            CLRB                     ;
E711: 90 D8         SUBA  <$D8               ;
E713: 22 01         BHI   $E716              ;
E715: 4F            CLRA                     ;
E716: DD DA         STD   <$DA               ;
E718: EC A4         LDD   ,Y                 ;
E71A: 93 D0         SUBD  <$D0               ;
E71C: 93 DA         SUBD  <$DA               ;
E71E: DD CE         STD   <$CE               ;
E720: A6 41         LDA   1,U                ;
E722: 97 D5         STA   <$D5               ;
E724: D6 D2         LDB   <$D2               ;
E726: 3D            MUL                      ;
E727: EE 42         LDU   2,U                ;
E729: 33 CB         LEAU  D,U                ;
E72B: A6 21         LDA   1,Y                ;
E72D: 97 D4         STA   <$D4               ;
E72F: 10 AE 22      LDY   2,Y                ;
E732: D6 D0         LDB   <$D0               ;
E734: 3D            MUL                      ;
E735: 31 AB         LEAY  D,Y                ;
E737: 96 D1         LDA   <$D1               ;
E739: 31 A6         LEAY  A,Y                ;
E73B: 96 D3         LDA   <$D3               ;
E73D: 33 C6         LEAU  A,U                ;
E73F: D6 CF         LDB   <$CF               ;bookmark 001
E741: 5A            DECB                     ;
E742: A6 C5         LDA   B,U                ;
E744: 27 2A         BEQ   $E770              ;
E746: A6 A5         LDA   B,Y                ;
E748: 27 26         BEQ   $E770              ;
E74A: 31 A5         LEAY  B,Y                ;
E74C: 1F 20         TFR   Y,D                ;
E74E: EE 02         LDU   2,X                ;
E750: A3 42         SUBD  2,U                ;
E752: 10 AE 04      LDY   4,X                ;
E755: E0 41         SUBB  1,U                ;
E757: 82 00         SBCA  #$00               ;
E759: 25 06         BCS   $E761              ;
E75B: 31 A9 01 00   LEAY  $0100,Y            ;
E75F: 20 F4         BRA   $E755              ;
E761: EB 41         ADDB  1,U                ;
E763: 89 00         ADCA  #$00               ;
E765: 31 A5         LEAY  B,Y                ;
E767: 10 9F F8      STY   <$F8               ;
E76A: AD 98 08      JSR   [$08,X]            ;
E76D: 86 01         LDA   #$01               ;
E76F: 39            RTS                      ;
E770: 5A            DECB                     ;
E771: 2A CF         BPL   $E742              ;
E773: DC D4         LDD   <$D4               ;
E775: 31 A6         LEAY  A,Y                ;
E777: 33 C5         LEAU  B,U                ;
E779: 0A CE         DEC   <$CE               ;
E77B: 26 C2         BNE   $E73F              ;
E77D: DE DC         LDU   <$DC               ;
E77F: 7E E6 DC      JMP   $E6DC              ;
E782: 0F B6         CLR   <$B6               ;
;service entry on InsertEventLink event link
E784: 8E E7 99      LDX   #$E799             ;
E787: 96 B6         LDA   <$B6               ;
E789: E6 86         LDB   A,X                ;
E78B: 27 F5         BEQ   $E782              ;
E78D: 0C B6         INC   <$B6               ;
E78F: D7 27         STB   <$27               ;
E791: 86 02         LDA   #$02               ;load InsertEventLink event count
E793: 8E E7 84      LDX   #$E784             ;load jump point for event return
E796: 7E D0 01      JMP   InsertEventLink         ;


      ;DATA
E799: 38 
E79A: 39            RTS                      ;

E79B: 3A            ABX                      ;
E79C: 3B            RTI                      ;
E79D: 3C 3D         CWAI  $3D                ;
E79F: 3E            RESET                    ;
E7A0: 3F            SWI                      ;
E7A1: 37 2F         PULU  CC,A,B,DP,Y        ;
E7A3: 27 1F         BEQ   $E7C4              ;
E7A5: 17 47 47      LBSR  $12EEF             ;
E7A8: 87 
E7A9: 87 
E7AA: C7 
E7AB: C7 
E7AC: C6 C5         LDB   #$C5               ;
E7AE: CC CB CA      LDD   #$CBCA             ;
E7B1: DA E8         ORB   <$E8               ;
E7B3: F8 F9 FA      EORB  $F9FA              ;
E7B6: FB FD FF      ADDB  $FDFF              ;
E7B9: BF 3F 3E      STX   $3F3E              ;
E7BC: 3C 00         CWAI  $00                ;



;initialization routine?
E7BE: 8E A0 5F      LDX   #$A05F             ;start the event chain over again
E7C1: 9F 63         STX   <$63               ;initialize this variable address to $A05F
E7C3: 96 5D         LDA   <$5D               ;
E7C5: 27 FC         BEQ   $E7C3              ;if <$5D is zero, are we waiting for an interrupt to get us out of this loop?
E7C7: 0F 5D         CLR   <$5D               ;clear a counter for ...
E7C9: D6 BA         LDB   <$BA               ;
E7CB: C5 7D         BITB  #$7D               ;
E7CD: 27 04         BEQ   $E7D3              ;
E7CF: 0F 5E         CLR   <$5E               ;
E7D1: 20 47         BRA   $E81A              ;
E7D3: 48            ASLA                     ;
E7D4: 9B 5E         ADDA  <$5E               ;
E7D6: 80 04         SUBA  #$04               ;
E7D8: 2A 01         BPL   $E7DB              ;
E7DA: 4F            CLRA                     ;
E7DB: 97 5E         STA   <$5E               ;
E7DD: 81 02         CMPA  #$02               ;
E7DF: 25 39         BCS   $E81A              ;
E7E1: C6 03         LDB   #$03               ;
E7E3: D7 AE         STB   <$AE               ;
E7E5: 81 02         CMPA  #$02               ;
E7E7: 23 31         BLS   $E81A              ;
E7E9: 86 02         LDA   #$02               ;
E7EB: 97 5E         STA   <$5E               ;
E7ED: 10 8E A0 65   LDY   #$A065             ;
E7F1: AE A4         LDX   ,Y                 ;
E7F3: 27 25         BEQ   $E81A              ;
E7F5: A6 88 14      LDA   $14,X              ;
E7F8: 27 04         BEQ   $E7FE              ;
E7FA: 31 84         LEAY  ,X                 ;
E7FC: 20 F3         BRA   $E7F1              ;
E7FE: EE 84         LDU   ,X                 ;
E800: EF A4         STU   ,Y                 ;
E802: DC DF         LDD   <$DF               ;
E804: 84 3F         ANDA  #$3F               ;
E806: 8B 60         ADDA  #$60               ;
E808: E3 0A         ADDD  10,X               ;
E80A: ED 0A         STD   10,X               ;
E80C: BD F3 FE      JSR   $F3FE              ;
E80F: CC 00 00      LDD   #$0000             ;
E812: ED 04         STD   4,X                ;
E814: DE 6B         LDU   <$6B               ;
E816: 9F 6B         STX   <$6B               ;
E818: EF 84         STU   ,X                 ;
E81A: 86 02         LDA   #$02               ;
E81C: 97 36         STA   <$36               ;
E81E: B7 D0 00      STA   $D000              ;
E821: 8D 3E         BSR   $E861              ;
E823: BD FC 66      JSR   $FC66              ;"JSR  $FD2D" would have been faster
E826: BD D7 11      JSR   $D711              ;
E829: 9E 82         LDX   <$82               ;
E82B: 26 0C         BNE   $E839              ;
E82D: 9E 86         LDX   <$86               ;
E82F: 27 17         BEQ   $E848              ;
E831: DC 88         LDD   <$88               ;
E833: 0F 86         CLR   <$86               ;
E835: 0F 87         CLR   <$87               ;
E837: 20 06         BRA   $E83F              ;
E839: DC 84         LDD   <$84               ;
E83B: 0F 82         CLR   <$82               ;
E83D: 0F 83         CLR   <$83               ;
E83F: D4 BA         ANDB  <$BA               ;
E841: 26 E6         BNE   $E829              ;
E843: BD D0 55      JSR   $D055              ;
E846: 20 E1         BRA   $E829              ;
E848: CE A0 5F      LDU   #$A05F             ;
E84B: 20 09         BRA   Ticker             ;


E84D: 6A 44         DEC   4,U                ;decrement count for this link
E84F: 26 05         BNE   Ticker             ;is it ready?
E851: DF 63         STU   <$63               ;it's matured, save current link pointer
E853: 6E D8 02      JMP   [$02,U]            ;jump to handler for this link
Ticker
E856: EE C4         LDU   ,U                 ;not ready yet, go to next link
E858: 26 F3         BNE   $E84D              ;if the link is non-zero it must be valid
E85A: 10 CE BF FF   LDS   #$BFFF             ;initialize the stack pointer
E85E: 7E E7 BE      JMP   $E7BE              ;



;SUBRTN
E861: 96 BA         LDA   <$BA               ;
E863: 85 10         BITA  #$10               ;
E865: 26 2D         BNE   $E894              ;
E867: DC BF         LDD   <$BF               ;
E869: CE F9 C1      LDU   #$F9C1             ;
E86C: 0D BD         TST   <$BD               ;
E86E: 2A 03         BPL   $E873              ;
E870: CE F9 CB      LDU   #$F9CB             ;
E873: 34 46         PSHS  U,B,A              ;
E875: 0C DE         INC   <$DE               ;
E877: BD E6 BA      JSR   $E6BA              ;
E87A: 35 46         PULS  A,B,U              ;
E87C: 26 08         BNE   $E886              ;
E87E: 8E A0 6D      LDX   #$A06D             ;
E881: BD E6 BD      JSR   $E6BD              ;
E884: 27 0E         BEQ   $E894              ;
E886: 8E DA 46      LDX   #$DA46             ;
E889: 86 00         LDA   #$00               ;
E88B: BD D0 55      JSR   $D055              ;
E88E: 96 BA         LDA   <$BA               ;
E890: 8A 08         ORA   #$08               ;
E892: 97 BA         STA   <$BA               ;
E894: 0F DE         CLR   <$DE               ;
E896: 39            RTS                      ;

E897: 96 AF         LDA   <$AF               ;
E899: 26 23         BNE   $E8BE              ;
E89B: 0C AF         INC   <$AF               ;
E89D: DC BD         LDD   <$BD               ;
E89F: 53            COMB                     ;
E8A0: 43            COMA                     ;
E8A1: C3 00 01      ADDD  #$0001             ;
E8A4: DD BB         STD   <$BB               ;
E8A6: 86 02         LDA   #$02               ;load InsertEventLink event count
E8A8: 8E E8 AE      LDX   #$E8AE             ;load jump point for event return
E8AB: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E8AE: 96 7B         LDA   <$7B               ;
E8B0: 85 40         BITA  #$40               ;
E8B2: 26 F2         BNE   $E8A6              ;
E8B4: 86 05         LDA   #$05               ;load InsertEventLink event count
E8B6: 8E E8 BC      LDX   #$E8BC             ;load jump point for event return
E8B9: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E8BC: 0F AF         CLR   <$AF               ;
E8BE: 7E D0 0A      JMP   $D00A              ;
E8C1: 96 9A         LDA   <$9A               ;
E8C3: 26 57         BNE   $E91C              ;
E8C5: 9E 8D         LDX   <$8D               ;
E8C7: A6 09         LDA   9,X                ;
E8C9: 27 51         BEQ   $E91C              ;
E8CB: 0C 9A         INC   <$9A               ;
E8CD: 6A 09         DEC   9,X                ;
E8CF: BD D6 80      JSR   $D680              ;
E8D2: CC D4 D2      LDD   #$D4D2             ;
E8D5: BD D5 4D      JSR   $D54D              ;
E8D8: 9E 65         LDX   <$65               ;
E8DA: 27 14         BEQ   $E8F0              ;
E8DC: EC 04         LDD   4,X                ;
E8DE: 27 0C         BEQ   $E8EC              ;
E8E0: A6 88 14      LDA   $14,X              ;
E8E3: 81 02         CMPA  #$02               ;
E8E5: 24 05         BCC   $E8EC              ;
E8E7: AD 98 08      JSR   [$08,X]            ;
E8EA: 20 EC         BRA   $E8D8              ;
E8EC: AE 84         LDX   ,X                 ;
E8EE: 20 EA         BRA   $E8DA              ;
E8F0: DE 63         LDU   <$63               ;
E8F2: 86 04         LDA   #$04               ;
E8F4: A7 47         STA   7,U                ;
E8F6: 03 26         COM   <$26               ;
E8F8: 86 02         LDA   #$02               ;load InsertEventLink event count
E8FA: 8E E9 00      LDX   #$E900             ;load jump point for event return
E8FD: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E900: 6A 47         DEC   7,U                ;
E902: 26 F2         BNE   $E8F6              ;
E904: 86 0A         LDA   #$0A               ;load InsertEventLink event count
E906: 8E E9 0C      LDX   #$E90C             ;load jump point for event return
E909: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E90C: 96 7B         LDA   <$7B               ;
E90E: 85 04         BITA  #$04               ;
E910: 26 F2         BNE   $E904              ;
E912: 86 0A         LDA   #$0A               ;load InsertEventLink event count
E914: 8E E9 1A      LDX   #$E91A             ;load jump point for event return
E917: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E91A: 0F 9A         CLR   <$9A               ;
E91C: 7E D0 0A      JMP   $D00A              ;


;can't find an entry point in this part, yet. I think at least part of it is valid code
;{
E91F: 96 BA         LDA   <$BA               ;
E921: 85 FD         BITA  #$FD               ;
E923: 10 26 00 95   LBNE  $E9BC              ;
E927: 86 77         LDA   #$77               ;
E929: 97 BA         STA   <$BA               ;
;this looks like valid code to me but where is the entry point?
E92B: BD F5 F1      JSR   ClrVidMem          ;
E92E: 86 0F         LDA   #$0F               ;load InsertEventLink event count
E930: 8E E9 36      LDX   #$E936             ;load jump point for event return
E933: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E936: 9E 6D         LDX   <$6D               ;
E938: 27 05         BEQ   $E93F              ;
E93A: BD D0 F2      JSR   $D0F2              ;
E93D: 20 F7         BRA   $E936              ;
E93F: 0F 99         CLR   <$99               ;
E941: DC DF         LDD   <$DF               ;
E943: DD 20         STD   <$20               ;
E945: DD 22         STD   <$22               ;
E947: 54            LSRB                     ;
E948: 24 08         BCC   $E952              ;
E94A: CC 20 00      LDD   #$2000             ;
E94D: 8E 03 00      LDX   #$0300             ;
E950: 20 06         BRA   $E958              ;
E952: 8E FD 00      LDX   #$FD00             ;
E955: CC 70 00      LDD   #$7000             ;
E958: DD C3         STD   <$C3               ;
E95A: 9F BB         STX   <$BB               ;
E95C: D6 E0         LDB   <$E0               ;
E95E: 54            LSRB                     ;
E95F: CB 2A         ADDB  #$2A               ;
E961: D7 C5         STB   <$C5               ;
E963: DD C1         STD   <$C1               ;
E965: 4F            CLRA                     ;
E966: 5F            CLRB                     ;
E967: 97 C9         STA   <$C9               ;
E969: DD C7         STD   <$C7               ;
E96B: DD CA         STD   <$CA               ;
E96D: BD F4 FA      JSR   $F4FA              ;
E970: C6 50         LDB   #$50               ;
E972: BD DA 3D      JSR   $DA3D              ;
E975: BD D0 95      JSR   $D095              ;
E978: F9 C1 ED      ADCB  $C1ED              ;
E97B: BC 00 00      CMPX  $0000              ;
E97E: CC 00 00      LDD   #$0000             ;
E981: ED 0E         STD   14,X               ;
E983: ED 88 10      STD   $10,X              ;
E986: DC C5         LDD   <$C5               ;
E988: ED 0C         STD   12,X               ;
E98A: DC C3         LDD   <$C3               ;
E98C: 44            LSRA                     ;
E98D: 56            RORB                     ;
E98E: 44            LSRA                     ;
E98F: 56            RORB                     ;
E990: D3 20         ADDD  <$20               ;
E992: ED 0A         STD   10,X               ;
E994: 96 BB         LDA   <$BB               ;
E996: 2A 05         BPL   $E99D              ;
E998: CE F9 CB      LDU   #$F9CB             ;
E99B: EF 02         STU   2,X                ;
E99D: DE 63         LDU   <$63               ;
E99F: AF 47         STX   7,U                ;
E9A1: BD FC 60      JSR   $FC60              ;
E9A4: 86 28         LDA   #$28               ;load InsertEventLink event count
E9A6: 8E E9 AC      LDX   #$E9AC             ;load jump point for event return
E9A9: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E9AC: AE 47         LDX   7,U                ;
E9AE: BD F3 FB      JSR   $F3FB              ;
E9B1: BD DA 3C      JSR   $DA3C              ;
E9B4: 96 E1         LDA   <$E1               ;
E9B6: 81 C0         CMPA  #$C0               ;
E9B8: 10 22 F0 8A   LBHI  $DA46              ;
E9BC: 7E D0 0A      JMP   $D00A              ;
;service entry on InsertEventLink event link
E9BF: 9E 9F         LDX   <$9F               ;
E9C1: 30 01         LEAX  1,X                ;
E9C3: 8C A1 82      CMPX  #$A182             ;
E9C6: 23 03         BLS   $E9CB              ;
E9C8: 8E A1 62      LDX   #$A162             ;
E9CB: 9F 9F         STX   <$9F               ;
E9CD: 9E A8         LDX   <$A8               ;
E9CF: 30 01         LEAX  1,X                ;
E9D1: 8C A1 BA      CMPX  #$A1BA             ;
E9D4: 23 03         BLS   $E9D9              ;
E9D6: 8E A1 A2      LDX   #$A1A2             ;
E9D9: 9F A8         STX   <$A8               ;
E9DB: 86 04         LDA   #$04               ;load InsertEventLink event count
E9DD: 8E E9 BF      LDX   #$E9BF             ;load jump point for event return
E9E0: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E9E3: BD EA 33      JSR   $EA33              ;
E9E6: 86 02         LDA   #$02               ;load InsertEventLink event count
E9E8: 8E E9 EE      LDX   #$E9EE             ;load jump point for event return
E9EB: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E9EE: BD EA 0A      JSR   $EA0A              ;
E9F1: BD E5 6A      JSR   $E56A              ;
E9F4: 86 02         LDA   #$02               ;load InsertEventLink event count
E9F6: 8E E9 FC      LDX   #$E9FC             ;load jump point for event return
E9F9: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
E9FC: BD F5 0B      JSR   ROMPg1             ;
E9FF: BD C0 03      JSR   $C003              ;
EA02: 86 04         LDA   #$04               ;load InsertEventLink event count
EA04: 8E E9 E3      LDX   #$E9E3             ;load jump point for event return
EA07: 7E D0 01      JMP   InsertEventLink         ;
EA0A: DC 20         LDD   <$20               ;
EA0C: 83 0C 80      SUBD  #$0C80             ;
EA0F: DD 73         STD   <$73               ;
EA11: 8E A0 65      LDX   #$A065             ;
EA14: 20 16         BRA   $EA2C              ;
EA16: EC 0A         LDD   10,X               ;
EA18: 93 73         SUBD  <$73               ;
EA1A: 10 83 3E 80   CMPD  #$3E80             ;
EA1E: 25 0C         BCS   $EA2C              ;
EA20: EE 84         LDU   ,X                 ;
EA22: EF A4         STU   ,Y                 ;
EA24: DE 6B         LDU   <$6B               ;
EA26: EF 84         STU   ,X                 ;
EA28: 9F 6B         STX   <$6B               ;
EA2A: 30 A4         LEAX  ,Y                 ;
EA2C: 31 84         LEAY  ,X                 ;
EA2E: AE 84         LDX   ,X                 ;
EA30: 26 E4         BNE   $EA16              ;
EA32: 39            RTS                      ;

EA33: DC 20         LDD   <$20               ;
EA35: 83 0C 80      SUBD  #$0C80             ;
EA38: DD 73         STD   <$73               ;
EA3A: 8E A0 6B      LDX   #$A06B             ;
EA3D: 20 39         BRA   $EA78              ;
EA3F: EC 88 10      LDD   $10,X              ;
EA42: 58            ASLB                     ;
EA43: 49            ROLA                     ;
EA44: 58            ASLB                     ;
EA45: 49            ROLA                     ;
EA46: 58            ASLB                     ;
EA47: 49            ROLA                     ;
EA48: E3 0C         ADDD  12,X               ;
EA4A: 81 2A         CMPA  #$2A               ;
EA4C: 24 02         BCC   $EA50              ;
EA4E: 86 F0         LDA   #$F0               ;
EA50: 81 F0         CMPA  #$F0               ;
EA52: 23 02         BLS   $EA56              ;
EA54: 86 2A         LDA   #$2A               ;
EA56: ED 0C         STD   12,X               ;
EA58: EC 0E         LDD   14,X               ;
EA5A: 58            ASLB                     ;
EA5B: 49            ROLA                     ;
EA5C: 58            ASLB                     ;
EA5D: 49            ROLA                     ;
EA5E: 58            ASLB                     ;
EA5F: 49            ROLA                     ;
EA60: E3 0A         ADDD  10,X               ;
EA62: ED 0A         STD   10,X               ;
EA64: 93 73         SUBD  <$73               ;
EA66: 10 83 3E 80   CMPD  #$3E80             ;
EA6A: 24 0C         BCC   $EA78              ;
EA6C: EE 84         LDU   ,X                 ;
EA6E: EF A4         STU   ,Y                 ;
EA70: DE 65         LDU   <$65               ;
EA72: EF 84         STU   ,X                 ;
EA74: 9F 65         STX   <$65               ;
EA76: 30 A4         LEAX  ,Y                 ;
EA78: 31 84         LEAY  ,X                 ;
EA7A: AE 84         LDX   ,X                 ;
EA7C: 26 C1         BNE   $EA3F              ;
EA7E: 39            RTS                      ;

EA7F: 40            NEGA                     ;
;SUBRTN
EA80: 8E EA B4      LDX   #$EAB4             ;
EA83: 86 00         LDA   #$00               ;
EA85: BD D0 55      JSR   $D055              ;
EA88: 33 84         LEAU  ,X                 ;
EA8A: BD D0 95      JSR   $D095              ;
EA8D: F9 A3 EB      ADCB  $A3EB              ;
EA90: 2B 33         BMI   $EAC5              ;
EA92: 33 
EA93: AF 47         STX   7,U                ;
EA95: EF 06         STU   6,X                ;
EA97: DC DF         LDD   <$DF               ;
EA99: 84 1F         ANDA  #$1F               ;
EA9B: D3 20         ADDD  <$20               ;
EA9D: ED 0A         STD   10,X               ;
EA9F: 54            LSRB                     ;
EAA0: CB 2A         ADDB  #$2A               ;
EAA2: E7 0C         STB   12,X               ;
EAA4: 4F            CLRA                     ;
EAA5: 5F            CLRB                     ;
EAA6: ED 88 10      STD   $10,X              ;
EAA9: ED 0E         STD   14,X               ;
EAAB: 86 08         LDA   #$08               ;
EAAD: A7 49         STA   9,U                ;
EAAF: 8D 44         BSR   $EAF5              ;
EAB1: 7E FC 60      JMP   $FC60              ;
;service entry on InsertEventLink event link
EAB4: AE 47         LDX   7,U                ;
EAB6: EC 02         LDD   2,X                ;
EAB8: 10 83 F8 EC   CMPD  #$F8EC             ;
EABC: 27 28         BEQ   $EAE6              ;
EABE: 6A 49         DEC   9,U                ;
EAC0: 26 13         BNE   $EAD5              ;
EAC2: B6 A1 10      LDA   $A110              ;
EAC5: BD DD 9E      JSR   $DD9E              ;
EAC8: A7 49         STA   9,U                ;
EACA: BD EE BA      JSR   $EEBA              ;
EACD: 27 06         BEQ   $EAD5              ;
EACF: CC D5 2F      LDD   #$D52F             ;
EAD2: BD D5 4D      JSR   $D54D              ;
;}
EAD5: EE 02         LDU   2,X                ;
EAD7: 33 4A         LEAU  10,U               ;
EAD9: 11 83 F9 B7   CMPU  #$F9B7             ;
EADD: 23 05         BLS   $EAE4              ;
EADF: CE F9 A3      LDU   #$F9A3             ;
EAE2: 8D 0A         BSR   $EAEE              ;
EAE4: EF 02         STU   2,X                ;
EAE6: 86 06         LDA   #$06               ;load InsertEventLink event count
EAE8: 8E EA B4      LDX   #$EAB4             ;load jump point for event return
EAEB: 7E D0 01      JMP   InsertEventLink         ;
;SUBRTN
EAEE: 96 DF         LDA   <$DF               ;
EAF0: B1 A1 11      CMPA  $A111              ;
EAF3: 23 35         BLS   $EB2A              ;
EAF5: CC 40 01      LDD   #$4001             ;
EAF8: DD 73         STD   <$73               ;
EAFA: EC 0A         LDD   10,X               ;
EAFC: 93 CC         SUBD  <$CC               ;
EAFE: 2B 02         BMI   $EB02              ;
EB00: 00 73         NEG   <$73               ;
EB02: C3 02 80      ADDD  #$0280             ;
EB05: 10 83 05 00   CMPD  #$0500             ;
EB09: 23 07         BLS   $EB12              ;
EB0B: D6 73         LDB   <$73               ;
EB0D: 1D            SEX                      ;
EB0E: D3 C7         ADDD  <$C7               ;
EB10: ED 0E         STD   14,X               ;
EB12: A6 0C         LDA   12,X               ;
EB14: 90 C0         SUBA  <$C0               ;
EB16: 2B 02         BMI   $EB1A              ;
EB18: 00 74         NEG   <$74               ;
EB1A: 8B 0A         ADDA  #$0A               ;
EB1C: 81 14         CMPA  #$14               ;
EB1E: 23 0A         BLS   $EB2A              ;
EB20: 5F            CLRB                     ;
EB21: 96 74         LDA   <$74               ;
EB23: D3 CA         ADDD  <$CA               ;
EB25: 47            ASRA                     ;
EB26: 56            RORB                     ;
EB27: ED 88 10      STD   $10,X              ;
EB2A: 39            RTS                      ;

EB2B: 7A A1 19      DEC   $A119              ;
EB2E: BD F4 16      JSR   $F416              ;
EB31: 01 
EB32: 20 D4         BRA   $EB08              ;


;out of sync?
EB34: FD 39 97      STD   $3997              ;
EB37: 73 BD D0      COM   $BDD0              ;
EB3A: 95 F8         BITA  <$F8               ;
EB3C: F7 EB 74      STB   $EB74              ;
EB3F: CC CC BD      LDD   #$CCBD             ;
EB42: D7 11         STB   <$11               ;
EB44: DC E0         LDD   <$E0               ;
EB46: 84 3F         ANDA  #$3F               ;
EB48: 8B 10         ADDA  #$10               ;
EB4A: ED 0A         STD   10,X               ;
EB4C: 54            LSRB                     ;
EB4D: CB 2A         ADDB  #$2A               ;
EB4F: E7 0C         STB   12,X               ;
EB51: D6 DF         LDB   <$DF               ;
EB53: C4 3F         ANDB  #$3F               ;
EB55: CB E0         ADDB  #$E0               ;
EB57: 1D            SEX                      ;
EB58: ED 0E         STD   14,X               ;
EB5A: D6 E1         LDB   <$E1               ;
EB5C: C4 7F         ANDB  #$7F               ;
EB5E: C0 40         SUBB  #$40               ;
EB60: 1D            SEX                      ;
EB61: 2B 04         BMI   $EB67              ;
EB63: CA 20         ORB   #$20               ;
EB65: 20 02         BRA   $EB69              ;
EB67: C4 DF         ANDB  #$DF               ;
EB69: ED 88 10      STD   $10,X              ;
EB6C: BD FC 60      JSR   $FC60              ;
EB6F: 0A 73         DEC   <$73               ;
EB71: 26 C5         BNE   $EB38              ;
EB73: 39            RTS                      ;

EB74: BD F4 1D      JSR   $F41D              ;
EB77: 02 
EB78: 10 
EB79: D4 F3         ANDB  <$F3               ;
EB7B: 86 06         LDA   #$06               ;
EB7D: BD DD 9E      JSR   $DD9E              ;
EB80: 31 84         LEAY  ,X                 ;
EB82: BD EB 9E      JSR   $EB9E              ;
EB85: 7A A1 14      DEC   $A114              ;
EB88: 39            RTS                      ;

EB89: BD D7 11      JSR   $D711              ;
EB8C: D6 DF         LDB   <$DF               ;
EB8E: 1D            SEX                      ;
EB8F: 58            ASLB                     ;
EB90: 49            ROLA                     ;
EB91: ED 88 10      STD   $10,X              ;
EB94: D6 E1         LDB   <$E1               ;
EB96: C4 3F         ANDB  #$3F               ;
EB98: CB E0         ADDB  #$E0               ;
EB9A: 1D            SEX                      ;
EB9B: ED 0E         STD   14,X               ;
EB9D: 39            RTS                      ;

;SUBRTN
EB9E: 34 76         PSHS  U,Y,X,B,A          ;
EBA0: 97 73         STA   <$73               ;
EBA2: B6 A1 16      LDA   $A116              ;
EBA5: 4C            INCA                     ;
EBA6: 81 14         CMPA  #$14               ;
EBA8: 22 3D         BHI   $EBE7              ;
EBAA: B7 A1 16      STA   $A116              ;
EBAD: 8E EC 17      LDX   #$EC17             ;
EBB0: 86 00         LDA   #$00               ;
EBB2: BD D0 55      JSR   $D055              ;
EBB5: 33 84         LEAU  ,X                 ;
EBB7: BD D0 95      JSR   $D095              ;
EBBA: F9 7B EB      ADCB  $7BEB              ;
EBBD: E9 24         ADCB  4,Y                ;
EBBF: 24 EC         BCC   $EBAD              ;
EBC1: 2A ED         BPL   $EBB0              ;
EBC3: 0A EC         DEC   <$EC               ;
EBC5: 2C ED         BGE   $EBB4              ;
EBC7: 0C AF         INC   <$AF               ;
EBC9: 47            ASRA                     ;
EBCA: EF 06         STU   6,X                ;
EBCC: 8D BB         BSR   $EB89              ;
EBCE: DC E0         LDD   <$E0               ;
EBD0: F4 A1 0E      ANDB  $A10E              ;
EBD3: E7 49         STB   9,U                ;
EBD5: 84 1F         ANDA  #$1F               ;
EBD7: A7 44         STA   4,U                ;
EBD9: B6 A1 0D      LDA   $A10D              ;
EBDC: BD DD 9E      JSR   $DD9E              ;
EBDF: A7 4B         STA   11,U               ;
EBE1: 9F 65         STX   <$65               ;
EBE3: 0A 73         DEC   <$73               ;
EBE5: 26 BB         BNE   $EBA2              ;
EBE7: 35 F6         PULS  A,B,X,Y,U,PC       ;

EBE9: 7A A1 16      DEC   $A116              ;
EBEC: BD F3 FB      JSR   $F3FB              ;
EBEF: 34 10         PSHS  X                  ;
EBF1: BD D0 13      JSR   $D013              ;
EBF4: 35 10         PULS  X                  ;
EBF6: EC 0A         LDD   10,X               ;
EBF8: 83 00 40      SUBD  #$0040             ;
EBFB: ED 0A         STD   10,X               ;
EBFD: EC 0C         LDD   12,X               ;
EBFF: 80 02         SUBA  #$02               ;
EC01: A7 0C         STA   12,X               ;
EC03: CE F8 E2      LDU   #$F8E2             ;
EC06: EF 02         STU   2,X                ;
EC08: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
EC0B: CC 01 15      LDD   #$0115             ;
EC0E: BD D3 60      JSR   $D360              ;
EC11: CC D5 16      LDD   #$D516             ;
EC14: 7E D5 4D      JMP   $D54D              ;
EC17: AE 47         LDX   7,U                ;
EC19: F6 A1 0C      LDB   $A10C              ;
EC1C: 10 9E CC      LDY   <$CC               ;
EC1F: 10 AC 0A      CMPY  10,X               ;
EC22: 24 01         BCC   $EC25              ;
EC24: 50            NEGB                     ;
EC25: 1D            SEX                      ;
EC26: ED 0E         STD   14,X               ;
EC28: 20 54         BRA   $EC7E              ;
;service entry on InsertEventLink event link
EC2A: E6 49         LDB   9,U                ;
EC2C: AE 47         LDX   7,U                ;
EC2E: 96 C0         LDA   <$C0               ;
EC30: A1 0C         CMPA  12,X               ;
EC32: 22 01         BHI   $EC35              ;
EC34: 50            NEGB                     ;
EC35: 1D            SEX                      ;
EC36: E3 88 10      ADDD  $10,X              ;
EC39: 10 83 02 00   CMPD  #$0200             ;
EC3D: 2D 03         BLT   $EC42              ;
EC3F: CC 02 00      LDD   #$0200             ;
EC42: 10 83 FE 00   CMPD  #$FE00             ;
EC46: 2E 03         BGT   $EC4B              ;
EC48: CC FE 00      LDD   #$FE00             ;
EC4B: ED 88 10      STD   $10,X              ;
EC4E: 43            COMA                     ;
EC4F: 53            COMB                     ;
EC50: 58            ASLB                     ;
EC51: 49            ROLA                     ;
EC52: 58            ASLB                     ;
EC53: 49            ROLA                     ;
EC54: 1F 89         TFR   A,B                ;
EC56: 1D            SEX                      ;
EC57: E3 88 10      ADDD  $10,X              ;
EC5A: ED 88 10      STD   $10,X              ;
EC5D: D6 DF         LDB   <$DF               ;
EC5F: C4 1F         ANDB  #$1F               ;
EC61: CB F0         ADDB  #$F0               ;
EC63: 1D            SEX                      ;
EC64: E3 88 10      ADDD  $10,X              ;
EC67: ED 88 10      STD   $10,X              ;
EC6A: DC CC         LDD   <$CC               ;
EC6C: A3 0A         SUBD  10,X               ;
EC6E: C3 12 C0      ADDD  #$12C0             ;
EC71: 10 83 25 80   CMPD  #$2580             ;
EC75: 22 A0         BHI   $EC17              ;
EC77: 6A 4B         DEC   11,U               ;
EC79: 26 03         BNE   $EC7E              ;
EC7B: BD EC 86      JSR   $EC86              ;
EC7E: 86 03         LDA   #$03               ;load InsertEventLink event count
EC80: 8E EC 2A      LDX   #$EC2A             ;load jump point for event return
EC83: 7E D0 01      JMP   InsertEventLink         ;
EC86: 34 10         PSHS  X                  ;
EC88: DC CC         LDD   <$CC               ;
EC8A: A3 0A         SUBD  10,X               ;
EC8C: A8 0E         EORA  14,X               ;
EC8E: 2B 2F         BMI   $ECBF              ;
EC90: 31 84         LEAY  ,X                 ;
EC92: BD E3 F3      JSR   $E3F3              ;
EC95: E4 D9 F9 5B   ANDB  [$-6A5,U]          ;
EC99: E5 1E         BITB  -2,X               ;
EC9B: 27 22         BEQ   $ECBF              ;
EC9D: EC 2E         LDD   14,Y               ;
EC9F: 58            ASLB                     ;
ECA0: 49            ROLA                     ;
ECA1: 58            ASLB                     ;
ECA2: 49            ROLA                     ;
ECA3: 58            ASLB                     ;
ECA4: 49            ROLA                     ;
ECA5: ED 0E         STD   14,X               ;
ECA7: CC D5 34      LDD   #$D534             ;
ECAA: BD D5 4D      JSR   $D54D              ;
ECAD: 5F            CLRB                     ;
ECAE: 96 C0         LDA   <$C0               ;
ECB0: A0 0C         SUBA  12,X               ;
ECB2: 47            ASRA                     ;
ECB3: 56            RORB                     ;
ECB4: 47            ASRA                     ;
ECB5: 56            RORB                     ;
ECB6: 47            ASRA                     ;
ECB7: 56            RORB                     ;
ECB8: 47            ASRA                     ;
ECB9: 56            RORB                     ;
ECBA: 47            ASRA                     ;
ECBB: 56            RORB                     ;
ECBC: ED 88 10      STD   $10,X              ;
ECBF: B6 A1 0D      LDA   $A10D              ;
ECC2: BD DD 9E      JSR   $DD9E              ;
ECC5: A7 4B         STA   11,U               ;
ECC7: 35 90         PULS  X,PC               ;
;service entry on InsertEventLink event link
ECC9: AE 47         LDX   7,U                ;
ECCB: 30 02         LEAX  2,X                ;
ECCD: 8C A1 3A      CMPX  #$A13A             ;
ECD0: 25 03         BCS   $ECD5              ;
ECD2: 8E A1 1A      LDX   #$A11A             ;
ECD5: AF 47         STX   7,U                ;
ECD7: AE 84         LDX   ,X                 ;
ECD9: 27 76         BEQ   $ED51              ;
ECDB: EC 04         LDD   4,X                ;
ECDD: 27 72         BEQ   $ED51              ;
ECDF: EC 08         LDD   8,X                ;
ECE1: 10 83 ED 70   CMPD  #$ED70             ;
ECE5: 26 6A         BNE   $ED51              ;
ECE7: EC 02         LDD   2,X                ;
ECE9: 10 83 F9 0B   CMPD  #$F90B             ;
ECED: 22 2F         BHI   $ED1E              ;
ECEF: 96 DF         LDA   <$DF               ;
ECF1: 81 08         CMPA  #$08               ;
ECF3: 23 50         BLS   $ED45              ;
ECF5: BD ED 59      JSR   $ED59              ;
ECF8: 8B 04         ADDA  #$04               ;
ECFA: 81 E8         CMPA  #$E8               ;
ECFC: 23 02         BLS   $ED00              ;
ECFE: 86 E8         LDA   #$E8               ;
ED00: C6 01         LDB   #$01               ;
ED02: A1 0C         CMPA  12,X               ;
ED04: 27 07         BEQ   $ED0D              ;
ED06: 22 01         BHI   $ED09              ;
ED08: 50            NEGB                     ;
ED09: EB 0C         ADDB  12,X               ;
ED0B: E7 0C         STB   12,X               ;
ED0D: EE 02         LDU   2,X                ;
ED0F: 33 4A         LEAU  10,U               ;
ED11: 11 83 F9 0B   CMPU  #$F90B             ;
ED15: 23 03         BLS   $ED1A              ;
ED17: CE F9 01      LDU   #$F901             ;
ED1A: C6 E0         LDB   #$E0               ;
ED1C: 20 2C         BRA   $ED4A              ;
ED1E: 96 DF         LDA   <$DF               ;
ED20: 81 08         CMPA  #$08               ;
ED22: 23 F3         BLS   $ED17              ;
ED24: 8D 33         BSR   $ED59              ;
ED26: 8B 0F         ADDA  #$0F               ;
ED28: 81 E8         CMPA  #$E8               ;
ED2A: 23 02         BLS   $ED2E              ;
ED2C: 86 E8         LDA   #$E8               ;
ED2E: C6 01         LDB   #$01               ;
ED30: A1 0C         CMPA  12,X               ;
ED32: 27 07         BEQ   $ED3B              ;
ED34: 22 01         BHI   $ED37              ;
ED36: 50            NEGB                     ;
ED37: EB 0C         ADDB  12,X               ;
ED39: E7 0C         STB   12,X               ;
ED3B: EE 02         LDU   2,X                ;
ED3D: 33 4A         LEAU  10,U               ;
ED3F: 11 83 F9 1F   CMPU  #$F91F             ;
ED43: 23 03         BLS   $ED48              ;
ED45: CE F9 15      LDU   #$F915             ;
ED48: C6 20         LDB   #$20               ;
ED4A: EF 02         STU   2,X                ;
ED4C: 1D            SEX                      ;
ED4D: E3 0A         ADDD  10,X               ;
ED4F: ED 0A         STD   10,X               ;
ED51: 86 02         LDA   #$02               ;load InsertEventLink event count
ED53: 8E EC C9      LDX   #$ECC9             ;load jump point for event return
ED56: 7E D0 01      JMP   InsertEventLink         ;


;SUBRTN
ED59: 34 14         PSHS  X,B                ;
ED5B: EC 0A         LDD   10,X               ;
ED5D: 44            LSRA                     ;
ED5E: 56            RORB                     ;
ED5F: 44            LSRA                     ;
ED60: 56            RORB                     ;
ED61: 44            LSRA                     ;
ED62: 56            RORB                     ;
ED63: 44            LSRA                     ;
ED64: 56            RORB                     ;
ED65: 44            LSRA                     ;
ED66: 56            RORB                     ;
ED67: 44            LSRA                     ;
ED68: 56            RORB                     ;
ED69: 8E B3 00      LDX   #$B300             ;
ED6C: A6 8B         LDA   D,X                ;
ED6E: 35 94         PULS  B,X,PC             ;
ED70: 96 DE         LDA   <$DE               ;
ED72: 27 03         BEQ   $ED77              ;
ED74: 4F            CLRA                     ;
ED75: 35 86         PULS  A,B,PC             ;


;SUBRTN
ED77: 8D 4B         BSR   $EDC4              ;
ED79: BD F3 FB      JSR   $F3FB              ;
ED7C: CC F8 D8      LDD   #$F8D8             ;
ED7F: ED 02         STD   2,X                ;
ED81: EC 0A         LDD   10,X               ;
ED83: 83 00 40      SUBD  #$0040             ;
ED86: ED 0A         STD   10,X               ;
ED88: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
ED8B: CC D4 E4      LDD   #$D4E4             ;
ED8E: 7E D5 4D      JMP   $D54D              ;
ED91: EE 06         LDU   6,X                ;
ED93: 27 DB         BEQ   $ED70              ;
ED95: 96 DE         LDA   <$DE               ;
ED97: 27 26         BEQ   $EDBF              ;
ED99: EC 42         LDD   2,U                ;
ED9B: 10 83 F2 4C   CMPD  #$F24C             ;
ED9F: 27 16         BEQ   $EDB7              ;
EDA1: CC D4 DA      LDD   #$D4DA             ;
EDA4: BD D5 4D      JSR   $D54D              ;
EDA7: 34 10         PSHS  X                  ;
EDA9: 8E EE 73      LDX   #$EE73             ;
EDAC: 86 00         LDA   #$00               ;
EDAE: BD D0 55      JSR   $D055              ;
EDB1: 31 84         LEAY  ,X                 ;
EDB3: 35 10         PULS  X                  ;
EDB5: AF 27         STX   7,Y                ;
EDB7: CC F2 4C      LDD   #$F24C             ;
EDBA: ED 42         STD   2,U                ;
EDBC: 4F            CLRA                     ;
EDBD: 35 86         PULS  A,B,PC             ;
EDBF: 8D B6         BSR   $ED77              ;
EDC1: 7E D0 13      JMP   $D013              ;


;SUBRTN
EDC4: 31 84         LEAY  ,X                 ;
EDC6: 34 52         PSHS  U,X,A              ;
EDC8: CE A1 1A      LDU   #$A11A             ;
EDCB: 86 40         LDA   #$40               ;
EDCD: 10 AC C1      CMPY  ,U++               ;
EDD0: 27 06         BEQ   $EDD8              ;
EDD2: 4A            DECA                     ;
EDD3: 26 F8         BNE   $EDCD              ;
EDD5: BD D0 3A      JSR   $D03A              ;
EDD8: 4F            CLRA                     ;
EDD9: 5F            CLRB                     ;
EDDA: ED 5E         STD   -2,U               ;
EDDC: 0A FA         DEC   <$FA               ;
EDDE: 26 08         BNE   $EDE8              ;
EDE0: 8E ED EA      LDX   #$EDEA             ;
EDE3: 86 00         LDA   #$00               ;
EDE5: BD D0 55      JSR   $D055              ;
EDE8: 35 D2         PULS  A,X,U,PC           ;

EDEA: 96 BA         LDA   <$BA               ;
EDEC: 8A 02         ORA   #$02               ;
EDEE: 97 BA         STA   <$BA               ;
EDF0: 6F 47         CLR   7,U                ;
EDF2: BD F4 FF      JSR   ROMPg7             ;
EDF5: BD C0 09      JSR   $C009              ;
EDF8: 8E B1 25      LDX   #$B125             ;
EDFB: CE 00 00      LDU   #$0000             ;
EDFE: 86 40         LDA   #$40               ;
EE00: EF 91         STU   [,X++]             ;
EE02: 4A            DECA                     ;
EE03: 26 FB         BNE   $EE00              ;
EE05: 9E 67         LDX   <$67               ;
EE07: CC F9 F1      LDD   #$F9F1             ;
EE0A: ED 02         STD   2,X                ;
EE0C: C6 02         LDB   #$02               ;
EE0E: D7 73         STB   <$73               ;
EE10: BD D7 11      JSR   $D711              ;
EE13: 84 3F         ANDA  #$3F               ;
EE15: D3 20         ADDD  <$20               ;
EE17: ED 0A         STD   10,X               ;
EE19: BD ED 59      JSR   $ED59              ;
EE1C: A7 0C         STA   12,X               ;
EE1E: 80 0A         SUBA  #$0A               ;
EE20: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
EE23: 0A 73         DEC   <$73               ;
EE25: 26 E9         BNE   $EE10              ;
EE27: 96 DF         LDA   <$DF               ;
EE29: 84 1F         ANDA  #$1F               ;
EE2B: 8E E7 99      LDX   #$E799             ;
EE2E: A6 86         LDA   A,X                ;
EE30: 97 26         STA   <$26               ;
EE32: CC D4 E4      LDD   #$D4E4             ;
EE35: BD D5 4D      JSR   $D54D              ;
EE38: 8E EE 44      LDX   #$EE44             ;load jump point for event return
EE3B: 86 02         LDA   #$02               ;load InsertEventLink event count
EE3D: C6 08         LDB   #$08               ;
EE3F: D7 5E         STB   <$5E               ;
EE41: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
EE44: 0F 26         CLR   <$26               ;
EE46: A6 47         LDA   7,U                ;coming up with an event count between here ...
EE48: 44            LSRA                     ;
EE49: 44            LSRA                     ;
EE4A: 44            LSRA                     ;
EE4B: 4C            INCA                     ;
EE4C: BD DD 9E      JSR   $DD9E              ;
EE4F: 8E EE 54      LDX   #$EE54             ;load jump point for event return
EE52: 20 E9         BRA   $EE3D              ;... and here
;service entry on InsertEventLink event link
EE54: 6C 47         INC   7,U                ;
EE56: A6 47         LDA   7,U                ;
EE58: 81 10         CMPA  #$10               ;
EE5A: 26 A9         BNE   $EE05              ;
EE5C: CC D4 C7      LDD   #$D4C7             ;
EE5F: BD D5 4D      JSR   $D54D              ;
EE62: 7E D0 0A      JMP   $D00A              ;
EE65: BD D0 95      JSR   $D095              ;
EE68: F9 DD ED      ADCB  $DDED              ;
EE6B: BC 00 00      CMPX  $0000              ;
EE6E: CC 01 25      LDD   #$0125             ;
EE71: 20 0C         BRA   $EE7F              ;
EE73: BD D0 95      JSR   $D095              ;
EE76: F9 E7 ED      ADCB  $E7ED              ;
EE79: BC 00 00      CMPX  $0000              ;
EE7C: CC 01 50      LDD   #$0150             ;
EE7F: BD D3 60      JSR   $D360              ;
EE82: 10 AE 47      LDY   7,U                ;
EE85: DC C7         LDD   <$C7               ;
EE87: ED 0E         STD   14,X               ;
EE89: CC 00 00      LDD   #$0000             ;
EE8C: ED 88 10      STD   $10,X              ;
EE8F: 86 11         LDA   #$11               ;
EE91: A7 88 14      STA   $14,X              ;
EE94: EC 2A         LDD   10,Y               ;
EE96: ED 0A         STD   10,X               ;
EE98: EC 2C         LDD   12,Y               ;
EE9A: 2B 05         BMI   $EEA1              ;
EE9C: C3 18 00      ADDD  #$1800             ;
EE9F: 20 03         BRA   $EEA4              ;
EEA1: 83 20 00      SUBD  #$2000             ;
EEA4: ED 0C         STD   12,X               ;
EEA6: 9F 65         STX   <$65               ;
EEA8: AF 47         STX   7,U                ;
EEAA: 86 32         LDA   #$32               ;load InsertEventLink event count
EEAC: 8E EE B2      LDX   #$EEB2             ;load jump point for event return
EEAF: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
EEB2: AE 47         LDX   7,U                ;
EEB4: BD F3 FB      JSR   $F3FB              ;
EEB7: 7E D0 0A      JMP   $D00A              ;


;SUBRTN
EEBA: 34 10         PSHS  X                  ;
EEBC: BD E3 F3      JSR   $E3F3              ;
EEBF: E4 D9 F9 5B   ANDB  [$-6A5,U]          ;
EEC3: E5 1E         BITB  -2,X               ;
EEC5: 27 35         BEQ   $EEFC              ;
EEC7: D6 DF         LDB   <$DF               ;
EEC9: C4 1F         ANDB  #$1F               ;
EECB: CB F0         ADDB  #$F0               ;
EECD: DB BF         ADDB  <$BF               ;
EECF: E0 04         SUBB  4,X                ;
EED1: 1D            SEX                      ;
EED2: 58            ASLB                     ;
EED3: 49            ROLA                     ;
EED4: 58            ASLB                     ;
EED5: 49            ROLA                     ;
EED6: ED 0E         STD   14,X               ;
EED8: D6 DF         LDB   <$DF               ;
EEDA: C1 78         CMPB  #$78               ;
EEDC: 23 0A         BLS   $EEE8              ;
EEDE: DC C7         LDD   <$C7               ;
EEE0: 58            ASLB                     ;
EEE1: 49            ROLA                     ;
EEE2: 58            ASLB                     ;
EEE3: 49            ROLA                     ;
EEE4: E3 0E         ADDD  14,X               ;
EEE6: ED 0E         STD   14,X               ;
EEE8: D6 E1         LDB   <$E1               ;
EEEA: C4 1F         ANDB  #$1F               ;
EEEC: CB F0         ADDB  #$F0               ;
EEEE: DB C0         ADDB  <$C0               ;
EEF0: E0 05         SUBB  5,X                ;
EEF2: 1D            SEX                      ;
EEF3: 58            ASLB                     ;
EEF4: 49            ROLA                     ;
EEF5: 58            ASLB                     ;
EEF6: 49            ROLA                     ;
EEF7: ED 88 10      STD   $10,X              ;
EEFA: 86 01         LDA   #$01               ;
EEFC: 35 90         PULS  X,PC               ;


;SUBRTN
EEFE: 6A 4D         DEC   13,U               ;
EF00: 26 12         BNE   $EF14              ;
EF02: B6 A1 05      LDA   $A105              ;
EF05: BD DD 9E      JSR   $DD9E              ;
EF08: A7 4D         STA   13,U               ;
EF0A: 8D AE         BSR   $EEBA              ;
EF0C: 27 06         BEQ   $EF14              ;
EF0E: CC D5 25      LDD   #$D525             ;
EF11: BD D5 4D      JSR   $D54D              ;
EF14: 39            RTS                      ;


;SUBRTN
EF15: 34 02         PSHS  A                  ;
EF17: 97 73         STA   <$73               ;
EF19: 8E F1 5E      LDX   #$F15E             ;
EF1C: 86 00         LDA   #$00               ;
EF1E: BD D0 55      JSR   $D055              ;
EF21: 33 84         LEAU  ,X                 ;
EF23: BD D0 95      JSR   $D095              ;
EF26: F8 CE EF      EORB  $CEEF              ;
EF29: 6D CC 33      TST   $33,PC             ;
EF2C: BD D7 11      JSR   $D711              ;
EF2F: DC 20         LDD   <$20               ;
EF31: 83 25 80      SUBD  #$2580             ;
EF34: DD 75         STD   <$75               ;
EF36: DC E0         LDD   <$E0               ;
EF38: 93 75         SUBD  <$75               ;
EF3A: 10 83 4B 00   CMPD  #$4B00             ;
EF3E: 24 03         BCC   $EF43              ;
EF40: C3 80 00      ADDD  #$8000             ;
EF43: D3 75         ADDD  <$75               ;
EF45: ED 0A         STD   10,X               ;
EF47: 96 DF         LDA   <$DF               ;
EF49: 44            LSRA                     ;
EF4A: 8B 2A         ADDA  #$2A               ;
EF4C: A7 0C         STA   12,X               ;
EF4E: 4F            CLRA                     ;
EF4F: 5F            CLRB                     ;
EF50: ED 88 10      STD   $10,X              ;
EF53: ED 0E         STD   14,X               ;
EF55: B6 A1 0B      LDA   $A10B              ;
EF58: BD DD 9E      JSR   $DD9E              ;
EF5B: A7 47         STA   7,U                ;
EF5D: BD FC 60      JSR   $FC60              ;
EF60: EF 06         STU   6,X                ;
EF62: AF 47         STX   7,U                ;
EF64: 7C A1 15      INC   $A115              ;
EF67: 0A 73         DEC   <$73               ;
EF69: 26 AE         BNE   $EF19              ;
EF6B: 35 82         PULS  A,PC               ;

EF6D: 7A A1 15      DEC   $A115              ;
EF70: BD F4 16      JSR   $F416              ;
EF73: 01 
EF74: 15 
EF75: D4 F8         ANDB  <$F8               ;
EF77: 39            RTS                      ;


;SUBRTN
EF78: 34 10         PSHS  X                  ;
EF7A: 96 FA         LDA   <$FA               ;
EF7C: 27 1C         BEQ   $EF9A              ;
EF7E: 9E 9B         LDX   <$9B               ;
EF80: 30 02         LEAX  2,X                ;
EF82: 8C A1 5A      CMPX  #$A15A             ;
EF85: 25 03         BCS   $EF8A              ;
EF87: 8E A1 1A      LDX   #$A11A             ;
EF8A: EC 84         LDD   ,X                 ;
EF8C: 26 06         BNE   $EF94              ;
EF8E: 9C 9B         CMPX  <$9B               ;
EF90: 26 EE         BNE   $EF80              ;
EF92: 35 90         PULS  X,PC               ;
EF94: 9F 9B         STX   <$9B               ;
EF96: ED 49         STD   9,U                ;
EF98: AF 4B         STX   11,U               ;
EF9A: 35 90         PULS  X,PC               ;


;SUBRTN
EF9C: 34 02         PSHS  A                  ;
EF9E: 97 73         STA   <$73               ;
EFA0: 0D FA         TST   <$FA               ;
EFA2: 26 03         BNE   $EFA7              ;
EFA4: 7E EF 19      JMP   $EF19              ;
EFA7: 8E EF F6      LDX   #$EFF6             ;
EFAA: 86 00         LDA   #$00               ;
EFAC: BD D0 55      JSR   $D055              ;
EFAF: 33 84         LEAU  ,X                 ;
EFB1: BD D0 95      JSR   $D095              ;
EFB4: F9 85 F2      ADCB  $85F2              ;
EFB7: 0B 
EFB8: 44            LSRA                     ;
EFB9: 33 BD D7 11   LEAU  [$-28EF,PC]        ;
EFBD: DC E0         LDD   <$E0               ;
EFBF: ED 0A         STD   10,X               ;
EFC1: 86 2C         LDA   #$2C               ;
EFC3: A7 0C         STA   12,X               ;
EFC5: FC A1 03      LDD   $A103              ;
EFC8: ED 88 10      STD   $10,X              ;
EFCB: B6 A1 05      LDA   $A105              ;
EFCE: BD DD 9E      JSR   $DD9E              ;
EFD1: A7 4D         STA   13,U               ;
EFD3: B6 A1 02      LDA   $A102              ;
EFD6: BD DD 9E      JSR   $DD9E              ;
EFD9: 1F 89         TFR   A,B                ;
EFDB: 4F            CLRA                     ;
EFDC: C5 01         BITB  #$01               ;
EFDE: 27 02         BEQ   $EFE2              ;
EFE0: 53            COMB                     ;
EFE1: 43            COMA                     ;
EFE2: ED 0E         STD   14,X               ;
EFE4: EF 06         STU   6,X                ;
EFE6: BD FC 60      JSR   $FC60              ;
EFE9: AF 47         STX   7,U                ;
EFEB: 8D 8B         BSR   $EF78              ;
EFED: 7C A1 12      INC   $A112              ;
EFF0: 0A 73         DEC   <$73               ;
EFF2: 26 AC         BNE   $EFA0              ;
EFF4: 35 82         PULS  A,PC               ;

;service entry on InsertEventLink event link
EFF6: AE 47         LDX   7,U                ;
EFF8: 10 AE 49      LDY   9,U                ;
EFFB: EC D8 0B      LDD   [$0B,U]            ;
EFFE: 27 16         BEQ   $F016              ;
F000: A6 29         LDA   9,Y                ;
F002: 81 70         CMPA  #$70               ;
F004: 26 10         BNE   $F016              ;
F006: A6 0A         LDA   10,X               ;
F008: 84 FC         ANDA  #$FC               ;
F00A: 97 73         STA   <$73               ;
F00C: A6 2A         LDA   10,Y               ;
F00E: 84 FC         ANDA  #$FC               ;
F010: 91 73         CMPA  <$73               ;
F012: 27 51         BEQ   $F065              ;
F014: 20 0F         BRA   $F025              ;
F016: A6 88 14      LDA   $14,X              ;
F019: 84 FE         ANDA  #$FE               ;
F01B: A7 88 14      STA   $14,X              ;
F01E: BD EF 78      JSR   $EF78              ;
F021: 10 27 01 19   LBEQ  $F13E              ;
F025: BD ED 59      JSR   $ED59              ;
F028: 80 32         SUBA  #$32               ;
F02A: A0 0C         SUBA  12,X               ;
F02C: 22 0F         BHI   $F03D              ;
F02E: 81 EC         CMPA  #$EC               ;
F030: 2D 04         BLT   $F036              ;
F032: 4F            CLRA                     ;
F033: 5F            CLRB                     ;
F034: 20 0A         BRA   $F040              ;
F036: FC A1 03      LDD   $A103              ;
F039: 43            COMA                     ;
F03A: 53            COMB                     ;
F03B: 20 03         BRA   $F040              ;
F03D: FC A1 03      LDD   $A103              ;
F040: ED 88 10      STD   $10,X              ;
F043: EC 02         LDD   2,X                ;
F045: 10 83 F8 EC   CMPD  #$F8EC             ;
F049: 27 12         BEQ   $F05D              ;
F04B: BD EE FE      JSR   $EEFE              ;
F04E: EE 02         LDU   2,X                ;
F050: 33 4A         LEAU  10,U               ;
F052: 11 83 F9 99   CMPU  #$F999             ;
F056: 23 03         BLS   $F05B              ;
F058: CE F9 85      LDU   #$F985             ;
F05B: EF 02         STU   2,X                ;
F05D: 86 06         LDA   #$06               ;load InsertEventLink event count
F05F: 8E EF F6      LDX   #$EFF6             ;load jump point for event return
F062: 7E D0 01      JMP   InsertEventLink         ;
F065: 4F            CLRA                     ;
F066: 5F            CLRB                     ;
F067: 6C 88 14      INC   $14,X              ;
F06A: ED 0E         STD   14,X               ;
F06C: ED 88 10      STD   $10,X              ;
F06F: CC F9 85      LDD   #$F985             ;
F072: ED 02         STD   2,X                ;
;service entry on InsertEventLink event link
F074: AE 47         LDX   7,U                ;
F076: 10 AE 49      LDY   9,U                ;
F079: EC D8 0B      LDD   [$0B,U]            ;
F07C: 27 98         BEQ   $F016              ;
F07E: A6 29         LDA   9,Y                ;
F080: 81 70         CMPA  #$70               ;
F082: 26 92         BNE   $F016              ;
F084: EC 2A         LDD   10,Y               ;
F086: C4 E0         ANDB  #$E0               ;
F088: DD 75         STD   <$75               ;
F08A: EC 0A         LDD   10,X               ;
F08C: C4 E0         ANDB  #$E0               ;
F08E: 10 93 75      CMPD  <$75               ;
F091: 27 0D         BEQ   $F0A0              ;
F093: 2D 04         BLT   $F099              ;
F095: C6 E0         LDB   #$E0               ;
F097: 20 02         BRA   $F09B              ;
F099: C6 20         LDB   #$20               ;
F09B: 1D            SEX                      ;
F09C: E3 0A         ADDD  10,X               ;
F09E: ED 0A         STD   10,X               ;
F0A0: A6 2C         LDA   12,Y               ;
F0A2: 80 0C         SUBA  #$0C               ;
F0A4: A1 0C         CMPA  12,X               ;
F0A6: 27 16         BEQ   $F0BE              ;
F0A8: FC A1 03      LDD   $A103              ;
F0AB: 24 02         BCC   $F0AF              ;
F0AD: 43            COMA                     ;
F0AE: 53            COMB                     ;
F0AF: E3 0C         ADDD  12,X               ;
F0B1: ED 0C         STD   12,X               ;
F0B3: BD EE FE      JSR   $EEFE              ;
F0B6: 86 01         LDA   #$01               ;load InsertEventLink event count
F0B8: 8E F0 74      LDX   #$F074             ;load jump point for event return
F0BB: 7E D0 01      JMP   InsertEventLink         ;
F0BE: EC 0A         LDD   10,X               ;
F0C0: C3 00 40      ADDD  #$0040             ;
F0C3: A3 2A         SUBD  10,Y               ;
F0C5: 10 83 00 80   CMPD  #$0080             ;
F0C9: 22 E8         BHI   $F0B3              ;
F0CB: CC F1 E0      LDD   #$F1E0             ;
F0CE: ED 08         STD   8,X                ;
F0D0: FC A1 03      LDD   $A103              ;
F0D3: 53            COMB                     ;
F0D4: 43            COMA                     ;
F0D5: ED 88 10      STD   $10,X              ;
F0D8: ED A8 10      STD   $10,Y              ;
F0DB: CC D5 0C      LDD   #$D50C             ;
F0DE: BD D5 4D      JSR   $D54D              ;
F0E1: CC ED 91      LDD   #$ED91             ;
F0E4: ED 28         STD   8,Y                ;
;service entry on InsertEventLink event link
F0E6: DE 63         LDU   <$63               ;
F0E8: AE 47         LDX   7,U                ;
F0EA: A6 0C         LDA   12,X               ;
F0EC: 81 32         CMPA  #$32               ;
F0EE: 23 0B         BLS   $F0FB              ;
F0F0: BD EE FE      JSR   $EEFE              ;
F0F3: 86 04         LDA   #$04               ;load InsertEventLink event count
F0F5: 8E F0 E6      LDX   #$F0E6             ;load jump point for event return
F0F8: 7E D0 01      JMP   InsertEventLink         ;
F0FB: CC D5 11      LDD   #$D511             ;
F0FE: BD D5 4D      JSR   $D54D              ;
;service entry on InsertEventLink event link
F101: AE 47         LDX   7,U                ;
F103: 10 AE 49      LDY   9,U                ;
F106: EC D8 0B      LDD   [$0B,U]            ;
F109: 26 0B         BNE   $F116              ;
F10B: BD F3 FB      JSR   $F3FB              ;
F10E: 7A A1 12      DEC   $A112              ;
F111: 0C FB         INC   <$FB               ;
F113: 7E D0 0A      JMP   $D00A              ;
F116: 4F            CLRA                     ;
F117: 5F            CLRB                     ;
F118: ED 88 10      STD   $10,X              ;
F11B: ED A8 10      STD   $10,Y              ;
F11E: A6 2C         LDA   12,Y               ;
F120: A1 0C         CMPA  12,X               ;
F122: 23 0F         BLS   $F133              ;
F124: 6A 2C         DEC   12,Y               ;
F126: 86 12         LDA   #$12               ;
F128: BD D5 39      JSR   $D539              ;play a sound, not sure which one, though.
F12B: 86 01         LDA   #$01               ;load InsertEventLink event count
F12D: 8E F1 01      LDX   #$F101             ;load jump point for event return
F130: 7E D0 01      JMP   InsertEventLink         ;
F133: 30 A4         LEAX  ,Y                 ;
F135: EC 24         LDD   4,Y                ;
F137: 8B 01         ADDA  #$01               ;
F139: DD F8         STD   <$F8               ;
F13B: BD ED 77      JSR   $ED77              ;
F13E: 7A A1 12      DEC   $A112              ;
F141: 7C A1 15      INC   $A115              ;
F144: AE 47         LDX   7,U                ;
F146: 6F 88 14      CLR   $14,X              ;
F149: CC F8 CE      LDD   #$F8CE             ;
F14C: ED 02         STD   2,X                ;
F14E: CC CC 33      LDD   #$CC33             ;
F151: ED 88 12      STD   $12,X              ;
F154: CC EF 6D      LDD   #$EF6D             ;
F157: ED 08         STD   8,X                ;
F159: B6 A1 0B      LDA   $A10B              ;
F15C: A7 49         STA   9,U                ;
;service entry on InsertEventLink event link
F15E: AE 47         LDX   7,U                ;
F160: F6 A1 0A      LDB   $A10A              ;
F163: 10 9E CC      LDY   <$CC               ;
F166: 10 AC 0A      CMPY  10,X               ;
F169: 2C 01         BGE   $F16C              ;
F16B: 50            NEGB                     ;
F16C: 1D            SEX                      ;
F16D: ED 0E         STD   14,X               ;
F16F: DC CC         LDD   <$CC               ;
F171: A3 0A         SUBD  10,X               ;
F173: C3 01 7C      ADDD  #$017C             ;
F176: 10 83 07 00   CMPD  #$0700             ;
F17A: 23 21         BLS   $F19D              ;
F17C: 96 C0         LDA   <$C0               ;
F17E: A0 0C         SUBA  12,X               ;
F180: 23 0B         BLS   $F18D              ;
F182: 81 08         CMPA  #$08               ;
F184: 22 0B         BHI   $F191              ;
F186: FC A1 08      LDD   $A108              ;
F189: 43            COMA                     ;
F18A: 53            COMB                     ;
F18B: 20 0B         BRA   $F198              ;
F18D: 81 F8         CMPA  #$F8               ;
F18F: 2E 04         BGT   $F195              ;
F191: 4F            CLRA                     ;
F192: 5F            CLRB                     ;
F193: 20 03         BRA   $F198              ;
F195: FC A1 08      LDD   $A108              ;
F198: ED 88 10      STD   $10,X              ;
F19B: 20 12         BRA   $F1AF              ;
F19D: 96 C0         LDA   <$C0               ;
F19F: A1 0C         CMPA  12,X               ;
F1A1: FC A1 08      LDD   $A108              ;
F1A4: 24 02         BCC   $F1A8              ;
F1A6: 43            COMA                     ;
F1A7: 53            COMB                     ;
F1A8: ED 88 10      STD   $10,X              ;
F1AB: EC 04         LDD   4,X                ;
F1AD: 27 29         BEQ   $F1D8              ;
F1AF: F6 A1 07      LDB   $A107              ;
F1B2: 96 DF         LDA   <$DF               ;
F1B4: 2B 01         BMI   $F1B7              ;
F1B6: 50            NEGB                     ;
F1B7: EB 0C         ADDB  12,X               ;
F1B9: C1 2A         CMPB  #$2A               ;
F1BB: 24 02         BCC   $F1BF              ;
F1BD: C6 F0         LDB   #$F0               ;
F1BF: E7 0C         STB   12,X               ;
F1C1: 6A 49         DEC   9,U                ;
F1C3: 26 13         BNE   $F1D8              ;
F1C5: B6 A1 0B      LDA   $A10B              ;
F1C8: BD DD 9E      JSR   $DD9E              ;
F1CB: A7 49         STA   9,U                ;
F1CD: BD EE BA      JSR   $EEBA              ;
F1D0: 27 06         BEQ   $F1D8              ;
F1D2: CC D5 2A      LDD   #$D52A             ;
F1D5: BD D5 4D      JSR   $D54D              ;
F1D8: 86 03         LDA   #$03               ;load InsertEventLink event count
F1DA: 8E F1 5E      LDX   #$F15E             ;load jump point for event return
F1DD: 7E D0 01      JMP   InsertEventLink         ;
F1E0: EE 06         LDU   6,X                ;
F1E2: EC D8 0B      LDD   [$0B,U]            ;
F1E5: 27 24         BEQ   $F20B              ;
F1E7: CC 00 00      LDD   #$0000             ;
F1EA: CC 00 00      LDD   #$0000             ;
F1ED: 34 10         PSHS  X                  ;
F1EF: 8E F2 16      LDX   #$F216             ;
F1F2: 86 00         LDA   #$00               ;
F1F4: BD D0 55      JSR   $D055              ;
F1F7: EE 49         LDU   9,U                ;
F1F9: EF 07         STU   7,X                ;
F1FB: CC D4 E9      LDD   #$D4E9             ;
F1FE: BD D5 4D      JSR   $D54D              ;
F201: CC 00 00      LDD   #$0000             ;
F204: ED C8 10      STD   $10,U              ;
F207: AF 46         STX   6,U                ;
F209: 35 10         PULS  X                  ;
F20B: 7A A1 12      DEC   $A112              ;
F20E: BD F4 16      JSR   $F416              ;
F211: 01 
F212: 15 
F213: D5 07         BITB  <$07               ;
F215: 39            RTS                      ;
;service entry on InsertEventLink event link
F216: AE 47         LDX   7,U                ;
F218: CC 00 08      LDD   #$0008             ;
F21B: E3 88 10      ADDD  $10,X              ;
F21E: 10 83 03 00   CMPD  #$0300             ;
F222: 24 03         BCC   $F227              ;
F224: ED 88 10      STD   $10,X              ;
F227: BD ED 59      JSR   $ED59              ;
F22A: A1 0C         CMPA  12,X               ;
F22C: 22 16         BHI   $F244              ;
F22E: EC 88 10      LDD   $10,X              ;
F231: 10 83 00 E0   CMPD  #$00E0             ;
F235: 23 39         BLS   $F270              ;
F237: EC 04         LDD   4,X                ;
F239: C3 01 07      ADDD  #$0107             ;
F23C: DD F8         STD   <$F8               ;
F23E: BD ED 77      JSR   $ED77              ;
F241: 7E D0 0A      JMP   $D00A              ;
F244: 86 04         LDA   #$04               ;load InsertEventLink event count
F246: 8E F2 16      LDX   #$F216             ;load jump point for event return
F249: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
F24C: AE 47         LDX   7,U                ;
F24E: CC 00 00      LDD   #$0000             ;
F251: ED 88 10      STD   $10,X              ;
F254: 96 C5         LDA   <$C5               ;
F256: 8B 0A         ADDA  #$0A               ;
F258: A7 0C         STA   12,X               ;
F25A: DC CC         LDD   <$CC               ;
F25C: C3 00 80      ADDD  #$0080             ;
F25F: ED 0A         STD   10,X               ;
F261: BD ED 59      JSR   $ED59              ;
F264: A1 0C         CMPA  12,X               ;
F266: 25 0F         BCS   $F277              ;
F268: 86 01         LDA   #$01               ;load InsertEventLink event count
F26A: 8E F2 4C      LDX   #$F24C             ;load jump point for event return
F26D: 7E D0 01      JMP   InsertEventLink         ;
F270: 34 10         PSHS  X                  ;
F272: 8E EE 65      LDX   #$EE65             ;
F275: 20 05         BRA   $F27C              ;
F277: 34 10         PSHS  X                  ;
F279: 8E EE 73      LDX   #$EE73             ;
F27C: 86 00         LDA   #$00               ;
F27E: BD D0 55      JSR   $D055              ;
F281: 31 84         LEAY  ,X                 ;
F283: 35 10         PULS  X                  ;
F285: AF 27         STX   7,Y                ;
F287: CC 00 00      LDD   #$0000             ;
F28A: ED 06         STD   6,X                ;
F28C: ED 88 10      STD   $10,X              ;
F28F: CC ED 70      LDD   #$ED70             ;
F292: ED 08         STD   8,X                ;
F294: CC D4 DF      LDD   #$D4DF             ;
F297: BD D5 4D      JSR   $D54D              ;
F29A: 7E D0 0A      JMP   $D00A              ;
F29D: 97 73         STA   <$73               ;
F29F: F6 A1 06      LDB   $A106              ;
F2A2: 03 AA         COM   <$AA               ;
F2A4: 2B 01         BMI   $F2A7              ;
F2A6: 50            NEGB                     ;
F2A7: D7 74         STB   <$74               ;
F2A9: 8E F2 F7      LDX   #$F2F7             ;
F2AC: 86 00         LDA   #$00               ;
F2AE: BD D0 3E      JSR   $D03E              ;
F2B1: 33 84         LEAU  ,X                 ;
F2B3: 96 73         LDA   <$73               ;
F2B5: A7 4F         STA   15,U               ;
F2B7: 4F            CLRA                     ;
F2B8: 5F            CLRB                     ;
F2B9: ED 47         STD   7,U                ;
F2BB: ED 49         STD   9,U                ;
F2BD: ED 4B         STD   11,U               ;
F2BF: ED 4D         STD   13,U               ;
F2C1: BD D0 95      JSR   $D095              ;
F2C4: F9 29 F3      ADCB  $29F3              ;
F2C7: BC 88 88      CMPX  $8888              ;
F2CA: D6 74         LDB   <$74               ;
F2CC: 1D            SEX                      ;
F2CD: ED 0E         STD   14,X               ;
F2CF: 4F            CLRA                     ;
F2D0: 5F            CLRB                     ;
F2D1: ED 88 10      STD   $10,X              ;
F2D4: 96 73         LDA   <$73               ;
F2D6: 44            LSRA                     ;
F2D7: 56            RORB                     ;
F2D8: 9B 73         ADDA  <$73               ;
F2DA: D3 CC         ADDD  <$CC               ;
F2DC: 8B 80         ADDA  #$80               ;
F2DE: ED 0A         STD   10,X               ;
F2E0: 86 50         LDA   #$50               ;
F2E2: A7 0C         STA   12,X               ;
F2E4: A7 C8 10      STA   $10,U              ;
F2E7: EF 06         STU   6,X                ;
F2E9: 9F 65         STX   <$65               ;
F2EB: 96 73         LDA   <$73               ;
F2ED: 48            ASLA                     ;
F2EE: 8B 05         ADDA  #$05               ;
F2F0: AF C6         STX   A,U                ;
F2F2: 0A 73         DEC   <$73               ;
F2F4: 26 CB         BNE   $F2C1              ;
F2F6: 39            RTS                      ;
;service entry on InsertEventLink event link
F2F7: 96 DF         LDA   <$DF               ;
F2F9: 84 06         ANDA  #$06               ;
F2FB: 8B 07         ADDA  #$07               ;
F2FD: AE C6         LDX   A,U                ;
F2FF: 10 27 00 B1   LBEQ  $F3B4              ;
F303: D6 DF         LDB   <$DF               ;
F305: 86 0A         LDA   #$0A               ;
F307: C4 3F         ANDB  #$3F               ;
F309: CB E0         ADDB  #$E0               ;
F30B: 2B 01         BMI   $F30E              ;
F30D: 40            NEGA                     ;
F30E: 10 AE 02      LDY   2,X                ;
F311: 31 A6         LEAY  A,Y                ;
F313: 10 8C F9 29   CMPY  #$F929             ;
F317: 24 04         BCC   $F31D              ;
F319: 10 8E F9 29   LDY   #$F929             ;
F31D: 10 8C F9 47   CMPY  #$F947             ;
F321: 23 04         BLS   $F327              ;
F323: 10 8E F9 47   LDY   #$F947             ;
F327: 10 AF 02      STY   2,X                ;
F32A: 1D            SEX                      ;
F32B: E3 88 10      ADDD  $10,X              ;
F32E: ED 88 10      STD   $10,X              ;
F331: 58            ASLB                     ;
F332: 49            ROLA                     ;
F333: 58            ASLB                     ;
F334: 49            ROLA                     ;
F335: 58            ASLB                     ;
F336: 49            ROLA                     ;
F337: 1F 89         TFR   A,B                ;
F339: 50            NEGB                     ;
F33A: 1D            SEX                      ;
F33B: E3 88 10      ADDD  $10,X              ;
F33E: ED 88 10      STD   $10,X              ;
F341: A6 05         LDA   5,X                ;
F343: 26 3B         BNE   $F380              ;
F345: 96 DF         LDA   <$DF               ;
F347: 81 40         CMPA  #$40               ;
F349: 22 16         BHI   $F361              ;
F34B: 84 03         ANDA  #$03               ;
F34D: 8B FE         ADDA  #$FE               ;
F34F: AB C8 10      ADDA  $10,U              ;
F352: 81 40         CMPA  #$40               ;
F354: 24 02         BCC   $F358              ;
F356: 86 40         LDA   #$40               ;
F358: 81 68         CMPA  #$68               ;
F35A: 25 02         BCS   $F35E              ;
F35C: 86 68         LDA   #$68               ;
F35E: A7 C8 10      STA   $10,U              ;
F361: A6 C8 10      LDA   $10,U              ;
F364: A0 0C         SUBA  12,X               ;
F366: 8B 10         ADDA  #$10               ;
F368: 81 20         CMPA  #$20               ;
F36A: 23 48         BLS   $F3B4              ;
F36C: 80 10         SUBA  #$10               ;
F36E: 2B 05         BMI   $F375              ;
F370: CC FF F0      LDD   #$FFF0             ;
F373: 20 03         BRA   $F378              ;
F375: CC 00 10      LDD   #$0010             ;
F378: E3 88 10      ADDD  $10,X              ;
F37B: ED 88 10      STD   $10,X              ;
F37E: 20 34         BRA   $F3B4              ;
F380: 90 C0         SUBA  <$C0               ;
F382: 2B 12         BMI   $F396              ;
F384: 81 20         CMPA  #$20               ;
F386: 25 05         BCS   $F38D              ;
F388: CC FF F0      LDD   #$FFF0             ;
F38B: 20 19         BRA   $F3A6              ;
F38D: 81 10         CMPA  #$10               ;
F38F: 22 1B         BHI   $F3AC              ;
F391: CC 00 10      LDD   #$0010             ;
F394: 20 10         BRA   $F3A6              ;
F396: 81 E0         CMPA  #$E0               ;
F398: 2E 05         BGT   $F39F              ;
F39A: CC 00 10      LDD   #$0010             ;
F39D: 20 07         BRA   $F3A6              ;
F39F: 81 F0         CMPA  #$F0               ;
F3A1: 2D 09         BLT   $F3AC              ;
F3A3: CC FF F0      LDD   #$FFF0             ;
F3A6: E3 88 10      ADDD  $10,X              ;
F3A9: ED 88 10      STD   $10,X              ;
F3AC: 96 E1         LDA   <$E1               ;
F3AE: 84 07         ANDA  #$07               ;
F3B0: 26 02         BNE   $F3B4              ;
F3B2: 8D 28         BSR   $F3DC              ;
F3B4: 86 01         LDA   #$01               ;load InsertEventLink event count
F3B6: 8E F2 F7      LDX   #$F2F7             ;load jump point for event return
F3B9: 7E D0 01      JMP   InsertEventLink         ;
F3BC: BD F4 1D      JSR   $F41D              ;
F3BF: 01 
F3C0: 25 D5         BCS   $F397              ;
F3C2: 02 
F3C3: 7A A1 13      DEC   $A113              ;
F3C6: EE 06         LDU   6,X                ;
F3C8: 31 47         LEAY  7,U                ;
F3CA: AC A1         CMPX  ,Y++               ;
F3CC: 26 FC         BNE   $F3CA              ;
F3CE: 4F            CLRA                     ;
F3CF: 5F            CLRB                     ;
F3D0: ED 3E         STD   -2,Y               ;
F3D2: 6A 4F         DEC   15,U               ;
F3D4: 26 05         BNE   $F3DB              ;
F3D6: 30 C4         LEAX  ,U                 ;
F3D8: BD D0 15      JSR   $D015              ;
F3DB: 39            RTS                      ;

F3DC: 96 99         LDA   <$99               ;
F3DE: 81 0A         CMPA  #$0A               ;
F3E0: 24 18         BCC   $F3FA              ;
F3E2: BD E3 F3      JSR   $E3F3              ;
F3E5: E4 98 F9      ANDB  [$-7,X]            ;
F3E8: 5B 
F3E9: E5 1E         BITB  -2,X               ;
F3EB: 27 0D         BEQ   $F3FA              ;
F3ED: D6 E0         LDB   <$E0               ;
F3EF: 1D            SEX                      ;
F3F0: 58            ASLB                     ;
F3F1: 49            ROLA                     ;
F3F2: 96 DF         LDA   <$DF               ;
F3F4: 84 1F         ANDA  #$1F               ;
F3F6: 4C            INCA                     ;
F3F7: A7 88 15      STA   $15,X              ;
F3FA: 39            RTS                      ;


;SUBRTN
F3FB: BD D0 C7      JSR   $D0C7              ;


;SUBRTN
F3FE: 34 76         PSHS  U,Y,X,B,A          ;
F400: BD F5 03      JSR   ROMPg2             ;
F403: EC 04         LDD   4,X                ;
F405: 10 AE 02      LDY   2,X                ;
F408: AD B8 08      JSR   [$08,Y]            ;
F40B: 35 F6         PULS  A,B,X,Y,U,PC       ;

F40D: 34 10         PSHS  X                  ;
F40F: BD D0 13      JSR   $D013              ;
F412: 35 10         PULS  X                  ;
F414: 20 0A         BRA   $F420              ;


;SUBRTN
F416: 34 10         PSHS  X                  ;
F418: BD D0 13      JSR   $D013              ;
F41B: 35 10         PULS  X                  ;



;SUBRTN
F41D: BD D0 C7      JSR   $D0C7              ;
F420: 34 46         PSHS  U,B,A              ;
F422: EE 64         LDU   4,S                ;loading the return address?
F424: 37 06         PULU  A,B                ;
F426: BD D3 60      JSR   $D360              ;
F429: 8D 09         BSR   $F434              ;
F42B: 37 06         PULU  A,B                ;
F42D: EF 64         STU   4,S                ;
F42F: BD D5 4D      JSR   $D54D              ;
F432: 35 C6         PULS  A,B,U,PC           ;



;SUBRTN
F434: 34 76         PSHS  U,Y,X,B,A          ;
F436: 8D C6         BSR   $F3FE              ;
F438: BD FC 63      JSR   $FC63              ;"JSR  $FCCC" would have been faster
F43B: 35 F6         PULS  A,B,X,Y,U,PC       ;

F43D: 8E F4 5B      LDX   #$F45B             ;
F440: AF 47         STX   7,U                ;
F442: 86 06         LDA   #$06               ;load InsertEventLink event count
F444: 8E F4 4A      LDX   #$F44A             ;load jump point for event return
F447: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
F44A: AE 47         LDX   7,U                ;
F44C: EC 81         LDD   ,X++               ;
F44E: DD 33         STD   <$33               ;
F450: A6 80         LDA   ,X+                ;
F452: 97 35         STA   <$35               ;
F454: 8C F4 64      CMPX  #$F464             ;
F457: 25 E7         BCS   $F440              ;
F459: 20 E2         BRA   $F43D              ;

F45B: 81 81 2F 81 2F 
F460: 07 2F 81 07 

;service entry on InsertEventLink event link
F464: 86 FF         LDA #$FF                 ;
F466: 97 30         STA <$30                 ;
F468: 0F 32         CLR <$32                 ;
F46A: 86 03         LDA #$03                 ;load InsertEventLink event count
F46C: 8E F4 72      LDX #$F472               ;load jump point for event return
F46F: 7E D0 01      JMP >InsertEventLink     ;
;service entry on InsertEventLink event link
F472: 96 DF         LDA <$DF                 ;
F474: 84 1F         ANDA  #$1F               ;
F476: 8E E7 99      LDX   #$E799             ;
F479: A6 86         LDA   A,X                ;
F47B: 97 30         STA   <$30               ;
F47D: 97 32         STA   <$32               ;
F47F: 8E CC B0      LDX   #$CCB0             ;
F482: 9C A6         CMPX  <$A6               ;
F484: 26 03         BNE   $F489              ;
F486: 8E CC BC      LDX   #$CCBC             ;
F489: 9F A6         STX   <$A6               ;
F48B: 86 06         LDA   #$06               ;load InsertEventLink event count
F48D: 8E F4 64      LDX   #$F464             ;load jump point for event return
F490: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
F493: 96 8A         LDA   <$8A               ;
F495: 26 24         BNE   $F4BB              ;
F497: 8E 0F 1C      LDX   #$0F1C             ;
F49A: 96 8B         LDA   <$8B               ;
F49C: 4A            DECA                     ;
F49D: 27 03         BEQ   $F4A2              ;
F49F: 8E 71 1C      LDX   #$711C             ;
F4A2: CC 18 08      LDD   #$1808             ;
F4A5: BD F5 C7      JSR   ScrnBlkClr         ;
F4A8: 86 08         LDA   #$08               ;load InsertEventLink event count
F4AA: 8E F4 B0      LDX   #$F4B0             ;load jump point for event return
F4AD: 7E D0 01      JMP   InsertEventLink         ;
;service entry on InsertEventLink event link
F4B0: BD D3 D9      JSR   $D3D9              ;
F4B3: 86 0C         LDA   #$0C               ;load InsertEventLink event count
F4B5: 8E F4 93      LDX   #$F493             ;load jump point for event return
F4B8: 7E D0 01      JMP   InsertEventLink         ;
F4BB: 7E D0 0A      JMP   $D00A              ;

This appears to be an interface to the InsertEventLink routine for the paged ROMs? I don't understand the reason for it, yet. Some of the destinations/counts in bank 1 are: $C0DA/1, $C144/255, $C1DC/60, $C1E7/15, $C1FD/1, $C2EB/10, $C412/230, $C429/160, $C475/21, $C49C/2, $C500/80, $C531/96, $C585/95, $C598/23, $C5CA/32, $C5DA/32, $C5ED/255, $C677/255, $C605/1, $C66B/6, $C6B0/2, $C738/5, $C754/48, $C7B7/46, $C7D4/40, $C831/10, $C848/1, $C8F4/16, $C92E/2.
There is an entry in the jump table for this routine, but it is used only once in bank 7. Its destination/count is $C649/1

InsEventLnkPgSav     ;in jump table
F4BE: DE 63         LDU   <$63               ;
F4C0: AF 4D         STX   13,U               ;
F4C2: D6 36         LDB   <$36               ;
F4C4: E7 4C         STB   12,U               ;
F4C6: 8E F4 CC      LDX   #$F4CC             ;load jump point for event return
F4C9: 7E D0 01      JMP   InsertEventLink    ;the count for InsertEventLink depends on the calling routine
;service entry on InsertEventLink event link
F4CC: A6 4C         LDA   12,U               ;
F4CE: 8D 3D         BSR   SwtchPgNum         ;
F4D0: 6E D8 0D      JMP   [13,U]             ;

This subroutine allows you to call a subroutine that is located in a ROM page other than the one you are currently using. The call (BSR, LBSR, or JSR) must have the subroutine address in the two immediate bytes following it. The third byte after it must have the page # that you wish to call.

CallOtherPage      ;
F4D3: 32 7D         LEAS  -3,S               ;create scratchpad area
F4D5: 34 42         PSHS  U,A                ;save U and A regs
F4D7: 96 36         LDA   <$36               ;get IO/ROM page #
F4D9: A7 65         STA   5,S                ;store it
F4DB: EE 66         LDU   6,S                ;get the return address
F4DD: A6 42         LDA   2,U                ;load A reg with ROM page #
F4DF: EE C4         LDU   ,U                 ;load U reg with subroutine address
F4E1: EF 63         STU   3,S                ;store that in the scratchpad space
F4E3: 8D 28         BSR   SwtchPgNum         ;change to designated ROM bank
F4E5: 35 42         PULS  A,U                ;restore U and A regs
F4E7: AD F4         JSR   [,S]               ;call the subroutine
F4E9: 34 42         PSHS  U,A                ;save U and A regs again
F4EB: A6 65         LDA   5,S                ;get calling ROM page # back
F4ED: 8D 1E         BSR   SwtchPgNum         ;switch back to caller
F4EF: EE 66         LDU   6,S                ;get return address
F4F1: 33 43         LEAU  3,U                ;adjust past subroutine and page # infor
F4F3: EF 66         STU   6,S                ;store it on stack
F4F5: 35 42         PULS  A,U                ;restore U and A again
F4F7: 32 63         LEAS  3,S                ;return scratchpad space
F4F9: 39            RTS                      ;return



;SUBRTN
F4FA: 8D 03         BSR   ROMPg7             ;
F4FC: 7E C0 00      JMP   $C000              ;go to $C015 in bank 7

Multiple entry points, one for each page # available for the 
address area $C000-$CFFF, page 0 excepted, being the I/O page/bank. Register A is mangled. 
<$36 is changed to reflect the current page #.

ROMPg7      ;SUBRTN
F4FF: 86 07         LDA   #$07               ;
F501: 20 0A         BRA   SwtchPgNum         ;
ROMPg2      ;SUBRTN                     ;subroutine to change ROM page to 2
F503: 86 02         LDA   #$02               ;
F505: 20 06         BRA   SwtchPgNum         ;
ROMPg3      ;SUBRTN                     ;subroutine to change ROM page to 3
F507: 86 03         LDA   #$03               ;
F509: 20 02         BRA   SwtchPgNum         ;
ROMPg1      ;SUBRTN                     ;subroutine to change ROM page to 1
F50B: 86 01         LDA   #$01               ;
SwtchPgNum  ;SUBRTN                     ;subroutine to change to page # specified by contents of A reg
F50D: 97 36         STA   <$36               ;store ROM page #
F50F: B7 D0 00      STA   $D000              ;change ROM page
F512: 39            RTS                      ;go back



;SUBRTN
F513: 34 7F         PSHS  U,Y,X,DP,B,A,CC    ;this is the only place I can find where all of the regs are pushed onto the stack
F515: 8D EC         BSR   ROMPg2             ;change to ROM 2
F517: BD C0 02      JSR   $C002              ;$CAA7 in ROM 2
F51A: 35 FF         PULS  CC,A,B,DP,X,Y,U,PC ;and then they are pulled along with the PC for a return



;SUBRTN
F51C: 8D E9         BSR   ROMPg3             ;change to ROM 3
F51E: 7E C0 0F      JMP   $C00F              ;$CBE0 on ROM 3
F521: 39            RTS                      ;


This paints in shapes according to the data in the address that is passed? Used to paint alphanumeric characters on screen, score and possibly extra ships (lives) and bombs.


It doesn't look very useful for the dynamic portion of the game screen, I think. Only for the "lives", bombs, and score, perhaps?



> ; on entry ; Y = offset in page 2 of source character data. ; D = screen
>> address of top left pixel ; memory pointed at by Y contains the following:
>> ; [width], [height], [address of data]  
DrawChar     ;SUBRTN
F522: 34 76         PSHS  U,Y,X,B,A          ;
F524: 1F 01         TFR   D,X                ; X = D (screen address)
F526: 96 36         LDA   <$36               ;save current page #
F528: 34 02         PSHS  A                  ;on the stack
F52A: 86 02         LDA   #$02               ; A = 2
F52C: 97 36         STA   <$36               ; [$36] = 2
F52E: B7 D0 00      STA   $D000              ;page 2
F531: EC A4         LDD   ,Y                 ; D = Y[0], A = width, B = height
F533: 10 AE 22      LDY   2,Y                ; Y = Y[2] 
F536: 34 06         PSHS  B,A                ; save width and height on stack. 
F538: C5 01         BITB  #$01               ; is B (height) odd?
F53A: 26 17         BNE   DrawCharOdd        ; yes, skip even code...
DrawCharEven
F53C: C0 02         SUBB  #$02               ; pre-decrement
DrawCharEvenInner
F53E: EE A5         LDU   B,Y                ; U = Y[B] read two bytes from source
F540: EF 85         STU   B,X                ; X[B] = U write two bytes to screen
F542: C0 02         SUBB  #$02               ;pre-decrement for next pair of bytes, if any
F544: 2A F8         BPL   DrawCharEvenInner  ;if still positive or 0, there's more to do
F546: E6 61         LDB   1,S                ; get B (height) back.
F548: 30 89 01 00   LEAX  $0100,X            ; move right two pixels on the screen. 
F54C: 31 A5         LEAY  B,Y                ; Y += B move right two pixels in the source.
F54E: 4A            DECA                     ; one less column to do.
F54F: 26 EB         BNE   DrawCharEven       ; if there are more cols to do, go back
F551: 20 1D         BRA   DrawCharExit       ; Done. DrawCharOdd ;odd # of bytes
DrawCharOdd
F553: 5A            DECB                     ; pre-decrement
F554: A6 A5         LDA   B,Y                ; A = Y[B] read one byte from source
F556: A7 85         STA   B,X                ; X[B] = A write one byte to screen
F558: C0 02         SUBB  #$02               ; pre-decrement even part.
F55A: 2B 08         BMI   DrawCharOddOuter   ; if there was only one, skip the middle.
DrawCharOddInner
F55C: EE A5         LDU   B,Y                ; U = Y[B] read two bytes from source
F55E: EF 85         STU   B,X                ; X[B] = U write two bytes to screen
F560: C0 02         SUBB  #$02               ;pre-decrement for next pair of bytes, if any
F562: 2A F8         BPL   DrawCharOddInner   ;if still positive or 0, there's more to do
DrawCharOddOuter
F564: E6 61         LDB   1,S                ; get B (height) back.
F566: 30 89 01 00   LEAX  $0100,X            ; move right two pixels on the screen.
F56A: 31 A5         LEAY  B,Y                ; Y += B move right two pixels in the source.
F56C: 6A E4         DEC   ,S                 ; one less column to do.
F56E: 26 E3         BNE   DrawCharOdd        ; if there are more cols to do, go back
DrawCharExit
F570: 32 62         LEAS  2,S                ; skip past width and height on the stack. 
F572: 35 02         PULS  A                  ; pop previous page number from the stack
F574: 97 36         STA   <$36               ; save previous page number in [$36] 
F576: B7 D0 00      STA   $D000              ;restore page #
F579: 35 F6         PULS  A,B,X,Y,U,PC       ; pop all registers and do hack RET by popping PC.



Clear video memory block.
ScrnBlkClrP2      ;SUBRTN
F57B: 34 56         PSHS  U,X,B,A            ;
F57D: 1F 01         TFR   D,X                ;
F57F: 96 36         LDA   <$36               ;save page #
F581: 34 02         PSHS  A                  ;on the stack
F583: 86 02         LDA   #$02               ;
F585: 97 36         STA   <$36               ;page 2
F587: B7 D0 00      STA   $D000              ;   what is the purpose of changing the ROM page #?
F58A: EC A4         LDD   ,Y                 ;index reg Y points to size of block to clear
; A=# of lines to clear, B=# of bytes/line to clear
F58C: CE 00 00      LDU   #$0000             ;need some 0's for clearing memory
F58F: 34 04         PSHS  B                  ;
F591: C5 01         BITB  #$01               ;even or odd?
F593: 26 13         BNE   $F5A8              ;branch to odd if bit 0 is set
;even # of bytes to clear
F595: C0 02         SUBB  #$02               ;have to assume there is at least 2 bytes, otherwise why would we be here?
F597: EF 85         STU   B,X                ;clear them
F599: C0 02         SUBB  #$02               ;check for two more
F59B: 2A FA         BPL   $F597              ;loop until they're all done
F59D: E6 E4         LDB   ,S                 ;reload our byte count
F59F: 30 89 01 00   LEAX  $0100,X            ;go to next line
F5A3: 4A            DECA                     ;
F5A4: 26 EF         BNE   $F595              ;keep looping until all lines are done
F5A6: 20 16         BRA   $F5BE              ;restore and return when done
;odd # of bytes to clear
F5A8: 5A            DECB                     ;there is at least one byte to clear, take care of that part of the count
F5A9: 6F 85         CLR   B,X                ;clear that byte
F5AB: C0 02         SUBB  #$02               ;is there a pair of bytes to clear now?
F5AD: 2B 06         BMI   $F5B5              ;if it goes negative there isn't
F5AF: EF 85         STU   B,X                ;clear two more bytes
F5B1: C0 02         SUBB  #$02               ;check for two more bytes
F5B3: 2A FA         BPL   $F5AF              ;loop until all bytes cleared
F5B5: E6 E4         LDB   ,S                 ;recover byte count
F5B7: 30 89 01 00   LEAX  $0100,X            ;next line
F5BB: 4A            DECA                     ;
F5BC: 26 EA         BNE   $F5A8              ;keep looping for all lines
F5BE: 35 06         PULS  A,B                ;former contents of A,B is now swapped B,A
F5C0: D7 36         STB   <$36               ;
F5C2: F7 D0 00      STB   $D000              ;restore previous page #
F5C5: 35 D6         PULS  A,B,X,U,PC         ;

ScrnBlkClr      ;SUBRTN Entry point where we don't change the page #, although, it must still be saved on the stack
F5C7: 34 56         PSHS  U,X,B,A            ;
F5C9: 96 36         LDA   <$36               ;save page #
F5CB: 34 02         PSHS  A                  ;on the stack
F5CD: A6 61         LDA   1,S                ;recover A reg entry value w/o changing the stack pointer
F5CF: 20 BB         BRA   $F58C              ;


Clear video memory completely

VidMemClr      ;SUBRTN
;clear video memory, 32 bytes per loop
F5D1: 34 76         PSHS  U,Y,X,B,A          ;
F5D3: CE 9C 00      LDU   #$9C00             ;
F5D6: 8E 00 00      LDX   #$0000             ;
F5D9: 1F 12         TFR   X,Y                ;
F5DB: 1F 10         TFR   X,D                ;
F5DD: 36 36         PSHU  Y,X,B,A            ;6 bytes cleared
F5DF: 36 36         PSHU  Y,X,B,A            ;12 bytes cleared
F5E1: 36 36         PSHU  Y,X,B,A            ;18 bytes cleared
F5E3: 36 36         PSHU  Y,X,B,A            ;24 bytes cleared
F5E5: 36 36         PSHU  Y,X,B,A            ;30 bytes cleared
F5E7: 36 10         PSHU  X                  ;32 bytes cleared, (11~*5+7)*1248 =
F5E9: 11 83 00 00   CMPU  #$0000             ;1248 loops of 32 bytes each
F5ED: 26 EE         BNE   $F5DD              ;
F5EF: 35 F6         PULS  A,B,X,Y,U,PC       ;39,936 bytes cleared, let's restore registers we changed and go back

Clear video memory in blocks of 214 bytes + 42 bytes which are not cleared, for a total of 256 bytes per block.

ClrVidMem       ;SUBRTN
;clear video memory, in blocks of 256 bytes, 42 bytes of which are untouched
F5F1: 34 7E         PSHS  U,Y,X,DP,B,A       ;
F5F3: CE 9C 00      LDU   #$9C00             ;
F5F6: 8E 00 00      LDX   #$0000             ;
F5F9: 1F 12         TFR   X,Y                ;
F5FB: 1F 10         TFR   X,D                ;
F5FD: 1F 8B         TFR   A,DP               ;
F5FF: C6 08         LDB   #$08               ;
F601: 36 3A         PSHU  Y,X,DP,A           ;
F603: 36 3A         PSHU  Y,X,DP,A           ;
F605: 36 3A         PSHU  Y,X,DP,A           ;
F607: 36 3A         PSHU  Y,X,DP,A           ;
F609: 5A            DECB                     ;8 loops of 24 bytes each = 192
F60A: 26 F5         BNE   $F601              ;
F60C: 36 3A         PSHU  Y,X,DP,A           ;
F60E: 36 3A         PSHU  Y,X,DP,A           ;
F610: 36 3A         PSHU  Y,X,DP,A           ;
F612: 36 30         PSHU  Y,X                ;22 more bytes + 192 = 214
F614: 33 C8 D6      LEAU  $-2A,U             ;214 + 42 skipped bytes = 256
F617: 11 83 00 00   CMPU  #$0000             ;
F61B: 26 E2         BNE   $F5FF              ;keep doing this 156 times until the video memory is cleared
F61D: 35 FE         PULS  A,B,DP,X,Y,U,PC    ;



 RESET
 Defender powers up and starts here

selecting colors for display? \\
Numbers stored in 7489/189/289's 
are 1's complemented on output. However, since the output is again inverted by PNP transistors, my original table was in error. This was made readily apparent to me by Patrick Naughton's [https://dl.dropboxusercontent.com/u/8722788/6809/index.html Defender emulator]. Thank you, Patrick. Here is the corrected table.  \\
Values generated are as follows \\

            RED    GREEN    BLUE (Adjusted weight of blue value)



RESET
F61F: 7F D0 00      CLR   $D000              ; Switch to bank 0 (I/O page)
F622: 8E CC 00      LDX   #PIA_addr_base     ; Load PIA base address
; setting up some 6821 PIAs here
F625: 6F 01         CLR   1,X                ;Setup for PIAs at $CC00 and $CC04
F627: 6F 03         CLR   3,X                ;going to data direction registers (DDR) on all of them
F629: 6F 05         CLR   5,X                ;
F62B: 6F 07         CLR   7,X                ;
F62D: 86 C0         LDA   #$C0               ;
F62F: A7 84         STA   ,X                 ;$CC00, ch A to two outputs (LEDs) and 6 inputs (coin door)
F631: 86 FF         LDA   #$FF               ;
F633: A7 02         STA   2,X                ;$CC02, ch B to 8 outputs (sound and LEDs)
F635: 6F 04         CLR   4,X                ;$CC04, ch A to eight inputs
F637: 6F 06         CLR   6,X                ;$CC06, ch B to eight inputs
F639: 86 04         LDA   #$04               ;switch 3 of the 4 to peripheral I/O registers,CA(B)1 hi2low & int disabled,CA(B)2 is input, hi2low active & int disabled
F63B: A7 03         STA   3,X                ;$CC02, ch B
F63D: A7 05         STA   5,X                ;$CC04, ch A
F63F: A7 07         STA   7,X                ;$CC06, ch B
F641: 8A 10         ORA   #$10               ;Switch first PIO reg to IO reg, CA1 hi2low & int disabled, CA2 made input w/ low2hi active & int disabled
F643: A7 01         STA   1,X                ;

F645: 8E C0 00      LDX   #$C000             ;address of first register in color value index registers
F648: 86 C0         LDA   #$C0               ;load value to be stored in $C000 (color value to sub for a 0 nybble)
Loop0002
F64A: A7 80         STA   ,X+                ;store it and increment pointer
F64C: C6 B5         LDB   #$B5               ;load constant for multiplying
F64E: 3D            MUL                      ;create value for next color
F64F: 8C C0 10      CMPX  #$C010             ;are we done?
F652: 26 F6         BNE   Loop0002           ;loop if not


F654: 1A 80         ORCC  #$80               ;set CCR.7 (Entire)
F656: 1C EF         ANDCC #$EF               ;reset CCR.4 (IRQ)
F658: 10 8E 00 02   LDY   #$0002             ;load the number of DRAM tests to perform
F65C: 4F            CLRA                     ;
F65D: 1F 8B         TFR   A,DP               ;made direct page reg a 0
F65F: 1C BF         ANDCC #$BF               ;reset CCR.6 (FIRQ)
F661: 5F            CLRB                     ;start with 0 in the D reg in this next part. 

This is a DRAM test. It does its test by placing a pseudo random, "carpet" pattern in the DRAM, and then going through the same sequence again to compare what's in memory to the contents of the D register. At the end of the first test, if everything went well and Y is greater than 1, it takes the final value in D to start over, and do it all again. The Y register is used as a counter for the number of RAM tests to perform. \\

RAMTest
F662: 1F 03         TFR   D,U                ;save this starting value so we can duplicate this sequence for testing
F664: 8E 00 00      LDX   #$0000             ;
Loop0001
F667: 53            COMB                     ;
F668: C5 09         BITB  #$09               ;
F66A: 26 05         BNE   $F671              ;
F66C: 53            COMB                     ;
F66D: 46            RORA                     ;
F66E: 56            RORB                     ;
F66F: 20 0B         BRA   $F67C              ;
F671: 53            COMB                     ;
F672: C5 09         BITB  #$09               ;
F674: 26 04         BNE   $F67A              ;
F676: 46            RORA                     ;
F677: 56            RORB                     ;
F678: 20 02         BRA   $F67C              ;
F67A: 44            LSRA                     ;
F67B: 56            RORB                     ;
F67C: ED 81         STD   ,X++               ;
F67E: 1E 10         EXG   X,D                ;
F680: 5D            TSTB                     ;
F681: 26 17         BNE   $F69A              ;
F683: C6 38         LDB   #$38               ;
F685: F7 C3 FC      STB   $C3FC              ;reset watchdog
F688: 1F A9         TFR   CCR,B              ;
F68A: C5 10         BITB  #$10               ;IRQ masked?
F68C: 27 0B         BEQ   $F699              ;
F68E: 7F D0 00      CLR   $D000              ;access I/O page (*PSO low)
F691: F6 CC 00      LDB   PIA_addr_base      ;
F694: 53            COMB                     ;
F695: C5 03         BITB  #$03               ;
F697: 27 51         BEQ   $F6EA              ;
F699: 5F            CLRB                     ;
F69A: 1E 10         EXG   X,D                ;
F69C: 8C C0 00      CMPX  #$C000             ;
F69F: 26 C6         BNE   Loop0001           ;
F6A1: 1F 30         TFR   U,D                ;
F6A3: 8E 00 00      LDX   #$0000             ;
F6A6: 53            COMB                     ;
F6A7: C5 09         BITB  #$09               ;
F6A9: 26 05         BNE   $F6B0              ;
F6AB: 53            COMB                     ;
F6AC: 46            RORA                     ;
F6AD: 56            RORB                     ;
F6AE: 20 0B         BRA   $F6BB              ;
F6B0: 53            COMB                     ;
F6B1: C5 09         BITB  #$09               ;
F6B3: 26 04         BNE   $F6B9              ;
F6B5: 46            RORA                     ;
F6B6: 56            RORB                     ;
F6B7: 20 02         BRA   $F6BB              ;
F6B9: 44            LSRA                     ;
F6BA: 56            RORB                     ;
F6BB: 10 A3 81      CMPD  ,X++               ;
F6BE: 27 17         BEQ   $F6D7              ;
F6C0: 1E 02         EXG   D,Y                ;
F6C2: 1F A8         TFR   CCR,A              ;
F6C4: 85 10         BITA  #$10               ;
F6C6: 27 0A         BEQ   $F6D2              ;
F6C8: 86 03         LDA   #$03               ;
F6CA: 97 36         STA   <$36               ;store page # before changing it
F6CC: B7 D0 00      STA   $D000              ;changing to page 3
F6CF: 7E C0 2A      JMP   $C02A              ;
F6D2: 4F            CLRA                     ;
F6D3: 1E 20         EXG   Y,D                ;
F6D5: 1A 40         ORCC  #$40               ;
F6D7: 1E 10         EXG   X,D                ;
F6D9: 5D            TSTB                     ;
F6DA: 26 42         BNE   $F71E              ;
F6DC: 1F A9         TFR   CCR,B              ;
F6DE: C5 10         BITB  #$10               ;
F6E0: 27 12         BEQ   $F6F4              ;
F6E2: F6 CC 00      LDB   PIA_addr_base      ;
F6E5: 53            COMB                     ;
F6E6: C5 03         BITB  #$03               ;
F6E8: 26 2E         BNE   $F718              ;
F6EA: 86 03         LDA   #$03               ;
F6EC: 97 36         STA   <$36               ;store page #
F6EE: B7 D0 00      STA   $D000              ;page 3
F6F1: 7E C0 2D      JMP   $C02D              ;"JMP $C2C3"
F6F4: 1F A9         TFR   CCR,B              ;
F6F6: C5 40         BITB  #$40               ;
F6F8: 27 1E         BEQ   $F718              ;
F6FA: 1C BF         ANDCC #$BF               ;
F6FC: 1F B9         TFR   DP,B               ;
F6FE: 1F 8B         TFR   A,DP               ;
F700: 80 03         SUBA  #$03               ;
F702: 24 FC         BCC   $F700              ;
F704: 4C            INCA                     ;
F705: 26 04         BNE   $F70B              ;
F707: CA 02         ORB   #$02               ;
F709: 20 09         BRA   $F714              ;
F70B: 4C            INCA                     ;
F70C: 26 04         BNE   $F712              ;
F70E: CA 01         ORB   #$01               ;
F710: 20 02         BRA   $F714              ;
F712: CA 04         ORB   #$04               ;
F714: 1F B8         TFR   DP,A               ;
F716: 1F 9B         TFR   B,DP               ;
F718: C6 38         LDB   #$38               ;
F71A: F7 C3 FC      STB   $C3FC              ;clear the watchdog
F71D: 5F            CLRB                     ;
F71E: 1E 10         EXG   X,D                ;
F720: 8C C0 00      CMPX  #$C000             ;have we compared all the DRAM data to our "random" data yet?
F723: 10 26 FF 7F   LBNE  $F6A6              ;if not, go back and do another pair of bytes
F727: 31 3F         LEAY  -1,Y               ;do any more DRAM testing?
F729: 10 26 FF 35   LBNE  RAMTest            ;yes?, well let's go do it again then

ROM check \\

F72D: 1F A9         TFR   CCR,B              ;
F72F: 5D            TSTB                     ;
F730: 2B 0B         BMI   $F73D              ;skip this next part if the E (entire) flag is set
F732: C6 03         LDB   #$03               ;
F734: F7 D0 00      STB   $D000              ;set page to 3
F737: BD F8 00      JSR   $F800              ;clear <$49,<$52, put 3 in <$36,<$48, put $FFFF in <$59
F73A: 7E C0 30      JMP   $C030              ;"JMP $C406"
F73D: C5 10         BITB  #$10               ;is the IRQ flag set?
F73F: 10 26 FF 1F   LBNE  RAMTest            ;if the IRQ is set, then test DRAM again? Why?
F743: 86 9E         LDA   #$9E               ;IRQ not set, so ...
F745: 1F B9         TFR   DP,B               ;
F747: 5D            TSTB                     ;is the DP still zero?
F748: 27 04         BEQ   $F74E              ;then we must change it to $9E
F74A: 4C            INCA                     ;
F74B: 54            LSRB                     ;
F74C: 25 FC         BCS   $F74A              ;
F74E: 1F 8B         TFR   A,DP               ;changing the DP to $9E, or perhaps another value as well?
F750: 8B 01         ADDA  #$01               ;
F752: 5F            CLRB                     ;
F753: 1F 04         TFR   D,S                ;set system stack to next memory page
F755: BD F8 00      JSR   $F800              ;clear <$49,<$52, put 3 in <$36,<$48, put $FFFF in <$59

;SUBRTN in jump table
F758: CE F8 6E      LDU   #$F86E             ;
F75B: 7F D0 00      CLR   $D000              ;switch to I/O page
F75E: 86 38         LDA   #$38               ;
F760: B7 C3 FC      STA   $C3FC              ;clear the watchdog
F763: A6 C4         LDA   ,U                 ;
F765: E6 C4         LDB   ,U                 ;
F767: 27 2A         BEQ   $F793              ;
F769: C4 0F         ANDB  #$0F               ;
F76B: F7 D0 00      STB   $D000              ;
F76E: 84 70         ANDA  #$70               ;
F770: 44            LSRA                     ;
F771: 8B C0         ADDA  #$C0               ;
F773: 5F            CLRB                     ;
F774: 1F 01         TFR   D,X                ;
F776: 10 8E 08 00   LDY   #$0800             ;
F77A: 1F 30         TFR   U,D                ;
F77C: C0 6C         SUBB  #$6C               ;
F77E: 54            LSRB                     ;
F77F: 4F            CLRA                     ;
F780: E9 80         ADCB  ,X+                ;
F782: 31 3F         LEAY  -1,Y               ;
F784: 26 FA         BNE   $F780              ;
F786: C1 80         CMPB  #$80               ;
F788: 27 09         BEQ   $F793              ;
F78A: 1F A8         TFR   CCR,A              ;
F78C: 85 10         BITA  #$10               ;
F78E: 27 3E         BEQ   $F7CE              ;
F790: 7E F5 07      JMP   ROMPg3             ;switch to page 3 and return

F793: 33 41         LEAU  1,U                ;
F795: 11 83 F8 86   CMPU  #$F886             ;
F799: 26 C0         BNE   $F75B              ;checking more ROMs?
F79B: 1F A8         TFR   CCR,A              ;
F79D: 85 10         BITA  #$10               ;is IRQ mask set?
F79F: 26 EF         BNE   $F790              ;

F7A1: 1F B8         TFR   DP,A               ;
F7A3: 81 9E         CMPA  #$9E               ;
F7A5: 26 08         BNE   $F7AF              ;
F7A7: BD F5 07      JSR   ROMPg3             ;switch to page 3
F7AA: BD C0 00      JSR   $C000              ;looking for coin input, etc.?
F7AD: 20 26         BRA   $F7D5              ;
F7AF: C6 40         LDB   #$40               ;
F7B1: 8D 05         BSR   $F7B8              ;
F7B3: BD C0 03      JSR   $C003              ;
F7B6: 20 1D         BRA   $F7D5              ;



;SUBRTN
F7B8: 8E CC 00      LDX   #PIA_addr_base        ;
F7BB: E7 84         STB   ,X                 ;set/reset LEDs, possible sound output
F7BD: E7 02         STB   2,X                ;set/reset LEDs
F7BF: 7F D0 00      CLR   $D000              ;make sure it's the I/O page? little late for that?
F7C2: 86 38         LDA   #$38               ;
F7C4: B7 C3 FC      STA   $C3FC              ;reset watchdog
F7C7: 30 1F         LEAX  -1,X               ;wait for a while
F7C9: 26 F7         BNE   $F7C2              ;
F7CB: 7E F5 07      JMP   ROMPg3             ;change to page 3 and return



F7CE: C6 80         LDB   #$80               ;
F7D0: 8D E6         BSR   $F7B8              ;
F7D2: BD C0 06      JSR   $C006              ;
F7D5: BD C0 09      JSR   $C009              ;
F7D8: 7E D7 38      JMP   $D738              ;



WriteIOPort      ;SUBRTN
F7DB: 34 03         PSHS  A,CC               ;save regs A & CCR
F7DD: 96 36         LDA   <$36               ;get the $C000 page #
F7DF: 34 02         PSHS  A                  ;save it on the stack
F7E1: 0F 36         CLR   <$36               ;put a zero in the page # reg
F7E3: 7F D0 00      CLR   $D000              ;switch to I/O page
F7E6: E7 84         STB   ,X                 ;write data to port addressed by X reg
F7E8: 35 02         PULS  A                  ;restore previous $C000 page #
F7EA: 97 36         STA   <$36               ;store it
F7EC: B7 D0 00      STA   $D000              ;switch back to previous page #
F7EF: 35 83         PULS  CC,A,PC            ;restore regs A & CCR, and return

ReadIOPort      ;SUBRTN
F7F1: 34 03         PSHS  A,CC               ;save regs A & CCR
F7F3: 96 36         LDA   <$36               ;get the $C000 page #
F7F5: 34 02         PSHS  A                  ;save it on the stack
F7F7: 0F 36         CLR   <$36               ;put a zero in the page # reg
F7F9: 7F D0 00      CLR   $D000              ;switch to I/O page
F7FC: E6 84         LDB   ,X                 ;read data from port addressed by X reg
F7FE: 20 E8         BRA   $F7E8              ;go to convergence with $F7DB routine



;SUBRTN
F800: 34 06         PSHS  B,A                ;
F802: 0F 52         CLR   <$52               ;
F804: 0F 49         CLR   <$49               ;
F806: 86 03         LDA   #$03               ;
F808: 97 36         STA   <$36               ;
F80A: 97 48         STA   <$48               ;
F80C: CC FF FF      LDD   #$FFFF             ;
F80F: DD 59         STD   <$59               ;
F811: 35 86         PULS  A,B,PC             ;



SRAMRead      ;SUBRTN
F813: A6 01         LDA   1,X                ;load least significant nybble first
F815: 84 0F         ANDA  #$0F               ;mask noise in upper nybble
F817: 34 02         PSHS  A                  ;save it
F819: A6 81         LDA   ,X++               ;load most significant nybble now and advance beyond these two nybbles
F81B: 48            ASLA                     ;multiply by 16
F81C: 48            ASLA                     ;
F81D: 48            ASLA                     ;
F81E: 48            ASLA                     ;
F81F: AB E0         ADDA  ,S+                ;add the LSNyb and advance past it on stack
F821: 39            RTS                      ;return with byte in the A reg


RdSRAMbyte      ;SUBRTN
F822: 34 04         PSHS  B                  ;save B reg
F824: D6 36         LDB   <$36               ;save $C000 page #
F826: 34 04         PSHS  B                  ;save it on the stack
F828: 0F 36         CLR   <$36               ;
F82A: 7F D0 00      CLR   $D000              ;switch to I/O page
F82D: 8D E4         BSR   SRAMRead           ;
F82F: 35 04         PULS  B                  ;retrieve $C000 page # from stack
F831: D7 36         STB   <$36               ;
F833: F7 D0 00      STB   $D000              ;restore it
F836: 35 84         PULS  B,PC               ;restore B reg and return with byte in A reg


SRAMWordRd      ;SUBRTN (16 bit call)
F838: 8D E8         BSR   RdSRAMbyte         ;we want 4 nybbles in a word in the D reg


SRAMByteRd      ;SUBRTN (8 bit call)
F83A: 34 02         PSHS  A                  ;saving MSB(16 bit)/contents of A reg on call entry(8 bit)
F83C: 8D E4         BSR   RdSRAMbyte         ;get the LSB
F83E: 1F 89         TFR   A,B                ;put LSB in B reg
F840: 35 82         PULS  A,PC               ;restore MSB(16 bit)/contents of A reg on call entry(8 bit)




SRAMWrite      ;SUBRTN
F842: 34 02         PSHS  A                  ;save our byte
F844: A7 01         STA   1,X                ;store LSN
F846: 44            LSRA                     ;divide by 16
F847: 44            LSRA                     ;
F848: 44            LSRA                     ;
F849: 44            LSRA                     ;
F84A: A7 81         STA   ,X++               ;store MSN
F84C: 35 82         PULS  A,PC               ;restore our byte


WrSRAMbyte   ;SUBRTN
F84E: 34 04         PSHS  B                  ;save B reg
F850: D6 36         LDB   <$36               ;load $C000 page #
F852: 34 04         PSHS  B                  ;save it on stack
F854: 0F 36         CLR   <$36               ;
F856: 7F D0 00      CLR   $D000              ;switch to I/O page
F859: 8D E7         BSR   SRAMWrite          ;write byte to 2 nybbles
F85B: 35 04         PULS  B                  ;restore $C000 page # from stack
F85D: D7 36         STB   <$36               ;
F85F: F7 D0 00      STB   $D000              ;restore it
F862: 35 84         PULS  B,PC               ;restore saved B reg and return

SRAMWordWr      ;SUBRTN (16 bit call)
F864: 8D E8         BSR   WrSRAMbyte         ;A reg to 2 nybbles SRAM

SRAMByteWr     ;SUBRTN (8 bit call)
F866: 34 02         PSHS  A                  ;saving MSB(16 bit)/contents of A reg on call entry(8 bit)
F868: 1F 98         TFR   B,A                ;put LSB in A 
F86A: 8D E2         BSR   WrSRAMbyte         ;A reg to 2 nybbles SRAM
F86C: 35 82         PULS  A,PC               ;restore MSB(16 bit)/contents of A reg on call entry(8 bit) and return



;DATA?
;I believe this to be a data area
;This address is loaded into the U reg at $F758
F86E: 20 00         BRA   $F870              ;
F870: 40            NEGA                     ;
F871: 50            NEGB                     ;
F872: 60 70         NEG   -16,S              ;
F874: 30 00         LEAX  0,X                ;
F876: 00 00         NEG   <$00               ;
F878: 07 00         ASR   <$00               ;
F87A: 03 00         COM   <$00               ;
F87C: 02 
F87D: 00 01         NEG   <$01               ;
F87F: 00 13         NEG   <$13               ;
F881: 00 12         NEG   <$12               ;
F883: 00 11         NEG   <$11               ;
F885: 00 E5         NEG   <$E5               ;
F887: 91 00         CMPA  <$00               ;
F889: E8 00         EORB  0,X                ;
F88B: 00 00         NEG   <$00               ;
F88D: 00 E8         NEG   <$E8               ;
F88F: C1 00         CMPB  #$00               ;
F891: F8 E9 1F      EORB  $E91F              ;
F894: 00 F8         NEG   <$F8               ;
F896: D8 4E         EORB  <$4E               ;
F898: 00 00         NEG   <$00               ;
F89A: D8 39         EORB  <$39               ;
F89C: 00 00         NEG   <$00               ;
F89E: E8 
F89F: 97 00         STA   <$00               ;
F8A1: E8 00         EORB  0,X                ;
F8A3: 00 00         NEG   <$00               ;
F8A5: 00 00         NEG   <$00               ;
F8A7: 00 00         NEG   <$00               ;
F8A9: 00 D4         NEG   <$D4               ;
F8AB: 4C            INCA                     ;
F8AC: 00 00         NEG   <$00               ;
F8AE: D4 75         ANDB  <$75               ;
F8B0: 02 
F8B1: 00 D4         NEG   <$D4               ;
F8B3: 3D            MUL                      ;
F8B4: 00 00         NEG   <$00               ;
F8B6: D4 6E         ANDB  <$6E               ;
F8B8: 02 
F8B9: 00 D4         NEG   <$D4               ;
F8BB: 7C 02 00      INC   $0200              ;
F8BE: 00 00         NEG   <$00               ;
F8C0: 07 28         ASR   <$28               ;
F8C2: 2F 81         BLE   $F845              ;
F8C4: A4 15         ANDA  -11,X              ;
F8C6: C7 
F8C7: FF 00 00      STU   $0000              ;
F8CA: 00 00         NEG   <$00               ;
F8CC: 00 00         NEG   <$00               ;
F8CE: 05 
F8CF: 08 F9         LSL   <$F9               ;
F8D1: FB FA 23      ADDB  $FA23              ;
F8D4: D1 93         CMPB  <$93               ;
F8D6: D1 1F         CMPB  <$1F               ;
F8D8: 04 08         LSR   <$08               ;
F8DA: FA 4B FA      ORB   $4BFA              ;
F8DD: 4B 
F8DE: D1 39         CMPB  <$39               ;
F8E0: D1 6B         CMPB  <$6B               ;
F8E2: 04 08         LSR   <$08               ;
F8E4: FA 6B FA      ORB   $6BFA              ;
F8E7: 6B 
F8E8: D1 39         CMPB  <$39               ;
F8EA: D1 6B         CMPB  <$6B               ;

;I believe this to be a data area
F8EC: 01 
F8ED: 01 
F8EE: F8 F6 F8      EORB  $F6F8              ;
F8F1: F6 D8 DB      LDB   $D8DB              ;
F8F4: D8 DB         EORB  <$DB               ;
F8F6: 00 04         NEG   <$04               ;
F8F8: 08 FA         LSL   <$FA               ;
F8FA: 8B FA         ADDA  #$FA               ;
F8FC: AB D1         ADDA  [,U++]             ;
F8FE: 39            RTS                      ;

F8FF: D1 6B         CMPB  <$6B               ;
F901: 02 
F902: 08 FA         LSL   <$FA               ;
F904: CB FA         ADDB  #$FA               ;
F906: DB D0         ADDB  <$D0               ;
F908: F9 D1 0B      ADCB  $D10B              ;
F90B: 02 
F90C: 08 FA         LSL   <$FA               ;
F90E: EB 
F90F: FA FB D0      ORB   $FBD0              ;
F912: F9 D1 0B      ADCB  $D10B              ;
F915: 02 
F916: 08 FB         LSL   <$FB               ;
F918: 0B 
F919: FB 1B D0      ADDB  $1BD0              ;
F91C: F9 D1 0B      ADCB  $D10B              ;
F91F: 02 
F920: 08 FB         LSL   <$FB               ;
F922: 2B FB         BMI   $F91F              ;
F924: 3B            RTI                      ;
F925: D0 F9         SUBB  <$F9               ;
F927: D1 0B         CMPB  <$0B               ;
F929: 04 08         LSR   <$08               ;
F92B: FB 4B FB      ADDB  $4BFB              ;
F92E: 6B 
F92F: D1 39         CMPB  <$39               ;
F931: D1 6B         CMPB  <$6B               ;
F933: 04 08         LSR   <$08               ;
F935: FB 8B FB      ADDB  $8BFB              ;
F938: AB D1         ADDA  [,U++]             ;
F93A: 39            RTS                      ;

F93B: D1 6B         CMPB  <$6B               ;
F93D: 04 08         LSR   <$08               ;
F93F: FB CB FB      ADDB  $CBFB              ;
F942: EB D1         ADDB  [,U++]             ;
F944: 39            RTS                      ;

F945: D1 6B         CMPB  <$6B               ;
F947: 04 08         LSR   <$08               ;
F949: FC 0B FC      LDD   $0BFC              ;
F94C: 2B D1         BMI   $F91F              ;
F94E: 39            RTS                      ;

F94F: D1 6B         CMPB  <$6B               ;
F951: 04 08         LSR   <$08               ;
F953: CC 90 CC      LDD   #$90CC             ;
F956: 90 D1         SUBA  <$D1               ;
F958: 39            RTS                      ;

F959: D1 6B         CMPB  <$6B               ;
F95B: 02 
F95C: 03 CC         COM   <$CC               ;
F95E: B0 CC B6      SUBA  $CCB6              ;
F961: D1 F1         CMPB  <$F1               ;
F963: D2 0D         SBCB  <$0D               ;
F965: 02 
F966: 03 CC         COM   <$CC               ;
F968: BC CC C2      CMPX  $CCC2              ;
F96B: D1 F1         CMPB  <$F1               ;
F96D: D2 0D         SBCB  <$0D               ;
F96F: 08 01         LSL   <$01               ;
F971: F9 73 FF      ADCB  $73FF              ;
F974: FF FF FF      STU   $FFFF              ;
F977: FF FF FF      STU   $FFFF              ;
F97A: FF 03 04      STU   $0304              ;
F97D: CC C8 CC      LDD   #$C8CC             ;
F980: D4 D1         ANDB  <$D1               ;
F982: AD D1         JSR   [,U++]             ;
F984: D7 05         STB   <$05               ;
F986: 08 CC         LSL   <$CC               ;
F988: E0 CD 08 D1   SUBB  $08D1,PC           ;
F98C: 93 D1         SUBD  <$D1               ;
F98E: 1F 05         TFR   D,PC               ;
F990: 08 CD         LSL   <$CD               ;
F992: 30 CD 58 D1   LEAX  $58D1,PC           ;
F996: 93 D1         SUBD  <$D1               ;
F998: 1F 05         TFR   D,PC               ;
F99A: 08 CD         LSL   <$CD               ;
F99C: 80 CD         SUBA  #$CD               ;
F99E: A8 D1         EORA  [,U++]             ;
F9A0: 93 D1         SUBD  <$D1               ;
F9A2: 1F 06         TFR   D,?                ;
F9A4: 04 CD         LSR   <$CD               ;
F9A6: D0 CD         SUBB  <$CD               ;
F9A8: E8 
F9A9: D2 1F         SBCB  <$1F               ;
F9AB: D2 60         SBCB  <$60               ;
F9AD: 06 04         ROR   <$04               ;
F9AF: CE 00 CE      LDU   #$00CE             ;
F9B2: 18 
F9B3: D2 1F         SBCB  <$1F               ;
F9B5: D2 60         SBCB  <$60               ;
F9B7: 06 04         ROR   <$04               ;
F9B9: CE 30 CE      LDU   #$30CE             ;
F9BC: 48            ASLA                     ;
F9BD: D2 1F         SBCB  <$1F               ;
F9BF: D2 60         SBCB  <$60               ;
F9C1: 08 06         LSL   <$06               ;
F9C3: CE 60 CE      LDU   #$60CE             ;
F9C6: 90 D2         SUBA  <$D2               ;
F9C8: 8E D2 DF      LDX   #$D2DF             ;
F9CB: 08 06         LSL   <$06               ;
F9CD: CE C0 CE      LDU   #$C0CE             ;
F9D0: F0 D2 8E      SUBB  $D28E              ;
F9D3: D2 DF         SBCB  <$DF               ;
;data for painting in a reserve ship? ("life")
F9D5: 05 04 CF 20

F9D9: 03 03 CF 34

F9DD: 06 06 CF 3D
F9E1: CF 61 D3 3D   
F9E5: D3 50         ADDD  <$50               ;
F9E7: 06 06         ROR   <$06               ;
F9E9: CF 
F9EA: 85 CF         BITA  #$CF               ;
F9EC: A9 D3         ADCA  [,--U]             ;
F9EE: 3D            MUL                      ;
F9EF: D3 50         ADDD  <$50               ;
F9F1: 08 06         LSL   <$06               ;
F9F3: CF 
F9F4: CD 
F9F5: CF 
F9F6: CD 
F9F7: F5 22 F5      BITB  $22F5              ;
F9FA: 7B 
F9FB: 00 00         NEG   <$00               ;
F9FD: 03 03         COM   <$03               ;
F9FF: 00 00         NEG   <$00               ;
FA01: 03 30         COM   <$30               ;
FA03: 0C 3C         INC   <$3C               ;
FA05: 0C 08         INC   <$08               ;
FA07: 38 
FA08: 30 00         LEAX  0,X                ;
FA0A: 00 C0         NEG   <$C0               ;
FA0C: C0 C8         SUBB  #$C8               ;
FA0E: 78 78 70      ASL   $7870              ;
FA11: 70 70 00      NEG   $7000              ;
FA14: 30 03         LEAX  3,X                ;
FA16: 03 30         COM   <$30               ;
FA18: 30 03         LEAX  3,X                ;
FA1A: 00 00         NEG   <$00               ;
FA1C: 00 00         NEG   <$00               ;
FA1E: 00 00         NEG   <$00               ;
FA20: 00 00         NEG   <$00               ;
FA22: 30 00         LEAX  0,X                ;
FA24: 00 00         NEG   <$00               ;
FA26: 00 00         NEG   <$00               ;
FA28: 00 00         NEG   <$00               ;
FA2A: 30 00         LEAX  0,X                ;
FA2C: 03 30         COM   <$30               ;
FA2E: 30 03         LEAX  3,X                ;
FA30: 03 30         COM   <$30               ;
FA32: 00 CC         NEG   <$CC               ;
FA34: CC CC 87      LDD   #$CC87             ;
FA37: 87 
FA38: 07 07         ASR   <$07               ;
FA3A: 07 00         ASR   <$00               ;
FA3C: 03 80         COM   <$80               ;
FA3E: 80 83         SUBA  #$83               ;
FA40: 03 00         COM   <$00               ;
FA42: 00 00         NEG   <$00               ;
FA44: 00 30         NEG   <$30               ;
FA46: 30 00         LEAX  0,X                ;
FA48: 00 30         NEG   <$30               ;
FA4A: 03 00         COM   <$00               ;
FA4C: 00 0D         NEG   <$0D               ;
FA4E: 6C 6C         INC   12,S               ;
FA50: 0D 00         TST   <$00               ;
FA52: 00 06         NEG   <$06               ;
FA54: E6 C8 83      LDB   $-7D,U             ;
FA57: 82 C8         SBCA  #$C8               ;
FA59: EC 06         LDD   6,X                ;
FA5B: 60 6D         NEG   13,S               ;
FA5D: 8C 28 28      CMPX  #$2828             ;
FA60: 8C 6D 60      CMPX  #$6D60             ;
FA63: 00 00         NEG   <$00               ;
FA65: E0 C6         SUBB  A,U                ;
FA67: C6 E0         LDB   #$E0               ;
FA69: 00 00         NEG   <$00               ;
FA6B: 00 00         NEG   <$00               ;
FA6D: 02 
FA6E: 22 24         BHI   $FA94              ;
FA70: 02 
FA71: 00 00         NEG   <$00               ;
FA73: 02 
FA74: 22 44         BHI   $FABA              ;
FA76: 44            LSRA                     ;
FA77: 24 42         BCC   $FABB              ;
FA79: 22 00         BHI   $FA7B              ;
FA7B: 20 22         BRA   $FA9F              ;
FA7D: 44            LSRA                     ;
FA7E: 44            LSRA                     ;
FA7F: 24 42         BCC   $FAC3              ;
FA81: 22 00         BHI   $FA83              ;
FA83: 00 00         NEG   <$00               ;
FA85: 20 22         BRA   $FAA9              ;
FA87: 22 20         BHI   $FAA9              ;
FA89: 00 00         NEG   <$00               ;
FA8B: 00 0E         NEG   <$0E               ;
FA8D: 00 D8         NEG   <$D8               ;
FA8F: 00 0E         NEG   <$0E               ;
FA91: 00 00         NEG   <$00               ;
FA93: 0F 08         CLR   <$08               ;
FA95: 8C C8 8C      CMPX  #$C88C             ;
FA98: 08 0F         LSL   <$0F               ;
FA9A: 00 00         NEG   <$00               ;
FA9C: 0E 80         JMP   <$80               ;
FA9E: C8 80         EORB  #$80               ;
FAA0: 0E 00         JMP   <$00               ;
FAA2: 00 00         NEG   <$00               ;
FAA4: 00 00         NEG   <$00               ;
FAA6: D0 00         SUBB  <$00               ;
FAA8: 00 00         NEG   <$00               ;
FAAA: 00 00         NEG   <$00               ;
FAAC: 00 00         NEG   <$00               ;
FAAE: 0D 00         TST   <$00               ;
FAB0: 00 00         NEG   <$00               ;
FAB2: 00 00         NEG   <$00               ;
FAB4: E0 08         SUBB  8,X                ;
FAB6: 8C 08 E0      CMPX  #$08E0             ;
FAB9: 00 00         NEG   <$00               ;
FABB: F0 80 C8      SUBB  $80C8              ;
FABE: 8C C8 80      CMPX  #$C880             ;
FAC1: F0 00 00      SUBB  $0000              ;
FAC4: E0 00         SUBB  0,X                ;
FAC6: 8D 00         BSR   $FAC8              ;
FAC8: E0 00         SUBB  0,X                ;
FACA: 00 33         NEG   <$33               ;
FACC: 43            COMA                     ;
FACD: 43            COMA                     ;
FACE: 87 
FACF: 87 
FAD0: 07 07         ASR   <$07               ;
FAD2: 07 00         ASR   <$00               ;
FAD4: 00 80         NEG   <$80               ;
FAD6: 80 80         SUBA  #$80               ;
FAD8: 00 00         NEG   <$00               ;
FADA: 00 03         NEG   <$03               ;
FADC: 04 04         LSR   <$04               ;
FADE: 08 08         LSL   <$08               ;
FAE0: 00 00         NEG   <$00               ;
FAE2: 00 30         NEG   <$30               ;
FAE4: 30 38         LEAX  -8,Y               ;
FAE6: 78 78 70      ASL   $7870              ;
FAE9: 70 70 33      NEG   $7033              ;
FAEC: 43            COMA                     ;
FAED: 43            COMA                     ;
FAEE: 87 
FAEF: 87 
FAF0: 77 77 77      ASR   $7777              ;
FAF3: 00 00         NEG   <$00               ;
FAF5: 80 80         SUBA  #$80               ;
FAF7: 80 00         SUBA  #$00               ;
FAF9: 00 00         NEG   <$00               ;
FAFB: 03 04         COM   <$04               ;
FAFD: 04 08         LSR   <$08               ;
FAFF: 08 07         LSL   <$07               ;
FB01: 07 07         ASR   <$07               ;
FB03: 30 30         LEAX  -16,Y              ;
FB05: 38 
FB06: 78 78 70      ASL   $7870              ;
FB09: 70 70 03      NEG   $7003              ;
FB0C: 03 83         COM   <$83               ;
FB0E: 87 
FB0F: 87 
FB10: 07 07         ASR   <$07               ;
FB12: 07 30         ASR   <$30               ;
FB14: 40            NEGA                     ;
FB15: 40            NEGA                     ;
FB16: 80 80         SUBA  #$80               ;
FB18: 00 00         NEG   <$00               ;
FB1A: 00 00         NEG   <$00               ;
FB1C: 00 08         NEG   <$08               ;
FB1E: 08 08         LSL   <$08               ;
FB20: 00 00         NEG   <$00               ;
FB22: 00 33         NEG   <$33               ;
FB24: 34 34         PSHS  Y,X,B              ;
FB26: 78 78 70      ASL   $7870              ;
FB29: 70 70 03      NEG   $7003              ;
FB2C: 03 83         COM   <$83               ;
FB2E: 87 
FB2F: 87 
FB30: 07 07         ASR   <$07               ;
FB32: 07 30         ASR   <$30               ;
FB34: 40            NEGA                     ;
FB35: 40            NEGA                     ;
FB36: 80 80         SUBA  #$80               ;
FB38: 70 70 70      NEG   $7070              ;
FB3B: 00 00         NEG   <$00               ;
FB3D: 08 08         LSL   <$08               ;
FB3F: 08 00         LSL   <$00               ;
FB41: 00 00         NEG   <$00               ;
FB43: 33 34         LEAU  -12,Y              ;
FB45: 34 78         PSHS  U,Y,X,DP           ;
FB47: 78 77 77      ASL   $7777              ;
FB4A: 77 08 08      ASR   $0808              ;
FB4D: DD DE         STD   <$DE               ;
FB4F: DE DE         LDU   <$DE               ;
FB51: DD 00         STD   <$00               ;
FB53: 88 88         EORA  #$88               ;
FB55: DD EE         STD   <$EE               ;
FB57: FE EE DD      LDU   $EEDD              ;
FB5A: 00 88         NEG   <$88               ;
FB5C: 88 D8         EORA  #$D8               ;
FB5E: D8 D8         EORB  <$D8               ;
FB60: D0 D0         SUBB  <$D0               ;
FB62: 00 00         NEG   <$00               ;
FB64: 00 00         NEG   <$00               ;
FB66: 00 00         NEG   <$00               ;
FB68: 00 00         NEG   <$00               ;
FB6A: 00 00         NEG   <$00               ;
FB6C: 00 0D         NEG   <$0D               ;
FB6E: 0D 0D         TST   <$0D               ;
FB70: 0D 0D         TST   <$0D               ;
FB72: 00 88         NEG   <$88               ;
FB74: 88 DD         EORA  #$DD               ;
FB76: EE 
FB77: EF 
FB78: EE DD 00 88   LDU   [$0088,PC]         ;
FB7C: 88 DD         EORA  #$DD               ;
FB7E: ED ED ED DD   STD   $-1223,PC          ;
FB82: 00 80         NEG   <$80               ;
FB84: 80 80         SUBA  #$80               ;
FB86: 80 80         SUBA  #$80               ;
FB88: 00 00         NEG   <$00               ;
FB8A: 00 00         NEG   <$00               ;
FB8C: 08 DD         LSL   <$DD               ;
FB8E: DE DE         LDU   <$DE               ;
FB90: DE DD         LDU   <$DD               ;
FB92: 00 00         NEG   <$00               ;
FB94: 88 DD         EORA  #$DD               ;
FB96: EE 
FB97: FE EE DD      LDU   $EEDD              ;
FB9A: 00 00         NEG   <$00               ;
FB9C: 88 D8         EORA  #$D8               ;
FB9E: D8 D8         EORB  <$D8               ;
FBA0: D8 D0         EORB  <$D0               ;
FBA2: 00 00         NEG   <$00               ;
FBA4: 00 00         NEG   <$00               ;
FBA6: 00 00         NEG   <$00               ;
FBA8: 00 00         NEG   <$00               ;
FBAA: 00 00         NEG   <$00               ;
FBAC: 00 0D         NEG   <$0D               ;
FBAE: 0D 0D         TST   <$0D               ;
FBB0: 0D 0D         TST   <$0D               ;
FBB2: 00 00         NEG   <$00               ;
FBB4: 88 DD         EORA  #$DD               ;
FBB6: EE 
FBB7: EF 
FBB8: EE DD 00 00   LDU   [$0000,PC]         ;
FBBC: 88 DD         EORA  #$DD               ;
FBBE: ED ED ED DD   STD   $-1223,PC          ;
FBC2: 00 00         NEG   <$00               ;
FBC4: 80 80         SUBA  #$80               ;
FBC6: 80 80         SUBA  #$80               ;
FBC8: 80 00         SUBA  #$00               ;
FBCA: 00 00         NEG   <$00               ;
FBCC: 00 DD         NEG   <$DD               ;
FBCE: DE DE         LDU   <$DE               ;
FBD0: DE DD         LDU   <$DD               ;
FBD2: 00 00         NEG   <$00               ;
FBD4: 00 DD         NEG   <$DD               ;
FBD6: EE 
FBD7: FE EE DD      LDU   $EEDD              ;
FBDA: 00 00         NEG   <$00               ;
FBDC: 00 D8         NEG   <$D8               ;
FBDE: D8 D8         EORB  <$D8               ;
FBE0: D8 D8         EORB  <$D8               ;
FBE2: 00 00         NEG   <$00               ;
FBE4: 00 00         NEG   <$00               ;
FBE6: 00 00         NEG   <$00               ;
FBE8: 00 00         NEG   <$00               ;
FBEA: 00 00         NEG   <$00               ;
FBEC: 00 0D         NEG   <$0D               ;
FBEE: 0D 0D         TST   <$0D               ;
FBF0: 0D 0D         TST   <$0D               ;
FBF2: 00 00         NEG   <$00               ;
FBF4: 00 DD         NEG   <$DD               ;
FBF6: EE 
FBF7: EF 
FBF8: EE DD 00 00   LDU   [$0000,PC]         ;
FBFC: 00 DD         NEG   <$DD               ;
FBFE: ED ED ED DD   STD   $-1223,PC          ;
FC02: 00 00         NEG   <$00               ;
FC04: 00 80         NEG   <$80               ;
FC06: 80 80         SUBA  #$80               ;
FC08: 80 80         SUBA  #$80               ;
FC0A: 00 00         NEG   <$00               ;
FC0C: 00 DD         NEG   <$DD               ;
FC0E: DE DE         LDU   <$DE               ;
FC10: DE DD         LDU   <$DD               ;
FC12: 00 00         NEG   <$00               ;
FC14: 00 DD         NEG   <$DD               ;
FC16: EE 
FC17: FE EE DD      LDU   $EEDD              ;
FC1A: 88 00         EORA  #$00               ;
FC1C: 00 D0         NEG   <$D0               ;
FC1E: D8 D8         EORB  <$D8               ;
FC20: D8 D8         EORB  <$D8               ;
FC22: 88 00         EORA  #$00               ;
FC24: 00 00         NEG   <$00               ;
FC26: 00 00         NEG   <$00               ;
FC28: 00 00         NEG   <$00               ;
FC2A: 00 00         NEG   <$00               ;
FC2C: 00 0D         NEG   <$0D               ;
FC2E: 0D 0D         TST   <$0D               ;
FC30: 0D 0D         TST   <$0D               ;
FC32: 00 00         NEG   <$00               ;
FC34: 00 DD         NEG   <$DD               ;
FC36: EE 
FC37: EF 
FC38: EE DD 88 00   LDU   [$-7800,PC]        ;
FC3C: 00 DD         NEG   <$DD               ;
FC3E: ED ED ED DD   STD   $-1223,PC          ;
FC42: 88 00         EORA  #$00               ;
FC44: 00 00         NEG   <$00               ;
FC46: 80 80         SUBA  #$80               ;
FC48: 80 80         SUBA  #$80               ;
FC4A: 80 00         SUBA  #$00               ;
FC4C: 00 00         NEG   <$00               ;
FC4E: 00 00         NEG   <$00               ;
FC50: 00 00         NEG   <$00               ;
FC52: 00 00         NEG   <$00               ;
FC54: 00 00         NEG   <$00               ;
FC56: 00 00         NEG   <$00               ;
FC58: 00 00         NEG   <$00               ;
FC5A: 00 00         NEG   <$00               ;
FC5C: 00 00         NEG   <$00               ;
FC5E: 00 00         NEG   <$00               ;

I fail to see the logic of jumping/calling to a subroutine that has only a single JMP opcode in it. There are three of them in a row right here.

;SUBRTN
FC60: 7E FC 69      JMP   $FC69              ;all JMP/JSR opcodes to this location could be changed to go to $FC69 for faster execution


;SUBRTN
FC63: 7E FC CC      JMP   $FCCC              ;all JMP/JSR opcodes to this location could be changed to go to $FCCC for faster execution


;SUBRTN
FC66: 7E FD 2D      JMP   $FD2D              ;all JMP/JSR opcodes to this location could be changed to go to $FD2D for faster execution



;SUBRTN
FC69: 34 66         PSHS  U,Y,B,A            ;
FC6B: EC 02         LDD   2,X                ;
FC6D: 34 06         PSHS  B,A                ;save D reg
FC6F: FC FF 9D      LDD   $FF9D              ;
FC72: ED 02         STD   2,X                ;
FC74: 9F 65         STX   <$65               ;
FC76: EC 0A         LDD   10,X               ;
FC78: 93 20         SUBD  <$20               ;
FC7A: 10 83 26 00   CMPD  #$2600             ;
FC7E: 22 17         BHI   $FC97              ;
FC80: 10 9E E2      LDY   <$E2               ;
FC83: 27 09         BEQ   $FC8E              ;
FC85: 31 A8 40      LEAY  $40,Y              ;
FC88: 10 8C A0 00   CMPY  #$A000             ;
FC8C: 26 04         BNE   $FC92              ;
FC8E: 10 8E 9C 00   LDY   #$9C00             ;
FC92: 10 9C E2      CMPY  <$E2               ;
FC95: 26 06         BNE   $FC9D              ;
;equal, not much more to do
FC97: 35 06         PULS  A,B                ;restore D reg before we exit
FC99: ED 02         STD   2,X                ;
FC9B: 20 2D         BRA   $FCCA              ;
;not equal, means we have a bit more to do
FC9D: A6 A4         LDA   ,Y                 ;
FC9F: 2B E4         BMI   $FC85              ;loop if negative
FCA1: 27 03         BEQ   $FCA6              ;is it 0?
FCA3: BD FD D5      JSR   $FDD5              ;positive number
FCA6: 96 BA         LDA   <$BA               ;
FCA8: 85 80         BITA  #$80               ;
FCAA: 26 06         BNE   $FCB2              ;
FCAC: FC FF DD      LDD   $FFDD              ;
FCAF: BD FF DA      JSR   $FFDA              ;"JSR  $D54D" would have been faster
FCB2: A6 88 14      LDA   $14,X              ;
FCB5: 8A 02         ORA   #$02               ;
FCB7: A7 88 14      STA   $14,X              ;
FCBA: CC AF 00      LDD   #$AF00             ;
FCBD: ED A4         STD   ,Y                 ;
FCBF: 35 06         PULS  A,B                ;restore
FCC1: ED 22         STD   2,Y                ;
FCC3: 33 A8 40      LEAU  $40,Y              ;
FCC6: EF 24         STU   4,Y                ;
FCC8: AF 2A         STX   10,Y               ;
FCCA: 35 E6         PULS  A,B,Y,U,PC         ;



;SUBRTN
FCCC: 34 66         PSHS  U,Y,B,A            ;
FCCE: EC 0A         LDD   10,X               ;
FCD0: 93 20         SUBD  <$20               ;
FCD2: 81 26         CMPA  #$26               ;
FCD4: 22 55         BHI   $FD2B              ;
FCD6: DD E9         STD   <$E9               ;
FCD8: 10 9E E2      LDY   <$E2               ;
FCDB: 27 09         BEQ   $FCE6              ;
FCDD: 31 A8 40      LEAY  $40,Y              ;
FCE0: 10 8C A0 00   CMPY  #$A000             ;
FCE4: 26 04         BNE   $FCEA              ;
FCE6: 10 8E 9C 00   LDY   #$9C00             ;
FCEA: 10 9C E2      CMPY  <$E2               ;
FCED: 27 3C         BEQ   $FD2B              ;
FCEF: A6 A4         LDA   ,Y                 ;
FCF1: 2B EA         BMI   $FCDD              ;loop
FCF3: 27 03         BEQ   $FCF8              ;
FCF5: BD FD D5      JSR   $FDD5              ;
FCF8: 10 9F E2      STY   <$E2               ;
FCFB: CC 01 00      LDD   #$0100             ;
FCFE: ED A4         STD   ,Y                 ;
FD00: EC 02         LDD   2,X                ;
FD02: ED 22         STD   2,Y                ;
FD04: 33 A8 40      LEAU  $40,Y              ;
FD07: EF 24         STU   4,Y                ;
FD09: DC E9         LDD   <$E9               ;
FD0B: 58            ASLB                     ;
FD0C: 49            ROLA                     ;
FD0D: 58            ASLB                     ;
FD0E: 49            ROLA                     ;
FD0F: E6 0C         LDB   12,X               ;
FD11: ED 28         STD   8,Y                ;
FD13: 93 F8         SUBD  <$F8               ;
FD15: EE 22         LDU   2,Y                ;
FD17: AB C4         ADDA  ,U                 ;
FD19: 24 08         BCC   $FD23              ;
FD1B: EB 41         ADDB  1,U                ;
FD1D: 24 04         BCC   $FD23              ;
FD1F: DC F8         LDD   <$F8               ;
FD21: 20 06         BRA   $FD29              ;
FD23: EC C4         LDD   ,U                 ;
FD25: 44            LSRA                     ;
FD26: 54            LSRB                     ;
FD27: E3 28         ADDD  8,Y                ;
FD29: ED 26         STD   6,Y                ;
FD2B: 35 E6         PULS  A,B,Y,U,PC         ;



;SUBRTN
FD2D: 10 8E 9C 00   LDY   #$9C00             ;
FD31: 96 BA         LDA   <$BA               ;
FD33: 85 04         BITA  #$04               ;
FD35: 27 0C         BEQ   $FD43              ;
FD37: A6 A4         LDA   ,Y                 ;
FD39: 2B 56         BMI   $FD91              ;
FD3B: CC 00 00      LDD   #$0000             ;
FD3E: ED A4         STD   ,Y                 ;
FD40: 7E FD C9      JMP   $FDC9              ;
FD43: EC A4         LDD   ,Y                 ;
FD45: 10 27 00 80   LBEQ  $FDC9              ;
FD49: 2B 33         BMI   $FD7E              ;
FD4B: C3 00 AA      ADDD  #$00AA             ;
FD4E: ED A4         STD   ,Y                 ;
FD50: 81 30         CMPA  #$30               ;
FD52: 23 0A         BLS   $FD5E              ;
FD54: BD FD D5      JSR   $FDD5              ;
FD57: CC 00 00      LDD   #$0000             ;
FD5A: ED A4         STD   ,Y                 ;
FD5C: 20 6B         BRA   $FDC9              ;
FD5E: DC 20         LDD   <$20               ;
FD60: C4 C0         ANDB  #$C0               ;
FD62: 34 06         PSHS  B,A                ;
FD64: DC 22         LDD   <$22               ;
FD66: C4 C0         ANDB  #$C0               ;
FD68: A3 E1         SUBD  ,S++               ;
FD6A: 58            ASLB                     ;
FD6B: 49            ROLA                     ;
FD6C: 58            ASLB                     ;
FD6D: 49            ROLA                     ;
FD6E: 34 02         PSHS  A                  ;
FD70: A6 26         LDA   6,Y                ;
FD72: AB E4         ADDA  ,S                 ;
FD74: A7 26         STA   6,Y                ;
FD76: A6 28         LDA   8,Y                ;
FD78: AB E0         ADDA  ,S+                ;
FD7A: A7 28         STA   8,Y                ;
FD7C: 20 45         BRA   $FDC3              ;
FD7E: 83 01 00      SUBD  #$0100             ;
FD81: ED A4         STD   ,Y                 ;
FD83: 2A 0C         BPL   $FD91              ;
FD85: AE 2A         LDX   10,Y               ;
FD87: EC 0A         LDD   10,X               ;
FD89: 93 20         SUBD  <$20               ;
FD8B: 8B 0C         ADDA  #$0C               ;
FD8D: 85 C0         BITA  #$C0               ;
FD8F: 27 18         BEQ   $FDA9              ;
FD91: CC 00 00      LDD   #$0000             ;
FD94: ED A4         STD   ,Y                 ;
FD96: EC 22         LDD   2,Y                ;
FD98: AE 2A         LDX   10,Y               ;
FD9A: ED 02         STD   2,X                ;
FD9C: A6 88 14      LDA   $14,X              ;
FD9F: 84 FD         ANDA  #$FD               ;
FDA1: A7 88 14      STA   $14,X              ;
FDA4: BD FD D5      JSR   $FDD5              ;
FDA7: 20 20         BRA   $FDC9              ;
FDA9: 80 0C         SUBA  #$0C               ;
FDAB: 58            ASLB                     ;
FDAC: 49            ROLA                     ;
FDAD: 58            ASLB                     ;
FDAE: 49            ROLA                     ;
FDAF: E6 0C         LDB   12,X               ;
FDB1: ED 28         STD   8,Y                ;
FDB3: C6 DA         LDB   #$DA               ;
FDB5: 3D            MUL                      ;
FDB6: 48            ASLA                     ;
FDB7: EE 22         LDU   2,Y                ;
FDB9: E6 C4         LDB   ,U                 ;
FDBB: 3D            MUL                      ;
FDBC: E6 41         LDB   1,U                ;
FDBE: 54            LSRB                     ;
FDBF: E3 28         ADDD  8,Y                ;
FDC1: ED 26         STD   6,Y                ;
FDC3: BD FD D5      JSR   $FDD5              ;
FDC6: BD FD EF      JSR   $FDEF              ;
FDC9: 31 A8 40      LEAY  $40,Y              ;
FDCC: 10 8C A0 00   CMPY  #$A000             ;
FDD0: 10 26 FF 5D   LBNE  $FD31              ;
FDD4: 39            RTS                      ;



;SUBRTN
FDD5: 34 16         PSHS  X,B,A              ;
FDD7: CC 00 00      LDD   #$0000             ;
FDDA: 30 A8 40      LEAX  $40,Y              ;
FDDD: 9F F3         STX   <$F3               ;
FDDF: AE 24         LDX   4,Y                ;
FDE1: 9C F3         CMPX  <$F3               ;
FDE3: 27 08         BEQ   $FDED              ;
FDE5: ED 91         STD   [,X++]             ;
FDE7: 9C F3         CMPX  <$F3               ;
FDE9: 26 FA         BNE   $FDE5              ;
FDEB: AF 24         STX   4,Y                ;
FDED: 35 96         PULS  A,B,X,PC           ;


 
FDEF: 34 76         PSHS  U,Y,X,B,A          ;
FDF1: 10 9F F6      STY   <$F6               ;
FDF4: A6 A4         LDA   ,Y                 ;
FDF6: 84 7F         ANDA  #$7F               ;
FDF8: 97 E7         STA   <$E7               ;
FDFA: 33 A8 40      LEAU  $40,Y              ;
FDFD: 0F E6         CLR   <$E6               ;
FDFF: AE 22         LDX   2,Y                ;
FE01: EC 02         LDD   2,X                ;
FE03: DD F3         STD   <$F3               ;
FE05: EC 84         LDD   ,X                 ;
FE07: 97 F1         STA   <$F1               ;
FE09: D7 F2         STB   <$F2               ;
FE0B: C5 01         BITB  #$01               ;
FE0D: 26 05         BNE   $FE14              ;
FE0F: 8E FF 27      LDX   #$FF27             ;load a jump location
FE12: 20 03         BRA   $FE17              ;
FE14: 8E FE F3      LDX   #$FEF3             ;load a jump location
FE17: 9F ED         STX   <$ED               ;store jump location
FE19: EC 26         LDD   6,Y                ;
FE1B: A3 28         SUBD  8,Y                ;
FE1D: 97 E4         STA   <$E4               ;
FE1F: 54            LSRB                     ;
FE20: D7 E5         STB   <$E5               ;
FE22: 09 E6         ROL   <$E6               ;
FE24: 96 E7         LDA   <$E7               ;
FE26: D6 E4         LDB   <$E4               ;
FE28: 3D            MUL                      ;
FE29: DD E9         STD   <$E9               ;
FE2B: E6 26         LDB   6,Y                ;
FE2D: 4F            CLRA                     ;
FE2E: 93 E9         SUBD  <$E9               ;
FE30: DD E9         STD   <$E9               ;
FE32: 4D            TSTA                     ;
FE33: 27 18         BEQ   $FE4D              ;
FE35: DC F3         LDD   <$F3               ;
FE37: DB F2         ADDB  <$F2               ;
FE39: 89 00         ADCA  #$00               ;
FE3B: DD F3         STD   <$F3               ;
FE3D: 0A F1         DEC   <$F1               ;
FE3F: 10 27 00 F2   LBEQ  $FF35              ;
FE43: DC E9         LDD   <$E9               ;
FE45: DB E7         ADDB  <$E7               ;
FE47: 89 00         ADCA  #$00               ;
FE49: DD E9         STD   <$E9               ;
FE4B: 20 E5         BRA   $FE32              ;
FE4D: C1 98         CMPB  #$98               ;
FE4F: 10 22 00 E2   LBHI  $FF35              ;
FE53: 96 E7         LDA   <$E7               ;
FE55: 48            ASLA                     ;
FE56: 97 E8         STA   <$E8               ;
FE58: D6 E5         LDB   <$E5               ;
FE5A: 3D            MUL                      ;
FE5B: DD EB         STD   <$EB               ;
FE5D: E6 27         LDB   7,Y                ;
FE5F: 4F            CLRA                     ;
FE60: 93 EB         SUBD  <$EB               ;
FE62: D0 E6         SUBB  <$E6               ;
FE64: 89 00         ADCA  #$00               ;
FE66: 0F F5         CLR   <$F5               ;
FE68: 4D            TSTA                     ;
FE69: 26 04         BNE   $FE6F              ;
FE6B: C1 2A         CMPB  #$2A               ;
FE6D: 24 10         BCC   $FE7F              ;
FE6F: 0C F5         INC   <$F5               ;
FE71: 0A F2         DEC   <$F2               ;
FE73: 0A F2         DEC   <$F2               ;
FE75: 10 2F 00 BC   LBLE  $FF35              ;
FE79: DB E8         ADDB  <$E8               ;
FE7B: 89 00         ADCA  #$00               ;
FE7D: 20 E9         BRA   $FE68              ;
FE7F: DD EB         STD   <$EB               ;
FE81: 96 F2         LDA   <$F2               ;load offset for the vector table
FE83: 84 FE         ANDA  #$FE               ;eliminate LSbit, but not the 4 MSbits? Must have been taken care of prior to storing it?
FE85: 8E FF 48      LDX   #$FF48             ;load start address for vector table
FE88: AE 86         LDX   A,X                ;calc EA in vector table
FE8A: 9F EF         STX   <$EF               ;store this in the DP, presumably at $A0EF
FE8C: 9E F3         LDX   <$F3               ;
FE8E: 08 F5         LSL   <$F5               ;
FE90: 96 EA         LDA   <$EA               ;
FE92: D6 F5         LDB   <$F5               ;
FE94: 3A            ABX                      ;
FE95: D6 EC         LDB   <$EC               ;
FE97: 6E 9F A0 EF   JMP   [$A0EF]            ;jump to vector address
;8/8 in $FF48 vector table
FE9B: ED C3         STD   ,--U               ;
FE9D: 10 AE 81      LDY   ,X++               ;
FEA0: 10 AF D4      STY   [,U]               ;
FEA3: DB E8         ADDB  <$E8               ;
FEA5: 25 56         BCS   $FEFD              ;
;7/8 in $FF48 vector table
FEA7: ED C3         STD   ,--U               ;
FEA9: 10 AE 81      LDY   ,X++               ;
FEAC: 10 AF D4      STY   [,U]               ;
FEAF: DB E8         ADDB  <$E8               ;
FEB1: 25 50         BCS   $FF03              ;
;6/8 in $FF48 vector table
FEB3: ED C3         STD   ,--U               ;
FEB5: 10 AE 81      LDY   ,X++               ;
FEB8: 10 AF D4      STY   [,U]               ;
FEBB: DB E8         ADDB  <$E8               ;
FEBD: 25 4A         BCS   $FF09              ;
;5/8 in $FF48 vector table
FEBF: ED C3         STD   ,--U               ;
FEC1: 10 AE 81      LDY   ,X++               ;
FEC4: 10 AF D4      STY   [,U]               ;
FEC7: DB E8         ADDB  <$E8               ;
FEC9: 25 44         BCS   $FF0F              ;
;4/8 in $FF48 vector table
FECB: ED C3         STD   ,--U               ;
FECD: 10 AE 81      LDY   ,X++               ;
FED0: 10 AF D4      STY   [,U]               ;
FED3: DB E8         ADDB  <$E8               ;
FED5: 25 3E         BCS   $FF15              ;
;3/8 in $FF48 vector table
FED7: ED C3         STD   ,--U               ;
FED9: 10 AE 81      LDY   ,X++               ;
FEDC: 10 AF D4      STY   [,U]               ;
FEDF: DB E8         ADDB  <$E8               ;
FEE1: 25 38         BCS   $FF1B              ;
;2/8 in $FF48 vector table
FEE3: ED C3         STD   ,--U               ;
FEE5: 10 AE 81      LDY   ,X++               ;
FEE8: 10 AF D4      STY   [,U]               ;
FEEB: DB E8         ADDB  <$E8               ;
FEED: 25 32         BCS   $FF21              ;
;1/8 in $FF48 vector table
FEEF: 6E 9F A0 ED   JMP   [$A0ED]            ;
FEF3: 25 30         BCS   $FF25              ;
FEF5: ED C3         STD   ,--U               ;
FEF7: E6 80         LDB   ,X+                ;
FEF9: E7 D4         STB   [,U]               ;
FEFB: 20 2A         BRA   $FF27              ;
FEFD: 30 0C         LEAX  12,X               ;
FEFF: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF03: 30 0A         LEAX  10,X               ;
FF05: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF09: 30 08         LEAX  8,X                ;
FF0B: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF0F: 30 06         LEAX  6,X                ;
FF11: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF15: 30 04         LEAX  4,X                ;
FF17: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF1B: 30 02         LEAX  2,X                ;
FF1D: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF21: 6E 9F A0 ED   JMP   [$A0ED]            ;
FF25: 30 01         LEAX  1,X                ;
FF27: 0A F1         DEC   <$F1               ;
FF29: 27 0A         BEQ   $FF35              ;
FF2B: 9B E7         ADDA  <$E7               ;
FF2D: 25 06         BCS   $FF35              ;
FF2F: 81 98         CMPA  #$98               ;
FF31: 10 23 FF 5D   LBLS  $FE92              ;
FF35: 9E F6         LDX   <$F6               ;
FF37: EF 04         STU   4,X                ;
FF39: EC 06         LDD   6,X                ;
FF3B: 81 98         CMPA  #$98               ;
FF3D: 22 07         BHI   $FF46              ;
FF3F: D0 E6         SUBB  <$E6               ;
FF41: 8E 00 00      LDX   #$0000             ;
FF44: AF 8B         STX   D,X                ;
FF46: 35 F6         PULS  A,B,X,Y,U,PC       ;

Vector table with 8 entries

FF48: FE EF                                  ;   $FEEF
FF4A: FE E3                                  ;   $FEE3
FF4C: FE D7                                  ;   $FED7
FF4E: FE CB                                  ;   $FECB
FF50: FE BF                                  ;   $FEBF
FF52: FE B3                                  ;   $FEB3
FF54: FE A7                                  ;   $FEA7
FF56: FE 9B                                  ;   $FE9B

FF58: 00 
FF59: 00 00         NEG   <$00               ;
FF5B: 00 00         NEG   <$00               ;
FF5D: 00 00         NEG   <$00               ;
FF5F: 00 00         NEG   <$00               ;
FF61: 00 00         NEG   <$00               ;
FF63: 00 00         NEG   <$00               ;
FF65: 00 00         NEG   <$00               ;
FF67: 00 00         NEG   <$00               ;
FF69: 00 00         NEG   <$00               ;
FF6B: 00 00         NEG   <$00               ;
FF6D: 00 00         NEG   <$00               ;
FF6F: 00 00         NEG   <$00               ;
FF71: 00 00         NEG   <$00               ;
FF73: 00 00         NEG   <$00               ;
FF75: 00 00         NEG   <$00               ;
FF77: 00 00         NEG   <$00               ;
FF79: 00 00         NEG   <$00               ;
FF7B: 00 00         NEG   <$00               ;
FF7D: 00 00         NEG   <$00               ;
FF7F: 00 00         NEG   <$00               ;
FF81: 00 00         NEG   <$00               ;
FF83: 00 00         NEG   <$00               ;
FF85: 00 00         NEG   <$00               ;
FF87: 00 00         NEG   <$00               ;
FF89: 00 00         NEG   <$00               ;
FF8B: 00 00         NEG   <$00               ;
FF8D: 00 00         NEG   <$00               ;
FF8F: 00 00         NEG   <$00               ;
FF91: 00 00         NEG   <$00               ;
FF93: 00 00         NEG   <$00               ;
FF95: 00 00         NEG   <$00               ;
FF97: 00 00         NEG   <$00               ;
FF99: 00 00         NEG   <$00               ;
FF9B: 00 00         NEG   <$00               ;



;very small vector table?
FF9D: F8 EC                                  ;   $F8EC         ;address $FF9D? opcode at $FC6F uses this exact number
;$F8EC is used in opcodes at $EAB8, and $F045
FF9F: F8 6E                                  ;   $F86E         ;address? opcodes at $C150, $C18C, and $C1AF, page 3 use this exact number ($FF9F). 
;$F86E is used in opcode at $F758

;jump table
RdSRAMbyteX      ;SUBRTN
FFA1: 7E F8 22      JMP   RdSRAMbyte         ;
SRAMByteRdX      ;SUBRTN
FFA4: 7E F8 3A      JMP   SRAMByteRd         ;
SRAMWordRdX      ;SUBRTN
FFA7: 7E F8 38      JMP   SRAMWordRd         ;
WrSRAMbyteX      ;SUBRTN
FFAA: 7E F8 4E      JMP   WrSRAMbyte         ;
SRAMByteWrX      ;SUBRTN
FFAD: 7E F8 66      JMP   SRAMByteWr         ;
SRAMWordWrX      ;SUBRTN
FFB0: 7E F8 64      JMP   SRAMWordWr         ;
DrawCharX      ;SUBRTN
FFB3: 7E F5 22      JMP   DrawChar           ;
ScrnBlkClrP2X      ;SUBRTN
FFB6: 7E F5 7B      JMP   ScrnBlkClrP2         ;
ScrnBlkClrX      ;SUBRTN
FFB9: 7E F5 C7      JMP   ScrnBlkClr         ;
VidMemClrX      ;SUBRTN
FFBC: 7E F5 D1      JMP   VidMemClr          ;
;SUBRTN
FFBF: 7E F7 58      JMP   $F758              ;
;SUBRTN
FFC2: 7E F7 93      JMP   $F793              ;
RAMTestX      ;
FFC5: 7E F6 62      JMP   RAMTest            ;
;
FFC8: 7E F7 D5      JMP   $F7D5              ;
;
FFCB: 7E F4 FA      JMP   $F4FA              ;
CallOtherPageX      ;SUBRTN
FFCE: 7E F4 D3      JMP   CallOtherPage         ;
InsEventLnkPgSavX      ;
FFD1: 7E F4 BE      JMP   InsEventLnkPgSav         ;
WriteIOPortX      ;SUBRTN
FFD4: 7E F7 DB      JMP   WriteIOPort         ;
ReadIOPortX      ;SUBRTN
FFD7: 7E F7 F1      JMP   ReadIOPort         ;
;SUBRTN
FFDA: 7E D5 4D      JMP   $D54D              ;

FFDD:    D4 EE 2A 
FFE0: 00 00 00 00 
FFE4: 00 00 00 00 
FFE8: 00 00 00 00 
FFEC: 00 00 00 00 

; Vectors
FFF0: F6 1F                                  ; take care of the Motorola reserved vector, too.
FFF2: F6 1F                                  ; SWI3 (RESET)
FFF4: F6 1F                                  ; SWI2 (RESET)
FFF6: F6 1F                                  ; FIRQ (RESET)
FFF8: A0 8F                                  ; IRQ
FFFA: F6 1F                                  ; SWI (RESET)
FFFC: F6 1F                                  ; NMI (RESET)
FFFE: F6 1F                                  ; RESET
```
