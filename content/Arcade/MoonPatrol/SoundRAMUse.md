![Moon Patrol Sound RAM Use](MoonPatrol.jpg)

# Moon Patrol Sound RAM Use

>>> memory

| | | |
| --- | --- | --- |
| 0080      | seqV0                | Sequence voice 0 on AY0 (FF for off, count down to 0=process) |
| 0081      | seqV0                | Sequence voice 1 on AY0 (FF for off, count down to 0=process) |
| 0082      | seqV0                | Sequence voice 2 on AY1 (FF for off, count down to 0=process) |
| 0083      | seqV0                | Sequence voice 3 |
| 0084:0085 | seqPtr1              | Sequence pointer voice 0 |
| 0086:0087 | seqPtr2              | Sequence pointer voice 1 |
| 0088:0089 | seqPtr3              | Sequence pointer voice 2 |
| 008A:008B | seqPtr4              | Sequence pointer voice 3 |
| 008C      | seq1CmdType          | Type of command being processed on sequencer 1 |
| 008D      | seq2CmdType          | Type of command being processed on sequencer 2 |
| 008E      | seq3CmdType          | Type of command being processed on sequencer 3 |
| 008F      | seq4CmdType          | Type of command being processed on sequencer 4 |
| 0090      | cmdCnt               | Count of commands of the current type (if not 0). Resets to type 0 when done. |
| 0091      | m0091                | |
| 0092      | m0092                | |
| 0093      | m0093                | |

These eight bytes (2 per sequencer) are parameters for any complex commands.
The actual content depends on which complex command is being played.

>>> memory

| | | |
| --- | --- | --- |
| 0094:0097 | modeParams1          | Mode parameters (number 1) |
| 0098:009B | modeParams2          | Mode parameters (number 2) |
| 009C      | msbRetSeq1           | MSB of return address for script sequencer 0 |
| 009D      | msbRetSeq2           | MSB of return address for script sequencer 1 |
| 009E      | msbRetSeq3           | MSB of return address for script sequencer 2 |
| 009F      | msbRetSeq4           | MSB of return address for script sequencer 3 |
| 00A0      | lsbRetSeq1           | LSB of return address for script sequencer 0 |
| 00A1      | lsbRetSeq2           | LSB of return address for script sequencer 1 |
| 00A2      | lsbRetSeq3           | LSB of return address for script sequencer 2 |
| 00A3      | lsbRetSeq4           | LSB of return address for script sequencer 3 |
| 00A4      | cmdSeq1              | Sound command running on sequencer 0 |
| 00A5      | cmdSeq2              | Sound command running on sequencer 1 |
| 00A6      | cmdSeq3              | Sound command running on sequencer 2 |
| 00A7      | cmdSeq4              | Sound command running on sequencer 3 |
| 00A8      | volDec00             | not-zero to decrement volume on AY0-0 |
| 00A9      | volDec01             | not-zero to decrement volume on AY0-1 |
| 00AA      | volDec02             | not-zero to decrement volume on AY0-2 |
| 00AB      | volDec10             | not-zero to decrement volume on AY1-0 |
| 00AC      | volDec11             | not-zero to decrement volume on AY1-1 |
| 00AD      | volDec12             | not-zero to decrement volume on AY1-2 |
| 00AE      | volCnt00             | counter to decrement volume on AY0-0 |
| 00AF      | volCnt01             | counter to decrement volume on AY0-1 |
| 00B0      | volCnt02             | counter to decrement volume on AY0-2 |
| 00B1      | volCnt10             | counter to decrement volume on AY1-0 |
| 00B2      | volCnt11             | counter to decrement volume on AY1-1 |
| 00B3      | volCnt12             | counter to decrement volume on AY1-2 |
| 00B4      | volRel00             | reload for decrement volume on AY0-0 |
| 00B5      | volRel01             | reload for decrement volume on AY0-1 |
| 00B6      | volRel02             | reload for decrement volume on AY0-2 |
| 00B7      | volRel10             | reload for decrement volume on AY1-0 |
| 00B8      | volRel11             | reload for decrement volume on AY1-1 |
| 00B9      | volRel12             | reload for decrement volume on AY1-2 |
| 00BA      | curMix0              | current mixer value for AY0 |
| 00BB      | curMix1              | current mixer value for AY1 |
| 00BC      | sndCmd               | sound command (FF for none) |
| 00BD      | nmiTick              | NMI tick counter for non-NMI users |
| 00BE      | strmStatus           | status of sample streamers. 000000_AB A=801 (1=stopped), B=802 (1=stopped)|
| 00BF      | nmiTick2             | NMI tick counter |
| 00C0      | sndProcTmr           | timer for AY sound processing (0 means not time) |
| 00C1      | curSamp801           | current value of sampler 801 |
| 00C2      | curSamp802           | current value of sampler 802 |
| 00C3:00C4 | byteCnt801           | counter to bytes to play out 801 |
| 00C5:00C6 | byteCnt802           | counter to bytes to play out 802 |
| 00C7:00C8 | ptr801               | pointer to bytes to play out 801 |
| 00C9:00CA | ptr802               | pointer to bytes to play out 802 |
| 00CB      | lastCmd              | last requested sound command|
| 00CC      | m00CC                | Not used |
| 00CD:00CE | curSeqPtr            | temporary storage: current sequence pointer |
| 00CF:00D0 | tmpFreq              | temporary storage: used in frequency sweeper |
| 00D1:00D2 | curVoice             | temporary storage: current voice for sequence processing |
| 00D3:00D7 | m00D3                | Not used |
| 00D8      | brdStatus            | board status to return to main board. Set to $13 at start. Bit 0 is the status of the sample player. |

80 - CF cleared at startup (doesn't get all temporaries)

Stack builds to lower memory from FF
