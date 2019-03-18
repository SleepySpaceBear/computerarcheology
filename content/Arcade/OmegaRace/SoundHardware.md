![Omega Race Sound Hardware](ORace.jpg)

# Sound Hardware

>>> memory

| | | |
| --- | --- | --- |
| 00pw      | AY0ADDRESS       | Address for AY0 |
| 00pr      | SOUNDCMD         | Command from main CPU |
| 01pw      | AY0VALUE         | Value for AY0 |
| 02pw      | AY1ADDRESS       | Address for AY1 |
| 03pw      | AY1VALUE         | Value for AY1 |

```
 /* audio CPU */
 /* XTAL101 Crystal @ 12mhz */
 /* through 74LS161, Pin 12 = divide by 8 */
 /* Fed to CPU as 1.5mhz though line J4-D */
 MDRV_CPU_ADD("audiocpu", Z80,12000000/8)
 MDRV_CPU_PROGRAM_MAP(sound_map, 0)
 MDRV_CPU_IO_MAP(sound_port, 0)
 MDRV_CPU_PERIODIC_INT(nmi_line_pulse,250)
```
