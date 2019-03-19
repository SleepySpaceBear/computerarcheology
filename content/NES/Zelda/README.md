![Zelda](Zelda.jpg)

# The Legend of Zelda

>>> deploy:<br>
>>>   +Zelda.jpg<br>
>>>   +ZeldaBanks.jpg<br>
>>>   +zelda.js<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   Bank0.md<br>
>>>   Bank1.md<br>
>>>   Bank2.md<br>
   Bank3.md<br>
   Bank4.md<br>
   Bank5.md<br>
   Bank6.md<br>
   Bank7.md<br>
   ----<br>
   Journal.md<br>

# Code

* [Hardware](Hardware.md)
* [RAM Content](RAMUse.md)
* [Bank 0 - Audio](Bank0.md)
* [Bank 1 - Game strings, splash screen tiles](Bank1.md)
* [Bank 2 - Pregame, common sprite tiles, common background tiles](Bank2.md)
* [Bank 3 - Overworld and dungeon sprite and background tiles](Bank3.md)
* [Bank 4](Bank4.md)
* [Bank 5](Bank5.md)
* [Bank 6](Bank6.md)
* [Bank 7 - Common code](Bank7.md)

# Simulator File Header 

```
0000: 4E 45 53 1A ; "NES" and DOS end-of-file
0004: 08 ; 8*16K PRG ROM size
0005: 00 ; 0*8K CHR ROM size (0 means board uses CHR RAM)
0006: 12 ; 0001_0010 : xxxx0xx0 = vertical arrangement/horizontal mirroring (CIRAM A10 = PPU A11) 
;                      xxxxxx1x = Battery-backed SRAM from 6000-7FFF 
;                      0001xxxx = Lower nibble of mapper number
0007: 00 ; 0000_0000 : 0000xxxx = Upper nibble of mapper number
0008: 00 ; 0*8K PRG RAM size (0 means 8K)
0009: 00 ; 0000000_0 : xxxxxxx0 = NTSC TV system
000A: 00 ; Unofficial flags
000B: 00 00 00 00 00 ; Unused
```

# Memory Layout 

The 6502 processor has a 16-bit address bus, and it can directly address 64K bytes of memory for code and data. The PPU 
graphics processor has a separate 14-bit address bus, and it can directly address 16K of graphics information. Most games 
for the NES use a lot more memory than is directly accessible by these two processors. They do this by paging (also called 
bank-switching) sections of memory in and out of the two address spaces.

Depending on the game, an NES cartridge contains RAM and ROM for both CPU and PPU busses. Often these chips (especially ROMs) 
are much larger than 64K and depend on dedicated circuitry inside the cartridge to map smaller areas of the chips into the two 
address spaces. The game program controls the banks by writing to registers in the dedicated circuitry. There were many different 
Memory Management Controllers (MMCs) used in cartridges over the years. Most were designed to be program configurable so that a 
single cartridge configuration could be used for a variety of games.

Zelda uses MMC1 to map a single 128K CPU ROM as 8 16K banks. The controller is configured to always map the last 16K bank (bank 7) 
to CPU address C000-FFFF. The other 7 16K banks (banks 0 - 6) are swapped in and out of CPU address 8000-BFFF under program control.

An 8K RAM chip is mapped to CPU address 6000-7FFF. This chip is battery-backed with a CR2032 battery in the cartridge. This RAM 
holds saved-games. The battery isn't (easily) replaceable. When the battery dies you throw away the cartridge.

The Zelda cartridge also includes an 8K RAM chip that maps to the PPU address space at 0000-1FFF. The PPU reads image tiles ("patterns" 
for background and sprites) from this area. Large games use ROM for these tiles (patterns), and this area is referred to as VROM (video 
ROM) in the documentation. In Zelda this area is RAM, and the program copies the tile images from the CPU ROM to the PPU RAM.

Emulators allow you to run NES games on your computer. They need to know how all the ROMs are mapped by the cartridge, and they need to 
know about RAM and battery-backed RAM. All of the ROM is packed into a single file with a 16-byte header that describes the contents.

The following image shows how binary chunks from the Zelda.nes file map to NES memory. You can use the formulas to convert a code address 
from the code back to an offset in the Zelda.nes file (for patching).

![](ZeldaBanks.jpg)
 
# Tile Images

The first bank of VRAM (0000-0FFF) is used for sprites. The second bank of VRAM (1000-1FFF) is used for background tiles.

Tile images are 16 bytes each for an 8x8 pixel pattern. Each pixel is 2 bits. The actual color of a pixel is controlled 
by a color pallet. The color is independent of the pattern.

