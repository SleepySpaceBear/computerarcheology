%%title = Pyramid 2000
%%image = Pyramid.jpg

{{{html
<div class="playMe">
<div>
<script src="/CoCo/Pyramid/BinaryDataPyramid.js"></script>
<script src="/js/6809.js"></script>
<script src="/CoCo/CoCoText.js"></script>
<script src="/CoCo/Pyramid/pyramid.js"></script>
<script>window.onload = function() {startPyramid("pyramidConsole","pyramidTape");}</script>
}}}
# Play Me! 
Play the game in a CoCo emulator. Click on the green console and press any key.

{{{html
<textarea readonly id="pyramidConsole" rows="16" style="background-color: #00FF01; color: black;font-family: monospace;font-size:12px;width:33ch;" ></textarea>

<div id="cocoTapeArea" style="display:none">
The text area below is the virtual cassette tape. Instead of writing to tape, the emulator writes data as two-digit hex
values to this text area.</p>

The SAVE command will write 260 bytes (520 characters)
to the text box. You must select all the characters (CNTRL-A) and copy them (CNTRL-C). Then store them
in a text file for later use. </p>

Before the LOAD command you must paste the desired saved-data back into the text area.</p>

<textarea id="pyramidTape" rows="8" style="font-size:8px;width:80ch;" ></textarea>
</div>
</div>
</div>
}}}

# Code Links

* [Disassembled Code](Code.html)
* [RAM Usage](RAMUse.html)

# The Great Lost Pyramid

"The seal on the entrance is still unbroken -- perhaps the tomb is still intact,
untouched by the passage of time, impervious to the elements, still settled in
quiet repose. There must be treasures. If even half of the stories about the Lost
Pyramid are true, ... But why dwell on that now -- you are here, and adventure
awaits just a step away." - From the game manual introduction

