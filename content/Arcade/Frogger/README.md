![Frogger](Frogger.jpg)

>>> deploy:<br>
>>>   +Frogger.jpg<br>
>>>   +Frogger.js<br>
>>>   SoundHardware.md<br>
>>>   SoundRAMUse.md<br>
>>>   SoundCode.md<br>
>>>   Hardware.md<br>
>>>   Code.md<br>
>>>   RAMUse.md<br>
>>>   GFX.md<br>
>>>   FroggerFix.mp3<br>
>>>   Journal.md<br>

# Frogger

# Code Links

* [Disassembled Sound Code](SoundCode.md)
* [Sound RAM Usage](SoundRAMUse.md)
* [Sound Hardware Info](SoundHardware.md)

# Music to Hop By

From the moment you press start [Frogger](http://en.wikipedia.org/wiki/Frogger) plays a steady stream of music -- 26 different song 
fragments in all. You have to beat the first five levels and die to play them all! But even then there is one song you can never 
hear all the way to finish. The timer runs out before the main game song finishes. And even if you stop the timer (which I'll show 
you how to do) you still won't hear the complete song. There is a bug in the song data that shuts off the song's harmony voice near 
the end.

In this dig I'll show you how to fix the song data and unearth music buried deep in the Frogger ROM -- music never before heard 
since the game's release in 1981. Until now.

>>> tourGuide {

# Tour Guide 
Listen to the hidden music: [Hidden Music](#HiddenMusic)

>>> }

## The Mechanics of Sound 

I'll compare the code of three different sound boards and see how each approached sound in a slightly different way. 
All three boards are disassembled on this site: 
  * Frogger
  * [Time Pilot](../TimePilot) (also by Konami)
  * [Moon Patrol](../MoonPatrol)

Most sound effects fall into one of two categories: one-shot and ongoing. A one-shot sound is the audio record of an event. 
Examples include a laser firing, a frog jumping, 
and an alien exploding. These effects take a fraction of a second, and the code simply starts them and lets them run to completion.

An ongoing effect is the continuous sound of a game object. Examples include a racecar motor, a falling bomb, and a mother-ship 
traversing the screen. These effects usually 
take longer than a second and are often continuous. The code starts them up and stops them manually when the game object is removed.

Sound effects evolve over time. Imagine the quarter-second sound of an alien exploding. The effect starts loud and decays away to 
nothing by the end. The effect itself is 
mostly white noise (a random spread of frequencies), but the average frequency of the noise decays with time as well. The game code 
must change the volume and frequency of this 
effect from start to finish, which may not seem like a big deal. But a quarter of a second is a long, long time in the code world.

Music is the most complex sound effect of all. Musical notes are played at precise frequencies with precise timing. Unless you are 
coding up an ice-cream truck notes are not just
pure sine waves that start and stop abruptly. Notes have complex waveforms with inherent harmonics (trumpets and flutes sound very 
different when playing the same note). Notes have 
volume envelopes; an instrument attacks a note hard but the note slowly (or quickly) fades with time.

Music usually plays as multiple notes (instruments) at the same time (harmony). Different instruments also play different rhythms of 
notes at the same time. For instance, a base 
groove running beneath a main melody.

There are usually limited sound resources. Only so many effects can be playing at any one time. When a sound effect needs to be 
played the code must look at what sound effects are 
currently playing and decide whether to preempt one or to ignore the new sound effect. Can a continuous sound (like music) be 
interrupted momentarily and then restarted? Resource 
scheduling is tedious. Sound effects are not something that is just added to the code later as to spice it up. Sound is an integral 
part of the code from the beginning.

## Sound Boards and Sound Hardware

Most arcade games use a dedicated sound board with its own CPU and sound-effect code. The main game board sends requests to the 
sound board to start/stop effects. The sound board 
decides which effects have what priority and how to schedule simultaneous sounds. The sound board manages all the simultaneous 
effects as the sounds evolve over time. The sound 
board processes music scripts.

Early arcade sound hardware provided a number of channels -- one channel for single playing sound effect. The hardware allowed 
the code to change the frequency and the volume of 
the channels independently.

The [General Instruments AY-3-8910](http://en.wikipedia.org/wiki/YM2149) sound chip was popular in arcade games and computers 
in the 80's. A single chip provides three independent 
channels. A sound board often used multiple AY chips. You have heard the AY voices in classics like 1942, Frogger, burger Time, 
Journey, Jungle Hunt, Scramble, Spy Hunter, Time Pilot, 
Tron, and Two Tigers to name a few.

The AY chip provides three independent voices labeled A, B, and C. A mixer register configures each voice as either a TONE, or 
NOISE, or off. Each voice has a 12-bit frequency 
control for its tone.

The voices have independently controlled frequencies. But the NOISE base frequency is controlled with a separate register. NOISE 
can thus be played through multiple voices, but the 
frequency is the same on all of them.

Each voice has an independent volume control register. The chip also has one complex volume (envelope) control circuit that can 
be configured to control a voice's volume. There is only
 one of these circuits to share among the three voices.

The envelope control has three registers to control is pattern, period, and repeating nature. A fast on/off warble that repeats 
is great for a firing laser sound. An envelope that dies 
off once is great for a gunshot (a NOISE effect). Since there is only one envelope control, it is impossible to have two sound 
effects using separate envelope controls at the same time.

The AY-3-8910 provides two general purpose 8-bit TTL compatible input/output ports. Sound boards often use these I/O ports 
receive commands from the main board.

## Three Solutions 

Time Pilot uses a Z80 CPU and two AY-3-8910 chips. Moon Patrol uses a 6803 CPU and two AY-3-8910 chips. Frogger, the earliest 
board, uses a Z80 CPU and just one AY chip. Frogger is mostly 
two-voice music with a third voice for sound effects. Three voices were plenty.

Frogger and Time Pilot are both by Konami. They used similar solutions to sound. Both boards use a Switch Capacitor Audio Filter 
network. Each AY voice has two capacitors, 0.047uF and 
0.220uF, that can be switched into the audio path. There are four possible filter capacitance configurations: none, 0.047, 0.220, 
or both added (0.267).

Frogger uses a Z80 CPU and 1 AY sound chip (3 voices). Konami included a SCAF on evolutions of the sound board. Time Pilot uses 
a Z80 and 2 sound chips. Moon Patrol uses 2 AY chips 
and a 6801 CPU.

### Threading 

Sound evolves over time. A thread is the code that changes the volume and frequency of a single sound effect over time. At any 
given moment there could be several threads manipulating 
different simultaneous sound effects.

Frogger and Time Pilot use a common approach. For Time Pilot there are six possible threads each tied to one of the six AY 
channels (two chips times three voices each). If a laser-blast 
is assigned to thread two then channel B of AY chip 1 is dedicated to the laser-blast from start to finish. Frogger has three 
threads mapped to its three voices (one chip).

Moon Patrol has six voices but only four threads. As we will see shortly, Frogger and !TimePilot map threads to channels with 
each thread having one channel. !MoonPatrol maps individual 
sound effects to individual channels with a thread. A thread manages several channels.

All three sound boards are time-driven. A main loop "ticks" at regular intervals and runs all threads for a brief time. Then the 
loop waits for the next tick and processes all threads 
again. The main board interrupts the loop briefly to request a new sound command. The interrupt service looks for an available 
thread to start the new sound on (see below).

The Moon Patrol main thread loop "ticks" at 250Hz. Time Pilot ticks at 175Hz. Frogger ticks at a blazing 700Hz (but only has three 
threads to process).

In Frogger and Time Pilot, the individual threads are implemented as Z80 code. Each sound effect has two routines: an initializer 
and a player. On the first tick of an effect the 
initialzer sets up the capacitors and initial states of the sound. From then on the thread calls the "player" routine on every 
tick. The player routine returns a flag to tell the 
main loop if the sound has ended or if it should continue next tick.

Moon Patrol, on the other hand, uses an interpreted language to implement the threads. Sound scripts are written in a 
domain-specific-language that contains jumps and subroutine 
calls and complex commands dedicated to sound. Why the trouble?

The pure-Z80 code requires the sound effect code to be aware of the threading. Instead of designing a sound effect from start to 
finish the developer has to build in 
return-and-come-back points in the algorithm to "give up the ball" for the other threads.

With the domain specific language, however, the sound script is developed from start to finish in a straight line without any 
knowledge of how/when the CPU breaks away to service 
the other threads. The sound algorithm is more straight-forward, but it requires the developer to learn a new (invented) language.

With the domain specific language the developer gets to focus on sound effects. The commands in the language are sound-specific. 
Sound developers don't have to be experts in 
Z80 programming. But the domain specific language requires an interpreter which eats up code space in ROM and CPU cycles when 
running.

### Moon Patrol Sound Language (MPSL) 

I'm sure that's not what the designers called it -- MPSL. The Moon Patrol page describes these commands in great deal, but a 
quick overview will aid the discussion here.

There are "simple" commands and "complex" commands and commands to control program "flow". The flow commands are STOP, CALL 
subroutine, and RETURN from subroutine.

The simple commands allow the MPSL program to write to a value to any register on either chip with the REGISTER. The MPSL 
program gives the register number and the new value. There 
is a command to SET_VOLUME of a voice (voices 1-6). There is a command to set the automatic DECAY_SPEED of a voice.

There are three complex commands implemented in the code. REGISTER_SAMPLES plays a list of values to a single register one 
value every tick. It is only used in the UFO explosion 
effect. The TOGGLE_REGISTER command writes an alternating value to a single register every tick. This command is never used. 
There is a SWEEP command to change the value of a register 
from a starting value to an ending value over a specified time value.

### Scheduling 

There are usually multiple sound effects playing at the same time. Sound effects and music come and go independently of 
one another. Scheduling is the process of deciding which sound 
effects should be started on which threads. Sound effects have priorities. The coin-inserted sound, for instance, might be 
more important than a missile sound. If a missile sound is 
playing and a coin is inserted the scheduler can stop the missile sound and start the higher priority coin sound.

Frogger has 24 different sound effects that the main game board can request by number. The sound board uses a table to look 
up the priority of a sound. The higher the priority value 
in the table the more important the sound is. The frog-hopping sound, for instance, has the highest priority -- it will 
always be played. The scheduler will stop the lowest priority 
command and start the highest priority.

The separate music voices are handled as separate sound effects. The main board starts them one right after the other. The 
support (or harmony) voices have a lower priority, and if a 
lot of sounds are played the background voices will drop out.

Time Pilot has 28 different sounds that map to the six threads. Like in Frogger, each sound has a priority. But instead of 
looking up the command number in a table, the command number 
IS the priority. Thus if all six threads are playing sounds then command 11 (Squad Appears) will preempt command 3 (1910 bomb).

Letting the command number be the priority makes the sound board simpler. But it means that the priorities can't be changed 
without changing the main code. In Frogger, the priorities 
are in a table in the sound board. They can be changed without modifying the main code.

The Moon Patrol scheduling is radically different. Voices 1, 2, and 3 are dedicated to 3-voice music on thread 0. When the 
player's car explodes thread 0 stops the music and plays 
a 3 voice complex explosion effect.

During game play, the music is only 2 voices running on thread 0. The music plays on voices 1 and 2. Thread 1 is used to 
play continuous-alien-sounds on voice 3. Continuous sounds are 
the space-plant and the UFO-flying.

Voices 5 and 6 are dedicated to the car-jumping sound with thread 3. There is a lot of jumping in the game. The dedication is a 
good policy.

Thread 2 has full control of voice 4. There are four sounds that share that thread/voice. They use the priority-preempting 
schedule like Time Pilot and Frogger.

### Music 

Designing music is an artistic process that involves a starving composer and a piano. Rendering that music is the programmer's 
job and involves managing precise musical frequencies, 
precise musical timing, and note envelopes for starting and stopping.

Most modern pianos have 88 keys, each with a very specific frequency. The MIDI electronic music standard defines 128 note numbers. 
Note 60 maps to "Middle C", which has a frequency 
of 261.63Hz. The AY uses two registers to define a frequency value. But there are far fewer possible frequencies in music.

Frogger and Time Pilot use a note table to map a note number to a two-byte frequency. Remember the Time Pilot code is an 
evolved form of Frogger. Music processing is nearly identical, 
but Time Pilot adds some new features.

A song doesn't generally bounce all over the list of possible notes. The notes of a song are usually all with the same two 
or three octaves. Frogger and Time Pilot take advantage of 
this by defining a note as a five bit number (0 -- 31) added to a base note number. The base note number is set at the 
beginning of the song. This defines whether the music is a low 
instrument (like a base groove) or a higher main melody.

Moon Patrol in stark contrast has no note table at all. In fact it has absolutely no music processing at all. Music is coded 
just like all other sound effects. The notes are played by 
stuffing a two-byte value into the AY frequency registers for each note with the REGISTER command. This seems inefficient, 
but the upper byte of the two-byte value rarely changes. The 
music script ends up setting the AYs upper byte once and then changing the lower byte for each new note. Like Frogger and 
Time Pilot, the upper byte ends up defining the base note value 
and the lower byte ends up defining the individual notes.

Frogger and Time Pilot use 5-bit note numbers 0 -- 31. The upper three bits define the note length. The note length is converted 
to a power of two. For instance, a note length value 
of 1 is the shortest note. A value of 2 is twice as long as the shortest value (1*2 times longer). A value of 3 is twice as long 
again (1*2*2=4 times longer). A value of 4 is twice 
longer still (1*2*2*2=8 times longer).

This notation maps well to music, which is defined mostly in notes with power-of-two lengths like whole-notes, half-notes, 
quarter-notes, eighth-notes, etc. Music does allow for dotted 
notes and ties between notes that can't be represented as a power of two. But most music encodes nicely.

The base music interval -- the shortest note -- is configurable for the song. This is simply a count of the base ticks. This value 
defines the base tempo of the song. The Frogger code
 decrements the volume of the playing note automatically. The Time Pilot code decrements the volume too, but the rate is configurable 
 on a per-voice basis.

Again, Moon Patrol doesn't have any specific music handling at all. The sound effect scripts delay the proper note length before 
playing the next note. In Frogger and Time Pilot, music 
timing is coded more naturally in powers-of-two. In Moon Patrol the timing is code manually in tick counts.

Frogger and Time Pilot treat note number 0 as a rest (silence) no matter what the base note adds in. They treat the value 31 as a 
flag that the upper 3 bits represent a special command. 
Thus there can be 8 special commands.

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

## Frogger Specific 

On the sound board the D1 and D0 lines are swapped for the first chip. This is no doubt a mistake in the hardware that was 
just corrected in burning the ROM. The second graphics chip 
has the same problem.

Main board writes a command to the board that appears in port A of the AY chip. The hardware automatically generates a RST $38 
whenever a command is written. The ISR handles the 
scheduling. The main loop just plays whatever is scheduled.

Most sound commands are started and left alone. Some can be stopped and the main board sets an extra bit in the command to 
indicate "stop" instead of "start".

There are three threads to process commands. Each thread is hardcoded to one of the three AY voices. Each thread has a two-byte 
data structure.

The first byte of the two-byte structure is the command number 1 -- 24. A value of 0 means the thread is available for use. The second 
byte in the two-byte structure is the 
init-flag. If this value is 0 then the thread calls the sound command's initialization routine then sets the flag to 1. If the flag 
is 1 then the thread calls the sound command's 
continuation routine on every tick. The continuation routine returns a non-zero value to terminate the command.

There are three music-voice-structures used to manage music on any of the voices. Each structure has eight bytes. Byte 0 is the 
base delay counter. This is decremented each 
thread tick. When this value reaches zero it is reloaded from the global base-tempo value. On every other zero-crossing the volume 
of the voice is decremented by one.

Byte 1 is the note's delay value. This is decremented with every zero-crossing of byte 0. When this value reaches zero the note has 
ended and the music script continues to 
the next entry.

Bytes 2 and 3 are the pointer to the current entry in the music script.

Bytes 4 and 5 are the pointer to the base note number for the music. The music script defines notes 1 through 30 that are added to 
this base note.

Byte 6 is the current value of the note's volume as it decays away.

Byte 7 is the song's volume used to reload byte 6 at the start of every note.

There are several "process music on voice B" entries in the command table. They do exactly the same thing, but they have different 
command numbers and thus different priorities. 
This allows the code to make some background songs more important than others.

The interesting part is that the jump table points to different copies of the same code. It would have saved space to point the 
jumps to the same code. But the duplicated code 
is only 10 bytes per copy.

## Hidden Music

In order to hear all of the music in the main song you have to turn off the timer. Then you can sit patiently at the starting 
point and listen. Here is the patch file to turn 
the timer off (main board ROM) and fix the bug in the music.

```plainCode
;##$OriginalBinary frogger.26+frogger.27+frsm3.7

; Stop the two-byte timer
089E: 00              NOP
;089E: 77              LD      (HL),A      

08A3: 00              NOP
;08A3: 77              LD      (HL),A 

;##$OriginalBinary frogger.608(76543201)+frogger.609+frogger.610

1134: C2       ; Noticeable sour note (Change to this so that voice continues)
;1134: DF       ; SC06:Volume off and end song
```

TODO I am rethinking this. Later in the game this might be played.

The background voice of the main song has a "stop" command near the end, but there is music beyond the stop. This music has 
never been heard by anyone except the original game 
designers. In order to hear the music you have to replace the "stop" with a valid note. I tried to make the fixed note as 
obviously sour as possible so you can spot it in the 
song. Here is the recording of the main song played to completion.

[FroggerFix.mp3](FroggerFix.mp3 )

You can hear the sour note almost exactly at the 00:25 second mark in the song. That's where the lower background voice would 
have dropped out if you could have heard it. 
Interestingly the timer expires just about the same point. Near the end of the song the voices seem almost out of sync.

The intro 16 beats are from a Japanese song called Inu No Omawarisan (The Dog Policeman). 
[Listen to it on YouTube](https://www.youtube.com/watch?v=QIRpYwVpP4E).

The main song is from a Japanese anime called Araiguma Rascal. 
[Listen to the opening music](https://www.youtube.com/watch?v=2YMH5ntJEZ0).
