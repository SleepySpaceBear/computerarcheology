![Sound Board Hardware](TimePilot.jpg)

# Sound Hardware

There are two capacitors that can be switched onto each audio channel
to ground. The MSB bit set to one selects a 0.22uF and the LSB bit set selects
a 0.047uF cap. Most effects just switch out the caps (writing 00), but the
explosion effects switch in one or the other (never both).

```
V1 1000xxxxAAxxxxxx
V2 1000xxAAxxxxxxxx
V3 1000AAxxxxxxxxxx
V4 1000xxxxxxxxxxAA
V5 1000xxxxxxxxAAxx
V6 1000xxxxxxAAxxxx
```

>>> memory

| | | |
| --- | --- | --- |
| 4000 | AY0_DATA | |
| 5000 | AY0_ADDR | |
| 6000 | AY1_DATA | |
| 7000 | AY1_ADDR | |
