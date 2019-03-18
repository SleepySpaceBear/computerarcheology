![DVG PROM](ORace.jpg)

# DVG PROM

```

     Omega Race has two pairs of the state PROM output
     lines swapped before going into the decoder.
     Since all other avg/dvg games connect the PROM
     in a consistent way to the decoder, we swap the bits
     here. 
 for (i=0; i&ltlen; i++) prom[i] = BITSWAP8(prom[i],7,6,5,4,1,0,3,2);

Courtesy of Mr. Gary Dion

Original dvgprom.bin dump:
 
       0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F
 
00h   00 04 07 07 05 09 0D 07  06 07 04 00 0F 03 0A 0B 
10h   00 04 07 07 05 09 0D 07  06 07 04 00 0F 03 0A 0B 
20h   00 04 07 07 05 09 0D 07  06 07 04 07 0F 03 0E 0B 
30h   00 04 07 07 05 09 0D 07  0E 07 04 00 02 03 0A 0B 
40h   00 04 07 07 05 09 0D 07  06 07 04 00 02 03 0A 0B 
50h   00 04 07 07 05 09 0D 07  06 07 04 00 06 03 0A 0B 
60h   00 04 07 07 05 09 0D 07  06 07 04 00 06 03 0A 0B 
70h   00 04 07 07 05 09 0D 07  06 07 04 00 0A 03 0A 0B 
 
80h   06 08 07 07 05 09 0D 07  06 07 04 00 0F 03 0A 0B 
90h   06 08 07 07 05 09 0D 07  06 07 04 00 0F 03 0A 0B 
A0h   06 08 07 07 05 09 0D 07  06 07 04 07 0F 03 0E 0B 
B0h   06 08 07 07 05 09 0D 07  0E 07 04 00 02 03 0A 0B 
C0h   06 08 07 07 05 09 0D 07  06 07 04 00 02 03 0A 0B 
D0h   06 08 07 07 05 09 0D 07  06 07 04 00 06 03 0A 0B 
E0h   06 08 07 07 05 09 0D 07  06 07 04 00 06 03 0A 0B 
F0h   06 08 07 07 05 09 0D 07  06 07 04 00 0A 03 0A 0B
 
 
Byte swapped for 3,2,1,0 -> 1,0,3,2:
 
       0  1  2  3  4  5  6  7   8  9  A  B  C  D  E  F
 
00h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 0F 0C 0A 0E 
10h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 0F 0C 0A 0E 
20h   00 04 0D 0D 05 06 07 0D  09 0D 04 0D 0F 0C 0B 0E 
30h   00 04 0D 0D 05 06 07 0D  0B 0D 04 00 08 0C 0A 0E 
 
40h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 08 0C 0A 0E 
50h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 09 0C 0A 0E 
60h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 09 0C 0A 0E 
70h   00 04 0D 0D 05 06 07 0D  09 0D 04 00 0A 0C 0A 0E 
 
80h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 0F 0C 0A 0E 
90h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 0F 0C 0A 0E 
A0h   09 02 0D 0D 05 06 07 0D  09 0D 04 0D 0F 0C 0B 0E 
B0h   09 02 0D 0D 05 06 07 0D  0B 0D 04 00 08 0C 0A 0E 
 
C0h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 08 0C 0A 0E 
D0h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 09 0C 0A 0E 
E0h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 09 0C 0A 0E 
F0h   09 02 0D 0D 05 06 07 0D  09 0D 04 00 0A 0C 0A 0E
 
Decoding States:
 
State 08 - SPUSH/
State 09 - SPOP/
State 0A - SGO/
State 0B - SSTOP/
State 0C - STORE2/
State 0D - STORE1/
State 0E - STORE0/
State 0F - STORE3/
```