The 256 background tiles in VRAM (1000-1FFF) are divided into fixed tiles that never change over the course of the game 
and tiles that are swapped in and out as the player moves between the surface and dungeons. The fixed tiles are numbered 
00-6F and F2-FF. I suspect the second fixed set was added with new functionality as the development progressed. Interestingly, 
the tiles from 30-5F are blank and could have been used for this overflow.

The common (fixed) background tiles are loaded from ROM bank 2 (877F and 8E7F).

The 130 background tiles from 70-F1 are swapped in and out as the game progresses. The splash screen tiles are loaded from ROM 
bank 1 (96B4). The surface tiles are loaded from ROM bank 3 (893B). The dungeon tiles are loaded from ROM bank 3 (811B).

The 256 sprite tiles in VRAM (0000-FFF) are divided into fixed tiles that never change and enemy images that change as the 
player moves to different areas. Zelda uses two-tile sprites (8x16 pixels). Multiple sprites are grouped together to make 
larger creatures.

The fixed sprite tiles are numbered 00-8D. These are the images of Link, the game objects, and other miscellaneous sprites 
used everywhere. These are loaded from two separate places. The main area 00-6F comes from ROM bank 2 (807F). The area from 
70-8D loads as part of the splash sequence from ROM bank 1 (8DB4). This area is loaded as part of a much larger "splash screen 
sprites". These pictures must have been developed "on top" of TileSetC from bank 3 because some of those images "show through" 
into unused slots.

The game overwrites the splash sprites beginning at 8E but leaves 70-8D intact. There is plenty of room in bank 2 to add these 
images to the common sprite images thus keeping them together. I'm not sure how/why they got broken up.

Sprite tile numbers 8E-FF contain the "normal" creatures and the "bosses". On the surface, the entire range is used for "normals" 
since there are no surface bosses. The surface creatures are loaded from ROM bank 3 (915B).

In the dungeons things get a little complicated. The 16 tiles from 8E-9D contain common sprites in all dungeons (Bubble, Gel, Trap, 
Old Man, and Keese). These are loaded from ROM bank 3 (8CBB). Each dungeon has its own set of creature images loaded into 9E-BF. 
Each dungeon has its own set of boss-images is loaded into C0-FF.

These "per dungeon" tile sets are shared among the various levels. For instance levels 1, 2, and 7 share the same "normal" creatures. 
Levels 1, 2, 5, and 7 share the same "boss" tiles. The game only shows one of these bosses per level, of course. The code in ROM 
bank 3 (8044) configures the dungeon tiles correctly.

Note that the dungeon tile sets seem to be different for the second quest. It may be a simple substitution (like use first-quest-level-4 
for second-quest-level-1). Investigation to come.

```html
<table border="1">
  <tr>
    <th>Sprite Tiles</th>
    <th>Splash</th>
    <th>Surface</th>
    <th>Level 1</th>
    <th>Level 2</th>
    <th>Level 3</th>
    <th>Level 4</th>
    <th>Level 5</th>
    <th>Level 6</th>
    <th>Level 7</th>
    <th>Level 8</th>
    <th>Level 9</th>
  </tr>

  <tr>
    <td>00-6F (Common objects)</td>
    <td colspan="11"><a target="_blank" href="Bank2.html#TilesSCommon1">Link, treasure, misc 2:807F</a></td>
  </tr>

  <tr>
    <td>70-8D (Common objects)</td>
    <td colspan="11"><a target="_blank" href="Bank1.html#TilesSSplash">Ladder, misc 1:8DB4</a></td>
  </tr>

  <tr>
    <td>8E-9D (Shared Creatures)</td>
    <td rowspan="3"><a target="_blank" href="Bank1.html#TilesSSplash8E">Splash images 1:8F94</a></td>
    <td rowspan="3"><a target="_blank" href="Bank3.html#TilesSSurface">Surface creatures 3:915B</a></td>
    <td colspan="9"><a target="_blank" href="Bank3.html#TilesSDungeon">Dungeon creatures 3:9CBB</a></td>
  </tr>

  <tr>
    <td>9E-BF (Specific creatures)</td>
    <td><a target="_blank" href="Bank3.html#TilesS127">1,2,7 3:9DBB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS127">1,2,7 3:9DBB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS358">3,5,8 3:987B</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS469">4,6,9 3:9A9B</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS358">3,5,8 3:987B</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS469">4,6,9 3:9A9B</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS127">1,2,7 3:9DBB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS358">3,5,8 3:987B</a></td>
    <td><a target="_blank" href="Bank3.html#TilesS469">4,6,9 3:9A9B</a></td>
  </tr>

  <tr>
    <td>C0-FF (Bosses)</td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss1257">1,2,5,7 3:9FDB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss1257">1,2,5,7 3:9FDB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss3468">3,4,6,8 3:A3DB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss3468">3,4,6,8 3:A3DB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss1257">1,2,5,7 3:9FDB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss3468">3,4,6,8 3:A3DB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss1257">1,2,5,7 3:9FDB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss3468">3,4,6,8 3:A3DB</a></td>
    <td><a target="_blank" href="Bank3.html#TilesSBoss9">Ganon 3:A7DB</a></td>
  </tr>

  <tr/>
    <th>Background Tiles</th>
  <tr/>

 
  <tr>
    <td>00-6F (Test, misc)</td>
    <td colspan="12"><a target="_blank" href="Bank2.html#TilesBCommon1">Common 2:877F</a></td>
  </tr>
  <tr>
    <td>70-F1</td>
    <td><a target="_blank" href="Bank1.html#TilesBSplash">Splash 1:96B4</a></td>
    <td><a target="_blank" href="Bank3.html#TilesBSurface">Surface 3:893B</a></td>
    <td colspan="10"><a target="_blank" href="Bank3.html#TilesBDungeon">Dungeon 3:811B</a></td>
  </tr>
  <tr>
    <td>F2-FF (Misc)</td>
    <td colspan="12"><a target="_blank" href="Bank2.html#TilesBCommon2">Common 2:8E7F</a></td>
  </tr>

</table>
```

