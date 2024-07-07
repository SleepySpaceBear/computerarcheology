![GFX2 (Sprites)](Galaga.jpg)

>>> binary roms/2800l.bin + roms/2700k.bin

# Sprite tiles

| ROM       | Size | Ofs  | CRC      | SHA1                                     |
| --------  | ---- | ---- | -------- | ---------------------------------------- |
| 2800l.bin | 4096 |    0 | ad447c80 | e697c180178cabd1d32483c5d8889a40633f7857 |
| 2700k.bin | 4096 |    0 | dd6f1afc | c340ed8c25e0979629a9a1730edc762bd72d0cff |

Sprites are 16x16 pixels built from four 8x8 tiles. These 8x8 tiles have the same 
bits-to-pixel layout as the background tiles. This file is 512 tiles of 8x8 pixels. 
The hardware takes four tiles at a time to make a sprite: 512/4 = 128 sprites (00-7F).

Something is not 100% correct. In my bits-to-pixels, I have a different coding
for the first 32 sprites (128 tiles -- 2K bytes). I haven't found any code in
mame to indicate why.

The sprites are renedered here with an RGB color palette to visualize the individual
pixels.

Several of the sprites are grouped together to make larger pictures. These super groups
are shown later on this page.

```html
<canvas width="1060" height="2100"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getSprite16x16Data"
    data-pixWidth="8"
    data-gridX="16"
    data-gridY="16"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#C00000","#00C000","#0000C0"]'
    data-command=":8x16:00,01,02,03,04,05,06,07,08,09,0A,0B,0C,0D,0E,0F,
                        10,11,12,13,14,15,16,17,18,19,1A,1B,1C,1D,1E,1F,
                        20,21,22,23,24,25,26,27,28,29,2A,2B,2C,2D,2E,2F,
                        30,31,32,33,34,35,36,37,38,39,3A,3B,3C,3D,3E,3F,
                        40,41,42,43,44,45,46,47,48,49,4A,4B,4C,4D,4E,4F,
                        50,51,52,53,54,55,56,57,58,59,5A,5B,5C,5D,5E,5F,
                        60,61,62,63,64,65,66,67,68,69,6A,6B,6C,6D,6E,6F,
                        70,71,72,73,74,75,76,77,78,79,7A,7B,7C,7D,7E,7F">
</canvas>
```

# Player explosion groupings

```html
<canvas width="1060" height="280"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getSprite16x16Data"
    data-pixWidth="8"
    data-gridX="16"
    data-gridY="16"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#DEDEDE","#FF0000","#00FFDE"]'
    data-command=":2x2:22,20,23,21,+x,:2x2:26,24,27,25,+x,:2x2:2A,28,2B,29,+x,:2x2:2E,2C,2F,2D">
</canvas>
```

# Large score groupings

```html
<canvas width="600" height="150"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getSprite16x16Data"
    data-pixWidth="8"
    data-gridX="16"
    data-gridY="16"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#C00000","#00C000","#0000C0"]'
    data-command=":2x1:3E,3C,+x,:2x1:3F,3D">
</canvas>
```

# Alien explosion groupings

```html
<canvas width="600" height="280"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getSprite16x16Data"
    data-pixWidth="8"
    data-gridX="16"
    data-gridY="16"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#C00000","#00C000","#0000C0"]'
    data-command="41,+x,42,+x,:2x2:46,44,47,45">
</canvas>
```

# NAMCO tiles

Sprite 4D is not used in the game. The four tiles it uses are shown here
as the raw 8x8 pixel tiles. These are the same as the "namco" tiles from
the background map (tiles 32, 33, 34, and 35).

```html
<canvas width="600" height="80"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getChar8x8Data"
    data-pixWidth="8"
    data-gridX="8"
    data-gridY="8"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#C00000","#00C000","#0000C0"]'
    data-command=":4x1:134,135,136,137">
</canvas>
```

# Lines

Sprites 4E and 4F are not used in the game. Here are the raw 8x8 pixel tiles:

```html
<canvas width="1000" height="80"  
    data-canvasFunction="TileEngine.handleTileCanvas"
    data-getTileDataFunction="Galaga.getChar8x8Data"
    data-pixWidth="8"
    data-gridX="8"
    data-gridY="8"
    data-pixHeight="8"
    data-gap="0.25"
    data-gridPad="1"
    data-colors='["#000000","#C00000","#00C000","#0000C0"]'
    data-command=":8x1:138,138,13A,13B,13C,13D,13E,13F">
</canvas>
```

# Binary data

