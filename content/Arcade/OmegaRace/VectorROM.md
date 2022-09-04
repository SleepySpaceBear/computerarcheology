![DVG Vector ROM](ORace.jpg)

# Omeg Race DVG Vector ROM

>>> cpu DVG

>>> binary 9000:roms/omega.e1 + roms/omega.f1

For info about the vector generator hardware and opcodes:<br>
[DVG Information](../Asteroids/DVG.html)

The player ship sprites are first and last in the ROM. Each picture draws the player just a
little rotated CCW from the original position (facing right). Pictures come in pairs. The first
picture is the thrust stream for the ship. The second picture is the ship. The thrust stream
is drawn right where the ship picture ends.

 Note that there is no perfectly vertical picture. In the game you can't point perfectly vertical.

```code
ShipsA:
; The first ship image below shows the thrust pattern.
```

# Player (Part 1) 

```html
<canvas width="1225" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-colors='["#FFFFFF","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#635629","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C"]'
  data-origin="9000"
  data-command="baseScale=1,x=50,y=50,900E,9000,x=125,y=50,904E,x=200,y=50,9090,x=275,y=50,90D2,x=350,y=50,9116,x=425,y=50,9156,x=500,y=50,9192,x=575,y=50,91D2,x=650,y=50,9212,x=725,y=50,9250,x=800,y=50,9290,x=875,y=50,92D0,x=950,y=50,930C,x=1025,y=50,934C,x=1100,y=50,9390,x=1175,y=50,93D2">
</canvas>
```