# Name Table Layout 

The PPU generates a background on the screen that is 32x30 tiles. Each tile is 8x8 pixels. A pixel can have one of 4 
colors (2 bits per pixel). Thus an 8x8 tile definition (pattern) requires 2bits*8*8 = 16 bytes.

A "name table" holds 32x30 = 960 bytes, one byte per screen tile, to describe which tile from pattern memory (PPU 0000-1FFF) to 
draw at each cell on the screen. If the first byte of the name table is a 00 then the first tile from pattern memory at 0000 is 
used to draw the 8x8 pixels at the top left of the screen. The name table includes 40 bytes of "attributes" that describes the 
colors of the rendered tiles. This rounds the name table out to an even 1K bytes.

Each cell in the name table can specify one of 256 tiles. In pattern memory 256 tiles consume 256x16 = 4K bytes. The pattern memory 
thus contains TWO separate areas: one at 0000-0FFF and one at 1000-1FFF. The sprites and the background can be configured to read 
from either area individually (sprites from one, background from the other, or both from the same pattern area).

The PPU provides for four separate name tables and various scrolling/mirroring modes among them. The four name tables make a 2x2 
square creating a giant name table of 64x60 cells. The screen can only show an area 32x30, and scrolling registers allow the display 
to be moved around (on a pixel boundary) within the giant map. This makes for smooth and easy scrolling around the larger background.

The PPU hardware on the console only includes space for two name tables (a total of 2K bytes). Games that need the giant map must 
include 2K of RAM on the cartridge for the extra two name tables. More commonly, games used the two built-in name tables to provide 
a 2-table scroller ... either vertically or horizontally.

Games can either join the tables horizontally to make a 64x30 table or vertically to make a 32x60 table. Zelda switches configurations 
to scroll left/right or up/down as the player moves between two play fields.

If "horizontal mirroring" is enabled then the two built-in name tables are joined vertically. The two name tables on the right are exact 
copies of the left. The terminology can be misleading since with "horizontal mirroring" the tables are joined vertically and no 
mirror-imaging is performed.

If "vertical mirroring" is enabled then the two built in tables are joined horizontally, and the two name tables on the bottom are 
copies of the top two.

The cartridge provides an electrical signal to the PPU to describe how the name tables should be accessed. Thus the built-in name 
table layout (mirroring) is controlled by the cartridge hardware and thus the MMC1 registers.

# Extracting the Code

## December 7, 2009

It starts with the NES emulator file ZELDA.NES, which is 128K ROM data plus the 16 byte header that describes the cartridge hardware.
 Based on the header, Zelda turns out to be a simple configuration. There is only program ROM (no extra video data) organized 
 into 8 16K banks. There is battery-backed RAM from 6000 to 7FFF. I wrote a java tool to extract the header and the individual ROM banks.

ROM banks are controlled by a custom memory-mapping chip called MMC1. The NES maps ROM to half (32K) of the address space from 8000 to 
FFFF. The MMC1 allows this area to be switched in as full 32K pages or two 16K pages with either the top or bottom page fixed.

