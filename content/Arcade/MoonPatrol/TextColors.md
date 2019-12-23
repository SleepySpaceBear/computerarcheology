![Text Colors](MoonPatrol.jpg)

# Text Colors

| ROM      | Size | Content  | Ofs  | CRC      | SHA1                                     |
| -------- | ---- | -------- | ---- | -------- | ---------------------------------------- |
| mpc-4.2a |  512 | tx_pal   |    0 | 07f99284 | dfc52958f2520e1ce4446dd4c84c91413bbacf76 |

```plainCode
; Colors used in color sets:
;
; 01    21 00 00 <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 07    FF 00 00 <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 0F    FF 21 00 <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 28    00 B8 00 <FONT style="BACKGROUND-COLOR:#00B800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 3F    FF FF 00 <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 5C    97 68 51 <FONT style="BACKGROUND-COLOR:#976851">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 67    FF 97 51 <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 87    FF 00 AE <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 91    21 47 AE <FONT style="BACKGROUND-COLOR:#2147AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 9D    B8 68 AE <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; BD    B8 FF AE <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; C8    00 21 FF <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; E8    00 B8 FF <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; FF    FF FF FF <FONT style="BACKGROUND-COLOR:#FFFFFF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>

0000: 00 E8 FF 0F ;  0 ---- <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFFFF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0004: C8 0F 3F C8 ;  1 <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0008: E8 01 0F C8 ;  2 <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
000C: E8 28 87 00 ;  3 <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ----
0010: 00 67 00 5C ;  4 ---- <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#976851">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0014: 67 01 00 00 ;  5 <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- ----
0018: C8 87 01 E8 ;  6 <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
001C: E8 87 00 00 ;  7 <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- ----
0020: 00 FF 00 00 ;  9 ---- <FONT style="BACKGROUND-COLOR:#FFFFFF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- ----
0024: C8 01 0F 00 ;  9 <FONT style="BACKGROUND-COLOR:#0021FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ----
0028: E8 87 00 00 ;  A <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- ----
002C: 9D 87 91 E8 ;  B <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#2147AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0030: 9D 0F 3F 9D ;  C <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0034: E8 01 0F 9D ;  D <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0038: 9D 01 0F 00 ;  E <FONT style="BACKGROUND-COLOR:#B868AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF2100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ----
003C: 00 01 BD E8 ;  F ---- <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0040: 00 67 BD E8 ; 10 ---- <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0044: 00 07 BD E8 ; 11 ---- <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0048: 00 67 BD E8 ; 12 ---- <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
004C: 00 67 BD 01 ; 13 ---- <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8FFAE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0050: 00 67 E8 01 ; 14 ---- <FONT style="BACKGROUND-COLOR:#FF9751">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00B8FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#210000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>

0054: 00 00 00 00 00 00 00 00 00 00 00 00 
0060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
00F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0110: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0130: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0140: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0150: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0160: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0170: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0180: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
0190: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
01F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
```