```code
; Thrust fragment                                                               
9000: BF 30 FF 07     VEC     scale=3(/64) x=-3FF y=BF   i=0   (-15.98 ,   2.98 )
9004: BF 34 3F F6     VEC     scale=3(/64) x=-23F y=-BF  i=15  ( -8.98 ,  -2.98 )
9008: 7F 34 3F F2     VEC     scale=3(/64) x=23F  y=-7F  i=15  (  8.98 ,  -1.98 )
900C: 00 D0           RTS                         
; Player facing right
900E: 00 20 7F 02     VEC     scale=2(/128)x=27F  y=0    i=0   (  4.99 ,   0.00 )
9012: 3F 41 7F F6     VEC     scale=4(/32) x=-27F y=13F  i=15  (-19.96 ,   9.96 )
9016: 9F 46 5F F1     VEC     scale=4(/32) x=15F  y=-29F i=15  ( 10.96 , -20.96 )
901A: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
901C: 7F 34 7F F6     VEC     scale=3(/64) x=-27F y=-7F  i=15  ( -9.98 ,  -1.98 )
9020: FF 41 1F F2     VEC     scale=4(/32) x=21F  y=1FF  i=15  ( 16.96 ,  15.96 )
9024: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
9028: FF 24 7F F6     VEC     scale=2(/128)x=-27F y=-FF  i=15  ( -4.99 ,  -1.99 )
902C: FF 41 1F F6     VEC     scale=4(/32) x=-21F y=1FF  i=15  (-16.96 ,  15.96 )
9030: 7F 34 7F F2     VEC     scale=3(/64) x=27F  y=-7F  i=15  (  9.98 ,  -1.98 )
9034: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
9036: 9F 46 5F F5     VEC     scale=4(/32) x=-15F y=-29F i=15  (-10.96 , -20.96 )
903A: 1F 41 7F F2     VEC     scale=4(/32) x=27F  y=11F  i=15  ( 19.96 ,   8.96 )
903E: 00 D0           RTS                         
;
9040: 3F 30 FF 07     VEC     scale=3(/64) x=-3FF y=3F   i=0   (-15.98 ,   0.98 )
9044: BF 34 3F F6     VEC     scale=3(/64) x=-23F y=-BF  i=15  ( -8.98 ,  -2.98 )
9048: 7F 34 3F F2     VEC     scale=3(/64) x=23F  y=-7F  i=15  (  8.98 ,  -1.98 )
904C: 00 D0           RTS                         
;
904E: 00 20 7F 02     VEC     scale=2(/128)x=27F  y=0    i=0   (  4.99 ,   0.00 )
9052: FF 40 9F F6     VEC     scale=4(/32) x=-29F y=FF   i=15  (-20.96 ,   7.96 )
9056: 5F 46 9F F1     VEC     scale=4(/32) x=19F  y=-25F i=15  ( 12.96 , -18.96 )
905A: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
905C: BF 34 7F F6     VEC     scale=3(/64) x=-27F y=-BF  i=15  ( -9.98 ,  -2.98 )
9060: 3F 42 FF F1     VEC     scale=4(/32) x=1FF  y=23F  i=15  ( 15.96 ,  17.96 )
9064: FF 24 7F F2     VEC     scale=2(/128)x=27F  y=-FF  i=15  (  4.99 ,  -1.99 )
9068: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
906C: BF 41 3F F6     VEC     scale=4(/32) x=-23F y=1BF  i=15  (-17.96 ,  13.96 )
9070: 3F 34 7F F2     VEC     scale=3(/64) x=27F  y=-3F  i=15  (  9.98 ,  -0.98 )
9074: 7F 24 FF F7     VEC     scale=2(/128)x=-3FF y=-7F  i=15  ( -7.99 ,  -0.99 )
9078: BF 46 1F F5     VEC     scale=4(/32) x=-11F y=-2BF i=15  ( -8.96 , -21.96 )
907C: 5F 41 5F F2     VEC     scale=4(/32) x=25F  y=15F  i=15  ( 18.96 ,  10.96 )
9080: 00 D0           RTS                         
;
9082: 00 30 FF 07     VEC     scale=3(/64) x=-3FF y=0    i=0   (-15.98 ,   0.00 )
9086: FF 25 FF F7     VEC     scale=2(/128)x=-3FF y=-1FF i=15  ( -7.99 ,  -3.99 )
908A: 3F 34 3F F2     VEC     scale=3(/64) x=23F  y=-3F  i=15  (  8.98 ,  -0.98 )
908E: 00 D0           RTS                         
;
9090: 7F 20 7F 02     VEC     scale=2(/128)x=27F  y=7F   i=0   (  4.99 ,   0.99 )
9094: BF 40 BF F6     VEC     scale=4(/32) x=-2BF y=BF   i=15  (-21.96 ,   5.96 )
9098: 5F 46 DF F1     VEC     scale=4(/32) x=1DF  y=-25F i=15  ( 14.96 , -18.96 )
909C: FF 20 FF F3     VEC     scale=2(/128)x=3FF  y=FF   i=15  (  7.99 ,   1.99 )
90A0: FF 34 3F F6     VEC     scale=3(/64) x=-23F y=-FF  i=15  ( -8.98 ,  -3.98 )
90A4: 5F 42 9F F1     VEC     scale=4(/32) x=19F  y=25F  i=15  ( 12.96 ,  18.96 )
90A8: F3 F5           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
90AA: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
90AE: 7F 41 7F F6     VEC     scale=4(/32) x=-27F y=17F  i=15  (-19.96 ,  11.96 )
90B2: 3F 30 BF F2     VEC     scale=3(/64) x=2BF  y=3F   i=15  ( 10.98 ,   0.98 )
90B6: FF 24 FF F7     VEC     scale=2(/128)x=-3FF y=-FF  i=15  ( -7.99 ,  -1.99 )
90BA: DF 46 DF F4     VEC     scale=4(/32) x=-DF  y=-2DF i=15  ( -6.96 , -22.96 )
90BE: 9F 41 3F F2     VEC     scale=4(/32) x=23F  y=19F  i=15  ( 17.96 ,  12.96 )
90C2: 00 D0           RTS                         
;
90C4: 3F 34 FF 07     VEC     scale=3(/64) x=-3FF y=-3F  i=0   (-15.98 ,  -0.98 )
90C8: FF 26 FF F7     VEC     scale=2(/128)x=-3FF y=-2FF i=15  ( -7.99 ,  -5.99 )
90CC: 00 30 7F F2     VEC     scale=3(/64) x=27F  y=0    i=15  (  9.98 ,   0.00 )
90D0: 00 D0           RTS                         
;
90D2: 7F 20 7F 02     VEC     scale=2(/128)x=27F  y=7F   i=0   (  4.99 ,   0.99 )
90D6: 7F 40 BF F6     VEC     scale=4(/32) x=-2BF y=7F   i=15  (-21.96 ,   3.96 )
90DA: 1F 46 1F F2     VEC     scale=4(/32) x=21F  y=-21F i=15  ( 16.96 , -16.96 )
90DE: 7F 21 7F F3     VEC     scale=2(/128)x=37F  y=17F  i=15  (  6.99 ,   2.99 )
90E2: 3F 35 3F F6     VEC     scale=3(/64) x=-23F y=-13F i=15  ( -8.98 ,  -4.98 )
90E6: 7F 42 7F F1     VEC     scale=4(/32) x=17F  y=27F  i=15  ( 11.96 ,  19.96 )
90EA: 7F 24 7F F2     VEC     scale=2(/128)x=27F  y=-7F  i=15  (  4.99 ,  -0.99 )
90EE: 7F 26 FF F5     VEC     scale=2(/128)x=-1FF y=-27F i=15  ( -3.99 ,  -4.99 )
90F2: 5F 41 9F F6     VEC     scale=4(/32) x=-29F y=15F  i=15  (-20.96 ,  10.96 )
90F6: 7F 30 7F F2     VEC     scale=3(/64) x=27F  y=7F   i=15  (  9.98 ,   1.98 )
90FA: 7F 25 7F F7     VEC     scale=2(/128)x=-37F y=-17F i=15  ( -6.99 ,  -2.99 )
90FE: DF 46 7F F4     VEC     scale=4(/32) x=-7F  y=-2DF i=15  ( -3.96 , -22.96 )
9102: 7F 33 FF F3     VEC     scale=3(/64) x=3FF  y=37F  i=15  ( 15.98 ,  13.98 )
9106: 00 D0           RTS                         
;
9108: BF 34 FF 07     VEC     scale=3(/64) x=-3FF y=-BF  i=0   (-15.98 ,  -2.98 )
910C: FF 26 7F F7     VEC     scale=2(/128)x=-37F y=-2FF i=15  ( -6.99 ,  -5.99 )
9110: 3F 30 7F F2     VEC     scale=3(/64) x=27F  y=3F   i=15  (  9.98 ,   0.98 )
9114: 00 D0           RTS                         
;
9116: FF 20 7F 02     VEC     scale=2(/128)x=27F  y=FF   i=0   (  4.99 ,   1.99 )
911A: 1F 40 DF F6     VEC     scale=4(/32) x=-2DF y=1F   i=15  (-22.96 ,   0.96 )
911E: DF 45 3F F2     VEC     scale=4(/32) x=23F  y=-1DF i=15  ( 17.96 , -14.96 )
9122: F2 F9           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
9124: 7F 27 FF F7     VEC     scale=2(/128)x=-3FF y=-37F i=15  ( -7.99 ,  -6.99 )
9128: BF 42 1F F1     VEC     scale=4(/32) x=11F  y=2BF  i=15  (  8.96 ,  21.96 )
912C: 7F 24 FF F2     VEC     scale=2(/128)x=2FF  y=-7F  i=15  (  5.99 ,  -0.99 )
9130: 7F 26 FF F5     VEC     scale=2(/128)x=-1FF y=-27F i=15  ( -3.99 ,  -4.99 )
9134: 1F 41 BF F6     VEC     scale=4(/32) x=-2BF y=11F  i=15  (-21.96 ,   8.96 )
9138: BF 30 BF F2     VEC     scale=3(/64) x=2BF  y=BF   i=15  ( 10.98 ,   2.98 )
913C: F6 FD           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
913E: DF 46 3F F4     VEC     scale=4(/32) x=-3F  y=-2DF i=15  ( -1.96 , -22.96 )
9142: FF 33 BF F3     VEC     scale=3(/64) x=3BF  y=3FF  i=15  ( 14.98 ,  15.98 )
9146: 00 D0           RTS                         
;
9148: FF 34 BF 07     VEC     scale=3(/64) x=-3BF y=-FF  i=0   (-14.98 ,  -3.98 )
914C: 7F 27 7F F7     VEC     scale=2(/128)x=-37F y=-37F i=15  ( -6.99 ,  -6.99 )
9150: 3F 30 3F F2     VEC     scale=3(/64) x=23F  y=3F   i=15  (  8.98 ,   0.98 )
9154: 00 D0           RTS                         
;
9156: 02 F1           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
9158: 1F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-1F  i=15  (-21.96 ,  -0.96 )
915C: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
9160: F2 F9           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
9162: BF 35 3F F6     VEC     scale=3(/64) x=-23F y=-1BF i=15  ( -8.98 ,  -6.98 )
9166: DF 42 FF F0     VEC     scale=4(/32) x=FF   y=2DF  i=15  (  7.96 ,  22.96 )
916A: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
916C: 7F 26 7F F5     VEC     scale=2(/128)x=-17F y=-27F i=15  ( -2.99 ,  -4.99 )
9170: BF 40 DF F6     VEC     scale=4(/32) x=-2DF y=BF   i=15  (-22.96 ,   5.96 )
9174: BF 30 BF F2     VEC     scale=3(/64) x=2BF  y=BF   i=15  ( 10.98 ,   2.98 )
9178: F6 FD           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
917A: DF 46 1F F0     VEC     scale=4(/32) x=1F   y=-2DF i=15  (  0.96 , -22.96 )
917E: 1F 42 7F F1     VEC     scale=4(/32) x=17F  y=21F  i=15  ( 11.96 ,  16.96 )
9182: 00 D0           RTS                         
;
9184: 7F 35 BF 07     VEC     scale=3(/64) x=-3BF y=-17F i=0   (-14.98 ,  -5.98 )
9188: 7F 27 FF F6     VEC     scale=2(/128)x=-2FF y=-37F i=15  ( -5.99 ,  -6.99 )
918C: 7F 30 7F F2     VEC     scale=3(/64) x=27F  y=7F   i=15  (  9.98 ,   1.98 )
9190: 00 D0           RTS                         
;
9192: FF 12 FF 03     VEC     scale=1(/256)x=3FF  y=2FF  i=0   (  3.99 ,   2.99 )
9196: 5F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-5F  i=15  (-21.96 ,  -2.96 )
919A: 7F 45 7F F2     VEC     scale=4(/32) x=27F  y=-17F i=15  ( 19.96 , -11.96 )
919E: 7F 22 FF F3     VEC     scale=2(/128)x=3FF  y=27F  i=15  (  7.99 ,   4.99 )
91A2: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
91A4: FF 42 9F F0     VEC     scale=4(/32) x=9F   y=2FF  i=15  (  4.96 ,  23.96 )
91A8: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
91AA: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
91AE: 7F 40 FF F6     VEC     scale=4(/32) x=-2FF y=7F   i=15  (-23.96 ,   3.96 )
91B2: FF 30 BF F2     VEC     scale=3(/64) x=2BF  y=FF   i=15  ( 10.98 ,   3.98 )
91B6: 7F 26 FF F7     VEC     scale=2(/128)x=-3FF y=-27F i=15  ( -7.99 ,  -4.99 )
91BA: DF 46 5F F0     VEC     scale=4(/32) x=5F   y=-2DF i=15  (  2.96 , -22.96 )
91BE: 5F 42 5F F1     VEC     scale=4(/32) x=15F  y=25F  i=15  ( 10.96 ,  18.96 )
91C2: 00 D0           RTS                         
;
91C4: BF 35 7F 07     VEC     scale=3(/64) x=-37F y=-1BF i=0   (-13.98 ,  -6.98 )
91C8: FF 27 7F F6     VEC     scale=2(/128)x=-27F y=-3FF i=15  ( -4.99 ,  -7.99 )
91CC: BF 30 3F F2     VEC     scale=3(/64) x=23F  y=BF   i=15  (  8.98 ,   2.98 )
91D0: 00 D0           RTS                         
;
91D2: FF 12 FF 03     VEC     scale=1(/256)x=3FF  y=2FF  i=0   (  3.99 ,   2.99 )
91D6: 7F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-7F  i=15  (-21.96 ,  -3.96 )
91DA: 3F 45 BF F2     VEC     scale=4(/32) x=2BF  y=-13F i=15  ( 21.96 ,  -9.96 )
91DE: 7F 22 7F F3     VEC     scale=2(/128)x=37F  y=27F  i=15  (  6.99 ,   4.99 )
91E2: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
91E4: DF 42 7F F0     VEC     scale=4(/32) x=7F   y=2DF  i=15  (  3.96 ,  22.96 )
91E8: 7F 20 7F F2     VEC     scale=2(/128)x=27F  y=7F   i=15  (  4.99 ,   0.99 )
91EC: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
91F0: 1F 40 DF F6     VEC     scale=4(/32) x=-2DF y=1F   i=15  (-22.96 ,   0.96 )
91F4: 7F 31 3F F2     VEC     scale=3(/64) x=23F  y=17F  i=15  (  8.98 ,   5.98 )
91F8: F7 F7           SVEC    scale=0(/128)x=-200 y=-200 i=15  ( -4.00 ,  -4.00 )
91FA: DF 46 9F F0     VEC     scale=4(/32) x=9F   y=-2DF i=15  (  4.96 , -22.96 )
91FE: 7F 42 1F F1     VEC     scale=4(/32) x=11F  y=27F  i=15  (  8.96 ,  19.96 )
9202: 00 D0           RTS                         
;
9204: 3F 36 3F 07     VEC     scale=3(/64) x=-33F y=-23F i=0   (-12.98 ,  -8.98 )
9208: FF 27 FF F5     VEC     scale=2(/128)x=-1FF y=-3FF i=15  ( -3.99 ,  -7.99 )
920C: FF 21 FF F3     VEC     scale=2(/128)x=3FF  y=1FF  i=15  (  7.99 ,   3.99 )
9210: 00 D0           RTS                         
;
9212: 02 F2           SVEC    scale=0(/128)x=200  y=200  i=0   (  4.00 ,   4.00 )
9214: DF 44 9F F6     VEC     scale=4(/32) x=-29F y=-DF  i=15  (-20.96 ,  -6.96 )
9218: FF 44 BF F2     VEC     scale=4(/32) x=2BF  y=-FF  i=15  ( 21.96 ,  -7.96 )
921C: F3 F3           SVEC    scale=0(/128)x=200  y=200  i=15  (  4.00 ,   4.00 )
921E: 3F 36 7F F5     VEC     scale=3(/64) x=-17F y=-23F i=15  ( -5.98 ,  -8.98 )
9222: FF 42 1F F0     VEC     scale=4(/32) x=1F   y=2FF  i=15  (  0.96 ,  23.96 )
9226: 7F 20 7F F2     VEC     scale=2(/128)x=27F  y=7F   i=15  (  4.99 ,   0.99 )
922A: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
922E: 1F 44 FF F6     VEC     scale=4(/32) x=-2FF y=-1F  i=15  (-23.96 ,  -0.96 )
9232: 7F 31 3F F2     VEC     scale=3(/64) x=23F  y=17F  i=15  (  8.98 ,   5.98 )
9236: F7 F7           SVEC    scale=0(/128)x=-200 y=-200 i=15  ( -4.00 ,  -4.00 )
9238: BF 46 FF F0     VEC     scale=4(/32) x=FF   y=-2BF i=15  (  7.96 , -21.96 )
923C: 9F 42 DF F0     VEC     scale=4(/32) x=DF   y=29F  i=15  (  6.96 ,  20.96 )
9240: 00 D0           RTS                         
;
9242: 7F 36 FF 06     VEC     scale=3(/64) x=-2FF y=-27F i=0   (-11.98 ,  -9.98 )
9246: 3F 36 BF F4     VEC     scale=3(/64) x=-BF  y=-23F i=15  ( -2.98 ,  -8.98 )
924A: 7F 22 FF F3     VEC     scale=2(/128)x=3FF  y=27F  i=15  (  7.99 ,   4.99 )
924E: 00 D0           RTS                         
;
9250: FF 13 FF 02     VEC     scale=1(/256)x=2FF  y=3FF  i=0   (  2.99 ,   3.99 )
9254: 1F 45 7F F6     VEC     scale=4(/32) x=-27F y=-11F i=15  (-19.96 ,  -8.96 )
9258: 9F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-9F  i=15  ( 22.96 ,  -4.96 )
925C: F3 F3           SVEC    scale=0(/128)x=200  y=200  i=15  (  4.00 ,   4.00 )
925E: 3F 36 7F F5     VEC     scale=3(/64) x=-17F y=-23F i=15  ( -5.98 ,  -8.98 )
9262: DF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2DF  i=15  ( -0.96 ,  22.96 )
9266: FF 20 7F F2     VEC     scale=2(/128)x=27F  y=FF   i=15  (  4.99 ,   1.99 )
926A: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
926E: 7F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-7F  i=15  (-22.96 ,  -3.96 )
9272: F2 FA           SVEC    scale=1(/64) x=200  y=200  i=15  (  8.00 ,   8.00 )
9274: 7F 27 7F F6     VEC     scale=2(/128)x=-27F y=-37F i=15  ( -4.99 ,  -6.99 )
9278: BF 46 3F F1     VEC     scale=4(/32) x=13F  y=-2BF i=15  (  9.96 , -21.96 )
927C: BF 42 7F F0     VEC     scale=4(/32) x=7F   y=2BF  i=15  (  3.96 ,  21.96 )
9280: 00 D0           RTS                         
;
9282: BF 36 BF 06     VEC     scale=3(/64) x=-2BF y=-2BF i=0   (-10.98 , -10.98 )
9286: 7F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-27F i=15  ( -1.98 ,  -9.98 )
928A: FF 22 7F F3     VEC     scale=2(/128)x=37F  y=2FF  i=15  (  6.99 ,   5.99 )
928E: 00 D0           RTS                         
;
9290: FF 13 FF 02     VEC     scale=1(/256)x=2FF  y=3FF  i=0   (  2.99 ,   3.99 )
9294: 5F 45 5F F6     VEC     scale=4(/32) x=-25F y=-15F i=15  (-18.96 , -10.96 )
9298: 5F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-5F  i=15  ( 22.96 ,  -2.96 )
929C: FF 23 7F F2     VEC     scale=2(/128)x=27F  y=3FF  i=15  (  4.99 ,   7.99 )
92A0: BF 36 FF F4     VEC     scale=3(/64) x=-FF  y=-2BF i=15  ( -3.98 , -10.98 )
92A4: FF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2FF  i=15  ( -3.96 ,  23.96 )
92A8: FF 20 7F F2     VEC     scale=2(/128)x=27F  y=FF   i=15  (  4.99 ,   1.99 )
92AC: F0 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
92AE: 9F 44 FF F6     VEC     scale=4(/32) x=-2FF y=-9F  i=15  (-23.96 ,  -4.96 )
92B2: F2 FA           SVEC    scale=1(/64) x=200  y=200  i=15  (  8.00 ,   8.00 )
92B4: FF 27 7F F6     VEC     scale=2(/128)x=-27F y=-3FF i=15  ( -4.99 ,  -7.99 )
92B8: 7F 46 7F F1     VEC     scale=4(/32) x=17F  y=-27F i=15  ( 11.96 , -19.96 )
92BC: BF 42 5F F0     VEC     scale=4(/32) x=5F   y=2BF  i=15  (  2.96 ,  21.96 )
92C0: 00 D0           RTS                         
;
92C2: 3F 37 7F 06     VEC     scale=3(/64) x=-27F y=-33F i=0   ( -9.98 , -12.98 )
92C6: 3F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-23F i=15  ( -0.98 ,  -8.98 )
92CA: 7F 23 7F F3     VEC     scale=2(/128)x=37F  y=37F  i=15  (  6.99 ,   6.99 )
92CE: 00 D0           RTS                         
;
92D0: 01 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
92D2: 7F 45 1F F6     VEC     scale=4(/32) x=-21F y=-17F i=15  (-16.96 , -11.96 )
92D6: 1F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-1F  i=15  ( 22.96 ,  -0.96 )
92DA: F1 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
92DC: BF 36 BF F4     VEC     scale=3(/64) x=-BF  y=-2BF i=15  ( -2.98 , -10.98 )
92E0: DF 42 BF F4     VEC     scale=4(/32) x=-BF  y=2DF  i=15  ( -5.96 ,  22.96 )
92E4: 7F 21 7F F2     VEC     scale=2(/128)x=27F  y=17F  i=15  (  4.99 ,   2.99 )
92E8: F0 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
92EA: FF 44 DF F6     VEC     scale=4(/32) x=-2DF y=-FF  i=15  (-22.96 ,  -7.96 )
92EE: 3F 32 BF F1     VEC     scale=3(/64) x=1BF  y=23F  i=15  (  6.98 ,   8.98 )
92F2: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
92F4: 5F 46 9F F1     VEC     scale=4(/32) x=19F  y=-25F i=15  ( 12.96 , -18.96 )
92F8: BF 42 1F F0     VEC     scale=4(/32) x=1F   y=2BF  i=15  (  0.96 ,  21.96 )
92FC: 00 D0           RTS                         
;
92FE: 3F 37 FF 05     VEC     scale=3(/64) x=-1FF y=-33F i=0   ( -7.98 , -12.98 )
9302: 7F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-27F i=15  ( -0.98 ,  -9.98 )
9306: 7F 23 FF F2     VEC     scale=2(/128)x=2FF  y=37F  i=15  (  5.99 ,   6.99 )
930A: 00 D0           RTS                         
;
930C: 7F 22 FF 00     VEC     scale=2(/128)x=FF   y=27F  i=0   (  1.99 ,   4.99 )
9310: BF 37 FF F7     VEC     scale=3(/64) x=-3FF y=-3BF i=15  (-15.98 , -14.98 )
9314: 3F 40 DF F2     VEC     scale=4(/32) x=2DF  y=3F   i=15  ( 22.96 ,   1.96 )
9318: F1 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
931A: BF 36 BF F4     VEC     scale=3(/64) x=-BF  y=-2BF i=15  ( -2.98 , -10.98 )
931E: BF 42 1F F5     VEC     scale=4(/32) x=-11F y=2BF  i=15  ( -8.96 ,  21.96 )
9322: FF 21 7F F2     VEC     scale=2(/128)x=27F  y=1FF  i=15  (  4.99 ,   3.99 )
9326: FF 26 7F F0     VEC     scale=2(/128)x=7F   y=-2FF i=15  (  0.99 ,  -5.99 )
932A: 1F 45 BF F6     VEC     scale=4(/32) x=-2BF y=-11F i=15  (-21.96 ,  -8.96 )
932E: FF 23 7F F3     VEC     scale=2(/128)x=37F  y=3FF  i=15  (  6.99 ,   7.99 )
9332: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9334: 3F 46 DF F1     VEC     scale=4(/32) x=1DF  y=-23F i=15  ( 14.96 , -17.96 )
9338: DF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2DF  i=15  ( -0.96 ,  22.96 )
933C: 00 D0           RTS                         
;
933E: 7F 37 BF 05     VEC     scale=3(/64) x=-1BF y=-37F i=0   ( -6.98 , -13.98 )
9342: 7F 36 00 F0     VEC     scale=3(/64) x=0    y=-27F i=15  (  0.00 ,  -9.98 )
9346: FF 23 FF F2     VEC     scale=2(/128)x=2FF  y=3FF  i=15  (  5.99 ,   7.99 )
934A: 00 D0           RTS                         
;
934C: 7F 22 7F 00     VEC     scale=2(/128)x=7F   y=27F  i=0   (  0.99 ,   4.99 )
9350: FF 37 7F F7     VEC     scale=3(/64) x=-37F y=-3FF i=15  (-13.98 , -15.98 )
9354: 7F 40 DF F2     VEC     scale=4(/32) x=2DF  y=7F   i=15  ( 22.96 ,   3.96 )
9358: 7F 23 7F F1     VEC     scale=2(/128)x=17F  y=37F  i=15  (  2.99 ,   6.99 )
935C: 7F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-27F i=15  ( -1.98 ,  -9.98 )
9360: 9F 42 5F F5     VEC     scale=4(/32) x=-15F y=29F  i=15  (-10.96 ,  20.96 )
9364: FF 21 7F F2     VEC     scale=2(/128)x=27F  y=1FF  i=15  (  4.99 ,   3.99 )
9368: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
936C: 7F 45 7F F6     VEC     scale=4(/32) x=-27F y=-17F i=15  (-19.96 , -11.96 )
9370: 3F 32 3F F1     VEC     scale=3(/64) x=13F  y=23F  i=15  (  4.98 ,   8.98 )
9374: 7F 27 7F F5     VEC     scale=2(/128)x=-17F y=-37F i=15  ( -2.99 ,  -6.99 )
9378: 1F 46 1F F2     VEC     scale=4(/32) x=21F  y=-21F i=15  ( 16.96 , -16.96 )
937C: BF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2BF  i=15  ( -3.96 ,  21.96 )
9380: 00 D0           RTS                         
;
9382: BF 37 3F 05     VEC     scale=3(/64) x=-13F y=-3BF i=0   ( -4.98 , -14.98 )
9386: 3F 36 3F F0     VEC     scale=3(/64) x=3F   y=-23F i=15  (  0.98 ,  -8.98 )
938A: FF 23 FF F1     VEC     scale=2(/128)x=1FF  y=3FF  i=15  (  3.99 ,   7.99 )
;
938E: 00 D0           RTS                         
9390: 7F 22 7F 00     VEC     scale=2(/128)x=7F   y=27F  i=0   (  0.99 ,   4.99 )
9394: 3F 46 9F F5     VEC     scale=4(/32) x=-19F y=-23F i=15  (-12.96 , -17.96 )
9398: DF 40 DF F2     VEC     scale=4(/32) x=2DF  y=DF   i=15  ( 22.96 ,   6.96 )
939C: FF 23 FF F0     VEC     scale=2(/128)x=FF   y=3FF  i=15  (  1.99 ,   7.99 )
93A0: BF 36 3F F4     VEC     scale=3(/64) x=-3F  y=-2BF i=15  ( -0.98 , -10.98 )
93A4: 7F 42 7F F5     VEC     scale=4(/32) x=-17F y=27F  i=15  (-11.96 ,  19.96 )
93A8: 7F 22 7F F1     VEC     scale=2(/128)x=17F  y=27F  i=15  (  2.99 ,   4.99 )
93AC: F1 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
93AE: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
93B2: 3F 32 FF F0     VEC     scale=3(/64) x=FF   y=23F  i=15  (  3.98 ,   8.98 )
93B6: FF 27 FF F4     VEC     scale=2(/128)x=-FF  y=-3FF i=15  ( -1.99 ,  -7.99 )
93BA: DF 45 5F F2     VEC     scale=4(/32) x=25F  y=-1DF i=15  ( 18.96 , -14.96 )
93BE: BF 42 BF F4     VEC     scale=4(/32) x=-BF  y=2BF  i=15  ( -5.96 ,  21.96 )
93C2: 00 D0           RTS                         
;
93C4: FF 37 FF 04     VEC     scale=3(/64) x=-FF  y=-3FF i=0   ( -3.98 , -15.98 )
93C8: 3F 36 7F F0     VEC     scale=3(/64) x=7F   y=-23F i=15  (  1.98 ,  -8.98 )
93CC: 3F 32 BF F0     VEC     scale=3(/64) x=BF   y=23F  i=15  (  2.98 ,   8.98 )
93D0: 00 D0           RTS                         
;
93D2: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
93D6: 5F 46 5F F5     VEC     scale=4(/32) x=-15F y=-25F i=15  (-10.96 , -18.96 )
93DA: 1F 41 BF F2     VEC     scale=4(/32) x=2BF  y=11F  i=15  ( 21.96 ,   8.96 )
93DE: FF 23 7F F0     VEC     scale=2(/128)x=7F   y=3FF  i=15  (  0.99 ,   7.99 )
93E2: 7F 36 3F F0     VEC     scale=3(/64) x=3F   y=-27F i=15  (  0.98 ,  -9.98 )
93E6: 3F 42 BF F5     VEC     scale=4(/32) x=-1BF y=23F  i=15  (-13.96 ,  17.96 )
93EA: 7F 22 7F F1     VEC     scale=2(/128)x=17F  y=27F  i=15  (  2.99 ,   4.99 )
93EE: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
93F2: FF 45 3F F6     VEC     scale=4(/32) x=-23F y=-1FF i=15  (-17.96 , -15.96 )
93F6: 7F 32 BF F0     VEC     scale=3(/64) x=BF   y=27F  i=15  (  2.98 ,   9.98 )
93FA: F0 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
93FC: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
9400: 9F 42 FF F4     VEC     scale=4(/32) x=-FF  y=29F  i=15  ( -7.96 ,  20.96 )
9404: 00 D0           RTS                         

; ?? not used
9406: 3C FF           SVEC    scale=3(/16) x=0    y=-200 i=3   (  0.00 , -32.00 )
```

