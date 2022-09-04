![Omega Race](ORace.jpg)

>>> deploy:<br>
>>>   +ORace.jpg<br>
>>>   Hardware.md<br>
>>>   RAMUse.md<br>
>>>   MainBoard.md<br>
>>>   ----<br>
>>>   SoundHardware.md<br>
>>>   SoundRAMUse.md<br>
>>>   SoundBoard.md<br>
>>>   ----<br>
>>>  DVGPROM.md<br>
>>>  %VectorROM.md<br>
>>>  ----<br>
>>>  Journal.md<br>

# Omega Race

* [Main Board](MainBoard.md)
* [Sound Board](SoundBoard.md)
* [Vector ROM](VectorROM.md)
* [DVG PROM](DVGPROM.md)

# Diagnostics 

My friend Gary Dion is repairing his Omega Race board. He was telling me about the diagnostic LED flashes. I dug into the code to figure out what they mean.

Omega Race was a fun vector graphics game. Maybe I'll come back and finish the dig one day. Gary pointed me to a site describing a bug in the game -- a random 
line that appears. I would look for that. The game uses two AY38910 sound chips like the other sound boards I've spent so much time with. The sound board here is 
only 2K ROM. It would make a great addition to my collection of sound board digs.

# The DVG Digital Vector Generator

Most all modern computer displays use a "raster display" made of a grid of tiny dots (pixels). But several early arcade games used a "vector graphics display" instead. 
In vector graphics, the game creates a list of vectors (lines) and special hardware drives the electron beam in the monitor from points A to points B in order.

Philip Pemberton wrote a wonderful guide for the DVG used in Asteroids: [Hitch-Hacker's Guide to the Atari Digital Vector Generator](http://www.philpem.me.uk/elec/vecgen.pdf). 
Omega Race appears to use the same hardware.

The DVG is essentially a separate CPU that reads memory shared with the main game CPU. Most of the DVG instructions are vector commands, but there are JUMP, JUMP-SUBROUTINE, 
and RETURN-FROM-SUBROUTINE that control the DVG's flow through the vector list.

The DVG shares memory 8000-9FFF of the main CPU. The first 4K of this space (8000-8FFF) is RAM that the main CPU writes into. The second 4K of this space (9000-9FFF) is ROM 
that contains the sequences of vectors to draw the game pictures.

The main CPU writes the vector commands into memory beginning at 8000 and then tells the DVG to start. The DVG begins processing the created vector list beginning at 8000. The 
created vector list is primarily filled with "set coordinate" and "jump-subroutine" to call the ROM routines.

For instance, to print the message "HELLO" at the center of the screen the main CPU would write a LABS command (four bytes) to 8000. This command moves the X, Y coordinate to 
the desired screen location and sets the global scaling.

Then the main CPU would fill 8004 with a JUMP-SUBROUTINE command (2 bytes) to call the routine in ROM at 9910. This routine draws an 'H' on the screen. The main CPU adds JSR 
instructions for each of the other letters at 8006, 8008, 800A, 800C.

Finally the main CPU adds a HALT instruction (2 bytes) at the end of the list at 800E and tells the DVG to run the list. The "list" of vectors is really a "program" that the 
DVG follows, and the main CPU creates displays by writing DVG programs on the fly.

# TODO 

Comment out the sound board to identify the sound effects.

Search the main code for "OUT ($14),A" and match those to their sound effects from the main board.