```code
0000: 88 CC EE FF BB 99 18 19 11 1D 3F BF FF DF CF E7
0010: 00 06 8E BF FF 7F 7E FD 22 66 EE EE AA 22 02 02
0020: 11 01 01 00 00 00 00 00 77 33 33 33 33 11 11 11
0030: DD 89 89 88 88 00 00 00 00 00 00 00 00 00 00 00
0040: 11 11 33 33 22 02 00 00 00 00 8B 8B EF 77 E7 EB
0050: 00 00 44 CF CF DF FF 7F 00 00 00 11 33 EE EE 44
0060: 00 00 00 00 00 00 00 00 AB 3B 33 77 77 22 22 22
0070: FE EE AA 02 00 00 00 00 04 00 00 00 00 00 00 00
0080: 00 00 00 01 02 00 00 00 44 CC CC CD EF 77 77 DF
0090: 00 00 00 2A EE EF CF FF 00 00 00 00 00 00 11 FF
00A0: 01 00 00 00 00 11 11 00 C7 77 FF FF CC 88 00 00
00B0: FF FF EA 04 00 00 00 00 EE 04 08 00 00 00 00 00
00C0: 00 00 00 00 01 00 00 01 11 33 77 3B 33 77 FB 23
00D0: 00 00 00 0C 9D EE EF FF 00 00 00 88 00 00 08 08
00E0: 00 00 00 00 11 22 00 00 23 77 EE CC 00 00 00 00
00F0: 7F FF 62 44 09 00 00 00 FF EE 44 08 00 00 00 00
0100: 00 00 00 00 00 00 00 00 00 11 13 15 33 77 7B 77
0110: CC 88 88 88 8E BF FF FF 00 00 00 00 00 88 00 08
0120: 00 00 11 33 66 00 00 00 EF EF FF DC 01 00 00 00
0130: EF 7F FF 99 00 01 00 00 08 00 FF EE 08 00 00 00
0140: 00 00 00 00 00 00 00 00 00 00 01 00 10 7F 33 77
0150: 11 77 EE 66 EF CF FF 7F 88 00 00 00 08 08 CC 88
0160: 11 FF 11 00 00 00 00 00 EF FF 88 13 00 00 00 00
0170: 2F FF F7 D9 00 13 00 00 0C 0C 00 CC FF CC 00 00
0180: 00 00 00 00 00 00 00 11 00 00 00 00 17 00 11 FF
0190: 00 3F 00 11 FB F7 FF 9F 00 FF EE CC 88 8E 0E CC
01A0: FF 11 00 00 00 00 00 00 FF FF 11 00 17 00 00 00
01B0: 3F 9F FF F7 FB 11 00 3F FF CC 0E 8E 88 CC EE FF
01C0: 00 00 00 00 00 00 00 11 00 00 00 00 17 00 11 FF
01D0: 00 3F 00 11 FB F7 FF 9F 00 FF EE CC 88 8E 0E CC
01E0: FF 11 00 00 00 00 00 00 FF FF 11 00 17 00 00 00
01F0: 3F 9F FF F7 FB 11 00 3F FF CC 0E 8E 88 CC EE FF
0200: 30 70 43 43 52 61 21 30 00 80 80 80 80 81 C1 F3
0210: 00 00 00 00 00 04 14 FE 60 F0 96 96 D2 B4 A4 E0
0220: 70 10 00 00 00 00 00 00 F3 F3 73 30 43 C3 10 10
0230: FE FE F6 E0 96 96 40 40 F0 C0 00 00 00 80 00 00
0240: 00 00 00 10 10 30 70 30 00 30 70 E0 80 81 A3 F3
0250: 80 A0 10 10 00 14 04 CC 00 00 00 80 C0 C0 C0 C0
0260: 10 10 00 10 30 00 00 00 F7 F7 72 B4 2D 61 10 00
0270: EE FC FC F0 08 48 20 00 C0 C0 A0 00 00 00 00 00
0280: 00 00 10 10 10 10 70 30 40 E0 E0 2C 48 48 C0 C6
0290: 00 00 00 00 00 00 00 18 00 00 00 00 00 E0 E0 2C
02A0: 10 00 10 61 01 10 00 00 F7 FF F7 F3 A4 96 90 00
02B0: 18 F8 F8 F0 70 00 00 00 A4 C0 80 00 00 00 00 00
02C0: 00 00 10 10 00 10 10 00 00 10 30 F0 E0 D1 F3 F7
02D0: 00 E0 F0 80 00 0C 8A CE 00 00 80 40 40 60 60 E0
02E0: 60 01 01 10 00 00 00 00 F7 79 79 16 86 10 10 00
02F0: EE DC F8 F0 60 00 00 00 E0 C0 80 80 C0 00 00 00
0300: 00 00 00 00 10 10 10 00 00 10 21 70 F0 E0 E0 E7
0310: 00 E0 68 68 80 00 00 08 00 00 00 00 00 00 00 00
0320: 60 12 03 70 21 00 00 00 FF FF F7 F2 58 80 80 00
0330: 00 08 F8 C3 F0 C0 40 00 00 E0 78 68 C0 00 00 00
0340: 00 00 00 00 00 40 20 03 00 40 30 70 E0 F1 F7 F7
0350: 00 00 F0 F0 20 00 8E 88 00 00 00 80 C0 20 00 30
0360: 43 30 21 01 10 10 00 00 F3 F7 7B B0 B0 00 00 00
0370: 8E CC 80 F0 F0 E0 40 00 60 E0 C0 80 80 00 00 00
0380: 00 00 00 20 30 03 C3 30 10 10 30 30 70 F7 F7 F3
0390: 30 E1 96 F0 C0 88 8E 88 E0 3C 3C E0 00 00 00 00
03A0: C3 03 30 20 00 00 00 00 F7 F7 70 30 30 10 10 00
03B0: 8E 88 C0 F0 96 E1 30 00 00 00 00 E0 3C 3C E0 00
03C0: 00 00 00 20 30 03 43 30 10 10 30 70 70 F7 F7 F3
03D0: 00 80 F0 F0 10 88 8E 88 00 00 00 80 C0 60 30 00
03E0: 43 03 30 20 00 00 00 00 F7 F7 70 70 30 10 10 00
03F0: 8E 88 10 F0 F0 80 00 00 30 60 C0 80 00 00 00 00
0400: 00 00 00 00 11 33 11 00 00 00 00 44 DC EF FE FE
0410: 00 00 00 11 D1 3F F3 F3 00 00 00 00 CC EE CC 88
0420: 11 33 33 33 00 00 00 00 EF 8B 9B 98 98 00 00 00
0430: 3F 0E 4E 40 40 00 00 00 CC EE EE EE 88 00 00 00
0440: 00 00 00 00 00 00 00 11 00 00 CC CC FE FE 47 CF
0450: 00 00 00 80 D1 F3 3F 7F 00 00 00 00 88 88 00 00
0460: 11 22 22 22 00 00 00 00 70 7C 53 10 00 00 00 00
0470: C4 F3 19 22 22 22 00 00 00 00 00 00 00 00 00 00
0480: 00 00 00 00 00 11 77 77 00 00 11 FF FF FF FE 67
0490: 00 00 00 20 68 2C 97 F3 00 00 00 00 00 88 EE CC
04A0: 77 22 00 00 00 00 00 00 07 47 51 90 20 00 00 00
04B0: 7F 7F 19 33 77 55 00 00 EE 88 88 88 88 00 00 00
04C0: 00 00 00 00 00 00 11 33 00 00 11 33 33 99 FE 12
04D0: 00 00 88 88 70 3C 96 C2 00 00 00 00 00 00 00 CC
04E0: 22 00 00 00 00 00 00 00 0F 47 A3 41 00 11 00 00
04F0: F3 5D 44 66 CC 88 00 00 CC 88 00 00 00 00 00 00
0500: 00 00 00 11 33 11 33 00 00 11 11 FF FF BB 33 07
0510: 00 44 CC EE CC BC 96 C3 00 00 00 00 00 80 00 00
0520: 00 10 00 00 00 00 00 00 C7 03 63 80 11 33 11 00
0530: 7B FF FF 77 EE CC CC 00 CC 88 88 88 00 00 00 00
0540: 00 00 00 00 00 33 00 00 00 00 00 00 66 AA 31 34
0550: 00 00 00 33 FF EE BC 3C 00 00 00 00 00 00 00 80
0560: 00 00 00 00 00 00 00 00 F4 34 72 02 11 EE 00 00
0570: 3C 3F FF BB 88 00 00 00 00 00 CC CC 00 00 00 00
0580: 00 00 00 11 00 00 10 00 00 EE FF FF 11 17 C7 07
0590: 00 22 77 FF FF EE D2 D2 00 00 00 00 88 00 00 00
05A0: 10 00 00 11 00 00 00 00 C7 17 11 FF FF EE 00 00
05B0: D2 EE FF FF 77 22 00 00 00 00 88 00 00 00 00 00
05C0: 00 00 00 11 00 00 00 00 00 00 00 FF 11 17 C7 07
05D0: 00 00 00 77 77 EE D2 D2 00 00 00 88 88 00 00 80
05E0: 00 00 00 11 00 00 00 00 C7 17 11 FF 00 00 00 00
05F0: D2 EE 77 77 00 00 00 00 00 00 88 88 00 00 00 00
0600: 00 00 00 30 30 30 10 00 00 00 00 80 81 D1 C1 E1
0610: 00 00 00 08 0C DC 1C 3C 00 00 00 E0 E0 E0 C0 80
0620: 00 00 00 00 10 00 00 00 71 33 43 A3 00 00 00 00
0630: FC EE 9E AE 88 00 00 00 00 00 00 80 40 00 00 00
0640: 00 00 00 00 00 00 00 00 00 00 60 60 60 60 61 61
0650: 00 00 00 04 0E EE 0E 1C 00 00 00 00 C0 C0 C0 80
0660: 00 00 10 00 00 00 00 00 33 F3 57 13 11 00 00 00
0670: FC FC 0C 6C 10 10 00 00 00 00 00 00 00 00 00 00
0680: 00 00 00 10 10 00 00 00 00 00 C0 E0 C0 E0 D1 E1
0690: 00 00 00 00 00 0C 8E CC 00 00 00 00 00 00 00 60
06A0: 00 10 60 00 00 00 00 00 C3 77 3F BF 47 55 00 00
06B0: 1C 78 F8 C8 80 40 40 00 E0 E0 C0 00 00 00 00 00
06C0: 00 00 00 00 00 00 00 10 00 00 10 30 30 31 61 F7
06D0: 00 80 C0 80 85 CE 6F 3E 00 00 00 00 00 00 40 E0
06E0: 20 00 00 00 00 00 00 00 BF 3F 47 9B 00 10 00 00
06F0: BE F8 C8 80 80 00 00 00 C0 80 00 00 00 00 00 00
0700: 00 00 00 00 00 00 60 10 00 30 70 70 70 60 E1 CF
0710: 00 80 80 00 00 04 8E CE 00 00 00 00 00 00 00 00
0720: 23 01 33 00 00 00 00 00 EF EF 3E 9C 20 40 40 00
0730: 4C A0 F0 F0 10 00 00 00 00 80 C0 C0 80 00 00 00
0740: 00 00 00 00 30 00 00 00 00 00 00 00 30 B0 BF 3F
0750: 00 00 70 F0 80 27 2F 2F 00 00 00 00 00 00 08 00
0760: 11 00 00 00 00 00 00 00 FF 3F 64 20 40 00 00 00
0770: 0C F0 F0 00 00 00 00 00 00 C0 C0 00 00 00 00 00
0780: 00 00 10 00 00 00 00 11 00 00 00 80 50 BE 3F FF
0790: 00 30 70 F0 E0 80 2F 2F 00 80 80 80 00 00 00 08
07A0: 00 00 00 00 10 00 00 00 3F BE 50 80 00 00 00 00
07B0: 2F 80 E0 F0 70 30 00 00 00 00 00 80 80 80 00 00
07C0: 00 00 00 10 00 00 00 11 00 00 00 80 50 BE 3F FF
07D0: 00 00 00 70 F0 80 2F 2F 00 00 00 80 80 00 00 08
07E0: 00 00 00 10 00 00 00 00 3F BE 50 80 00 00 00 00
07F0: 2F 80 F0 70 00 00 00 00 00 00 80 80 00 00 00 00

0800: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 33 46
0810: 00 00 00 00 01 66 22 88 00 33 44 8A 11 76 80 00
0820: 00 11 11 02 11 00 00 00 8A 10 08 08 CC 88 44 88
0830: CC A8 00 00 00 00 10 F0 00 00 00 70 00 10 F0 F0
0840: 00 00 CC 02 99 11 00 00 00 00 33 0C 11 06 10 00
0850: 00 00 00 88 44 02 91 55 00 00 00 00 00 00 00 00
0860: F0 00 10 F0 70 F0 F0 F0 F0 E0 C0 80 E0 E0 C0 F0
0870: 31 31 01 01 22 44 11 20 08 08 8C 8C 88 88 00 00
0880: 00 11 11 00 00 00 00 00 88 04 04 88 A8 44 54 33
0890: 10 00 00 00 00 CC 03 91 F0 10 00 70 00 00 00 08
08A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
08B0: CE 33 00 00 00 00 00 00 54 44 13 00 00 00 00 00
08C0: F0 F0 70 F0 10 00 F0 00 C0 E0 E0 80 C0 E0 F0 11
08D0: 44 44 01 00 20 55 55 2A 00 00 00 88 88 00 00 00
08E0: 00 CE 02 CE 02 11 00 00 20 FF 37 26 04 88 00 00
08F0: 08 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0900: 00 00 22 33 11 00 00 00 00 00 00 00 88 89 CD 03
0910: 00 00 22 33 22 00 11 77 00 00 88 88 04 00 CC FF
0920: 00 00 00 11 00 00 00 11 44 44 91 11 11 77 FF BB
0930: 66 DD FE FD CF 46 CF CD 77 BB EE 8E 0D 0D 01 07
0940: 00 00 00 00 00 77 FF DD 00 00 00 80 22 88 AA 66
0950: 00 00 00 00 00 01 2A 0C 00 00 44 44 88 00 00 00
0960: AA EF 1E 07 07 02 40 0E FF 19 6E 1F 35 1F 3F 33
0970: 00 00 EE FF BB 66 EE CC 00 88 44 00 00 00 00 00
0980: 11 11 00 11 11 00 00 00 D9 BB DD EC CD FF 33 00
0990: 47 8F CE CE CF 8B 66 FF 29 05 08 26 0E 06 1D FF
09A0: 00 00 00 00 11 22 22 00 40 22 DD 99 00 00 00 00
09B0: 66 33 33 11 40 22 22 00 FF 66 99 FF EE 00 00 00
09C0: 84 0A 01 0A 0F 0D 1F C2 3F 1F 35 17 33 3F FF 77
09D0: BB FF 66 BB BB 66 CC 88 00 44 66 44 66 11 00 00
09E0: FF BB 77 FF EE 00 00 00 AA CC CC 88 22 44 00 00
09F0: 33 04 A8 98 44 00 00 00 00 00 00 00 88 44 00 00
0A00: 88 54 22 22 00 33 67 CF 00 00 91 11 FF CC 0B 07
0A10: 22 FF DD 2A 0F 3F 07 0F EE FF 33 1D 0E 8F 0F 03
0A20: CE CD EE 45 EE EF EF FF 1E 2F 4F 0F 0F 07 0E 6D
0A30: CE 87 0D 0E 8F 0F 01 0E 0D 8F 0F 06 00 04 0B 01
0A40: 00 11 BB CC FF 77 1E 87 A2 22 CC 11 99 BB 7F 0C
0A50: 00 01 01 CC EE BF 3F 37 11 22 40 08 40 00 00 00
0A60: 0F 1F 0B 03 09 08 83 0E 0D 0F 0F 09 03 06 05 07
0A70: 3B 2E B7 1F 0D 0F 0F 0F 00 00 66 FF 3F 3F 37 6E
0A80: FF 11 77 FF EE 66 67 67 3D 1F 9B 17 2F 0F 07 5B
0A90: 0F 0D 1A 0F 0E 0D 0F 8F 07 01 0A 04 08 13 07 7F
0AA0: 33 11 00 11 11 33 44 00 8F 8A 23 23 91 00 00 00
0AB0: 6F 0F 07 0B 8C FF 77 00 0F 97 6F 06 3F EE 88 00
0AC0: 0C 08 0B 84 0A 03 0B 0F 01 07 07 1A 03 0B 0E 4D
0AD0: 0B 85 0D 1B 1F 19 66 FF AA 88 88 CC CC 88 00 00
0AE0: 1F 2F 4B 8E 77 FF 00 00 0F 0F 0B FF BB 00 00 00
0AF0: FF CC CC 98 00 40 22 00 00 00 88 88 C8 62 33 11
0B00: 00 00 02 13 11 00 00 00 00 00 00 00 08 09 C1 03
0B10: 00 00 02 03 02 00 11 67 00 00 08 80 40 00 0C 3F
0B20: 00 00 00 11 00 00 00 11 04 04 89 01 01 17 3F 3B
0B30: 06 4D 0F 7C 8F 06 0F 0D 07 0B 0E 0E 0D 0D 01 25
0B40: 00 00 00 00 00 77 0F 4D 00 00 00 80 22 08 AA 06
0B50: 00 00 00 00 00 11 0A 0C 00 00 04 04 80 00 00 00
0B60: 0A 0F 0F 07 07 02 04 0E 2F 09 86 0F 07 0F 0F 03
0B70: 00 00 6E 1F 0B 26 2E 0C 00 88 44 00 00 00 00 00
0B80: 01 10 00 01 01 00 00 00 1D 1A 4D 8E 8D 0F 03 00
0B90: 07 0F 0E 4A 0F 0B 06 0F 0B 05 08 06 0E 06 0D 0F
0BA0: 00 00 00 00 10 22 22 00 04 02 0D 09 00 00 00 00
0BB0: 46 03 03 01 04 22 22 00 0F 06 09 3E CE 00 00 00
0BC0: 0C 28 01 0A 0F 0D 0F 0E 1E 2F 27 07 03 0F 0F 17
0BD0: 0B 4F 66 2B 2B 06 CC 88 00 04 06 04 06 01 00 00
0BE0: 0F 0B 27 87 EE 00 00 00 2A 0C CC 08 02 04 00 00
0BF0: 03 04 0A 09 04 00 00 00 00 00 00 00 80 40 00 00
0C00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 30
0C10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0C20: 00 00 00 00 00 00 00 00 F1 30 00 00 00 00 00 00
0C30: 0F 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0C40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 30
0C50: 00 00 00 00 01 02 04 88 00 00 00 00 00 00 00 00
0C60: 00 00 00 00 00 00 00 00 31 30 40 00 00 00 00 00
0C70: 80 80 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0C80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0C90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0CA0: 00 00 00 00 00 00 00 00 30 F1 30 00 00 00 00 00
0CB0: 00 0F 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0CC0: 00 00 00 00 00 00 00 00 00 00 00 00 20 20 70 72
0CD0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0CE0: 00 00 00 00 00 00 00 00 02 02 02 02 00 00 00 00
0CF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0D00: 00 00 00 00 00 00 00 00 00 77 CC 88 77 00 99 AA
0D10: 00 CC 22 66 CC 00 CC 22 00 00 00 00 00 00 00 00
0D20: 00 00 00 00 00 00 00 00 AA AA EE 00 00 FF 44 00
0D30: 22 22 44 00 22 EE 22 00 00 00 00 00 00 00 00 00
0D40: 00 00 00 00 00 00 00 00 00 07 08 08 07 00 07 08
0D50: 00 0C 02 02 0C 00 0C 02 00 00 00 00 00 00 00 00
0D60: 00 00 00 00 00 00 00 00 08 07 00 00 0F 04 02 01
0D70: 02 0C 00 08 0E 08 08 08 00 00 00 00 00 00 00 00
0D80: 00 00 00 00 00 00 00 00 00 07 08 08 07 00 07 08
0D90: 00 0C 02 02 0C 00 0C 02 00 00 00 00 00 00 00 00
0DA0: 00 00 00 00 00 00 00 00 08 07 00 09 0A 0A 0A 0E
0DB0: 02 0C 00 0C 02 02 02 04 00 00 00 00 00 00 00 00
0DC0: 00 00 00 00 00 00 00 00 00 07 08 08 07 00 07 08
0DD0: 00 0C 02 02 0C 00 0C 02 00 00 00 00 00 00 00 00
0DE0: 00 00 00 00 00 00 00 00 08 07 00 06 09 09 09 06
0DF0: 02 0C 00 0C 02 02 02 0C 00 00 00 00 00 00 00 00
0E00: 00 00 00 00 00 00 00 00 70 80 80 70 00 70 80 80
0E10: C0 20 20 C0 00 C0 20 20 00 00 00 00 00 00 00 00
0E20: 00 00 00 00 00 00 00 00 70 00 70 80 80 70 00 F0
0E30: C0 00 C0 20 20 C0 00 E0 00 00 00 00 00 00 00 00
0E40: 00 00 00 00 00 00 00 00 77 88 88 77 00 77 88 88
0E50: CC 22 22 CC 00 CC 22 22 00 00 00 00 00 00 00 00
0E60: 00 00 00 00 00 00 00 00 77 00 99 AA AA EE 00 FF
0E70: CC 00 CC 22 22 44 00 EE 00 00 00 00 00 00 00 00
0E80: 00 00 00 00 00 00 00 00 07 08 08 07 00 07 08 08
0E90: 0C 02 02 0C 00 0C 02 02 00 00 00 00 00 00 00 00
0EA0: 00 00 00 00 00 00 00 00 07 00 08 09 05 03 00 0F
0EB0: 0C 00 0C 02 02 0C 00 0E 00 00 00 00 00 00 00 00
0EC0: 00 00 00 00 00 10 12 1E 00 00 0F 00 10 76 1E 1E
0ED0: 00 00 0F 1E FE FE FE FE 00 00 1C 1C 10 10 DC FE
0EE0: 3E 1E 12 10 00 00 00 00 DE 1E 1E 76 10 00 0F 00
0EF0: 1E FE FE FE FE 1E 0F 00 1C FE DC 10 10 1C 1C 00
0F00: 00 00 00 00 00 00 00 00 00 00 00 00 00 70 80 80
0F10: 00 00 00 00 00 C0 20 20 00 00 00 00 00 00 00 00
0F20: 00 00 00 00 00 00 00 00 70 00 70 80 80 70 00 70
0F30: C0 00 C0 20 20 C0 00 C0 00 00 00 00 00 00 00 00
0F40: 00 00 00 00 00 00 00 00 00 00 00 00 00 77 88 88
0F50: 00 00 00 00 00 CC 22 22 00 00 00 00 00 00 00 00
0F60: 00 00 00 00 00 00 00 00 77 00 77 88 88 77 00 77
0F70: CC 00 CC 22 22 CC 00 CC 00 00 00 00 00 00 00 00
0F80: 00 00 00 00 00 00 00 00 80 80 70 00 60 90 80 80
0F90: 20 20 C0 00 20 20 A0 60 00 00 00 00 00 00 00 00
0FA0: 00 00 00 00 00 00 00 00 60 00 00 00 00 00 00 00
0FB0: 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0FC0: 00 00 00 00 00 00 00 00 88 88 77 00 88 DD AA 88
0FD0: 22 22 CC 00 CC 22 22 22 00 00 00 00 00 00 00 00
0FE0: 00 00 00 00 00 00 00 00 88 00 00 00 00 00 00 00
0FF0: 44 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1000: 33 77 CC 88 88 77 33 00 88 CC 22 22 66 CC 88 00
1010: 00 00 FF FF 44 00 00 00 22 22 EE EE 22 22 00 00
1020: 66 FF BB 99 99 CC 44 00 22 22 AA AA EE EE 66 00
1030: 88 DD FF BB 99 88 00 00 CC EE 22 22 22 66 44 00
1040: 00 00 00 00 00 00 00 11 00 00 00 00 00 00 22 11
1050: 00 00 00 00 00 00 88 22 00 00 00 00 00 00 00 00
1060: 00 00 00 00 00 00 00 00 57 27 57 88 22 00 00 00
1070: 4C 4C 88 44 88 00 00 00 00 00 00 00 00 00 00 00
1080: 00 00 00 00 10 00 44 11 00 00 02 00 A2 03 AB 05
1090: 00 00 10 B8 44 22 1B 86 00 00 00 00 00 88 00 44
10A0: 00 11 22 10 10 00 00 00 BC 21 65 81 44 22 00 00
10B0: BE 3C B4 54 11 04 00 00 88 80 84 00 00 00 00 00
10C0: 04 00 22 01 44 38 20 44 11 88 74 00 8B 00 44 88
10D0: 22 10 22 89 01 22 88 00 20 80 00 08 08 11 C0 00
10E0: 00 DA 01 03 44 00 11 88 22 C0 00 22 44 10 02 02
10F0: 55 00 15 24 C0 22 00 44 30 20 E9 40 65 00 88 01
1100: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 00
1110: 00 00 11 00 00 00 44 00 00 00 00 00 04 22 88 00
1120: 00 00 00 00 00 00 00 00 00 04 22 11 88 44 00 22
1130: 11 04 00 20 11 00 A8 20 00 C0 81 22 00 00 02 00
1140: 00 00 00 00 04 A2 80 00 00 00 00 00 00 40 40 88
1150: 00 00 00 00 00 00 00 88 00 00 00 00 00 00 00 00
1160: 88 11 22 22 00 00 00 00 11 02 00 C0 00 10 04 44
1170: 00 00 60 00 88 01 00 44 00 00 00 44 00 00 00 00
1180: 00 00 00 00 00 02 00 00 00 80 80 00 11 00 22 00
1190: 22 0C 00 00 60 20 00 22 00 00 00 11 00 00 44 06
11A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
11B0: 80 80 00 00 44 00 00 00 10 00 22 04 00 00 00 00
11C0: 00 22 00 00 00 00 88 00 00 22 15 30 00 88 44 01
11D0: 88 00 11 00 22 00 00 00 00 00 00 00 00 00 00 00
11E0: 82 00 00 44 00 00 00 00 80 40 00 00 00 00 00 00
11F0: 88 00 00 08 00 00 00 00 00 00 00 00 00 00 00 00
1200: 00 44 00 11 00 00 00 00 20 00 00 00 00 00 00 11
1210: 00 00 00 00 40 00 00 00 04 00 00 00 00 00 00 11
1220: 00 44 00 00 00 00 00 08 00 00 00 00 00 40 00 00
1230: 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1240: 00 00 88 C0 00 00 00 00 00 40 00 00 00 00 00 11
1250: 00 00 10 00 00 00 01 00 00 80 00 00 22 00 00 00
1260: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1270: 00 00 11 00 00 00 00 00 00 00 00 00 00 04 00 00
1280: 00 11 00 00 60 00 00 00 00 00 00 00 00 00 44 04
1290: 00 00 88 00 00 00 00 00 00 00 00 00 00 40 00 00
12A0: 00 00 00 10 22 00 00 00 00 00 00 00 00 00 00 00
12B0: 00 00 00 00 88 00 00 00 08 00 00 00 00 10 10 00
12C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
12D0: 00 80 11 00 00 22 00 00 00 00 00 00 00 00 80 00
12E0: 00 00 08 00 00 00 00 00 00 88 00 00 00 00 22 00
12F0: 00 22 00 00 00 00 00 00 00 00 00 00 20 18 00 00
1300: 00 00 00 01 03 01 03 00 00 01 01 0F 0F 0B 03 77
1310: 00 04 0C 0E 0C 7C F6 F3 00 00 00 00 00 80 00 00
1320: 00 10 00 00 00 00 00 00 B7 33 53 80 01 03 01 00
1330: CB 0F 0F 07 0E 0C 0C 00 0C 08 08 08 00 00 00 00
1340: 0F 0C 0C 0F 0F 0C 0C 0F 0F 00 00 0F 0F 00 00 0F
1350: 0C 0C 0C 0F 07 00 00 07 03 03 03 0F 0E 00 00 0F
1360: 0C 0F 07 00 00 0C 0C 0C 03 0F 0E 00 00 03 03 03
1370: 00 00 07 0F 0C 0C 0C 0C 00 00 0E 0F 03 03 03 03
1380: 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
1390: 00 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
13A0: 01 01 01 01 01 01 01 00 01 01 01 01 01 01 01 01
13B0: 00 00 00 01 01 01 01 01 00 00 01 01 01 01 01 01
13C0: 01 01 01 01 01 00 00 00 01 01 01 01 01 01 00 00
13D0: 00 00 00 00 00 01 01 01 00 00 00 01 01 01 01 01
13E0: 01 01 01 00 00 00 00 00 01 01 01 01 01 00 00 00
13F0: 00 00 00 00 00 00 00 01 00 00 00 00 00 00 01 01
1400: 00 00 00 00 00 00 10 30 00 00 11 11 51 D1 D5 FF
1410: 00 00 00 00 40 60 74 FE 00 00 00 00 00 00 00 80
1420: 31 31 20 20 00 00 00 00 EF 2F 07 03 01 00 00 00
1430: FF 9F 0C 08 00 00 00 00 80 80 80 80 00 00 00 00
1440: 00 00 00 00 00 00 10 10 00 00 00 00 20 60 F3 FF
1450: 00 00 44 44 CC 98 BA FF 00 00 00 00 00 00 80 80
1460: 10 30 20 00 00 00 00 00 FF 17 03 03 01 00 00 00
1470: 7F 7F 1F 0C 00 00 00 00 C0 C8 C0 80 80 00 00 00
1480: 00 00 00 00 00 10 10 30 00 00 00 10 F0 F7 FF 77
1490: 00 00 11 B3 22 44 DD 7F 00 00 00 00 00 80 80 80
14A0: 20 00 00 00 00 00 00 00 37 07 03 03 00 00 00 00
14B0: 7F FF 3F 10 10 20 00 00 80 C0 80 80 00 00 00 00
14C0: 00 00 00 00 10 30 20 00 00 00 00 F0 F7 FF 77 37
14D0: 00 00 00 C0 99 AA CC 7F 00 00 00 88 00 00 80 80
14E0: 00 00 00 00 00 00 00 00 27 17 07 00 00 00 00 00
14F0: FF FF 7F 32 30 60 00 00 80 80 80 80 00 00 00 00
1500: 00 00 00 00 10 20 00 00 00 00 20 F0 F7 77 37 27
1510: 00 00 00 E0 CC 99 EE 4C 00 00 00 00 CC 88 00 80
1520: 00 00 00 00 00 00 00 00 1F 1F 03 00 00 10 00 00
1530: FE FE FE 74 E0 80 00 00 80 00 00 00 00 00 00 00
1540: 00 00 00 10 00 00 00 00 00 00 70 F2 77 37 3F 0F
1550: 00 00 00 C0 E8 CC 99 FF 00 00 00 00 00 00 CC 00
1560: 01 00 00 00 00 00 00 00 3F 1F 13 11 30 60 00 00
1570: CC FC E8 C8 C0 00 00 00 00 00 00 00 00 00 00 00
1580: 00 00 00 00 00 00 00 00 00 00 00 F0 33 13 17 3F
1590: 00 00 00 80 C0 E8 FC 88 00 00 00 00 00 00 00 00
15A0: 01 00 00 00 00 00 00 00 0F 3F 17 13 33 F0 00 00
15B0: FF 88 FC E8 C0 80 00 00 CC 00 00 00 00 00 00 00
15C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
15D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
15E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
15F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1600: 00 00 00 00 00 00 00 00 00 00 00 11 11 33 33 3F
1610: 00 00 CC 22 11 88 88 8E 00 00 00 00 00 00 00 00
1620: 01 01 03 02 00 00 00 00 3B 3B 19 28 20 00 00 00
1630: 8B 8B 03 82 80 00 00 00 00 00 08 08 00 00 00 00
1640: 00 00 00 00 00 00 00 01 00 66 99 00 00 11 11 3F
1650: 00 00 00 88 88 88 CC CC 00 00 00 00 00 00 00 00
1660: 03 07 05 00 00 00 00 00 3B 33 22 50 50 00 00 00
1670: 8E 8B 03 07 05 00 00 00 00 00 00 00 00 00 00 00
1680: 00 00 00 00 00 00 01 03 00 00 00 00 00 00 1F 19
1690: 00 00 00 00 33 CC EE CC 00 00 00 00 88 44 44 00
16A0: 05 01 00 00 00 00 00 00 3B 33 62 A0 20 00 00 00
16B0: 8C 8A 06 06 0E 0A 00 00 00 00 00 00 00 00 00 00
16C0: 00 00 00 00 00 00 03 01 00 00 00 00 00 0E 1D 3B
16D0: 00 00 EE 11 11 EE EE EE 00 00 00 00 00 00 00 00
16E0: 01 00 00 00 00 00 00 00 33 73 A0 40 01 00 00 00
16F0: CC 8A 06 0E 0C 04 00 00 00 00 00 00 00 00 00 00
1700: 00 00 00 00 00 03 01 03 00 00 00 00 00 0E 0D 33
1710: 00 00 00 00 00 77 EE EE 00 00 00 00 00 88 44 44
1720: 00 10 00 00 00 00 00 00 33 F7 40 81 03 00 01 00
1730: CC 04 04 0C 0C 08 00 00 00 00 00 00 00 00 00 00
1740: 00 00 00 00 01 00 01 00 00 00 00 00 0E 0F 09 33
1750: 00 00 00 00 00 00 CC FF 00 00 00 00 88 44 44 88
1760: 10 00 10 00 00 00 00 00 B3 77 80 01 07 03 06 00
1770: EE 88 08 08 08 00 00 00 00 00 00 00 00 00 00 00
1780: 00 00 00 00 00 00 00 10 00 00 00 0C 07 0F 00 B3
1790: 00 00 00 00 00 08 08 EE 00 00 00 00 00 00 00 00
17A0: 00 10 00 00 00 00 00 00 77 B3 00 0F 07 0C 00 00
17B0: FF EE 08 08 11 00 00 00 88 44 44 88 00 00 00 00
17C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
17D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
17E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
17F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1800: 00 00 00 02 02 03 03 01 00 00 01 01 01 03 0F 3C
1810: 00 00 00 00 00 09 0F 87 00 00 00 08 08 08 08 00
1820: 01 00 00 00 00 00 00 00 1E 9E CF 67 01 01 00 00
1830: 0F 2E 6E CC 00 00 00 00 00 00 00 00 00 00 00 00
1840: 00 00 01 01 01 01 01 01 00 00 00 00 08 0D 0F 3C
1850: 00 00 08 08 08 0C 0C 87 00 00 00 00 00 04 0C 0C
1860: 00 00 00 00 00 00 00 00 9E 9E CF DF 02 02 00 00
1870: 0F 0F 6E CC 00 00 00 00 08 00 00 00 00 00 00 00
1880: 00 00 00 00 00 00 00 00 00 04 04 0C 0C 0F 0F 9E
1890: 00 00 02 02 04 0C 0C 86 00 00 00 00 00 00 02 0C
18A0: 11 00 00 00 00 00 00 00 9E AD 8F 37 19 00 00 00
18B0: 0F 0F 4E CC 00 00 00 00 0C 08 00 00 00 00 00 00
18C0: 00 00 00 00 00 00 00 11 00 00 02 04 0E 0E 0F AD
18D0: 00 00 00 00 01 02 0C 0C 00 00 00 00 00 00 00 00
18E0: 11 11 11 00 01 00 00 00 1E 2D 8F 4F 77 00 00 00
18F0: 0C 87 0F 8F 88 00 00 00 00 04 08 00 00 00 00 00
1900: 00 00 00 00 00 00 00 00 00 00 01 03 03 07 CF 8F
1910: 00 04 08 08 00 08 0F 86 00 00 00 00 00 0C 00 00
1920: 11 00 00 01 00 00 00 00 9E AD 0F 77 11 00 00 00
1930: 86 0E 0F 8F 00 00 00 00 00 00 0E 08 00 00 00 00
1940: 00 00 00 00 00 00 00 00 00 00 00 01 03 47 CF 8F
1950: 00 00 0E 0C 08 08 0E 87 00 00 00 00 00 00 00 0C
1960: 00 03 00 00 00 00 00 00 BC 0F CF FF 00 00 00 00
1970: 86 84 0E 0F 0F 00 00 00 00 00 00 00 0C 00 00 00
1980: 00 00 00 00 00 00 00 00 00 00 00 00 01 67 CF 8F
1990: 00 00 00 07 0E 0C 0C 86 00 00 00 08 00 00 00 00
19A0: 03 00 00 00 00 00 00 00 3C 8F CF 67 01 00 00 00
19B0: 87 86 0C 0C 0E 07 00 00 0C 00 00 00 00 08 00 00
19C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
19D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
19E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
19F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1A00: 00 00 00 00 00 00 00 01 00 00 10 10 10 10 10 1C
1A10: 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00
1A20: 07 70 F0 00 00 00 00 00 1E F0 D0 10 32 66 00 00
1A30: 0F F0 70 00 88 CC 00 00 0C C0 E0 00 00 00 00 00
1A40: 00 00 00 00 00 00 03 70 00 00 00 00 00 00 0E 1E
1A50: 00 00 40 40 80 80 80 02 00 00 00 00 00 00 00 00
1A60: F0 10 00 00 00 00 00 00 F0 D0 10 64 DD 11 00 00
1A70: 0F C3 70 10 00 88 00 00 00 0C 84 C0 40 00 00 00
1A80: 00 00 00 00 00 02 03 F0 00 00 00 00 00 08 0C 0E
1A90: 00 00 00 10 20 40 C0 80 00 00 00 00 00 00 00 00
1AA0: 30 00 00 00 11 00 00 00 D2 F0 30 A8 EA 22 22 00
1AB0: 00 0E 87 E1 70 30 00 00 00 00 00 08 08 80 80 00
1AC0: 00 00 00 00 03 E1 70 30 00 00 00 00 00 0C 0E 86
1AD0: 00 00 00 00 10 20 40 80 00 00 00 80 00 00 00 00
1AE0: 00 00 11 33 00 00 00 00 D2 21 50 90 CC 88 00 00
1AF0: 00 0C 0E 86 C3 E1 60 20 00 00 00 00 00 00 00 00
1B00: 00 00 00 61 30 30 10 00 00 00 00 08 0C 86 86 C2
1B10: 00 00 00 00 00 10 60 C0 00 00 00 00 80 00 00 00
1B20: 00 77 10 11 11 00 00 00 70 E1 30 B8 10 10 00 00
1B30: 00 08 0C 0E 84 86 80 80 00 00 00 00 00 00 00 00
1B40: 00 00 10 00 00 00 00 22 00 00 86 C2 C3 43 61 21
1B50: 00 00 00 00 00 08 00 70 00 00 00 00 00 00 C0 00
1B60: 33 00 11 11 00 00 00 00 70 90 B8 30 30 10 10 10
1B70: 80 0C 0C 0C 84 84 80 00 00 00 00 00 00 00 00 00
1B80: 00 00 00 00 00 00 22 33 00 40 61 61 61 61 61 21
1B90: 00 00 00 00 08 08 08 00 00 00 00 00 00 00 00 00
1BA0: 10 33 22 00 00 00 00 00 F0 21 61 61 61 61 61 40
1BB0: F0 00 08 08 08 00 00 00 C0 00 00 00 00 00 00 00
1BC0: 00 00 00 00 00 22 66 22 00 00 00 00 00 77 44 77
1BD0: 00 00 00 00 00 CC 11 99 00 00 00 00 00 CC 22 22
1BE0: 22 22 22 77 00 00 00 00 00 00 44 33 00 00 00 00
1BF0: 55 55 55 88 00 00 00 00 22 22 22 CC 00 00 00 00
1C00: 00 00 00 03 21 10 00 00 00 00 00 11 1D 0F 87 E1
1C10: 44 CC CC CC 88 3B 7F 7F 00 00 00 33 FF EE EE 88
1C20: 11 33 77 44 00 00 00 00 F8 FD BB 33 77 77 66 44
1C30: 4E 8E E8 10 00 00 00 00 00 00 00 00 A0 40 A0 10
1C40: 00 00 00 03 21 76 77 11 00 00 00 11 1F 0F C3 E9
1C50: 44 CC CC CC CC 0C 7F 7F 00 00 00 00 00 00 CC FF
1C60: 00 00 00 00 00 00 00 00 30 77 77 FF EE EE CC 88
1C70: F7 B7 60 10 00 00 00 00 FF EE 00 00 A0 40 A0 10
1C80: 00 00 11 03 21 10 00 00 00 00 88 DD 1F 87 F0 70
1C90: 22 77 FF EE CC 88 0C CC 00 00 00 00 00 00 00 00
1CA0: 00 11 11 33 33 22 00 00 FD DD CC 88 00 00 00 00
1CB0: EE FF FF 77 33 00 00 00 00 00 88 88 A8 40 A0 10
1CC0: 00 00 00 03 21 10 00 00 00 00 00 11 1D 0F 87 E1
1CD0: 44 CC CC CC 88 3B 7F 7F 00 00 00 33 FF EE EE 88
1CE0: 11 33 77 44 00 00 00 00 F8 FD BB 33 77 77 66 44
1CF0: 4E 8E E8 10 00 00 00 00 00 00 00 00 A0 40 A0 10
1D00: 00 00 00 03 21 76 77 11 00 00 00 11 1F 0F C3 E9
1D10: 44 CC CC CC CC 0C 7F 7F 00 00 00 00 00 00 CC FF
1D20: 00 00 00 00 00 00 00 00 30 77 77 FF EE EE CC 88
1D30: F7 B7 60 10 00 00 00 00 FF EE 00 00 A0 40 A0 10
1D40: 00 00 11 03 21 10 00 00 00 00 88 DD 1F 87 F0 70
1D50: 22 77 FF EE CC 88 0C CC 00 00 00 00 00 00 00 00
1D60: 00 11 11 33 33 22 00 00 FD DD CC 88 00 00 00 00
1D70: EE FF FF 77 33 00 00 00 00 00 88 88 A8 40 A0 10
1D80: 00 00 00 03 21 10 00 00 00 00 00 11 1D 0F 87 E1
1D90: 44 CC CC CC 88 3B 7F 7F 00 00 00 33 FF EE EE 88
1DA0: 11 33 77 44 00 00 00 00 F8 FD BB 33 77 77 66 44
1DB0: 4E 8E E8 10 00 00 00 00 00 00 00 00 A0 40 A0 10
1DC0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1DD0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1DE0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1DF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1E00: 00 00 60 60 71 71 71 60 12 12 74 FC FD B9 11 71
1E10: 08 08 C4 E6 F7 B3 11 C0 00 00 C0 C0 C0 C0 C0 C0
1E20: 60 14 10 10 10 10 00 00 F0 F1 F3 E7 F3 E1 E1 61
1E30: E0 F0 F8 FC F8 F0 E0 C0 C0 04 00 00 00 00 00 00
1E40: 00 30 30 30 30 71 60 24 00 00 32 FE FE 30 11 F1
1E50: 4A 4A C0 E2 FB FB 33 91 00 00 00 60 60 60 E8 C0
1E60: 10 30 30 30 30 30 10 00 F0 F3 FF DF F7 D2 B4 34
1E70: C0 E0 E0 E8 E0 E0 C0 80 C0 C0 04 00 00 00 00 00
1E80: 00 10 10 30 30 70 04 30 C0 C0 F7 F7 FF 10 E0 F1
1E90: 02 12 E9 F0 F5 FD D9 91 00 08 00 00 00 A8 F8 E8
1EA0: 30 70 F1 70 70 70 01 00 F0 FE FF BF 7D 78 F0 E0
1EB0: D1 C0 D0 E0 C1 C0 80 00 E0 C0 80 80 00 00 00 00
1EC0: 00 00 00 10 30 34 00 30 30 70 E0 F3 F7 44 00 E0
1ED0: 00 00 00 CD F8 F0 F4 F9 00 00 48 84 08 00 88 88
1EE0: 70 F1 F1 F1 F1 D2 34 30 F1 FA FC 7E FE F0 F0 E0
1EF0: 11 91 B3 90 B0 B0 02 00 B8 F8 E0 C0 80 00 00 00
1F00: 00 00 00 00 01 00 30 70 00 10 30 F0 51 80 F0 F0
1F10: 40 E0 C0 EE FF 30 73 F6 00 00 00 02 A4 C3 C0 C4
1F20: 71 F0 F1 C3 34 30 30 00 FC FE 7E FE F4 F0 E0 40
1F30: B9 D1 D1 D1 B0 B0 24 00 CC CC FC F0 E0 80 00 00
1F40: 00 00 00 00 00 30 70 F0 00 00 34 30 00 E0 F0 F8
1F50: 00 70 F0 C4 FF 77 30 B3 00 80 80 00 00 8B F0 C3
1F60: F1 D3 3D 70 70 30 00 00 FE 7E FC FC F0 E0 00 00
1F70: FC B1 91 91 32 F0 68 00 C0 CC 88 88 E0 E0 00 00
1F80: 00 00 00 00 30 70 F0 F1 00 00 12 10 E0 F0 F8 FC
1F90: 00 00 F0 F0 77 33 91 B0 00 00 C0 C0 00 88 CC C3
1FA0: 1F F1 F0 70 30 00 00 00 7E FC F8 F0 E0 10 12 00
1FB0: FF B0 91 33 77 F0 F0 00 F0 C3 CC 88 00 C0 C0 00
1FC0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1FD0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1FE0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
1FF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```html
<script src="galaga.js"></script>
<script src="/js/Binary.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/Canvas.js"></script>
<script>