# Enemy Triangle 

Circle enemy with triangle (just one picture)

```html
<canvas width="100" height="100"
  data-command="baseScale=1,x=50,y=50,9408">
</canvas>
```

```code
EnemyTri:
9408: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
940A: BF 36 BF F1     VEC     scale=3(/64) x=1BF  y=-2BF i=15  (  6.98 , -10.98 )
940E: 00 30 3F F7     VEC     scale=3(/64) x=-33F y=0    i=15  (-12.98 ,   0.00 )
9412: BF 32 7F F1     VEC     scale=3(/64) x=17F  y=2BF  i=15  (  5.98 ,  10.98 )
9416: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
941A: 7F 32 7F A6     VEC     scale=3(/64) x=-27F y=27F  i=10  ( -9.98 ,   9.98 )
941E: 00 30 BF A6     VEC     scale=3(/64) x=-2BF y=0    i=10  (-10.98 ,   0.00 )
9422: 7F 36 7F A6     VEC     scale=3(/64) x=-27F y=-27F i=10  ( -9.98 ,  -9.98 )
9426: BF 36 00 A0     VEC     scale=3(/64) x=0    y=-2BF i=10  (  0.00 , -10.98 )
942A: 7F 36 7F A2     VEC     scale=3(/64) x=27F  y=-27F i=10  (  9.98 ,  -9.98 )
942E: 00 30 BF A2     VEC     scale=3(/64) x=2BF  y=0    i=10  ( 10.98 ,   0.00 )
9432: 7F 32 7F A2     VEC     scale=3(/64) x=27F  y=27F  i=10  (  9.98 ,   9.98 )
9436: 9F 42 3F C5     VEC     scale=4(/32) x=-13F y=29F  i=12  ( -9.96 ,  20.96 )
943A: 3F 45 9F C6     VEC     scale=4(/32) x=-29F y=-13F i=12  (-20.96 ,  -9.96 )
943E: 9F 46 3F C1     VEC     scale=4(/32) x=13F  y=-29F i=12  (  9.96 , -20.96 )
9442: 3F 41 9F C2     VEC     scale=4(/32) x=29F  y=13F  i=12  ( 20.96 ,   9.96 )
9446: BF 32 00 A0     VEC     scale=3(/64) x=0    y=2BF  i=10  (  0.00 ,  10.98 )
944A: 3F 41 9F C6     VEC     scale=4(/32) x=-29F y=13F  i=12  (-20.96 ,   9.96 )
944E: 9F 46 3F C5     VEC     scale=4(/32) x=-13F y=-29F i=12  ( -9.96 , -20.96 )
9452: 3F 45 9F C2     VEC     scale=4(/32) x=29F  y=-13F i=12  ( 20.96 ,  -9.96 )
9456: 9F 42 3F C1     VEC     scale=4(/32) x=13F  y=29F  i=12  (  9.96 ,  20.96 )
945A: 00 D0           RTS                         
```

# Enemy (no triangle) 

Circle enemy (no triangle). There are three pictures for animation.

```html
<canvas width="250" height="100"
  data-command="baseScale=1,x=50,y=50,945C,x=125,y=50,94A2,x=200,y=50,94E8">
</canvas>
```

```code
EnemyNoTri:
945C: 7F 31 FF 03     VEC     scale=3(/64) x=3FF  y=17F  i=0   ( 15.98 ,   5.98 )
9460: 7F 32 7F 66     VEC     scale=3(/64) x=-27F y=27F  i=6   ( -9.98 ,   9.98 )
9464: 00 30 BF 66     VEC     scale=3(/64) x=-2BF y=0    i=6   (-10.98 ,   0.00 )
9468: 7F 36 7F 66     VEC     scale=3(/64) x=-27F y=-27F i=6   ( -9.98 ,  -9.98 )
946C: BF 36 00 60     VEC     scale=3(/64) x=0    y=-2BF i=6   (  0.00 , -10.98 )
9470: 7F 36 7F 62     VEC     scale=3(/64) x=27F  y=-27F i=6   (  9.98 ,  -9.98 )
9474: 00 30 BF 62     VEC     scale=3(/64) x=2BF  y=0    i=6   ( 10.98 ,   0.00 )
9478: 7F 32 7F 62     VEC     scale=3(/64) x=27F  y=27F  i=6   (  9.98 ,   9.98 )
947C: 9F 42 3F 85     VEC     scale=4(/32) x=-13F y=29F  i=8   ( -9.96 ,  20.96 )
9480: 3F 45 9F 86     VEC     scale=4(/32) x=-29F y=-13F i=8   (-20.96 ,  -9.96 )
9484: 9F 46 3F 81     VEC     scale=4(/32) x=13F  y=-29F i=8   (  9.96 , -20.96 )
9488: 3F 41 9F 82     VEC     scale=4(/32) x=29F  y=13F  i=8   ( 20.96 ,   9.96 )
948C: BF 32 00 60     VEC     scale=3(/64) x=0    y=2BF  i=6   (  0.00 ,  10.98 )
9490: 3F 41 9F 86     VEC     scale=4(/32) x=-29F y=13F  i=8   (-20.96 ,   9.96 )
9494: 9F 46 3F 85     VEC     scale=4(/32) x=-13F y=-29F i=8   ( -9.96 , -20.96 )
9498: 3F 45 9F 82     VEC     scale=4(/32) x=29F  y=-13F i=8   ( 20.96 ,  -9.96 )
949C: 9F 42 3F 81     VEC     scale=4(/32) x=13F  y=29F  i=8   (  9.96 ,  20.96 )
94A0: 00 D0           RTS                         
;
94A2: 7F 32 7F 03     VEC     scale=3(/64) x=37F  y=27F  i=0   ( 13.98 ,   9.98 )
94A6: BF 31 3F 67     VEC     scale=3(/64) x=-33F y=1BF  i=6   (-12.98 ,   6.98 )
94AA: BF 34 7F 66     VEC     scale=3(/64) x=-27F y=-BF  i=6   ( -9.98 ,  -2.98 )
94AE: 3F 37 BF 65     VEC     scale=3(/64) x=-1BF y=-33F i=6   ( -6.98 , -12.98 )
94B2: 7F 36 BF 60     VEC     scale=3(/64) x=BF   y=-27F i=6   (  2.98 ,  -9.98 )
94B6: BF 35 3F 63     VEC     scale=3(/64) x=33F  y=-1BF i=6   ( 12.98 ,  -6.98 )
94BA: BF 30 7F 62     VEC     scale=3(/64) x=27F  y=BF   i=6   (  9.98 ,   2.98 )
94BE: 3F 33 BF 61     VEC     scale=3(/64) x=1BF  y=33F  i=6   (  6.98 ,  12.98 )
94C2: 1F 42 FF 85     VEC     scale=4(/32) x=-1FF y=21F  i=8   (-15.96 ,  16.96 )
94C6: FF 45 1F 86     VEC     scale=4(/32) x=-21F y=-1FF i=8   (-16.96 , -15.96 )
94CA: 1F 46 FF 81     VEC     scale=4(/32) x=1FF  y=-21F i=8   ( 15.96 , -16.96 )
94CE: FF 41 1F 82     VEC     scale=4(/32) x=21F  y=1FF  i=8   ( 16.96 ,  15.96 )
94D2: 7F 32 BF 64     VEC     scale=3(/64) x=-BF  y=27F  i=6   ( -2.98 ,   9.98 )
94D6: 7F 40 DF 86     VEC     scale=4(/32) x=-2DF y=7F   i=8   (-22.96 ,   3.96 )
94DA: DF 46 7F 84     VEC     scale=4(/32) x=-7F  y=-2DF i=8   ( -3.96 , -22.96 )
94DE: 7F 44 DF 82     VEC     scale=4(/32) x=2DF  y=-7F  i=8   ( 22.96 ,  -3.96 )
94E2: DF 42 7F 80     VEC     scale=4(/32) x=7F   y=2DF  i=8   (  3.96 ,  22.96 )
94E6: 00 D0           RTS                         
;
94E8: 7F 33 BF 02     VEC     scale=3(/64) x=2BF  y=37F  i=0   ( 10.98 ,  13.98 )
94EC: BF 30 3F 67     VEC     scale=3(/64) x=-33F y=BF   i=6   (-12.98 ,   2.98 )
94F0: 7F 35 BF 66     VEC     scale=3(/64) x=-2BF y=-17F i=6   (-10.98 ,  -5.98 )
94F4: 3F 37 BF 64     VEC     scale=3(/64) x=-BF  y=-33F i=6   ( -2.98 , -12.98 )
94F8: BF 36 7F 61     VEC     scale=3(/64) x=17F  y=-2BF i=6   (  5.98 , -10.98 )
94FC: BF 34 3F 63     VEC     scale=3(/64) x=33F  y=-BF  i=6   ( 12.98 ,  -2.98 )
9500: 7F 31 BF 62     VEC     scale=3(/64) x=2BF  y=17F  i=6   ( 10.98 ,   5.98 )
9504: 3F 33 BF 60     VEC     scale=3(/64) x=BF   y=33F  i=6   (  2.98 ,  12.98 )
9508: BF 41 5F 86     VEC     scale=4(/32) x=-25F y=1BF  i=8   (-18.96 ,  13.96 )
950C: 5F 46 BF 85     VEC     scale=4(/32) x=-1BF y=-25F i=8   (-13.96 , -18.96 )
9510: BF 45 5F 82     VEC     scale=4(/32) x=25F  y=-1BF i=8   ( 18.96 , -13.96 )
9514: 5F 42 BF 81     VEC     scale=4(/32) x=1BF  y=25F  i=8   ( 13.96 ,  18.96 )
9518: BF 32 7F 65     VEC     scale=3(/64) x=-17F y=2BF  i=6   ( -5.98 ,  10.98 )
951C: 5F 44 FF 86     VEC     scale=4(/32) x=-2FF y=-5F  i=8   (-23.96 ,  -2.96 )
9520: FF 46 5F 80     VEC     scale=4(/32) x=5F   y=-2FF i=8   (  2.96 , -23.96 )
9524: 5F 40 FF 82     VEC     scale=4(/32) x=2FF  y=5F   i=8   ( 23.96 ,   2.96 )
9528: FF 42 5F 84     VEC     scale=4(/32) x=-5F  y=2FF  i=8   ( -2.96 ,  23.96 )
952C: 00 D0           RTS                         
```

# Enemy Chaser 

Triangle, chasing ememy in different positions

```html
<canvas width="350" height="100"
  data-command="baseScale=1,x=50,y=50,952E,x=125,y=50,9554,x=200,y=50,957C,x=275,y=50,95A4">
</canvas>
```

