![Frogger Sound Board Hardware](Frogger.jpg)

# Sound Hardware

# AY38910 Chip

Port space addressing is straightforward.
If upper address bit 7 is set, value is written to chip address register.
If address bit 6 is set, value is written (or read) to chip register last addressed.

>>> memory

| | | |
| --- | --- | --- |
| 40p  | AY_DATA | Read/write the selected AY internal register |
| 80pw | AY_ADDR | Write here to select AY internal register |

# Capacitor Network

>>> memory

| | | |
| --- | --- | --- |
| 6000:6FFFw | caps | Capacitor network |

There is a capacitor filter control network controlled through memory addresses 
 decoded from 6000. Reading from an address sets the filter as follows:

 Address 0110_aa_bb_cc_dd_ee_ff<br>
 aa, bb, cc are AY chip 0 voices<br>
 dd, ee, ff are AY chip 1 voices (not used in this 1-chip hardware)<br>

 For each voice the two-bit data switches capacitors as follows:<br>
 00 None<br>
 01 0.220uF<br>
 10 0.047uF<br>
 11 0.047uF + 0.220uF<br>
