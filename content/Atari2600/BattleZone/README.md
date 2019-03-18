![Battle Zone](A2600Battlezone.jpg)

>>> deploy:<br>
>>>   +A2600Battlezone.jpg<br>
>>>   RAMUse.md<br>
>>>   Code.jd<br>
>>>   ----<br>
>>>   Journal.md<br>

# Battle Zone

[Battle Zone Code](Code.md)

>>> { playMe

# Play Me!

It might take a few seconds for the ROM to load, but play Atari2600 BattleZone here:

[http://javatari.org&ROM=BattleZone](http://javatari.org?ROM=https://github.com/topherCantrell/computerarcheology/blob/master/content/Atari2600/BattleZone/Batlzone.bin?raw=true)

>>> }

# The Banks

There are two ROM banks in the !BattleZone cartridge. Like in Missile Command, Atari put the bank switching logic in the ROM chip to save chip-count 
and thus cost. When the program accesses FFF9 the chip switches to the upper 4K of code (Bank 1). When the program access FFF8 the chip switches to 
the lower 4K of code (Bank 0). The "read/write" line is not delivered to the cartridge. The code reads from these locations to switch banks.

The code in Bank 0 is assembled as addresses D000-DFFF. The code in Bank 1 is assembled as addresses F000-FFFF. Only A0..A12 are delivered to the 
cartridge. The upper address bits are for the human reader.

Both banks have a bank-switching function at the end of memory at xFF2. The first instruction here switches the ROM bank to the "other" bank. The next 
instruction is a "jump" statement. Code running in Bank 0 jumps to DFF2, which switches to Bank 1 and continues at F019. Code running in Bank 1 jumps 
to FFF2, which switches to Bank 0 and continues at D003.

The RESET vector in Bank 1 points to F003. The RESET vector in Bank 0 points to D000. The three byte instruction at D000 flips to Bank 1 and the code 
continues at F003. Thus pressing the reset button in either bank takes the CPU to F003 in Bank 1. This is the startup code.

Bank 0 is the visible part of the video kernel. It takes over at scanline 40 and draws everything the player sees. At scanline 234 Bank 1 takes over 
and handles the non-visual game logic. This is a nice separation of responsibility.

# Player Hit Sequence

There are two views in the visual video kernel. The "normal" view is what the player sees most of the time: the radar at the top, the mountains, the 
terrain, and the tank at the bottom.

The "fuzzy" view is what the player sees when his tank has been hit.

The "fuzzy" view is created by setting the background color and tracing four lines using the player objects (2) and the missile objects (2).

TODO dig into the background-color and line algorithm in Bank 0.

When the player is hit, the code at F229 writes the value $80 into the hit-sequence counter >$C1. This counter decrements with each screen drawn. Early 
in the sequence ($80 to $58) the display alternates between the "normal" view and the "fuzzy" view every other frame. The rapid interlacing merges in 
the player's mind making the normal view look fractured.

Late in the sequence ($57 to $01) the changing "fuzzy" view is drawn every frame.

At 60 frames per second (NTSC) the player-hit sequence takes 2 seconds. The first second is the normal/fuzzy view. The last second is just the fuzzy view.