```code
EnemyChase:
952E: FF 12 FF D2     VEC     scale=1(/256)x=2FF  y=2FF  i=13  (  2.99 ,   2.99 )
9532: BF 34 3F D3     VEC     scale=3(/64) x=33F  y=-BF  i=13  ( 12.98 ,  -2.98 )
9536: 00 40 DF D7     VEC     scale=4(/32) x=-3DF y=0    i=13  (-30.96 ,   0.00 )
953A: 7F 34 3F D3     VEC     scale=3(/64) x=33F  y=-7F  i=13  ( 12.98 ,  -1.98 )
953E: D1 F1           SVEC    scale=0(/128)x=0    y=0    i=13  (  0.00 ,   0.00 )
9540: D8 F2           SVEC    scale=2(/32) x=0    y=200  i=13  (  0.00 ,  16.00 )
9542: 3F 37 7F D4     VEC     scale=3(/64) x=-7F  y=-33F i=13  ( -1.98 , -12.98 )
9546: 7F 26 7F D2     VEC     scale=2(/128)x=27F  y=-27F i=13  (  4.99 ,  -4.99 )
954A: 3F 37 BF D4     VEC     scale=3(/64) x=-BF  y=-33F i=13  ( -2.98 , -12.98 )
954E: BF 33 00 D0     VEC     scale=3(/64) x=0    y=3BF  i=13  (  0.00 ,  14.98 )
9552: A7 EB           JMP     $974E               ; {code.Triangles}
;
9554: D1 F2           SVEC    scale=0(/128)x=0    y=200  i=13  (  0.00 ,   4.00 )
9556: 7F 30 3F D3     VEC     scale=3(/64) x=33F  y=7F   i=13  ( 12.98 ,   1.98 )
955A: 5F 45 9F D7     VEC     scale=4(/32) x=-39F y=-15F i=13  (-28.96 , -10.96 )
955E: 7F 30 3F D3     VEC     scale=3(/64) x=33F  y=7F   i=13  ( 12.98 ,   1.98 )
9562: FF 12 FF D0     VEC     scale=1(/256)x=FF   y=2FF  i=13  (  0.99 ,   2.99 )
9566: BF 33 3F D5     VEC     scale=3(/64) x=-13F y=3BF  i=13  ( -4.98 ,  14.98 )
956A: 3F 37 7F D0     VEC     scale=3(/64) x=7F   y=-33F i=13  (  1.98 , -12.98 )
956E: 7F 25 7F D3     VEC     scale=2(/128)x=37F  y=-17F i=13  (  6.99 ,  -2.99 )
9572: 3F 37 7F D0     VEC     scale=3(/64) x=7F   y=-33F i=13  (  1.98 , -12.98 )
9576: 7F 33 7F D5     VEC     scale=3(/64) x=-17F y=37F  i=13  ( -5.98 ,  13.98 )
957A: A7 EB           JMP     $974E               ; {code.Triangles}
;
957C: D0 F2           SVEC    scale=0(/128)x=0    y=200  i=13  (  0.00 ,   4.00 )
957E: BF 31 BF D2     VEC     scale=3(/64) x=2BF  y=1BF  i=13  ( 10.98 ,   6.98 )
9582: 9F 46 9F D6     VEC     scale=4(/32) x=-29F y=-29F i=13  (-20.96 , -20.96 )
9586: BF 31 7F D2     VEC     scale=3(/64) x=27F  y=1BF  i=13  (  9.98 ,   6.98 )
958A: FF 12 00 D0     VEC     scale=1(/256)x=0    y=2FF  i=13  (  0.00 ,   2.99 )
958E: BF 32 7F D6     VEC     scale=3(/64) x=-27F y=2BF  i=13  ( -9.98 ,  10.98 )
9592: BF 36 BF D1     VEC     scale=3(/64) x=1BF  y=-2BF i=13  (  6.98 , -10.98 )
9596: 00 20 7F D3     VEC     scale=2(/128)x=37F  y=0    i=13  (  6.99 ,   0.00 )
959A: 7F 36 BF D1     VEC     scale=3(/64) x=1BF  y=-27F i=13  (  6.98 ,  -9.98 )
959E: 7F 32 BF D6     VEC     scale=3(/64) x=-2BF y=27F  i=13  (-10.98 ,   9.98 )
95A2: A7 EB           JMP     $974E               ; {code.Triangles}
;
95A4: FF 13 FF D4     VEC     scale=1(/256)x=-FF  y=3FF  i=13  ( -0.99 ,   3.99 )
95A8: BF 32 BF D1     VEC     scale=3(/64) x=1BF  y=2BF  i=13  (  6.98 ,  10.98 )
95AC: 9F 47 5F D5     VEC     scale=4(/32) x=-15F y=-39F i=13  (-10.96 , -28.96 )
95B0: BF 32 BF D1     VEC     scale=3(/64) x=1BF  y=2BF  i=13  (  6.98 ,  10.98 )
95B4: FF 12 FF D5     VEC     scale=1(/256)x=-1FF y=2FF  i=13  ( -1.99 ,   2.99 )
95B8: 7F 31 7F D7     VEC     scale=3(/64) x=-37F y=17F  i=13  (-13.98 ,   5.98 )
95BC: BF 35 BF D2     VEC     scale=3(/64) x=2BF  y=-1BF i=13  ( 10.98 ,  -6.98 )
95C0: 7F 21 7F D3     VEC     scale=2(/128)x=37F  y=17F  i=13  (  6.99 ,   2.99 )
95C4: BF 35 BF D2     VEC     scale=3(/64) x=2BF  y=-1BF i=13  ( 10.98 ,  -6.98 )
95C8: 3F 31 BF D7     VEC     scale=3(/64) x=-3BF y=13F  i=13  (-14.98 ,   4.98 )
95CC: A7 EB           JMP     $974E               ; {code.Triangles}
```

# Lasers 

```code
Lasers:
; Laser shots at different angles (just single vectors)
;
95CE: 00 30 BF F7     VEC     scale=3(/64) x=-3BF y=0    i=15  (-14.98 ,   0.00 )
95D2: 00 D0           RTS                         
95D4: 3F 34 7F F7     VEC     scale=3(/64) x=-37F y=-3F  i=15  (-13.98 ,  -0.98 )
95D8: 00 D0           RTS                         
95DA: 7F 34 7F F7     VEC     scale=3(/64) x=-37F y=-7F  i=15  (-13.98 ,  -1.98 )
95DE: 00 D0           RTS                         
95E0: FF 34 3F F7     VEC     scale=3(/64) x=-33F y=-FF  i=15  (-12.98 ,  -3.98 )
95E4: 00 D0           RTS                         
95E6: 3F 35 3F F7     VEC     scale=3(/64) x=-33F y=-13F i=15  (-12.98 ,  -4.98 )
95EA: 00 D0           RTS                         
95EC: BF 35 FF F6     VEC     scale=3(/64) x=-2FF y=-1BF i=15  (-11.98 ,  -6.98 )
95F0: 00 D0           RTS                         
95F2: FF 35 BF F6     VEC     scale=3(/64) x=-2BF y=-1FF i=15  (-10.98 ,  -7.98 )
95F6: 00 D0           RTS                         
95F8: FF 35 7F F6     VEC     scale=3(/64) x=-27F y=-1FF i=15  ( -9.98 ,  -7.98 )
95FC: 00 D0           RTS                         
95FE: 3F 36 3F F6     VEC     scale=3(/64) x=-23F y=-23F i=15  ( -8.98 ,  -8.98 )
9602: 00 D0           RTS                         
9604: 7F 36 FF F5     VEC     scale=3(/64) x=-1FF y=-27F i=15  ( -7.98 ,  -9.98 )
9608: 00 D0           RTS                         
960A: BF 36 BF F5     VEC     scale=3(/64) x=-1BF y=-2BF i=15  ( -6.98 , -10.98 )
960E: 00 D0           RTS                         
9610: FF 36 3F F5     VEC     scale=3(/64) x=-13F y=-2FF i=15  ( -4.98 , -11.98 )
9614: 00 D0           RTS                         
9616: 3F 37 FF F4     VEC     scale=3(/64) x=-FF  y=-33F i=15  ( -3.98 , -12.98 )
961A: 00 D0           RTS                         
961C: 7F 37 7F F4     VEC     scale=3(/64) x=-7F  y=-37F i=15  ( -1.98 , -13.98 )
9620: 00 D0           RTS                         
9622: 7F 37 3F F4     VEC     scale=3(/64) x=-3F  y=-37F i=15  ( -0.98 , -13.98 )
9626: 00 D0           RTS                         
9628: BF 37 00 F0     VEC     scale=3(/64) x=0    y=-3BF i=15  (  0.00 , -14.98 )
962C: 00 D0           RTS                         
962E: BF 37 3F F0     VEC     scale=3(/64) x=3F   y=-3BF i=15  (  0.98 , -14.98 )
9632: 00 D0           RTS                         
9634: 7F 37 7F F0     VEC     scale=3(/64) x=7F   y=-37F i=15  (  1.98 , -13.98 )
9638: 00 D0           RTS                         
963A: 7F 37 BF F0     VEC     scale=3(/64) x=BF   y=-37F i=15  (  2.98 , -13.98 )
963E: 00 D0           RTS                         
9640: 3F 37 3F F1     VEC     scale=3(/64) x=13F  y=-33F i=15  (  4.98 , -12.98 )
9644: 00 D0           RTS                         
9646: FF 36 7F F1     VEC     scale=3(/64) x=17F  y=-2FF i=15  (  5.98 , -11.98 )
964A: 00 D0           RTS                         
964C: BF 36 FF F1     VEC     scale=3(/64) x=1FF  y=-2BF i=15  (  7.98 , -10.98 )
9650: 00 D0           RTS                         
9652: 7F 36 3F F2     VEC     scale=3(/64) x=23F  y=-27F i=15  (  8.98 ,  -9.98 )
9656: 00 D0           RTS                         
9658: 3F 36 7F F2     VEC     scale=3(/64) x=27F  y=-23F i=15  (  9.98 ,  -8.98 )
965C: 00 D0           RTS                         
965E: FF 35 BF F2     VEC     scale=3(/64) x=2BF  y=-1FF i=15  ( 10.98 ,  -7.98 )
9662: 00 D0           RTS                         
9664: FF 35 FF F2     VEC     scale=3(/64) x=2FF  y=-1FF i=15  ( 11.98 ,  -7.98 )
9668: 00 D0           RTS                         
966A: BF 35 3F F3     VEC     scale=3(/64) x=33F  y=-1BF i=15  ( 12.98 ,  -6.98 )
966E: 00 D0           RTS                         
9670: 3F 35 7F F3     VEC     scale=3(/64) x=37F  y=-13F i=15  ( 13.98 ,  -4.98 )
9674: 00 D0           RTS                         
9676: FF 34 7F F3     VEC     scale=3(/64) x=37F  y=-FF  i=15  ( 13.98 ,  -3.98 )
967A: 00 D0           RTS                         
967C: 7F 34 BF F3     VEC     scale=3(/64) x=3BF  y=-7F  i=15  ( 14.98 ,  -1.98 )
9680: 00 D0           RTS                         
9682: 3F 34 BF F3     VEC     scale=3(/64) x=3BF  y=-3F  i=15  ( 14.98 ,  -0.98 )
9686: 00 D0           RTS                         
9688: 00 30 FF F3     VEC     scale=3(/64) x=3FF  y=0    i=15  ( 15.98 ,   0.00 )
968C: 00 D0           RTS                         
968E: 00 30 FF F3     VEC     scale=3(/64) x=3FF  y=0    i=15  ( 15.98 ,   0.00 )
9692: 00 D0           RTS                         
9694: 7F 30 BF F3     VEC     scale=3(/64) x=3BF  y=7F   i=15  ( 14.98 ,   1.98 )
9698: 00 D0           RTS                         
969A: BF 30 BF F3     VEC     scale=3(/64) x=3BF  y=BF   i=15  ( 14.98 ,   2.98 )
969E: 00 D0           RTS                         
96A0: 3F 31 7F F3     VEC     scale=3(/64) x=37F  y=13F  i=15  ( 13.98 ,   4.98 )
96A4: 00 D0           RTS                         
96A6: 7F 31 7F F3     VEC     scale=3(/64) x=37F  y=17F  i=15  ( 13.98 ,   5.98 )
96AA: 00 D0           RTS                         
96AC: FF 31 3F F3     VEC     scale=3(/64) x=33F  y=1FF  i=15  ( 12.98 ,   7.98 )
96B0: 00 D0           RTS                         
96B2: 3F 32 FF F2     VEC     scale=3(/64) x=2FF  y=23F  i=15  ( 11.98 ,   8.98 )
96B6: 00 D0           RTS                         
96B8: 3F 32 BF F2     VEC     scale=3(/64) x=2BF  y=23F  i=15  ( 10.98 ,   8.98 )
96BC: 00 D0           RTS                         
96BE: 7F 32 7F F2     VEC     scale=3(/64) x=27F  y=27F  i=15  (  9.98 ,   9.98 )
96C2: 00 D0           RTS                         
96C4: BF 32 3F F2     VEC     scale=3(/64) x=23F  y=2BF  i=15  (  8.98 ,  10.98 )
96C8: 00 D0           RTS                         
96CA: FF 32 FF F1     VEC     scale=3(/64) x=1FF  y=2FF  i=15  (  7.98 ,  11.98 )
96CE: 00 D0           RTS                         
96D0: 3F 33 7F F1     VEC     scale=3(/64) x=17F  y=33F  i=15  (  5.98 ,  12.98 )
96D4: 00 D0           RTS                         
96D6: 7F 33 3F F1     VEC     scale=3(/64) x=13F  y=37F  i=15  (  4.98 ,  13.98 )
96DA: 00 D0           RTS                         
96DC: BF 33 BF F0     VEC     scale=3(/64) x=BF   y=3BF  i=15  (  2.98 ,  14.98 )
96E0: 00 D0           RTS                         
96E2: BF 33 7F F0     VEC     scale=3(/64) x=7F   y=3BF  i=15  (  1.98 ,  14.98 )
96E6: 00 D0           RTS                         
96E8: FF 33 00 F0     VEC     scale=3(/64) x=0    y=3FF  i=15  (  0.00 ,  15.98 )
96EC: 00 D0           RTS                         
96EE: FF 33 00 F0     VEC     scale=3(/64) x=0    y=3FF  i=15  (  0.00 ,  15.98 )
96F2: 00 D0           RTS                         
96F4: BF 33 3F F4     VEC     scale=3(/64) x=-3F  y=3BF  i=15  ( -0.98 ,  14.98 )
96F8: 00 D0           RTS                         
96FA: BF 33 7F F4     VEC     scale=3(/64) x=-7F  y=3BF  i=15  ( -1.98 ,  14.98 )
96FE: 00 D0           RTS                         
9700: 7F 33 FF F4     VEC     scale=3(/64) x=-FF  y=37F  i=15  ( -3.98 ,  13.98 )
9704: 00 D0           RTS                         
9706: 3F 33 3F F5     VEC     scale=3(/64) x=-13F y=33F  i=15  ( -4.98 ,  12.98 )
970A: 00 D0           RTS                         
970C: FF 32 BF F5     VEC     scale=3(/64) x=-1BF y=2FF  i=15  ( -6.98 ,  11.98 )
9710: 00 D0           RTS                         
9712: BF 32 FF F5     VEC     scale=3(/64) x=-1FF y=2BF  i=15  ( -7.98 ,  10.98 )
9716: 00 D0           RTS                         
9718: 7F 32 3F F6     VEC     scale=3(/64) x=-23F y=27F  i=15  ( -8.98 ,   9.98 )
971C: 00 D0           RTS                         
971E: 3F 32 7F F6     VEC     scale=3(/64) x=-27F y=23F  i=15  ( -9.98 ,   8.98 )
9722: 00 D0           RTS                         
9724: 3F 32 BF F6     VEC     scale=3(/64) x=-2BF y=23F  i=15  (-10.98 ,   8.98 )
9728: 00 D0           RTS                         
972A: FF 31 FF F6     VEC     scale=3(/64) x=-2FF y=1FF  i=15  (-11.98 ,   7.98 )
972E: 00 D0           RTS                         
9730: 7F 31 3F F7     VEC     scale=3(/64) x=-33F y=17F  i=15  (-12.98 ,   5.98 )
9734: 00 D0           RTS                         
9736: 3F 31 3F F7     VEC     scale=3(/64) x=-33F y=13F  i=15  (-12.98 ,   4.98 )
973A: 00 D0           RTS                         
973C: BF 30 7F F7     VEC     scale=3(/64) x=-37F y=BF   i=15  (-13.98 ,   2.98 )
9740: 00 D0           RTS                         
9742: 7F 30 7F F7     VEC     scale=3(/64) x=-37F y=7F   i=15  (-13.98 ,   1.98 )
9746: 00 D0           RTS                         
9748: 00 30 BF F7     VEC     scale=3(/64) x=-3BF y=0    i=15  (-14.98 ,   0.00 )
974C: 00 D0           RTS                         
```

