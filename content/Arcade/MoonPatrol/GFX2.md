![Sprite Tiles](MoonPatrol.jpg)

>>> binary roms/mpb-2.3m + roms/mpb-1.3n

# Sprite Tiles

| ROM      | Size | Content  | Ofs  | CRC      | SHA1                                     |
| -------- | ---- | -------- | ---- | -------- | ---------------------------------------- |
| mpb-2.3m | 4096 | sp       |    0 | 707ace5e | 93c682e13e74bce29ced3a87bffb29569c114c3b |
| mpb-1.3n | 4096 | sp       | 1000 | 9b72133a | 1393ef92ae1ad58a4b62ca1660c0793d30a8b5e2 |

The image data is dumped here with ROM mpb-1.3n following mb-2.3m as an 8K block
of bytes. In reality the display generator hardware reads both ROMs as a single
4K block of words. The corresponding bits from each ROM are organized as
two bit planes.

The sprite generator displays 16x16 pixels with 2 bits per pixel. These ROM chips
are bit planes with the most-significant bit of the pair coming from mpb-2.3m 
(0000-0FFFF here). The least-significant bit comes from mpb-1.3n (1000-1FFF here).

These ROMs describe the pixel patterns only. Each hardware sprite structure has a 
one-byte color-set value. Thus a single sprite can only display 4 colors, but each 
sprite can use a different color set.

All of the color sets for the sprites define the first pixel color (bits value 00) 
as color 0, which is transparent. Sprites show through each other as they are drawn
on top of one another. The background shows through if all layers of pixels
are transparent.

There are 128 sprite patterns defined here numbered 00 - 7F.

Most game objects are larger than 16x16 pixels (one sprite). Usually several sprites 
are grouped together to create larger objects. The rendering below shows the image 
numbers in patterns as they are used in the game. The rendering below uses the 
color sets for each object as used in the game.

# Blank Tile 

```html
<canvas width="150" 
        data-canvasFunction="TileEngine.handleTileCanvas"
        data-getTileDataFunction="MoonPatrol.getSprite16x16Data"
        height="150"
        data-pixWidth="8"
        data-gridX="16"
        data-gridY="16"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-colors="CS0"
        data-command="0">
</canvas>
```

# Moon Buggy and 2 Wheel Sizes (2 pictures each) 

```html
<canvas width="900" 
        height="275"
        data-colors="CS0"
        data-command=":2x2:1,2,3,4,+x,+y,+y,+y,+y,+y,+y,+y,+y,5,+x,6,+x,7,+x,8">
</canvas>
```

# Moon Buggy Crashing 

```html
<canvas width="900" 
        height="275"
        data-colors="CS0"
        data-command=":2x2:9,A,B,C,+x,:2x2:D,E,F,10">
</canvas>
```

# Moon Buggy Explosion  

```html
<canvas width="1200" 
        height="275"
        data-colors='CS1'
        data-command=":3x2:11,12,13,14,15,16,+x,:3x2:17,18,19,1A,1B,1C,+x,:3x2:1D,1E,1F,20,21,22">
</canvas><br>
<canvas width="900" 
        height="150"         
        data-command=":2x1:23,24,+x,:2x1:25,26,+x,27">
</canvas>
```

# Player Forward Shot  

```html
<canvas width="900" 
        height="150"         
        data-command="28,+x,29,+x,2A,+x,2B,+x,2C">
</canvas>
```

# Rocks  

```html
<canvas width="900" 
        height="150"
        data-colors='CS4'     
        data-command="2D,+x,2E,+x,2F,+x,30">
</canvas>
```

# Boulders 

```html
<canvas width="900" 
        height="150" 
        data-colors='["#808080","#845100","#808080","#3E3700"]'     
        data-command="31,+x,32,+x,33,+x,34,+x,36,+x,37">
</canvas>
```

# Tank-Shot and Tank  

```html
<canvas width="150" 
        height="150"    
        data-colors="CS0"
        data-command="39">
</canvas>
<canvas width="900" 
        height="150"    
        data-colors='["#808080","#C1C800","#00001A","#C10000"]'    
        data-command="38">
</canvas>
```

# Alien Speeder (and 2 thrust patterns) 

```html
<canvas width="900" 
        height="150"
        data-command="7C,+x,7B,+x,:2x1:3A,3B">
</canvas>
```

# ?? Unknown 

```html
<canvas width="150" 
        height="150"
        data-colors="CS0"
        data-command="3C">
</canvas>
```

# Ground Mine 

```html
<canvas width="150" 
        height="150"
        data-colors='["#808080","#00001A","#C1C8C8","#808080"]'    
        data-command="3D">
</canvas>
```

# Exploding Rocks/Boulders  

```html
<canvas width="900" 
        height="150"
        data-colors="CS1"    
        data-command="3E,+x,3F,+x,40,+x,41">
</canvas>
```

# Alien Ships (3 kinds with rotations)  

```html
<canvas width="900" 
        height="150"
        data-colors='["#808080","#C1C800","#6290C8","#C10000"]'    
        data-command="42,+x,+x,+x,43,+x,44,+x,+x,+x,45,+x,46,+x,47">
</canvas>
```

# Alien Ship Explosion  

```html
<canvas width="900" 
        height="150"
        data-colors="CS1"    
        data-command="48,+x,49,+x,4A">
</canvas>
```

# Alien Ship Shot (bubble alien)  

```html
<canvas width="900" 
        height="150"
        data-colors="CS0"    
        data-command="35">
</canvas>
```

# Alien Ship Shots (fin alien and saucer alien, 3 rotations)  

```html
<canvas width="900" 
        height="150"
        data-colors="CS1"    
        data-command="4B,+x,4C,+x,4D">
</canvas>
```

# Crater-Opening Ground Explosion  

```html
<canvas width="1200" 
        height="375"
        data-colors="CS1"    
        data-command="4E,+x,:2x2:4F,50,51,52,+x,:2x2:53,54,55,56,+x,:2x2:57,58,59,5A,+x,:2x3:5B,5C,5D,5E,5F,60">
</canvas>
```

# Alien Shot Hitting Ground  

```html
<canvas width="1000" 
        height="275"    
        data-colors='["#808080","#840000","#C1C8C8","#C1C800"]'     
        data-command="61,+x,62,+x,63,+x,:2x2:64,65,66,67,+x,:2x2:68,69,6A,6B">
</canvas>
```

# ?? Rubble  

```html
<canvas width="900" 
        height="275"
        data-colors="CS3"    
        data-command=":1x2:6C,6D,+x,:1x2:6E,6F">
</canvas>
```

# Space Plant (3 bases and 4 leaves)  

```html
<canvas width="265" 
        height="150"    
        data-colors='["#808080","#C10000","#00AEC8","#005100"]'     
        data-command=":2x1:78,79">
</canvas>
<canvas width="600" 
        height="150"    
        data-colors="CS8"     
        data-command=":2x1:71,72,+x,:2x1:76,77">
</canvas><br>
<canvas width="600" 
        height="150"    
        data-colors='["#808080","#C10000","#00C800","#840000"]'     
        data-command="70,+x,73,+x,74,+x,75">
</canvas>
```

# Shot Hitting Shot  

```html
<canvas width="500" 
        height="150"
        data-colors="CS1"    
        data-command="7A">
</canvas>
```

# Score Indicators 

 Changing color sets changes value. Very clever.[[br]]
 Shown here will all pixels visible.

```html
<canvas width="500" 
        height="150"
        data-colors="CS0"
        data-command="7D,+x,7E">
</canvas>
```

# Score Indicators (Color Set 0E)  

```html
<canvas width="500" 
        height="150"
        data-colors='["#808080","#C10000","#808080","#C10000"]'
        data-command="7D,+x,7E">
</canvas>
```

# Score Indicators (Color Set 0F)  

```html
<canvas width="500" 
        height="150"
        data-colors='["#808080","#808080","#C10000","#C10000"]'
        data-command="7D,+x,7E">
</canvas>
```

Each sprite is laid out in 32 bytes (256 pixels, 16*16=256) in each of the two ROMs.
The data is organized as four 8x8 pixel blocks. The first 8 bytes define the upper
left block within the sprite. The second 8 bytes define the lower left block within
the sprite. The third 8 bytes define the upper right and the fourth 8 bytes define
the lower right. I'll describe these quadrants as A, B, C, and D (lettered in order
of memory) as follows:

```
AC
BD
```

The most significant bit of the data goes to the left on the screen. The least
significant goes to the right. The first byte in an 8-byte quadrant goes on the
top row. The last byte in an 8-byte quadrant goes on the last row.

The bit planes are combined to form a 2-bit value for each pixel. This value
picks one of 4 colors from the color set. The color-sets are defined in PROM4,
and each byte in the color-set is an index to the actual color in PROM3. Thus
PROM3 defines all the possible colors and PROM4 organizes them four at a time
into sets of colors. Each sprite picks which set it wants to use, and the 2-bit
pixel number combined from the bit-planes here pick the pixel color from the
set.

Remember: this is all in hardware, and the lookups are very fast.

Color bits ... bB : "b" from lower bank (0xxx) and "B" from upper bank (1xxx)

Using color-set-0 as an example, bB:

```
 00 PROM3:0000 (00) transparent
 01 PROM3:0001 (01) black
 10 PROM3:0002 (C6) violet/red
 11 PROM3:0003 (37) turquoise
```

To describe the data layout, I am numbering the pixels as they
appear on the screen as follows:

```
 Aa7 Aa6 Aa5 Aa4 Aa3 Aa2 Aa1 Aa0   Ca7 Ca6 Ca5 Ca4 Ca3 Ca2 Ca1 Ca0
 Ab7 Ab6 Ab5 Ab4 Ab3 Ab2 Ab1 Ab0   Cb7 Cb6 Cb5 Cb4 Cb3 Cb2 Cb1 Cb0
 Ac7 Ac6 Ac5 Ac4 Ac3 Ac2 Ac1 Ac0   Cc7 Cc6 Cc5 Cc4 Cc3 Cc2 Cc1 Cc0
 Ad7 Ad6 Ad5 Ad4 Ad3 Ad2 Ad1 Ad0   Cd7 Cd6 Cd5 Cd4 Cd3 Cd2 Cd1 Cd0
 Ae7 Ae6 Ae5 Ae4 Ae3 Ae2 Ae1 Ae0   Ce7 Ce6 Ce5 Ce4 Ce3 Ce2 Ce1 Ce0
 Af7 Af6 Af5 Af4 Af3 Af2 Af1 Af0   Cf7 Cf6 Cf5 Cf4 Cf3 Cf2 Cf1 Cf0
 Ag7 Ag6 Ag5 Ag4 Ag3 Ag2 Ag1 Ag0   Cg7 Cg6 Cg5 Cg4 Cg3 Cg2 Cg1 Cg0
 Ah7 Ah6 Ah5 Ah4 Ah3 Ah2 Ah1 Ah0   Ch7 Ch6 Ch5 Ch4 Ch3 Ch2 Ch1 Ch0

 Ba7 Ba6 Ba5 Ba4 Ba3 Ba2 Ba1 Ba0   Da7 Da6 Da5 Da4 Da3 Da2 Da1 Da0
 Bb7 Bb6 Bb5 Bb4 Bb3 Bb2 Bb1 Bb0   Db7 Db6 Db5 Db4 Db3 Db2 Db1 Db0
 Bc7 Bc6 Bc5 Bc4 Bc3 Bc2 Bc1 Bc0   Dc7 Dc6 Dc5 Dc4 Dc3 Dc2 Dc1 Dc0
 Bd7 Bd6 Bd5 Bd4 Bd3 Bd2 Bd1 Bd0   Dd7 Dd6 Dd5 Dd4 Dd3 Dd2 Dd1 Dd0
 Be7 Be6 Be5 Be4 Be3 Be2 Be1 Be0   De7 De6 De5 De4 De3 De2 De1 De0
 Bf7 Bf6 Bf5 Bf4 Bf3 Bf2 Bf1 Bf0   Df7 Df6 Df5 Df4 Df3 Df2 Df1 Df0
 Bg7 Bg6 Bg5 Bg4 Bg3 Bg2 Bg1 Bg0   Dg7 Dg6 Dg5 Dg4 Dg3 Dg2 Dg1 Dg0
 Bh7 Bh6 Bh5 Bh4 Bh3 Bh2 Bh1 Bh0   Dh7 Dh6 Dh5 Dh4 Dh3 Dh2 Dh1 Dh0
```

These individual pixes map to bits in the data as follow for Image 0

