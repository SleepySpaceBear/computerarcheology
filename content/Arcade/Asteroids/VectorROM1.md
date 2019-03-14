![Asteroids DVG Vector ROM](Asteroids.jpg)

# Asteroids DVG Vector ROM

```{html
<script src="/Arcade/Asteroids/VectorROM.js"></script>

<script src="/js/BinaryData.js"></script>
<script src="/js/DVG.js"></script>
<script src="/js/CANVAS.js"></script>
```

```
; OriginalBinary 035127.01 (Rev 1)

;;= TODO =

;; Lots of info here about what the areas in the ROM are:
;; [http://arcarc.xmission.com/Tech/dvg.txt http://arcarc.xmission.com/Tech/dvg.txt]

;; Thanks to [https://github.com/slx7R4GDZM slx7R4GDZM] for many fixes and discoveries here.

;;= DVG Info =

;; For info about the vector generator hardware and opcodes:
;;
;; [/Arcade/DVG.html DVG Information]

;;= Test Pattern =

; Diamond pattern across screen with a parallel
; line pattern in the center.

;;{{{html
;;<canvas width="520" height="520"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="screenScale=0.5,0800">
;;</canvas>
;;}}}

0800: 80 A0 00 00    CUR scale=00(/512)   y=128  x=0                 
0804: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
0808: 00 90 ff 73    VEC  scale=09(/1)    bri=07  x=1023    y=0      (1023.00, 0.00)
080C: ff 92 00 70    VEC  scale=09(/1)    bri=07  x=0       y=767    (0.00, 767.00)
0810: 00 90 ff 77    VEC  scale=09(/1)    bri=07  x=-1023   y=0      (-1023.00, 0.00)
0814: ff 96 00 70    VEC  scale=09(/1)    bri=07  x=0       y=-767   (0.00, -767.00)
;
0818: ff 92 ff 72    VEC  scale=09(/1)    bri=07  x=767     y=767    (767.00, 767.00)
081C: 00 86 00 72    VEC  scale=08(/2)    bri=07  x=512     y=-512   (256.00, -256.00)
0820: fe 87 fe 77    VEC  scale=08(/2)    bri=07  x=-1022   y=-1022  (-511.00, -511.00)
0824: 00 92 00 76    VEC  scale=09(/1)    bri=07  x=-512    y=512    (-512.00, 512.00)
0828: fe 81 00 72    VEC  scale=08(/2)    bri=07  x=512     y=510    (256.00, 255.00)
082C: ff 96 ff 72    VEC  scale=09(/1)    bri=07  x=767     y=-767   (767.00, -767.00)
;
0830: 7f a3 ff 03    CUR  scale=00(/512)  y=895  x=1023
0834: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
0838: ff 96 ff 76    VEC  scale=09(/1)    bri=07  x=-767    y=-767   (-767.00, -767.00)
083C: fe 81 00 76    VEC  scale=08(/2)    bri=07  x=-512    y=510    (-256.00, 255.00)
0840: 00 92 00 72    VEC  scale=09(/1)    bri=07  x=512     y=512    (512.00, 512.00)
0844: fe 87 fe 73    VEC  scale=08(/2)    bri=07  x=1022    y=-1022  (511.00, -511.00)
0848: 00 86 00 76    VEC  scale=08(/2)    bri=07  x=-512    y=-512   (-256.00, -256.00)
084C: ff 92 ff 76    VEC  scale=09(/1)    bri=07  x=-767    y=767    (-767.00, 767.00)
;
0850: fc a1 f4 01    CUR  scale=00(/512)  y=508  x=500
0854: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
0858: db f0          SVEC scale=02(/128)  bri=13  x=3       y=0      (0.02, 0.00)
085A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
085C: cf f0          SVEC scale=02(/128)  bri=12  x=-3      y=0      (-0.02, 0.00)
085E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0860: bb f0          SVEC scale=02(/128)  bri=11  x=3       y=0      (0.02, 0.00)
0862: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0864: af f0          SVEC scale=02(/128)  bri=10  x=-3      y=0      (-0.02, 0.00)
0866: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0868: 9b f0          SVEC scale=02(/128)  bri=09  x=3       y=0      (0.02, 0.00)
086A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
086C: 8f f0          SVEC scale=02(/128)  bri=08  x=-3      y=0      (-0.02, 0.00)
086E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0870: 7b f0          SVEC scale=02(/128)  bri=07  x=3       y=0      (0.02, 0.00)
0872: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0874: 6f f0          SVEC scale=02(/128)  bri=06  x=-3      y=0      (-0.02, 0.00)
0876: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0878: 5b f0          SVEC scale=02(/128)  bri=05  x=3       y=0      (0.02, 0.00)
087A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
087C: 4f f0          SVEC scale=02(/128)  bri=04  x=-3      y=0      (-0.02, 0.00)
087E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0880: 3b f0          SVEC scale=02(/128)  bri=03  x=3       y=0      (0.02, 0.00)
0882: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
0884: 2f f0          SVEC scale=02(/128)  bri=02  x=-3      y=0      (-0.02, 0.00)
0886: 4c d0          RTS                                               ; ?? 0x4c

;;= Page Select Error =

;;{{{html
;;<canvas width="500" height="60"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=20,y=45,baseScale=1,088C">
;;</canvas>
;;}}}

; "PAGE SELECT ERROR"
0888: e4 a0 2c 11    CUR  scale=01(/256)  y=228  x=300                 
088C: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
0890: e4 ca          JSR  $0DC8                                        ; {} P
0892: 79 ca          JSR  $0CF2                                        ; {} A
0894: ab ca          JSR  $0D56                                        ; {} G
0896: 9c ca          JSR  $0D38                                        ; {} E
0898: 2d cb          JSR  $0E5A                                        ; {} SPACE
089A: fc ca          JSR  $0DF8                                        ; {} S
089C: 9c ca          JSR  $0D38                                        ; {} E
089E: ce ca          JSR  $0D9C                                        ; {} L
08A0: 9c ca          JSR  $0D38                                        ; {} E
08A2: 8e ca          JSR  $0D1C                                        ; {} C
08A4: 03 cb          JSR  $0E06                                        ; {} T
08A6: 2d cb          JSR  $0E5A                                        ; {} SPACE
08A8: 9c ca          JSR  $0D38                                        ; {} E
08AA: f4 ca          JSR  $0DE8                                        ; {} R
08AC: f4 ca          JSR  $0DE8                                        ; {} R
08AE: de ca          JSR  $0DBC                                        ; {} O
08B0: f4 ca          JSR  $0DE8                                        ; {} R
08B2: 00 d0          RTS                                               

;;= Credits =

;;{{{html
;;<canvas width="500" height="60"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=20,y=45,baseScale=1,08B8">
;;</canvas>
;;}}}

; "ASTEROIDS BY ATARI"
08B4: 80 a0 7c 01    CUR  scale=00(/512)  y=128  x=380                 
08B8: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
08BC: 79 ca          JSR  $0CF2                                        ; {} A
08BE: fc ca          JSR  $0DF8                                        ; {} S
08C0: 03 cb          JSR  $0E06                                        ; {} T
08C2: 9c ca          JSR  $0D38                                        ; {} E
08C4: f4 ca          JSR  $0DE8                                        ; {} R
08C6: de ca          JSR  $0DBC                                        ; {} O
08C8: bb ca          JSR  $0D76                                        ; {} I
08CA: 94 ca          JSR  $0D28                                        ; {} D
08CC: fc ca          JSR  $0DF8                                        ; {} S
08CE: 2d cb          JSR  $0E5A                                        ; {} SPACE
08D0: 81 ca          JSR  $0D02                                        ; {} B
08D2: 20 cb          JSR  $0E40                                        ; {} Y
08D4: 2d cb          JSR  $0E5A                                        ; {} SPACE
08D6: 79 ca          JSR  $0CF2                                        ; {} A
08D8: 03 cb          JSR  $0E06                                        ; {} T
08DA: 79 ca          JSR  $0CF2                                        ; {} A
08DC: f4 ca          JSR  $0DE8                                        ; {} R
08DE: bb ca          JSR  $0D76                                        ; {} I
08E0: 00 d0          RTS                                               

; Ship Explosion
08E2: c6 ff          SVEC scale=01(/256)  bri=12  x=-2      y=-3     (-0.01, -0.01)
08E4: c1 fe          SVEC scale=01(/256)  bri=12  x=1       y=-2     (0.00, -0.01)
08E6: c3 f1          SVEC scale=00(/512)  bri=12  x=3       y=1      (0.01, 0.00)
08E8: cd f1          SVEC scale=02(/128)  bri=12  x=-1      y=1      (-0.01, 0.01)
08EA: c7 f1          SVEC scale=00(/512)  bri=12  x=-3      y=1      (-0.01, 0.00)
08EC: c1 fd          SVEC scale=01(/256)  bri=12  x=1       y=-1     (0.00, -0.00)
08EE: d8 1e 32 ec    VEC  scale=01(/256)  bri=14  x=-50     y=-728   (-0.20, -2.84)
08F2: 00 c4          JSR  $0000                                        ; Do routine at start of vector RAM
08F4: 3c 14 0a 46    VEC  scale=01(/256)  bri=04  x=-522    y=-60    (-2.04, -0.23)
08F8: d8 d8          RTS                                               ; ?? 0x8d8


;;= Shrapnel Patterns =

;; This is used when the player's shot hits something.
;;
;; Notice that all four patterns are the same just slightly spread out. This is extremely
;; clever. You could use one pattern and vary the scale to make it look like it is
;; spreading out. But the scale jumps are powers-of-two. These slightly-scaled patterns
;; can be used to take up the gaps in the large scaling doubles!

;;{{{html
;;<canvas width="420" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=0,x=50,y=50,09A2,x=150,y=50,096C,x=250,y=50,092E,x=350,y=50,0902">
;;</canvas>
;;}}}

; Jump table for 4
08FA: d1 c8          JSR  $09A2                                        ; {}
08FC: b6 c8          JSR  $096C                                        ; {}
08FE: 97 c8          JSR  $092E                                        ; {}
0900: 81 c8          JSR  $0902                                        ; {}
;
; Shrapnel pattern 1
0902: 0d f8          SVEC scale=03(/64)   bri=00  x=-1      y=0      (-0.02, 0.00)
0904: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0906: 0d fd          SVEC scale=03(/64)   bri=00  x=-1      y=-1     (-0.02, -0.02)
0908: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
090A: 09 fd          SVEC scale=03(/64)   bri=00  x=1       y=-1     (0.02, -0.02)
090C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
090E: 0B f1          SVEC scale=02(/128)  bri=00  x=3       y=1      (0.02, 0.01)
0910: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0912: 0a f5          SVEC scale=02(/128)  bri=00  x=2       y=-1     (0.02, -0.01)
0914: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0916: 08 f9          SVEC scale=03(/64)   bri=00  x=0       y=1      (0.00, 0.02)
0918: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
091A: 09 f3          SVEC scale=02(/128)  bri=00  x=1       y=3      (0.01, 0.02)
091C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
091E: 0d f3          SVEC scale=02(/128)  bri=00  x=-1      y=3      (-0.01, 0.02)
0920: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0922: 80 54 00 06    VEC  scale=05(/16)   bri=00  x=-512    y=-128   (-32.00, -8.00)
0926: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0928: 0f f1          SVEC scale=02(/128)  bri=00  x=-3      y=1      (-0.02, 0.01)
092A: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
092C: 00 d0          RTS                                               
;
; Shrapnel pattern 2
092E: 00 30 80 07    VEC  scale=03(/64)   bri=00  x=-896    y=0      (-14.00, 0.00)
0932: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0934: 80 37 80 07    VEC  scale=03(/64)   bri=00  x=-896    y=-896   (-14.00, -14.00)
0938: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
093A: 80 37 80 03    VEC  scale=03(/64)   bri=00  x=896     y=-896   (14.00, -14.00)
093E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0940: e0 40 a0 02    VEC  scale=04(/32)   bri=00  x=672     y=224    (21.00, 7.00)
0944: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0946: c0 35 80 03    VEC  scale=03(/64)   bri=00  x=896     y=-448   (14.00, -7.00)
094A: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
094C: 80 33 00 00    VEC  scale=03(/64)   bri=00  x=0       y=896    (0.00, 14.00)
0950: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0952: a0 42 e0 00    VEC  scale=04(/32)   bri=00  x=224     y=672    (7.00, 21.00)
0956: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0958: a0 42 e0 04    VEC  scale=04(/32)   br 
095C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
095E: e0 44 80 07    VEC  scale=04(/32)   bri=00  x=-896    y=-224   (-28.00, -7.00)
0962: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0964: e0 40 a0 06    VEC  scale=04(/32)   bri=00  x=-672    y=224    (-21.00, 7.00)
0968: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
096A: 00 d0          RTS                                               
;
; Shrapnel pattern 3
096C: 07 f8          SVEC scale=01(/256)  bri=00  x=-3      y=0      (-0.01, 0.00)
096E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0970: 07 ff          SVEC scale=01(/256)  bri=00  x=-3      y=-3     (-0.01, -0.01)
0972: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0974: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
0976: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0978: c0 40 40 02    VEC  scale=04(/32)   bri=00  x=576     y=192    (18.00, 6.00)
097C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
097E: 80 35 00 03    VEC  scale=03(/64)   bri=00  x=768     y=-384   (12.00, -6.00)
0982: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0984: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0986: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0988: 40 42 c0 00    VEC  scale=04(/32)   bri=00  x=192     y=576    (6.00, 18.00)
098C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
098E: 40 42 c0 04    VEC  scale=04(/32)   bri=00  x=-192    y=576    (-6.00, 18.00)
0992: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
0994: c0 44 00 07    VEC  scale=04(/32)   bri=00  x=-768    y=-192   (-24.00, -6.00)
0998: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
099A: c0 40 40 06    VEC  scale=04(/32)   bri=00  x=-576    y=192    (-18.00, 6.00)
099E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09A0: 00 d0          RTS                                               
;
; Shrapnel pattern 4
09A2: 00 30 80 06    VEC  scale=03(/64)   bri=00  x=-640    y=0      (-10.00, 0.00)
09A6: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09A8: 80 36 80 06    VEC  scale=03(/64)   bri=00  x=-640    y=-640   (-10.00, -10.00)
09AC: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09AE: 80 36 80 02    VEC  scale=03(/64)   bri=00  x=640     y=-640   (10.00, -10.00)
09B2: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09B4: 40 31 c0 03    VEC  scale=03(/64)   bri=00  x=960     y=320    (15.00, 5.00)
09B8: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09BA: 40 35 80 02    VEC  scale=03(/64)   bri=00  x=640     y=-320   (10.00, -5.00)
09BE: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09C0: 80 32 00 00    VEC  scale=03(/64)   bri=00  x=0       y=640    (0.00, 10.00)
09C4: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09C6: c0 33 40 01    VEC  scale=03(/64)   bri=00  x=320     y=960    (5.00, 15.00)
09CA: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09CC: c0 33 40 05    VEC  scale=03(/64)   bri=00  x=-320    y=960    (-5.00, 15.00)
09D0: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09D2: a0 44 80 06    VEC  scale=04(/32)   bri=00  x=-640    y=-160   (-20.00, -5.00)
09D6: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09D8: 40 31 c0 07    VEC  scale=03(/64)   bri=00  x=-960    y=320    (-15.00, 5.00)
09DC: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
09DE: 00 d0          RTS                                               

;;= Rock Patterns =

;;{{{html
;;<canvas width="400" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=0,x=50,y=50,09E8,x=150,y=50,0A00,x=250,y=50,0A1C,x=350,y=50,0A36">
;;</canvas>
;;}}}

; Jump table for 4
09E0: f4 c8          JSR  $09E8                                        ; {}
09E2: 00 c9          JSR  $0A00                                        ; {}
09E4: 0e c9          JSR  $0A1C                                        ; {}
09E6: 1b c9          JSR  $0A36                                        ; {}
;
; Rock Pattern 1
09E8: 08 f9          SVEC scale=03(/64)   bri=00  x=0       y=1      (0.00, 0.02)
09EA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
09EC: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
09EE: 7d f6          SVEC scale=02(/128)  bri=07  x=-1      y=-2     (-0.01, -0.02)
09F0: 79 f6          SVEC scale=02(/128)  bri=07  x=1       y=-2     (0.01, -0.02)
09F2: 8f f6          SVEC scale=02(/128)  bri=08  x=-3      y=-2     (-0.02, -0.02)
09F4: 8f f0          SVEC scale=02(/128)  bri=08  x=-3      y=0      (-0.02, 0.00)
09F6: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
09F8: 78 fa          SVEC scale=03(/64)   bri=07  x=0       y=2      (0.00, 0.03)
09FA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
09FC: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
09FE: 00 d0          RTS                                               
;
; Rock Pattern 2
0A00: 0a f1          SVEC scale=02(/128)  bri=00  x=2       y=1      (0.02, 0.01)
0A02: 7a f1          SVEC scale=02(/128)  bri=07  x=2       y=1      (0.02, 0.01)
0A04: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
0A06: 7e f5          SVEC scale=02(/128)  bri=07  x=-2      y=-1     (-0.02, -0.01)
0A08: 7e f1          SVEC scale=02(/128)  bri=07  x=-2      y=1      (-0.02, 0.01)
0A0A: 7d fd          SVEC scale=03(/64)   bri=07  x=-1      y=-1     (-0.02, -0.02)
0A0C: 79 f6          SVEC scale=02(/128)  bri=07  x=1       y=-2     (0.01, -0.02)
0A0E: 7d f6          SVEC scale=02(/128)  bri=07  x=-1      y=-2     (-0.01, -0.02)
0A10: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
0A12: 79 f1          SVEC scale=02(/128)  bri=07  x=1       y=1      (0.01, 0.01)
0A14: 8b f5          SVEC scale=02(/128)  bri=08  x=3       y=-1     (0.02, -0.01)
0A16: 8a f3          SVEC scale=02(/128)  bri=08  x=2       y=3      (0.02, 0.02)
0A18: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
0A1A: 00 d0          RTS                                               
;
; Rock Pattern 3
0A1C: 0d f8          SVEC scale=03(/64)   bri=00  x=-1      y=0      (-0.02, 0.00)
0A1E: 7e f5          SVEC scale=02(/128)  bri=07  x=-2      y=-1     (-0.02, -0.01)
0A20: 7a f7          SVEC scale=02(/128)  bri=07  x=2       y=-3     (0.02, -0.02)
0A22: 7a f3          SVEC scale=02(/128)  bri=07  x=2       y=3      (0.02, 0.02)
0A24: 78 f7          SVEC scale=02(/128)  bri=07  x=0       y=-3     (0.00, -0.02)
0A26: 79 f8          SVEC scale=03(/64)   bri=07  x=1       y=0      (0.02, 0.00)
0A28: 7a f3          SVEC scale=02(/128)  bri=07  x=2       y=3      (0.02, 0.02)
0A2A: 78 f9          SVEC scale=03(/64)   bri=07  x=0       y=1      (0.00, 0.02)
0A2C: 7e f3          SVEC scale=02(/128)  bri=07  x=-2      y=3      (-0.02, 0.02)
0A2E: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
0A30: 7f f7          SVEC scale=02(/128)  bri=07  x=-3      y=-3     (-0.02, -0.02)
0A32: 7a f5          SVEC scale=02(/128)  bri=07  x=2       y=-1     (0.02, -0.01)
0A34: 00 d0          RTS                                               
;
; Rock Pattern 4
0A36: 09 f0          SVEC scale=02(/128)  bri=00  x=1       y=0      (0.01, 0.00)
0A38: 7b f1          SVEC scale=02(/128)  bri=07  x=3       y=1      (0.02, 0.01)
0A3A: 68 f1          SVEC scale=02(/128)  bri=06  x=0       y=1      (0.00, 0.01)
0A3C: 7f f2          SVEC scale=02(/128)  bri=07  x=-3      y=2      (-0.02, 0.02)
0A3E: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
0A40: 69 f6          SVEC scale=02(/128)  bri=06  x=1       y=-2     (0.01, -0.02)
0A42: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
0A44: 78 f7          SVEC scale=02(/128)  bri=07  x=0       y=-3     (0.00, -0.02)
0A46: 7a f7          SVEC scale=02(/128)  bri=07  x=2       y=-3     (0.02, -0.02)
0A48: 7b f1          SVEC scale=02(/128)  bri=07  x=3       y=1      (0.02, 0.01)
0A4A: 69 f5          SVEC scale=02(/128)  bri=06  x=1       y=-1     (0.01, -0.01)
0A4C: 69 f9          SVEC scale=03(/64)   bri=06  x=1       y=1      (0.02, 0.02)
0A4E: 7f f2          SVEC scale=02(/128)  bri=07  x=-3      y=2      (-0.02, 0.02)
0A50: 00 d0          RTS                                               

;;= UFO =
;;{{{html
;;<canvas width="100" height="75"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=50,y=40,baseScale=0,0A54">
;;</canvas>
;;}}}

; Jump table for 1
0A52: 2a c9          JSR  $0A54       
;                                  
0A54: 0e f1          SVEC scale=02(/128)  bri=00  x=-2      y=1      (-0.02, 0.01)
0A56: ca f8          SVEC scale=03(/64)   bri=12  x=2       y=0      (0.03, 0.00)
0A58: 0B f6          SVEC scale=02(/128)  bri=00  x=3       y=-2     (0.02, -0.02)
0A5A: 00 60 80 d6    VEC  scale=06(/8)    bri=13  x=-640    y=0      (-80.00, 0.00)
0A5E: db f6          SVEC scale=02(/128)  bri=13  x=3       y=-2     (0.02, -0.02)
0A60: ca f8          SVEC scale=03(/64)   bri=12  x=2       y=0      (0.03, 0.00)
0A62: db f2          SVEC scale=02(/128)  bri=13  x=3       y=2      (0.02, 0.02)
0A64: df f2          SVEC scale=02(/128)  bri=13  x=-3      y=2      (-0.02, 0.02)
0A66: cd f2          SVEC scale=02(/128)  bri=12  x=-1      y=2      (-0.01, 0.02)
0A68: cd f8          SVEC scale=03(/64)   bri=12  x=-1      y=0      (-0.02, 0.00)
0A6A: cd f6          SVEC scale=02(/128)  bri=12  x=-1      y=-2     (-0.01, -0.02)
0A6C: df f6          SVEC scale=02(/128)  bri=13  x=-3      y=-2     (-0.02, -0.02)
0A6E: 00 d0          RTS                                               

;;= Player Ships =

; Table for ships and thrusts based on player's direction.
; The addresses are where the ROM appears in the main CPU's
; memory map (begins at 5000). Thus 5292 - 5000 + 0800 = 0A92.
; The thrust pattern for each ship follows the ship itself.
;
0A70: 92 52  ;{{#ShipDir0:ShipDir0:0}}
0A72: aa 52  ;{{#ShipDir4:ShipDir4:0}}
0A74: ce 52  ;{{#ShipDir8:ShipDir8:0}} 
0A76: f2 52  ;{{#ShipDir12:ShipDir12:0}}
0A78: 16 53  ;{{#ShipDir16:ShipDir16:0}}
0A7A: 38 53  ;{{#ShipDir20:ShipDir20:0}}
0A7C: 5c 53  ;{{#ShipDir24:ShipDir24:0}}
0A7E: 80 53  ;{{#ShipDir28:ShipDir28:0}}
0A80: a4 53  ;{{#ShipDir32:ShipDir32:0}}
0A82: c8 53  ;{{#ShipDir36:ShipDir36:0}}
0A84: ec 53  ;{{#ShipDir40:ShipDir40:0}}
0A86: 10 54  ;{{#ShipDir44:ShipDir44:0}}
0A88: 34 54  ;{{#ShipDir48:ShipDir48:0}}
0A8A: 58 54  ;{{#ShipDir52:ShipDir52:0}}
0A8C: 7c 54  ;{{#ShipDir56:ShipDir56:0}}
0A8E: a0 54  ;{{#ShipDir60:ShipDir60:0}}
0A90: c4 54  ;{{#ShipDir64:ShipDir64:0}}

;;{{{html
;;<canvas width="1060" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=-1,
;;    x=50,y=50,A92,AA4,    
;;    x=110,y=50,0AAA,
;;    x=170,y=50,0ACE,
;;    x=230,y=50,0AF2,
;;    x=290,y=50,0B16,
;;    x=350,y=50,0B38,
;;    x=410,y=50,0B5C,
;;    x=470,y=50,0B80,
;;    x=530,y=50,0BA4,
;;    x=590,y=50,0BC8,
;;    x=650,y=50,0BEC,
;;    x=710,y=50,0C10,
;;    x=770,y=50,0C34,
;;    x=830,y=50,0C58,
;;    x=890,y=50,0C7C,
;;    x=950,y=50,0CA0,
;;    x=1010,y=50,0CC4,0CD6
;;  ">
;;</canvas>
;;}}}

ShipDir0:
0A92: 0f f6          SVEC scale=02(/128)  bri=00  x=-3      y=-2     (-0.02, -0.02)
0A94: c8 fa          SVEC scale=03(/64)   bri=12  x=0       y=2      (0.00, 0.03)
0A96: bd f9          SVEC scale=03(/64)   bri=11  x=-1      y=1      (-0.02, 0.02)
0A98: 00 65 00 c3    VEC  scale=06(/8)    bri=12  x=768     y=-256   (96.00, -32.00)
0A9C: 00 65 00 c7    VEC  scale=06(/8)    bri=12  x=-768    y=-256   (-96.00, -32.00)
0AA0: b9 f9          SVEC scale=03(/64)   bri=11  x=1       y=1      (0.02, 0.02)
0AA2: 00 d0          RTS                                               
ThrustDir0:
0AA4: ce f9          SVEC scale=03(/64)   bri=12  x=-2      y=1      (-0.03, 0.02)
0AA6: ca f9          SVEC scale=03(/64)   bri=12  x=2       y=1      (0.03, 0.02)
0AA8: 00 d0          RTS                                               

ShipDir4:
0AAA: 40 46 c0 06    VEC  scale=04(/32)   bri=00  x=-704    y=-576   (-22.00, -18.00)
0AAE: 00 52 30 c4    VEC  scale=05(/16)   bri=12  x=-48     y=512    (-3.00, 32.00)
0AB2: c0 41 20 c6    VEC  scale=04(/32)   bri=12  x=-544    y=448    (-17.00, 14.00)
0AB6: b0 64 18 c3    VEC  scale=06(/8)    bri=12  x=792     y=-176   (99.00, -22.00)
0ABA: 48 65 e0 c6    VEC  scale=06(/8)    bri=12  x=-736    y=-328   (-92.00, -41.00)
0ABE: 20 42 c0 c1    VEC  scale=04(/32)   bri=12  x=448     y=544    (14.00, 17.00)
0AC2: 00 d0          RTS                                               
ThrustDir4:
0AC4: d0 50 10 c6    VEC  scale=05(/16)   bri=12  x=-528    y=208    (-33.00, 13.00)
0AC8: 60 42 c0 c3    VEC  scale=04(/32)   bri=12  x=960     y=608    (30.00, 19.00)
0ACC: 00 d0          RTS                                               

ShipDir8:
0ACE: 80 46 80 06    VEC  scale=04(/32)   bri=00  x=-640    y=-640   (-20.00, -20.00)
0AD2: e0 43 c0 c4    VEC  scale=04(/32)   bri=12  x=-192    y=992    (-6.00, 31.00)
0AD6: a0 41 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=416    (-19.00, 13.00)
0ADA: 68 64 20 c3    VEC  scale=06(/8)    bri=12  x=800     y=-104   (100.00, -13.00)
0ADE: 90 65 c0 c6    VEC  scale=06(/8)    bri=12  x=-704    y=-400   (-88.00, -50.00)
0AE2: 60 42 a0 c1    VEC  scale=04(/32)   bri=12  x=416     y=608    (13.00, 19.00)
0AE6: 00 d0          RTS                                               
ThrustDir8:
0AE8: 90 50 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=144    (-35.00, 9.00)
0AEC: c0 42 80 c3    VEC  scale=04(/32)   bri=12  x=896     y=704    (28.00, 22.00)
0AF0: 00 d0          RTS                                               

ShipDir12:
0AF2: c0 46 40 06    VEC  scale=04(/32)   bri=00  x=-576    y=-704   (-18.00, -22.00)
0AF6: e0 43 20 c5    VEC  scale=04(/32)   bri=12  x=-288    y=992    (-9.00, 31.00)
0AFA: 60 41 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=352    (-20.00, 11.00)
0AFE: 18 64 28 c3    VEC  scale=06(/8)    bri=12  x=808     y=-24    (101.00, -3.00)
0B02: d0 65 98 c6    VEC  scale=06(/8)    bri=12  x=-664    y=-464   (-83.00, -58.00)
0B06: 80 42 60 c1    VEC  scale=04(/32)   bri=12  x=352     y=640    (11.00, 20.00)
0B0A: 00 d0          RTS                                               
ThrustDir12:
0B0C: 60 50 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=96     (-35.00, 6.00)
0B10: 20 43 40 c3    VEC  scale=04(/32)   bri=12  x=832     y=800    (26.00, 25.00)
0B14: 00 d0          RTS                                               

ShipDir16:
0B16: 0e f7          SVEC scale=02(/128)  bri=00  x=-2      y=-3     (-0.02, -0.02)
0B18: c0 43 80 c5    VEC  scale=04(/32)   bri=12  x=-384    y=960    (-12.00, 30.00)
0B1C: 20 41 a0 c6    VEC  scale=04(/32)   bri=12  x=-672    y=288    (-21.00, 9.00)
0B20: 38 60 28 c3    VEC  scale=06(/8)    bri=12  x=808     y=56     (101.00, 7.00)
0B24: 10 66 60 c6    VEC  scale=06(/8)    bri=12  x=-608    y=-528   (-76.00, -66.00)
0B28: a0 42 20 c1    VEC  scale=04(/32)   bri=12  x=288     y=672    (9.00, 21.00)
0B2C: 00 d0          RTS                                               
ThrustDir16:
0B2E: 30 50 40 c6    VEC  scale=05(/16)   bri=12  x=-576    y=48     (-36.00, 3.00)
0B32: 60 43 e0 c2    VEC  scale=04(/32)   bri=12  x=736     y=864    (23.00, 27.00)
0B36: 00 d0          RTS                                               

ShipDir20:
0B38: 20 47 c0 05    VEC  scale=04(/32)   bri=00  x=-448    y=-800   (-14.00, -25.00)
0B3C: 80 43 e0 c5    VEC  scale=04(/32)   bri=12  x=-480    y=896    (-15.00, 28.00)
0B40: e0 40 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=224    (-22.00, 7.00)
0B44: 88 60 20 c3    VEC  scale=06(/8)    bri=12  x=800     y=136    (100.00, 17.00)
0B48: 48 66 30 c6    VEC  scale=06(/8)    bri=12  x=-560    y=-584   (-70.00, -73.00)
0B4C: c0 42 e0 c0    VEC  scale=04(/32)   bri=12  x=224     y=704    (7.00, 22.00)
0B50: 00 d0          RTS                                               
ThrustDir20:
0B52: 10 54 40 c6    VEC  scale=05(/16)   bri=12  x=-576    y=-16    (-36.00, -1.00)
0B56: a0 43 a0 c2    VEC  scale=04(/32)   bri=12  x=672     y=928    (21.00, 29.00)
0B5A: 00 d0          RTS                                               

ShipDir24:
0B5C: 60 47 60 05    VEC  scale=04(/32)   bri=00  x=-352    y=-864   (-11.00, -27.00)
0B60: 60 43 40 c6    VEC  scale=04(/32)   bri=12  x=-576    y=864    (-18.00, 27.00)
0B64: 80 40 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=128    (-22.00, 4.00)
0B68: d8 60 10 c3    VEC  scale=06(/8)    bri=12  x=784     y=216    (98.00, 27.00)
0B6C: 80 66 f0 c5    VEC  scale=06(/8)    bri=12  x=-496    y=-640   (-62.00, -80.00)
0B70: c0 42 80 c0    VEC  scale=04(/32)   bri=12  x=128     y=704    (4.00, 22.00)
0B74: 00 d0          RTS                                               
ThrustDir24:
0B76: 40 54 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=-64    (-35.00, -4.00)
0B7A: e0 43 40 c2    VEC  scale=04(/32)   bri=12  x=576     y=992    (18.00, 31.00)
0B7E: 00 d0          RTS                                               

ShipDir28:
0B80: 80 47 00 05    VEC  scale=04(/32)   bri=00  x=-256    y=-896   (-8.00, -28.00)
0B84: 20 43 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=800    (-20.00, 25.00)
0B88: 40 40 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=64     (-23.00, 2.00)
0B8C: 20 61 f8 c2    VEC  scale=06(/8)    bri=12  x=760     y=288    (95.00, 36.00)
0B90: b0 66 b0 c5    VEC  scale=06(/8)    bri=12  x=-432    y=-688   (-54.00, -86.00)
0B94: e0 42 40 c0    VEC  scale=04(/32)   bri=12  x=64      y=736    (2.00, 23.00)
0B98: 00 d0          RTS                                               
ThrustDir28:
0B9A: 80 54 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=-128   (-35.00, -8.00)
0B9E: 10 52 f0 c0    VEC  scale=05(/16)   bri=12  x=240     y=528    (15.00, 33.00)
0BA2: 00 d0          RTS                                               

ShipDir32:
0BA4: 80 47 c0 04    VEC  scale=04(/32)   bri=00  x=-192    y=-896   (-6.00, -28.00)
0BA8: e0 42 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=736    (-23.00, 23.00)
0BAC: 00 40 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=0      (-23.00, 0.00)
0BB0: 68 61 d8 c2    VEC  scale=06(/8)    bri=12  x=728     y=360    (91.00, 45.00)
0BB4: d8 66 68 c5    VEC  scale=06(/8)    bri=12  x=-360    y=-728   (-45.00, -91.00)
0BB8: e0 42 00 c0    VEC  scale=04(/32)   bri=12  x=0       y=736    (0.00, 23.00)
0BBC: 00 d0          RTS                                               
ThrustDir32:
0BBE: b0 54 20 c6    VEC  scale=05(/16)   bri=12  x=-544    y=-176   (-34.00, -11.00)
0BC2: 20 52 b0 c0    VEC  scale=05(/16)   bri=12  x=176     y=544    (11.00, 34.00)
0BC6: 00 d0          RTS                                               

ShipDir36:
0BC8: a0 47 60 04    VEC  scale=04(/32)   bri=00  x=-96     y=-928   (-3.00, -29.00)
0BCC: 80 42 20 c7    VEC  scale=04(/32)   bri=12  x=-800    y=640    (-25.00, 20.00)
0BD0: 40 44 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=-64    (-23.00, -2.00)
0BD4: b0 61 b0 c2    VEC  scale=06(/8)    bri=12  x=688     y=432    (86.00, 54.00)
0BD8: f8 66 20 c5    VEC  scale=06(/8)    bri=12  x=-288    y=-760   (-36.00, -95.00)
0BDC: e0 42 40 c4    VEC  scale=04(/32)   bri=12  x=-64     y=736    (-2.00, 23.00)
0BE0: 00 d0          RTS                                               
ThrustDir36:
0BE2: f0 54 10 c6    VEC  scale=05(/16)   bri=12  x=-528    y=-240   (-33.00, -15.00)
0BE6: 30 52 80 c0    VEC  scale=05(/16)   bri=12  x=128     y=560    (8.00, 35.00)
0BEA: 00 d0          RTS                                               

ShipDir40:
0BEC: a0 47 00 00    VEC  scale=04(/32)   bri=00  x=0       y=-928   (0.00, -29.00)
0BF0: 40 42 60 c7    VEC  scale=04(/32)   bri=12  x=-864    y=576    (-27.00, 18.00)
0BF4: 80 44 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-128   (-22.00, -4.00)
0BF8: f0 61 80 c2    VEC  scale=06(/8)    bri=12  x=640     y=496    (80.00, 62.00)
0BFC: 10 67 d8 c4    VEC  scale=06(/8)    bri=12  x=-216    y=-784   (-27.00, -98.00)
0C00: c0 42 80 c4    VEC  scale=04(/32)   bri=12  x=-128    y=704    (-4.00, 22.00)
0C04: 00 d0          RTS                                               
ThrustDir40:
0C06: 40 46 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=-576   (-31.00, -18.00)
0C0A: 30 52 40 c0    VEC  scale=05(/16)   bri=12  x=64      y=560    (4.00, 35.00)
0C0E: 00 d0          RTS                                               

ShipDir44:
0C10: a0 47 60 00    VEC  scale=04(/32)   bri=00  x=96      y=-928   (3.00, -29.00)
0C14: e0 41 80 c7    VEC  scale=04(/32)   bri=12  x=-896    y=480    (-28.00, 15.00)
0C18: e0 44 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-224   (-22.00, -7.00)
0C1C: 30 62 48 c2    VEC  scale=06(/8)    bri=12  x=584     y=560    (73.00, 70.00)
0C20: 20 67 88 c4    VEC  scale=06(/8)    bri=12  x=-136    y=-800   (-17.00, -100.00)
0C24: c0 42 e0 c4    VEC  scale=04(/32)   bri=12  x=-224    y=704    (-7.00, 22.00)
0C28: 00 d0          RTS                                               
ThrustDir44:
0C2A: a0 46 a0 c7    VEC  scale=04(/32)   bri=12  x=-928    y=-672   (-29.00, -21.00)
0C2E: 40 52 10 c0    VEC  scale=05(/16)   bri=12  x=16      y=576    (1.00, 36.00)
0C32: 00 d0          RTS                                               

ShipDir48:
0C34: 80 47 c0 00    VEC  scale=04(/32)   bri=00  x=192     y=-896   (6.00, -28.00)
0C38: 80 41 c0 c7    VEC  scale=04(/32)   bri=12  x=-960    y=384    (-30.00, 12.00)
0C3C: 20 45 a0 c6    VEC  scale=04(/32)   bri=12  x=-672    y=-288   (-21.00, -9.00)
0C40: 60 62 10 c2    VEC  scale=06(/8)    bri=12  x=528     y=608    (66.00, 76.00)
0C44: 28 67 38 c4    VEC  scale=06(/8)    bri=12  x=-56     y=-808   (-7.00, -101.00)
0C48: a0 42 20 c5    VEC  scale=04(/32)   bri=12  x=-288    y=672    (-9.00, 21.00)
0C4C: 00 d0          RTS                                               
ThrustDir48:
0C4E: e0 46 60 c7    VEC  scale=04(/32)   bri=12  x=-864    y=-736   (-27.00, -23.00)
0C52: 40 52 30 c4    VEC  scale=05(/16)   bri=12  x=-48     y=576    (-3.00, 36.00)
0C56: 00 d0          RTS                                               

ShipDir52:
0C58: 80 47 00 01    VEC  scale=04(/32)   bri=00  x=256     y=-896   (8.00, -28.00)
0C5C: 20 41 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=288    (-31.00, 9.00)
0C60: 60 45 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=-352   (-20.00, -11.00)
0C64: 98 62 d0 c1    VEC  scale=06(/8)    bri=12  x=464     y=664    (58.00, 83.00)
0C68: 28 67 18 c0    VEC  scale=06(/8)    bri=12  x=24      y=-808   (3.00, -101.00)
0C6C: 80 42 60 c5    VEC  scale=04(/32)   bri=12  x=-352    y=640    (-11.00, 20.00)
0C70: 00 d0          RTS                                               
ThrustDir52:
0C72: 40 47 20 c7    VEC  scale=04(/32)   bri=12  x=-800    y=-832   (-25.00, -26.00)
0C76: 30 52 60 c4    VEC  scale=05(/16)   bri=12  x=-96     y=560    (-6.00, 35.00)
0C7A: 00 d0          RTS                                               

ShipDir56:
0C7C: 60 47 60 01    VEC  scale=04(/32)   bri=00  x=352     y=-864   (11.00, -27.00)
0C80: c0 40 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=192    (-31.00, 6.00)
0C84: a0 45 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=-416   (-19.00, -13.00)
0C88: c0 62 90 c1    VEC  scale=06(/8)    bri=12  x=400     y=704    (50.00, 88.00)
0C8C: 20 67 68 c0    VEC  scale=06(/8)    bri=12  x=104     y=-800   (13.00, -100.00)
0C90: 60 42 a0 c5    VEC  scale=04(/32)   bri=12  x=-416    y=608    (-13.00, 19.00)
0C94: 00 d0          RTS                                               
ThrustDir56:
0C96: 80 47 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-896   (-22.00, -28.00)
0C9A: 30 52 90 c4    VEC  scale=05(/16)   bri=12  x=-144    y=560    (-9.00, 35.00)
0C9E: 00 d0          RTS                                               

ShipDir60:
0CA0: 20 47 c0 01    VEC  scale=04(/32)   bri=00  x=448     y=-800   (14.00, -25.00)
0CA4: 30 50 00 c6    VEC  scale=05(/16)   bri=12  x=-512    y=48     (-32.00, 3.00)
0CA8: c0 45 20 c6    VEC  scale=04(/32)   bri=12  x=-544    y=-448   (-17.00, -14.00)
0CAC: e0 62 48 c1    VEC  scale=06(/8)    bri=12  x=328     y=736    (41.00, 92.00)
0CB0: 18 67 b0 c0    VEC  scale=06(/8)    bri=12  x=176     y=-792   (22.00, -99.00)
0CB4: 20 42 c0 c5    VEC  scale=04(/32)   bri=12  x=-448    y=544    (-14.00, 17.00)
0CB8: 00 d0          RTS                                               
ThrustDir60:
0CBA: c0 47 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=-960   (-19.00, -30.00)
0CBE: 10 52 d0 c4    VEC  scale=05(/16)   bri=12  x=-208    y=528    (-13.00, 33.00)
0CC2: 00 d0          RTS                                               

ShipDir64:
0CC4: 0a f7          SVEC scale=02(/128)  bri=00  x=2       y=-3     (0.02, -0.02)
0CC6: ce f8          SVEC scale=03(/64)   bri=12  x=-2      y=0      (-0.03, 0.00)
0CC8: cd fd          SVEC scale=03(/64)   bri=12  x=-1      y=-1     (-0.02, -0.02)
0CCA: 00 63 00 c1    VEC  scale=06(/8)    bri=12  x=256     y=768    (32.00, 96.00)
0CCE: 00 67 00 c1    VEC  scale=06(/8)    bri=12  x=256     y=-768   (32.00, -96.00)
0CD2: cd f9          SVEC scale=03(/64)   bri=12  x=-1      y=1      (-0.02, 0.02)
0CD4: 00 d0          RTS                                               
ThrustDir64:
0CD6: cd fe          SVEC scale=03(/64)   bri=12  x=-1      y=-2     (-0.02, -0.03)
0CD8: cd fa          SVEC scale=03(/64)   bri=12  x=-1      y=2      (-0.02, 0.03)
0CDA: 00 d0          RTS                                               

;;= Lives =

;; Ships in reserve. These are defined so you can draw them one right after the other (three drawn here).

;;{{{html
;;<canvas width="200" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=50,y=50,baseScale=-1,0CDC,0CDC,0CDC">
;;</canvas>
;;}}}

0CDC: 0e f7          SVEC scale=02(/128)  bri=00  x=-2      y=-3     (-0.02, -0.02)
0CDE: 7a f8          SVEC scale=03(/64)   bri=07  x=2       y=0      (0.03, 0.00)
0CE0: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
0CE2: 00 63 00 75    VEC  scale=06(/8)    bri=07  x=-256    y=768    (-32.00, 96.00)
0CE6: 00 67 00 75    VEC  scale=06(/8)    bri=07  x=-256    y=-768   (-32.00, -96.00)
0CEA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
0CEC: c0 60 80 02    VEC  scale=06(/8)    bri=00  x=640     y=192    (80.00, 24.00)
0CF0: 32 d0          RTS                                             ; ?? 0x32

;;= Characters =

;;{{{html
;;<canvas width="500" height="120"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=30,y=45,baseScale=1,0CF2,0D02,0D1C,0D28,0D38,0D48,0D56,0D68,0D76,0D84,0D90,0D9C,0DA6,0DB2,0DBC,0DC8,0DD6,0DE8,x=30,y=90,0DF8,0E06,0E12,0E1E,0E28,0E36,0E40,0E4E,0E5A,0E5E,0E66,0E76,0E84,0E92,0EA0,0EAE,0EB8,0EC8">
;;</canvas>
;;}}}

; "A"
0CF2: 70 fa          SVEC scale=01(/256)  bri=07  x=0       y=2      (0.00, 0.01)
0CF4: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
0CF6: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0CF8: 70 fe          SVEC scale=01(/256)  bri=07  x=0       y=-2     (0.00, -0.01)
0CFA: 06 f9          SVEC scale=01(/256)  bri=00  x=-2      y=1      (-0.01, 0.00)
0CFC: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0CFE: 02 f6          SVEC scale=00(/512)  bri=00  x=2       y=-2     (0.00, -0.00)
0D00: 00 d0          RTS                                               

; "B"
0D02: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D04: 73 f0          SVEC scale=00(/512)  bri=07  x=3       y=0      (0.01, 0.00)
0D06: 61 f5          SVEC scale=00(/512)  bri=06  x=1       y=-1     (0.00, -0.00)
0D08: 60 f5          SVEC scale=00(/512)  bri=06  x=0       y=-1     (0.00, -0.00)
0D0A: 65 f5          SVEC scale=00(/512)  bri=06  x=-1      y=-1     (-0.00, -0.00)
0D0C: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
0D0E: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
0D10: 61 f5          SVEC scale=00(/512)  bri=06  x=1       y=-1     (0.00, -0.00)
0D12: 60 f5          SVEC scale=00(/512)  bri=06  x=0       y=-1     (0.00, -0.00)
0D14: 65 f5          SVEC scale=00(/512)  bri=06  x=-1      y=-1     (-0.00, -0.00)
0D16: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
0D18: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0D1A: 00 d0          RTS                                               

; "C"
0D1C: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D1E: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D20: 06 ff          SVEC scale=01(/256)  bri=00  x=-2      y=-3     (-0.01, -0.01)
0D22: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D24: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0D26: 00 d0          RTS                                               

; "D"
0D28: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D2A: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
0D2C: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0D2E: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
0D30: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
0D32: 76 f0          SVEC scale=00(/512)  bri=07  x=-2      y=0      (-0.00, 0.00)
0D34: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0D36: 00 d0          RTS                                               

; "E"
0D38: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D3A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D3C: 05 f7          SVEC scale=00(/512)  bri=00  x=-1      y=-3     (-0.00, -0.01)
0D3E: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
0D40: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
0D42: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D44: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0D46: 00 d0          RTS                                               

; "F"
0D48: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D4A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D4C: 05 f7          SVEC scale=00(/512)  bri=00  x=-1      y=-3     (-0.00, -0.01)
0D4E: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
0D50: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
0D52: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0D54: 00 d0          RTS                                               

; "G"
0D56: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D58: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D5A: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
0D5C: 06 f6          SVEC scale=00(/512)  bri=00  x=-2      y=-2     (-0.00, -0.00)
0D5E: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
0D60: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
0D62: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0D64: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0D66: 00 d0          RTS                                               

; "H"
0D68: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D6A: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
0D6C: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D6E: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
0D70: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0D72: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0D74: 00 d0          RTS                                               

; "I"
0D76: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0D78: 06 f0          SVEC scale=00(/512)  bri=00  x=-2      y=0      (-0.00, 0.00)
0D7A: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D7C: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0D7E: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0D80: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
0D82: 00 d0          RTS                                               

; "J"
0D84: 00 f2          SVEC scale=00(/512)  bri=00  x=0       y=2      (0.00, 0.00)
0D86: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0D88: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
0D8A: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D8C: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0D8E: 00 d0          RTS                                               

; "K"
0D90: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0D92: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
0D94: 77 f7          SVEC scale=00(/512)  bri=07  x=-3      y=-3     (-0.01, -0.01)
0D96: 73 f7          SVEC scale=00(/512)  bri=07  x=3       y=-3     (0.01, -0.01)
0D98: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
0D9A: 00 d0          RTS                                               

; "L"
0D9C: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0D9E: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0DA0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DA2: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0DA4: 00 d0          RTS                                               

; "M"
0DA6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DA8: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0DAA: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
0DAC: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0DAE: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0DB0: 00 d0          RTS                                               

; "N"
0DB2: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DB4: 72 ff          SVEC scale=01(/256)  bri=07  x=2       y=-3     (0.01, -0.01)
0DB6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DB8: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0DBA: 00 d0          RTS                                               

; "O"
0DBC: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DBE: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DC0: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0DC2: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0DC4: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0DC6: 00 d0          RTS                                               

; "P"
0DC8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DCA: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DCC: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0DCE: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0DD0: 03 f7          SVEC scale=00(/512)  bri=00  x=3       y=-3     (0.01, -0.01)
0DD2: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
0DD4: 00 d0          RTS                                               

; "Q"
0DD6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DD8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DDA: 70 fe          SVEC scale=01(/256)  bri=07  x=0       y=-2     (0.00, -0.01)
0DDC: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
0DDE: 76 f0          SVEC scale=00(/512)  bri=07  x=-2      y=0      (-0.00, 0.00)
0DE0: 02 f2          SVEC scale=00(/512)  bri=00  x=2       y=2      (0.00, 0.00)
0DE2: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0DE4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0DE6: 00 d0          RTS                                               

; "R"
0DE8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0DEA: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DEC: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0DEE: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0DF0: 01 f0          SVEC scale=00(/512)  bri=00  x=1       y=0      (0.00, 0.00)
0DF2: 73 f7          SVEC scale=00(/512)  bri=07  x=3       y=-3     (0.01, -0.01)
0DF4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0DF6: 00 d0          RTS                                               

; "S"
0DF8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0DFA: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
0DFC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0DFE: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
0E00: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E02: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E04: 00 d0          RTS                                               

; "T"
0E06: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E08: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0E0A: 06 f0          SVEC scale=00(/512)  bri=00  x=-2      y=0      (-0.00, 0.00)
0E0C: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E0E: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E10: 00 d0          RTS                                               

; "U"
0E12: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E14: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0E16: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E18: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0E1A: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E1C: 00 d0          RTS                                               

; "V"
0E1E: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E20: 71 ff          SVEC scale=01(/256)  bri=07  x=1       y=-3     (0.00, -0.01)
0E22: 71 fb          SVEC scale=01(/256)  bri=07  x=1       y=3      (0.00, 0.01)
0E24: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E26: 00 d0          RTS                                               

; "W"
0E28: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E2A: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0E2C: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
0E2E: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
0E30: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0E32: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E34: 00 d0          RTS                                               

; "X"
0E36: 72 fb          SVEC scale=01(/256)  bri=07  x=2       y=3      (0.01, 0.01)
0E38: 06 f8          SVEC scale=01(/256)  bri=00  x=-2      y=0      (-0.01, 0.00)
0E3A: 72 ff          SVEC scale=01(/256)  bri=07  x=2       y=-3     (0.01, -0.01)
0E3C: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E3E: 00 d0          RTS                                               

; "Y"
0E40: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E42: 70 fa          SVEC scale=01(/256)  bri=07  x=0       y=2      (0.00, 0.01)
0E44: 76 f2          SVEC scale=00(/512)  bri=07  x=-2      y=2      (-0.00, 0.00)
0E46: 02 f8          SVEC scale=01(/256)  bri=00  x=2       y=0      (0.01, 0.00)
0E48: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
0E4A: 02 fe          SVEC scale=01(/256)  bri=00  x=2       y=-2     (0.01, -0.01)
0E4C: 00 d0          RTS                                               

; "Z"
0E4E: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E50: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E52: 76 ff          SVEC scale=01(/256)  bri=07  x=-2      y=-3     (-0.01, -0.01)
0E54: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E56: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E58: 00 d0          RTS                                               

; SPACE
0E5A: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
0E5C: 00 d0          RTS                                               

; "1"
0E5E: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E60: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0E62: 02 ff          SVEC scale=01(/256)  bri=00  x=2       y=-3     (0.01, -0.01)
0E64: 00 d0          RTS                                               

; "2"
0E66: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E68: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E6A: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0E6C: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0E6E: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0E70: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E72: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E74: 00 d0          RTS                                               

; "3"
0E76: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E78: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0E7A: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0E7C: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
0E7E: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E80: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
0E82: 00 d0          RTS                                               

; "4"
0E84: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0E86: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0E88: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E8A: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
0E8C: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0E8E: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0E90: 00 d0          RTS                                               

; "5"
0E92: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E94: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
0E96: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0E98: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
0E9A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0E9C: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
0E9E: 00 d0          RTS                                               

; "6"
0EA0: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
0EA2: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0EA4: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0EA6: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0EA8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0EAA: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
0EAC: 00 d0          RTS                                               

; "7"
0EAE: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
0EB0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0EB2: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0EB4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
0EB6: 00 d0          RTS                                               

; "8"
0EB8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0EBA: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0EBC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0EBE: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
0EC0: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
0EC2: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0EC4: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
0EC6: 00 d0          RTS                                               

; "9"
0EC8: 02 f8          SVEC scale=01(/256)  bri=00  x=2       y=0      (0.01, 0.00)
0ECA: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
0ECC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
0ECE: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
0ED0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
0ED2: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
0ED4: 00 d0          RTS                                               

; Cross reference table for character data
0ED6: 2d cb          JSR  $0E5A                                        ; {} SPACE 1
0ED8: de ca          JSR  $0DBC                                        ; {} O and 0 ... same pattern
0EDA: 2f cb          JSR  $0E5E                                        ; {} 1
0EDC: 33 cb          JSR  $0E66                                        ; {} 2
0EDE: 3b cb          JSR  $0E76                                        ; {} 3
0EE0: 42 cb          JSR  $0E84                                        ; {} 4
0EE2: 49 cb          JSR  $0E92                                        ; {} 5
0EE4: 50 cb          JSR  $0EA0                                        ; {} 6 
0EE6: 57 cb          JSR  $0EAE                                        ; {} 7 2
0EE8: 5c cb          JSR  $0EB8                                        ; {} 8 3
0EEA: 64 cb          JSR  $0EC8                                        ; {} 9 4
0EEC: 79 ca          JSR  $0CF2                                        ; {} A 5
0EEE: 81 ca          JSR  $0D02                                        ; {} B 6
0EF0: 8e ca          JSR  $0D1C                                        ; {} C 7
0EF2: 94 ca          JSR  $0D28                                        ; {} D 8
0EF4: 9c ca          JSR  $0D38                                        ; {} E 9
0EF6: a4 ca          JSR  $0D48                                        ; {} F 10
0EF8: ab ca          JSR  $0D56                                        ; {} G 11
0EFA: b4 ca          JSR  $0D68                                        ; {} H 12
0EFC: bb ca          JSR  $0D76                                        ; {} I 13
0EFE: c2 ca          JSR  $0D84                                        ; {} J 14
0F00: c8 ca          JSR  $0D90                                        ; {} K 15
0F02: ce ca          JSR  $0D9C                                        ; {} L 16
0F04: d3 ca          JSR  $0DA6                                        ; {} M 17
0F06: d9 ca          JSR  $0DB2                                        ; {} N 18
0F08: de ca          JSR  $0DBC                                        ; {} O 19
0F0A: e4 ca          JSR  $0DC8                                        ; {} P 20
0F0C: eb ca          JSR  $0DD6                                        ; {} Q 21
0F0E: f4 ca          JSR  $0DE8                                        ; {} R 22
0F10: fc ca          JSR  $0DF8                                        ; {} S 23
0F12: 03 cb          JSR  $0E06                                        ; {} T 24
0F14: 09 cb          JSR  $0E12                                        ; {} U 25
0F16: 0f cb          JSR  $0E1E                                        ; {} V 26
0F18: 14 cb          JSR  $0E28                                        ; {} W 27
0F1A: 1b cb          JSR  $0E36                                        ; {} X 28
0F1C: 20 cb          JSR  $0E40                                        ; {} Y 29
0F1E: 27 cb          JSR  $0E4E                                        ; {} Z 30

;; = Messages =
; Message offsets
0F20: 0B  ; HIGH SCORES
0F21: 13  ; PLAYER
0F22: 19  ; YOUR SCORE IS ONE OF THE TEN BEST
0F23: 2f  ; PEASE ENTER YOUR INITIALS
0F24: 41  ; PUSH ROTATE TO SELECT LETTER
0F25: 55  ; PUSH HYPERSPACE WHEN LETTER IS CORRECT
0F26: 6f  ; PUSH START
0F27: 77  ; GAME OVER
0F28: 7d  ; 1 COIN 2 PLAYS
0F29: 87  ; 1 COIN 1 PLAY
0F2A: 91  ; 2 COINS 1 PLAY

;; Messages are packed with 3 characters in 2 bytes (3 5-bit characters).
;; The upper 15 bits are used. If the last bit is set then the message terminates.
;; If the last bit is clear then the next two bytes are parsed UNLESS the parser
;; finds a 00000 character. That pattern terminates the message too.
;;
;; Here is the character map for a 5 bit character (00-1F):[[BR]]
;; "@_012ABCDEFGHIJKLMNOPQRSTUVWXYZ"
;; Again ... a 0 ("@") terminates the message

; HIGH SCORES
; 01100_01101_01011_0 01100_00001_10111_0 00111_10011_10110_0 01001_10111_00000_0
; H     I     G       H     _     S       C     O     R       E     S     @ 
0F2B: 63 56 60 6e 3c ec 4d c0 
 
; PLAYER_
; 10100_10000_00101_0 11101_01001_10110_0 00001_00000_00000_0 
; P     L     A       Y     E     R       _     @     @  
0F33: a4 0a ea 6c 08 00

; YOUR SCORE IS ONE OF THE TEN BEST
; 11101_10011_11001_0 10110_00001_10111_0 00111_10011_10110_0 01001_00001_01101_0 10111_00001_10011_0 10010_01001_00001_0 10011_01010_00001_0 11000_01100_01001_0 00001_11000_01001_0 10010_00001_00110_0 01001_10111_11000_1 
; Y     O     U       R     _     S       C     O     R       E     _     I       S     _     O       N     E     _       O     F     _       T     H     E       _     T     E       N     _     B       E     S     T     @ 
0F39: ec f2 b0 6e 3c ec 48 5a b8 66 92 42 9a 82 c3 12 0e 12 90 4c 4d f1

; PEASE ENTER YOUR INITIALS
; 10100_10000_01001_0 00101_10111_01001_0 00001_01001_10010_0 11000_01001_10110_0 00001_11101_10011_0 11001_10110_00001_0 01101_10010_01101_0 11000_01101_00101_0 10000_10111_00000_0 
; P     L     E       A     S     E       _     E     N       T     E     R       _     Y     O       U     R     _       I     N     I       T     I     A       L     S     @     
0F4F: a4 12 2d d2 0a 64 c2 6c 0f 66 cd 82 6c 9a c3 4a 85 c0

; PUSH ROTATE TO SELECT LETTER
; 10100_11001_10111_0 01100_00001_10110_0 10011_11000_00101_0 11000_01001_00001_0 11000_10011_00001_0 10111_01001_10000_0 01001_00111_11000_0 00001_10000_01001_0 11000_11000_01001_0 10110_00000_00000_0 
; P     U     S       H     _     R       O     T     A       T     E     _       T     O     _       S     E     L       E     C     T       _     L     E       T     T     E       R     @     @     
0F61: a6 6e 60 6c 9e 0a c2 42 c4 c2 ba 60 49 f0 0c 12 c6 12 b0 00

; PUSH HYPERSPACE WHEN LETTER IS CORRECT
; 10100_11001_10111_0 01100_00001_01100_0 11101_10100_01001_0 10110_10111_10100_0 00101_00111_01001_0 00001_11011_01100_0 01001_10010_00001_0 10000_01001_11000_0 11000_01001_10110_0 00001_01101_10111_0 00001_00111_10011_0 10110_10110_01001_0 00111_11000_00000_0 
; P     U     S       H     _     H       Y     P     E       R     S     P       A     C     E       _     W     H       E     N     _       L     E     T       T     E     R       _     I     S       _     C     O       R     R     E       C     T     @     
0F75: a6 6e 60 58 ed 12 b5 e8 29 d2 0e d8 4c 82 82 70 c2 6c 0B 6e 09 e6 b5 92 3e 00

; PUSH START
; 10100_11001_10111_0 01100_00001_10111_0 11000_00101_10110_0 11000_00000_00000_0 
; P     U     S       H           S       T     A     R       T     @     @     
0F8F: a6 6e 60 6e c1 6c c0 00

; GAME OVER
; 01011_00101_10001_0 01001_00001_10011_0 11010_01001_10110_1 
; G     A     M       E     _     O       V     E     R     @     
0F97: 59 62 48 66 d2 6d

; 1 COIN 2 PLAYS
; 00011_00001_00111_0 10011_01101_10010_0 00001_00100_00001_0 10100_10000_00101_0 11101_10111_00000_0 
; 1     _     C       O     I     N       _     2     _       P     L     A       Y     S     @    
0F9D: 18 4e 9b 64 09 02 a4 0a ed c0

; 1 COIN 1 PLAY
; 00011_00001_00111_0 10011_01101_10010_0 00001_00011_00001_0 10100_10000_00101_0 11101_00000_00000_0 
; 1     _     C       O     I     N       _     1     _       P     L     A       Y     @     @ 
0FA7: 18 4e 9b 64 08 c2 a4 0a e8 00

; 2 COINS 1 PLAY
; 00100_00001_00111_0 10011_01101_10010_0 10111_00001_00011_0 00001_10100_10000_0 00101_11101_00000_0 
; 2     _     C       O     I     N       S     _     1       _     P     L       A     Y     @     
0FB1: 20 4e 9b 64 b8 46 0d 20 2f 40

;; = Sine lookup table =
; Used for vertical thrust (offset by 64 to get cosine for horizontal thrust)
0FBB: 00 03 06 09 0c 10 13 16
0FC3: 19 1c 1f 22 25 28 2b 2e
0FCB: 31 33 36 39 3c 3f 41 44
0FD3: 47 49 4c 4e 51 53 55 58
0FDB: 5a 5c 5e 60 62 64 66 68
0FE3: 6a 6b 6d 6f 70 71 73 74
0FEB: 75 76 78 79 7a 7a 7b 7c
0FF3: 7d 7d 7e 7e 7e 7f 7f 7f
0FFB: 7f

; Extra space
0FFC: 00 00 00 00
```