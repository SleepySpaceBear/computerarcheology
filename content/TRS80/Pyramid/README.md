![Pyramid](TRS80Pyramid.jpg)

# TRS80 Pyramid
>>> deploy:<br>
>>>   +TRS80Pyramid.jpg<br>
>>>   +trs80pyramid.js<br>
>>>   +BinaryDataTRS80Pyramid.js
>>>   RAMUse.md<br>
>>>   Code.md<br>
>>>   ----<br>
>>>   RAMUse1.md<br>
>>>   Code1.md<br>
>>>   ----<br>
>>>   Journal.md<br>

```html
<script src="/TRS80/Pyramid/BinaryDataTRS80Pyramid.js"></script>
<script src="/js/Z80.js"></script>
<script src="/TRS80/TRS80Text.js"></script>
<script src="/TRS80/Pyramid/trs80pyramid.js"></script>
<script>window.onload = function() {startTRS80Pyramid("trs80PyramidConsole","trs80PyramidTape");}</script>
```

>>> playMe {

# Play Me! 
Play the game in a TRS80 emulator. Click on the black console and press any key.


```html
<textarea id="trs80PyramidConsole" rows="16" style="wrap:hard;background-color: black;color: white;font-family: monospace;font-size:12px;width:65ch;" ></textarea>

<div id="tapeArea" style="display:none">
The text area below is the virtual cassette tape. Instead of writing to tape, the emulator writes data as two-digit hex
values to this text area.</p>

The SAVE command will write 260 bytes (520 characters)
to the text box. You must select all the characters (CNTRL-A) and copy them (CNTRL-C). Then store them
in a text file for later use. </p>

Before the LOAD command you must paste the desired saved-data back into the text area.</p>

<textarea id="trs80PyramidTape" rows="8" style="font-size:8px;width:80ch;" ></textarea>
</div>
```

>>> }

# Code Links

* [Disassembled Code](Code.md)
* [RAM Usage](RAMUse.md)

# CoCo Implementation

The TRS80 Color Computer implementation is identical to the TRS80 implementation except for the general script. The
TRS80 has a FIND command that prints "I CAN ONLY TELL YOU WHAT YOU SEE AS YOU MOVE ABOUT AND MANIPULATE THINGS. I CAN NOT TELL YOU WHERE REMOTE THINGS ARE." and a HELP command that prints "I'M AS CONFUSED AS YOU ARE.".

These two commands (and their strings) were removed from the CoCo version.

[CoCo Pyrarmid](../../CoCo/Pyramid)

# Messages for 64 Columns 

The compressed message strings contain spaces to pad the words out to 64 columns (the size of the monitor). For instance:

```
; IT_IS_NOW_PITCH_DARK.__IF_YOU_PROCEED,_YOU_WILL_LIKELY_FALL_INTOA_PIT.[CR]
7976: 17 73 7B 4B 7B 09 9A E3 16 9A BD FB 14 6F B2 4B 
7986: 13 9B 64 1B A1 F9 A6 A7 53 73 5D C7 DE FB 17 F3 
7996: 8C 8D 8C 53 61 4B 15 F3 8C 9E 7A FB 9D 96 A5 2E 
79A6: 00 
```

The word "INTO" ends at the right edge of the monitor. The next character "A" is printed at the start
of the next line.

The CoCo version of this code uses a auto-word-wrap feature that adds spaces to keep letters of a word together
on the same line. The CoCo screen is only 32 characters wide. The strings would have had lots of wasted
spaces to format for the CoCo. 

When you are reading through the strings here you'll see odd spacing and words run together. That's why. The
strings are hand-formatted to the TRS80 64-column monitor.

# References 

If you seek specific game information, solutions, and online emulators then check out [Sean Murphy's wonderful site](http://www.figmentfly.com).
