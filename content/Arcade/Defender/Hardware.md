![Defender Hardware](Defender.jpg)

# Hardware

```
 $0000..$BFFF is always RAM 
     stack pointer is initialized to $BFFF 
     $0000-$97FF Screen RAM 
     $A000-$BFFF General RAM 

 C000..CFFF is bank switched by writing the bank number to D000-DFFF as follows: 
  0: I/O and CMOS RAM space 
   $C000-$CFFF: Game I/O 
     $C000-$C00F: Color palette registers 
     $C010      : Screen control 
     $C3FC-$C3FF: Watchdog - write $38 or $39 to reset 
     $C400-$C7FF: Game Configuration CMOS RAM 
     $C800-$CBFF: Read 6 MSbits of Video Address Bus 
     $CC00-$CC03: ROM board PIA (sound output, input from coin door, and LED output) 
        $CC00: PIA 1,Channel A, bits 0-5 are inputs, 6-7 are outputs 
            Bits 0-5: Inputs from the coin door. A value of 1 indicates an active input. 
                Bit 0: auto/manual switch 
                Bit 1: advance button 
                Bit 2: right coin 
                Bit 3: high score reset 
                Bit 4: left coin 
                Bit 5: center coin 
            Bit 6: LED2 
            Bit 7: LED1 
        $C001: Both C pins are used.
            CA1: COUNT240 interrupt 
            CA2: SLAM (? don't know what that means, yet ) 
        $CC02: All bits are outputs 
            Bits 0-5: Sound board output 
            Bit 6: LED4 
            Bit 7: LED3 
        $CC03: Both C pins are used.
            CB1: 4mSec interrupt 
            CB2: Connected to pin 8 of sound board connector.  
                There is nothing on the sound board to change this from a 1 to a 0, so I presume at some point it must/can be switched to an output. Since it looks like this would prevent any interrupts being sent to the sound board CPU, it seems to me that it would be a good way to silence the arcade game. 

     $CC04-$CC07: Interface board PIA (input from player) 
        $CC04: All bits are inputs 
            Bits 0-3: 
        $CC05:  
            CA1: Grounded 
            CA2: Grounded 
        $CC06: All bits are inputs 
        $CC07: 
            CB1: Grounded 
            CB2: Select either player 1 or 2. 
  1: Bank1 (defend.9+defend.12) (2x2K) 
  2: Bank2 (defend.8+defend.11) (2x2K) 
  3: Bank3 (defend.7+defend.10) (2x2K) 
  4,5,6: No ROM chips 
  7: Bank7 (defend.6)  (2K) 
```

 $D000..$FFFF is always ROM ((defend.1+defend.4)(2x2K)+defend.2(4K)+defend.3(4K))

The original author of this page (name unknown) made this statement:

"Note that writes to ROM always fall through to the bank0 I/O and CMOS RAM space." 

This may actually appear to be a true statement, if all you have to go from is an imperfect simulator. I have not checked this out on MAME, or any other simulator, and I do not have a Defender arcade game, but I have analyzed the schematics, and I have rejected this as an erroneous statement. While a write to $D000-$DFFF will always change the page # of the $Cxxx memory, the address of a write to $Cxxx is always controlled by the ROM page #. 

If you disagree please send me an email with an explanation of why I am wrong. If you want to convince me, however, please begin by explaining the purpose of the subroutine located at $F7DB, in the Fixed bank.

# Screen RAM Layout

 From [Sean Riddle's page](http://seanriddle.com/ripper.html)

```
The display is 304 x 256 pixels, using 16 colors at a time out of a hardware palette of 256. 
The byte at memory location $0000 in the upper left-hand corner of the screen. 
4 bits are used for each pixel, so that byte displays as 2 pixels, side by side. 
The value of the 4 bits is used to offset into a lookup table, and the contents of that location 
in the table determine the color displayed for that pixel. 
Memory location $0001 displays as 2 pixels immediately below, $0002 is below that one, etc. 
The bottom left corner of the screen is memory location $00FF. 
Memory location $0100 displays the 3rd and 4th pixels in the top line. 
Note that the monitor may not display all the pixels, depending on how it is set up. 
Generally the top and bottom of the display are adjusted off the screen with overscan.
```