```code
; Image 0 (bit plane 0 ... see 1000 for bit plane 1)
;                    First byte: (MSB) Aa7_Aa6_Aa5_Aa4_Aa3_Aa3_Aa1_Aa0 (LSB)
0000: 00 00 00 00 00 00 00 00  ; Aa* Ab* Ac* Ad* Ae* Af* Ag* Ah* 
0008: 00 00 00 00 00 00 00 00  ; Ba* Bb* Bc* Bd* Be* Bf* Bg* Bh* 
0010: 00 00 00 00 00 00 00 00  ; Ca* Cb* Cc* Cd* Ce* Cf* Cg* Ch* 
0018: 00 00 00 00 00 00 00 00  ; Da* Db* Dc* Dd* De* Df* Dg* Dh*
 
;  Image 1 (bit plane 0 ... see 1020 for bit plane 1)
0020: 00 00 00 00 00 00 00 00 ; 
0028: 00 00 00 00 00 00 00 0E ; 
0030: 00 00 00 00 00 40 40 40 ; 
0038: 40 40 40 41 43 4F 47 0F ;
 
; Image 2 (bit plane 0 ... see 1040 for bit plane 1)
0040: 00 00 00 00 00 00 00 00 ; 
0048: 00 00 7E FF FF FF FF FF ; 
0050: 00 00 00 00 00 00 00 00 ; 
0058: 00 00 00 00 80 C0 F0 01 ;
 
0060: 3F 7F FF FF FF FF FF 7F ; 
0068: 00 00 00 00 00 00 00 00 ; 
0070: FF FF FF FF FF FF FF FF ; 
0078: 00 00 00 00 00 00 00 00 ; 
0080: FC FF FF FF FF FF FF FF ; 
0088: 00 00 00 00 00 00 00 00 ; 
0090: 0D E1 FC FC FC FC F8 F8 ; 
0098: 00 00 00 00 00 00 00 00 ; 
00A0: 08 40 02 18 98 19 00 24 ; 
00A8: 00 00 00 00 00 00 00 00 ; 
00B0: 00 00 00 00 00 00 00 00 ; 
00B8: 00 00 00 00 00 00 00 00 ; 
00C0: 10 02 40 18 19 98 00 42 ; 
00C8: 08 00 00 00 00 00 00 00 ; 
00D0: 00 00 00 00 00 00 00 00 ; 
00D8: 00 00 00 00 00 00 00 00 ; 
00E0: 00 00 48 00 30 B4 00 48 ; 
00E8: 00 00 00 00 00 00 00 00 ; 
00F0: 00 00 00 00 00 00 00 00 ; 
00F8: 00 00 00 00 00 00 00 00 ; 
0100: 00 20 00 00 B4 30 00 00 ; 
0108: 10 00 00 00 00 00 00 00 ; 
0110: 00 00 00 00 00 00 00 00 ; 
0118: 00 00 00 00 00 00 00 00 ; 
0120: 00 00 00 00 00 00 00 00 ; 
0128: 00 04 04 02 02 01 00 00 ; 
0130: 00 00 00 00 00 03 03 0F ; 
0138: 0F 0F 0F 1F 3F 1F 9F BF ; 
0140: 00 00 00 7C FF FF FC F8 ; 
0148: F3 F7 FF FE FE FC FE FE ; 
0150: 00 00 10 98 88 00 10 B8 ; 
0158: F8 F8 F0 30 10 00 10 00 ; 
0160: 00 01 0F 1F 1F 3E 3C 3C ; 
0168: 38 18 1C 00 00 00 00 00 ; 
0170: 3C 7C F0 F0 F8 B0 10 02 ; 
0178: 90 00 00 00 40 00 00 00 ; 
0180: FC 30 20 20 00 00 40 00 ; 
0188: 00 00 00 00 00 00 00 00 ; 
0190: 00 80 00 00 00 00 00 00 ; 
0198: 00 00 00 00 00 00 00 00 ; 
01A0: 00 00 00 00 00 00 0F 1F ; 
01A8: 3F 3F 15 00 20 0C 0C 20 ; 
01B0: 00 00 00 02 04 04 08 10 ; 
01B8: C0 E3 FB FF FF FF F3 F0 ; 
01C0: 00 00 00 00 00 00 00 00 ; 
01C8: 30 7C FF FF FF FF FF FF ; 
01D0: 00 00 00 00 00 00 00 00 ; 
01D8: 00 00 00 C0 C0 C0 E0 E0 ; 
01E0: 00 02 00 00 00 00 00 00 ; 
01E8: 00 00 00 00 00 00 00 00 ; 
01F0: 20 0C 2C 00 01 08 00 00 ; 
01F8: 00 00 00 00 00 00 00 00 ; 
0200: FD FC 7F FF FF 7F 3F 18 ; 
0208: 00 03 0B 00 00 02 00 00 ; 
0210: C0 70 10 80 84 CC E8 F0 ; 
0218: 60 20 40 00 00 00 00 00 ; 
0220: 00 00 00 00 00 00 00 00 ; 
0228: 00 00 00 00 00 00 00 00 ; 
0230: 00 00 00 00 00 00 00 00 ; 
0238: 00 00 00 00 03 0F 3F 7F ; 
0240: 00 00 00 20 20 20 E0 E0 ; 
0248: E0 41 E3 EF FF FF FF FF ; 
0250: 00 00 00 00 00 00 00 00 ; 
0258: 7F FF FF FF FF FF FF FF ; 
0260: 00 00 00 00 00 00 00 00 ; 
0268: 00 00 80 C0 F0 FF FF FF ; 
0270: 00 00 00 00 00 00 00 00 ; 
0278: 00 00 00 00 00 00 00 00 ; 
0280: 00 00 00 00 00 00 00 00 ; 
0288: 00 00 00 00 00 00 00 00 ; 
0290: FF FF FF FF FF 7F 7F 3F ; 
0298: 3F 0C 00 00 00 00 00 00 ; 
02A0: FF FF FF FF FF FF BF 1F ; 
02A8: 1F 06 00 00 00 00 00 00 ; 
02B0: FF FF FF FF FF FF C3 81 ; 
02B8: 81 00 00 00 00 00 00 00 ; 
02C0: FC FC FC FC F8 F8 F0 E0 ; 
02C8: E0 C0 00 00 00 00 00 00 ; 
02D0: 00 00 00 00 00 00 00 00 ; 
02D8: 00 00 00 00 00 00 00 00 ; 
02E0: 00 00 00 00 00 00 00 03 ; 
02E8: 00 00 00 00 00 00 03 1D ; 
02F0: 00 01 02 12 11 09 CD 67 ; 
02F8: 37 7F 7F 33 60 E0 C0 C7 ; 
0300: 04 08 08 10 10 38 B8 FD ; 
0308: FF CF 83 02 00 00 60 F9 ; 
0310: 02 84 44 44 42 66 F7 FF ; 
0318: FF C8 00 00 18 7D FF FF ; 
0320: 00 00 04 04 08 18 70 E1 ; 
0328: FB 7F 3E 0F 07 C3 E3 E1 ; 
0330: 00 00 00 00 00 10 60 80 ; 
0338: 00 00 60 98 00 80 C0 F0 ; 
0340: 00 00 00 01 01 03 06 08 ; 
0348: 00 00 00 00 00 00 01 00 ; 
0350: E7 4F 4F C7 E3 B0 18 3E ; 
0358: 3F 37 63 41 41 82 02 00 ; 
0360: FF FF FF CF 87 00 00 4E ; 
0368: FF FF 3B 10 10 20 20 20 ; 
0370: FF FF FF BB 00 00 03 0F ; 
0378: 1F FF EF CB C9 44 44 20 ; 
0380: F1 F3 E3 47 0F 06 07 CF ; 
0388: FD 7C 38 1C 04 02 01 01 ; 
0390: 88 00 80 C0 E0 60 10 80 ; 
0398: C0 C0 20 20 10 00 00 00 ; 
03A0: 00 00 00 00 00 00 00 00 ; 
03A8: 00 02 07 0F 07 0E 1E 1F ; 
03B0: 00 00 01 0B 1F 1F 3F 7E ; 
03B8: FE FC CC 00 00 01 03 07 ; 
03C0: 00 00 C1 F3 FF FF FF 3F ; 
03C8: 19 10 00 00 60 F9 FF FF ; 
03D0: 00 80 C0 F3 FF FF E7 C3 ; 
03D8: 82 00 00 00 E3 CF FF FF ; 
03E0: 00 00 00 B0 F8 FC FE 3E ; 
03E8: 1F 13 01 01 83 C3 C7 83 ; 
03F0: 00 00 00 00 00 00 00 00 ; 
03F8: 80 80 C0 E0 F0 F0 E0 F0 ; 
0400: 1F 0F 1F 0F 07 07 03 01 ; 
0408: 00 00 00 00 00 00 00 00 ; 
0410: 87 C3 80 00 00 82 C7 CF ; 
0418: FF 7F 7F 3F 33 00 00 00 ; 
0420: FF 7F 3F 0D 00 00 00 00 ; 
0428: 83 87 CF FF FF F3 20 00 ; 
0430: FF FF FD D8 00 00 08 0C ; 
0438: 1F 9F FF FE FC 60 00 00 ; 
0440: E1 C1 81 03 27 3F 3F 7F ; 
0448: FE FC F0 E0 60 00 00 00 ; 
0450: F0 E0 E0 C0 C0 80 80 00 ; 
0458: 00 00 00 00 00 00 00 00 ; 
0460: 03 07 07 77 7E 7C F0 E0 ; 
0468: E1 E1 70 70 39 3F 1F 0D ; 
0470: 00 CE FF FF 71 00 68 FF ; 
0478: FF 99 00 00 CF FF F3 80 ; 
0480: 39 FF FF CF 00 00 CF FF ; 
0488: FF CF 00 00 39 FF EF C3 ; 
0490: 80 C0 F0 FC FE 3E 0F 87 ; 
0498: C6 06 0C 0E CE FC F0 30 ; 
04A0: 00 00 00 00 01 07 0F 1F ; 
04A8: 1F 1F 0F 03 01 01 00 00 ; 
04B0: 00 00 00 00 9C FF E7 80 ; 
04B8: 00 91 FF FF F3 C0 00 00 ; 
04C0: 00 00 00 70 FC FF 93 01 ; 
04C8: 00 81 93 FF FB 60 00 00 ; 
04D0: 00 00 00 00 C0 E0 F0 F0 ; 
04D8: F0 F0 E0 E0 40 00 00 00 ; 
04E0: 00 00 00 00 00 0C 3F 70 ; 
04E8: 73 3F 0C 00 00 00 00 00 ; 
04F0: 00 00 00 00 00 F0 BC 0E ; 
04F8: 1E F4 C0 00 00 00 00 00 ; 
0500: 00 00 00 00 00 00 00 20 ; 
0508: 00 00 00 00 00 00 00 00 ; 
0510: 00 00 00 00 00 20 70 F0 ; 
0518: 60 00 00 00 00 00 00 00 ; 
0520: 00 00 00 00 00 00 04 00 ; 
0528: 00 00 00 00 00 00 00 00 ; 
0530: 00 00 00 00 00 60 F0 70 ; 
0538: 20 00 00 00 00 00 00 00 ; 
0540: 00 00 00 00 00 00 00 00 ; 
0548: 00 00 00 00 00 00 00 00 ; 
0550: 00 00 00 00 00 00 00 00 ; 
0558: 00 00 00 00 00 00 00 00 ; 
0560: 00 00 00 00 00 00 00 00 ; 
0568: 00 00 00 00 00 00 00 00 ; 
0570: 00 00 00 00 00 00 60 F0 ; 
0578: F0 60 00 00 00 00 00 00 ; 
0580: 00 00 00 01 03 03 01 03 ; 
0588: 03 01 01 00 00 00 00 00 ; 
0590: 00 00 B0 F8 FC FC FE FC ; 
0598: FC FC F8 98 00 00 00 00 ; 
05A0: 00 00 00 00 00 00 00 00 ; 
05A8: 00 08 08 18 28 00 02 26 ; 
05B0: 00 00 00 00 00 00 00 00 ; 
05B8: 00 00 00 00 00 00 00 00 ; 
05C0: 00 00 00 00 02 00 08 00 ; 
05C8: 01 03 06 80 10 21 00 00 ; 
05D0: 00 00 00 00 00 60 E0 E0 ; 
05D8: E0 20 30 70 D0 18 3C 1C ; 
05E0: 00 03 00 00 04 08 08 00 ; 
05E8: 00 00 04 08 00 82 C0 80 ; 
05F0: 00 C0 E0 60 70 20 60 50 ; 
05F8: 10 30 20 30 30 78 3C 7E ; 
0600: 07 07 03 07 09 01 02 02 ; 
0608: 04 00 00 04 08 00 00 00 ; 
0610: 00 00 80 80 80 80 E0 30 ; 
0618: 30 50 10 28 48 00 00 00 ; 
0620: 00 00 00 00 00 00 00 00 ; 
0628: 02 01 00 00 00 00 00 00 ; 
0630: 00 00 00 00 00 00 00 00 ; 
0638: 00 00 00 00 00 00 00 00 ; 
0640: 00 00 00 00 00 00 00 00 ; 
0648: 08 08 04 02 00 00 00 00 ; 
0650: 00 00 00 00 00 00 00 00 ; 
0658: 00 00 00 00 00 00 00 00 ; 
0660: 00 00 00 00 00 00 04 08 ; 
0668: 08 08 00 00 00 00 00 00 ; 
0670: 00 00 00 00 00 00 00 00 ; 
0678: 00 00 00 00 00 00 00 00 ; 
0680: 00 00 00 00 00 03 00 00 ; 
0688: 00 00 00 00 00 00 00 00 ; 
0690: 00 00 00 00 00 80 40 00 ; 
0698: 00 00 00 00 00 00 00 00 ; 
06A0: 00 00 00 00 00 00 01 03 ; 
06A8: 01 00 00 00 00 00 00 00 ; 
06B0: 00 00 00 00 00 00 80 C0 ; 
06B8: 80 00 00 00 00 00 00 00 ; 
06C0: 00 00 00 00 00 00 08 08 ; 
06C8: 08 08 08 04 02 00 00 00 ; 
06D0: 00 00 00 00 00 00 00 00 ; 
06D8: 00 00 00 00 00 00 00 00 ; 
06E0: 00 00 00 03 04 08 00 00 ; 
06E8: 00 00 00 00 00 00 00 00 ; 
06F0: 00 00 00 C0 00 00 00 00 ; 
06F8: 00 00 00 00 00 00 00 00 ; 
0700: 00 00 FE FF 00 00 03 00 ; 
0708: 01 04 31 7B 7B 31 00 00 ; 
0710: 00 00 00 00 00 00 C0 00 ; 
0718: 80 20 8C DE DE 8C 00 00 ; 
0720: 00 00 00 00 00 00 00 00 ; 
0728: 00 00 00 00 00 00 00 00 ; 
0730: 00 00 00 00 00 00 00 00 ; 
0738: 00 00 00 00 00 00 00 00 ; 
0740: 00 00 00 00 00 00 00 00 ; 
0748: 00 00 00 00 00 00 00 00 ; 
0750: 00 00 00 78 7E 3F 1F 0F ; 
0758: 1F 0F 0F 1F 07 00 00 00 ; 
0760: 00 00 00 00 30 E0 E0 C0 ; 
0768: FF FF FF FF 03 00 00 00 ; 
0770: 00 00 00 00 00 00 00 70 ; 
0778: FC F0 F0 F0 C0 00 00 00 ; 
0780: 00 00 00 00 00 00 00 00 ; 
0788: 00 E0 E0 00 00 00 00 00 ; 
0790: 00 00 00 00 00 00 00 00 ; 
0798: 00 00 00 00 00 00 00 00 ; 
07A0: 78 78 00 00 00 00 00 00 ; 
07A8: 00 00 00 00 00 00 00 00 ; 
07B0: 00 00 00 00 00 00 00 00 ; 
07B8: 00 00 00 00 00 00 00 00 ; 
07C0: 00 00 00 00 00 00 01 01 ; 
07C8: 01 00 00 00 00 00 00 00 ; 
07D0: 00 00 00 00 00 00 80 C0 ; 
07D8: C0 80 00 00 00 00 00 00 ; 
07E0: 00 00 00 00 00 01 03 07 ; 
07E8: 07 03 01 00 00 00 00 00 ; 
07F0: 00 00 00 00 00 80 80 C0 ; 
07F8: C0 C0 80 00 00 00 00 00 ; 
0800: 00 03 0F 1E 38 71 73 27 ; 
0808: 67 63 70 60 39 1F 06 00 ; 
0810: 00 C0 F0 7C 1C 8E C6 E4 ; 
0818: E4 CE 86 0C BC F8 C0 00 ; 
0820: 06 0F 3F 32 70 46 CF CF ; 
0828: 87 CF 66 E0 70 3C 1F 07 ; 
0830: C0 F0 9C 0C 46 E2 F3 E2 ; 
0838: F7 F7 C3 06 06 DC F8 B0 ; 
0840: 00 00 00 00 01 07 0F 0F ; 
0848: 03 00 00 38 00 00 00 00 ; 
0850: 00 00 00 00 00 C0 E0 E0 ; 
0858: 80 00 00 38 00 00 00 00 ; 
0860: 00 01 03 07 07 07 03 05 ; 
0868: 18 3C 7E 7F 7E 3C 18 00 ; 
0870: 00 80 C0 E0 E0 E0 C0 A0 ; 
0878: 18 3C 7E FE 7E 3C 18 00 ; 
0880: 00 00 00 00 18 3D 7E 7E ; 
0888: 7E 3C 1A 01 00 00 00 00 ; 
0890: 30 78 FC FC FC 78 30 10 ; 
0898: 10 30 78 FC FC FC 78 30 ; 
08A0: 00 00 00 00 00 00 00 00 ; 
08A8: 1C 03 00 00 00 00 00 00 ; 
08B0: 00 00 00 00 00 00 00 00 ; 
08B8: 00 00 00 00 00 00 00 00 ; 
08C0: 00 00 00 00 00 00 00 00 ; 
08C8: 0C 03 00 00 00 00 00 00 ; 
08D0: 00 00 00 00 00 00 00 00 ; 
08D8: 00 80 00 00 00 00 00 00 ; 
08E0: 00 00 00 00 00 00 00 00 ; 
08E8: 04 03 00 00 00 00 00 00 ; 
08F0: 00 00 00 00 00 00 00 00 ; 
08F8: 00 C0 00 00 00 00 00 00 ; 
0900: 00 00 00 09 04 02 00 20 ; 
0908: C0 18 23 02 04 00 00 00 ; 
0910: 00 00 80 00 10 60 C0 40 ; 
0918: 00 10 00 50 40 20 00 00 ; 
0920: 00 00 00 20 11 09 24 00 ; 
0928: 20 0A 1A 23 49 11 02 00 ; 
0930: 00 00 40 80 8C 10 60 00 ; 
0938: 08 40 A0 10 40 20 00 00 ; 
0940: 02 81 24 32 08 00 B8 6C ; 
0948: 00 02 07 1D 20 40 89 10 ; 
0950: 02 20 88 B0 E1 74 38 10 ; 
0958: 40 E0 7C D2 88 84 00 10 ; 
0960: 00 00 00 00 00 00 01 03 ; 
0968: 01 00 00 00 00 00 00 00 ; 
0970: 00 00 00 00 00 00 80 E0 ; 
0978: 80 00 00 00 00 00 00 00 ; 
0980: 00 00 00 00 00 04 03 03 ; 
0988: 03 00 00 00 00 00 00 00 ; 
0990: 00 00 00 00 00 00 80 80 ; 
0998: 80 40 00 00 00 00 00 00 ; 
09A0: 00 00 00 00 00 05 03 03 ; 
09A8: 03 01 01 00 00 00 00 00 ; 
09B0: 00 00 00 00 00 40 80 80 ; 
09B8: 80 00 00 00 00 00 00 00 ; 
09C0: 00 14 0F 5C 30 E0 40 C0 ; 
09C8: 00 00 00 00 00 00 00 00 ; 
09D0: 00 A0 C0 E4 38 0D 06 07 ; 
09D8: 00 00 00 00 00 00 00 00 ; 
09E0: 00 00 00 00 00 00 00 00 ; 
09E8: 00 00 00 00 01 00 01 05 ; 
09F0: 00 00 00 00 00 00 00 00 ; 
09F8: 04 02 4F 2F 39 F0 C0 80 ; 
0A00: 00 00 00 00 00 00 00 00 ; 
0A08: 20 C0 F4 FE 9F 0F 03 01 ; 
0A10: 00 00 00 00 00 00 00 00 ; 
0A18: 00 00 00 80 00 00 C0 D0 ; 
0A20: 03 07 07 06 0E 00 00 00 ; 
0A28: 00 00 00 00 00 00 00 00 ; 
0A30: 00 00 00 00 00 00 00 00 ; 
0A38: 00 00 00 00 00 00 00 00 ; 
0A40: 00 00 00 00 00 00 00 00 ; 
0A48: 00 00 00 00 00 00 00 00 ; 
0A50: E0 60 70 38 18 00 00 00 ; 
0A58: 00 00 00 00 00 00 00 00 ; 
0A60: 00 00 00 00 00 04 02 02 ; 
0A68: 01 00 20 14 03 07 07 53 ; 
0A70: 04 04 40 42 22 20 04 02 ; 
0A78: 57 3F 3F FF F9 F0 E0 C0 ; 
0A80: 10 00 20 22 02 04 44 20 ; 
0A88: 60 FB FF 7F 1F 0B 02 00 ; 
0A90: 00 00 00 00 00 00 10 20 ; 
0A98: 80 00 20 C4 C8 C0 E0 EA ; 
0AA0: 0F 0E 1E 1E 3C 00 00 00 ; 
0AA8: 00 00 00 00 00 00 00 00 ; 
0AB0: 80 00 00 00 00 00 00 00 ; 
0AB8: 00 00 00 00 00 00 00 00 ; 
0AC0: 00 00 00 00 00 00 00 00 ; 
0AC8: 00 00 00 00 00 00 00 00 ; 
0AD0: F0 7C FC 3C 1E 00 00 00 ; 
0AD8: 00 00 00 00 00 00 00 00 ; 
0AE0: 00 00 00 00 00 00 00 09 ; 
0AE8: 05 07 07 0F 0F 1F 1F 7F ; 
0AF0: 08 04 0D 8F 5F FF FF FF ; 
0AF8: FF FF FF FF FF FF FF FF ; 
0B00: 20 40 E0 F8 FC FE FF FF ; 
0B08: FF FF FF FF FF FF FF FF ; 
0B10: 00 00 00 00 00 40 80 90 ; 
0B18: E0 E0 E0 F4 F8 F8 F8 FC ; 
0B20: 3F 3F 3F 1F 7F 03 01 00 ; 
0B28: 00 00 00 00 00 00 00 00 ; 
0B30: FF FE F7 FA F0 E0 F8 FD ; 
0B38: FB 7F 5F 1F 0F 03 01 01 ; 
0B40: FF FF 6F 5F 0F 1F 3F 3E ; 
0B48: 5E F4 F0 E0 C0 80 80 00 ; 
0B50: F8 FC FC FE FE C0 C0 80 ; 
0B58: 00 00 00 00 00 00 00 00 ; 
0B60: 00 00 00 00 00 00 00 00 ; 
0B68: 00 04 03 03 01 03 43 27 ; 
0B70: 00 00 00 01 00 01 21 13 ; 
0B78: 1B 1F 1F BF FF FF FF FF ; 
0B80: 00 00 00 00 00 04 08 98 ; 
0B88: D8 FE FE FF FF FF FF FF ; 
0B90: 00 00 00 00 00 00 00 00 ; 
0B98: 00 10 20 60 E0 C0 E0 F2 ; 
0BA0: 3F 1F 1F 1F 1F 1F BF 7F ; 
0BA8: 7F 3F 7F 7F 7F 7F FF FC ; 
0BB0: FF FF FF FF FF FF FF FF ; 
0BB8: FF FE FC F0 D0 C0 80 00 ; 
0BC0: FF FF FF FF FF FF FF FF ; 
0BC8: FF FF 9F 0F 01 00 00 00 ; 
0BD0: F4 FC F8 F8 FD FE FC FC ; 
0BD8: FD FE FE FE FE 7F 3F 0F ; 
0BE0: 70 20 00 00 00 00 00 00 ; 
0BE8: 00 00 00 00 00 00 00 00 ; 
0BF0: 00 00 00 00 00 00 00 00 ; 
0BF8: 00 00 00 00 00 00 00 00 ; 
0C00: 00 00 00 00 00 00 00 00 ; 
0C08: 00 00 00 00 00 00 00 00 ; 
0C10: 04 00 00 00 00 00 00 00 ; 
0C18: 00 00 00 00 00 00 00 00 ; 
0C20: 00 00 00 00 20 10 10 40 ; 
0C28: 21 13 1F 3F 1F 3F 3F 1D ; 
0C30: 00 00 00 50 00 20 20 40 ; 
0C38: C0 C0 F0 F9 FA FC F8 DC ; 
0C40: 00 00 00 00 01 01 81 03 ; 
0C48: 47 67 F7 FB 7F 7F 3F 7B ; 
0C50: 80 00 80 80 00 80 80 C8 ; 
0C58: E0 E2 C4 EC DE FE FE CC ; 
0C60: 00 04 00 00 00 40 40 21 ; 
0C68: 3D 9F 7F FF FF FF 7B 39 ; 
0C70: 00 00 04 00 00 00 C0 E1 ; 
0C78: F0 F8 FE FF FF FF FF 46 ; 
0C80: 00 00 00 00 00 00 00 00 ; 
0C88: 00 00 00 00 00 00 00 00 ; 
0C90: 00 00 00 00 00 00 00 00 ; 
0C98: 00 00 00 10 00 04 02 12 ; 
0CA0: 00 00 00 00 00 00 00 00 ; 
0CA8: 00 00 00 00 00 00 00 08 ; 
0CB0: 00 00 00 00 00 00 00 00 ; 
0CB8: 00 00 00 00 00 00 00 00 ; 
0CC0: 00 00 00 00 08 07 01 00 ; 
0CC8: 10 29 07 07 03 03 01 00 ; 
0CD0: 11 09 8B 4F 2F BF FF FF ; 
0CD8: FF FF FF FF F7 FB FB 71 ; 
0CE0: 10 10 B2 F4 F9 FA FE FC ; 
0CE8: FE FE FE FF F7 EF CF 9E ; 
0CF0: 00 00 00 00 00 00 00 00 ; 
0CF8: 00 00 00 00 00 00 00 00 ; 
0D00: 00 00 00 00 00 00 00 00 ; 
0D08: 00 00 00 00 00 00 00 00 ; 
0D10: 00 00 00 00 00 00 00 20 ; 
0D18: 10 10 10 08 08 89 45 45 ; 
0D20: 00 00 00 00 00 00 00 00 ; 
0D28: 40 40 80 80 88 11 22 64 ; 
0D30: 00 00 00 00 00 00 00 00 ; 
0D38: 00 00 00 00 00 00 00 00 ; 
0D40: 00 08 06 03 03 03 07 07 ; 
0D48: 0F 0F 07 07 03 03 01 00 ; 
0D50: 67 37 37 1F BF BF BF FF ; 
0D58: FF FF FF FF FF FB BB 71 ; 
0D60: E6 F8 F9 FF FE FE FF FF ; 
0D68: FF FF FF FF FF FF DF 8E ; 
0D70: 00 40 80 00 20 40 80 80 ; 
0D78: D0 C0 80 80 80 00 00 00 ; 
0D80: 00 00 00 00 00 00 00 00 ; 
0D88: 00 00 00 01 03 03 03 02 ; 
0D90: 00 00 00 00 00 00 00 00 ; 
0D98: 00 00 E0 60 F8 F8 F4 FE ; 
0DA0: 01 01 00 18 2E 7E 7E 3D ; 
0DA8: 7F 6F 36 00 00 00 00 00 ; 
0DB0: FE FC D8 30 00 02 07 0D ; 
0DB8: 0F 06 66 B0 F8 78 60 00 ; 
0DC0: 00 00 00 00 00 00 00 00 ; 
0DC8: 00 00 00 00 00 01 03 05 ; 
0DD0: 00 00 00 00 00 00 00 00 ; 
0DD8: 00 00 00 00 00 C0 A0 E0 ; 
0DE0: 0F 0F 07 02 01 00 08 1C ; 
0DE8: 1A 2E 3E 18 00 00 00 00 ; 
0DF0: D0 F0 F0 E0 C0 18 3E 3E ; 
0DF8: 5D 7F 7F 36 0E 04 00 00 ; 
0E00: 01 0F 1F 07 00 00 00 00 ; 
0E08: 00 00 00 00 00 00 00 00 ; 
0E10: B0 F0 F0 F0 F0 00 00 00 ; 
0E18: 00 00 00 00 00 00 00 00 ; 
0E20: 00 00 00 00 00 00 00 00 ; 
0E28: 00 00 00 01 07 1F 3F 79 ; 
0E30: 00 7E 7E 7E 7E 7E 7E 3C ; 
0E38: 7E 7E FF FF FF FF E7 C3 ; 
0E40: 00 00 00 00 00 00 00 00 ; 
0E48: 00 00 00 80 E0 F8 FC 9E ; 
0E50: 00 00 00 00 00 00 00 00 ; 
0E58: 00 00 00 00 00 00 00 00 ; 
0E60: 00 04 03 03 07 0F 07 03 ; 
0E68: 00 00 00 00 00 00 00 00 ; 
0E70: 80 40 40 60 60 E0 F0 F0 ; 
0E78: 70 00 00 00 00 00 00 00 ; 
0E80: 01 08 04 06 03 07 0F 07 ; 
0E88: 03 00 00 00 00 00 00 00 ; 
0E90: 00 80 C0 40 60 60 E0 F0 ; 
0E98: F0 70 10 00 00 00 00 00 ; 
0EA0: 01 08 04 06 02 07 07 0F ; 
0EA8: 07 03 00 00 00 00 00 00 ; 
0EB0: 00 80 C0 C0 60 60 60 E0 ; 
0EB8: F0 F0 70 10 00 00 00 00 ; 
0EC0: 00 00 00 00 00 00 00 00 ; 
0EC8: 00 00 00 01 07 1F 3F 79 ; 
0ED0: 7E 7E 7E 7E 7E 3C 3C 7E ; 
0ED8: 7E 7E FF FF FF FF E7 C3 ; 
0EE0: 00 00 00 00 00 00 00 00 ; 
0EE8: 00 00 00 80 E0 F8 FC 9E ; 
0EF0: 00 00 00 00 00 00 00 00 ; 
0EF8: 00 00 00 00 00 00 00 00 ; 
0F00: 00 00 00 00 00 00 00 00 ; 
0F08: 00 00 00 01 07 1F 3F 79 ; 
0F10: 00 00 20 64 7E 3C 3C 7E ; 
0F18: 7E 7E FF FF FF FF E7 C3 ; 
0F20: 00 00 00 00 00 00 00 00 ; 
0F28: 00 00 00 80 E0 F8 FC 9E ; 
0F30: 00 00 00 00 00 00 00 00 ; 
0F38: 00 00 00 00 00 00 00 00 ; 
0F40: 00 00 00 00 00 00 00 00 ; 
0F48: 00 00 00 00 00 00 00 00 ; 
0F50: 00 00 00 00 00 00 00 00 ; 
0F58: 00 00 00 00 00 00 00 00 ; 
0F60: 00 00 00 00 00 00 00 00 ; 
0F68: 00 06 0F 06 00 00 00 00 ; 
0F70: 00 00 00 78 7E 3F 1F 0F ; 
0F78: 1F 0F 0F 1F 07 00 00 00 ; 
0F80: 00 00 00 00 00 00 00 00 ; 
0F88: 00 06 0F 06 00 00 00 00 ; 
0F90: 00 00 00 78 7E 3F 1F 0F ; 
0F98: 1F 0F 0F 1F 07 00 00 00 ; 
0FA0: 00 00 00 00 00 00 00 00 ; 
0FA8: 00 3C 21 21 39 05 05 38 ; 
0FB0: 00 00 00 00 00 00 00 00 ; 
0FB8: 00 C6 29 29 29 29 29 C6 ; 
0FC0: 00 00 00 00 00 00 00 00 ; 
0FC8: 00 98 A5 A5 A5 A5 A5 98 ; 
0FD0: 00 00 00 00 00 00 00 00 ; 
0FD8: 00 C6 29 29 29 29 29 C6 ; 
0FE0: 00 00 00 00 00 00 00 00 ; 
0FE8: 00 00 00 00 00 00 00 00 ; 
0FF0: 00 00 00 00 00 00 00 00 ; 
0FF8: 00 00 00 00 00 00 00 00 ; 

; Bit plane 1

; Image 0 (bit plane 1 ... see 0000 for bit plane 0)
1000: 00 00 00 00 00 00 00 00 ; 
1008: 00 00 00 00 00 00 00 00 ; 
1010: 00 00 00 00 00 00 00 00 ; 
1018: 00 00 00 00 00 00 00 00 ; 

; Image 1 (bit plane 1 ... see 0020 for bit plane 0)
1020: 00 00 00 00 00 00 00 00 ; 
1028: 00 00 00 00 00 00 03 01 ; 
1030: 00 00 00 00 00 00 00 00 ; 
1038: A0 A0 A0 00 A0 A0 B8 F0 ; 

; Image 2 (bit plane 1 ... see 0040 for bit plane 0)
1040: 00 00 00 00 00 00 00 00 ; 
1048: 00 00 00 1F 7F FF F8 03 ; 
1050: 00 00 00 00 00 00 00 00 ; 
1058: 00 00 00 00 80 C0 00 FE ; 

1060: 00 00 00 00 00 00 00 00 ; 
1068: 00 00 00 00 00 00 00 00 ; 
1070: 40 00 00 00 00 00 00 00 ; 
1078: 00 00 00 00 00 00 00 00 ; 
1080: 03 00 00 00 00 00 00 00 ; 
1088: 00 00 00 00 00 00 00 00 ; 
1090: F2 1E 00 00 00 00 00 00 ; 
1098: 00 00 00 00 00 00 00 00 ; 
10A0: 18 7E 7E FF FF FF 7E 7E ; 
10A8: 18 00 00 00 00 00 00 00 ; 
10B0: 00 00 00 00 00 00 00 00 ; 
10B8: 00 00 00 00 00 00 00 00 ; 
10C0: 18 7E 7E FF FF FF 7E 7E ; 
10C8: 18 00 00 00 00 00 00 00 ; 
10D0: 00 00 00 00 00 00 00 00 ; 
10D8: 00 00 00 00 00 00 00 00 ; 
10E0: 00 30 78 78 FC FC 78 78 ; 
10E8: 30 00 00 00 00 00 00 00 ; 
10F0: 00 00 00 00 00 00 00 00 ; 
10F8: 00 00 00 00 00 00 00 00 ; 
1100: 00 30 78 78 FC FC 78 78 ; 
1108: 30 00 00 00 00 00 00 00 ; 
1110: 00 00 00 00 00 00 00 00 ; 
1118: 00 00 00 00 00 00 00 00 ; 
1120: 00 00 00 00 00 00 00 00 ; 
1128: 00 00 00 01 04 00 03 01 ; 
1130: 00 00 00 00 00 00 00 01 ; 
1138: 01 03 03 00 00 00 00 00 ; 
1140: 00 00 00 0C 3E 78 F3 E7 ; 
1148: EC C8 00 01 01 03 03 01 ; 
1150: 00 00 00 20 70 F8 E0 40 ; 
1158: 40 00 80 C0 E0 F0 F0 E0 ; 
1160: 03 06 00 00 00 01 03 07 ; 
1168: 07 07 07 03 01 00 00 00 ; 
1170: C3 87 0F 0F 0F CF E7 E3 ; 
1178: F0 F0 E0 E0 C0 00 00 00 ; 
1180: 81 C0 C0 E0 E0 C0 C0 80 ; 
1188: 00 00 00 00 00 00 00 00 ; 
1190: E0 C0 00 00 00 00 00 00 ; 
1198: 00 00 00 00 00 00 00 00 ; 
11A0: 00 00 00 00 00 00 00 00 ; 
11A8: 00 00 0E 1F 3F 3F 3F 3F ; 
11B0: 00 00 00 08 00 12 B0 E8 ; 
11B8: 38 1C 04 00 00 80 8E 1F ; 
11C0: 00 00 00 00 00 00 00 00 ; 
11C8: 00 00 08 1E 1F 0F 03 00 ; 
11D0: 00 00 00 00 00 00 00 00 ; 
11D8: 00 00 00 00 80 80 E0 E0 ; 
11E0: 1F 0E 00 00 00 00 00 00 ; 
11E8: 00 00 00 00 00 00 00 00 ; 
11F0: 3F 3F 3F 3F 1F 0E 00 00 ; 
11F8: 00 00 00 00 00 00 00 00 ; 
1200: 02 83 80 00 00 00 02 07 ; 
1208: 07 0F 0F 07 07 03 00 00 ; 
1210: 20 80 E0 70 78 30 10 00 ; 
1218: 80 C0 C0 80 80 00 00 00 ; 
1220: 00 00 00 00 06 01 01 00 ; 
1228: 00 00 00 00 60 19 07 03 ; 
1230: 02 01 21 11 10 08 0D CF ; 
1238: E7 7F 7F FF FC F0 C0 80 ; 
1240: 00 00 10 10 89 89 0B 1F ; 
1248: 1F BE 1C 08 00 00 00 00 ; 
1250: 40 44 82 82 8E DF FF FF ; 
1258: 81 00 00 00 00 00 00 00 ; 
1260: 00 08 08 10 10 30 60 E1 ; 
1268: F3 FF 7F 3F 0F 00 00 00 ; 
1270: 00 00 00 00 00 40 40 80 ; 
1278: 00 80 80 C6 F8 E0 80 80 ; 
1280: 03 01 01 03 07 1D 61 01 ; 
1288: 00 03 03 04 08 00 00 00 ; 
1290: 00 00 00 00 00 80 80 C0 ; 
1298: C0 F3 7F 38 30 10 20 20 ; 
12A0: 00 00 00 00 00 00 40 E0 ; 
12A8: E0 F9 FF 7F 12 10 08 08 ; 
12B0: 00 00 00 00 00 00 3C 7E ; 
12B8: 7E FF BD 39 10 10 20 20 ; 
12C0: 03 03 03 03 07 07 0E 1C ; 
12C8: 1C 3E F6 F3 60 20 20 10 ; 
12D0: C0 80 00 80 C0 60 20 18 ; 
12D8: 00 00 00 00 80 80 40 00 ; 
12E0: 00 00 00 00 00 00 00 00 ; 
12E8: 00 00 00 00 00 00 00 00 ; 
12F0: 00 00 00 00 00 00 00 00 ; 
12F8: 00 00 00 0C 1F 1F 3F 3F ; 
1300: 00 00 00 00 00 00 00 00 ; 
1308: 00 30 7C FD FF FF FF FF ; 
1310: 00 00 00 00 00 00 00 00 ; 
1318: 00 C7 FF FF FF FF FF FF ; 
1320: 00 00 00 00 00 00 00 00 ; 
1328: 00 80 C0 F0 F8 FC FC FE ; 
1330: 00 00 00 00 00 00 00 00 ; 
1338: 00 00 00 00 00 00 00 00 ; 
1340: 00 00 00 00 00 00 00 00 ; 
1348: 00 00 00 00 00 00 00 00 ; 
1350: 1F 3F 3F 3F 1F 0F 07 01 ; 
1358: 00 00 00 00 00 00 00 00 ; 
1360: FF FF FF FF FF FF FF B1 ; 
1368: 00 00 00 00 00 00 00 00 ; 
1370: FF FF FF FF FF FF FC F0 ; 
1378: E0 00 00 00 00 00 00 00 ; 
1380: FE FC FC F8 F0 F8 F8 30 ; 
1388: 00 00 00 00 00 00 00 00 ; 
1390: 00 00 00 00 00 00 00 00 ; 
1398: 00 00 00 00 00 00 00 00 ; 
13A0: 00 00 00 00 00 00 00 00 ; 
13A8: 00 00 00 00 00 01 01 00 ; 
13B0: 00 00 00 00 00 00 00 01 ; 
13B8: 01 03 33 FF FF FF FF FF ; 
13C0: 00 00 00 00 00 00 00 C0 ; 
13C8: E6 EF FF FF FF FF FF FF ; 
13D0: 00 00 00 00 00 00 18 3C ; 
13D8: 7D FF FF FF FF FF FF FF ; 
13E0: 00 00 00 00 00 00 00 C0 ; 
13E8: E0 EC FE FE FC FC F8 FC ; 
13F0: 00 00 00 00 00 00 00 00 ; 
13F8: 00 00 00 00 00 00 00 00 ; 
1400: 00 00 00 00 00 00 00 00 ; 
1408: 00 00 00 00 00 00 00 00 ; 
1410: 7F 3F 7F FF FF 7D 38 30 ; 
1418: 00 00 00 00 00 00 00 00 ; 
1420: FF FF FF FF FF FF FF FF ; 
1428: 7C 78 30 00 00 00 00 00 ; 
1430: FF FF FF FF FF FF F7 F3 ; 
1438: E0 60 00 00 00 00 00 00 ; 
1440: FE FE FE FC D8 C0 C0 80 ; 
1448: 00 00 00 00 00 00 00 00 ; 
1450: 00 00 00 00 00 00 00 00 ; 
1458: 00 00 00 00 00 00 00 00 ; 
1460: 00 00 00 00 01 03 0F 1F ; 
1468: 1F 1F 0F 0F 06 00 00 00 ; 
1470: 00 00 00 00 8E FF FF FF ; 
1478: FF FF FF FF 30 00 00 00 ; 
1480: 00 00 00 30 FF FF FF FF ; 
1488: FF FF FF FF C6 00 00 00 ; 
1490: 00 00 00 00 00 C0 F0 F8 ; 
1498: F8 F8 F0 F0 30 00 00 00 ; 
14A0: 00 00 00 00 01 07 0F 1F ; 
14A8: 1F 1F 0F 03 01 01 00 00 ; 
14B0: 00 00 00 00 9C FF FF FF ; 
14B8: FF FF FF FF F3 C0 00 00 ; 
14C0: 00 00 00 70 FC FF FF FF ; 
14C8: FF FF FF FF FB 60 00 00 ; 
14D0: 00 00 00 00 C0 E0 F0 F0 ; 
14D8: F0 F0 E0 E0 40 00 00 00 ; 
14E0: 00 00 00 00 00 0C 3F 7F ; 
14E8: 7F 3F 0C 00 00 00 00 00 ; 
14F0: 00 00 00 00 00 F0 FC FE ; 
14F8: FE F4 C0 00 00 00 00 00 ; 
1500: 00 00 00 00 00 00 02 2C ; 
1508: 00 00 00 00 00 00 00 00 ; 
1510: 00 00 00 00 00 20 70 F0 ; 
1518: 60 00 00 00 00 00 00 00 ; 
1520: 00 00 00 00 00 00 04 32 ; 
1528: 00 00 00 00 00 00 00 00 ; 
1530: 00 00 00 00 00 60 F0 70 ; 
1538: 20 00 00 00 00 00 00 00 ; 
1540: 00 00 00 00 00 00 01 01 ; 
1548: 00 00 00 00 00 00 00 00 ; 
1550: 00 00 00 00 60 F0 F8 F8 ; 
1558: F8 F0 60 00 00 00 00 00 ; 
1560: 00 00 00 01 03 03 03 01 ; 
1568: 03 01 01 00 00 00 00 00 ; 
1570: 00 00 D0 F8 FC F8 FC FC ; 
1578: FC FC F8 D0 00 00 00 00 ; 
1580: 00 03 07 07 0F 0F 07 0F ; 
1588: 0F 0F 07 03 03 01 00 00 ; 
1590: F0 FC FE FE FF FF FF FF ; 
1598: FE FF FF FE FC B8 00 00 ; 
15A0: 00 00 00 00 00 00 00 00 ; 
15A8: 00 18 38 78 78 7C FE FE ; 
15B0: 00 00 00 00 00 00 00 00 ; 
15B8: 00 00 00 00 00 00 00 00 ; 
15C0: 00 00 00 00 0E 1F 1F 1F ; 
15C8: 7F 7F 7F FF FF FF FF FF ; 
15D0: 00 00 00 00 00 60 E0 E0 ; 
15D8: E0 E0 F0 F0 F0 F8 FC FC ; 
15E0: 00 03 03 07 07 0F 0F 3F ; 
15E8: 3F 7F 7F FF FF FF FF FF ; 
15F0: 00 C0 E0 E0 F0 E0 E0 F0 ; 
15F8: F0 F0 E0 F0 F0 F8 FC FE ; 
1600: 07 07 0F 1F 1F 3F 3F 3F ; 
1608: 3F 7F 7F 7F 7F FF FF FF ; 
1610: 00 00 80 80 80 80 E0 F0 ; 
1618: F0 F0 F0 F8 F8 F8 F8 F8 ; 
1620: 00 00 00 00 01 03 07 07 ; 
1628: 07 07 03 01 00 00 00 00 ; 
1630: 00 00 00 00 80 C0 E0 E0 ; 
1638: E0 E0 C0 80 00 00 00 00 ; 
1640: 00 00 00 03 0F 0F 1F 1F ; 
1648: 1F 1F 1F 0F 0F 03 00 00 ; 
1650: 00 00 00 80 E0 E0 F0 F0 ; 
1658: F0 F0 F0 E0 E0 80 00 00 ; 
1660: 00 00 00 03 0F 0F 1F 1F ; 
1668: 1F 1F 1F 0F 0F 03 00 00 ; 
1670: 00 00 00 80 E0 E0 F0 F0 ; 
1678: F0 F0 F0 E0 E0 80 00 00 ; 
1680: 00 00 00 03 0F 0F 1F 1F ; 
1688: 1F 1F 1F 0F 0F 03 00 00 ; 
1690: 00 00 00 80 E0 E0 F0 F0 ; 
1698: F0 F0 F0 E0 E0 80 00 00 ; 
16A0: 00 00 00 00 00 00 00 00 ; 
16A8: 01 00 00 00 00 00 00 00 ; 
16B0: 00 00 00 00 00 00 80 00 ; 
16B8: 00 00 00 00 00 00 00 00 ; 
16C0: 03 0F 0F 1F 1F 3F 3F 3F ; 
16C8: 3F 3F 3F 1F 1F 0F 0F 03 ; 
16D0: C0 F0 F0 F8 F8 FC FC FC ; 
16D8: FC FC FC F8 F8 F0 F0 C0 ; 
16E0: 03 0F 0F 1F 1F 3F 3F 3F ; 
16E8: 3F 3F 3F 1F 1F 0F 0F 03 ; 
16F0: C0 F0 F0 F8 F8 FC FC FC ; 
16F8: FC FC FC F8 F8 F0 F0 C0 ; 
1700: 03 07 FF FF 0F 0F 00 03 ; 
1708: 37 7B CE 84 84 CE 7B 31 ; 
1710: E0 F0 F0 F8 F8 F8 00 C0 ; 
1718: E6 DE 73 21 21 73 DE 8C ; 
1720: 00 00 3C 00 00 00 00 00 ; 
1728: 00 00 00 00 00 00 00 00 ; 
1730: 00 00 00 00 00 00 00 00 ; 
1738: 00 00 00 00 00 00 00 00 ; 
1740: 00 00 00 00 00 00 00 00 ; 
1748: 00 00 00 00 00 00 00 00 ; 
1750: 00 00 00 78 7E 3F 1E 0C ; 
1758: 00 3C 3C 00 07 00 00 00 ; 
1760: 00 00 00 00 0C 1F 1F 3F ; 
1768: 00 00 01 00 03 00 00 00 ; 
1770: 00 00 00 00 00 80 C0 80 ; 
1778: 00 F8 F8 00 C0 00 00 00 ; 
1780: 00 00 00 00 00 00 00 00 ; 
1788: 00 E0 E0 00 00 00 00 00 ; 
1790: 00 00 00 00 00 00 00 00 ; 
1798: 00 00 00 00 00 00 00 00 ; 
17A0: 84 84 FC 00 00 00 00 00 ; 
17A8: 00 00 00 00 00 00 00 00 ; 
17B0: 00 00 00 00 00 00 00 00 ; 
17B8: 00 00 00 00 00 00 00 00 ; 
17C0: 00 00 00 00 01 03 07 07 ; 
17C8: 0F 0F 07 01 00 00 00 00 ; 
17D0: 00 00 00 00 80 E0 E0 F0 ; 
17D8: F0 F0 E0 C0 00 00 00 00 ; 
17E0: 00 00 02 07 0F 1F 3F 3F ; 
17E8: 1F 1F 1F 0F 03 01 00 00 ; 
17F0: 00 00 C0 C0 E0 F0 E0 F0 ; 
17F8: F0 F0 E0 E0 80 00 00 00 ; 
1800: 00 00 00 01 07 0F 0F 1F ; 
1808: 1F 1F 0F 1F 06 00 00 00 ; 
1810: 00 00 00 80 E0 F0 F8 F8 ; 
1818: F8 F0 F8 F0 40 00 00 00 ; 
1820: 00 00 00 0D 0F 3F 3F 3F ; 
1828: 7F 3F 1F 1F 0F 03 00 00 ; 
1830: 00 00 60 F0 F8 FC FC FC ; 
1838: F8 F8 FC F8 F8 20 00 00 ; 
1840: 00 00 00 00 00 00 02 00 ; 
1848: 3C 7F FC 38 00 00 00 00 ; 
1850: 00 00 00 00 00 00 80 00 ; 
1858: 78 FC 7E 38 00 00 00 00 ; 
1860: 00 00 00 00 00 00 00 04 ; 
1868: 00 00 10 01 00 00 00 00 ; 
1870: 00 00 00 00 00 80 00 20 ; 
1878: 00 00 00 A0 00 00 00 00 ; 
1880: 00 00 00 00 00 01 08 00 ; 
1888: 00 00 02 01 00 00 00 00 ; 
1890: 00 00 00 00 10 00 00 10 ; 
1898: 10 00 00 00 40 00 00 00 ; 
18A0: 00 00 00 00 03 0F 3F FF ; 
18A8: FF 3F 07 00 00 00 00 00 ; 
18B0: 00 00 00 00 C0 F0 FC FF ; 
18B8: FF FC E0 00 00 00 00 00 ; 
18C0: 00 00 00 00 03 0F 3F FF ; 
18C8: FF 3F 07 00 00 00 00 00 ; 
18D0: 00 00 00 00 C0 F0 FC FF ; 
18D8: FF FC E0 00 00 00 00 00 ; 
18E0: 00 00 00 00 03 0F 3F FF ; 
18E8: FF 3F 07 00 00 00 00 00 ; 
18F0: 00 00 00 00 C0 F0 FC FF ; 
18F8: FF FC E0 00 00 00 00 00 ; 
1900: 00 00 00 00 00 01 03 07 ; 
1908: 03 01 03 02 04 00 00 00 ; 
1910: 00 00 00 00 10 60 C0 C0 ; 
1918: E0 80 80 40 40 20 00 00 ; 
1920: 00 08 04 00 00 06 03 07 ; 
1928: 2F 0F 1B 23 49 21 02 00 ; 
1930: 00 00 00 00 00 E0 80 C0 ; 
1938: E0 80 80 00 80 40 00 00 ; 
1940: 02 81 44 32 09 0D 07 03 ; 
1948: 07 4D 00 00 00 00 00 00 ; 
1950: 02 20 88 B0 E1 F4 F8 F0 ; 
1958: A6 10 8C 02 00 00 00 00 ; 
1960: 00 00 00 00 00 00 00 03 ; 
1968: 00 00 00 00 00 00 00 00 ; 
1970: 00 00 00 00 00 00 00 E0 ; 
1978: 00 00 00 00 00 00 00 00 ; 
1980: 00 00 00 00 00 04 02 01 ; 
1988: 00 00 00 00 00 00 00 00 ; 
1990: 00 00 00 00 00 00 00 00 ; 
1998: 80 40 00 00 00 00 00 00 ; 
19A0: 00 00 00 00 00 01 01 01 ; 
19A8: 01 01 01 00 00 00 00 00 ; 
19B0: 00 00 00 00 00 00 00 00 ; 
19B8: 00 00 00 00 00 00 00 00 ; 
19C0: 00 14 0F 5C 30 E6 2F DF ; 
19C8: 0F 07 03 01 00 00 00 00 ; 
19D0: 00 A0 C0 E4 38 8D E6 F7 ; 
19D8: E0 80 00 00 00 00 00 00 ; 
19E0: 00 00 00 00 00 00 00 00 ; 
19E8: 00 00 00 00 00 00 01 01 ; 
19F0: 00 00 00 00 00 00 00 00 ; 
19F8: 00 02 0F 2F 39 F0 C0 82 ; 
1A00: 00 00 00 00 00 00 00 00 ; 
1A08: 00 C0 F4 FE 9F 0F 03 41 ; 
1A10: 00 00 00 00 00 00 00 00 ; 
1A18: 00 00 00 00 00 00 C0 C0 ; 
1A20: 03 07 07 06 0E 00 00 00 ; 
1A28: 00 00 00 00 00 00 00 00 ; 
1A30: 0F 1F 3F 3C 78 3C 0E 07 ; 
1A38: 02 00 00 00 00 00 00 00 ; 
1A40: E0 F8 FC FC 3E 78 E0 C0 ; 
1A48: 80 00 00 00 00 00 00 00 ; 
1A50: E0 60 70 38 18 00 00 00 ; 
1A58: 00 00 00 00 00 00 00 00 ; 
1A60: 00 00 00 00 00 00 00 00 ; 
1A68: 00 00 00 00 03 07 07 03 ; 
1A70: 00 00 00 00 00 00 00 02 ; 
1A78: 27 3F 3F FF F9 F0 E0 C5 ; 
1A80: 00 00 00 00 00 00 00 20 ; 
1A88: 60 FB FF 7F 1F 0B 82 A0 ; 
1A90: 00 00 00 00 00 00 00 00 ; 
1A98: 00 00 00 C0 C0 C0 E0 E0 ; 
1AA0: 0F 0E 1E 1E 3C 00 00 00 ; 
1AA8: 00 00 00 00 00 00 00 00 ; 
1AB0: 87 1F 3F 3F 7F 7F 1F 0F ; 
1AB8: 07 02 00 00 00 00 00 00 ; 
1AC0: F0 F8 F8 FC FE FC F8 F0 ; 
1AC8: E0 E0 C0 80 00 00 00 00 ; 
1AD0: F0 7C FC 3C 1E 00 00 00 ; 
1AD8: 00 00 00 00 00 00 00 00 ; 
1AE0: 00 00 00 00 00 00 00 09 ; 
1AE8: 05 07 07 0F 0F 1F 1F 7D ; 
1AF0: 08 04 0D 8F 5F FF FF FF ; 
1AF8: FF EF F7 F2 E0 E0 C0 00 ; 
1B00: 20 40 E0 F8 FC FE FF FF ; 
1B08: DF BF 3F 1D 0B 07 03 01 ; 
1B10: 00 00 00 00 00 40 80 90 ; 
1B18: E0 E0 E0 F4 F8 F8 F8 BC ; 
1B20: 3E 3E 3E 1C 70 00 00 00 ; 
1B28: 00 00 00 00 00 00 00 00 ; 
1B30: 00 01 08 05 0F 1F 07 02 ; 
1B38: 04 00 00 00 00 00 00 00 ; 
1B40: 00 00 90 A0 F0 E0 C0 C0 ; 
1B48: A0 00 00 00 00 00 00 00 ; 
1B50: 78 3C 3C 1A 0E 00 00 00 ; 
1B58: 00 00 00 00 00 00 00 00 ; 
1B60: 00 00 00 00 00 00 00 00 ; 
1B68: 00 00 00 00 00 00 00 00 ; 
1B70: 00 00 00 00 00 00 00 00 ; 
1B78: 00 00 00 00 00 00 01 00 ; 
1B80: 00 00 00 00 00 00 00 00 ; 
1B88: 00 00 00 00 00 00 20 00 ; 
1B90: 00 00 00 00 00 00 00 00 ; 
1B98: 00 00 00 00 00 00 00 00 ; 
1BA0: 00 00 00 00 01 00 00 01 ; 
1BA8: 01 03 0B 07 07 0F 0F 1F ; 
1BB0: 01 27 1F 3F 3F FF FF FF ; 
1BB8: FF FF FF FF FF FE FC F8 ; 
1BC0: 20 E4 F8 FE FF FF FF FF ; 
1BC8: FF FF FF FF FF FF 3F 0F ; 
1BD0: 00 00 00 00 00 80 80 80 ; 
1BD8: D0 E0 E0 F0 F0 F8 F8 F8 ; 
1BE0: 1F 1F 1F 0F 07 03 03 01 ; 
1BE8: 00 00 00 00 00 00 00 00 ; 
1BF0: C0 E0 F0 F4 FC FE FF FF ; 
1BF8: 7F 3F 3F 0F 03 01 01 00 ; 
1C00: 03 0F 1F 3F 7F FF FF FF ; 
1C08: FE FC F8 F8 F0 C0 80 00 ; 
1C10: F8 F0 E0 E0 C0 00 00 00 ; 
1C18: 00 00 00 00 00 00 00 00 ; 
1C20: 00 00 02 01 21 14 14 42 ; 
1C28: 22 14 98 38 04 80 00 00 ; 
1C30: 00 00 00 50 00 A4 28 40 ; 
1C38: 42 44 2C 01 02 0C 00 00 ; 
1C40: 00 00 10 10 09 0D 86 10 ; 
1C48: 48 08 08 04 00 00 00 00 ; 
1C50: 80 00 80 80 04 A8 48 11 ; 
1C58: 10 12 24 00 00 00 00 00 ; 
1C60: 01 25 10 09 09 45 47 2E ; 
1C68: 32 80 10 00 00 08 00 00 ; 
1C70: 00 10 94 A0 E2 F4 34 1D ; 
1C78: 0E 04 08 00 00 08 00 00 ; 
1C80: 00 00 00 00 00 00 00 00 ; 
1C88: 00 00 00 00 00 00 00 00 ; 
1C90: 00 00 00 00 00 00 00 00 ; 
1C98: 00 00 00 10 00 04 82 52 ; 
1CA0: 00 00 00 00 00 00 00 00 ; 
1CA8: 00 00 80 80 40 41 82 CA ; 
1CB0: 00 00 00 00 00 00 00 00 ; 
1CB8: 00 00 00 00 00 00 00 00 ; 
1CC0: 00 00 00 00 08 07 01 00 ; 
1CC8: 12 28 06 04 00 00 00 00 ; 
1CD0: 51 29 BB 5F 3F BE FC 98 ; 
1CD8: 08 04 00 00 00 00 00 00 ; 
1CE0: D4 DC FE FC 99 1A 0E 0C ; 
1CE8: 12 00 00 00 00 00 00 00 ; 
1CF0: 00 00 80 00 00 00 80 00 ; 
1CF8: 00 20 D0 80 80 00 00 00 ; 
1D00: 00 00 00 00 00 00 00 00 ; 
1D08: 00 00 00 00 00 00 00 00 ; 
1D10: 04 01 01 01 08 08 04 24 ; 
1D18: 14 95 55 4F 2F BF 7F 7F ; 
1D20: 00 00 00 00 80 88 C2 42 ; 
1D28: C4 CC CC D8 F8 F9 FE FC ; 
1D30: 00 00 00 00 00 00 00 00 ; 
1D38: 00 00 00 00 00 00 00 00 ; 
1D40: 00 08 26 03 23 10 08 08 ; 
1D48: F7 00 00 00 00 00 00 00 ; 
1D50: 7F FF 7F 3C B8 38 0C 88 ; 
1D58: 08 04 00 00 10 00 20 00 ; 
1D60: FE FC FF 7F 26 20 10 00 ; 
1D68: 00 00 00 00 00 10 00 00 ; 
1D70: 00 40 80 00 20 40 00 00 ; 
1D78: 10 00 00 00 00 00 00 00 ; 
1D80: 00 00 00 00 00 00 00 00 ; 
1D88: 00 00 00 00 00 00 00 00 ; 
1D90: 00 00 00 00 00 00 00 00 ; 
1D98: 00 00 00 00 00 00 00 00 ; 
1DA0: 00 00 00 00 00 00 00 00 ; 
1DA8: 00 00 00 00 00 00 00 00 ; 
1DB0: 00 00 00 00 00 00 00 00 ; 
1DB8: 00 00 00 00 00 00 00 00 ; 
1DC0: 00 00 00 00 00 00 00 00 ; 
1DC8: 00 00 00 00 00 00 00 00 ; 
1DD0: 00 00 00 00 00 00 00 00 ; 
1DD8: 00 00 00 00 00 00 00 00 ; 
1DE0: 00 00 00 00 00 00 00 00 ; 
1DE8: 00 00 00 00 00 00 00 00 ; 
1DF0: 00 00 00 00 00 00 00 00 ; 
1DF8: 00 00 00 00 00 00 00 00 ; 
1E00: 00 00 00 18 3F 7F EF 8D ; 
1E08: 18 11 01 02 00 00 00 00 ; 
1E10: 00 20 10 20 00 F0 F0 E0 ; 
1E18: E0 C0 80 00 00 00 00 00 ; 
1E20: 00 00 00 00 00 00 02 00 ; 
1E28: 00 00 00 00 01 00 00 00 ; 
1E30: 00 00 00 00 08 18 00 00 ; 
1E38: 00 18 38 30 91 81 00 00 ; 
1E40: 00 00 00 00 00 00 40 00 ; 
1E48: 00 00 00 00 80 00 00 00 ; 
1E50: 00 00 00 00 00 00 00 00 ; 
1E58: 00 00 00 00 00 00 00 00 ; 
1E60: 00 04 03 03 01 00 18 7C ; 
1E68: FF 8F 3F 3C 61 01 03 02 ; 
1E70: 80 40 40 60 60 20 00 00 ; 
1E78: 80 F0 F0 F0 E0 C0 00 00 ; 
1E80: 01 08 04 0C 03 01 00 18 ; 
1E88: 7C FF 8F 3F 3C 61 01 03 ; 
1E90: 00 80 C0 40 60 60 20 00 ; 
1E98: 00 80 E0 F0 F0 E0 C0 00 ; 
1EA0: 01 08 04 06 02 07 01 00 ; 
1EA8: 18 7C 7F CF 9F 1C 31 21 ; 
1EB0: 00 80 C0 C0 60 60 60 20 ; 
1EB8: 00 00 80 E0 F0 F0 E0 C0 ; 
1EC0: 00 00 03 02 00 00 00 00 ; 
1EC8: 00 00 00 00 01 00 00 00 ; 
1ED0: 00 00 00 00 00 00 00 00 ; 
1ED8: 00 00 00 00 01 00 00 00 ; 
1EE0: 00 00 C0 40 40 00 00 00 ; 
1EE8: 00 00 00 00 80 00 00 00 ; 
1EF0: 00 00 00 00 00 00 00 00 ; 
1EF8: 00 00 00 00 00 00 00 00 ; 
1F00: 00 00 00 00 00 00 00 00 ; 
1F08: 00 00 00 00 00 00 00 00 ; 
1F10: 00 00 00 00 00 00 00 00 ; 
1F18: 00 00 00 00 00 00 00 00 ; 
1F20: 00 00 00 00 00 00 00 00 ; 
1F28: 00 00 00 00 80 00 00 00 ; 
1F30: 00 00 00 00 00 00 00 00 ; 
1F38: 00 00 00 00 00 00 00 00 ; 
1F40: 00 00 00 00 02 04 01 08 ; 
1F48: 02 00 04 02 00 00 00 00 ; 
1F50: 00 00 00 00 80 00 20 00 ; 
1F58: A0 00 40 80 00 00 00 00 ; 
1F60: 00 00 00 00 00 00 00 00 ; 
1F68: 0C 3E FF 1E 0C 00 00 00 ; 
1F70: 00 00 00 78 7E 3F 1E 0C ; 
1F78: 00 3C 3C 00 07 00 00 00 ; 
1F80: 00 00 00 00 00 00 00 00 ; 
1F88: 00 0E 3F 06 00 00 00 00 ; 
1F90: 00 00 00 78 7E 3F 1E 0C ; 
1F98: 00 3C 3C 00 07 00 00 00 ; 
1FA0: 00 00 00 00 00 00 00 00 ; 
1FA8: 00 18 25 05 09 05 25 18 ; 
1FB0: 00 00 00 00 00 00 00 00 ; 
1FB8: 00 C6 29 29 29 29 29 C6 ; 
1FC0: 00 00 00 00 00 00 00 00 ; 
1FC8: 00 18 25 25 19 25 25 18 ; 
1FD0: 00 00 00 00 00 00 00 00 ; 
1FD8: 00 C6 29 29 29 29 29 C6 ; 
1FE0: 00 00 00 00 00 00 00 00 ; 
1FE8: 00 00 00 00 00 00 00 00 ; 
1FF0: 00 00 00 00 00 00 00 00 ; 
1FF8: 00 00 00 00 00 00 00 00 ; 
```