# Triangles 

Single and double

```html
<canvas width="200" height="100"
  data-command="baseScale=1,x=50,y=50,974E,x=125,y=50,975E">
</canvas>
```

```code
Triangles:
; Triangle (up)
974E: 7F 35 FF 02     VEC     scale=3(/64) x=2FF  y=-17F i=0   ( 11.98 ,  -5.98 )
9752: FF 33 FF F6     VEC     scale=3(/64) x=-2FF y=3FF  i=15  (-11.98 ,  15.98 )
9756: FF 37 FF F6     VEC     scale=3(/64) x=-2FF y=-3FF i=15  (-11.98 , -15.98 )
975A: FB F0           SVEC    scale=2(/32) x=200  y=0    i=15  ( 16.00 ,   0.00 )
975C: 00 D0           RTS                         

; Triangles (up and down)
975E: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9760: FF 33 FF F6     VEC     scale=3(/64) x=-2FF y=3FF  i=15  (-11.98 ,  15.98 )
9764: FF 37 FF F6     VEC     scale=3(/64) x=-2FF y=-3FF i=15  (-11.98 , -15.98 )
9768: FF 37 FF F2     VEC     scale=3(/64) x=2FF  y=-3FF i=15  ( 11.98 , -15.98 )
976C: FF 33 FF F2     VEC     scale=3(/64) x=2FF  y=3FF  i=15  ( 11.98 ,  15.98 )
9770: FF F0           SVEC    scale=2(/32) x=-200 y=0    i=15  (-16.00 ,   0.00 )
9772: 00 D0           RTS                         
```

# Explosion 

Multi-line explosion ... three pictures for animation

```html
<canvas width="400" height="200"
  data-command="baseScale=1,x=50,y=100,9774,x=150,y=100,97B0,x=300,y=100,9824">
</canvas>
```

```code
Explosion:
9774: BF 32 00 F0     VEC     scale=3(/64) x=0    y=2BF  i=15  (  0.00 ,  10.98 )
9778: BF 46 00 F0     VEC     scale=4(/32) x=0    y=-2BF i=15  (  0.00 , -21.96 )
977C: FF 21 7F 06     VEC     scale=2(/128)x=-27F y=1FF  i=0   ( -4.99 ,   3.99 )
9780: BF 33 3F F2     VEC     scale=3(/64) x=23F  y=3BF  i=15  (  8.98 ,  14.98 )
9784: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
9786: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
9788: FF 20 7F 06     VEC     scale=2(/128)x=-27F y=FF   i=0   ( -4.99 ,   1.99 )
978C: DF 40 5F F2     VEC     scale=4(/32) x=25F  y=DF   i=15  ( 18.96 ,   6.96 )
9790: 7F 26 FF 00     VEC     scale=2(/128)x=FF   y=-27F i=0   (  1.99 ,  -4.99 )
9794: 00 40 BF F6     VEC     scale=4(/32) x=-2BF y=0    i=15  (-21.96 ,   0.00 )
9798: FF 13 FF 04     VEC     scale=1(/256)x=-FF  y=3FF  i=0   ( -0.99 ,   3.99 )
979C: FF 44 9F F2     VEC     scale=4(/32) x=29F  y=-FF  i=15  ( 20.96 ,  -7.96 )
97A0: 00 F7           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
97A2: 7F 33 7F F7     VEC     scale=3(/64) x=-37F y=37F  i=15  (-13.98 ,  13.98 )
97A6: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
97AA: FF 37 BF F1     VEC     scale=3(/64) x=1BF  y=-3FF i=15  (  6.98 , -15.98 )
97AE: 00 D0           RTS                         
;
97B0: BF 32 00 00     VEC     scale=3(/64) x=0    y=2BF  i=0   (  0.00 ,  10.98 )
97B4: 7F 32 00 50     VEC     scale=3(/64) x=0    y=27F  i=5   (  0.00 ,   9.98 )
97B8: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
97BC: 55 FE           SVEC    scale=1(/64) x=0    y=-200 i=5   (  0.00 ,  -8.00 )
97BE: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
97C0: 53 FB           SVEC    scale=1(/64) x=200  y=200  i=5   (  8.00 ,   8.00 )
97C2: BF 36 7F 05     VEC     scale=3(/64) x=-17F y=-2BF i=0   ( -5.98 , -10.98 )
97C6: 7F 31 FF 52     VEC     scale=3(/64) x=2FF  y=17F  i=5   ( 11.98 ,   5.98 )
97CA: BF 36 7F 04     VEC     scale=3(/64) x=-7F  y=-2BF i=0   ( -1.98 , -10.98 )
97CE: 56 F8           SVEC    scale=1(/64) x=-200 y=0    i=5   ( -8.00 ,   0.00 )
97D0: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
97D2: 7F 25 FF 53     VEC     scale=2(/128)x=3FF  y=-17F i=5   (  7.99 ,  -2.99 )
97D6: 3F 37 7F 00     VEC     scale=3(/64) x=7F   y=-33F i=0   (  1.98 , -12.98 )
97DA: 7F 32 7F 56     VEC     scale=3(/64) x=-27F y=27F  i=5   ( -9.98 ,   9.98 )
97DE: 7F 21 7F 07     VEC     scale=2(/128)x=-37F y=17F  i=0   ( -6.99 ,   2.99 )
97E2: 3F 36 FF 50     VEC     scale=3(/64) x=FF   y=-23F i=5   (  3.98 ,  -8.98 )
97E6: FF 25 7F 07     VEC     scale=2(/128)x=-37F y=-1FF i=0   ( -6.99 ,  -3.99 )
97EA: 50 FA           SVEC    scale=1(/64) x=0    y=200  i=5   (  0.00 ,   8.00 )
97EC: 7F 22 7F 06     VEC     scale=2(/128)x=-27F y=27F  i=0   ( -4.99 ,   4.99 )
97F0: 7F 27 7F 56     VEC     scale=2(/128)x=-27F y=-37F i=5   ( -4.99 ,  -6.99 )
97F4: 7F 21 FF 07     VEC     scale=2(/128)x=-3FF y=17F  i=0   ( -7.99 ,   2.99 )
97F8: FF 31 3F 53     VEC     scale=3(/64) x=33F  y=1FF  i=5   ( 12.98 ,   7.98 )
97FC: FF 10 FF 07     VEC     scale=1(/256)x=-3FF y=FF   i=0   ( -3.99 ,   0.99 )
9800: FF 24 7F 57     VEC     scale=2(/128)x=-37F y=-FF  i=5   ( -6.99 ,  -1.99 )
9804: FF 21 7F 07     VEC     scale=2(/128)x=-37F y=1FF  i=0   ( -6.99 ,   3.99 )
9808: 00 30 3F 53     VEC     scale=3(/64) x=33F  y=0    i=5   ( 12.98 ,   0.00 )
980C: FF 13 FF 04     VEC     scale=1(/256)x=-FF  y=3FF  i=0   ( -0.99 ,   3.99 )
9810: 7F 21 FF 57     VEC     scale=2(/128)x=-3FF y=17F  i=5   ( -7.99 ,   2.99 )
9814: 01 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
9816: BF 36 BF 52     VEC     scale=3(/64) x=2BF  y=-2BF i=5   ( 10.98 , -10.98 )
981A: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
981E: 7F 23 7F 55     VEC     scale=2(/128)x=-17F y=37F  i=5   ( -2.99 ,   6.99 )
9822: 00 D0           RTS                         
;
9824: 9F 42 00 00     VEC     scale=4(/32) x=0    y=29F  i=0   (  0.00 ,  20.96 )
9828: BF 32 00 F0     VEC     scale=3(/64) x=0    y=2BF  i=15  (  0.00 ,  10.98 )
982C: 03 FE           SVEC    scale=1(/64) x=200  y=-200 i=0   (  8.00 ,  -8.00 )
982E: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9830: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9832: FF 32 7F F2     VEC     scale=3(/64) x=27F  y=2FF  i=15  (  9.98 ,  11.98 )
9836: FF 36 7F 01     VEC     scale=3(/64) x=17F  y=-2FF i=0   (  5.98 , -11.98 )
983A: 3F 35 7F F6     VEC     scale=3(/64) x=-27F y=-13F i=15  ( -9.98 ,  -4.98 )
983E: BF 36 7F 04     VEC     scale=3(/64) x=-7F  y=-2BF i=0   ( -1.98 , -10.98 )
9842: 00 20 7F F3     VEC     scale=2(/128)x=37F  y=0    i=15  (  6.99 ,   0.00 )
9846: 01 FF           SVEC    scale=1(/64) x=0    y=-200 i=0   (  0.00 ,  -8.00 )
9848: 3F 31 3F F7     VEC     scale=3(/64) x=-33F y=13F  i=15  (-12.98 ,   4.98 )
984C: FF 36 3F 00     VEC     scale=3(/64) x=3F   y=-2FF i=0   (  0.98 , -11.98 )
9850: 7F 26 7F F2     VEC     scale=2(/128)x=27F  y=-27F i=15  (  4.99 ,  -4.99 )
9854: 7F 35 BF 06     VEC     scale=3(/64) x=-2BF y=-17F i=0   (-10.98 ,  -5.98 )
9858: 7F 33 7F F5     VEC     scale=3(/64) x=-17F y=37F  i=15  ( -5.98 ,  13.98 )
985C: FF 25 7F 07     VEC     scale=2(/128)x=-37F y=-1FF i=0   ( -6.99 ,  -3.99 )
9860: F0 FF           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9862: 3F 42 3F 05     VEC     scale=4(/32) x=-13F y=23F  i=0   ( -9.96 ,  17.96 )
9866: 7F 27 7F F6     VEC     scale=2(/128)x=-27F y=-37F i=15  ( -4.99 ,  -6.99 )
986A: FF 30 3F 07     VEC     scale=3(/64) x=-33F y=FF   i=0   (-12.98 ,   3.98 )
986E: 7F 31 BF F2     VEC     scale=3(/64) x=2BF  y=17F  i=15  ( 10.98 ,   5.98 )
9872: 7F 23 7F 00     VEC     scale=2(/128)x=7F   y=37F  i=0   (  0.99 ,   6.99 )
9876: FF 34 FF F7     VEC     scale=3(/64) x=-3FF y=-FF  i=15  (-15.98 ,  -3.98 )
987A: 01 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
987C: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
987E: 7F 23 7F 01     VEC     scale=2(/128)x=17F  y=37F  i=0   (  2.99 ,   6.99 )
9882: F7 F1           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
9884: 7F 42 7F 04     VEC     scale=4(/32) x=-7F  y=27F  i=0   ( -3.96 ,  19.96 )
9888: 7F 37 7F F3     VEC     scale=3(/64) x=37F  y=-37F i=15  ( 13.98 , -13.98 )
988C: 7F 20 FF 03     VEC     scale=2(/128)x=3FF  y=7F   i=0   (  7.99 ,   0.99 )
9890: 7F 32 3F F5     VEC     scale=3(/64) x=-13F y=27F  i=15  ( -4.98 ,   9.98 )
9894: 3F 47 7F 01     VEC     scale=4(/32) x=17F  y=-33F i=0   ( 11.96 , -25.96 )
9898: 00 D0           RTS                         
```

# Letters 

Letters of the alphabet

```html
<canvas width="850" height="40"
  data-command="baseScale=1,x=20,y=30,989A,*,*,*,*,98EE,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*">
</canvas>
```