Each of the 8 banks must be disassembled with a fixed origin. The 6502 branch instructions are relative but some instructions (like JSR) 
use an absolute two-byte address. I ran the 8 banks through the disassembler with an origin of 8000 to start with. The bottom of each 
bank is identical with a reset vector to BF50 (FF50 for bank 7).

The RESET vector sets up the MMC1 registers with 16K bank swapping (confirmed by the NES header). The top bank from C000 to FFFF is left 
fixed (bank 7). The other banks swap in and out of the lower half from 8000 to BFFF.

I ran the individual banks through the disassembler at their correct origin. Note that the disassembler I used identifies NES hardware 
registers in comments beside the code.

The game configures the ROM banks as:

8000 -- BFFF 16K (Banks 0-6 swapped in and out as needed)
C000 -- FFFF 16K (Bank 7 always)
The game starts with the RESET vector in bank 7. Thus the Legend of Zelda begins at FF50 in ROM bank 7.

## December 10, 2009

I took a cursory glance through the code and copied the RESET vector comments through all banks. 128K of ROM is quite formidable. I 
expected to find a lot of data for graphics images, and there are lots of "???" opcodes (data areas). I didn't expect to find the huge 
empty blocks of FF's in all the banks. I estimate less than 1/4th of the 128K ROM is actual code. That's a good thing!

I wrote a java tool to help me format data and blank areas more densely. This shrunk the size of the disassembly text considerably.

# Image Quest

## December 14, 2009

I did a little interactive-disassembly. Using the "patch" tool I filled data areas with a pattern of "AA" (alternating pixels) and 
looked for graphics changes in the emulator. When I got to Bank2 I bumped into the images of the letters and numbers. I wrote a tool 
to extract images in a text format and applied it to Bank2. There are all the letters, numbers, and lots of misc images like the 
treasure pictures used in the splash screen explanation.

There is a small section of code above the images at the beginning of Bank2. The code contains a block-copy algorithm to fill VRAM 
with the image data. There is also an "init" routine to copy the images as three separate chunks into VRAM. The init routine reads 
from a table of eighteen bytes at the very beginning of Bank2. I hope this structure is duplicated in other banks.

The massive block of images at the beginning of Bank2 is divided into two large and one smaller chunks:

```
807F -- 877E    Treasure picture images
877F -- 8E7E    Numbers, letters, punctuation, and symbols
8E7F -- 8F5E    Misc pictures (??)
```
With a little more POKEing around I found the letters for the treasure-descriptions in the splash sequence. They are offset exactly 
as they appear in the 877F area with '0' having a value of 0 and 'A' having a value of 10. The space character is 36 (one after 'Z').

# Game Flow

## December 25, 2009

Just a few instructions into the startup sequence the program makes it to E45B in bank 7. This is an endless loop where the main 
program spins for ever more. The game is driven by the NMI interrupt tick.

```
E45B: 4C 5B E4    JMP   $E45B         ; ENDLESS LOOP ... interrupt driven
```

# Battery Backed RAM

## December 26, 2009

At startup the program checks locations 6001 and 7FFF (battery backed ram). If the program does not find 5A in both, it clears a 
large chunk of the RAM.

# Sound

## December 29, 2009

The code in Bank 0 is filled with writes to the sound hardware. This bank seems to be exclusively sound. I will patch some of the 
data areas and hear the changes.

January 5, 2010

There are seven quick one-shot sound effects that can be played (one at a time) on the square-wave-1 channel. These include:

```
1 Anything bouncing off shield
2 Enemy death
3 ??
4 ??
5 Letters popping up when someone is talking
6 Picking a letter when entering a name
7 The near-death beep (played over and over)
```

Whenever one of these seven is requested it replaces any other effect being played with one exception. The near-heart beeping will 
NOT preempt an effect in play. The near-heart beeping is an ongoing effect that needs to run behind other effects.

It is possible (though rare) that two sound effects will be requested at the exact same time. In this case the table gives the 
priority. If (1) and (6) are requested at the same time, (1) will play. However, if (1) is requested and then a fraction of a 
second later (6) is requested then (6) will replace (1). The priority is only for this very rare simultaneous picking, and thus 
the special preemption logic hardcoded for the near-death beeping.

## January 24, 2010

I've been working on the sound code on and off. I just haven't been diligent in updating this journal.

Much thanks to James Vanderhyde for decoding two of the miscellaneous sound effects. He changed the "bouncing off shield" sound to 
the others and recognized Number3 is a wizzrobe magic attack and 4 is picking up a heart.

I have been focusing on the music data. I wrote a tool to decompose the music sequences into note values and beat counts.

## January 18, 2011

Almost a year later. I did beat Zelda: Twilight Princess since last here. Time to continue here. I'll take the next hobby session to 
reorient myself to the site.
