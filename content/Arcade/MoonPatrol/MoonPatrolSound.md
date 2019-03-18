![Moon Patrol Sound](MoonPatrol.jpg)

# Mood Patrol Sound

[Sound Board Code](SoundCode.md)

# The Arcade Game

Moon Patrol is a classic arcade shoot'em-up side scroller. The player drives a moon buggy that jumps pits and shoots rocks and flying saucers. I thought the game itself 
was a bit boring, but the background bass groove was worth the quarter to play. Anyone walking past that game would leave the mall arcade with that classic 
riff stuck in his head. That bass groove is the target of this dig, but I'll also show you three bugs I found in the code.

But first I'll compare the code of three different sound boards and see how each approached sound in a slightly different way. All three boards are disassembled 
on this site: [Froger](../Frogger), [Time Pilot](../TimePilot) (both by Konami), and Moon Patrol.

# The Mechanics of Sound

Most sound effects fall into one of two categories: one-shot and ongoing. A one-shot sound is the audio record of an event. Examples include a laser firing, a frog 
jumping, and an alien exploding. These effects take a fraction of a second, and the code simply starts them and lets them run to completion.

An ongoing effect is the continuous sound of a game object. Examples include a racecar motor, a falling bomb, and a mother-ship traversing the screen. These effects 
usually take longer than a second and are often continuous. The code starts them up and stops them manually when the game object is removed.

Sound effects evolve over time. Imagine the quarter-second sound of an alien exploding. The effect starts loud and decays away to nothing by the end. The effect itself 
is mostly white noise (a random spread of frequencies), but the average frequency of the noise decays with time as well. The game code must change the volume and frequency 
of this effect from start to finish, which may not seem like a big deal. But a quarter of a second is a long, long time in the code world.

Music is the most complex sound effect of all. Musical notes are played at precise frequencies with precise timing. Unless you are coding up an ice-cream truck notes are 
not just pure sine waves that start and stop abruptly. Notes have complex waveforms with inherent harmonics (trumpets and flutes sound very different when playing the same 
note). Notes have volume envelopes; an instrument attacks a note hard but the note slowly (or quickly) fades with time.

Music usually plays as multiple notes (instruments) at the same time (harmony). Different instruments also play different rhythms of notes at the same time. For instance, 
a base groove running beneath a main melody.

There are usually limited sound resources. Only so many effects can be playing at any one time. When a sound effect needs to be played the code must look at what sound 
effects are currently playing and decide whether to preempt one or to ignore the new sound effect. Can a continuous sound (like music) be interrupted momentarily and then 
restarted? Resource scheduling is tedious. Sound effects are not something that is just added to the code later as to spice it up. Sound is an integral part of the code 
from the beginning.

# Sound Boards and Sound Hardware

Most arcade games use a dedicated sound board with its own CPU and sound-effect code. The main game board sends requests to the sound board to start/stop effects. The sound 
board decides which effects have what priority and how to schedule simultaneous sounds. The sound board manages all the simultaneous effects as the sounds evolve over time. The 
sound board processes music scripts.

Early arcade sound hardware provided a number of channels -- one channel for single playing sound effect. The hardware allowed the code to change the frequency and the volume 
of the channels independently.