```code
Letters:
; A
;
989A: 90 FA           SVEC    scale=1(/64) x=0    y=200  i=9   (  0.00 ,   8.00 )
989C: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
989E: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
98A0: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98A2: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
98A4: FF 22 FF 07     VEC     scale=2(/128)x=-3FF y=2FF  i=0   ( -7.99 ,   5.99 )
98A8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
98AA: FF 26 FF 03     VEC     scale=2(/128)x=3FF  y=-2FF i=0   (  7.99 ,  -5.99 )
98AE: 00 D0           RTS                         

; B
;
98B0: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
98B4: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
98B6: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98B8: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98BA: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
98BC: 03 F0           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
98BE: 91 F6           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
98C0: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98C2: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
98C4: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
98C6: 00 D0           RTS                         

; C
;
98C8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
98CC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
98CE: 7F 36 00 00     VEC     scale=3(/64) x=0    y=-27F i=0   (  0.00 ,  -9.98 )
98D2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
98D4: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
98D6: 00 D0           RTS                         

; D
;
98D8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
98DC: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
98DE: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98E0: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
98E2: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
98E4: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
98E6: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
98E8: 00 D0           RTS                         

; E
;
98EA: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
98EC: 06 F8           SVEC    scale=1(/64) x=-200 y=0    i=0   ( -8.00 ,   0.00 )
;
; F
98EE: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
98F2: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
98F4: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
98F6: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
98F8: 7F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-17F i=0   ( 15.98 ,  -5.98 )
98FC: 00 D0           RTS                         

; G
;
98FE: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9902: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9904: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
9906: 91 F0           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9908: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
990A: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
990C: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
990E: 00 D0           RTS                         

; H
;
9910: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9914: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
9916: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9918: 00 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
991A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
991E: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9920: 00 D0           RTS                         

; I
;
9922: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9924: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9926: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9928: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
992C: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
992E: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9930: 7F 36 7F 02     VEC     scale=3(/64) x=27F  y=-27F i=0   (  9.98 ,  -9.98 )
9934: 00 D0           RTS                         

; J
;
9936: 00 F1           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9938: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
993A: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
993C: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9940: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
9944: 00 D0           RTS                         

; K
;
9946: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
994A: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
994C: 96 FD           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
994E: FF 26 FF 93     VEC     scale=2(/128)x=3FF  y=-2FF i=9   (  7.99 ,  -5.99 )
9952: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9954: 00 D0           RTS                         

; L
;
9956: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
995A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
995E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9960: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9962: 00 D0           RTS                         

; M
;
9964: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9968: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
996A: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
996C: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9970: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9972: 00 D0           RTS                         

; N
;
9974: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9978: 92 FE           SVEC    scale=1(/64) x=200  y=-200 i=9   (  8.00 ,  -8.00 )
997A: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
997C: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9980: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9982: 00 D0           RTS                         

; O
;
9984: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9988: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
998A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
998E: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9990: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
9992: 00 D0           RTS                         

; P
;
9994: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9998: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
999A: 90 F6           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
999C: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
999E: 7F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-17F i=0   ( 15.98 ,  -5.98 )
99A2: 00 D0           RTS                         

; Q
;
99A4: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
99A8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99AA: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
99AC: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
99AE: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
99B0: 03 F1           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
99B2: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
99B4: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
99B6: 00 D0           RTS                         

; R
;
99B8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
99BC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99BE: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
99C2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
99C4: 7F 26 FF 93     VEC     scale=2(/128)x=3FF  y=-27F i=9   (  7.99 ,  -4.99 )
99C8: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
99CA: 00 D0           RTS                         

; S
;
99CC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99CE: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
99D2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
99D4: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
99D8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99DA: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
99DE: 00 D0           RTS                         

; T
;
99E0: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
99E4: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99E6: 06 F0           SVEC    scale=0(/128)x=-200 y=0    i=0   ( -4.00 ,   0.00 )
99E8: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
99EC: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
99EE: 00 D0           RTS                         

; U
;
99F0: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
99F4: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
99F8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
99FA: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
99FE: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
9A02: 00 D0           RTS                         

; V
;
9A04: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9A08: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
9A0A: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
9A0C: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
9A0E: 90 F3           SVEC    scale=0(/128)x=0    y=200  i=9   (  0.00 ,   4.00 )
9A10: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
9A14: 00 D0           RTS                         

; W
;
9A16: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9A1A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9A1E: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
9A20: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
9A22: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9A26: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
9A2A: 00 D0           RTS                         

; X
;
9A2C: 7F 32 FF 91     VEC     scale=3(/64) x=1FF  y=27F  i=9   (  7.98 ,   9.98 )
9A30: 06 F8           SVEC    scale=1(/64) x=-200 y=0    i=0   ( -8.00 ,   0.00 )
9A32: 7F 36 FF 91     VEC     scale=3(/64) x=1FF  y=-27F i=9   (  7.98 ,  -9.98 )
9A36: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9A38: 00 D0           RTS                         

; Y
;
9A3A: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9A3E: 7F 26 FF 91     VEC     scale=2(/128)x=1FF  y=-27F i=9   (  3.99 ,  -4.99 )
9A42: 7F 22 FF 91     VEC     scale=2(/128)x=1FF  y=27F  i=9   (  3.99 ,   4.99 )
9A46: 06 F6           SVEC    scale=0(/128)x=-200 y=-200 i=0   ( -4.00 ,  -4.00 )
9A48: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
9A4A: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9A4C: 00 D0           RTS                         

; Z
;
9A4E: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9A52: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9A54: 7F 36 FF 95     VEC     scale=3(/64) x=-1FF y=-27F i=9   ( -7.98 ,  -9.98 )
9A58: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9A5A: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9A5C: 00 D0           RTS                         
```

# Numbers 

Numbers and the "space" character

```html
<canvas width="350" height="40"
  data-command="baseScale=1,x=20,y=30,9A5E,*,*,*,*,*,*,*,*,*">
</canvas>
```

```code
Numbers:
; 0
;
9A5E: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9A60: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A62: 90 F3           SVEC    scale=0(/128)x=0    y=200  i=9   (  0.00 ,   4.00 )
9A64: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A66: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9A68: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A6A: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
9A6C: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A6E: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
9A70: 00 30 7F 03     VEC     scale=3(/64) x=37F  y=0    i=0   ( 13.98 ,   0.00 )
9A74: 00 D0           RTS                         

; 1
;
9A76: 7F 23 FF 00     VEC     scale=2(/128)x=FF   y=37F  i=0   (  1.99 ,   6.99 )
9A7A: FF 12 FF 91     VEC     scale=1(/256)x=1FF  y=2FF  i=9   (  1.99 ,   2.99 )
9A7E: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9A82: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9A84: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9A86: 00 30 7F 02     VEC     scale=3(/64) x=27F  y=0    i=0   (  9.98 ,   0.00 )
9A8A: 00 D0           RTS                         

; 2
;
9A8C: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
9A8E: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A90: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9A92: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9A94: FF 16 00 90     VEC     scale=1(/256)x=0    y=-2FF i=9   (  0.00 ,  -2.99 )
9A98: 96 FD           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9A9A: FF 05 00 90     VEC     scale=0(/512)x=0    y=-1FF i=9   (  0.00 ,  -0.99 )
9A9E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9AA0: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9AA2: 00 D0           RTS                         

; 3
;
9AA4: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
9AA6: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AA8: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9AAA: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AAC: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AAE: FF 05 FF 97     VEC     scale=0(/512)x=-3FF y=-1FF i=9   ( -1.99 ,  -0.99 )
9AB2: 95 F0           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AB4: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
9AB6: FF 05 FF 93     VEC     scale=0(/512)x=3FF  y=-1FF i=9   (  1.99 ,  -0.99 )
9ABA: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9ABC: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9ABE: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
9AC0: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AC2: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
9AC6: 00 D0           RTS                         

; 4
;
9AC8: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9ACC: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
9AD0: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9AD2: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
9AD6: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9ADA: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9ADC: 00 D0           RTS                         

; 5
;
9ADE: 7F 32 FF 01     VEC     scale=3(/64) x=1FF  y=27F  i=0   (  7.98 ,   9.98 )
9AE2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9AE4: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
9AE8: FF 01 FF 93     VEC     scale=0(/512)x=3FF  y=1FF  i=9   (  1.99 ,   0.99 )
9AEC: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
9AEE: FF 05 FF 93     VEC     scale=0(/512)x=3FF  y=-1FF i=9   (  1.99 ,  -0.99 )
9AF2: FF 16 00 90     VEC     scale=1(/256)x=0    y=-2FF i=9   (  0.00 ,  -2.99 )
9AF6: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AF8: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
9AFA: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9AFC: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
9B00: 00 D0           RTS                         

; 6
;
9B02: 7F 32 FF 01     VEC     scale=3(/64) x=1FF  y=27F  i=0   (  7.98 ,   9.98 )
9B06: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
9B08: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9B0A: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
9B0C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9B0E: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
9B12: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9B14: 3F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-13F i=0   ( 15.98 ,  -4.98 )
9B18: 00 D0           RTS                         

; 7
;
9B1A: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
9B1E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9B20: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9B22: 96 FE           SVEC    scale=1(/64) x=-200 y=-200 i=9   ( -8.00 ,  -8.00 )
;
; space
9B24: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
9B26: 00 D0           RTS                         

; 8
;
9B28: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9B2C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9B2E: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
9B32: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9B34: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
9B38: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9B3A: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
9B3E: 00 D0           RTS                         

; 9
;
9B40: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9B42: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
9B46: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
9B48: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
9B4C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
9B4E: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
9B52: 00 D0           RTS                         
```

# Special Chars 

Punctuation and special characters

```html
<canvas width="350" height="100"
  data-command="baseScale=1,x=20,y=30,9B54,9B66,9B84,9B94,9B9A,9BA6">
</canvas>
```

```code
Special:
; .
;
9B54: FF 01 FF 91     VEC     scale=0(/512)x=1FF  y=1FF  i=9   (  0.99 ,   0.99 )
9B58: 00 00 FF 05     VEC     scale=0(/512)x=-1FF y=0    i=0   ( -0.99 ,   0.00 )
9B5C: FF 05 FF 91     VEC     scale=0(/512)x=1FF  y=-1FF i=9   (  0.99 ,  -0.99 )
9B60: 00 30 BF 03     VEC     scale=3(/64) x=3BF  y=0    i=0   ( 14.98 ,   0.00 )
9B64: 00 D0           RTS                         

; ,
;
9B66: 00 00 FF 01     VEC     scale=0(/512)x=1FF  y=0    i=0   (  0.99 ,   0.00 )
9B6A: 00 00 FF 95     VEC     scale=0(/512)x=-1FF y=0    i=9   ( -0.99 ,   0.00 )
9B6E: FF 01 00 90     VEC     scale=0(/512)x=0    y=1FF  i=9   (  0.00 ,   0.99 )
9B72: 00 00 FF 91     VEC     scale=0(/512)x=1FF  y=0    i=9   (  0.99 ,   0.00 )
9B76: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
9B78: 3F 30 BF 03     VEC     scale=3(/64) x=3BF  y=3F   i=0   ( 14.98 ,   0.98 )
9B7C: 00 D0           RTS                         

; CR/LF
;
9B7E: 7F 46 FF 05     VEC     scale=4(/32) x=-1FF y=-27F i=0   (-15.96 , -19.96 )
9B82: 00 D0           RTS                         

; Triangle (left)
;
9B84: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
9B86: 7F 22 FF C7     VEC     scale=2(/128)x=-3FF y=27F  i=12  ( -7.99 ,   4.99 )
9B8A: 7F 22 FF C3     VEC     scale=2(/128)x=3FF  y=27F  i=12  (  7.99 ,   4.99 )
9B8E: 7F 36 00 C0     VEC     scale=3(/64) x=0    y=-27F i=12  (  0.00 ,  -9.98 )
9B92: 00 D0           RTS                         

; =
;
9B94: 7F 23 7F 00     VEC     scale=2(/128)x=7F   y=37F  i=0   (  0.99 ,   6.99 )
9B98: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )

; _
9B9A: FF 16 00 00     VEC     scale=1(/256)x=0    y=-2FF i=0   (  0.00 ,  -2.99 )
9B9E: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
9BA0: FF 34 BF 03     VEC     scale=3(/64) x=3BF  y=-FF  i=0   ( 14.98 ,  -3.98 )
9BA4: 00 D0           RTS                         

; Player (as character)
;
9BA6: 4F 54 1F 03     VEC     scale=5(/16) x=31F  y=-4F  i=0   ( 49.93 ,  -4.93 )
9BAA: E9 C9           JSR     $93D2               ; {}
9BAC: 00 D0           RTS                         


; ?? Perhaps ROM padding for some reason

9BAE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BB2: 00 00 2D 00     VEC     scale=0(/512)x=2D   y=0    i=0   (  0.08 ,   0.00 )
9BB6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BBA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BBE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BC2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BC6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BCA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BCE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BD2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BD6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BDA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BDE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BE2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BE6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BEA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BEE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BF2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
9BF6: 00 00 BF 30     VEC     scale=0(/512)x=BF   y=0    i=3   (  0.37 ,   0.00 )
```

# Player (Part 2) 

More ship/thrust pictures like at start

```html
<canvas width="1225" height="100"
  data-command="baseScale=1,x=50,y=50,9C06,x=125,y=50,9C46,x=200,y=50,9C88,x=275,y=50,9CCA,x=350,y=50,9D0E,x=425,y=50,9D4E,x=500,y=50,9D8A,x=575,y=50,9DCA,x=650,y=50,9E0A,x=725,y=50,9E48,x=800,y=50,9E88,x=875,y=50,9EC8,x=950,y=50,9F04,x=1025,y=50,9F44,x=1100,y=50,9F88,x=1175,y=50,9FCA">
</canvas>
```

