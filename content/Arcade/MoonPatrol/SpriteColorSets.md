![Sprite Color Sets](MoonPatrol.jpg)

>>> binary 0000:roms/mpc-2.2h

# Sprite Color Sets

| ROM      | Size | Content  | Ofs  | CRC      | SHA1                                     |
| -------- | ---- | -------- | ---- | -------- | ---------------------------------------- |
| mpc-2.2h |  256 | spr_clut |    0 | 7ae4cd97 | bc0662fac82ffe65f02092d912b2c2b0c7a8ac2b |

The lower 6 bits of the 2nd byte of the sprite structure contains a color-set value.
Thus there could be 64 color-set's (00..3F). The Moon Patrol hardware appears to
mask off the upper bit making 32 color-sets (00..1F) with set 0x20 masking to 0x00.
 
This PROM describes what color values goes in what color sets. There are 8 bytes per color
set, but only the first 4 colors are used (sprite pixels are 2-bits ... 4 colors).

MoonPatrol only defines 16 color sets (00..0F).

Each byte here is an offset into the PROM3 color definition. For instance the first 4 bytes
in the table below describe the 4 colors for color-set-0: 0, 1, 2, 3. Looking these up in
PROM3 yields color values 00 (transparent), 01 (near black), C6 (red/violet), and 
37 (turquoise). Color-set-1 is made of colors values from PROM3 at addresses 0, 4, 2, and 5.

```code
;                  Pixel value:  00   01   10   11 
0000: 00 01 02 03 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C100AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00AEC8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> Color set 0 
0008: 00 04 02 05 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#84C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C100AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 1
0010: 00 05 06 07 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#840000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 2
0018: 00 07 08 09 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#840000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C1C8C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C1C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 3
0020: 00 0A 00 0B 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#845100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#3E3700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 4
0028: 00 00 00 00 00 00 00 00 ; ---- ---- ---- ---- 5
0030: 00 00 00 00 00 00 00 00 ; ---- ---- ---- ---- 6
0038: 00 09 0E 05 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#C1C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#6290C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 7
0040: 00 05 03 0F 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00AEC8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#005100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 8
0048: 00 09 01 05 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#C1C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> 9
0050: 00 01 08 00 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C1C8C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- A
0058: 00 01 05 00 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- B
0060: 00 01 05 03 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00AEC8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> C
0068: 00 04 0D 05 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#84C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C19000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> D
0070: 00 05 00 05 00 00 00 00 ; ---- <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> E
0078: 00 00 05 05 00 00 00 00 ; ---- ---- <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> F
;
; Transparent (not used) here down
;
0080: 00 00 00 00 00 00 00 00 ; 10 
0088: 00 00 00 00 00 00 00 00 ; 11
0090: 00 00 00 00 00 00 00 00 ; 12
0098: 00 00 00 00 00 00 00 00 ; 13
00A0: 00 00 00 00 00 00 00 00 ; 14
00A8: 00 00 00 00 00 00 00 00 ; 15
00B0: 00 00 00 00 00 00 00 00 ; 16
00B8: 00 00 00 00 00 00 00 00 ; 17
00C0: 00 00 00 00 00 00 00 00 ; 18
00C8: 00 00 00 00 00 00 00 00 ; 19
00D0: 00 00 00 00 00 00 00 00 ; 1A
00D8: 00 00 00 00 00 00 00 00 ; 1B
00E0: 00 00 00 00 00 00 00 00 ; 1C
00E8: 00 00 00 00 00 00 00 00 ; 1D
00F0: 00 00 00 00 00 00 00 00 ; 1E
00F8: 00 00 00 00 00 00 00 00 ; 1F
```
