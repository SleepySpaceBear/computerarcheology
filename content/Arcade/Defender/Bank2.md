![Defender Bank 2](Defender.jpg)

>>> cpu 6809

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](Hardware.md)

# Bank2 

(write 2 to $D000)

```code
;One possible vector and a jump table
C000: C5 FB         BITB  #$FB               ;points to "0" ASCII in table
C002: 7E CA A7      JMP   $CAA7              ;
C005: 7E CA B2      JMP   $CAB2              ;
C008: 7E CA BD      JMP   $CABD              ;
C00B: 7E CA C8      JMP   $CAC8              ;
C00E: 7E CB C1      JMP   $CBC1              ;
C011: 7E CB CC      JMP   $CBCC              ;
C014: 7E CB D7      JMP   $CBD7              ;
C017: 7E CB E2      JMP   $CBE2              ;
C01A: 7E CA 79      JMP   $CA79              ;
C01D: 7E CA 81      JMP   $CA81              ;
C020: 7E CA 51      JMP   $CA51              ;
C023: 7E CA 58      JMP   $CA58              ;

Data area

C026: 00 00                                  ;
C028: 00 00                                  ;
C02A: 00 00                                  ;
C02C: 00 00                                  ;
C02E: 00 5B                                  ;
C030: FF
C031: C0 BD                                  ;
C033: C0 BF                                  ;
C035: C0 C1                                  ;
C037: 00 00                                  ;
C039: C0 C1                                  ;
C03B: 00 00                                  ;
C03D: C0 C3                                  ;
C03F: 00 00                                  ;
C041: C0 C5                                  ;
C043: 00 00                                  ;
C045: C0 C5                                  ;
C047: 00 00                                  ;
C049: C0 C7                                  ;
C04B: 00 00                                  ;
C04D: C0 C3                                  ;
C04F: 00 00                                  ;
C051: C0 C9                                  ;
C053: 00 00                                  ;
C055: C0 CB                                  ;
C057: C0 CD                                  ;
C059: C0 CF                                  ;
C05B: 00 00                                  ;
C05D: C0 BD                                  ;
C05F: C0 D1                                  ;
C061: C0 D3                                  ;
C063: C0 D5                                  ;
C065: C0 DB                                  ;
C067: 00 00                                  ;
C069: C1 07                                  ;
C06B: C1 0D                                  ;
C06D: C1 11                                  ;
C06F: C1 13                                  ;
C071: C1 15                                  ;
C073: C1 19                                  ;
C075: C1 1D                                  ;
C077: C1 21                                  ;
C079: C1 27                                  ;
C07B: C1 2B                                  ;
C07D: C1 33                                  ;
C07F: C1 4D                                  ;
C081: C1 53                                  ;
C083: C1 6D                                  ;
C085: C1 88                                  ;
C087: C1 92                                  ;
C089: C1 96                                  ;
C08B: C1 9C                                  ;
C08D: C1 A0                                  ;
C08F: C1 A2                                  ;
C091: C1 A6                                  ;
C093: C1 A8                                  ;
C095: C1 AC                                  ;
C097: C1 B0                                  ;
C099: C1 B2                                  ;
C09B: C1 B4                                  ;
C09D: C1 B6                                  ;
C09F: C1 B8                                  ;
C0A1: C1 BC                                  ;
C0A3: C1 BE                                  ;
C0A5: C1 C2                                  ;
C0A7: C1 C6                                  ;
C0A9: C1 C8                                  ;
C0AB: C1 CA                                  ;
C0AD: C1 CC                                  ;
C0AF: C1 CE                                  ;
C0B1: C1 D0                                  ;
C0B3: C1 D2                                  ;
C0B5: C1 D4                                  ;
C0B7: C1 D6                                  ;
C0B9: C1 D8                                  ;
C0BB: C1 DA                                  ;
C0BD: C1 EA                                  ;
C0BF: C1 F8                                  ;
C0C1: C2 00                                  ;
C0C3: C2 08                                  ;
C0C5: C2 10                                  ;
C0C7: C2 1A                                  ;
C0C9: C2 24                                  ;
C0CB: C2 2C                                  ;
C0CD: C2 34                                  ;
C0CF: C2 3E                                  ;
C0D1: C2 48                                  ;
C0D3: C2 52                                  ;
C0D5: C2 5A                                  ;
C0D7: C2 64                                  ;
C0D9: C2 68                                  ;
C0DB: C2 74                                  ;
C0DD: C2 7E                                  ;
C0DF: C2 85                                  ;
C0E1: C2 8C                                  ;
C0E3: C2 93                                  ;
C0E5: C2 9A                                  ;
C0E7: C2 A1                                  ;
C0E9: C2 A8                                  ;
C0EB: C2 AA                                  ;
C0ED: C2 AC                                  ;
C0EF: C2 B4                                  ;
C0F1: C2 B8                                  ;
C0F3: C2 BC                                  ;
C0F5: C2 BE                                  ;
C0F7: C2 C6                                  ;
C0F9: C2 D2                                  ;
C0FB: C2 D6                                  ;
C0FD: C2 D8                                  ;
C0FF: C3 01                                  ;
C101: C3 0B                                  ;
C103: C3 21                                  ;

C105: C3 2B                                  ;"ADJUSTMENT"
C107: C4 64                                  ;"INITIAL"
C109: C5 8D                                  ;"TESTS"
C10B: C4 50                                  ;"INDICATE"
C10D: C5 BB                                  ;"UNIT"
C10F: C4 D1                                  ;"OK"
C111: C5 2D                                  ;"ROM"
C113: C5 1B                                  ;"RAM"
C115: C5 2D                                  ;"ROM"
C117: C4 04                                  ;"FAILURE"
C119: C5 1B                                  ;"RAM"
C11B: C4 04                                  ;"FAILURE"
C11D: C4 15                                  ;"GAME"
C11F: C4 E0                                  ;"OVER"
C121: C3 3E                                  ;"ALL"
C123: C5 31                                  ;"ROMS"
C125: C4 D1                                  ;"OK"
C127: C5 1B                                  ;"RAM"
C129: C5 81                                  ;"TEST"
C12B: C4 CA                                  ;"NO"
C12D: C5 1B                                  ;"RAM"
C12F: C3 F8                                  ;"ERRORS"
C131: C3 C6                                  ;"DETECTED"
C133: C3 93                                  ;"CMOS"
C135: C5 1B                                  ;"RAM"
C137: C4 04                                  ;"FAILURE"

C139: 06 28                                  ;
C13B: A0
C13C: C5 81                                  ;"TEST"
C13E: C4 AD                                  ;"MUST"
C140: C3 66                                  ;"BE"
C142: C3 F0                                  ;"ENTERED"

C144: 07
C144: C5 DA                                  ;"WITH"
C146: C3 98                                  ;"COIN"
C148: C3 CF                                  ;"DOOR"
C14B: C4 D8                                  ;"OPEN"
C14D: C3 93                                  ;"CMOS"
C14F: C5 1B                                  ;"RAM" 
C151: C4 D1                                  ;"OK"
C153: C4 A4                                  ;"MULTIPLE"
C155: C5 1B                                  ;"RAM"
C157: C4 04                                  ;"FAILURE"
C159: 03 FE         COM   <$FE               ;
C15B: C3 81                                  ;"TEST"
C15D: 04                                     ; ADDD  #$8104        ;
C15E: 10 
C15F: 02 
C160: F8

C161: C3 93                                  ;"CMOS"
C163: C5 1B                                  ;"RAM"
C165: C3 7D                                  ;"CAN"
C167: C4 CD                                  ;"NOT"
C169: C3 66                                  ;"BE"
C16B: C5 86                                  ;"TESTED"

C16D: C3 9D                                  ;"COLOR"
C16F: C5 1B                                  ;"RAM"
C171: C5 81                                  ;"TEST"

C173: 04 30                                  ;
C175: 02 
C176: E8

C177: C5 C3                                  ;"VERTICAL"
C179: C3 9D                                  ;"COLOR"
C17B: C3 61                                  ;"BARS"
C17D: C4 50                                  ;"INDICATE"

C17F: 07 03                                  ;
C181: FC

C182: C3 9D                                  ;"COLOR"
C184: C5 1B                                  ;"RAM"
C186: C4 04                                  ;"FAILURE"
C188: C3 49                                  ;"AUDIO"
C18A: C5 81                                  ;"TEST"

C18C: 07                                     ;CMPA  #$07          ;
C18D: 07 03                                  ;ASR   <$03          ;
C18F: 04

C190: C5 54                                  ;"SOUNDS"
C192: C5 7A                                  ;"SWITCH"
C194: C5 81                                  ;"TEST"
C196: C4 9C                                  ;"MONITOR"
C198: C5 81                                  ;"TEST"
C19A: C4 E5                                  ;"PATTERN"
C19C: C3 55                                  ;"AUTO"
C19E: C5 C0                                  ;"UP"
C1A0: C3 36                                  ;"ADVANCE"
C1A2: C5 27                                  ;"RIGHT"
C1A4: C3 98                                  ;"COIN"
C1A6: C4 35                                  ;"HIGHSCORE RESET"
C1A8: C4 8B                                  ;"LEFT"
C1AA: C3 98                                  ;"COIN"
C1AC: C3 85                                  ;"CENTER"
C1AE: C3 98                                  ;"COIN"
C1B0: C4 75                                  ;"INVALID SWITCH"
C1B2: C4 75                                  ;"INVALID SWITCH"
C1B4: C4 0C                                  ;"FIRE"
C1B6: C5 9C                                  ;"THRUST"
C1B8: C5 4E                                  ;"SMART"
C1BA: C3 69                                  ;"BOMB"
C1BB: C4 45                                  ;"HYPERSPACE"
C1BE: C5 B7                                  ;"TWO"
C1C0: C4 F5                                  ;"PLAYERS"
C1C2: C4 D4                                  ;"ONE"
C1C4: C4 EE                                  ;"PLAYER"
C1C6: C5 1F                                  ;"REVERSE"
C1C8: C3 D4                                  ;"DOWN"
C1CA: C5 C0                                  ;"UP"
C1CC: C4 75                                  ;"INVALID SWITCH"
C1CE: C4 75                                  ;"INVALID SWITCH"
C1D0: C4 75                                  ;"INVALID SWITCH"
C1D2: C4 75                                  ;"INVALID SWITCH"
C1D4: C4 75                                  ;"INVALID SWITCH"
C1D6: C4 75                                  ;"INVALID SWITCH"
C1D8: C4 75                                  ;"INVALID SWITCH"

;data for phrase "PRESS ADVANCE WITH SWITCH SET FOR"
C1DA: C5 0B                                  ;"PRESS"
C1DC: C3 36                                  ;"ADVANCE"
C1DE: C5 DA                                  ;"WITH"
C1E0: C5 7A                                  ;"SWITCH"
C1E2: C5 45                                  ;"SET"
C1E4: C4 11                                  ;"FOR"

C1E6: 03 FE                                  ;? VARIABLE ?

C1E8: C3 83                                  ;":"
C1EA: C3 55                                  ;"AUTO" 
C1EC: C4 11                                  ;"FOR"
C1EE: C3 4F                                  ;"AUDIT"

C1F0: 03 FE

C1F2: C3 81                                  ;","
C1F4: C4 15                                  ;"GAME"
C1F6: C3 2B                                  ;"ADJUSTMENT"
C1F8: C4 95                                  ;"MANUAL"
C1FA: C4 11                                  ;"FOR"
C1FC: C5 2D                                  ;"ROM"
C1FE: C5 81                                  ;"TEST"
C200: C3 55                                  ;"AUTO"
C202: C4 11                                  ;"FOR"
C204: C5 1B                                  ;"RAM"
C206: C5 81                                  ;"TEST"
C208: C3 55                                  ;"AUTO"
C20A: C5 AD                                  ;"TO"
C20C: C3 FF                                  ;"EXIT"
C20E: C5 81                                  ;"TEST"
C210: C3 55                                  ;"AUTO"
C212: C4 11                                  ;"FOR" 
C214: C3 93                                  ;"CMOS"
C216: C5 1B                                  ;"RAM" 
C218: C5 81                                  ;"TEST"
C21A: C3 55                                  ;"AUTO"
C2AC: C4 11                                  ;"FOR"
C21E: C3 9D                                  ;"COLOR"
C220: C5 1B                                  ;"RAM"
C222: C5 81                                  ;"TEST"
C224: C3 55                                  ;"AUTO"
C226: C4 11                                  ;"FOR"
C228: C3 49                                  ;"AUDIO"
C22A: C5 81                                  ;"TEST"
C22C: C3 55                                  ;"AUTO"
C22E: C4 11                                  ;"FOR"
C230: C5 7A                                  ;"SWITCH"
C232: C5 81                                  ;"TEST"
C234: C4 95                                  ;"MANUAL"
C236: C5 AD                                  ;"TO"
C238: C5 81                                  ;"TEST"
C23A: C4 59                                  ;"INDIVIDUAL"
C23C: C5 5A                                  ;"SOUNDS"
C23E: C3 55                                  ;"AUTO"
C240: C4 11                                  ;"FOR"
C242: C4 9C                                  ;"MONITOR"
C244: C5 81                                  ;"TEST"
C246: C4 E5                                  ;"PATTERN"
C248: C4 95                                  ;"MANUAL"
C24A: C5 AD                                  ;"TO"
C24C: C5 67                                  ;"STEP"
C24E: C5 97                                  ;"THRU"
C250: C4 E5                                  ;"PATTERN"
C252: C3 55                                  ;"AUTO"
C254: C4 11                                  ;"FOR"
C256: C4 15                                  ;"GAME"
C258: C4 E0                                  ;"OVER"
C25A: C4 95                                  ;"MANUAL"
C25C: C5 AD                                  ;"TO"
C25E: C5 67                                  ;"STEP"
C260: C5 97                                  ;"THRU"
C262: C3 2B                                  ;"ADJUSTMENT"
C264: C5 D1                                  ;"WILLIAMS"
C266: C3 BD                                  ;"DEFENDER"
C268: C5 0B                                  ;"PRESS"
C26A: C3 36                                  ;"ADVANCE"
C26C: C5 AD                                  ;"TO"
C26E: C5 67                                  ;"STEP"
C270: C5 97                                  ;"THRU"
C272: C5 81                                  ;"TEST"
C274: C5 0B                                  ;"PRESS"
C276: C4 35                                  ;"HIGHSCORE RESET"
C278: C5 AD                                  ;"TO"
C27A: C4 90                                  ;"MAKE"
C27C: C3 8C                                  ;"CHANGE"
C27E: C4 84                                  ;"LANDER"

C280: 07                                     ;ANDA  #$07          ;
C281: 03 06                                  ;COM   <$06          ;

C283: C4 B9                                  ;"350"
C285: C4 B2                                  ;"MUTANT"

C287: 07 03                                  ;ASR   <$03          ;
C289: 06

C28A: C4 B9                                  ;"350"
C28C: C4 FD                                  ;"POD"

C28E: 07 03                                  ;ASR   <$03          ;
C290: 00
C291: C4 C5                                  ;"1000"
C293: C3 6E                                  ;"BOMBER"

C295: 07                                     ;JMP   7,X           ;
C296: 03 06                                  ;COM   <$06          ;

C298: C4 C1                                  ;"250"
C29A: C5 72                                  ;"SWARMER"

C29C: 07 03                                  ;ASR   <$03          ;
C29E: 08

C29F: C4 B9                                  ;"350"
C2A1: C3 5A                                  ;"BAITER"

C2A3: 07 03                                  ;ASR   <$03          ;
C2A5: 06

C2A6: C4 BD                                  ;"200"
C2A8: C3 B4                                  ;"CREDITS:"
C2AA: C5 36                                  ;"SCANNER"
C2AC: C3 D9                                  ;"ELECTRONICS INC."

C2AE: 07                                     ;ADDD  #$D907        ;
C2AF: 07 03                                  ;ASR   <$03          ;
C2B1: 0C

C2B2: C5 02                                  ;"PRESENTS" 
C2B4: C4 EE                                  ;"PLAYER"
C2B6: C4 D4                                  ;"ONE"
C2B8: C4 EE                                  ;"PLAYER"
C2BA: C5 B7                                  ;"TWO"
C2BC: C3 75                                  ;"BONUS X"
C2BE: C5 0B                                  ;"PRESS"
C2C0: C4 D4                                  ;"ONE"
C2C2: C4 EE                                  ;"PLAYER"
C2C4: C5 61                                  ;"START"
C2C6: C5 0B                                  ;"PRESS"
C2C8: C4 D4                                  ;"ONE"
C2CA: C4 DD                                  ;"OR"
C2CC: C5 B7                                  ;"TWO"
C2CE: C4 EE                                  ;"PLAYER"
C2D0: C5 61                                  ;"START"
C2D2: C3 42                                  ;"ATTACK"
C2D4: C5 CC                                  ;"WAVE"
C2D6: C3 A3                                  ;"COMPLETED"
C2D8: C5 DF                                  ;"YOU"
C2DA: C4 30                                  ;"HAVE"
C2DC: C5 11                                  ;"QUALIFIED"
C2DE: C4 11                                  ;"FOR"

C2E0: 07

C2E1: C5 93                                  ;"THE"
C2E3: C3 BD                                  ;"DEFENDER"
C2E5: C4 23                                  ;"HALL OF FAME"

C2E7: 07 07                                  ;ASR   <$07          ;

C2E9: C5 3E                                  ;"SELECT"
C2EB: C4 6C                                  ;"INITIALS"
C2ED: C5 DA                                  ;"WITH"
C2EF: C5 C0                                  ;"UP"
C2F1: C3 D4                                  ;"DOWN"
C2F3: C5 6C                                  ;"STICK"

C2F5: 07                                     ;INC   7,X           ;
C2F6: 07

C2F7: C5 0B                                  ;"PRESS"
C2F9: C4 0C                                  ;"FIRE"
C2FB: C5 AD                                  ;"TO"
C2FD: C3 EA                                  ;"ENTER"
C2FF: C4 64                                  ;"INITIAL"

C301: A0                                     ;LSR   ,Y+           ;
C302: 00 02                                  ;NEG   <$02          ;
C304: 08 A0                                  ;LSL   <$A0          ;
C306: 02 
C307: 02 
C308: 10 
C309: A0 04                                  ;SUBA  4,X           ;

C30B: C4 23                                  ;"HALL OF FAME"

C30D: 06 22                                  ;ROR   <$22          ;
C30F: 68

C310: C5 B0                                  ;"TODAYS"

C312: 02 3E                                  ;SUBA  $023E         ;

C314: C3 3E                                  ;"ALL"
C316: C5 A8                                  ;"TIME"

C318: 07                                     ;EORA  7,X           ;
C319: 03 FC                                  ;COM   <$FC          ;

C31B: C4 1A                                  ;"GREATEST"

C31D: 02 
C31E: 3D                                     ;MUL                 ;

C31F: C4 1A                                  ;"GREATEST"
C321: A0 06                                  ;SUBA  6,X           ;
C323: 02 
C324: 05 
C325: A0 08                                  ;SUBA  8,X           ;
C327: 02 
C328: 13                                     ;SYNC                ;
C329: A0 0C                                  ;SUBA  12,X          ;

Some obvious text data, possibly Defender's entire vocabulary?

C32B: 41 44 4A 55                            ;   'ADJUSTMENT/'
C32F: 53 54 4D 45 
C333: 4E 54 2F 

C336: 41 44 56 41                            ;   'ADVANCE/'
C33A: 4E 43 45 2F

C33E: 41 4C 4C 2F                            ;   'ALL/'

C342: 41 54 54 41                            ;   'ATTACK/'
C346: 43 4B 2F

C349: 41 55 44 49                            ;   'AUDIO/'
C34D: 4F 2F

C34F: 41 55 44 49                            ;   'AUDIT/'
C353: 54 2F

C355: 41 55 54 4F                            ;   'AUTO/'
C359: 2F

C35A: 42 41 49 54                            ;   'BAITER/'
C35E: 45 52 2F

C361: 42 41 52 53                            ;   'BARS/'
C365: 2F

C366: 42 45 2F                               ;   'BE/'

C369: 42 4F 4D 42                            ;   'BOMB/'
C36D: 2F

C36E: 42 4F 4D 42                            ;   'BOMBER/'
C372: 45 52 2F

C375: 42 4F 4E 55                            ;   'BONUS X/'
C379: 53 20 58 2F

C37D: 43 41 4E 2F                            ;   'CAN/'

C381: 2C 2F                                  ;   ',/'

C383: 3A 2F                                  ;   ':/'

C385: 43 45 4E 54                            ;   'CENTER/'
C389: 45 52 2F 

C38C: 43 48 41 4E                            ;   'CHANGE/'
C390: 47 45 2F 

C393: 43 4D 4F 53                            ;   'CMOS/'
C397: 2F 

C398: 43 4F 49 4E                            ;   'COIN/'
C39C: 2F 

C39D: 43 4F 4C 4F                            ;   'COLOR/'
C3A1: 52 2F 

C3A3: 43 4F 4D 50                            ;   'COMPLETED/'
C3A7: 4C 45 54 45 
C3AB: 44 2F 

C3AD: 43 52 45 44                            ;   'CREDIT/'
C3B1: 49 54 2F 

C3B4: 43 52 45 44                            ;   'CREDITS:/'
C3B8: 49 54 53 3A 
C3BC: 2F 

C3BD: 44 45 46 45                            ;   'DEFENDER/'
C3C1: 4E 44 45 52 
C3C5: 2F 

C3C6: 44 45 54 45                            ;   'DETECTED/'
C3CA: 43 54 45 44 
C3CE: 2F 

C3DF: 44 4F 4F 52                            ;   'DOOR/'
C3D3: 2F 

C3D4: 44 4F 57 4E                            ;   'DOWN/'
C3D8: 2F 

C3D9: 45 4C 45 43                            ;   'ELECTRONICS INC./'
C3DD: 54 52 4F 4E 
C3E1: 49 43 53 20 
C3E5: 49 4E 43 2E 
C3E9: 2F

C3EA: 45 4E 54 45                            ;   'ENTER/'
C3EE: 52 2F 

C3F0: 45 4E 54 45                            ;   'ENTERED/'
C3F4: 52 45 44 2F 

C3F8: 45 52 52 4F                            ;   'ERRORS/'
C3FC: 52 53 2F 

C3FF: 45 58 49 54                            ;   'EXIT/'
C403: 2F 

C404: 46 41 49 4C                            ;   'FAILURE/'
C408: 55 52 45 2F 

C40C: 46 49 52 45                            ;   'FIRE/'
C410: 2F 

C411: 46 4F 52 2F                            ;   'FOR/'

C415: 47 41 4D 45                            ;   'GAME/'
C419: 2F 

C41A: 47 52 45 41                            ;   'GREATEST/'
C41E: 54 45 53 54 
C422: 2F 

C423: 48 41 4C 4C                            ;   'HALL OF FAME/'
C427: 20 4F 46 20 
C42B: 46 41 4D 45 
C42F: 2F 

C430: 48 41 56 45                            ;   'HAVE/'
C434: 2F 

C435: 48 49 47 48                            ;   'HIGHSCORE RESET/'
C439: 53 43 4F 52 
C43D: 45 20 52 45 
C441: 53 45 54 2F 

C445: 48 59 50 45                            ;   'HYPERSPACE/'
C449: 52 53 50 41 
C44D: 43 45 2F 

C450: 49 4E 44 49                            ;   'INDICATE/'
C454: 43 41 54 45 
C458: 2F 

C459: 49 4E 44 49                            ;   'INDIVIDUAL/'
C45D: 56 49 44 55 
C461: 41 4C 2F 

C464: 49 4E 49 54                            ;   'INITIAL/'
C468: 49 41 4C 2F 

C46C: 49 4E 49 54                            ;   'INITIALS/'
C470: 49 41 4C 53 
C474: 2F 

C475: 49 4E 56 41                            ;   'INVALID SWITCH/'
C479: 4C 49 44 20 
C47D: 53 57 49 54 
C481: 43 48 2F 

C484: 4C 41 4E 44                            ;   'LANDER/'
C488: 45 52 2F 

C48B: 4C 45 46 54                            ;   'LEFT/'
C48F: 2F 

C490: 4D 41 4B 45                            ;   'MAKE/'
C494: 2F 

C495: 4D 41 4E 55                            ;   'MANUAL/'
C499: 41 4C 2F 

C49C: 4D 4F 4E 49                            ;   'MONITOR/'
C4A0: 54 4F 52 2F 

C4A4: 4D 55 4C 54                            ;   'MULTIPLE/'
C4A8: 49 50 4C 45 
C4AC: 2F 

C4AD: 4D 55 53 54                            ;   'MUST/'
C4B1: 2F 

C4B2: 4D 55 54 41                            ;   'MUTANT/'
C4B6: 4E 54 2F 

C4B9: 31 35 30 2F                            ;   '350/'

C4BD: 32 30 30 2F                            ;   '200/'

C4C1: 32 35 30 2F                            ;   '250/'

C4C5: 31 30 30 30                            ;   '1000/'
C4C9: 2F

C4CA: 4E 4F 2F                               ;   'NO/'

C4CD: 4E 4F 54 2F                            ;   'NOT/'

C4D1: 4F 4B 2F                               ;   'OK/'

C4D4: 4F 4E 45 2F                            ;   'ONE/'

C4D8: 4F 50 45 4E                            ;   'OPEN/'
C4DC: 2F 

C4DD: 4F 52 2F                               ;   'OR/'

C4E0: 4F 56 45 52                            ;   'OVER/'
C4E4: 2F 

C4E5: 50 41 54 54                            ;   'PATTERN/'
C4E9: 45 52 4E 53 
C4ED: 2F 

C4EE: 50 4C 41 59                            ;   'PLAYER/'
C4F2: 45 52 2F 

C4F5: 50 4C 41 59                            ;   'PLAYERS/'
C4F9: 45 52 53 2F 

C4FD: 20 50 4F 44                            ;   ' POD/'
C501: 2F 

C502: 50 52 45 53                            ;   'PRESENTS/'
C506: 45 4E 54 53 
C50A: 2F 

C50B: 50 52 45 53                            ;   'PRESS/'
C50F: 53 2F 

C511: 51 55 41 4C                            ;   'QUALIFIED/'
C515: 49 46 49 45 
C519: 44 2F 

C51B: 52 41 4D 2F                            ;   'RAM/'

C51F: 52 45 56 45                            ;   'REVERSE/'
C523: 52 53 45 2F 

C527: 52 49 47 48                            ;   'RIGHT/'
C52B: 54 2F 

C52D: 52 4F 4D 2F                            ;   'ROM/'

C531: 52 4F 4D 53                            ;   'ROMS/'
C535: 2F 

C536: 53 43 41 4E                            ;   'SCANNER/'
C53A: 4E 45 52 2F 

C53E: 53 45 4C 45                            ;   'SELECT/'
C542: 43 54 2F 

C545: 53 45 54 2F                            ;   'SET/'

C549: 53 4C 41 4D                            ;   'SLAM/'
C54D: 2F 

C54E: 53 4D 41 52                            ;   'SMART/'
C552: 54 2F 

C553: 53 4F 55 4E                            ;   'SOUND/'
C558: 44 2F 

C55A: 53 4F 55 4E                            ;   'SOUNDS/'
C55E: 44 53 2F 

C561: 53 54 41 52                            ;   'START/'
C565: 54 2F 

C567: 53 54 45 50                            ;   'STEP/'
C56B: 2F 

C56C: 53 54 49 43                            ;   'STICK/'
C570: 4B 2F 

C572: 53 57 41 52                            ;   'SWARMER/'
C576: 4D 45 52 2F 

C57A: 53 57 49 54                            ;   'SWITCH/'
C57E: 43 48 2F 

C581: 54 45 53 54                            ;   'TEST/'
C585: 2F 

C586: 54 45 53 54                            ;   'TESTED/'
C58A: 45 44 2F 

C58D: 54 45 53 54                            ;   'TESTS/'
C591: 53 2F 

C593: 54 48 45 2F                            ;   'THE/'

C597: 54 48 52 55                            ;   'THRU/'
C59B: 2F 

C59C: 54 48 52 55                            ;   'THRUST/'
C5A0: 53 54 2F 

C5A3: 54 49 4C 54                            ;   'TILT/'
C5A7: 2F 

C5A8: 54 49 4D 45                            ;   'TIME/'
C5AC: 2F 

C5AD: 54 4F 2F                               ;   'TO/'

C5B0: 54 4F 44 41                            ;   'TODAYS/'
C5B4: 59 53 2F 

C5B7: 54 57 4F 2F                            ;   'TWO/'

C5BB: 55 4E 49 54                            ;   'UNIT/'
C5BF: 2F 

C5C0: 55 50 2F                               ;   'UP/'

C5C3: 56 45 52 54                            ;   'VERTICAL/'
C5C7: 49 43 41 4C 
C5CB: 2F 

C5CC: 57 41 56 45                            ;   'WAVE/'
C5D0: 2F 

C5D1: 57 49 4C 4C                            ;   'WILLIAMS/'
C5D5: 49 41 4D 53 
C5D9: 2F 

C5DA: 57 49 54 48                            ;   'WITH/'
C5DE: 2F 

C5DF: 59 4F 55 2F                            ;   'YOU/'



C5E3: 01 08 C6 97                            ;" "
C5E7: 01 08 C6 AF                            ;"!"
C5EB: 01 08 C6 B7                            ;","
C5EF: 03 08 C7 BF                            ;"?"
C5F3: 01 08 C6 BF                            ;"."
C5F7: 03 08 C7 BF                            ;"?"
C5FB: 03 08 C6 C7                            ;"0"
C5FF: 03 08 C6 DF                            ;"1"
C603: 03 08 C6 F7                            ;"2"
C607: 03 08 C7 0F                            ;"3"
C60B: 03 08 C7 27                            ;"4"
C60F: 03 08 C7 3F                            ;"5"
C613: 03 08 C7 57                            ;"6"
C617: 03 08 C7 6F                            ;"7"
C61B: 03 08 C7 87                            ;"8"
C61F: 03 08 C7 9F                            ;"9"
C623: 01 08 C7 B7                            ;":"
C627: 03 08 C7 BF                            ;"?"
C62B: 03 08 C6 97                            ;"   "
C62F: 03 08 C7 D7                            ;"A"
C633: 03 08 C7 EF                            ;"B"
C637: 03 08 C8 07                            ;"C"
C63B: 03 08 C8 1F                            ;"D"
C63F: 03 08 C8 37                            ;"E"
C643: 03 08 C8 4F                            ;"F"
C647: 03 08 C8 67                            ;"G"
C64B: 03 08 C8 7F                            ;"H"
C64F: 02 08 C8 97                            ;"I"
C653: 03 08 C8 A7                            ;"J"
C657: 03 08 C8 BF                            ;"K"
C65B: 03 08 C8 D7                            ;"L"
C65F: 04 08 C8 EF                            ;"M"
C663: 03 08 C9 0F                            ;"N"
C667: 03 08 C9 27                            ;"O"
C66B: 03 08 C9 3F                            ;"P"
C66F: 03 08 C9 57                            ;"Q"
C673: 03 08 C9 6F                            ;"R"
C677: 03 08 C9 87                            ;"S"
C67B: 03 08 C9 9F                            ;"T"
C67F: 03 08 C9 B7                            ;"U"
C683: 03 08 C9 CF                            ;"V"
C687: 04 08 C9 E7                            ;"W"
C68B: 03 08 CA 07                            ;"X"
C68F: 03 08 CA 1F                            ;"Y"
C693: 03 08 CA 37                            ;"Z"

Spaces, punctuation and numbers display data

C697: 00 00 00 00                            ;" " and "   "
C69B: 00 00 00 00
C69F: 00 00 00 00
C6A3: 00 00 00 00
C6A7: 00 00 00 00
C6AB: 00 00 00 00
C6AF: 01 01 01 01                            ;"!"
C6B3: 01 00 01 00
C6B7: 00 00 00 00                            ;","
C6BB: 00 01 01 10 
C6BF: 00 00 00 00                            ;"."
C6C3: 00 00 01 00
C6C7: 01 01 01 01                            ;0
C6CB: 01 01 01 00
C6CF: 11 00 00 00
C6D3: 00 00 11 00
C6D7: 11 11 11 11 
C6DB: 11 11 11 00
C6DF: 00 00 01 00                            ;1
C6E3: 00 00 00 00
C6E7: 01 11 10 00
C6EB: 00 00 00 00
C6EF: 11 11 11 11 
C6F3: 11 11 11 00
C6F7: 01 01 00 00                            ;2
C6FB: 00 01 01 00
C6FF: 11 00 00 01 
C703: 10 00 11 00
C707: 11 11 11 10 
C70B: 00 00 11 00
C70F: 01 00 00 00                            ;3
C713: 00 00 01 00
C717: 11 00 00 11 
C71B: 00 00 11 00
C71F: 11 11 11 11 
C723: 11 11 11 00
C727: 00 00 01 01                            ;4 
C72B: 00 00 00 00
C72F: 01 10 00 11
C733: 00 00 00 00
C737: 11 11 11 11 
C73B: 11 11 11 00
C73F: 01 01 01 01                            ;5
C743: 00 00 01 00
C747: 11 10 10 11 
C74B: 00 00 11 00
C74F: 11 00 00 11 
C753: 01 01 11 00
C757: 01 01 01 01                            ;6 
C75B: 01 01 01 00
C75F: 11 10 10 11 
C763: 10 10 11 00
C767: 11 00 00 11 
C76B: 01 01 11 00
C76F: 01 00 00 00                            ;7
C773: 00 01 01 00
C777: 11 00 00 01 
C77B: 11 10 10 00
C77F: 11 11 11 10 
C783: 00 00 00 00
C787: 01 01 01 00                            ;8
C78B: 01 01 01 00
C78F: 11 10 10 11 
C793: 10 10 11 00
C797: 11 01 01 10 
C79B: 01 01 11 00
C79F: 01 01 01 01                            ;9 
C7A3: 00 00 01 00
C7A7: 11 10 10 11 
C7AB: 00 00 11 00
C7AF: 11 01 01 11 
C7B3: 01 01 11 00
C7B7: 00 00 01 00                            ;":"
C7BB: 00 01 00 00
C7BF: 01 01 00 00                            ;"?"
C7C3: 00 00 00 00
C7C7: 11 00 00 01 
C7CB: 01 00 01 00
C7CF: 11 11 11 10 
C7D3: 00 00 00 00

Alphabet display data

C7D7: 01 01 01 01                            ;A
C7DB: 01 01 01 00
C7DF: 11 00 00 11 
C7E3: 00 00 00 00
C7E7: 11 11 11 11 
C7EB: 11 11 11 00
C7EF: 01 01 01 01                            ;B
C7F3: 01 01 01 00
C7F7: 11 00 00 11 
C7FB: 00 00 11 00
C7FF: 11 11 11 11 
C803: 11 11 11 00
C807: 01 01 01 01                            ;C
C80B: 01 01 01 00
C80F: 11 10 10 10 
C813: 10 10 11 00
C817: 11 00 00 00
C81B: 00 00 11 00
C81F: 01 01 01 01                            ;D 
C823: 01 01 01 00
C827: 11 00 00 00
C82B: 00 00 11 00
C82F: 10 11 11 11 
C833: 11 11 10 00
C837: 01 01 01 01                            ;E
C83B: 01 01 01 00
C83F: 11 10 10 11 
C843: 10 10 11 00
C847: 11 00 00 10 
C84B: 00 00 11 00
C84F: 01 01 01 01                            ;F
C853: 01 01 01 00
C857: 11 10 10 11 
C85B: 10 10 10 00
C85F: 11 00 00 10 
C863: 00 00 00 00
C867: 01 01 01 01                            ;G
C86B: 01 01 01 00
C86F: 11 10 10 10 
C873: 10 10 11 00
C877: 11 00 00 11 
C87B: 01 01 11 00
C87F: 01 01 01 01                            ;H
C883: 01 01 01 00
C887: 10 10 10 11 
C88B: 10 10 10 00
C88F: 01 01 01 11 
C893: 01 01 01 00
C897: 01 01 01 01                            ;I 
C89B: 01 01 01 00
C89F: 10 10 10 10 
C8A3: 10 10 10 00
C8A7: 00 00 00 00                            ;J
C8AB: 00 01 01 00
C8AF: 00 00 00 00
C8B3: 00 00 11 00
C8B7: 11 11 11 11 
C8BB: 11 11 11 00
C8BF: 01 01 01 01                            ;K
C8C3: 01 01 01 00
C8C7: 00 00 01 11 
C8CB: 01 00 00 00
C8CF: 01 10 00 00
C8D3: 00 10 01 00
C8D7: 01 01 01 01                            ;L
C8DB: 01 01 01 00
C8DF: 10 10 10 10 
C8E3: 10 10 11 00
C8E7: 00 00 00 00
C8EB: 00 00 11 00
C8EF: 01 01 01 01                            ;M
C8F3: 01 01 01 00
C8F7: 11 10 10 10 
C8FB: 10 10 10 00
C8FF: 11 10 10 10 
C903: 00 00 00 00
C907: 11 11 11 11 
C90B: 11 11 11 00 
C90F: 01 01 01 01                            ;N 
C913: 01 01 01 00
C917: 11 10 10 10 
C91B: 10 10 10 00
C91F: 11 01 01 01 
C923: 01 01 01 00 
C927: 01 01 01 01                            ;O 
C92B: 01 01 01 00
C92F: 11 10 10 10 
C933: 10 10 11 00
C937: 11 01 01 01 
C93B: 01 01 11 00
C93F: 01 01 01 01                            ;P
C943: 01 01 01 00
C947: 11 10 10 11 
C94B: 10 10 10 00
C94F: 11 01 01 11 
C953: 00 00 00 00
C957: 01 01 01 01                            ;Q
C95B: 01 01 01 00
C95F: 11 10 10 10 
C963: 10 10 11 00
C967: 11 01 01 01 
C96B: 01 11 11 10 
C96F: 01 01 01 01                            ;R
C973: 01 01 01 00
C977: 11 10 10 11 
C97B: 10 10 10 00
C97F: 11 01 01 11 
C983: 10 01 01 00
C987: 01 01 01 01                            ;S
C98B: 00 00 01 00
C98F: 11 10 10 11 
C993: 00 00 11 00
C997: 11 00 00 11 
C99B: 11 11 11 00
C99F: 11 00 00 00                            ;T
C9A3: 00 00 00 00
C9A7: 11 11 11 11 
C9AB: 11 11 11 00
C9AF: 11 00 00 00
C9B3: 00 00 00 00
C9B7: 01 01 01 01                            ;U
C9BB: 01 01 01 00
C9BF: 10 10 10 10 
C9C3: 10 10 11 00
C9C7: 01 01 01 01 
C9CB: 01 01 11 00
C9CF: 01 01 01 01                            ;V
C9D3: 01 00 00 00
C9D7: 00 00 00 00
C9DB: 00 10 01 00
C9DF: 01 01 01 01 
C9E3: 01 10 00 00
C9E7: 01 01 01 01                            ;W
C9EB: 01 01 00 00
C9EF: 10 10 10 10 
C9F3: 10 10 01 00
C9F7: 10 10 10 10 
C9FB: 10 10 01 00
C9FF: 10 10 10 10 
CA03: 10 10 00 00
CA07: 01 01 00 00                            ;X
CA0B: 00 01 01 00
CA0F: 00 00 10 01 
CA13: 10 00 00 00
CA17: 01 01 10 00
CA1B: 10 01 01 00
CA1F: 01 01 00 00                            ;Y
CA23: 00 00 00 00
CA27: 00 00 10 01 
CA2B: 01 01 01 00
CA2F: 01 01 10 00
CA33: 00 00 00 00
CA37: 01 00 00 00                            ;Z
CA3B: 01 01 01 00
CA3F: 11 00 01 10 
CA43: 00 00 11 00
CA47: 11 10 00 00
CA4B: 00 00 11 00



CA4F: 84
CA50: FF 



;in jump table
CA51: 34 70         PSHS  U,Y,X              ;
CA53: CE C0 D9      LDU   #$C0D9             ;
CA56: 20 05         BRA   $CA5D              ;

;in jump table
CA58: 34 70         PSHS  U,Y,X              ;
CA5A: CE C0 BB      LDU   #$C0BB             ;
CA5D: 8E 18 CE      LDX   #$18CE             ;
CA60: BD CA A7      JSR   $CAA7              ;
CA63: EE A1         LDU   ,Y++               ;
CA65: 27 06         BEQ   $CA6D              ;
CA67: 8E 10 DA      LDX   #$10DA             ;
CA6A: BD CA A7      JSR   $CAA7              ;
CA6D: EE A1         LDU   ,Y++               ;
CA6F: 27 06         BEQ   $CA77              ;
CA71: 8E 10 E4      LDX   #$10E4             ;
CA74: BD CA A7      JSR   $CAA7              ;
CA77: 35 F0         PULS  X,Y,U,PC           ;



;in jump table
CA79: 34 77         PSHS  U,Y,X,B,A,CC       ;
CA7B: 10 8E FF B6   LDY   #ScrnBlkClrP2X     ;
CA7F: 20 06         BRA   $CA87              ;


;in jump table
CA81: 34 77         PSHS  U,Y,X,B,A,CC       ;
CA83: 10 8E FF B3   LDY   #DrawCharX         ;loading a SUBR address
CA87: CC CA ED      LDD   #$CAED             ;loading a jump address
CA8A: 10 9F 3D      STY   <$3D               ;storing the SUBR address for later
CA8D: DD 3F         STD   <$3F               ;storing the jump address for later
CA8F: 9F 50         STX   <$50               ;
CA91: 9F 4E         STX   <$4E               ;
CA93: 8E 01 0A      LDX   #$010A             ;
CA96: 9F 4C         STX   <$4C               ;
CA98: 0F 58         CLR   <$58               ;
CA9A: EE 65         LDU   5,S                ;
CA9C: DF 54         STU   <$54               ;
CA9E: 33 C8 20      LEAU  $20,U              ;
CAA1: DF 56         STU   <$56               ;
CAA3: DF 52         STU   <$52               ;
CAA5: 20 46         BRA   $CAED              ;


;SUBRTN  in jump table
CAA7: 34 77         PSHS  U,Y,X,B,A,CC       ;
CAA9: 10 8E FF B3   LDY   #DrawCharX         ;set call address to DrawCharX
CAAD: CC CA ED      LDD   #$CAED             ;
CAB0: 20 1F         BRA   $CAD1              ;


;SUBRTN  in jump table
CAB2: 34 77         PSHS  U,Y,X,B,A,CC       ;
CAB4: 10 8E FF B6   LDY   #ScrnBlkClrP2X     ;
CAB8: CC CA ED      LDD   #$CAED             ;
CABB: 20 14         BRA   $CAD1              ;


;SUBRTN  in jump table
CABD: 34 77         PSHS  U,Y,X,B,A,CC       ;
CABF: 10 8E FF B3   LDY   #DrawCharX         ;set call address to DrawCharX
CAC3: CC CB 5F      LDD   #$CB5F             ;set jump address to exit w/o error
CAC6: 20 09         BRA   $CAD1              ;


;SUBRTN  in jump table
CAC8: 34 77         PSHS  U,Y,X,B,A,CC       ;
CACA: 10 8E FF B6   LDY   #ScrnBlkClrP2X     ;
CACE: CC CB 5F      LDD   #$CB5F             ;set jump address to exit w/o error
CAD1: 10 9F 3D      STY   <$3D               ;store call address for later
CAD4: DD 3F         STD   <$3F               ;store jump address for later
CAD6: 0D 52         TST   <$52               ;
CAD8: 26 13         BNE   $CAED              ;
CADA: 9F 50         STX   <$50               ;
CADC: 9F 4E         STX   <$4E               ;
CADE: 8E 01 0A      LDX   #$010A             ;
CAE1: 9F 4C         STX   <$4C               ;
CAE3: 0F 58         CLR   <$58               ;
CAE5: AE 42         LDX   2,U                ;
CAE7: 9F 56         STX   <$56               ;
CAE9: AE C4         LDX   ,U                 ;
CAEB: 20 21         BRA   $CB0E              ;

CAED: 0D 58         TST   <$58               ;
CAEF: 26 0E         BNE   $CAFF              ;
CAF1: 9E 54         LDX   <$54               ;
CAF3: E6 80         LDB   ,X+                ;
CAF5: C1 2F         CMPB  #$2F               ;
CAF7: 26 30         BNE   $CB29              ;
CAF9: C6 20         LDB   #$20               ;
CAFB: D7 58         STB   <$58               ;
CAFD: 20 2A         BRA   $CB29              ;
CAFF: 0F 58         CLR   <$58               ;
CB01: 9E 52         LDX   <$52               ;
CB03: 9C 56         CMPX  <$56               ;
CB05: 26 07         BNE   $CB0E              ;
;exit with error condition?
CB07: 0F 52         CLR   <$52               ;
CB09: 35 77         PULS  CC,A,B,X,Y,U       ;
CB0B: 1A 01         ORCC  #$01               ;exit w/ error, set C flag
CB0D: 39            RTS                      ;


CB0E: EE 81         LDU   ,X++               ;
CB10: 2B 11         BMI   $CB23              ;
CB12: 30 1F         LEAX  -1,X               ;
CB14: 1F 30         TFR   U,D                ;
CB16: 81 08         CMPA  #$08               ;
CB18: 22 ED         BHI   $CB07              ;
CB1A: 48            ASLA                     ;
CB1B: 10 8E CB 64   LDY   #$CB64             ;load jump vector table address in Y
CB1F: AD B6         JSR   [A,Y]              ;call subroutine in vector table with A reg offset
CB21: 20 E0         BRA   $CB03              ;
CB23: 9F 52         STX   <$52               ;
CB25: DF 54         STU   <$54               ;
CB27: 20 C4         BRA   $CAED              ;
CB29: 9F 54         STX   <$54               ;
CB2B: C0 20         SUBB  #$20               ;
CB2D: C1 01         CMPB  #$01               ;
CB2F: 23 16         BLS   $CB47              ;
CB31: C1 0B         CMPB  #$0B               ;
CB33: 23 10         BLS   $CB45              ;
CB35: C0 0A         SUBB  #$0A               ;
CB37: C1 10         CMPB  #$10               ;
CB39: 23 0C         BLS   $CB47              ;
CB3B: C1 14         CMPB  #$14               ;
CB3D: 23 06         BLS   $CB45              ;
CB3F: C0 04         SUBB  #$04               ;
CB41: C1 2C         CMPB  #$2C               ;
CB43: 23 02         BLS   $CB47              ;
CB45: C6 03         LDB   #$03               ;
CB47: 58            ASLB                     ;
CB48: 58            ASLB                     ;
CB49: 8E C5 E3      LDX   #$C5E3             ;
CB4C: 3A            ABX                      ;
CB4D: 1F 12         TFR   X,Y                ;
CB4F: DC 50         LDD   <$50               ;
CB51: 9E 3D         LDX   <$3D               ;retrieve stored subroutine address
CB53: AD 84         JSR   ,X                 ;call subroutine
CB55: AB A4         ADDA  ,Y                 ;
CB57: 9B 4C         ADDA  <$4C               ;
CB59: 97 50         STA   <$50               ;
CB5B: 9E 3F         LDX   <$3F               ;retrieve stored jump address
CB5D: 6E 84         JMP   ,X                 ;jump

CB5F: 35 77         PULS  CC,A,B,X,Y,U       ;
CB61: 1C FE         ANDCC #$FE               ;exit w/o error, clear C flag
CB63: 39            RTS                      ;



;Subroutine vector table
CB64: CB 76                                  ;  $CB76          ;
CB66: CB 7B                                  ;  $CB7B          ;
CB68: CB 80                                  ;  $CB80          ;
CB6A: CB 87                                  ;  $CB87          ;
CB6C: CB 8E                                  ;  $CB8E          ;
CB6E: CB 95                                  ;  $CB95          ;
CB70: CB 9C                                  ;  $CB9C          ;
CB72: CB A3                                  ;  $CBA3          ;
CB74: CB AC                                  ;  $CBAC          ;END of jump table


;SUBRTN
CB76: A6 80         LDA   ,X+                ;
CB78: 97 4C         STA   <$4C               ;
CB7A: 39            RTS                      ;


;SUBRTN
CB7B: E6 80         LDB   ,X+                ;
CB7D: D7 4D         STB   <$4D               ;
CB7F: 39            RTS                      ;


;SUBRTN
CB80: 96 4E         LDA   <$4E               ;
CB82: AB 80         ADDA  ,X+                ;
CB84: 97 50         STA   <$50               ;
CB86: 39            RTS                      ;


;SUBRTN
CB87: 96 50         LDA   <$50               ;
CB89: AB 80         ADDA  ,X+                ;
CB8B: 97 50         STA   <$50               ;
CB8D: 39            RTS                      ;


;SUBRTN
CB8E: D6 4F         LDB   <$4F               ;
CB90: EB 80         ADDB  ,X+                ;
CB92: D7 51         STB   <$51               ;
CB94: 39            RTS                      ;


;SUBRTN
CB95: D6 51         LDB   <$51               ;
CB97: EB 80         ADDB  ,X+                ;
CB99: D7 51         STB   <$51               ;
CB9B: 39            RTS                      ;


;SUBRTN
CB9C: EC 81         LDD   ,X++               ;
CB9E: DD 4E         STD   <$4E               ;
CBA0: DD 50         STD   <$50               ;
CBA2: 39            RTS                      ;


;SUBRTN
CBA3: 96 4E         LDA   <$4E               ;
CBA5: D6 51         LDB   <$51               ;
CBA7: DB 4D         ADDB  <$4D               ;
CBA9: DD 50         STD   <$50               ;
CBAB: 39            RTS                      ;


;SUBRTN
CBAC: 10 AE 81      LDY   ,X++               ;
CBAF: 9F 52         STX   <$52               ;
CBB1: 9E 3D         LDX   <$3D               ;retrieve stored subroutine address
CBB3: AD 84         JSR   ,X                 ;call subroutine
CBB5: AB A4         ADDA  ,Y                 ;
CBB7: 9B 4C         ADDA  <$4C               ;
CBB9: 97 50         STA   <$50               ;
CBBB: 32 62         LEAS  2,S                ;step over the return address
CBBD: 9E 3F         LDX   <$3F               ;load previously stored jump address
CBBF: 6E 84         JMP   ,X                 ;jump



;SUBRTN   in jump table
CBC1: 34 77         PSHS  U,Y,X,B,A,CC       ;
CBC3: 10 8E FF B3   LDY   #DrawCharX         ;set call address to DrawCharX
CBC7: CE CC 0F      LDU   #$CC0F             ;
CBCA: 20 1F         BRA   $CBEB              ;

;SUBRTN   in jump table
CBCC: 34 77         PSHS  U,Y,X,B,A,CC       ;
CBCE: 10 8E FF B6   LDY   #ScrnBlkClrP2X     ;
CBD2: CE CC 0F      LDU   #$CC0F             ;
CBD5: 20 14         BRA   $CBEB              ;

;in jump table
CBD7: 34 77         PSHS  U,Y,X,B,A,CC       ;
CBD9: 10 8E FF B3   LDY   #DrawCharX         ;set call address to DrawCharX
CBDD: CE CC 39      LDU   #$CC39             ;jump address to exit w/o error
CBE0: 20 09         BRA   $CBEB              ;

;in jump table
CBE2: 34 77         PSHS  U,Y,X,B,A,CC       ;
CBE4: 10 8E FF B6   LDY   #ScrnBlkClrP2X     ;
CBE8: CE CC 39      LDU   #$CC39             ;jump address to exit w/o error
CBEB: 10 9F 3D      STY   <$3D               ;store call address
CBEE: DF 3F         STU   <$3F               ;store jump address
CBF0: DE 59         LDU   <$59               ;
CBF2: 11 83 FF FF   CMPU  #$FFFF             ;
CBF6: 26 15         BNE   $CC0D              ;
CBF8: 9F 50         STX   <$50               ;
CBFA: DD 59         STD   <$59               ;
CBFC: 26 05         BNE   $CC03              ;
CBFE: CC 0F FF      LDD   #$0FFF             ;
CC01: 20 08         BRA   $CC0B              ;
CC03: 85 F0         BITA  #$F0               ;
CC05: 26 04         BNE   $CC0B              ;
CC07: 8D 35         BSR   $CC3E              ;
CC09: 20 F8         BRA   $CC03              ;
CC0B: DD 59         STD   <$59               ;
CC0D: DC 59         LDD   <$59               ;
CC0F: 84 F0         ANDA  #$F0               ;
CC11: 81 F0         CMPA  #$F0               ;
CC13: 26 07         BNE   $CC1C              ;
CC15: 35 77         PULS  CC,A,B,X,Y,U       ;
CC17: 9E 50         LDX   <$50               ;
CC19: 1A 01         ORCC  #$01               ;error occurred, set carry flag
CC1B: 39            RTS                      ;


CC1C: 44            LSRA                     ;
CC1D: 44            LSRA                     ;
CC1E: 8E C5 FB      LDX   #$C5FB             ;
CC21: 31 86         LEAY  A,X                ;
CC23: DC 50         LDD   <$50               ;
CC25: 9E 3D         LDX   <$3D               ;retrieve stored subroutine address
CC27: AD 84         JSR   ,X                 ;call subroutine
CC29: AB A4         ADDA  ,Y                 ;
CC2B: 9B 4C         ADDA  <$4C               ;
CC2D: 97 50         STA   <$50               ;
CC2F: DC 59         LDD   <$59               ;
CC31: 8D 0B         BSR   $CC3E              ;
CC33: DD 59         STD   <$59               ;
CC35: 9E 3F         LDX   <$3F               ;retrieve store jump address
CC37: 6E 84         JMP   ,X                 ;jump
CC39: 35 77         PULS  CC,A,B,X,Y,U       ;
CC3B: 1C FE         ANDCC #$FE               ;no error, clear carry
CC3D: 39            RTS                      ;



;SUBRTN
CC3E: 58            ASLB                     ;shifting the D reg left 4 bits
CC3F: 49            ROLA                     ;
CC40: 58            ASLB                     ;
CC41: 49            ROLA                     ;
CC42: 58            ASLB                     ;
CC43: 49            ROLA                     ;
CC44: 58            ASLB                     ;
CC45: 49            ROLA                     ;
CC46: CA 0F         ORB   #$0F               ;set all the bits in the LSN
CC48: 39            RTS                      ;return

 \\ \\ \\ data area

CC49: 00 00         NEG   <$00               ;
CC4B: 00 00         NEG   <$00               ;
CC4D: 00 00         NEG   <$00               ;
CC4F: 00 05         NEG   <$05               ;
CC51: 38 
CC52: 4E 
CC53: CE 96 09      LDU   #$9609             ;
CC56: AC 42         CMPX  2,U                ;
CC58: 90 16         SUBA  <$16               ;
CC5A: 52 
CC5B: A8 
CC5C: F2 12 96      SBCB  $1296              ;
CC5F: 6A 08         DEC   8,X                ;
CC61: C0 DE         SUBB  #$DE               ;
CC63: CA A5         ORB   #$A5               ;
CC65: 54            LSRB                     ;
CC66: 1B 
CC67: 88 2D         EORA  #$2D               ;
CC69: 59            ROLB                     ;
CC6A: A3 96         SUBD  [A,X]              ;
CC6C: 41 
CC6D: DC EF         LDD   <$EF               ;
CC6F: A3 27         SUBD  7,Y                ;
CC71: 03 B6         COM   <$B6               ;
CC73: 1C EF         ANDCC #$EF               ;
CC75: 5E 
CC76: FF D7 B0      STU   $D7B0              ;
CC79: 56            RORB                     ;
CC7A: A4 76         ANDA  -10,S              ;
CC7C: C3 A0 90      ADDD  #$A090             ;
CC7F: 9B D9         ADDA  <$D9               ;
CC81: 08 D3         LSL   <$D3               ;
CC83: 04 CB         LSR   <$CB               ;
CC85: 99 C8         ADCA  <$C8               ;
CC87: 70 43 94      NEG   $4394              ;
CC8A: 33 7B         LEAU  -5,S               ;
CC8C: 6B 
CC8D: 8D B2         BSR   $CC41              ;
CC8F: F8 00 0C      EORB  $000C              ;
CC92: CC CC CC      LDD   #$CCCC             ;
CC95: CC 0C 00      LDD   #$0C00             ;
CC98: CC CC CC      LDD   #$CCCC             ;
CC9B: CC CC CC      LDD   #$CCCC             ;
CC9E: CC CC CC      LDD   #$CCCC             ;
CCA1: CC CC CC      LDD   #$CCCC             ;
CCA4: CC CC CC      LDD   #$CCCC             ;
CCA7: CC 00 C0      LDD   #$00C0             ;
CCAA: CC CC CC      LDD   #$CCCC             ;
CCAD: CC C0 00      LDD   #$C000             ;
CCB0: A0 0A         SUBA  10,X               ;
CCB2: A0 A0         SUBA  ,Y+                ;
CCB4: 00 A0         NEG   <$A0               ;
CCB6: 0A 00         DEC   <$00               ;
CCB8: 0A 0A         DEC   <$0A               ;
CCBA: A0 0A         SUBA  10,X               ;
CCBC: 0A AA         DEC   <$AA               ;
CCBE: 0A 00         DEC   <$00               ;
CCC0: A0 00         SUBA  0,X                ;
CCC2: 00 0A         NEG   <$0A               ;
CCC4: 00 A0         NEG   <$A0               ;
CCC6: AA A0         ORA   ,Y+                ;
CCC8: 00 02         NEG   <$02               ;
CCCA: 23 02         BLS   $CCCE              ;
CCCC: 20 22         BRA   $CCF0              ;
CCCE: 23 22         BLS   $CCF2              ;
CCD0: 00 00         NEG   <$00               ;
CCD2: 20 00         BRA   $CCD4              ;
CCD4: 00 00         NEG   <$00               ;
CCD6: 02 
CCD7: 00 02         NEG   <$02               ;
CCD9: 22 32         BHI   $CD0D              ;
CCDB: 22 00         BHI   $CCDD              ;
CCDD: 20 32         BRA   $CD11              ;
CCDF: 20 00         BRA   $CCE1              ;
CCE1: 00 03         NEG   <$03               ;
CCE3: 03 00         COM   <$00               ;
CCE5: 00 03         NEG   <$03               ;
CCE7: 30 04         LEAX  4,X                ;
CCE9: 34 30         PSHS  Y,X                ;
CCEB: 30 34         LEAX  -12,Y              ;
CCED: 30 00         LEAX  0,X                ;
CCEF: 00 44         NEG   <$44               ;
CCF1: 44            LSRA                     ;
CCF2: 33 33         LEAU  -13,Y              ;
CCF4: 34 30         PSHS  Y,X                ;
CCF6: 30 30         LEAX  -16,Y              ;
CCF8: 00 30         NEG   <$30               ;
CCFA: 03 03         COM   <$03               ;
CCFC: 30 30         LEAX  -16,Y              ;
CCFE: 03 00         COM   <$00               ;
CD00: 00 00         NEG   <$00               ;
CD02: 00 00         NEG   <$00               ;
CD04: 00 00         NEG   <$00               ;
CD06: 00 30         NEG   <$30               ;
CD08: 00 00         NEG   <$00               ;
CD0A: 00 00         NEG   <$00               ;
CD0C: 00 00         NEG   <$00               ;
CD0E: 00 03         NEG   <$03               ;
CD10: 00 03         NEG   <$03               ;
CD12: 33 33         LEAU  -13,Y              ;
CD14: 03 03         COM   <$03               ;
CD16: 30 00         LEAX  0,X                ;
CD18: 44            LSRA                     ;
CD19: 44            LSRA                     ;
CD1A: 03 03         COM   <$03               ;
CD1C: 43            COMA                     ;
CD1D: 03 03         COM   <$03               ;
CD1F: 03 40         COM   <$40               ;
CD21: 43            COMA                     ;
CD22: 30 30         LEAX  -16,Y              ;
CD24: 43            COMA                     ;
CD25: 03 00         COM   <$00               ;
CD27: 00 00         NEG   <$00               ;
CD29: 00 30         NEG   <$30               ;
CD2B: 30 00         LEAX  0,X                ;
CD2D: 00 30         NEG   <$30               ;
CD2F: 03 00         COM   <$00               ;
CD31: 00 03         NEG   <$03               ;
CD33: 03 00         COM   <$00               ;
CD35: 00 03         NEG   <$03               ;
CD37: 30 04         LEAX  4,X                ;
CD39: 34 03         PSHS  A,CC               ;
CD3B: 03 34         COM   <$34               ;
CD3D: 30 00         LEAX  0,X                ;
CD3F: 00 44         NEG   <$44               ;
CD41: 44            LSRA                     ;
CD42: 30 30         LEAX  -16,Y              ;
CD44: 34 30         PSHS  Y,X                ;
CD46: 30 30         LEAX  -16,Y              ;
CD48: 00 30         NEG   <$30               ;
CD4A: 33 33         LEAU  -13,Y              ;
CD4C: 30 30         LEAX  -16,Y              ;
CD4E: 03 00         COM   <$00               ;
CD50: 00 00         NEG   <$00               ;
CD52: 00 00         NEG   <$00               ;
CD54: 00 00         NEG   <$00               ;
CD56: 00 30         NEG   <$30               ;
CD58: 00 00         NEG   <$00               ;
CD5A: 00 00         NEG   <$00               ;
CD5C: 00 00         NEG   <$00               ;
CD5E: 00 03         NEG   <$03               ;
CD60: 00 03         NEG   <$03               ;
CD62: 30 30         LEAX  -16,Y              ;
CD64: 03 03         COM   <$03               ;
CD66: 30 00         LEAX  0,X                ;
CD68: 44            LSRA                     ;
CD69: 44            LSRA                     ;
CD6A: 33 33         LEAU  -13,Y              ;
CD6C: 43            COMA                     ;
CD6D: 03 03         COM   <$03               ;
CD6F: 03 40         COM   <$40               ;
CD71: 43            COMA                     ;
CD72: 03 03         COM   <$03               ;
CD74: 43            COMA                     ;
CD75: 03 00         COM   <$00               ;
CD77: 00 00         NEG   <$00               ;
CD79: 00 30         NEG   <$30               ;
CD7B: 30 00         LEAX  0,X                ;
CD7D: 00 30         NEG   <$30               ;
CD7F: 03 00         COM   <$00               ;
CD81: 00 03         NEG   <$03               ;
CD83: 03 00         COM   <$00               ;
CD85: 00 03         NEG   <$03               ;
CD87: 30 00         LEAX  0,X                ;
CD89: 33 33         LEAU  -13,Y              ;
CD8B: 33 33         LEAU  -13,Y              ;
CD8D: 30 00         LEAX  0,X                ;
CD8F: 00 00         NEG   <$00               ;
CD91: 33 03         LEAU  3,X                ;
CD93: 03 33         COM   <$33               ;
CD95: 30 30         LEAX  -16,Y              ;
CD97: 30 00         LEAX  0,X                ;
CD99: 30 33         LEAX  -13,Y              ;
CD9B: 33 30         LEAU  -16,Y              ;
CD9D: 30 03         LEAX  3,X                ;
CD9F: 00 00         NEG   <$00               ;
CDA1: 00 00         NEG   <$00               ;
CDA3: 00 00         NEG   <$00               ;
CDA5: 00 00         NEG   <$00               ;
CDA7: 30 00         LEAX  0,X                ;
CDA9: 00 00         NEG   <$00               ;
CDAB: 00 00         NEG   <$00               ;
CDAD: 00 00         NEG   <$00               ;
CDAF: 03 00         COM   <$00               ;
CDB1: 03 33         COM   <$33               ;
CDB3: 33 03         LEAU  3,X                ;
CDB5: 03 30         COM   <$30               ;
CDB7: 00 00         NEG   <$00               ;
CDB9: 33 30         LEAU  -16,Y              ;
CDBB: 30 03         LEAX  3,X                ;
CDBD: 03 03         COM   <$03               ;
CDBF: 03 00         COM   <$00               ;
CDC1: 33 33         LEAU  -13,Y              ;
CDC3: 33 33         LEAU  -13,Y              ;
CDC5: 03 00         COM   <$00               ;
CDC7: 00 00         NEG   <$00               ;
CDC9: 00 30         NEG   <$30               ;
CDCB: 30 00         LEAX  0,X                ;
CDCD: 00 30         NEG   <$30               ;
CDCF: 03 00         COM   <$00               ;
CDD1: 03 34         COM   <$34               ;
CDD3: 03 33         COM   <$33               ;
CDD5: 70 40 33      NEG   $4033              ;
CDD8: 33 07         LEAU  7,X                ;
CDDA: 44            LSRA                     ;
CDDB: 33 33         LEAU  -13,Y              ;
CDDD: 00 04         NEG   <$04               ;
CDDF: 33 30         LEAU  -16,Y              ;
CDE1: 73 40 33      COM   $4033              ;
CDE4: 00 00         NEG   <$00               ;
CDE6: 30 00         LEAX  0,X                ;
CDE8: 00 00         NEG   <$00               ;
CDEA: 03 00         COM   <$00               ;
CDEC: 03 37         COM   <$37               ;
CDEE: 44            LSRA                     ;
CDEF: 33 33         LEAU  -13,Y              ;
CDF1: 00 04         NEG   <$04               ;
CDF3: 33 33         LEAU  -13,Y              ;
CDF5: 70 40 33      NEG   $4033              ;
CDF8: 33 07         LEAU  7,X                ;
CDFA: 44            LSRA                     ;
CDFB: 33 00         LEAU  0,X                ;
CDFD: 30 03         LEAX  3,X                ;
CDFF: 30 00         LEAX  0,X                ;
CE01: 03 30         COM   <$30               ;
CE03: 03 33         COM   <$33               ;
CE05: 00 44         NEG   <$44               ;
CE07: 33 33         LEAU  -13,Y              ;
CE09: 70 04 33      NEG   $0433              ;
CE0C: 33 07         LEAU  7,X                ;
CE0E: 40            NEGA                     ;
CE0F: 33 30         LEAU  -16,Y              ;
CE11: 03 44         COM   <$44               ;
CE13: 33 00         LEAU  0,X                ;
CE15: 00 30         NEG   <$30               ;
CE17: 00 00         NEG   <$00               ;
CE19: 00 03         NEG   <$03               ;
CE1B: 00 03         NEG   <$03               ;
CE1D: 30 04         LEAX  4,X                ;
CE1F: 33 33         LEAU  -13,Y              ;
CE21: 07 40         ASR   <$40               ;
CE23: 33 33         LEAU  -13,Y              ;
CE25: 00 44         NEG   <$44               ;
CE27: 33 33         LEAU  -13,Y              ;
CE29: 70 04 33      NEG   $0433              ;
CE2C: 00 30         NEG   <$30               ;
CE2E: 43            COMA                     ;
CE2F: 30 00         LEAX  0,X                ;
CE31: 03 34         COM   <$34               ;
CE33: 03 33         COM   <$33               ;
CE35: 07 04         ASR   <$04               ;
CE37: 33 33         LEAU  -13,Y              ;
CE39: 00 40         NEG   <$40               ;
CE3B: 33 33         LEAU  -13,Y              ;
CE3D: 70 44 33      NEG   $4433              ;
CE40: 30 03         LEAX  3,X                ;
CE42: 04 33         LSR   <$33               ;
CE44: 00 00         NEG   <$00               ;
CE46: 30 00         LEAX  0,X                ;
CE48: 00 00         NEG   <$00               ;
CE4A: 03 00         COM   <$00               ;
CE4C: 03 30         COM   <$30               ;
CE4E: 40            NEGA                     ;
CE4F: 33 33         LEAU  -13,Y              ;
CE51: 70 44 33      NEG   $4433              ;
CE54: 33 07         LEAU  7,X                ;
CE56: 04 33         LSR   <$33               ;
CE58: 33 00         LEAU  0,X                ;
CE5A: 40            NEGA                     ;
CE5B: 33 00         LEAU  0,X                ;
CE5D: 30 43         LEAX  3,U                ;
CE5F: 30 00         LEAX  0,X                ;
CE61: 06 26         ROR   <$26               ;
CE63: 06 26         ROR   <$26               ;
CE65: 00 66         NEG   <$66               ;
CE67: 66 66         ROR   6,S                ;
CE69: 88 88         EORA  #$88               ;
CE6B: 88 00         EORA  #$00               ;
CE6D: 60 66         NEG   6,S                ;
CE6F: 66 88 86      ROR   $-7A,X             ;
CE72: 00 00         NEG   <$00               ;
CE74: 00 66         NEG   <$66               ;
CE76: 66 93         ROR   [,--X]             ;
CE78: 00 00         NEG   <$00               ;
CE7A: 00 6D         NEG   <$6D               ;
CE7C: 66 00         ROR   0,X                ;
CE7E: 00 00         NEG   <$00               ;
CE80: 00 EF         NEG   <$EF               ;
CE82: 66 00         ROR   0,X                ;
CE84: 00 00         NEG   <$00               ;
CE86: 00 00         NEG   <$00               ;
CE88: 69 00         ROL   0,X                ;
CE8A: 00 00         NEG   <$00               ;
CE8C: 00 00         NEG   <$00               ;
CE8E: 30 00         LEAX  0,X                ;
CE90: 00 00         NEG   <$00               ;
CE92: 02 
CE93: 00 02         NEG   <$02               ;
CE95: 00 06         NEG   <$06               ;
CE97: 66 66         ROR   6,S                ;
CE99: 28 68         BVC   $CF03              ;
CE9B: 08 60         LSL   <$60               ;
CE9D: 66 66         ROR   6,S                ;
CE9F: 86 88         LDA   #$88               ;
CEA1: 88 00         EORA  #$00               ;
CEA3: 00 60         NEG   <$60               ;
CEA5: 66 86         ROR   A,X                ;
CEA7: 69 00         ROL   0,X                ;
CEA9: 00 00         NEG   <$00               ;
CEAB: 66 66         ROR   6,S                ;
CEAD: 30 00         LEAX  0,X                ;
CEAF: 00 00         NEG   <$00               ;
CEB1: DE 66         LDU   <$66               ;
CEB3: 00 00         NEG   <$00               ;
CEB5: 00 00         NEG   <$00               ;
CEB7: F0 66 00      SUBB  $6600              ;
CEBA: 00 00         NEG   <$00               ;
CEBC: 00 00         NEG   <$00               ;
CEBE: 93 00         SUBD  <$00               ;
CEC0: 00 00         NEG   <$00               ;
CEC2: 00 00         NEG   <$00               ;
CEC4: 39            RTS                      ;

CEC5: 00 00         NEG   <$00               ;
CEC7: 00 00         NEG   <$00               ;
CEC9: 0F 66         CLR   <$66               ;
CECB: 00 00         NEG   <$00               ;
CECD: 00 00         NEG   <$00               ;
CECF: ED 66         STD   6,S                ;
CED1: 00 00         NEG   <$00               ;
CED3: 00 00         NEG   <$00               ;
CED5: 66 66         ROR   6,S                ;
CED7: 03 00         COM   <$00               ;
CED9: 00 06         NEG   <$06               ;
CEDB: 66 68         ROR   8,S                ;
CEDD: 96 06         LDA   <$06               ;
CEDF: 66 66         ROR   6,S                ;
CEE1: 68 88 88      ASL   $-78,X             ;
CEE4: 60 66         NEG   6,S                ;
CEE6: 66 83         ROR   ,--X               ;
CEE8: 86 80         LDA   #$80               ;
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
CF00: 66 00         ROR   0,X                ;
CF02: 00 00         NEG   <$00               ;
CF04: 00 D6         NEG   <$D6               ;
CF06: 66 00         ROR   0,X                ;
CF08: 00 00         NEG   <$00               ;
CF0A: 00 66         NEG   <$66               ;
CF0C: 66 39         ROR   -7,Y               ;
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