COL00 = '#808080'
COL01 = '#210000'
COL07 = '#FF0000'
COL0F = '#FF2100'
COL28 = '#00B800'
COL3F = '#FFFF00'
COL5C = '#976851'
COL67 = '#FF9751'
COL87 = '#FF00AE'
COL91 = '#2147AE'
COL9D = '#B868AE'
COLBD = '#B8FFAE'
COLC8 = '#0021FF'
COLE8 = '#00B8FF'
COLFF = '#FFFFFF'

TileEngine.setColorMap(
    {
        '00' : [COL00,COLE8,COLFF,COL0F],
        '01' : [COLC8,COL0F,COL3F,COLC8], 
        '02' : [COLE8,COL01,COL0F,COLC8],
        '03' : [COLE8,COL28,COL87,COL00],       
        '04' : [COL00,COL67,COL00,COL5C],
        '05' : [COL67,COL01,COL00,COL00],
        '06' : [COLC8,COL87,COL01,COLE8],
        '07' : [COLE8,COL87,COL00,COL00],	
        '08' : [COL00,COLFF,COL00,COL00],
        '09' : [COLC8,COL01,COL0F,COL00],
        '0A' : [COLE8,COL87,COL00,COL00],
        '0B' : [COL9D,COL87,COL91,COLE8],
        '0C' : [COL9D,COL0F,COL3F,COL9D],
        '0D' : [COLE8,COL01,COL0F,COL9D],
        '0E' : [COL9D,COL01,COL0F,COL00],        
        '0F' : [COL00,COL01,COLBD,COLE8], 
        '10' : [COL00,COL67,COLBD,COLE8],
        '11' : [COL00,COL07,COLBD,COLE8], 
        '12' : [COL00,COL67,COLBD,COLE8],
        '13' : [COL00,COL67,COLBD,COL01],       
        '14' : [COL00,COL67,COLE8,COL01],      
        '*': ['#808080','#800000','#008000','#000080'], 
    }
  )

</script>
<script>    
    window.onload = function() {  
        Galaga.data = Binary.readBinary('GFX2.md.bin')        
        Galaga.origin = 0
        Canvas.redrawGraphics() 
    }
</script>
```