The [General Instruments AY-3-8910](http://en.wikipedia.org/wiki/YM2149) sound chip was popular in arcade games and computers in the 80's. A single chip provides three 
independent channels. A sound board often used multiple AY chips. You have heard the AY voices in classics like 1942, Frogger, burger Time, Journey, Jungle Hunt, Scramble, 
Spy Hunter, Time Pilot, Tron, and Two Tigers to name a few.

The AY chip provides three independent voices labeled A, B, and C. A mixer register configures each voice as either a TONE, or NOISE, or off. Each voice has a 12-bit frequency 
control for its tone.

The voices have independently controlled frequencies. But the NOISE base frequency is controlled with a separate register. NOISE can thus be played through multiple voices, but 
the frequency is the same on all of them.

Each voice has an independent volume control register. The chip also has one complex volume (envelope) control circuit that can be configured to control a voice's volume. There 
is only one of these circuits to share among the three voices.

The envelope control has three registers to control is pattern, period, and repeating nature. A fast on/off warble that repeats is great for a firing laser sound. An envelope 
that dies off once is great for a gunshot (a NOISE effect). Since there is only one envelope control, it is impossible to have two sound effects using separate envelope controls 
at the same time.

The AY-3-8910 provides two general purpose 8-bit TTL compatible input/output ports. Sound boards often use these I/O ports receive commands from the main board.

# Three Solutions

Time Pilot uses a Z80 CPU and two AY-3-8910 chips. Moon Patrol uses a 6803 CPU and two AY-3-8910 chips. Frogger, the earliest board, uses a Z80 CPU and just one AY chip. Frogger 
is mostly two-voice music with a third voice for sound effects. Three voices were plenty.

Frogger and Time Pilot are both by Konami. They used similar solutions to sound. Both boards use a Switch Capacitor Audio Filter network. Each AY voice has two capacitors, 0.047uF 
and 0.220uF, that can be switched into the audio path. There are four possible filter capacitance configurations: none, 0.047, 0.220, or both added (0.267).

Frogger uses a Z80 CPU and 1 AY sound chip (3 voices). Konami included a SCAF on evolutions of the sound board. Time Pilot uses a Z80 and 2 sound chips. Moon Patrol uses 2 AY chips 
and a 6801 CPU.

## Threading 

Sound evolves over time. A thread is the code that changes the volume and frequency of a single sound effect over time. At any given moment there could be several threads manipulating 
different simultaneous sound effects.

Frogger and Time Pilot use a common approach. For Time Pilot there are six possible threads each tied to one of the six AY channels (two chips times three voices each). If a laser-blast 
is assigned to thread two then channel B of AY chip 1 is dedicated to the laser-blast from start to finish. Frogger has three threads mapped to its three voices (one chip).

Moon Patrol has six voices but only four threads. As we will see shortly, Frogger and !TimePilot map threads to channels with each thread having one channel. !MoonPatrol maps 
individual sound effects to individual channels with a thread. A thread manages several channels.

All three sound boards are time-driven. A main loop "ticks" at regular intervals and runs all threads for a brief time. Then the loop waits for the next tick and processes all 
threads again. The main board interrupts the loop briefly to request a new sound command. The interrupt service looks for an available thread to start the new sound on (see below).

The Moon Patrol main thread loop "ticks" at 250Hz. Time Pilot ticks at 175Hz. Frogger ticks at a blazing 700Hz (but only has three threads to process).

In Frogger and Time Pilot, the individual threads are implemented as Z80 code. Each sound effect has two routines: an initializer and a player. On the first tick of an effect 
the initialzer sets up the capacitors and initial states of the sound. From then on the thread calls the "player" routine on every tick. The player routine returns a flag to tell the main loop if the sound has ended or if it should continue next tick.

Moon Patrol, on the other hand, uses an interpreted language to implement the threads. Sound scripts are written in a domain-specific-language that contains jumps and subroutine 
calls and complex commands dedicated to sound. Why the trouble?

The pure-Z80 code requires the sound effect code to be aware of the threading. Instead of designing a sound effect from start to finish the developer has to build in 
return-and-come-back points in the algorithm to "give up the ball" for the other threads.

With the domain specific language, however, the sound script is developed from start to finish in a straight line without any knowledge of how/when the CPU breaks away to 
service the other threads. The sound algorithm is more straight-forward, but it requires the developer to learn a new (invented) language.

With the domain specific language the developer gets to focus on sound effects. The commands in the language are sound-specific. Sound developers don't have to be experts 
in Z80 programming. But the domain specific language requires an interpreter which eats up code space in ROM and CPU cycles when running.

## Moon Patrol Sound Language (MPSL)

I'm sure that's not what the designers called it -- MPSL. The Moon Patrol page describes these commands in great deal, but a quick overview will aid the discussion here.

There are "simple" commands and "complex" commands and commands to control program "flow". The flow commands are STOP, CALL subroutine, and RETURN from subroutine.

The simple commands allow the MPSL program to write to a value to any register on either chip with the REGISTER. The MPSL program gives the register number and the 
new value. There is a command to SET_VOLUME of a voice (voices 1-6). There is a command to set the automatic DECAY_SPEED of a voice.

There are three complex commands implemented in the code. REGISTER_SAMPLES plays a list of values to a single register one value every tick. It is only used in the UFO 
explosion effect. The TOGGLE_REGISTER command writes an alternating value to a single register every tick. This command is never used. There is a SWEEP command to change 
the value of a register from a starting value to an ending value over a specified time value.

## Scheduling 

There are usually multiple sound effects playing at the same time. Sound effects and music come and go independently of one another. Scheduling is the process of deciding 
which sound effects should be started on which threads. Sound effects have priorities. The coin-inserted sound, for instance, might be more important than a missile sound. 
If a missile sound is playing and a coin is inserted the scheduler can stop the missile sound and start the higher priority coin sound.

Frogger has 24 different sound effects that the main game board can request by number. The sound board uses a table to look up the priority of a sound. The higher the 
priority value in the table the more important the sound is. The frog-hopping sound, for instance, has the highest priority -- it will always be played. The scheduler 
will stop the lowest priority command and start the highest priority.

The separate music voices are handled as separate sound effects. The main board starts them one right after the other. The support (or harmony) voices have a lower 
priority, and if a lot of sounds are played the background voices will drop out.

Time Pilot has 28 different sounds that map to the six threads. Like in Frogger, each sound has a priority. But instead of looking up the command number in a table, the 
command number IS the priority. Thus if all six threads are playing sounds then command 11 (Squad Appears) will preempt command 3 (1910 bomb).

Letting the command number be the priority makes the sound board simpler. But it means that the priorities can't be changed without changing the main code. In Frogger, the 
priorities are in a table in the sound board. They can be changed without modifying the main code.

The Moon Patrol scheduling is radically different. Voices 1, 2, and 3 are dedicated to 3-voice music on thread 0. When the player's car explodes thread 0 stops the music 
and plays a 3 voice complex explosion effect.

During game play, the music is only 2 voices running on thread 0. The music plays on voices 1 and 2. Thread 1 is used to play continuous-alien-sounds on voice 3. Continuous 
sounds are the space-plant and the UFO-flying.

Voices 5 and 6 are dedicated to the car-jumping sound with thread 3. There is a lot of jumping in the game. The dedication is a good policy.

Thread 2 has full control of voice 4. There are four sounds that share that thread/voice. They use the priority-preempting schedule like Time Pilot and Frogger.

## Music 

Designing music is an artistic process that involves a starving composer and a piano. Rendering that music is the programmer's job and involves managing precise musical 
frequencies, precise musical timing, and note envelopes for starting and stopping.

Most modern pianos have 88 keys, each with a very specific frequency. The MIDI electronic music standard defines 128 note numbers. Note 60 maps to "Middle C", which has a 
frequency of 261.63Hz. The AY uses two registers to define a frequency value. But there are far fewer possible frequencies in music.

Frogger and Time Pilot use a note table to map a note number to a two-byte frequency. Remember the Time Pilot code is an evolved form of Frogger. Music processing is nearly 
identical, but Time Pilot adds some new features.

A song doesn't generally bounce all over the list of possible notes. The notes of a song are usually all with the same two or three octaves. Frogger and Time Pilot take 
advantage of this by defining a note as a five bit number (0 -- 31) added to a base note number. The base note number is set at the beginning of the song. This defines 
whether the music is a low instrument (like a base groove) or a higher main melody.

Moon Patrol in stark contrast has no note table at all. In fact it has absolutely no music processing at all. Music is coded just like all other sound effects. The notes 
are played by stuffing a two-byte value into the AY frequency registers for each note with the REGISTER command. This seems inefficient, but the upper byte of the two-byte 
value rarely changes. The music script ends up setting the AYs upper byte once and then changing the lower byte for each new note. Like Frogger and Time Pilot, the upper 
byte ends up defining the base note value and the lower byte ends up defining the individual notes.

Frogger and Time Pilot use 5-bit note numbers 0 -- 31. The upper three bits define the note length. The note length is converted to a power of two. For instance, a note length 
value of 1 is the shortest note. A value of 2 is twice as long as the shortest value (1*2 times longer). A value of 3 is twice as long again (1*2*2=4 times longer). A value 
of 4 is twice longer still (1*2*2*2=8 times longer).

This notation maps well to music, which is defined mostly in notes with power-of-two lengths like whole-notes, half-notes, quarter-notes, eighth-notes, etc. Music does allow 
for dotted notes and ties between notes that can't be represented as a power of two. But most music encodes nicely.

The base music interval -- the shortest note -- is configurable for the song. This is simply a count of the base ticks. This value defines the base tempo of the song. The Frogger 
code decrements the volume of the playing note automatically. The Time Pilot code decrements the volume too, but the rate is configurable on a per-voice basis.

Again, Moon Patrol doesn't have any specific music handling at all. The sound effect scripts delay the proper note length before playing the next note. In Frogger and Time Pilot, 
music timing is coded more naturally in powers-of-two. In Moon Patrol the timing is code manually in tick counts.

Frogger and Time Pilot treat note number 0 as a rest (silence) no matter what the base note adds in. They treat the value 31 as a flag that the upper 3 bits represent a special 
command. Thus there can be 8 special commands.

For Frogger the special commands look like this:
```
0 Set the base note value to the next byte in the music data
1 Set the base tempo value to the next byte in the music data
2 Set the voice's volume to the next byte in the music data
3 -- 7 Turn voice off and end music processing on the voice (frees the thread for other sounds)
```

For Time Pilot the special commands look like this:
```
0 Set the base note value to the next byte in the music data
1 Set the base tempo for the voice to the next byte in the music data
2 Set the voice's volume to the next byte in the music data
3 Reset current note's amplitude
4,5,7 Turn voice off and end the music process on the voice (frees the thread for other sounds)
6 Jump to new music address (next two bytes in the music data are absolute address)
```

# Moon Patrol Specific 

Moon Patrol on the Wiki: [http://en.wikipedia.org/wiki/Moon_Patrol](http://en.wikipedia.org/wiki/Moon_Patrol)

The heart of the sound software is a scripting language used to describe sound effects in a language that is more, well, sound-effect-ish. Specific details follow, but there 
are three basic types of commands in the language: simple commands (like set-a-register-on-a-chip), flow commands (CALL, RETURN), and complex commands that change a single 
voice frequency over a longer period of time.

The sound processor maintains four separate script "sequencers". Each sequencer maintains its own script pointer (or program counter) along with two bytes of state information. 
The software is driven by a 4000Hz clock on the non-maskable-interrupt of the processor. This clock is generated by the MSM5205 as it requests samples from the CPU. The software 
divides the clock by 16 and calls all four sequencers, one at a time, every 4Ms.

Each sequencer pulls its next command from its script, advances its script pointer, and processes the command. The command returns the number of ticks to wait before processing 
the next command.

The sequencers are like separate threads -- separate processors working on their own programs independently of each other. The scripting "virtual machine" takes care of twiddling 
the hardware and scheduling time for each script. Developers are free to focus on single sound scripts in isolation. They are free to use a scripting language more natural to sound 
effects instead of the more tedious general purpose 6803 instruction set. The concepts of "Domain Specific Languages" and "virtual machines" were rooted in these early arcade systems.

The NMI interrupt handler also writes bytes to the two 4-bit DACs to reproduce pre-recorded sounds. Moon Patrol only uses one of these DACs and only for one effect: a pre-recorded 
explosion sound. Even though the explosion lasts half a second, the samples eat up the 1st 1K of ROM in the sound processor -- that's 1/4th of the ROM.

# Sound Commands 

## Flow Commands 

There are three commands that control the flow of the script. The STOP command puts the sequencer in an idle state making it available for another sound script. The CALL command 
stores the current script address and jumps to a new target location in the script. The current script address is not stacked ... just stored in a single memory word. Thus the 
"call stack" is only one level deep, but you can just ignore the return address making the CALL a GOTO. Very clever. The RETURN command returns the script to the next command 
after the last executed CALL statement.

```
;  FF        - STOP  
;  FE MM LL  - CALL MMLL 
;  F0-FD     - RETURN
```

The sound processor can be configured to decrease the volume of each of the 6 voices independently. The AY chip has an envelope generator that does this automatically, but each 
chip has only one envelope generator to share among its three voices. This auto-decay functionality lets each voice die out at its own rate.

## Simple Commands 

The "simple commands" are five "quick" commands that poke single values into registers and configure the programmatic volume decay of each voice. Bit 6 of these commands is 
a "continue" bit. If the bit is set, the next command is executed on the same clock tick. This allows you to poke several registers at once with no delay between the writes. 
If the bit is clear, the next byte from the script is returned as the "delay until next command" value.

```
;  For all following commands, bit 6 is the multi-bit. If set, the parser is run again and again
;  until the bit is clear. Then the return value RV is loaded from the end of the sequence.
;
; REGISTER
;   0m0r_rrrr VV     *RV    Store single register value REGISTER(r)=VV
;
; THREEVOICE
;   0m1c_0000 FF CC  *RV    ThreeVoices FF=fine, CC=coarse
;
; MIXER
;   0m1c_011o VV     *RV    Mixer AND (o=0) or OR (o=1) AYc with VV
;
; SET_VOLUME_AND_RESET_DECAY
;   0m1c_10vv NN     *RV    Set volume reload value and volume register to NN
;
; VOLUME_DECAY_SPEED
;   0m1c_11vv NN     *RV    Set volume counter to reload value NN
```

The REGISTER command sets the value of a single 8-bit register on one of the two AY chips. The THREETONE command creates a tone-and-harmony effect on a single chip. Voice A 
gets the value CCFF. Voice B gets the value CCFF/2. And Voice C gets the value (CCFF/2 + 1). This generates a cool sound for the music effects like "Reaching Goal" 
and "Congratulations".

Each chip has a mixer that defines whether the individual voices are enabled and whether they map to tone or noise. The MIXER command modifies individual bits by first 
reading the current value from the chip then modifying the bits (AND or OR) and then writing the new value back.

The VOLUME_DECAY_SPEED command enables volume decay on a given voice and sets the time-between-decrements to the given value. This is usually called once at the start of 
an effect to configure the decay.

The SET_VOLUME_AND_RESET_DECAY command sets the volume level of the given voice (0-5) and resets the current counter to the value given by VOLUME_DECAY_SPEED. This is usually 
called multiple times in an effect to start a tone that automatically dies out.

## Complex Commands 

Finally, there are three "complex" commands. These commands modify AY registers over a longer period of time.

The C_REGISTER_SAMPLES command reads a list of samples and writes them to a target AY register every N ticks. The "UFO Explosion" is the only effect to use this command. It 
plays out 24 samples, one sample every 14 ticks, to the noise period register.

```
;C_REGISTER_SAMPLES
;  Set the value of rrrrr to sI at regular intervals. CNT is the number of samples.
;  Always return RVAL.
;  80 - 9F   100_r_rrrr CNT RVAL s0 s1 s2 ... sN
```

The C_TOGGLE_REGISTER command writes two alternating values to a target register. The CNT defines how many writes will occur, and RVAL defines the delay between each write. 
This command is never used in any of the scripts.

```
;C_TOGGLE_REGISTER
; (Never used)
;  Alternate writing I94 and I98.
;  Always return RVAL;
;  A0 - BF   101_r_rrrr CNT I94 I98 RVAL
```

The C_SWEEP_VOICE command adds (or subtracts) a delta value to a voice over a period of time. This allows you sweep a voice frequency from a start value to an end value by 
a defined increment (or decrement). The "Player Missile", for instance, is a single sweep starting at 0020 decrementing by one for 11 steps. There are 4 ticks (16Ms) 
between each change.

There are actually two flavors of the sweep command. The first sweeps a single register value. The second sweeps a two-byte voice-pair (fine and coarse). The two-byte form 
is never used, which is a good thing since there is a bug in the code.

```
;C_TOGGLE_REGISTER
; (Never used)
;  Alternate writing I94 and I98.
;  Always return RVAL;
;  A0 - BF   101_r_rrrr CNT I94 I98 RVAL

;C_SWEEP_VOICE_REGISTER
;  Add delta (I98) to current value (I94) and set-register
;  C0 - EF   110_r_0rrr CNT I94 I98 RVAL   

;C_SWEEP_VOICE_PAIR
; (Bug in code ... this function is never used)
;  Add delta (DELTA) to fine/coarse pair r0rrr and r0rrr+1. 
;  C0 - EF   110_r_1rrr CNT I94 I98 RVAL DELTA
```

# Code Bugs 

Here is the snippet of code that sweeps an AY voice (fine and coarse registers).

```plainCode
FD6E: A6 05       LDA     $05,X                   ;  Delta value from script
FD70: 36          PSHA                            ;  Hold delta (sign-check shortly)
FD71: DE D1       LDX     $D1                     ;  Voice number
FD73: AB 94       ADDA    $94,X                   ;  Adjust ...
FD75: A7 94       STA     $94,X                   ;  ... fine tone value
FD77: 32          PULA                            ;  Original delta
FD78: 2B 0C       BMI     $FD86                   ;  Handle decrementing
FD7A: 24 02       BCC     $FD7E                   ;  No carry
FD7C: 6C 98       INC     $98,X                   ;  Increment coarse tone

;BUG1
; BUG IN CODE
; We did the math above on $94 and $98 as if they were FINE/COARSE. But we write the
; values as if they are COARSE/FINE. Actually, the FINE value in $94 is never written
; to the fine register ... the DELTA value is always the FINE value.
; Good thing this command was never used!
;
FD7E: BD FC DD    JSR     $FCDD                   ;  Write fine value to register B
FD81: 5C          INCB                            ;  To coarse register
FD82: A6 94       LDA     $94,X                   ;  Coarse value (SHOULD BE $98)
FD84: 20 4B       BRA     $FDD1                   ;  Write coarse value to register B and return 4,x
```

At FD73 the code adds the delta to the fine value store in $94,X. At FD7C the code increments $98,X if there was an overflow from the fine value. It would appear 
that $94,X is the "fine" register and $98,X is the "coarse" register. The JSR at FD7E should write the fine-value from $94,X to the fine-register on the chip. 
Instead it writes the DELTA value. The code at FD82 and FD84 should write the coarse-value form $98,X to the coarse-register on the chip. Instead it writes the 
fine-value to the coarse-register.

I found two more bugs in the code that are really "potential problems". They don't cause errors for the current code but could cause problems in future reuse. 
Since this code is over 30 years old and nobody uses it anymore, the point is moot.

```plainCode
FF74: BD FC AD    JSR     $FCAD                   ;  Stop all sounds
...
FF83: 86 BE       LDA     #$BE                    ;  10_111_110
;BUG2
; The initialization at FCAD sets BA to 10_111_111. The OR here with a 0 is pointless.
FF85: 9A BA       ORA     $BA                     ;  Flag off all but ...
FF87: 97 BA       STA     $BA                     ;  ... AY0 tone A (THIS DOESN'T REALLY DO ANYTHING)
```

The routine FCAD sets the value of $00BA to all 10_111_111. The code at FF83 ORs a value with a zero bit. Thus we know this OR does not change anything. Whatever 
the developer intended to do here is not getting done.

The last bug I found is in the FCAD function called above to stop all sounds. As we will see next, sequencer 0 and 1 are tied to the first AY chip. Sequencer 2 and 3 
are tied to the second AY chip. In disabling sounds, this code also sets all of the sequencers to idle -- all sequencers except for sequencer 3, which handles the 
jumping effect. Since the mixer values are set to 1s (disable sound) the background jump is silenced even though sequencer 3 continues to write values to the chip.

## Sound Scripts, Sequencers, and Scheduling 

The main CPU controls the sound processor by writing a command byte to one of the AY38910's input ports and triggering the IRQ interrupt on the 6803. The sound processor 
reads the byte, a value from 0 to 31, to request sound functions.

```plainCode
;ExplosionCommands
;  Sample table for 801-played sample stream. First word is pointer to samples. Second
;  word is number of samples.
F400: 00 00 00 01      ;   00 (Not used ... gap in jump table for Reinitialize RAM and disable all sounds)
F404: F0 00 04 00      ;   01  $400 bytes at F000 Explosion: Car shooting rocks
F408: F0 04 00 E0      ;   02   $E0 bytes at F004 Explosion: Missiles hitting ground
F40C: F0 04 03 FC      ;   03  $3FC bytes at F004 Explosion: code plays 3 right after 2
F410: 00 00 00 01      ;   04
F414: 00 00 00 01      ;   05
F418: 00 00 00 01      ;   06
F41C: 00 00 00 01      ;   07
F420: 00 00 00 01      ;   08  Reserved slots for other DAC effects
F424: 00 00 00 01      ;   09
F428: 00 00 00 01      ;   0A
F42C: 00 00 00 01      ;   0B
F430: 00 00 00 01      ;   0C
F434: 00 00 00 01      ;   0D
F438: 00 00 00 01      ;   0E
F43C: 00 00 00 01      ;   0F
F440: 00 00 00 01      ;       I bet the original goal was to not include 00 and make 16 DAC's from 01 through 10

;CommandScripts
F444: F7 E1            ;   10 Passing one point (test 2)  AY1:A Sequencer2. If same ...
F446: F7 B9            ;   11 UFO explosion (test 3)      AY1:A ... restart. If higher ...
F448: F7 AB            ;   12 Missile from car (test 4)   AY1:A ... command number ...
F44A: F7 F1            ;   13 Coin (test 5)               AY1:A ... ignore.
F44C: F8 03            ;   14 Car jump (test 6)           AY1:BC  Force sequencer3
F44E: F4 F2            ;   15 Channel AY0:0 off and STOP  ---     Force sequencer1
F450: F4 F5            ;   16 Space plant (test 7)        AY0:A   Force sequencer1
F452: F5 16            ;   17 UFO flying (test 8)         AY0:A   Force sequencer1
F454: F5 6C            ;   18 Background music (test 9)   AY0:Bc  Force sequencer0
F456: F4 A7            ;   19 STOP                        ---     Force sequencer0
F458: F4 A7            ;   1A STOP                        ---     Force sequencer0
F45A: F4 64            ;   1B Ending music (test 10)      AY0:ABC Force sequencer0
F45C: F8 4D            ;   1C Opening music (test 11)     AY0:ABC Force sequencer0
F45E: F4 A8            ;   1D Reaching goal (test 12)     AY0:ABC Force sequencer0
F460: F8 EC            ;   1E Congratulations (test 13)   AY0:ABC Force sequencer0
F462: F9 5F            ;   1F Car explosion (test 14)     AY0:abc Force sequencer0
```

During game play, AY0 (chip 0) is very busy. The background music is dedicated to channels B (with tone) and C (with drum noise), and the effect is dedicated to 
sequencer 0. Channel A of AY0 handles the "continuous" sound effects: the flying saucers swirling above or the space plant.

AY1 handles the other come-and-go effects. Channels B and C are dedicated to the car jumping, and sequencer 3 is dedicated to the effect. Channel A on AY1 handles 
everything else: coin inserts, missiles from the car, UFO explosions, and passing strategic points in the game.

Since it is possible for these last effects to overlap, there is a priority schedule applied to the commands. If one of these four commands is requested but is 
already playing, the sound effect is restarted. This takes care of the player firing the missile in rapid succession. If a command of lower number is already 
playing, a higher requested command is ignored. Thus coin inserts are lower priority than missiles from the car, but passing a strategic point in the game will 
preempt the other four.

Remember that there is a short explosion effect that is played as samples through the DAC. This effect (player shooting rocks, saucers shooting ground) does not 
consume an AY voice or sequencer. This effect can play independently anytime.

The three-voice effect commands 27-31 are handled specially. When one of these is requested the entire sound processor resets itself! It reinitializes the 6803 
hardware registers and silences all voices on the AY chips, and it clears RAM as if it were starting up. Then the three-voice effect is played on all three channels 
of AY0 using sequencer 0. No matter what else is going on with the sound processor, when one of these commands is requested everything comes to a screeching halt.

I wrote a Java program to read the binary data from F464 to F986 and generate text disassembly of the scripts. This disassembly is what you see in the code. I wonder 
what the original scripting language looked like; what were the names of the commands and how did they represent the labels for CALLs?

# The Bass Groove 

We started out looking for the code for the background music of the game. Let's dig into the actual script. Refer to the script line numbers in the actual code.

On line 1 the VOLUME_DECAY_SPEED sets the volume decay value for voice 1 to 16.

In this case the volume of voice 1 (AY0:A) will be decreased by one every 16 ticks.

Line 2 sets the base frequency of the noise generator. The higher the number the deeper the noise. The value 0 makes the drum sound a very high pitch.

Lines 3 and 4 set the AY chip's envelope generator period. The background music does use the onboard generator to ramp down the volume on the drum sound. The higher the 
number, the slower the envelope evolves (in this case decays).

Line 5 sets the volume of the drum voice to use the envelope generator. Line 6 enables tone on channel B and noise on channel C.

If you listen to the background music you will notice that there are patterns in the song. It is actually composed of six different fragments. Lines 7 through 18 stitch 
these fragments together into the song. Line 19 jumps back to the top of the song.

Lines 20 -- 54 are the first fragment of the song. The background drum beats every 32 ticks (almost 8 beats a second). If we make this beat an eighth-note, then the notes 
themselves are entirely quarter-notes always lining up with the eighth-notes -- sometimes on the beat and sometimes off.

Lines 20 -- 23 are all executed on the same tick (utilizing the simple-commands "continue" bit). Line 20 and 21 writes the value 02A7 to the fine/coarse registers for 
voice B. Line 22 gets the tone started with automatic decay. Line 23 sets the noise period thus restarting the drum beat.

I modified the script-disassembler Java program to show the actual frequencies being played in the song. The asterisks show the drum beats. Where a tone is played, you 
see the actual produced frequency and the closest note on the piano keyboard.

# Corrections 

Tony G. pointed out that the company name is "Konami" and not "Kanomi". Thanks Tony.