```code
ShipsB:
; Thrust pattern
9BFA: FF 03 BF 34     VEC     scale=0(/512)x=-BF  y=3FF  i=3   ( -0.37 ,   1.99 )
9BFE: 3F F2           SVEC    scale=2(/32) x=-200 y=200  i=3   (-16.00 ,  16.00 )
9C00: 7F 34 3F F6     VEC     scale=3(/64) x=-23F y=-7F  i=15  ( -8.98 ,  -1.98 )
9C04: 00 D0           RTS                         
; Player facing left
9C06: 00 20 7F 06     VEC     scale=2(/128)x=-27F y=0    i=0   ( -4.99 ,   0.00 )
9C0A: 3F 41 7F F2     VEC     scale=4(/32) x=27F  y=13F  i=15  ( 19.96 ,   9.96 )
9C0E: 9F 46 5F F5     VEC     scale=4(/32) x=-15F y=-29F i=15  (-10.96 , -20.96 )
9C12: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
9C14: 7F 34 7F F2     VEC     scale=3(/64) x=27F  y=-7F  i=15  (  9.98 ,  -1.98 )
9C18: FF 41 1F F6     VEC     scale=4(/32) x=-21F y=1FF  i=15  (-16.96 ,  15.96 )
9C1C: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
9C20: FF 24 7F F2     VEC     scale=2(/128)x=27F  y=-FF  i=15  (  4.99 ,  -1.99 )
9C24: FF 41 1F F2     VEC     scale=4(/32) x=21F  y=1FF  i=15  ( 16.96 ,  15.96 )
9C28: 7F 34 7F F6     VEC     scale=3(/64) x=-27F y=-7F  i=15  ( -9.98 ,  -1.98 )
9C2C: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
9C2E: 9F 46 5F F1     VEC     scale=4(/32) x=15F  y=-29F i=15  ( 10.96 , -20.96 )
9C32: 1F 41 7F F6     VEC     scale=4(/32) x=-27F y=11F  i=15  (-19.96 ,   8.96 )
9C36: 00 D0           RTS                         
;
9C38: 3F 30 FF 03     VEC     scale=3(/64) x=3FF  y=3F   i=0   ( 15.98 ,   0.98 )
9C3C: BF 34 3F F2     VEC     scale=3(/64) x=23F  y=-BF  i=15  (  8.98 ,  -2.98 )
9C40: 7F 34 3F F6     VEC     scale=3(/64) x=-23F y=-7F  i=15  ( -8.98 ,  -1.98 )
9C44: 00 D0           RTS                         
;
9C46: 00 20 7F 06     VEC     scale=2(/128)x=-27F y=0    i=0   ( -4.99 ,   0.00 )
9C4A: FF 40 9F F2     VEC     scale=4(/32) x=29F  y=FF   i=15  ( 20.96 ,   7.96 )
9C4E: 5F 46 9F F5     VEC     scale=4(/32) x=-19F y=-25F i=15  (-12.96 , -18.96 )
9C52: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
9C54: BF 34 7F F2     VEC     scale=3(/64) x=27F  y=-BF  i=15  (  9.98 ,  -2.98 )
9C58: 3F 42 FF F5     VEC     scale=4(/32) x=-1FF y=23F  i=15  (-15.96 ,  17.96 )
9C5C: FF 24 7F F6     VEC     scale=2(/128)x=-27F y=-FF  i=15  ( -4.99 ,  -1.99 )
9C60: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
9C64: BF 41 3F F2     VEC     scale=4(/32) x=23F  y=1BF  i=15  ( 17.96 ,  13.96 )
9C68: 3F 34 7F F6     VEC     scale=3(/64) x=-27F y=-3F  i=15  ( -9.98 ,  -0.98 )
9C6C: 7F 24 FF F3     VEC     scale=2(/128)x=3FF  y=-7F  i=15  (  7.99 ,  -0.99 )
9C70: BF 46 1F F1     VEC     scale=4(/32) x=11F  y=-2BF i=15  (  8.96 , -21.96 )
9C74: 5F 41 5F F6     VEC     scale=4(/32) x=-25F y=15F  i=15  (-18.96 ,  10.96 )
9C78: 00 D0           RTS                         
;
9C7A: 00 30 FF 03     VEC     scale=3(/64) x=3FF  y=0    i=0   ( 15.98 ,   0.00 )
9C7E: FF 25 FF F3     VEC     scale=2(/128)x=3FF  y=-1FF i=15  (  7.99 ,  -3.99 )
9C82: 3F 34 3F F6     VEC     scale=3(/64) x=-23F y=-3F  i=15  ( -8.98 ,  -0.98 )
9C86: 00 D0           RTS                         
;
9C88: 7F 20 7F 06     VEC     scale=2(/128)x=-27F y=7F   i=0   ( -4.99 ,   0.99 )
9C8C: BF 40 BF F2     VEC     scale=4(/32) x=2BF  y=BF   i=15  ( 21.96 ,   5.96 )
9C90: 5F 46 DF F5     VEC     scale=4(/32) x=-1DF y=-25F i=15  (-14.96 , -18.96 )
9C94: FF 20 FF F7     VEC     scale=2(/128)x=-3FF y=FF   i=15  ( -7.99 ,   1.99 )
9C98: FF 34 3F F2     VEC     scale=3(/64) x=23F  y=-FF  i=15  (  8.98 ,  -3.98 )
9C9C: 5F 42 9F F5     VEC     scale=4(/32) x=-19F y=25F  i=15  (-12.96 ,  18.96 )
9CA0: F7 F5           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
9CA2: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
9CA6: 7F 41 7F F2     VEC     scale=4(/32) x=27F  y=17F  i=15  ( 19.96 ,  11.96 )
9CAA: 3F 30 BF F6     VEC     scale=3(/64) x=-2BF y=3F   i=15  (-10.98 ,   0.98 )
9CAE: FF 24 FF F3     VEC     scale=2(/128)x=3FF  y=-FF  i=15  (  7.99 ,  -1.99 )
9CB2: DF 46 DF F0     VEC     scale=4(/32) x=DF   y=-2DF i=15  (  6.96 , -22.96 )
9CB6: 9F 41 3F F6     VEC     scale=4(/32) x=-23F y=19F  i=15  (-17.96 ,  12.96 )
9CBA: 00 D0           RTS                         
;
9CBC: 3F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-3F  i=0   ( 15.98 ,  -0.98 )
9CC0: FF 26 FF F3     VEC     scale=2(/128)x=3FF  y=-2FF i=15  (  7.99 ,  -5.99 )
9CC4: 00 30 7F F6     VEC     scale=3(/64) x=-27F y=0    i=15  ( -9.98 ,   0.00 )
9CC8: 00 D0           RTS                         
;
9CCA: 7F 20 7F 06     VEC     scale=2(/128)x=-27F y=7F   i=0   ( -4.99 ,   0.99 )
9CCE: 7F 40 BF F2     VEC     scale=4(/32) x=2BF  y=7F   i=15  ( 21.96 ,   3.96 )
9CD2: 1F 46 1F F6     VEC     scale=4(/32) x=-21F y=-21F i=15  (-16.96 , -16.96 )
9CD6: 7F 21 7F F7     VEC     scale=2(/128)x=-37F y=17F  i=15  ( -6.99 ,   2.99 )
9CDA: 3F 35 3F F2     VEC     scale=3(/64) x=23F  y=-13F i=15  (  8.98 ,  -4.98 )
9CDE: 7F 42 7F F5     VEC     scale=4(/32) x=-17F y=27F  i=15  (-11.96 ,  19.96 )
9CE2: 7F 24 7F F6     VEC     scale=2(/128)x=-27F y=-7F  i=15  ( -4.99 ,  -0.99 )
9CE6: 7F 26 FF F1     VEC     scale=2(/128)x=1FF  y=-27F i=15  (  3.99 ,  -4.99 )
9CEA: 5F 41 9F F2     VEC     scale=4(/32) x=29F  y=15F  i=15  ( 20.96 ,  10.96 )
9CEE: 7F 30 7F F6     VEC     scale=3(/64) x=-27F y=7F   i=15  ( -9.98 ,   1.98 )
9CF2: 7F 25 7F F3     VEC     scale=2(/128)x=37F  y=-17F i=15  (  6.99 ,  -2.99 )
9CF6: DF 46 7F F0     VEC     scale=4(/32) x=7F   y=-2DF i=15  (  3.96 , -22.96 )
9CFA: 7F 33 FF F7     VEC     scale=3(/64) x=-3FF y=37F  i=15  (-15.98 ,  13.98 )
9CFE: 00 D0           RTS                         
;
9D00: BF 34 FF 03     VEC     scale=3(/64) x=3FF  y=-BF  i=0   ( 15.98 ,  -2.98 )
9D04: FF 26 7F F3     VEC     scale=2(/128)x=37F  y=-2FF i=15  (  6.99 ,  -5.99 )
9D08: 3F 30 7F F6     VEC     scale=3(/64) x=-27F y=3F   i=15  ( -9.98 ,   0.98 )
9D0C: 00 D0           RTS                         
;
9D0E: FF 20 7F 06     VEC     scale=2(/128)x=-27F y=FF   i=0   ( -4.99 ,   1.99 )
9D12: 1F 40 DF F2     VEC     scale=4(/32) x=2DF  y=1F   i=15  ( 22.96 ,   0.96 )
9D16: DF 45 3F F6     VEC     scale=4(/32) x=-23F y=-1DF i=15  (-17.96 , -14.96 )
9D1A: F6 F9           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
9D1C: 7F 27 FF F3     VEC     scale=2(/128)x=3FF  y=-37F i=15  (  7.99 ,  -6.99 )
9D20: BF 42 1F F5     VEC     scale=4(/32) x=-11F y=2BF  i=15  ( -8.96 ,  21.96 )
9D24: 7F 24 FF F6     VEC     scale=2(/128)x=-2FF y=-7F  i=15  ( -5.99 ,  -0.99 )
9D28: 7F 26 FF F1     VEC     scale=2(/128)x=1FF  y=-27F i=15  (  3.99 ,  -4.99 )
9D2C: 1F 41 BF F2     VEC     scale=4(/32) x=2BF  y=11F  i=15  ( 21.96 ,   8.96 )
9D30: BF 30 BF F6     VEC     scale=3(/64) x=-2BF y=BF   i=15  (-10.98 ,   2.98 )
9D34: F2 FD           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
9D36: DF 46 3F F0     VEC     scale=4(/32) x=3F   y=-2DF i=15  (  1.96 , -22.96 )
9D3A: FF 33 BF F7     VEC     scale=3(/64) x=-3BF y=3FF  i=15  (-14.98 ,  15.98 )
9D3E: 00 D0           RTS                         
;
9D40: FF 34 BF 03     VEC     scale=3(/64) x=3BF  y=-FF  i=0   ( 14.98 ,  -3.98 )
9D44: 7F 27 7F F3     VEC     scale=2(/128)x=37F  y=-37F i=15  (  6.99 ,  -6.99 )
9D48: 3F 30 3F F6     VEC     scale=3(/64) x=-23F y=3F   i=15  ( -8.98 ,   0.98 )
9D4C: 00 D0           RTS                         
;
9D4E: 06 F1           SVEC    scale=0(/128)x=-200 y=0    i=0   ( -4.00 ,   0.00 )
9D50: 1F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-1F  i=15  ( 21.96 ,  -0.96 )
9D54: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
9D58: F6 F9           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
9D5A: BF 35 3F F2     VEC     scale=3(/64) x=23F  y=-1BF i=15  (  8.98 ,  -6.98 )
9D5E: DF 42 FF F4     VEC     scale=4(/32) x=-FF  y=2DF  i=15  ( -7.96 ,  22.96 )
9D62: F7 F0           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
9D64: 7F 26 7F F1     VEC     scale=2(/128)x=17F  y=-27F i=15  (  2.99 ,  -4.99 )
9D68: BF 40 DF F2     VEC     scale=4(/32) x=2DF  y=BF   i=15  ( 22.96 ,   5.96 )
9D6C: BF 30 BF F6     VEC     scale=3(/64) x=-2BF y=BF   i=15  (-10.98 ,   2.98 )
9D70: F2 FD           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
9D72: DF 46 1F F4     VEC     scale=4(/32) x=-1F  y=-2DF i=15  ( -0.96 , -22.96 )
9D76: 1F 42 7F F5     VEC     scale=4(/32) x=-17F y=21F  i=15  (-11.96 ,  16.96 )
9D7A: 00 D0           RTS                         
;
9D7C: 7F 35 BF 03     VEC     scale=3(/64) x=3BF  y=-17F i=0   ( 14.98 ,  -5.98 )
9D80: 7F 27 FF F2     VEC     scale=2(/128)x=2FF  y=-37F i=15  (  5.99 ,  -6.99 )
9D84: 7F 30 7F F6     VEC     scale=3(/64) x=-27F y=7F   i=15  ( -9.98 ,   1.98 )
9D88: 00 D0           RTS                         
;
9D8A: FF 12 FF 07     VEC     scale=1(/256)x=-3FF y=2FF  i=0   ( -3.99 ,   2.99 )
9D8E: 5F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-5F  i=15  ( 21.96 ,  -2.96 )
9D92: 7F 45 7F F6     VEC     scale=4(/32) x=-27F y=-17F i=15  (-19.96 , -11.96 )
9D96: 7F 22 FF F7     VEC     scale=2(/128)x=-3FF y=27F  i=15  ( -7.99 ,   4.99 )
9D9A: F2 FE           SVEC    scale=1(/64) x=200  y=-200 i=15  (  8.00 ,  -8.00 )
9D9C: FF 42 9F F4     VEC     scale=4(/32) x=-9F  y=2FF  i=15  ( -4.96 ,  23.96 )
9DA0: F7 F0           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
9DA2: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
9DA6: 7F 40 FF F2     VEC     scale=4(/32) x=2FF  y=7F   i=15  ( 23.96 ,   3.96 )
9DAA: FF 30 BF F6     VEC     scale=3(/64) x=-2BF y=FF   i=15  (-10.98 ,   3.98 )
9DAE: 7F 26 FF F3     VEC     scale=2(/128)x=3FF  y=-27F i=15  (  7.99 ,  -4.99 )
9DB2: DF 46 5F F4     VEC     scale=4(/32) x=-5F  y=-2DF i=15  ( -2.96 , -22.96 )
9DB6: 5F 42 5F F5     VEC     scale=4(/32) x=-15F y=25F  i=15  (-10.96 ,  18.96 )
9DBA: 00 D0           RTS                         
;
9DBC: BF 35 7F 03     VEC     scale=3(/64) x=37F  y=-1BF i=0   ( 13.98 ,  -6.98 )
9DC0: FF 27 7F F2     VEC     scale=2(/128)x=27F  y=-3FF i=15  (  4.99 ,  -7.99 )
9DC4: BF 30 3F F6     VEC     scale=3(/64) x=-23F y=BF   i=15  ( -8.98 ,   2.98 )
9DC8: 00 D0           RTS                         
;
9DCA: FF 12 FF 07     VEC     scale=1(/256)x=-3FF y=2FF  i=0   ( -3.99 ,   2.99 )
9DCE: 7F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-7F  i=15  ( 21.96 ,  -3.96 )
9DD2: 3F 45 BF F6     VEC     scale=4(/32) x=-2BF y=-13F i=15  (-21.96 ,  -9.96 )
9DD6: 7F 22 7F F7     VEC     scale=2(/128)x=-37F y=27F  i=15  ( -6.99 ,   4.99 )
9DDA: F2 FE           SVEC    scale=1(/64) x=200  y=-200 i=15  (  8.00 ,  -8.00 )
9DDC: DF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2DF  i=15  ( -3.96 ,  22.96 )
9DE0: 7F 20 7F F6     VEC     scale=2(/128)x=-27F y=7F   i=15  ( -4.99 ,   0.99 )
9DE4: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
9DE8: 1F 40 DF F2     VEC     scale=4(/32) x=2DF  y=1F   i=15  ( 22.96 ,   0.96 )
9DEC: 7F 31 3F F6     VEC     scale=3(/64) x=-23F y=17F  i=15  ( -8.98 ,   5.98 )
9DF0: F3 F7           SVEC    scale=0(/128)x=200  y=-200 i=15  (  4.00 ,  -4.00 )
9DF2: DF 46 9F F4     VEC     scale=4(/32) x=-9F  y=-2DF i=15  ( -4.96 , -22.96 )
9DF6: 7F 42 1F F5     VEC     scale=4(/32) x=-11F y=27F  i=15  ( -8.96 ,  19.96 )
9DFA: 00 D0           RTS                         
;
9DFC: 3F 36 3F 03     VEC     scale=3(/64) x=33F  y=-23F i=0   ( 12.98 ,  -8.98 )
9E00: FF 27 FF F1     VEC     scale=2(/128)x=1FF  y=-3FF i=15  (  3.99 ,  -7.99 )
9E04: FF 21 FF F7     VEC     scale=2(/128)x=-3FF y=1FF  i=15  ( -7.99 ,   3.99 )
9E08: 00 D0           RTS                         
;
9E0A: 06 F2           SVEC    scale=0(/128)x=-200 y=200  i=0   ( -4.00 ,   4.00 )
9E0C: DF 44 9F F2     VEC     scale=4(/32) x=29F  y=-DF  i=15  ( 20.96 ,  -6.96 )
9E10: FF 44 BF F6     VEC     scale=4(/32) x=-2BF y=-FF  i=15  (-21.96 ,  -7.96 )
9E14: F7 F3           SVEC    scale=0(/128)x=-200 y=200  i=15  ( -4.00 ,   4.00 )
9E16: 3F 36 7F F1     VEC     scale=3(/64) x=17F  y=-23F i=15  (  5.98 ,  -8.98 )
9E1A: FF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2FF  i=15  ( -0.96 ,  23.96 )
9E1E: 7F 20 7F F6     VEC     scale=2(/128)x=-27F y=7F   i=15  ( -4.99 ,   0.99 )
9E22: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
9E26: 1F 44 FF F2     VEC     scale=4(/32) x=2FF  y=-1F  i=15  ( 23.96 ,  -0.96 )
9E2A: 7F 31 3F F6     VEC     scale=3(/64) x=-23F y=17F  i=15  ( -8.98 ,   5.98 )
9E2E: F3 F7           SVEC    scale=0(/128)x=200  y=-200 i=15  (  4.00 ,  -4.00 )
9E30: BF 46 FF F4     VEC     scale=4(/32) x=-FF  y=-2BF i=15  ( -7.96 , -21.96 )
9E34: 9F 42 DF F4     VEC     scale=4(/32) x=-DF  y=29F  i=15  ( -6.96 ,  20.96 )
9E38: 00 D0           RTS                         
;
9E3A: 7F 36 FF 02     VEC     scale=3(/64) x=2FF  y=-27F i=0   ( 11.98 ,  -9.98 )
9E3E: 3F 36 BF F0     VEC     scale=3(/64) x=BF   y=-23F i=15  (  2.98 ,  -8.98 )
9E42: 7F 22 FF F7     VEC     scale=2(/128)x=-3FF y=27F  i=15  ( -7.99 ,   4.99 )
9E46: 00 D0           RTS                         
;
9E48: FF 13 FF 06     VEC     scale=1(/256)x=-2FF y=3FF  i=0   ( -2.99 ,   3.99 )
9E4C: 1F 45 7F F2     VEC     scale=4(/32) x=27F  y=-11F i=15  ( 19.96 ,  -8.96 )
9E50: 9F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-9F  i=15  (-22.96 ,  -4.96 )
9E54: F7 F3           SVEC    scale=0(/128)x=-200 y=200  i=15  ( -4.00 ,   4.00 )
9E56: 3F 36 7F F1     VEC     scale=3(/64) x=17F  y=-23F i=15  (  5.98 ,  -8.98 )
9E5A: DF 42 1F F0     VEC     scale=4(/32) x=1F   y=2DF  i=15  (  0.96 ,  22.96 )
9E5E: FF 20 7F F6     VEC     scale=2(/128)x=-27F y=FF   i=15  ( -4.99 ,   1.99 )
9E62: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
9E66: 7F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-7F  i=15  ( 22.96 ,  -3.96 )
9E6A: F6 FA           SVEC    scale=1(/64) x=-200 y=200  i=15  ( -8.00 ,   8.00 )
9E6C: 7F 27 7F F2     VEC     scale=2(/128)x=27F  y=-37F i=15  (  4.99 ,  -6.99 )
9E70: BF 46 3F F5     VEC     scale=4(/32) x=-13F y=-2BF i=15  ( -9.96 , -21.96 )
9E74: BF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2BF  i=15  ( -3.96 ,  21.96 )
9E78: 00 D0           RTS                         
;
9E7A: BF 36 BF 02     VEC     scale=3(/64) x=2BF  y=-2BF i=0   ( 10.98 , -10.98 )
9E7E: 7F 36 7F F0     VEC     scale=3(/64) x=7F   y=-27F i=15  (  1.98 ,  -9.98 )
9E82: FF 22 7F F7     VEC     scale=2(/128)x=-37F y=2FF  i=15  ( -6.99 ,   5.99 )
9E86: 00 D0           RTS                         
;
9E88: FF 13 FF 06     VEC     scale=1(/256)x=-2FF y=3FF  i=0   ( -2.99 ,   3.99 )
9E8C: 5F 45 5F F2     VEC     scale=4(/32) x=25F  y=-15F i=15  ( 18.96 , -10.96 )
9E90: 5F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-5F  i=15  (-22.96 ,  -2.96 )
9E94: FF 23 7F F6     VEC     scale=2(/128)x=-27F y=3FF  i=15  ( -4.99 ,   7.99 )
9E98: BF 36 FF F0     VEC     scale=3(/64) x=FF   y=-2BF i=15  (  3.98 , -10.98 )
9E9C: FF 42 7F F0     VEC     scale=4(/32) x=7F   y=2FF  i=15  (  3.96 ,  23.96 )
9EA0: FF 20 7F F6     VEC     scale=2(/128)x=-27F y=FF   i=15  ( -4.99 ,   1.99 )
9EA4: F4 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
9EA6: 9F 44 FF F2     VEC     scale=4(/32) x=2FF  y=-9F  i=15  ( 23.96 ,  -4.96 )
9EAA: F6 FA           SVEC    scale=1(/64) x=-200 y=200  i=15  ( -8.00 ,   8.00 )
9EAC: FF 27 7F F2     VEC     scale=2(/128)x=27F  y=-3FF i=15  (  4.99 ,  -7.99 )
9EB0: 7F 46 7F F5     VEC     scale=4(/32) x=-17F y=-27F i=15  (-11.96 , -19.96 )
9EB4: BF 42 5F F4     VEC     scale=4(/32) x=-5F  y=2BF  i=15  ( -2.96 ,  21.96 )
9EB8: 00 D0           RTS                         
;
9EBA: 3F 37 7F 02     VEC     scale=3(/64) x=27F  y=-33F i=0   (  9.98 , -12.98 )
9EBE: 3F 36 3F F0     VEC     scale=3(/64) x=3F   y=-23F i=15  (  0.98 ,  -8.98 )
9EC2: 7F 23 7F F7     VEC     scale=2(/128)x=-37F y=37F  i=15  ( -6.99 ,   6.99 )
9EC6: 00 D0           RTS                         
;
9EC8: 05 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
9ECA: 7F 45 1F F2     VEC     scale=4(/32) x=21F  y=-17F i=15  ( 16.96 , -11.96 )
9ECE: 1F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-1F  i=15  (-22.96 ,  -0.96 )
9ED2: F5 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
9ED4: BF 36 BF F0     VEC     scale=3(/64) x=BF   y=-2BF i=15  (  2.98 , -10.98 )
9ED8: DF 42 BF F0     VEC     scale=4(/32) x=BF   y=2DF  i=15  (  5.96 ,  22.96 )
9EDC: 7F 21 7F F6     VEC     scale=2(/128)x=-27F y=17F  i=15  ( -4.99 ,   2.99 )
9EE0: F4 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
9EE2: FF 44 DF F2     VEC     scale=4(/32) x=2DF  y=-FF  i=15  ( 22.96 ,  -7.96 )
9EE6: 3F 32 BF F5     VEC     scale=3(/64) x=-1BF y=23F  i=15  ( -6.98 ,   8.98 )
9EEA: F1 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9EEC: 5F 46 9F F5     VEC     scale=4(/32) x=-19F y=-25F i=15  (-12.96 , -18.96 )
9EF0: BF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2BF  i=15  ( -0.96 ,  21.96 )
9EF4: 00 D0           RTS                         
;
9EF6: 3F 37 FF 01     VEC     scale=3(/64) x=1FF  y=-33F i=0   (  7.98 , -12.98 )
9EFA: 7F 36 3F F0     VEC     scale=3(/64) x=3F   y=-27F i=15  (  0.98 ,  -9.98 )
9EFE: 7F 23 FF F6     VEC     scale=2(/128)x=-2FF y=37F  i=15  ( -5.99 ,   6.99 )
9F02: 00 D0           RTS                         
;
9F04: 7F 22 FF 04     VEC     scale=2(/128)x=-FF  y=27F  i=0   ( -1.99 ,   4.99 )
9F08: BF 37 FF F3     VEC     scale=3(/64) x=3FF  y=-3BF i=15  ( 15.98 , -14.98 )
9F0C: 3F 40 DF F6     VEC     scale=4(/32) x=-2DF y=3F   i=15  (-22.96 ,   1.96 )
9F10: F5 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
9F12: BF 36 BF F0     VEC     scale=3(/64) x=BF   y=-2BF i=15  (  2.98 , -10.98 )
9F16: BF 42 1F F1     VEC     scale=4(/32) x=11F  y=2BF  i=15  (  8.96 ,  21.96 )
9F1A: FF 21 7F F6     VEC     scale=2(/128)x=-27F y=1FF  i=15  ( -4.99 ,   3.99 )
9F1E: FF 26 7F F4     VEC     scale=2(/128)x=-7F  y=-2FF i=15  ( -0.99 ,  -5.99 )
9F22: 1F 45 BF F2     VEC     scale=4(/32) x=2BF  y=-11F i=15  ( 21.96 ,  -8.96 )
9F26: FF 23 7F F7     VEC     scale=2(/128)x=-37F y=3FF  i=15  ( -6.99 ,   7.99 )
9F2A: F1 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9F2C: 3F 46 DF F5     VEC     scale=4(/32) x=-1DF y=-23F i=15  (-14.96 , -17.96 )
9F30: DF 42 1F F0     VEC     scale=4(/32) x=1F   y=2DF  i=15  (  0.96 ,  22.96 )
9F34: 00 D0           RTS                         
;
9F36: 7F 37 BF 01     VEC     scale=3(/64) x=1BF  y=-37F i=0   (  6.98 , -13.98 )
9F3A: 7F 36 00 F4     VEC     scale=3(/64) x=0    y=-27F i=15  (  0.00 ,  -9.98 )
9F3E: FF 23 FF F6     VEC     scale=2(/128)x=-2FF y=3FF  i=15  ( -5.99 ,   7.99 )
9F42: 00 D0           RTS                         
;
9F44: 7F 22 7F 04     VEC     scale=2(/128)x=-7F  y=27F  i=0   ( -0.99 ,   4.99 )
9F48: FF 37 7F F3     VEC     scale=3(/64) x=37F  y=-3FF i=15  ( 13.98 , -15.98 )
9F4C: 7F 40 DF F6     VEC     scale=4(/32) x=-2DF y=7F   i=15  (-22.96 ,   3.96 )
9F50: 7F 23 7F F5     VEC     scale=2(/128)x=-17F y=37F  i=15  ( -2.99 ,   6.99 )
9F54: 7F 36 7F F0     VEC     scale=3(/64) x=7F   y=-27F i=15  (  1.98 ,  -9.98 )
9F58: 9F 42 5F F1     VEC     scale=4(/32) x=15F  y=29F  i=15  ( 10.96 ,  20.96 )
9F5C: FF 21 7F F6     VEC     scale=2(/128)x=-27F y=1FF  i=15  ( -4.99 ,   3.99 )
9F60: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
9F64: 7F 45 7F F2     VEC     scale=4(/32) x=27F  y=-17F i=15  ( 19.96 , -11.96 )
9F68: 3F 32 3F F5     VEC     scale=3(/64) x=-13F y=23F  i=15  ( -4.98 ,   8.98 )
9F6C: 7F 27 7F F1     VEC     scale=2(/128)x=17F  y=-37F i=15  (  2.99 ,  -6.99 )
9F70: 1F 46 1F F6     VEC     scale=4(/32) x=-21F y=-21F i=15  (-16.96 , -16.96 )
9F74: BF 42 7F F0     VEC     scale=4(/32) x=7F   y=2BF  i=15  (  3.96 ,  21.96 )
9F78: 00 D0           RTS                         
;
9F7A: BF 37 3F 01     VEC     scale=3(/64) x=13F  y=-3BF i=0   (  4.98 , -14.98 )
9F7E: 3F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-23F i=15  ( -0.98 ,  -8.98 )
9F82: FF 23 FF F5     VEC     scale=2(/128)x=-1FF y=3FF  i=15  ( -3.99 ,   7.99 )
9F86: 00 D0           RTS                         
;
9F88: 7F 22 7F 04     VEC     scale=2(/128)x=-7F  y=27F  i=0   ( -0.99 ,   4.99 )
9F8C: 3F 46 9F F1     VEC     scale=4(/32) x=19F  y=-23F i=15  ( 12.96 , -17.96 )
9F90: DF 40 DF F6     VEC     scale=4(/32) x=-2DF y=DF   i=15  (-22.96 ,   6.96 )
9F94: FF 23 FF F4     VEC     scale=2(/128)x=-FF  y=3FF  i=15  ( -1.99 ,   7.99 )
9F98: BF 36 3F F0     VEC     scale=3(/64) x=3F   y=-2BF i=15  (  0.98 , -10.98 )
9F9C: 7F 42 7F F1     VEC     scale=4(/32) x=17F  y=27F  i=15  ( 11.96 ,  19.96 )
9FA0: 7F 22 7F F5     VEC     scale=2(/128)x=-17F y=27F  i=15  ( -2.99 ,   4.99 )
9FA4: F5 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
9FA6: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
9FAA: 3F 32 FF F4     VEC     scale=3(/64) x=-FF  y=23F  i=15  ( -3.98 ,   8.98 )
9FAE: FF 27 FF F0     VEC     scale=2(/128)x=FF   y=-3FF i=15  (  1.99 ,  -7.99 )
9FB2: DF 45 5F F6     VEC     scale=4(/32) x=-25F y=-1DF i=15  (-18.96 , -14.96 )
9FB6: BF 42 BF F0     VEC     scale=4(/32) x=BF   y=2BF  i=15  (  5.96 ,  21.96 )
9FBA: 00 D0           RTS                         
;
9FBC: FF 37 FF 00     VEC     scale=3(/64) x=FF   y=-3FF i=0   (  3.98 , -15.98 )
9FC0: 3F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-23F i=15  ( -1.98 ,  -8.98 )
9FC4: 3F 32 BF F4     VEC     scale=3(/64) x=-BF  y=23F  i=15  ( -2.98 ,   8.98 )
9FC8: 00 D0           RTS                         
;
9FCA: 7F 22 00 04     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
9FCE: 5F 46 5F F1     VEC     scale=4(/32) x=15F  y=-25F i=15  ( 10.96 , -18.96 )
9FD2: 1F 41 BF F6     VEC     scale=4(/32) x=-2BF y=11F  i=15  (-21.96 ,   8.96 )
9FD6: FF 23 7F F4     VEC     scale=2(/128)x=-7F  y=3FF  i=15  ( -0.99 ,   7.99 )
9FDA: 7F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-27F i=15  ( -0.98 ,  -9.98 )
9FDE: 3F 42 BF F1     VEC     scale=4(/32) x=1BF  y=23F  i=15  ( 13.96 ,  17.96 )
9FE2: 7F 22 7F F5     VEC     scale=2(/128)x=-17F y=27F  i=15  ( -2.99 ,   4.99 )
9FE6: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
9FEA: FF 45 3F F2     VEC     scale=4(/32) x=23F  y=-1FF i=15  ( 17.96 , -15.96 )
9FEE: 7F 32 BF F4     VEC     scale=3(/64) x=-BF  y=27F  i=15  ( -2.98 ,   9.98 )
9FF2: F4 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
9FF4: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
9FF8: 9F 42 FF F0     VEC     scale=4(/32) x=FF   y=29F  i=15  (  7.96 ,  20.96 )
9FFC: 00 D0           RTS                         

; ?? not used
9FFE: FB FF           SVEC    scale=3(/16) x=200  y=-200 i=15  ( 32.00 , -32.00 )
```

```html
<script src="/js/Binary.js"></script>
<script src="/js/DVG.js"></script>
<script src="/js/Canvas.js"></script>
<script>
    window.onload = function() {   
        DVG.data = Binary.readBinary('VectorROM.md.bin')     
        Canvas.redrawGraphics()       
    }    
</script>
```