{{{tourGuide

# Tour Guide 

Check out a [snippet of the original source code](#TRS80Nugget) caught in an uninitialized buffer.

Have a look at the [game's main loop](Code.html#MainLoop). It is really short.

The code is code-within-code. The adventure language processor commands are [here](Code.html#ScriptCommands).

The spooky mummy is given life as part of the [Move to Room X](Code.html#MoveToRoomX) code.

Have a look at all the unpacked messages in the game:
* [General Messages](Code.html#AlternatingErrors)
* [Room Descriptions](Code.html#RoomDescriptions)
* [Object Descriptions](Code.html#ObjectDescriptions)
* [More General Messages](Code.html#GameSpecificMessages)

Visit the [Room Scripts](Code.html#RoomScripts) to see what you can do in each room. Then visit the 
[General Command Handler](Code.html#GeneralCommandHandler) script that runs after the current room
has a chance to take the command. These "adventure language scripts" are interpreted by the [Script Processor](Code.html#ProcessCommandList).

Read through all words that the game understands in the [Word table](Code.html#WordTable).
}}}

# References

If you seek specific game information, solutions, and online emulators then check out Sean Murphy's wonderful site.[[br]]
Solutions and info on Pyramid 2000, Raaka-Tu, and Bedlam:[[br]]
[http://www.figmentfly.com](http://www.figmentfly.com)

In August 2007 my article on 
[Text Adventure Gaming](http://www.cc-webshop.com/Circuit-Cellar-Issue-205-August-2007-PDF-FI-2007-205.htm) 
was published in Circuit Cellar magazine. I ported the game to play on a Propeller microcontroller.

# Colossal Cave Adventure

The Wikipedia says that Colossal Cave Adventure was the first computer text adventure game. The original source, recovered from 
Don Wood's student account at Stanford, is about 700 lines of FORTRAN with another 700 lines of data. It ran on giant mainframe 
computers in the mid 1970s. Many versions of the game began to appear shortly after. David Platt's Adventure550 was among the 
most popular. It featured an adventure language he called A-code and an interpreter for the language written in FORTRAN. Platt 
translated the game logic into his A-code language and enhanced it to score a max of 550 points.

All things Colossal Cave Adventure:
[http://en.wikipedia.org/wiki/Colossal_Cave_Adventure](http://en.wikipedia.org/wiki/Colossal_Cave_Adventure)

David Platt's A-code version of Adventure550:
[http://www.mipmip.org/adv550/src550a.shtml](http://www.mipmip.org/adv550/src550a.shtml)

# TRS-80 and CoCo
 
In 1979 Radio Shack released Robert Arnstein's Pyramid 2000 for the TRS-80 Model I. The game is basically a port of David Platt's A-code 
Adventure550 with the setting changed to a pyramid instead of a cave. The dungeon layout and error messages are almost identical. Arnstein's 
version is stripped down a bit to fit on a home computer, and Arnstein developed his own domain specific language and interpreter that is 
much simpler than Platt's A-code.

The TRS-80 Color Computer hit the market in 1980, but it wasn't until 1982 that 16K models were affordable. It was then that Arnstein ported 
the Model I version of Pyramid to the CoCo. The CoCo version is even smaller, and we will see in the code where functionality was removed 
but references were left behind.

Arnstein developed several text adventure games in the years to follow. In 1981 Raaka-Tu was released for the TRS-80 and Coco. It is a dungeon 
crawler similar to Pyramid but features a complex expression parser allowing commands like LIGHT CANDLE WITH LAMP. Raaka-Tu's adventure language 
is more advanced allowing the environment to come alive with patrolling guards and a serpent that follows you from room to room.

In 1982 Arnstein's BEDLAM landed the player in an insane asylum. There is no score keeping in the game: you either escapes or don't. The command 
line for BEDLAM is even more complex than Raaka-Tu using adjectives to distinguish RED doors from GREED ones. The objects in the adventure 
language become game participants themselves. The player must give Napoleon, X-Ray Johnson, and Houdini commands and interact with them to win. 

I will follow Arnstein's adventure language and interpreter as it evolved from Pyramid 2000 to Raaka-Tu and finally to Bedlam. Be sure to 
visit those pages as well:
* Pyramid 2000
* [Raaka Tu](/CoCo/RaakaTu)
* [Bedlam](/CoCo/Bedlam)

# Pyramid 2000 Implementation

The game includes colorful responses to certain command requests -- like rubbing the lamp:

{{{html
<div class="cocoScreen"> 
}}}
RUBBING THE ELECTRIC LAMP IS NOT[[br]]PARTICULARLY REWARDING. ANYWAY,[[br]]NOTHING EXCITING HAPPENS.
{{{html
</div>
}}}

Colossal Cave is based on an actual section of Mammoth Cave in Kentucky. Pyramid 2000 changes the setting from a cave to a pyramid, but the original 
flow and most of the descriptions are still based on Mammoth Cave.

In Adventure, the description for the place labeled "WENDMISTS" is:

"You are at the west end of Hall of Mists. A low wide crawl continues west and another goes north.  To the south is a little passage 6 feet off the floor."

In Pyramid 2000, the description for Room 19 is almost identical:

{{{html
<div class="cocoScreen"> 
}}}
YOU ARE AT THE WEST END OF THE[[br]]
HALL OF GODS. A LOW WIDE PASS[[br]]
CONTINUES WEST AND ANOTHER GOES[[br]]
NORTH. TO THE SOUTH IS A LITTLE[[br]]
 PASSAGE SIX FEET OFF THE FLOOR.
{{{html
</div>
}}}

# The Engine 

When you turn on the 16K TRS-80 Color Computer, the first 1K of memory is reserved for the BASIC interpreter. The next 512 bytes is reserved for the 
text mode screen map (32 characters per line * 16 rows = 512 bytes). That leaves 0x4000 - 0x600 = 14848 bytes of memory in the system for the Pyramid 
game, which is 14625 bytes long. The programmers had to do some squeezing to get the game to fit in 16K. They left out some rooms and objects, and they 
trimmed down the commands in the sub-language as we will see.

The first 2862 bytes of the game are the 6809 assembly implementation of the adventure-engine. The remaining 11763 bytes are data: the game scripts, object 
and room tables, and vocabulary.

The main game loop reads a line from the user and parses it against a known list of words. It looks for an action word (a VERB) and an optional target 
NOUN. Verbs like "NORTH" and "CLIMB" stand alone, but "DROP" and "EAT" require a NOUN to act on.

The main loop looks up the script for the current room and processes the VERB/NOUN. Most of the rooms just specify MOVE-TO locations for various 
directions. Some room scripts handle special actions like waving the scepter.

If the room's script does not handle the player's input then the main loop runs a very large general purpose script that handle inputs in every room. 
This general purpose script takes care of GETS and DROPS and LOOKS and INVENTORY. It also includes some colorful error messages if you try to eat things 
or feed things or otherwise behave strangely in the dungeon.

There is a routine executed after every user action. This routine handles some complex behaviors that are difficult to code in the adventure-script language. 
For instance, this routine counts the "turns" and times out the lamp. If the lamp dies, the routine will automatically change the batteries if you are 
carrying them. The routine also counts the treasures in your pack. If you have more than 2 the routine cues the Mummy to come in and move them to the 
treasure chest in the maze. This routine also tosses you in a pit if you walk around in the dark.

The engine code takes care of printing all messages on the screen. This includes auto-wrapping words at the end of each line and pausing the spew with 
a -MORE- prompt so the user doesn't miss anything. The most ingenious piece of code in the game (and the one that frustrated me the longest) is the 
message decompression routine.

A byte holds a value of 0-255. The Color Computer text mode only prints upper-case characters, and the game only uses a few punctuation marks. In fact, 
the game only prints 40 different characters. Storing a value ranging from 0-39 in a memory location that holds values from 0-255 wastes a lot of 
precious space. The game cleverly packs 3 characters into 2 bytes. 40*40*40 = 64000 combinations for three characters. Two bytes hold 65536 combinations. 
That's almost a perfect fit, and it compresses strings by 33%.

I wrote a Java utility to uncompress the strings in the code listing. You'll find all the packed strings uncompressed near the bottom of the code. 
Take a few moments to read through them! It's a great trip down memory lane.

# Adventure Language

The data area of the game is made of several data tables, the room scripts, the common-script, the packed strings, and the vocabulary. I wrote a java 
program to parse this data area and make great comments in the data section of the game.

The RoomTable at 0x112E contains 2 words for each room. The first word is the address of the description of the room. The second word is the address 
of the script for the room. Notice that rooms 67, 69, 74, and 75 have null pointers. These rooms are never "GO TO" targets from any other room. This 
must be part of the strip-down to fit in 16K, but notice that only the scripts and descriptions were removed -- the room table was not renumbered to 
close the gaps.

The AmbientLight table at 0x17EB contains a word for each of the 81 rooms. A single bit int the 16-bit word indicates if the room has light of its 
own or if it needs the lamp. This is a huge waste of space .... 16 bits to hold a single boolean. Why?

In the original Adventure code, there are lots of attributes that can be applied to each room. The code from Adventure:

{{{
SYNON    0,LIT         {Place is self-illuminated}
SYNON    1,BEENHERE    {We've been here at least once}
SYNON    2,NODWARF     {Dwarves can't go here}
SYNON    3,NOBACK      {Can't use BACK to go to/from this place}
SYNON    4,NOTINCAVE   {This place is not in the cave}
SYNON    5,HINTABLE    {There may be a hint for this place}
SYNON    6,H20HERE     {Water is available here}
SYNON    7,INMAZE      {This room is in one of the mazes}
SYNON    8,ONE.EXIT    {Only one exit out of room - dwarves can block your way and force you to fight them.}
SYNON    9,THROWER     {Throwing objects here will send them elsewhere, unless you're throwing them at something special (like a troll or dwarf).}
SYNON    12,DAMP       {The ground is damp here because he poured water or oil from the bottle}
}}}

The Pyramid 2000 code carries the storage for these attributes even though only one bit is used. 

The adventure scripting language itself is straightforward. I wrote a java program to turn the binary script into readable text as comments in the disassembly.

The first byte of each script segment is the token for the word (or words) that match the action. The remainder of the segment is what to do if the 
input word matches. Have a look at the script for Room 1 at 1272:

{{{
; Room 1
; "YOU ARE STANDING BEFORE THE ENTRANCE OF A PYRAMID. AROUND YOU IS A DESERT.[CR]"
1272: 01 03          ; N,NORTH
1274: 01 02          ;     MoveToRoomN  Room:2
1276: 02 03          ; E,EAST
1278: 01 03          ;     MoveToRoomN  Room:3
127A: 03 03          ; S,SOUTH
127C: 01 04          ;     MoveToRoomN  Room:4
127E: 04 03          ; W,WEST
1280: 01 05          ;     MoveToRoomN  Room:5
1282: 0B 03          ; IN,INSIDE
1284: 01 02          ;     MoveToRoomN  Room:2
1286: 00
}}}

If the user input matches "NORTH" then the script executes function "MoveToRoomN" passing in the value 2. The player moves to room 2. The segment 
completes (passes) and the script stops.

The script processor moves from segment to segment until one passes. A "pass" stops the processing dead in its tracks. Otherwise the room script 
continues to the end of the room script and if no segment matches then the "common" script is run.

The scripting engine has a "sub-script" ability that groups a series of commands and reverses the pass/fail status. Look at the script for Room 12:

{{{
; Room 12
; "AT YOUR FEET IS A SMALL PIT BREATHING TRACES OF WHITE MIST. AN EAST PASSAGE ENDS ..."
132D: 02 03          ; E,EAST
132F: 01 0B          ;     MoveToRoomN  Room:11
1331: 0A 0B          ; D,DOWN
1333: 07 07          ;     SubScriptRev
1335: 02 25          ;       AssertObjectNIsInPack Object:"Gold Nugget"
1337: 04 30 8A       ;       PrintMessageNN "YOU ARE AT THE BOTTOM OF THE PIT WITH A BROKEN NECK.[CR]"
133A: 05             ;       PrintScoreAndStop
133B: 01 0D          ;     MoveToRoomN  Room:13
133D: 04 04          ; W,WEST
133F: 04 30 AF       ;     PrintMessageNN "THE CRACK IS FAR TOO SMALL FOR YOU TO FOLLOW.[CR]"
1342: 00
}}}

If the user types DOWN the script enters a sub-script that asserts that the "Gold Nugget" is in the backpack. If the nugget is not in the backpack 
the assertion fails and the sub-script fails. But sub-script statuses are reversed so it actually passes and moves to the next command ... MoveToRoom 13.

If the nugget is in the pack however, the sub script continues with a death message and an endless loop. Don't try to climb down into the pit with 
the gold nugget in your pack!

It takes a little getting used to, but you should be able to follow the scripts through the code comments. Some of the scripts, especially in the 
common script, have nested sub-scripts several layers deep.

The script functions themselves are assembly routines in the engine that handle primitives like moving target objects from room to room (including 
the backpack). There are functions to print messages and turn one object into another. One function, the "AssertPackIsEmptyExceptForEmarald" has a 
very specific purpose for one room only. You'll find a complete list of these script functions in the script-commands-table in the code.

The object table at 0x18ED gives the pointer to the description of each game object. Objects 3, 4, 5, 10, 12, and 13 have been removed from the game 
but again -- the table was not renumbered to remove the gaps. There are no NOUN words in the vocabulary to refer to these missing objects.

But the common-script does contain reference to these objects! The original would complain if you tried to EAT object 10. It would say "I think I 
just lost my appetite!". And it would complain if you tried to FEED anything object 13. It would say "There is nothing here it wants to eat -- 
except perhaps you!".

There are several objects in the original Adventure that generate these messages: BEAR, TROLL, BIRD, SNAKE, DWARF, DRAGON, BASILISK, and GOBLINS. 
Maybe one of these removed-objects was in a room that got removed? At any rate, the common script was never cleaned up.

If you look through the script, you'll see several rooms that handle an unknown command to move the player to room 26. There are no VERB words in 
the vocabulary that match command number 0x20. But with a little digging, we can figure out what the missing command is.

I compared the Adventure code to the Pyramid code and found that Room 26 in Pyramid is Room Y2 in Adventure.

Room Y2 in Adventure is:

You are in a large room, with a passage to the south, a passage to the west, and a wall of broken rock to the east.  There is a large "Y2" on a 
rock in the room's center.

Room 26 in Pyramid is:

{{{html
<div class="cocoScreen"> 
}}}
YOU ARE IN A LARGE ROOM, WITH A [[br]]
PASSAGE TO THE SOUTH, AND A WALL[[br]]
OF BROKEN ROCK TO THE EAST.[[br]]
THERE IS A PANEL ON THE NORTH WALL.
{{{html
</div>
}}}

Then I compared the GOTOs to Room 26 in Pyramid to the GOTOs to Room Y2 in Adventure. Sure enough -- they line up perfectly. So the missing direction 
command in Pyramid is the "Y2" command from Adventure.

# TRS-80 Nugget

I looked briefly at the TRS-80 version of the Pyramid code. The game objects are the same. The descriptions are all the same except for double spaces 
after periods in the TRS80 version. The scripts are the same too, but the TRS80 vocabulary includes one extra word: "HELP".

I didn't comment the Z80 opcodes (yet), but I glanced through a hex dump of the code to find the ASCII strings. I ran across a fascinating accident 
in the TRS80 code.

In both CoCo and TRS80 versions of the game, there are ASCII strings that include 40-byte buffers to be filled in with words copied from the user's 
input buffer. If you type "THROW BLAHBLAHBLAH", for instance, the game will fill the buffer with "BLAHBLAHBLAH" and say 
"WHAT DO YOU WANT ME TO DO WITH THE BLAHBLAHBLAH?".

The original assembly code must have used a "RESERVE MEMORY" directive to declare these buffers instead of blanking them with initial value. When 
the assembler created the binary code, it skipped over these reserved holes and left whatever was in memory. In the CoCo case, the original memory 
was FFs and 00s ... not very interesting. But here are the contents of the TRS-80 version (I added the ASCII conversion to the side):

{{{
; "WHAT DO YOU WANT ME TO DO WITH THE "
464D:  57 48 41 54 20 44 4F 20 59 4F 55 20 57 41 4E 54 20 4D 45 20 54 4F 20 44 4F 20 57 49 54 48 20 54 48 45 20 
; 40 byte buffer for unknown noun word
4670:  2C 41 0D 12 30 30 30 30 20 20  ; ,A..0000  
467A:  4C 58 49 20 48 2C 52 41 4C 31  ; LXI H,RAL1
4684:  0D 14 30 30 30 30 20 43 4E 41  ; ..0000 CNA
468E:  4C 4C 20 4D 4F 56 20 41 2C 4D  ; LL MOV A,M
; "?"
4698:  3F 00 

; 40 byte buffer for unknown verb
469A:  30 30 30 30 20 20 49 4E 58 20  ; 0000  INX 
46A4:  48 0D 0D 30 30 30 30 20 20 41  ; H..0000  A
46AE:  4E 41 20 41 0D 10 30 30 30 30  ; NA A..0000
46B8:  20 20 4A 5A 20 43 4E 41 4C 4C  ;   JZ CNALL
;" WHAT?",0
46C2:  20 57 48 41 54 3F 00 
}}}

Piecing the text together looks like this: 

{{{
 --------------,A
(12) 0000  LXI H,RAL1
(14) 0000 CNALL MOV A,M-
(--) 0000  INX H
(0D) 0000  ANA A
(10) 0000  JZ CNALL
}}}

This memory contained the source code for the pyramid game itself! The assembler tool the developers were using must have reused this section of 
memory, and the memory originally contained the program. Thus the binary image contains a small snapshot of the original pre-assembled text. 
Very, very cool!

Notice the opcodes are 8080 flavors. The TRS80 used the Z80 processor and not the 8080. The Z80 is backwards compatible with the 8080, but the 
code contains Z80 specific instructions like "4516: CB 01 RLC C". Perhaps the developers were more familiar with the 8080 and used an assembler 
that allowed the older mnemonics along with the new? It remains a mystery.

After a little searching I found the matching segment in the disassembly:

{{{
55ED: 47              LD      B,A                 ; To B
55EE: 21 69 49        LD      HL,$4969            ; Start of room scripts
55F1: 7E              LD      A,(HL)              ; Get byte from script
55F2: 23              INC     HL                  ; Next in script
55F3: A7              AND     A                   ; 00?
55F4: CA F1 55        JP      Z,$55F1             ; Yes ... ignore
}}}

In the original source, the label "CNALL" is at 55F1. The data at address 4969 is called "RAL1". This data location is the start of the room 
scripts. This code is part of the script command executed when you enter the command "PLUGH".

In the CoCo version of the game, PLUGH does nothing. But in the TRS80 version the code run through the scripts for all the rooms and "rolls" 
the NORTH, SOUTH, EAST, and WEST directions by a random offset! You type NORTH but you go EAST instead.
