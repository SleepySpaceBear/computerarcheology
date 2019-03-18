![Moon Patrol Hardware Info](MoonPatrol.jpg)

# Hardware

>>> memory

| | | |
| --- | --- | --- |
| 0000p | ??0000p | |
| 0003p | ??0003p | |
| 000Ap | ??000Ap | |
| 000Cp | ??000Cp | |
| 000Dp | ??000Dp | |
| 000Ep | ??000Ep | |
| 0010p | SCROLL0 | Scroll ?? Not used |
| 0011p | SCROLL1 | Scroll ?? Not used |
| 0012p | SCROLL2 | Scroll ?? Not used |
| 0013p | SCROLL3 | Scroll ?? Not used |
| 0014p | SCROLL4 | Scroll ?? Not used |
| 0015p | SCROLL5 | Scroll ?? Not used |
| 0016p | SCROLL6 | Scroll ?? Not used |
| 0017p | SCROLL7 | Scroll ?? Not used |
| 0018p | SCROLL8 | Scroll ?? Not used |
| 0019p | SCROLL9 | Scroll ?? Not used |
| 001Ap | SCROLLA | Scroll ?? Not used |
| 001Bp | SCROLLB | Scroll ?? Not used |
| 001Cp | SCROLLC | Scroll |
| 001Dp | SCROLLD | Scroll |
| 001Ep | SCROLLE | Scroll |
| 001Fp | SCROLL0 | Scroll |
| 0040p | BKG1X   | Background 1 X position (hills/city) |
| 0060p | BKG1Y   | Background 1 Y position (hills/city) |
| 0080p | BKG2X   | Background 2 X position (distant mountains) |
| 00A0p | BKG2Y   | Background 2 Y position (distant mountains) |
| 00C0p | BKGCtrl | Background control (see below) |

```
BKGCtrl:
   ??Am_?ch?
   A=1 disable backgrounds, A=0 enable backgrounds
   m=1 don't draw mountains, m=0 draw mountains
   c=1 don't draw city, c=0 draw city
   h=1 don't draw hills, c=0 draw hills
```

>>> memory

| | | |
| --- | --- | --- |
| 8800r | PROTECT | Returns a mangled version of last value written to BG1X (port 40) |
| D000r | IN0 | ....XsBA    X=coin1, x=service credit, B=start2, A=start1 |
| D000w | SND_CMD | Sound command (bit 7 is the latch) |
| D001r | IN1 | f..j..lr    f=fire, b=jump, lr=left/right |
| D001w | FLIP    | ..B. xyAF       A=counterA B=counterB F=Flip?? y=CFlip2?? x=CFlipB?? |
| D002r | IN2 | f..jX.lr    (cocktail) a=fire, b=jump, X=coin1, lr=left/right|
| D003r | DSW1 | See below |
| D004r | DSW2 | See below |


DSW1: ddcceell  ll=patrol cars 00=1, 01=2, 10=3, 11=5, ee=extend points 00=NO, 01=10, 10=20_40_60 ,11=10_30_50 (Thousand)

The value of ddcc depends on "coin mode" bit in DSW2. If the switch is closed (value 0) then there are two slots
with different coin mappings. Otherwise there is just one slot mapping.

```
Coin mode A: (one currency)
  ddcc= 15:1C-1P, 14:2C-1P, 13:3C-1P, 12:4C-1P, 11:5C-1P, 10:6C-1P, 9:NA, 8:NA, 
        7:1C-2P, 6:1C-3P, 5:1C-4P, 4:1C-5P, 3:1C-6P, 2:NA, 1:NA, 0:FREE

  Even though the service mode doesn't show it, the game treats:
         9 is 7C-1P, 8 is 1C-1P, 2 is 1C-7P, 1 is 1C-8P

Coin mode B (two different currencies)
   Coin A: cc = 3:FREE,  2:3C-1P, 1:2C-1P, 0:1C-1P
   Coin B: dd = 3:1C-6P, 2:1C-5P, 1:1C-3P, 0:1C-2P
```
   
Lots of good information in Mame Source: mame/drivers/m52.c

```
Memory Map:
   0000-3FFF ROM
   8000-83FF Video RAM
   8400-87FF Color RAM
   8800-DFFF Hardware (see below)
   E000-E7FF RAM
```

The video refresh runs at 56.74Hz. An IRQ is generated at every VBLANK.

The background video RAM is tile based. Memory is reserved for 32x32 tiles, but the first
row is not visible. The first and last columns are not visible. Thus there are 30x31 tiles
on the screen. The first visible tile number for the upper left corner is 8021. The bottom
right corner is 83FE.

The memory at 8400 sets the color for each tile in the same memory layout ... one byte per
tile. The upper bit of the this value is the upper bit of the tile selection. Set to 1 for
tiles 256..511.

All inputs are active low (0=on, 1=off)

DIP switch up is closed (grounded). Down is open. In TTL that means up is 0
and down is 1. The service-mode shows these bits reversed: up is 1 and down
is 0.

Bits are organized LSB on the left numbered as switch number 1.
Thus bit 0 is on the far left numbered "1". Down is 1 and up is 0 when read
but displayed on the service screen as Down is 0 and up is 1.

```
  C800-C8FF 64 Sprites (4 bytes each)
     00 Y coord. 0 is bottom of the screen (all showing). EB is top of screen all showing. EC-FF clips off top of sprite.
     01 yx_cccccc    x=flipX, y=flipY, c=color set
     02 tile number (see GFX2)
     03 X coord. 0 is left of the screen half clipped. F0 is right of the screen half clipped. F1-FF clips off right of sprite.
```

The ISR copies E100-E1BF (48 sprites) into sprite memory during each vertical blank.

TODO show how the sprites are copied and which are for what

These bit values are shown complimented on the service mode screens and the bits are shown 
LSB first (as switch number 1).
