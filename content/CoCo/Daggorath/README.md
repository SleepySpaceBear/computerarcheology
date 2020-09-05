![Dungeons of Daggorath](Daggorath.jpg)

# Dungeons of Daggorath

>>> deploy:<br>
>>>   +Daggorath.jpg
>>>   +level1.svg<br>
>>>   +level2.svg<br>
>>>   +level3.svg<br>
>>>   +level4.svg<br>
>>>   +level5.svg<br>
>>>   +daggorath.js<br>
>>>   RAMUse.md<br>
>>>   Code.md<br>
>>>   ----<br>
>>>   Levels.md:Level Maps<br>
>>>   ----<br>
>>>   Journal.md<br>

TODO Overwrite the cassette code with a routine to ALLRAM. Then I can EXEC the ALLRAM, make
some POKE tweaks, and then EXEC 49152. Burn a new ROM.

# Code Links

* [Disassembled Code](Code.html)
* [RAM Usage](RAMUse.html)

>>> tourGuide {

# Tour Guide

>>> }

# Strategy

## Overview

http://dod.projects.l-w.ca/hg/index.cgi/shortlog/0fb9772b77fc

I like to beat the game in a long-and-drawn-out session that spans several days:

## Level 1: (15 or 20 minutes) 
* Kill most everything on the 1st level
* Use pine torches as needed
* Kill 2 Blobs (Iron Sword and Fire Ring), 4 Giants (Lunar and Pine torches), and lots of snakes (Wooden Sword and Leather Shield)

Your goal here is to get as many "bait" objects as you can. All creatures except the Wizard, Demon, and Scorpion will pick up
objects before they attack you. The more bait you have on the floor the more time you will have to kill a creature in your cell.

You don't have a scroll to navigate by on the first level. You can wander around until you find a hole,
or use these directions from your starting position to find the hole in the middle:

```
T A, M, T R, M, P L TO, U L, P R SW, T L, M M M, T L, M M M M M M M, T R
```

The door you see down the hall on the left is your guide. When you climb down, this is the direction you want to face.

## Level 2: (15 Minutes, Wait an hour, 15 Minutes, then Wait Overnight)
* Make your way all the way down the hall, turn right, and move straight to the hole in the bottom-left corner of this level.
* Get a Bronze shield in your hand and sit on a low power creature.
* Pull your Lunar Torch into an empty hand to put it out while you wait for an hour or so.
* The creatures will begin backing up in two long halls. Wait an hour or more.
* Kill ALL creatures on this level.
* Wait at least 3 hours on this level. I turn off the TV and wait over-night.

While you wait on this level the game creates random creatures for you to fight if/when you come back to this level. 
It takes 2.5 hours to create all 32 possible random creatures. Pull your torch and sit for an hour or two on a low
power creature. This will ensure all the other creatures lock on to you. Then kill them all. THEN pull your torch
and wait over night.

## Level 3: (30 Minutes)
* Unload all your bait. Watch carefully for the scorpions, which are difficult to see under LUNAR light.
* Kill, kill, kill. Accumulate bait.
* Get the SOLAR torch lit when you can (this lets you spot the scorpions).
* Drink the THEWS Flask when you get it.
* Be sure to kill all 4 Shield Knights.
* Lead the Demon off on a tangent as needed.
* When you are ready, pick up all the bait.
* Move all the way up the hall, turn right, move twice, turn right, move twice, turn around.
* Climb up.

## Repeat Level 2: (As many times as you want)
* This is the WHITE level.
* Go back to the bottom left corner.
* Drop all bait.
* Wait and kill everything you can. The more Galdrags you kill the better.
* After you kill everything wait at least 3 hours (I wait overnight).
* Find a ladder (I like the one near the upper-left). Climb down and back up. Repeat this process.

Use the HALE flasks as needed, but keep the rings in reserve. Try to take down at least TEN Galdrags 
in this up-and-down adventure. Use the LUNAR light as much as possible. Put the torches out when you 
can. Sit on low-powered creatures when you can.

The Level 2 (white level) is a particularly good level to build strength. In the bottom left you'll have
two long halls to attract creatures. When you finally get to Level 4 you'll want to be as powerful as 
possible since you'll have no bait objects.

## Level 3 Last Time (15 Minutes)

# Graphics

All the pictures are drawn in the upper 80% of the screen. This area is 256x152 pixels.

The images are all defined as drawn in the maze cell immediately in front of the player -- NOT the cell that the player is in. 
Many images drawn in the player's cell will clip off the screen.

The game draws lines (vectors), and the definition of an image is a list of vectors with some processing commands like 
jumps and subroutines. An image can be scaled as it is drawn. This gives the appearance that the image is far away or close up.
 An image is drawn with a bit-density that controls how often a bit in a line is drawn. Under crude light (like the pine torch) 
 images drawn two or three cells away contain only a few pixels making them hard to distinguish. 

The images for the giants and the knights each come in two forms. The club giant is the first type of giant you meet. 
The hatchet giant is much stronger. Both images use the same basic list of vectors and either a few lines for a club 
or a few lines for a hatchet. The knights also share the basic draw list but with a shield or a bare arm.

TODO describe the language

TODO describe the walls and scale factors

TODO table of images.