```html
<script src="MoonPatrol.js"></script>
<script src="/js/Binary.js"></script>
<script src="/js/TileEngine.js"></script>
<script src="/js/Canvas.js"></script>
<script>
  TileEngine.setColorMap(
    {
        'CS0' : ['#808080','#00001A','#C100AE','#00AEC8'],
        'CS1' : ["#808080","#84C800","#C100AE","#C10000"], 
        'CS2' : ["#808080","#C10000","#00C800","#840000"],
        'CS3' : ["#808080","#840000","#C1C8C8","#C1C800"],       
        'CS4' : ["#808080","#845100","#808080","#3E3700"],
        'CS5' : [],
        'CS6' : [],
        'CS7' : ["#808080","#C1C800","#6290C8","#C10000"],	
        'CS8' : ["#808080","#C10000","#00AEC8","#005100"],
        'CS9' : ["#808080","#C1C800","#00001A","#C10000"],
        'CSA' : ["#808080","#00001A","#C1C8C8","#808080"],
        'CSB' : [],
        'CSC' : [],
        'CSD' : [],
        'CSE' : ["#808080","#C10000","#808080","#C10000"],        
        'CSF' : ["#808080","#808080","#C10000","#C10000"],        
    }
  )
</script>
<script>    
    window.onload = function() {  
        MoonPatrol.data = Binary.readBinary('GFX2.md.bin')        
        MoonPatrol.origin = 0
        Canvas.redrawGraphics() 
    }
</script>
```

