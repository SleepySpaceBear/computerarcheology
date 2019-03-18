![Sound Code](MoonPatrol.jpg)

# Sound Code
>>> cpu 6803

>>> memoryTable hard 
[Hardware Info](SoundHardware.md)

>>> memoryTable ram 
[RAM Usage](SoundRAMUse.md)

# DAC Explosion Samples

```code
DACExplosionSamples: 
; Interesting. This explosion effect lasting 1/2 second consumes 1/4th of the ROM.
; Each byte contains 2 4-bit samples that are played one after the other.
;
; 1024 bytes = 2048 samples / 4000Hz = 0.512 seconds
;
F000: 88 08 14 3F 8D 51 0C 24 E0 91 00 F9 3A 1A 80 C2 F1 35 00 D1 59 88 89 D4 2B B0 52 8D 84 A1 2B 84
F020: A9 03 F0 88 21 30 BF 02 B9 B3 40 42 1D 98 B2 0C 8A 02 80 09 7F 91 12 88 23 23 98 D9 C3 42 3B 8E
F040: C2 00 0A A1 9C 33 38 89 C7 8A 10 02 F9 12 81 22 2A 9B E9 B2 0F 19 B9 63 9A 20 A0 08 9A 88 2F A4
F060: 35 20 A8 83 40 AA C9 89 8B 90 BD 92 35 18 C9 52 33 29 03 38 9B FD 82 AA 18 11 0B F9 13 19 92 62
F080: 3A CB D8 32 1A AB 83 49 B4 39 B9 AD CC A2 72 89 11 09 82 28 88 99 0E 05 21 89 BC CA 02 99 80 2A
F0A0: EB 13 33 25 42 43 10 36 09 B9 CE 90 14 31 10 9D D9 80 99 B8 8A AB A8 9B B2 76 34 22 18 09 BB 98
F0C0: 33 1B DA 89 92 0A BA BD 47 20 9B E9 01 18 88 25 41 32 33 52 CD 98 08 09 82 31 AF 99 90 89 9C CB
F0E0: CA 00 A0 11 10 B8 44 64 23 10 9C 99 C9 01 20 05 28 26 22 00 38 DB B0 8A A0 43 53 18 CD D8 03 19
F100: AA 9A A9 AC B2 76 22 AA 99 9A 90 0C CA AB 99 37 61 00 89 02 09 22 81 BD CB C9 05 54 20 08 99 A9
F120: 22 18 01 18 AE B9 04 48 BC 88 8A EC 80 11 9A 99 93 75 08 98 88 91 89 12 02 9A DB 04 33 82 39 FA
F140: 24 10 9A DD 91 35 33 10 19 A1 99 AB C3 77 1A AB CC 90 08 AC A0 23 33 22 05 31 31 13 09 BA 91 24
F160: 10 2C FC DC A8 99 99 88 BE 92 43 14 31 12 34 35 31 13 42 AA CC BD CA BA 01 00 99 9B A0 82 34 63
F180: 20 81 17 52 00 8A 9A 03 32 8C CB CD BC AB DA 8A 04 53 21 8A 81 45 42 28 AD BB A9 82 62 21 21 88
F1A0: 88 02 00 AD AA 92 70 8A CC CB BA A8 37 42 00 8A 99 AA B8 02 11 0A CA 13 23 75 41 08 99 82 54 32
F1C0: 98 A9 9A A9 9A 82 54 1D EB CB 99 03 53 10 99 89 BC 92 10 33 65 20 99 AA A1 00 32 1B EE BA 01 44
F1E0: 32 80 13 36 89 A9 ED B9 88 09 A0 31 18 07 31 14 08 80 31 20 09 DB 98 89 DD 90 03 82 50 9C A9 12
F200: 9C D8 88 34 83 63 32 12 08 32 AF BB FC 9A CC A0 13 42 08 81 11 35 32 42 22 0C CD 98 98 02 08 22
F220: 2A DA 8A 11 89 DC 99 B0 34 9D C8 12 1A EA 99 01 00 9A 37 42 36 23 21 98 10 9A CB AB B3 73 53 10
F240: AA FA 01 28 AA 88 90 9E DA A0 98 AC E9 82 11 10 22 81 47 53 22 09 90 89 12 8C FB AA 98 9A AB 90
F260: 32 1B D9 45 22 62 22 42 9C BB BB 99 02 45 34 23 9B B9 9C BB C8 02 63 39 91 44 30 01 48 BB FC BA
F280: CC A8 10 11 11 89 11 9D B8 03 74 34 20 88 01 23 20 88 BF B9 9A 01 08 AD 05 38 9B DA 93 48 AB AB
F2A0: 8B DB 99 82 37 29 CB A0 41 53 23 48 12 22 DD C9 81 34 32 28 9A 98 39 D9 8B 83 53 0F A9 9E B9 8A
F2C0: 88 88 25 12 32 BA 09 27 3A 9A 14 53 01 41 10 89 DC BB 83 52 9B DC 90 10 10 13 12 11 25 40 00 C8
F2E0: 8A B1 18 BC B4 34 09 9D CC BA AC 82 26 32 89 BC DA 98 21 32 37 31 00 11 A9 01 8F 98 00 23 1A A9
F300: 34 03 53 43 32 AD DB CB A9 BC 98 0B 00 61 24 20 88 35 23 50 08 CD B9 82 64 20 9A BB B9 9D DB 90
F320: 10 24 31 31 18 03 38 10 1A 1B FD CA 80 12 33 64 20 9A 88 88 98 03 30 BE 90 09 98 40 0A A4 53 19
F340: 13 9C FD AA A8 80 19 82 24 22 AD 90 56 20 99 20 8B BB 12 1B 85 30 EE B9 02 42 12 15 22 20 88 11
F360: 88 90 09 BF BC EA A8 88 9A 90 09 00 11 32 36 08 00 05 08 12 33 95 33 13 10 BC EC 99 21 11 33 63
F380: 31 00 AA FC AA 80 00 23 40 AC B9 90 92 53 89 FA A0 02 8A 91 2B DE 99 81 23 62 30 21 23 28 DC BC
F3A0: 81 10 99 08 14 72 20 9A A9 99 BE B9 24 18 AC 03 10 AB A9 02 34 35 42 00 08 88 29 9D A0 53 2A FB
F3C0: BB 01 00 8A A8 01 90 00 A1 36 32 02 3A AB 9C BB 89 8A CC AA 32 32 28 32 21 00 25 52 18 8A AA 11
F3E0: 28 08 20 32 AD EB A9 81 42 89 08 99 01 99 99 88 80 0A 08 33 52 37 10 AB D9 00 98 01 08 A8 03 42

; 0     
; 1     Half-second explosion played with samples on DAC-0 (Player shoots rocks)
; 2     Very, very short explosion with same samples (Missiles hitting ground)
; 3     Slightly shorter version of 1 (code plays 3 after 2 automatically)
;
; 4-15  Unused (perhaps slots for other DAC sounds)
```

# Explosion Commands

```code
ExplosionCommands: 
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
```

# Command Scripts

```code
CommandScripts: 
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

# End Music

```code
EndMusic: 
;  Script for command $1B - Ending music (test 10)
F464: 66 F8                            ; MIXER_AND AY0 11_111_000 ...
F466: 48 10                            ; REGISTER AY0:08 10 ...
F468: 49 10                            ; REGISTER AY0:09 10 ...
F46A: 4A 10                            ; REGISTER AY0:0A 10 ...
F46C: 4B 00                            ; REGISTER AY0:0B 00 ...
F46E: 4C 10                            ; REGISTER AY0:0C 10 ...
F470: 20 EE 00 28                      ; THREETONE AY0:00 fine=EE coarse=00 (28)
F474: 20 BD 00 28                      ; THREETONE AY0:00 fine=BD coarse=00 (28)
F478: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F47C: 20 86 00 28                      ; THREETONE AY0:00 fine=86 coarse=00 (28)
F480: 27 07 28                         ; MIXER_OR AY0 00_000_111 (28)
F483: 66 F8                            ; MIXER_AND AY0 11_111_000 ...
F485: 20 86 00 28                      ; THREETONE AY0:00 fine=86 coarse=00 (28)
F489: 20 8E 00 28                      ; THREETONE AY0:00 fine=8E coarse=00 (28)
F48D: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F491: 20 0C 01 28                      ; THREETONE AY0:00 fine=0C coarse=01 (28)
F495: 20 86 00 28                      ; THREETONE AY0:00 fine=86 coarse=00 (28)
F499: 20 FD 00 28                      ; THREETONE AY0:00 fine=FD coarse=00 (28)
F49D: 20 7E 00 28                      ; THREETONE AY0:00 fine=7E coarse=00 (28)
F4A1: 20 EE 00 A0                      ; THREETONE AY0:00 fine=EE coarse=00 (A0)
F4A5: 67 07                            ; MIXER_OR AY0 00_000_111 ...

;  Script for command $19, $1A
F4A7: FF                               ; STOP
```

# Reaching Goal

```code
ReachingGoal: 
;  Script for command $1D - Reaching goal (test 12)
F4A8: 66 F8                            ; MIXER_AND AY0 11_111_000 ...
F4AA: 48 10                            ; REGISTER AY0:08 10 ...
F4AC: 49 10                            ; REGISTER AY0:09 10 ...
F4AE: 4A 10                            ; REGISTER AY0:0A 10 ...
F4B0: 4B 00                            ; REGISTER AY0:0B 00 ...
F4B2: 4C 10                            ; REGISTER AY0:0C 10 ...
F4B4: FE F4 CD                         ; CALL F4CD(1)
F4B7: 20 77 00 24                      ; THREETONE AY0:00 fine=77 coarse=00 (24)
F4BB: 20 7E 00 24                      ; THREETONE AY0:00 fine=7E coarse=00 (24)
F4BF: 20 9F 00 24                      ; THREETONE AY0:00 fine=9F coarse=00 (24)
F4C3: FE F4 CD                         ; CALL F4CD(1)
F4C6: 20 EE 00 60                      ; THREETONE AY0:00 fine=EE coarse=00 (60)
F4CA: 67 07                            ; MIXER_OR AY0 00_000_111 ...
F4CC: FF                               ; STOP
F4CD: 20 EE 00 24                      ; THREETONE AY0:00 fine=EE coarse=00 (24)
F4D1: 20 9F 00 24                      ; THREETONE AY0:00 fine=9F coarse=00 (24)
F4D5: 20 77 00 24                      ; THREETONE AY0:00 fine=77 coarse=00 (24)
F4D9: 20 B3 00 24                      ; THREETONE AY0:00 fine=B3 coarse=00 (24)
F4DD: 20 8E 00 24                      ; THREETONE AY0:00 fine=8E coarse=00 (24)
F4E1: 20 77 00 24                      ; THREETONE AY0:00 fine=77 coarse=00 (24)
F4E5: 20 9F 00 24                      ; THREETONE AY0:00 fine=9F coarse=00 (24)
F4E9: 20 7E 00 24                      ; THREETONE AY0:00 fine=7E coarse=00 (24)
F4ED: 20 6A 00 24                      ; THREETONE AY0:00 fine=6A coarse=00 (24)
F4F1: FD                               ; RETURN (1)

;  Script for command $15
F4F2: 67 01                            ; MIXER_OR AY0 00_000_001 ...
F4F4: FF                               ; STOP
```

# Space Plant

```code
SpacePlant: 
;  Script for command $16 - Space plant (test 7)
F4F5: 66 FE                            ; MIXER_AND AY0 11_111_110 ...
F4F7: 48 0F                            ; REGISTER AY0:08 0F ...
F4F9: 41 02                            ; REGISTER AY0:01 02 ...
F4FB: 00 CE 24                         ; REGISTER AY0:00 CE (24)
F4FE: 00 A7 24                         ; REGISTER AY0:00 A7 (24)
F501: 00 7D 24                         ; REGISTER AY0:00 7D (24)
F504: 00 A7 24                         ; REGISTER AY0:00 A7 (24)
F507: 00 58 24                         ; REGISTER AY0:00 58 (24)
F50A: 00 A7 24                         ; REGISTER AY0:00 A7 (24)
F50D: 00 7D 24                         ; REGISTER AY0:00 7D (24)
F510: 00 A7 24                         ; REGISTER AY0:00 A7 (24)
F513: FE F4 FB                         ; CALL F4FB(1)
```

# UFO Flying 

```code
UFOFlying: 
;  Script for command $17 - UFO flying (test 8)
F516: 66 FE                            ; MIXER_AND AY0 11_111_110 ...
F518: 41 00                            ; REGISTER AY0:01 00 ...
F51A: 48 0D                            ; REGISTER AY0:08 0D ...
F51C: C0 10 30 01 06                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=10 initFreq=30 deltaFreq=01 timeBetween=06
F521: 48 0D                            ; REGISTER AY0:08 0D ...
F523: C0 18 40 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=40 deltaFreq=01 timeBetween=04
F528: C0 14 58 FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=58 deltaFreq=FF timeBetween=04
F52D: 48 0C                            ; REGISTER AY0:08 0C ...
F52F: C0 18 44 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=44 deltaFreq=01 timeBetween=04
F534: C0 14 5C FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=5C deltaFreq=FF timeBetween=04
F539: 48 0B                            ; REGISTER AY0:08 0B ...
F53B: C0 18 48 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=48 deltaFreq=01 timeBetween=04
F540: C0 14 60 FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=60 deltaFreq=FF timeBetween=04
F545: 48 0A                            ; REGISTER AY0:08 0A ...
F547: C0 14 4C 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=4C deltaFreq=01 timeBetween=04
F54C: C0 18 60 FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=60 deltaFreq=FF timeBetween=04
F551: 48 0B                            ; REGISTER AY0:08 0B ...
F553: C0 14 48 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=48 deltaFreq=01 timeBetween=04
F558: C0 18 5C FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=5C deltaFreq=FF timeBetween=04
F55D: 48 0C                            ; REGISTER AY0:08 0C ...
F55F: C0 14 44 01 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=14 initFreq=44 deltaFreq=01 timeBetween=04
F564: C0 18 58 FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=00 numSteps=18 initFreq=58 deltaFreq=FF timeBetween=04
F569: FE F5 21                         ; CALL F521(1)
```

# Background Music

```code
BackgroundMusic: 
;  Script for command $18 - Background music (test 9)
;
;  Sound processing divides the NMI clock (4KHz) by 16. The sound tick thus runs at
;  4000/16 = 250Hz (each tick lasts 0.004 seconds ... 4Ms).
;
;  The song loop is defined by 12 fragments. Each fragment has 16 delays of (20) ticks, (32 decimal).
;  The CALL and RETURN for each fragment take 1 tick each.
;  Thus the song takes 12*(32*16+2) = 6168 ticks.
;
;  6168 * 4Ms = 24.672 seconds to play entire song through once
;
F56C: 6D 10        ; 1 VOLUME_DECAY_SPEED voice=1 10 ...
F56E: 46 00        ; 2 REGISTER AY0:06 00 ...
F570: 4B 00        ; 3 REGISTER AY0:0B 00 ...
F572: 4C 02        ; 4 REGISTER AY0:0C 02 ...
F574: 4A 10        ; 5 REGISTER AY0:0A 10 ...
F576: 66 DD        ; 6 MIXER_AND AY0 11_011_101 ...
;
F578: FE F5 9F     ; 7 CALL F59F(1)   - Fragment A
F57B: FE F5 F4     ; 8 CALL F5F4(1)   - Fragment B
F57E: FE F5 9F     ; 9 CALL F59F(1)   - Fragment A
F581: FE F5 F4     ; 10 CALL F5F4(1)  - Fragment B
F584: FE F6 A2     ; 11 CALL F6A2(1)  - Fragment C
F587: FE F6 F9     ; 12 CALL F6F9(1)  - Fragment D
F58A: FE F5 9F     ; 13 CALL F59F(1)  - Fragment A
F58D: FE F5 F4     ; 14 CALL F5F4(1)  - Fragment B
F590: FE F7 54     ; 15 CALL F754(1)  - Fragment E
F593: FE F6 A2     ; 16 CALL F6A2(1)  - Fragment C
F596: FE F5 9F     ; 17 CALL F59F(1)  - Fragment A
F599: FE F6 4B     ; 18 CALL F64B(1)  - Fragment F
;
F59C: FE F5 6C     ; 19 CALL F56C(1) (GOTO)
;
F59F: 42 A7        ; 20 REGISTER AY0:02 A7 ...
F5A1: 43 02        ; 21 REGISTER AY0:03 02 ...                      
F5A3: 69 0E        ; 22 SET_VOLUME_AND_RESET_DECAY voice=1 0D ... 
F5A5: 0D 09 20     ; 23 REGISTER AY0:0D 09 (20)                   * E2  82.37168630338734
F5A8: 0D 09 20     ; 24 REGISTER AY0:0D 09 (20)                   * 
F5AB: 69 0E        ; 25 SET_VOLUME_AND_RESET_DECAY voice=1 0D ... 
F5AD: 0D 09 20     ; 26 REGISTER AY0:0D 09 (20)                   * E2  82.37168630338734
F5B0: 0D 09 20     ; 27 REGISTER AY0:0D 09 (20)                   * 
F5B3: 42 51        ; 28 REGISTER AY0:02 51 ...
F5B5: 43 01        ; 29 REGISTER AY0:03 01 ...                    
F5B7: 69 0E        ; 30 SET_VOLUME_AND_RESET_DECAY voice=1 0D ... 
F5B9: 0D 09 20     ; 31 REGISTER AY0:0D 09 (20)                   * E3  165.96550445103858
F5BC: 0D 09 20     ; 32 REGISTER AY0:0D 09 (20)                   * 
F5BF: 69 0E        ; 33 SET_VOLUME_AND_RESET_DECAY voice=1 0D ... 
F5C1: 0D 09 20     ; 34 REGISTER AY0:0D 09 (20)                   * E3  165.96550445103858
F5C4: 42 7A        ; 35 REGISTER AY0:02 7A ...                    
F5C6: 69 0E        ; 36 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5C8: 0D 09 20     ; 37 REGISTER AY0:0D 09 (20)                   * D3  147.96395502645504
F5CB: 0D 09 20     ; 38 REGISTER AY0:0D 09 (20)                   * 
F5CE: 69 0E        ; 39 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5D0: 0D 09 20     ; 40 REGISTER AY0:0D 09 (20)                   * D3  147.96395502645504
F5D3: 42 C1        ; 41 REGISTER AY0:02 C1 ...                    
F5D5: 69 0E        ; 42 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5D7: 0D 09 20     ; 43 REGISTER AY0:0D 09 (20)                   * B2  124.56653674832963
F5DA: 0D 09 20     ; 44 REGISTER AY0:0D 09 (20)                   * 
F5DD: 42 7A        ; 45 REGISTER AY0:02 7A ...                     
F5DF: 69 0E        ; 46 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5E1: 0D 09 20     ; 47 REGISTER AY0:0D 09 (20)                   * D3  147.96395502645504
F5E4: 0D 09 20     ; 48 REGISTER AY0:0D 09 (20)                   * 
F5E7: 42 51        ; 49 REGISTER AY0:02 51 ...
F5E9: 43 01        ; 50 REGISTER AY0:03 01 ...                      
F5EB: 69 0E        ; 51 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5ED: 0D 09 20     ; 52 REGISTER AY0:0D 09 (20)                   * E3  165.96550445103858
F5F0: 0D 09 20     ; 53 REGISTER AY0:0D 09 (20)                   * 
F5F3: FD           ; 54 RETURN (1)
;
F5F4: 42 A7        ; 55 REGISTER AY0:02 A7 ...
F5F6: 43 02        ; 56 REGISTER AY0:03 02 ...
F5F8: 69 0E        ; 57 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F5FA: 0D 09 20     ; 58 REGISTER AY0:0D 09 (20)                  * E2  82.37168630338734
F5FD: 0D 09 20     ; 59 REGISTER AY0:0D 09 (20)                  * 
F600: 69 0E        ; 60 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F602: 0D 09 20     ; 61 REGISTER AY0:0D 09 (20)                  * E2  82.37168630338734
F605: 0D 09 20     ; 62 REGISTER AY0:0D 09 (20)                  * 
F608: 42 51        ; 63 REGISTER AY0:02 51 ...
F60A: 43 01        ; 64 REGISTER AY0:03 01 ...
F60C: 69 0E        ; 65 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F60E: 0D 09 20     ; 66 REGISTER AY0:0D 09 (20)                  * E3  165.96550445103858
F611: 0D 09 20     ; 67 REGISTER AY0:0D 09 (20)                  * 
F614: 69 0E        ; 68 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F616: 0D 09 20     ; 69 REGISTER AY0:0D 09 (20)                  * E3  165.96550445103858
F619: 42 7A        ; 70 REGISTER AY0:02 7A ...
F61B: 69 0E        ; 71 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F61D: 0D 09 20     ; 72 REGISTER AY0:0D 09 (20)                  * D3  147.96395502645504
F620: 0D 09 20     ; 73 REGISTER AY0:0D 09 (20)                  * 
F623: 69 0E        ; 74 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F625: 0D 09 20     ; 75 REGISTER AY0:0D 09 (20)                  * D3  147.96395502645504
F628: 42 C1        ; 76 REGISTER AY0:02 C1 ...
F62A: 69 0E        ; 77 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F62C: 0D 09 20     ; 78 REGISTER AY0:0D 09 (20)                  * B2  124.56653674832963
F62F: 0D 09 20     ; 79 REGISTER AY0:0D 09 (20)                  * 
F632: 42 FC        ; 80 REGISTER AY0:02 FC ...
F634: 69 0E        ; 81 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F636: 0D 09 20     ; 82 REGISTER AY0:0D 09 (20)                  * A2  110.09916338582677
F639: 42 DD        ; 83 REGISTER AY0:02 DD ...
F63B: 69 0E        ; 84 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F63D: 0D 09 20     ; 85 REGISTER AY0:0D 09 (20)                  * A#2 117.25445492662473
F640: 42 C1        ; 86 REGISTER AY0:02 C1 ...
F642: 69 0E        ; 87 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F644: 0D 09 20     ; 88 REGISTER AY0:0D 09 (20)                  * B2  124.56653674832963
F647: 0D 09 20     ; 89 REGISTER AY0:0D 09 (20)                  * 
F64A: FD           ; 90 RETURN (1)
;
F64B: 42 A7        ; 91 REGISTER AY0:02 A7 ...
F64D: 43 02        ; 92 REGISTER AY0:03 02 ...
F64F: 69 0E        ; 93 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F651: 0D 09 20     ; 94 REGISTER AY0:0D 09 (20)                  * E2  82.37168630338734
F654: 69 0E        ; 95 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F656: 0D 09 20     ; 96 REGISTER AY0:0D 09 (20)                  * E2  82.37168630338734
F659: 0D 09 20     ; 97 REGISTER AY0:0D 09 (20)                  * 
F65C: 69 0E        ; 98 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F65E: 0D 09 20     ; 99 REGISTER AY0:0D 09 (20)                  * E2  82.37168630338734
F661: 42 16        ; 100 REGISTER AY0:02 16 ...
F663: 69 0E        ; 101 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F665: 0D 09 20     ; 102 REGISTER AY0:0D 09 (20)                 * G#2 104.73852996254682
F668: 69 0E        ; 103 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F66A: 0D 09 20     ; 104 REGISTER AY0:0D 09 (20)                 * G#2 104.73852996254682
F66D: 0D 09 20     ; 105 REGISTER AY0:0D 09 (20)                 * 
F670: 69 0E        ; 106 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F672: 0D 09 20     ; 107 REGISTER AY0:0D 09 (20)                 * G#2 104.73852996254682
F675: 42 FC        ; 108 REGISTER AY0:02 FC ...
F677: 43 01        ; 109 REGISTER AY0:03 01 ...
F679: 69 0E        ; 110 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F67B: 0D 09 20     ; 111 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F67E: 69 0E        ; 112 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F680: 0D 09 20     ; 113 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F683: 0D 09 20     ; 114 REGISTER AY0:0D 09 (20)                 * 
F686: 69 0E        ; 115 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F688: 0D 09 20     ; 116 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F68B: 42 DD        ; 117 REGISTER AY0:02 DD ...
F68D: 69 0E        ; 118 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F68F: 0D 09 20     ; 119 REGISTER AY0:0D 09 (20)                 * A#2 117.25445492662473
F692: 69 0E        ; 120 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F694: 0D 09 20     ; 121 REGISTER AY0:0D 09 (20)                 * A#2 117.25445492662473
F697: 0D 09 20     ; 122 REGISTER AY0:0D 09 (20)                 * 
F69A: 42 C1        ; 123 REGISTER AY0:02 C1 ...
F69C: 69 0E        ; 124 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F69E: 0D 09 20     ; 125 REGISTER AY0:0D 09 (20)                 * B2  124.56653674832963
F6A1: FD           ; 126 RETURN (1)
;
F6A2: 42 FC        ; 127 REGISTER AY0:02 FC ...
F6A4: 43 01        ; 128 REGISTER AY0:03 01 ...
F6A6: 69 0E        ; 129 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6A8: 0D 09 20     ; 130 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F6AB: 0D 09 20     ; 131 REGISTER AY0:0D 09 (20)                 * 
F6AE: 69 0E        ; 132 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6B0: 0D 09 20     ; 133 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F6B3: 0D 09 20     ; 134 REGISTER AY0:0D 09 (20)                 * 
F6B6: 42 FD        ; 135 REGISTER AY0:02 FD ...
F6B8: 43 00        ; 136 REGISTER AY0:03 00 ...
F6BA: 69 0E        ; 137 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6BC: 0D 09 20     ; 138 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F6BF: 0D 09 20     ; 139 REGISTER AY0:0D 09 (20)                 * 
F6C2: 69 0E        ; 140 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6C4: 0D 09 20     ; 141 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F6C7: 42 1C        ; 142 REGISTER AY0:02 1C ...
F6C9: 43 01        ; 143 REGISTER AY0:03 01 ...
F6CB: 69 0E        ; 144 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6CD: 0D 09 20     ; 145 REGISTER AY0:0D 09 (20)                 * G3  196.93794014084506
F6D0: 0D 09 20     ; 146 REGISTER AY0:0D 09 (20)                 * 
F6D3: 69 0E        ; 147 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6D5: 0D 09 20     ; 148 REGISTER AY0:0D 09 (20)                 * G3  196.93794014084506
F6D8: 42 51        ; 149 REGISTER AY0:02 51 ...
F6DA: 69 0E        ; 150 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6DC: 0D 09 20     ; 151 REGISTER AY0:0D 09 (20)                 * E3  165.96550445103858
F6DF: 0D 09 20     ; 152 REGISTER AY0:0D 09 (20)                 * 
F6E2: 42 1C        ; 153 REGISTER AY0:02 1C ...
F6E4: 69 0E        ; 154 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6E6: 0D 09 20     ; 155 REGISTER AY0:0D 09 (20)                 * G3  196.93794014084506
F6E9: 0D 09 20     ; 156 REGISTER AY0:0D 09 (20)                 * 
F6EC: 42 FD        ; 157 REGISTER AY0:02 FD ...
F6EE: 43 00        ; 158 REGISTER AY0:03 00 ...
F6F0: 69 0E        ; 159 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6F2: 0D 09 20     ; 160 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F6F5: 0D 09 20     ; 161 REGISTER AY0:0D 09 (20)                 * 
F6F8: FD           ; 162 RETURN (1)
;
F6F9: 42 FC        ; 163 REGISTER AY0:02 FC ...
F6FB: 43 01        ; 164 REGISTER AY0:03 01 ...
F6FD: 69 0E        ; 165 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F6FF: 0D 09 20     ; 166 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F702: 0D 09 20     ; 167 REGISTER AY0:0D 09 (20)                 * 
F705: 69 0E        ; 168 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F707: 0D 09 20     ; 169 REGISTER AY0:0D 09 (20)                 * A2  110.09916338582677
F70A: 0D 09 20     ; 170 REGISTER AY0:0D 09 (20)                 * 
F70D: 42 FD        ; 171 REGISTER AY0:02 FD ...
F70F: 43 00        ; 172 REGISTER AY0:03 00 ...
F711: 69 0E        ; 173 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F713: 0D 09 20     ; 174 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F716: 0D 09 20     ; 175 REGISTER AY0:0D 09 (20)                 * 
F719: 69 0E        ; 176 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F71B: 0D 09 20     ; 177 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F71E: 42 1C        ; 178 REGISTER AY0:02 1C ...
F720: 43 01        ; 179 REGISTER AY0:03 01 ...
F722: 69 0E        ; 180 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F724: 0D 09 20     ; 181 REGISTER AY0:0D 09 (20)                 * G3  196.93794014084506
F727: 0D 09 20     ; 182 REGISTER AY0:0D 09 (20)                 * 
F72A: 69 0E        ; 183 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F72C: 0D 09 20     ; 184 REGISTER AY0:0D 09 (20)                 * G3  196.93794014084506
F72F: 42 51        ; 185 REGISTER AY0:02 51 ...
F731: 69 0E        ; 186 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F733: 0D 09 20     ; 187 REGISTER AY0:0D 09 (20)                 * E3  165.96550445103858
F736: 0D 09 20     ; 188 REGISTER AY0:0D 09 (20)                 * 
F739: 42 7A        ; 189 REGISTER AY0:02 7A ...
F73B: 43 01        ; 190 REGISTER AY0:03 01 ...
F73D: 69 0E        ; 191 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F73F: 0D 09 20     ; 192 REGISTER AY0:0D 09 (20)                 * D3  147.96395502645504
F742: 42 65        ; 193 REGISTER AY0:02 65 ...
F744: 69 0E        ; 194 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F746: 0D 09 20     ; 195 REGISTER AY0:0D 09 (20)                 * D#3 156.66771708683473
F749: 42 51        ; 196 REGISTER AY0:02 51 ...
F74B: 69 0E        ; 197 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F74D: 0D 09 20     ; 198 REGISTER AY0:0D 09 (20)                 * E3  165.96550445103858
F750: 0D 09 20     ; 199 REGISTER AY0:0D 09 (20)                 * 
F753: FD           ; 200 RETURN (1)
;
F754: 42 C1        ; 201 REGISTER AY0:02 C1 ...
F756: 43 01        ; 202 REGISTER AY0:03 01 ...
F758: 69 0E        ; 203 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F75A: 0D 09 20     ; 204 REGISTER AY0:0D 09 (20)                 * B2  124.56653674832963
F75D: 0D 09 20     ; 205 REGISTER AY0:0D 09 (20)                 * 
F760: 69 0E        ; 206 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F762: 0D 09 20     ; 207 REGISTER AY0:0D 09 (20)                 * B2  124.56653674832963
F765: 0D 09 20     ; 208 REGISTER AY0:0D 09 (20)                 * 
F768: 42 E1        ; 209 REGISTER AY0:02 E1 ...
F76A: 43 00        ; 210 REGISTER AY0:03 00 ...
F76C: 69 0E        ; 211 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F76E: 0D 09 20     ; 212 REGISTER AY0:0D 09 (20)                 * B3  248.57944444444445
F771: 0D 09 20     ; 213 REGISTER AY0:0D 09 (20)                 * 
F774: 69 0E        ; 214 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F776: 0D 09 20     ; 215 REGISTER AY0:0D 09 (20)                 * B3  248.57944444444445
F779: 42 FD        ; 216 REGISTER AY0:02 FD ...
F77B: 69 0E        ; 217 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F77D: 0D 09 20     ; 218 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F780: 0D 09 20     ; 219 REGISTER AY0:0D 09 (20)                 * 
F783: 69 0E        ; 220 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F785: 0D 09 20     ; 221 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F788: 42 2C        ; 222 REGISTER AY0:02 2C ...
F78A: 43 01        ; 223 REGISTER AY0:03 01 ...
F78C: 69 0E        ; 224 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F78E: 0D 09 20     ; 225 REGISTER AY0:0D 09 (20)                 * F#3 186.43458333333334
F791: 0D 09 20     ; 226 REGISTER AY0:0D 09 (20)                 * 
F794: 42 FD        ; 227 REGISTER AY0:02 FD ...
F796: 43 00        ; 228 REGISTER AY0:03 00 ...
F798: 69 0E        ; 229 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F79A: 0D 09 20     ; 230 REGISTER AY0:0D 09 (20)                 * A3  221.06867588932806
F79D: 0D 09 20     ; 231 REGISTER AY0:0D 09 (20)                 * 
F7A0: 42 E1        ; 232 REGISTER AY0:02 E1 ...
F7A2: 69 0E        ; 233 SET_VOLUME_AND_RESET_DECAY voice=1 0D ...
F7A4: 0D 09 20     ; 234 REGISTER AY0:0D 09 (20)                 * B3  248.57944444444445
F7A7: 0D 09 20     ; 235 REGISTER AY0:0D 09 (20)                 * 
F7AA: FD           ; 246 RETURN (1)
```

# Missile 

```code
Missile: 
;  Script for command $12 - Missile from car (test 4)
F7AB: 76 FE                            ; MIXER_AND AY1 11_111_110 ...
F7AD: 51 00                            ; REGISTER AY1:01 00 ...
F7AF: 58 0D                            ; REGISTER AY1:08 0D ...
F7B1: D0 0B 20 FF 04                   ;  C_SWEEP_VOICE_REGISTER retister=10 numSteps=0B initFreq=20 deltaFreq=FF timeBetween=04
F7B6: 77 01                            ; MIXER_OR AY1 00_000_001 ...
F7B8: FF                               ; STOP
```

# UFO Explosion

```code
UFOExplosion: 
;  Script for command $11 - UFO explosion (test 3)
F7B9: 76 FE                            ; MIXER_AND AY1 11_111_110 ...
F7BB: 58 10                            ; REGISTER AY1:08 10 ...
F7BD: 51 00                            ; REGISTER AY1:01 00 ...
F7BF: 5C 18                            ; REGISTER AY1:0C 18 ...
F7C1: 5D 09                            ; REGISTER AY1:0D 09 ...
F7C3: 90 18 0E                         ;  C_REGISTER_SAMPLES register=10 numSamples=18 timeBetween=0E
F7C6: 60 50 60 72 60 50 60 72 60 50 60 72 60 50 60 72 60 50 60 72 60 50 60 72
F7DE: 77 01                            ; MIXER_OR AY1 00_000_001 ...
F7E0: FF                               ; STOP
```

# Pass Point

```code
PassPoint: 
;  Script for command $10 - Passing one point (test 2)
F7E1: 76 FE                            ; MIXER_AND AY1 11_111_110 ...
F7E3: 58 10                            ; REGISTER AY1:08 10 ...
F7E5: 50 4C                            ; REGISTER AY1:00 4C ...
F7E7: 51 00                            ; REGISTER AY1:01 00 ...
F7E9: 5C 14                            ; REGISTER AY1:0C 14 ...
F7EB: 1D 09 E0                         ; REGISTER AY1:0D 09 (E0)
F7EE: 77 01                            ; MIXER_OR AY1 00_000_001 ...
F7F0: FF                               ; STOP
```

# Coin

```code
Coin: 
;  Script for command $13 - Coin (test 5)
F7F1: 50 70                            ; REGISTER AY1:00 70 ...
F7F3: 51 00                            ; REGISTER AY1:01 00 ...
F7F5: 76 FE                            ; MIXER_AND AY1 11_111_110 ...
F7F7: 58 10                            ; REGISTER AY1:08 10 ...
F7F9: 5B 00                            ; REGISTER AY1:0B 00 ...
F7FB: 5C 10                            ; REGISTER AY1:0C 10 ...
F7FD: 1D 09 E0                         ; REGISTER AY1:0D 09 (E0)
F800: 77 01                            ; MIXER_OR AY1 00_000_001 ...
F802: FF                               ; STOP
```

# Jump

```code
Jump: 
;  Script for command $14 - Car jump (test 6)
F803: 52 00                            ; REGISTER AY1:02 00 ...
F805: 53 05                            ; REGISTER AY1:03 05 ...
F807: 55 00                            ; REGISTER AY1:05 00 ...
F809: 76 F9                            ; MIXER_AND AY1 11_111_001 ...
F80B: 59 0F                            ; REGISTER AY1:09 0F ...
F80D: 5A 0F                            ; REGISTER AY1:0A 0F ...
F80F: D4 08 60 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=60 deltaFreq=01 timeBetween=04
F814: 59 0E                            ; REGISTER AY1:09 0E ...
F816: 5A 0E                            ; REGISTER AY1:0A 0E ...
F818: D4 08 68 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=68 deltaFreq=01 timeBetween=04
F81D: 59 0D                            ; REGISTER AY1:09 0D ...
F81F: 5A 0D                            ; REGISTER AY1:0A 0D ...
F821: D4 08 70 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=70 deltaFreq=01 timeBetween=04
F826: 59 0C                            ; REGISTER AY1:09 0C ...
F828: 5A 0C                            ; REGISTER AY1:0A 0C ...
F82A: D4 08 78 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=78 deltaFreq=01 timeBetween=04
F82F: 59 0B                            ; REGISTER AY1:09 0B ...
F831: 5A 0B                            ; REGISTER AY1:0A 0B ...
F833: D4 08 80 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=80 deltaFreq=01 timeBetween=04
F838: 59 0A                            ; REGISTER AY1:09 0A ...
F83A: 5A 0A                            ; REGISTER AY1:0A 0A ...
F83C: D4 08 88 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=88 deltaFreq=01 timeBetween=04
F841: 59 09                            ; REGISTER AY1:09 09 ...
F843: 5A 09                            ; REGISTER AY1:0A 09 ...
F845: D4 08 90 01 04                   ;   C_SWEEP_VOICE_REGISTER retister=14 numSteps=08 initFreq=90 deltaFreq=01 timeBetween=04
F84A: 77 06                            ; MIXER_OR AY1 00_000_110 ...
F84C: FF                               ; STOP
```

# Start Music

```code
StartMusic: 
;  Script for command $1C - Opening music (test 11)
F84D: 6C 14                            ; VOLUME_DECAY_SPEED voice=0 14 ...
F84F: 6D 14                            ; VOLUME_DECAY_SPEED voice=1 14 ...
F851: 6E 0A                            ; VOLUME_DECAY_SPEED voice=2 0A ...
F853: 42 DD                            ; REGISTER AY0:02 DD ...
F855: 43 01                            ; REGISTER AY0:03 01 ...
F857: 4A 10                            ; REGISTER AY0:0A 10 ...
F859: 46 00                            ; REGISTER AY0:06 00 ...
F85B: 4B 00                            ; REGISTER AY0:0B 00 ...
F85D: 4C 04                            ; REGISTER AY0:0C 04 ...
F85F: 47 9C                            ; REGISTER AY0:07 9C ...
F861: FE F8 79                         ; CALL F879(1)
F864: FE F8 79                         ; CALL F879(1)
F867: 47 B8                            ; REGISTER AY0:07 B8 ...
F869: 40 EE                            ; REGISTER AY0:00 EE ...
F86B: 44 77                            ; REGISTER AY0:04 77 ...
F86D: 45 00                            ; REGISTER AY0:05 00 ...
F86F: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F871: 69 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=1 0F ...
F873: 2A 0F 40                         ; SET_VOLUME_AND_RESET_DECAY voice=2 0F (40)
F876: 47 BF                            ; REGISTER AY0:07 BF ...
F878: FF                               ; STOP
F879: 40 EE                            ; REGISTER AY0:00 EE ...
F87B: 41 00                            ; REGISTER AY0:01 00 ...
F87D: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F87F: 49 00                            ; REGISTER AY0:09 00 ...
F881: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F884: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F887: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F889: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F88C: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F88F: 40 86                            ; REGISTER AY0:00 86 ...
F891: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F893: 69 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=1 0F ...
F895: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F898: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F89A: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F89D: 48 00                            ; REGISTER AY0:08 00 ...
F89F: 49 00                            ; REGISTER AY0:09 00 ...
F8A1: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8A4: 40 9F                            ; REGISTER AY0:00 9F ...
F8A6: 69 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=1 0F ...
F8A8: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8AA: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8AD: 48 00                            ; REGISTER AY0:08 00 ...
F8AF: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8B2: 49 00                            ; REGISTER AY0:09 00 ...
F8B4: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8B7: 40 1C                            ; REGISTER AY0:00 1C ...
F8B9: 41 01                            ; REGISTER AY0:01 01 ...
F8BB: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8BD: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8C0: 40 86                            ; REGISTER AY0:00 86 ...
F8C2: 41 00                            ; REGISTER AY0:01 00 ...
F8C4: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8C7: 40 0C                            ; REGISTER AY0:00 0C ...
F8C9: 41 01                            ; REGISTER AY0:01 01 ...
F8CB: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8CD: 69 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=1 0F ...
F8CF: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8D2: 40 86                            ; REGISTER AY0:00 86 ...
F8D4: 41 00                            ; REGISTER AY0:01 00 ...
F8D6: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8D8: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8DB: 40 FD                            ; REGISTER AY0:00 FD ...
F8DD: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8DF: 49 00                            ; REGISTER AY0:09 00 ...
F8E1: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8E4: 40 7E                            ; REGISTER AY0:00 7E ...
F8E6: 68 0F                            ; SET_VOLUME_AND_RESET_DECAY voice=0 0F ...
F8E8: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F8EB: FD                               ; RETURN (1)
```

# Congratulations

```code
Congratulations: 
;  Script for command $1E - Congratulations (test 13)
F8EC: 66 F8                            ; MIXER_AND AY0 11_111_000 ...
F8EE: 48 10                            ; REGISTER AY0:08 10 ...
F8F0: 49 10                            ; REGISTER AY0:09 10 ...
F8F2: 4A 10                            ; REGISTER AY0:0A 10 ...
F8F4: 4B 00                            ; REGISTER AY0:0B 00 ...
F8F6: 4C 10                            ; REGISTER AY0:0C 10 ...
F8F8: FE F9 2D                         ; CALL F92D(1)
F8FB: FE F9 46                         ; CALL F946(1)
F8FE: FE F9 2D                         ; CALL F92D(1)
F901: 20 77 00 28                      ; THREETONE AY0:00 fine=77 coarse=00 (28)
F905: 20 7E 00 28                      ; THREETONE AY0:00 fine=7E coarse=00 (28)
F909: 20 8E 00 28                      ; THREETONE AY0:00 fine=8E coarse=00 (28)
F90D: 20 9F 00 78                      ; THREETONE AY0:00 fine=9F coarse=00 (78)
F911: FE F9 2D                         ; CALL F92D(1)
F914: FE F9 46                         ; CALL F946(1)
F917: FE F9 2D                         ; CALL F92D(1)
F91A: 20 3E 01 28                      ; THREETONE AY0:00 fine=3E coarse=01 (28)
F91E: 20 1C 01 28                      ; THREETONE AY0:00 fine=1C coarse=01 (28)
F922: 20 FD 00 28                      ; THREETONE AY0:00 fine=FD coarse=00 (28)
F926: 20 EE 00 78                      ; THREETONE AY0:00 fine=EE coarse=00 (78)
F92A: 67 07                            ; MIXER_OR AY0 00_000_111 ...
F92C: FF                               ; STOP
F92D: 20 EE 00 28                      ; THREETONE AY0:00 fine=EE coarse=00 (28)
F931: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F935: 20 77 00 28                      ; THREETONE AY0:00 fine=77 coarse=00 (28)
F939: 20 5E 00 28                      ; THREETONE AY0:00 fine=5E coarse=00 (28)
F93D: 20 77 00 28                      ; THREETONE AY0:00 fine=77 coarse=00 (28)
F941: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F945: FD                               ; RETURN (1)
F946: 20 59 00 28                      ; THREETONE AY0:00 fine=59 coarse=00 (28)
F94A: 20 77 00 28                      ; THREETONE AY0:00 fine=77 coarse=00 (28)
F94E: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F952: 20 4F 00 28                      ; THREETONE AY0:00 fine=4F coarse=00 (28)
F956: 20 6A 00 28                      ; THREETONE AY0:00 fine=6A coarse=00 (28)
F95A: 20 9F 00 28                      ; THREETONE AY0:00 fine=9F coarse=00 (28)
F95E: FD                               ; RETURN (1)
```

# Car Explosion

```code
CarExplosion: 
;  Script for command $1F - Car explosion (test 14)
F95F: 46 10                            ; REGISTER AY0:06 10 ...
F961: 66 C7                            ; MIXER_AND AY0 11_000_111 ...
F963: 48 10                            ; REGISTER AY0:08 10 ...
F965: 49 10                            ; REGISTER AY0:09 10 ...
F967: 4A 10                            ; REGISTER AY0:0A 10 ...
F969: 4B 00                            ; REGISTER AY0:0B 00 ...
F96B: 4C 0A                            ; REGISTER AY0:0C 0A ...
F96D: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F970: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F973: 0D 09 20                         ; REGISTER AY0:0D 09 (20)
F976: 4C 20                            ; REGISTER AY0:0C 20 ...
F978: 0D 09 FE                         ; REGISTER AY0:0D 09 (FE)
F97B: 00 00 00                         ; REGISTER AY0:00 00 (00)
F97E: 00 00 FE                         ; REGISTER AY0:00 00 (FE)
F981: 00 00 FE                         ; REGISTER AY0:00 00 (FE)
F984: 67 38                            ; MIXER_OR AY0 00_111_000 ...
F986: FF                               ; STOP

F987: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F9A7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F9C7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
F9E7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA07: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA27: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA47: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA67: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA87: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAA7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAC7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAE7: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

# Start

```code
START: 
;  IRQ2, SWI, and RESET
; 
FB00: 0F          SEI                             ;  Turn interrupts off
FB01: 8E 00 FF    LDS     #$00FF                  ;  Set stack pointer
FB04: BD FC 98    JSR     $FC98                   ;  Clear memory and configure internal ports
FB07: 86 BF       LDA     #$BF                    ;  10_111_111 (no tones, no noise)
FB09: C6 07       LDB     #$07                    ;  Configure I/O and all sound off
FB0B: BD FC D8    JSR     $FCD8                   ;  Write value A to AY register B (no delay during write)
FB0E: 86 13       LDA     #$13                    ;  0001_0011 (Chip status)
FB10: C6 0F       LDB     #$0F                    ;  Ouput port
FB12: BD FC D8    JSR     $FCD8                   ;  Write value A to AY register B (no delay during write)
FB15: BD FC AD    JSR     $FCAD                   ;  Reset all sounds/scripts
FB18: 7F 90 00    CLR     $9000                   ;{-2_WATCHDOG}  ??watchdog??
```

# Sound Loop

```code
SoundLoop: 
;  * Main sound loop
; 
FB1B: 0F          SEI                             ;  Turn interrupts off
FB1C: BD FC 48    JSR     $FC48                   ;  Count down script times and volumes
FB1F: 96 BC       LDA     $BC                     ;{-1_sndCmd}  Sound command read by IRQ1
FB21: 2B 07       BMI     $FB2A                   ;  Nothing to do ... skip

FB23: BD FE E1    JSR     $FEE1                   ;  Handle sound command from main program
FB26: 86 FF       LDA     #$FF                    ;  Command ...
FB28: 97 BC       STA     $BC                     ;{-1_sndCmd}  ... processed

FB2A: 0E          CLI                             ;  Turn interrupts on

FB2B: CE 00 00    LDX     #$0000                  ;  Voice number 0
FB2E: DF D1       STX     $D1                     ;{-1_curVoice}  Start with voice 0
FB30: 96 80       LDA     $80                     ;{-1_seqV0}  Time for voice 0?
FB32: 26 0B       BNE     $FB3F                   ;  No ... move on
FB34: DE 84       LDX     $84                     ;{-1_seqPtr1}  Get sequence 0 pointer
FB36: D6 8C       LDB     $8C                     ;{-1_seq1CmdType}  Command type running on sequencer 0
FB38: BD FD DC    JSR     $FDDC                   ;  Process sequence 0
FB3B: DF 84       STX     $84                     ;{-1_seqPtr1}  Store new sequence pointer
FB3D: 97 80       STA     $80                     ;{-1_seqV0}  Store new countdown timer

FB3F: 7C 00 D2    INC     $00D2                   ;{-1_curVoice}  For Voice 1
FB42: 96 81       LDA     $81                     ;{-1_seqV0}
FB44: 26 0B       BNE     $FB51                   ;
FB46: DE 86       LDX     $86                     ;{-1_seqPtr2}
FB48: D6 8D       LDB     $8D                     ;{-1_seq2CmdType}
FB4A: BD FD DC    JSR     $FDDC                   ;
FB4D: DF 86       STX     $86                     ;{-1_seqPtr2}
FB4F: 97 81       STA     $81                     ;{-1_seqV0}

FB51: 7C 00 D2    INC     $00D2                   ;{-1_curVoice}  For Voice 2
FB54: 96 82       LDA     $82                     ;{-1_seqV0}
FB56: 26 0B       BNE     $FB63                   ;
FB58: DE 88       LDX     $88                     ;{-1_seqPtr3}
FB5A: D6 8E       LDB     $8E                     ;{-1_seq3CmdType}
FB5C: BD FD DC    JSR     $FDDC                   ;
FB5F: DF 88       STX     $88                     ;{-1_seqPtr3}
FB61: 97 82       STA     $82                     ;{-1_seqV0}

FB63: 7C 00 D2    INC     $00D2                   ;{-1_curVoice}  For Voice 3
FB66: 96 83       LDA     $83                     ;{-1_seqV0}
FB68: 26 0B       BNE     $FB75                   ;
FB6A: DE 8A       LDX     $8A                     ;{-1_seqPtr4}
FB6C: D6 8F       LDB     $8F                     ;{-1_seq4CmdType}
FB6E: BD FD DC    JSR     $FDDC                   ;
FB71: DF 8A       STX     $8A                     ;{-1_seqPtr4}
FB73: 97 83       STA     $83                     ;{-1_seqV0}

FB75: 96 A8       LDA     $A8                     ;{-1_volDec00}  Decrement volume 0-0 command
FB77: 27 08       BEQ     $FB81                   ;  Nothing ... skip
FB79: 7F 00 A8    CLR     $00A8                   ;{-1_volDec00}  Command taken
FB7C: C6 08       LDB     #$08                    ;  Decrement volume register 1-0
FB7E: BD FD 3A    JSR     $FD3A                   ;  Do it
FB81: 96 A9       LDA     $A9                     ;{-1_volDec01}  Decrement volume 0-1 command
FB83: 27 08       BEQ     $FB8D                   ;
FB85: 7F 00 A9    CLR     $00A9                   ;{-1_volDec01}
FB88: C6 09       LDB     #$09                    ;
FB8A: BD FD 3A    JSR     $FD3A                   ;
FB8D: 96 AA       LDA     $AA                     ;{-1_volDec02}  Decrement volume 0-2 command
FB8F: 27 08       BEQ     $FB99                   ;
FB91: 7F 00 AA    CLR     $00AA                   ;{-1_volDec02}
FB94: C6 0A       LDB     #$0A                    ;
FB96: BD FD 3A    JSR     $FD3A                   ;
FB99: 96 AB       LDA     $AB                     ;{-1_volDec10}  Decrement volume 1-0 command
FB9B: 27 08       BEQ     $FBA5                   ;
FB9D: 7F 00 AB    CLR     $00AB                   ;{-1_volDec10}
FBA0: C6 18       LDB     #$18                    ;
FBA2: BD FD 53    JSR     $FD53                   ;
FBA5: 96 AC       LDA     $AC                     ;{-1_volDec11}  Decrement volume 1-1 command
FBA7: 27 08       BEQ     $FBB1                   ;
FBA9: 7F 00 AC    CLR     $00AC                   ;{-1_volDec11}
FBAC: C6 19       LDB     #$19                    ;
FBAE: BD FD 53    JSR     $FD53                   ;
FBB1: 96 AD       LDA     $AD                     ;{-1_volDec12}  Decrement volume 1-2 command
FBB3: 27 08       BEQ     $FBBD                   ;
FBB5: 7F 00 AD    CLR     $00AD                   ;{-1_volDec12}
FBB8: C6 1A       LDB     #$1A                    ;
FBBA: BD FD 53    JSR     $FD53                   ;

FBBD: 96 BE       LDA     $BE                     ;{-1_strmStatus}  Status of samplers
FBBF: 16          TAB                             ;  Hold it
FBC0: 9A D8       ORA     $D8                     ;{-1_brdStatus}  OR into board status
FBC2: 0F          SEI                             ;  Disable interrupts
FBC3: 97 D8       STA     $D8                     ;{-1_brdStatus}  New chip status
FBC5: 54          LSRB                            ;  Is sampler 801 done?
FBC6: 24 09       BCC     $FBD1                   ;  No ... let it run
FBC8: D6 CB       LDB     $CB                     ;{-1_lastCmd}  Last sound command
FBCA: C1 02       CMPB    #$02                    ;  Did we finish sound #2 ?
FBCC: 26 03       BNE     $FBD1                   ;  No ... carry on
FBCE: 5C          INCB                            ;  Fall into ...
FBCF: D7 BC       STB     $BC                     ;{-1_sndCmd}  ... Sound command = 3

FBD1: C6 0F       LDB     #$0F                    ;  AY0 Output B
FBD3: BD FC DE    JSR     $FCDE                   ;  Send back board status
FBD6: 7E FB 1B    JMP     $FB1B                   ;{SoundLoop}  Back to top of music loop
```

# NMI Timer

```code
NMITimer: 
; NMI
; Play samples out 801 and 802. On tick ZZZ0000 enable AY sound script processing.
; This clock is driven by the MSM5205 chip requesting data. The MSM5205 is wired
; to pull samples at 4000Hz. This NMI handler runs at 4000Hz.
; 
FBD9: 96 C1       LDA     $C1                     ;{-1_curSamp801}  Current value for 801
FBDB: B7 08 01    STA     $0801                   ;{-2_SAMP_1}  4-bit sample
FBDE: 96 C2       LDA     $C2                     ;{-1_curSamp802}  Current value for 802
FBE0: B7 08 02    STA     $0802                   ;{-2_SAMP_2}  4-bit sample
FBE3: 7C 00 BD    INC     $00BD                   ;{-1_nmiTick}  NMI counter
FBE6: 96 BF       LDA     $BF                     ;{-1_nmiTick2}
FBE8: 4C          INCA                            ;  Why not "INC BF" then "LDA BF" ? ...
FBE9: 97 BF       STA     $BF                     ;{-1_nmiTick2}  ... Same number of bytes!
FBEB: 44          LSRA                            ;  Odd or even?
FBEC: 24 32       BCC     $FC20                   ;  Do this on even ticks

;  Odd NMI ticks
FBEE: DE C3       LDX     $C3                     ;{-1_byteCnt801}  Decrement ...
FBF0: 09          DEX                             ;  ... 801 counter
FBF1: 27 1E       BEQ     $FC11                   ;  All done ... set bit 0 of BE and continue
FBF3: DF C3       STX     $C3                     ;{-1_byteCnt801}  New counter
FBF5: DE C7       LDX     $C7                     ;{-1_ptr801}  Pointer to bytes
FBF7: A6 00       LDA     $00,X                   ;  Get next byte
FBF9: 44          LSRA                            ;  Upper 4 bits
FBFA: 44          LSRA                            ;
FBFB: 44          LSRA                            ;
FBFC: 44          LSRA                            ;
FBFD: 97 C1       STA     $C1                     ;{-1_curSamp801}  Next value for 801

FBFF: DE C5       LDX     $C5                     ;{-1_byteCnt802}  Decrement ...
FC01: 09          DEX                             ;  802 counter
FC02: 27 15       BEQ     $FC19                   ;  All done ... set bit 1 of BE and out
FC04: DF C5       STX     $C5                     ;{-1_byteCnt802}  New counter
FC06: DE C9       LDX     $C9                     ;{-1_ptr802}  Pointer to bytes
FC08: A6 00       LDA     $00,X                   ;  Get next byte
FC0A: 44          LSRA                            ;  Upper 4 bits
FC0B: 44          LSRA                            ;
FC0C: 44          LSRA                            ;
FC0D: 44          LSRA                            ;
FC0E: 97 C2       STA     $C2                     ;{-1_curSamp802}  Next value for 802
FC10: 3B          RTI                             

FC11: 86 01       LDA     #$01                    ;  Set bit 0 ...
FC13: 9A BE       ORA     $BE                     ;{-1_strmStatus}  ... of ...
FC15: 97 BE       STA     $BE                     ;{-1_strmStatus}  ... BE
FC17: 20 E6       BRA     $FBFF                   ;  Continue with bit 1

FC19: 86 02       LDA     #$02                    ;  Set bit 1 ...
FC1B: 9A BE       ORA     $BE                     ;{-1_strmStatus}  ... of ...
FC1D: 97 BE       STA     $BE                     ;{-1_strmStatus}  ... BE
FC1F: 3B          RTI                             ;  NMI out

;  Even NMI ticks
FC20: 96 C7       LDA     $C7                     ;{-1_ptr801}  801 pointer
FC22: 81 A0       CMPA    #$A0                    ;  Pointer less than A0xx? (Hardware supports up to 24K ROM)
FC24: 25 09       BCS     $FC2F                   ;  Yes ... hold last value (Invalid pointer)
FC26: DE C7       LDX     $C7                     ;{-1_ptr801}  801 pointer
FC28: A6 00       LDA     $00,X                   ;  Get value
FC2A: 97 C1       STA     $C1                     ;{-1_curSamp801}  Next value for 801 (lower 4 bits)
FC2C: 08          INX                             ;  Next sample
FC2D: DF C7       STX     $C7                     ;{-1_ptr801}  Save pointer

FC2F: 96 C9       LDA     $C9                     ;{-1_ptr802}  802 pointer
FC31: 81 A0       CMPA    #$A0                    ;  Pointer less than A0xx?
FC33: 25 09       BCS     $FC3E                   ;  Yes ... hold last value
FC35: DE C9       LDX     $C9                     ;{-1_ptr802}  802 pointer
FC37: A6 00       LDA     $00,X                   ;  Get value
FC39: 97 C2       STA     $C2                     ;{-1_curSamp802}  Next value for 802
FC3B: 08          INX                             ;  Next sample
FC3C: DF C9       STX     $C9                     ;{-1_ptr802}  Save pointer

FC3E: 96 BF       LDA     $BF                     ;{-1_nmiTick2}  On tick zzzz0000 ...
FC40: 84 0E       ANDA    #$0E                    ;  ... process AY sound
FC42: 26 CC       BNE     $FC10                   ;  ...
FC44: 7C 00 C0    INC     $00C0                   ;{-1_sndProcTmr}  ...
FC47: 3B          RTI                             ;  NMI out


; The C0 flag gets set by the NMI handler at 4000/16 = 250Hz
;  * If processing sequence scripts, DECrement counters on each voice sequence
;    and lower the volume on the voices as requested.
; 
FC48: 96 C0       LDA     $C0                     ;{-1_sndProcTmr}  Time for scripts?
FC4A: 27 3E       BEQ     $FC8A                   ;  No ... skip
FC4C: 7A 00 C0    DEC     $00C0                   ;{-1_sndProcTmr}  Script pass made
FC4F: 96 80       LDA     $80                     ;{-1_seqV0}  Decrement 80 (voice 0 sequence counter) if active
FC51: 27 06       BEQ     $FC59                   ;  0 ...
FC53: 4C          INCA                            ;  ... or FF ...
FC54: 27 03       BEQ     $FC59                   ;  ... don't DECrement
FC56: 7A 00 80    DEC     $0080                   ;{-1_seqV0}
FC59: 96 81       LDA     $81                     ;{-1_seqV0}  Decrement 81 (voice 1 sequence counter) if active
FC5B: 27 06       BEQ     $FC63                   ;
FC5D: 4C          INCA                            ;
FC5E: 27 03       BEQ     $FC63                   ;
FC60: 7A 00 81    DEC     $0081                   ;{-1_seqV0}
FC63: 96 82       LDA     $82                     ;{-1_seqV0}  Decrement 82 (voice 2 sequence counter) if active
FC65: 27 06       BEQ     $FC6D                   ;
FC67: 4C          INCA                            ;
FC68: 27 03       BEQ     $FC6D                   ;
FC6A: 7A 00 82    DEC     $0082                   ;{-1_seqV0}
FC6D: 96 83       LDA     $83                     ;{-1_seqV0}  Decrement 83 (voice 3 sequence counter) if active
FC6F: 27 06       BEQ     $FC77                   ;
FC71: 4C          INCA                            ;
FC72: 27 03       BEQ     $FC77                   ;
FC74: 7A 00 83    DEC     $0083                   ;{-1_seqV0}
FC77: CE 00 06    LDX     #$0006                  ;  6 voices
FC7A: A6 AD       LDA     $AD,X                   ;  Countdown timer for volume DECrease
FC7C: 27 09       BEQ     $FC87                   ;  Not active ... skip
FC7E: 4A          DECA                            ;  Time to DECrease volume?
FC7F: 26 04       BNE     $FC85                   ;  No ... skip
FC81: 6C A7       INC     $A7,X                   ;  Flag DECrement volume for voice
FC83: A6 B3       LDA     $B3,X                   ;  Restore volume counter
FC85: A7 AD       STA     $AD,X                   ;  Current counter
FC87: 09          DEX                             ;  All voices?
FC88: 26 F0       BNE     $FC7A                   ;  No ... do all
FC8A: 39          RTS                             ;  Done
```

# IRQ1 Command Request

```code
IRQ1CommandRequest: 
; Thanks to Leo Bodnar for explaining the sound-command sequence.
; The main CPU address D000 (write) is connected to the sound CPU's AY0 sound chip general I/O.
; The upper most bit triggers the IRQ on the sound CPU. The main CPU writes the command to D000
; and toggles the upper bit of D000 bit low then high. The sound CPU clears the IRQ by accessing
; memory $9xxx.
;  IRQ1
; 
FC8B: B7 90 00    STA     $9000                   ;{-2_IRQ_ACK}  Release the IRQ line so it can fire again
FC8E: C6 0E       LDB     #$0E                    ;  Read from ...
FC90: BD FD 20    JSR     $FD20                   ;  ... I/O port A on AY chip 0
FC93: 84 1F       ANDA    #$1F                    ;  Only lower 5 bits
FC95: 97 BC       STA     $BC                     ;{-1_sndCmd}  Store sound command
FC97: 3B          RTI                             

FC98: CE FF FF    LDX     #$FFFF                  ;  Set DDR ...
FC9B: DF 00       STX     $00                     ;{-2_DDR1}  ... ports 1 and 2 (outputs)
FC9D: C6 4F       LDB     #$4F                    ;  4F bytes
FC9F: 08          INX                             ;  0
FCA0: 86 00       LDA     #$00                    ;  clear value
FCA2: A7 80       STA     $80,X                   ;  Write byte to memory
FCA4: 08          INX                             ;  Next in memory
FCA5: 5A          DECB                            ;  All bytes
FCA6: 26 FA       BNE     $FCA2                   ;  Do all bytes
FCA8: 86 13       LDA     #$13                    ;  Initial chip status ...
FCAA: 97 D8       STA     $D8                     ;{-1_brdStatus}  ... for return from command
FCAC: 39          RTS                             ;  Done

;  * Disable all sounds
; 
FCAD: BD FC C3    JSR     $FCC3                   ;  All sounds on AY0
FCB0: 86 BF       LDA     #$BF                    ;  10_111_111
FCB2: 97 BB       STA     $BB                     ;{-1_curMix1}  Mixer ... all sounds turned off
FCB4: C6 FF       LDB     #$FF                    ;  FF
;BUG3 {*BUG3}
; What about seqnecer 3? It is tied to AY1 too.
FCB6: D7 82       STB     $82                     ;{-1_seqV0}  Voice sequence 2 off
FCB8: D7 B1       STB     $B1                     ;{-1_volCnt10}  Volume DEC counter AY1-0
FCBA: D7 B2       STB     $B2                     ;{-1_volCnt11}  Volume DEC counter AY1-1
FCBC: D7 B3       STB     $B3                     ;{-1_volCnt12}  Volume DEC counter AY1-2
FCBE: C6 17       LDB     #$17                    ;  10_111_111
FCC0: 7E FC DE    JMP     $FCDE                   ;  Write value A to AY register B
; 
FCC3: 86 BF       LDA     #$BF                    ;  10_111_111
FCC5: 97 BA       STA     $BA                     ;{-1_curMix0}  Mixer ... all sounds turned off
FCC7: C6 FF       LDB     #$FF                    ;  FF
FCC9: D7 80       STB     $80                     ;{-1_seqV0}  Voice sequence 0 off
FCCB: D7 81       STB     $81                     ;{-1_seqV0}  Voice sequence 1 off
FCCD: D7 AE       STB     $AE                     ;{-1_volCnt00}  Volume DEC counter AY0-0
FCCF: D7 AF       STB     $AF                     ;{-1_volCnt01}  Volume DEC counter AY0-1
FCD1: D7 B0       STB     $B0                     ;{-1_volCnt02}  Volume DEC counter AY0-2
FCD3: C6 07       LDB     #$07                    ;  10_111_111 (all channels off)
FCD5: 7E FC DE    JMP     $FCDE                   ;  Write value A to AY register B and return

;  * Write value A to AY register B (no delay during write)
; 
FCD8: 7C 00 BD    INC     $00BD                   ;{-1_nmiTick}  Set NMI counter (bypass waiting)
FCDB: 20 04       BRA     $FCE1                   ;  Continue with write

; * Write value A to AY register B (turn off interrupts)
; 
FCDD: 0F          SEI                             ;  Disable interrupts

; * Write value A to AY register B
; 
FCDE: 7F 00 BD    CLR     $00BD                   ;{-1_nmiTick}  Clear NMI counter
FCE1: 37          PSHB                            ;  Save B ... (address)
FCE2: 36          PSHA                            ;  ... and A  (value)
FCE3: C1 10       CMPB    #$10                    ;  2nd chip?
FCE5: 2A 19       BPL     $FD00                   ;  Yes ... go
FCE7: 86 0D       LDA     #$0D                    ;  0000_1011
FCE9: 97 03       STA     $03                     ;{-2_PORT2}  Control lines
FCEB: D7 02       STB     $02                     ;{-2_PORT1}  Address
FCED: C6 08       LDB     #$08                    ;  0000_1000
FCEF: D7 03       STB     $03                     ;{-2_PORT2}  Control lines
FCF1: 5C          INCB                            ;  Bit 0 on
FCF2: 32          PULA                            ;  Value
FCF3: 97 02       STA     $02                     ;{-2_PORT1}  Write value
FCF5: 96 BD       LDA     $BD                     ;{-1_nmiTick}  Wait ...
FCF7: 27 FC       BEQ     $FCF5                   ;  ... for NMI counter
FCF9: D7 03       STB     $03                     ;{-2_PORT2}  Store control
FCFB: 5A          DECB                            ;  Clear bit 0
FCFC: D7 03       STB     $03                     ;{-2_PORT2}  Store control
FCFE: 33          PULB                            ;  Restore B
FCFF: 39          RTS                             ;  Done
FD00: 86 15       LDA     #$15                    ;  0001_0101
FD02: 97 03       STA     $03                     ;{-2_PORT2}  Control lines
FD04: C4 0F       ANDB    #$0F                    ;  Address 0-15
FD06: D7 02       STB     $02                     ;{-2_PORT1}  Store address
FD08: C6 10       LDB     #$10                    ;  0001_0000
FD0A: 20 E3       BRA     $FCEF                   ;  Write value
FD0C: 37          PSHB                            ;  Chip already selected
FD0D: 20 E4       BRA     $FCF3                   ;  Wrie value to selected chip
FD0F: 37          PSHB                            ;  Save B
FD10: 86 15       LDA     #$15                    ;  0001_0101
FD12: 97 03       STA     $03                     ;{-2_PORT2}  Chip 2 control lines
FD14: C4 0F       ANDB    #$0F                    ;  Address 0-15
FD16: D7 02       STB     $02                     ;{-2_PORT1}  Store address
FD18: C6 14       LDB     #$14                    ;  0001_0100
FD1A: 20 0D       BRA     $FD29                   ;  Continue read

; * Read AY register B into A
; 
FD1C: C1 10       CMPB    #$10                    ;  Second chip?
FD1E: 2A EF       BPL     $FD0F                   ;  Yes ... go handle
FD20: 37          PSHB                            ;  Save B
FD21: 86 0D       LDA     #$0D                    ;  0000_1011
FD23: 97 03       STA     $03                     ;{-2_PORT2}  Chip 1 control lines
FD25: D7 02       STB     $02                     ;{-2_PORT1}  Store address
FD27: C6 0C       LDB     #$0C                    ;  0000_1010
FD29: 4F          CLRA                            ;  0
FD2A: 97 03       STA     $03                     ;{-2_PORT2}  Control lines
FD2C: 97 00       STA     $00                     ;{-2_DDR1}  Port 2 now INPUTS
FD2E: D7 03       STB     $03                     ;{-2_PORT2}  Control lines
FD30: 96 02       LDA     $02                     ;{-2_PORT1}  Read from register
FD32: 5F          CLRB                            ;  0
FD33: D7 03       STB     $03                     ;{-2_PORT2}  Control lines
FD35: 5A          DECB                            ;  FF
FD36: D7 00       STB     $00                     ;{-2_DDR1}  Port 2 now OUTPUTS
FD38: 33          PULB                            ;  Restore B
FD39: 39          RTS                             ;  Done

; * Decrement AY chip 0 volume register B
; 
FD3A: 0F          SEI                             ;  Disable interrupts
FD3B: BD FD 20    JSR     $FD20                   ;  Read from port
FD3E: C6 09       LDB     #$09                    ;  0000_1001 control
FD40: 7F 00 BD    CLR     $00BD                   ;{-1_nmiTick}  Clear NMI counter
FD43: 84 1F       ANDA    #$1F                    ;  Only 5 bits used in volume register
FD45: 81 10       CMPA    #$10                    ;  M bit set? Auto-volume?
FD47: 2A 08       BPL     $FD51                   ;  Yes ... ignore this request
FD49: 4A          DECA                            ;  Decrement the volume
FD4A: 81 07       CMPA    #$07                    ;  Less than 7?
FD4C: 2B 03       BMI     $FD51                   ;  Yes ... low as we get. Ignore
FD4E: BD FD 0C    JSR     $FD0C                   ;  Write the new volume value
FD51: 0E          CLI                             ;  Enable interrupts
FD52: 39          RTS                             ;  Done

; * Decrement AY chip 1 volue register B
; 
FD53: 0F          SEI                             ;  Disable interrupts
FD54: BD FD 0F    JSR     $FD0F                   ;  Read Reg(B)->A
FD57: C6 11       LDB     #$11                    ;  0001_0001 control
FD59: 20 E5       BRA     $FD40                   ;  Continue with write volume value


;  Script command C0 - EF ( 5 or 6 bytes)
FD5B: 17          TBA                             ;  Check lower ...
FD5C: 84 0F       ANDA    #$0F                    ;  ... nibble
FD5E: 81 08       CMPA    #$08                    ;  Greater or equal to 8?
FD60: 2A 08       BPL     $FD6A                   ;{C_SWEEP_VOICE_PAIR}  Yes ... go sweep register-pair
```

# C_SWEEP_VOICE_REGISTER

```code
C_SWEEP_VOICE_REGISTER: 
;  Add delta (I98) to current value (I94) and set-register
;  C0 - EF   110_r_0rrr CNT I94 I98 RVAL   
FD62: A6 94       LDA     $94,X                   ;  Get current tone value
FD64: AB 98       ADDA    $98,X                   ;  Add delta
FD66: A7 94       STA     $94,X                   ;  Store current
FD68: 20 67       BRA     $FDD1                   ;  Write current to register B (0-6) and return 4,x
```

# C_SWEEP_VOICE_PAIR

```code
C_SWEEP_VOICE_PAIR: 
; (Bug in code ... this function is never used)
;  Add delta (DELTA) to fine/coarse pair r0rrr and r0rrr+1. 
;  C0 - EF   110_r_1rrr CNT I94 I98 RVAL DELTA
FD6A: CB 38       ADDB    #$38                    ;  Confusing way of getting rid of bit 3 in register value
FD6C: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Script pointer
FD6E: A6 05       LDA     $05,X                   ;  Delta value from script
FD70: 36          PSHA                            ;  Hold delta (sign-check shortly)
FD71: DE D1       LDX     $D1                     ;{-1_curVoice}  Voice number
FD73: AB 94       ADDA    $94,X                   ;  Adjust ...
FD75: A7 94       STA     $94,X                   ;  ... fine tone value
FD77: 32          PULA                            ;  Original delta
FD78: 2B 0C       BMI     $FD86                   ;  Handle decrementing
FD7A: 24 02       BCC     $FD7E                   ;{BUG1}  No carry
FD7C: 6C 98       INC     $98,X                   ;  Increment coarse tone
```

# BUG 1

```code
BUG1: 
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

FD86: 25 F6       BCS     $FD7E                   ;{BUG1}  Yes carry (we should get a carry until underflow)
FD88: 6A 98       DEC     $98,X                   ;  Decrement coarse value
FD8A: 20 F2       BRA     $FD7E                   ;{BUG1}  Do it

;  Skip over data of current series command and switch to command 0
FD8C: 6F 8C       CLR     $8C,X                   ;  Script command 0
FD8E: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Get the current sequence pointer
FD90: C1 A0       CMPB    #$A0                    ;
FD92: 2B 02       BMI     $FD96                   ;
FD94: 08          INX                             ;  IF B>=A0 ... X=X+2
FD95: 08          INX                             ;
FD96: 08          INX                             ;  X=X+3
FD97: 08          INX                             ;
FD98: 08          INX                             ;
FD99: C1 C0       CMPB    #$C0                    ;
FD9B: 2B 08       BMI     $FDA5                   ;  IF B>=C0 && (A&0F>=8) ... X=X+1
FD9D: 17          TBA                             ;
FD9E: 84 0F       ANDA    #$0F                    ;
FDA0: 81 08       CMPA    #$08                    ;
FDA2: 2B 01       BMI     $FDA5                   ;
FDA4: 08          INX                             ;
FDA5: 86 01       LDA     #$01                    ;  Process again on next sequencer tick
FDA7: 39          RTS                             ;  Done

;  Counted series commands
FDA8: DF CD       STX     $CD                     ;{-1_curSeqPtr}  Hold the pointer
FDAA: DE D1       LDX     $D1                     ;{-1_curVoice}  Get the voice number
FDAC: 6A 90       DEC     $90,X                   ;  All done with this type of command?
FDAE: 27 DC       BEQ     $FD8C                   ;  Yes ... move to next
FDB0: C1 A0       CMPB    #$A0                    ;  Go if ...
FDB2: 2A 10       BPL     $FDC4                   ;  ... A0 or above
```

# C_REGISTER_SAMPLES

```code
C_REGISTER_SAMPLES: 
;  Set the value of rrrrr to sI at regular intervals. CNT is the number of samples.
;  Always return RVAL.
;  80 - 9F   100_r_rrrr CNT RVAL s0 s1 s2 ... sN
FDB4: C4 1F       ANDB    #$1F                    ;  Mask off register number
FDB6: A6 94       LDA     $94,X                   ;  Get return value (time till next process)
FDB8: 36          PSHA                            ;  Hold return
FDB9: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Get back the pointer
FDBB: A6 03       LDA     $03,X                   ;  Get value to write
FDBD: BD FC DD    JSR     $FCDD                   ;  Write value A to AY register B (turn off interrupts)
FDC0: 0E          CLI                             ;  Interrupts back on
FDC1: 32          PULA                            ;  Restore A
FDC2: 08          INX                             ;  Next in sample list
FDC3: 39          RTS                             ;  Out

FDC4: C1 C0       CMPB    #$C0                    ;  Go if ...
FDC6: 2A 93       BPL     $FD5B                   ;  ... C0 or above
```

# C_TOGGLE_REGISTER

```code
C_TOGGLE_REGISTER: 
; (Never used)
;  Alternate writing I94 and I98.
;  Always return RVAL;
;  A0 - BF   101_r_rrrr CNT I94 I98 RVAL
FDC8: A6 90       LDA     $90,X                   ;  Current count of commands
FDCA: 44          LSRA                            ;  Lowest bit
FDCB: A6 94       LDA     $94,X                   ;  Value
FDCD: 25 02       BCS     $FDD1                   ;  Odd ... use value from 94
FDCF: A6 98       LDA     $98,X                   ;  Even ... use value from 98
FDD1: C4 1F       ANDB    #$1F                    ;  Mask off register number
FDD3: BD FC DD    JSR     $FCDD                   ;  Write value A to AY register B (turn off interrupts)
FDD6: 0E          CLI                             ;  Enable interrupts
FDD7: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Restore X
FDD9: A6 04       LDA     $04,X                   ;  Return value (count to next process)
FDDB: 39          RTS                             ;  Out
; 
;  * Process voice sequence. X=script pointer. B is ??process type??
;    Return X=new script pointer, A=count till next process
; 
FDDC: 26 CA       BNE     $FDA8                   ;  Not script command zero

FDDE: DF CD       STX     $CD                     ;{-1_curSeqPtr}  Store new sequence pointer
FDE0: E6 00       LDB     $00,X                   ;  Register number
FDE2: 2A 03       BPL     $FDE7                   ;{SimpleCommands}  Go handle ...
FDE4: 7E FE 93    JMP     $FE93                   ;  ... COMPLEX, STOP, CALL, RETURN
```

# Simple Commands

```code
SimpleCommands: 
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
FDE7: C4 3F       ANDB    #$3F                    ;  Mask off the "multi" bit
FDE9: C1 20       CMPB    #$20                    ;  Is it a single register command?
FDEB: 2A 11       BPL     $FDFE                   ;  No ... go handle 3-voice command

FDED: A6 01       LDA     $01,X                   ;  Get value
FDEF: BD FC DD    JSR     $FCDD                   ;  Write value A to AY register B (turn off interrupts)
FDF2: 0E          CLI                             ;  Interrupts on
FDF3: E6 00       LDB     $00,X                   ;  Restore register value
FDF5: 08          INX                             ;  Skip ...
FDF6: 08          INX                             ;  ... two byte command
FDF7: 58          ASLB                            ;  Repeat bit set?
FDF8: 2B E4       BMI     $FDDE                   ;  Yes ... do another
FDFA: A6 00       LDA     $00,X                   ;  Get return value
FDFC: 08          INX                             ;  Point to next command
FDFD: 39          RTS                             ;  Out

FDFE: C4 1F       ANDB    #$1F                    ;  Register value (0,16 or mixer)
FE00: 17          TBA                             ;  To A
FE01: 84 0F       ANDA    #$0F                    ;  Is it a valid chip register 0 (0 or 16)
FE03: 26 31       BNE     $FE36                   ;  No ... MIXER or VOLUME
;  3-tone note
FE05: A6 01       LDA     $01,X                   ;  Get the fine tone
FE07: 97 CE       STA     $CE                     ;{-1_curSeqPtr}  Store it
FE09: A6 02       LDA     $02,X                   ;  Get the coarse tone
FE0B: 97 CD       STA     $CD                     ;{-1_curSeqPtr}  Store it
FE0D: BD FE D4    JSR     $FED4                   ;  Write channel A tone
FE10: DC CD       LDD     $CD                     ;{-1_curSeqPtr}  CE,CD ...
FE12: 04          LSRD                            ;  ... divided by ...
FE13: DD CD       STD     $CD                     ;{-1_curSeqPtr}  ... 2
FE15: E6 00       LDB     $00,X                   ;  Original ...
FE17: C4 1F       ANDB    #$1F                    ;  ... register
FE19: 5C          INCB                            ;  Next ...
FE1A: 5C          INCB                            ;  ... pair
FE1B: BD FE D4    JSR     $FED4                   ;  Write channel B tone
FE1E: 7C 00 CE    INC     $00CE                   ;{-1_curSeqPtr}  Increment ...
FE21: 26 03       BNE     $FE26                   ;  ... word in ...
FE23: 7C 00 CD    INC     $00CD                   ;{-1_curSeqPtr}  ... CE, CD
FE26: BD FE D4    JSR     $FED4                   ;  Write channel C tone
FE29: CB 07       ADDB    #$07                    ;  Envelope shape register
FE2B: 86 09       LDA     #$09                    ;  Envelope shape cycle (CONT+HOLD)
FE2D: BD FC DE    JSR     $FCDE                   ;  Write envelope shape
FE30: 0E          CLI                             ;  Interrupts on
FE31: E6 00       LDB     $00,X                   ;  Restore command (for repeats)
FE33: 08          INX                             ;  Skip extra byte
FE34: 20 BF       BRA     $FDF5                   ;  Skip 2 bytes and done

FE36: 80 08       SUBA    #$08                    ;  <8
FE38: 2B 29       BMI     $FE63                   ;  Yes ... go to mixer command
;  Volume control
FE3A: DD CF       STD     $CF                     ;{-1_tmpFreq}  Hold n&1F and (n&0F-8)
FE3C: 84 03       ANDA    #$03                    ;  Complex encoding ...
FE3E: C1 30       CMPB    #$30                    ;  ... for ...
FE40: 2B 02       BMI     $FE44                   ;  ... sequencer ...
FE42: 8B 03       ADDA    #$03                    ;  ... number
FE44: 16          TAB                             ;  Sequencer number to B
FE45: A6 01       LDA     $01,X                   ;  Get value
FE47: CE 00 00    LDX     #$0000                  ;  Sequence number ...
FE4A: 3A          ABX                             ;  ... to X
FE4B: D6 CF       LDB     $CF                     ;{-1_tmpFreq}  Original A (remember already-8)
FE4D: C1 04       CMPB    #$04                    ;  Set counter?
FE4F: 2A 0B       BPL     $FE5C                   ;  Yes ... go set counter
;  Reset volume dec counter and actual volume volume
FE51: A6 B4       LDA     $B4,X                   ;  Get counter reload for volume on voice
FE53: A7 AE       STA     $AE,X                   ;  Reset volume DEC counter
FE55: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Restore script pointer
FE57: D6 D0       LDB     $D0                     ;{-1_tmpFreq}  Original B (register)
FE59: 7E FD ED    JMP     $FDED                   ;  Write from script to register and continue script
;  Set countreload for volume
FE5C: A7 B4       STA     $B4,X                   ;  Counter reload for volume DEC on voice
FE5E: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Restore script pointer
FE60: 7E FD F3    JMP     $FDF3                   ;  Continue script

;  Mixer control (AND or OR)
FE63: 4C          INCA                            ;  FF = OR bits in mixer value
FE64: 27 17       BEQ     $FE7D                   ;  Go OR
FE66: 5C          INCB                            ;  6 becomes 7 ... mixer register
FE67: C1 10       CMPB    #$10                    ;  AY1 chip?
FE69: 2A 09       BPL     $FE74                   ;  Yes ... go
FE6B: 96 BA       LDA     $BA                     ;{-1_curMix0}  Mixer value for AY0
FE6D: A4 01       ANDA    $01,X                   ;  Turn bits off
FE6F: 97 BA       STA     $BA                     ;{-1_curMix0}  New value
FE71: 7E FD EF    JMP     $FDEF                   ;  Write mixer and continue script
; 
FE74: 96 BB       LDA     $BB                     ;{-1_curMix1}  Mixer value for AY1
FE76: A4 01       ANDA    $01,X                   ;  Turn bits off
FE78: 97 BB       STA     $BB                     ;{-1_curMix1}  New value
FE7A: 7E FD EF    JMP     $FDEF                   ;  Write mixer and continue script
; 
FE7D: C1 10       CMPB    #$10                    ;  AY1 chip?
FE7F: 2A 09       BPL     $FE8A                   ;  Yes ... go
FE81: 96 BA       LDA     $BA                     ;{-1_curMix0}  Mixer value for AY0
FE83: AA 01       ORA     $01,X                   ;  Turn bits on
FE85: 97 BA       STA     $BA                     ;{-1_curMix0}  New value
FE87: 7E FD EF    JMP     $FDEF                   ;  Write mixer and continue script
; 
FE8A: 96 BB       LDA     $BB                     ;{-1_curMix1}  Mixer value for AY1
FE8C: AA 01       ORA     $01,X                   ;  Turn bits on
FE8E: 97 BB       STA     $BB                     ;{-1_curMix1}  New value
FE90: 7E FD EF    JMP     $FDEF                   ;  Write mixer and continue script

FE93: C1 F0       CMPB    #$F0                    ;  STOP or CALL or RETURN ?
FE95: 2A 17       BPL     $FEAE                   ;  Yes ... go handle

;  Start new series of commands
;  1ccccccc AA BB CC  c->commandType    (AA+1)->seriesCount    94,X<-BB     98,X<-CC
FE97: A6 01       LDA     $01,X                   ;  Get ...
FE99: EE 02       LDX     $02,X                   ;  ... params for series
FE9B: 3C          PSHX                            ;  Hold
FE9C: DE D1       LDX     $D1                     ;{-1_curVoice}  Current sequencer
FE9E: E7 8C       STB     $8C,X                   ;  Store series type
FEA0: 4C          INCA                            ;  Series count (always +1)
FEA1: A7 90       STA     $90,X                   ;
FEA3: 32          PULA                            ;  Store ...
FEA4: A7 94       STA     $94,X                   ;  ... series ...
FEA6: 32          PULA                            ;  ... parameters
FEA7: A7 98       STA     $98,X                   ;
FEA9: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Restore script pointer
FEAB: 86 01       LDA     #$01                    ;  Process again next tick
FEAD: 39          RTS                             ;  Done

FEAE: 5C          INCB                            ;  FF=STOP?
FEAF: 27 12       BEQ     $FEC3                   ;{STOP}  Yes ... return FF.
FEB1: DE D1       LDX     $D1                     ;{-1_curVoice}  Voice number
FEB3: 5C          INCB                            ;  FE=CALL?
FEB4: 26 10       BNE     $FEC6                   ;{RETURN}  No ... process return
```

# CALL

```code
CALL: 
;  FE MM LL  - CALL MMLL 
FEB6: DC CD       LDD     $CD                     ;{-1_curSeqPtr}  Sequence pointer
FEB8: A7 9C       STA     $9C,X                   ;  Store ...
FEBA: E7 A0       STB     $A0,X                   ;  ... return LSB and MSB
FEBC: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Sequence pointer
FEBE: EE 01       LDX     $01,X                   ;  Get jump address
FEC0: 86 01       LDA     #$01                    ;  Return 1 (processes again next step)
FEC2: 39          RTS                             ;  Done
```

# STOP

```code
STOP: 
;  FF        - STOP  
FEC3: 86 FF       LDA     #$FF                    ;  END OF SEQUENCE
FEC5: 39          RTS                             ;  Done
```

# RETURN

```code
RETURN: 
;  F0-FD     - RETURN
FEC6: A6 9C       LDA     $9C,X                   ;  Restore ..
FEC8: E6 A0       LDB     $A0,X                   ;  ... sequence ...
FECA: DD CD       STD     $CD                     ;{-1_curSeqPtr}  ... pointer
FECC: DE CD       LDX     $CD                     ;{-1_curSeqPtr}  Sequence pointer
FECE: 08          INX                             ;  Skip over ...
FECF: 08          INX                             ;  ... CALL ...
FED0: 08          INX                             ;  ... command
FED1: 86 01       LDA     #$01                    ;  Return 1 (processes again next step)
FED3: 39          RTS                             ;  Done

;  Write CE to consecutive registers pointed to by B
;  Leave with B pointing to next register.
; 
FED4: 96 CE       LDA     $CE                     ;{-1_curSeqPtr}  Fine value
FED6: BD FC DD    JSR     $FCDD                   ;  Write value A to AY register B (turn off interrupts)
FED9: 5C          INCB                            ;  Coarse register
FEDA: 96 CD       LDA     $CD                     ;{-1_curSeqPtr}  Coarse value
FEDC: BD FC DE    JSR     $FCDE                   ;  Write value A to AY register B
FEDF: 5C          INCB                            ;  Next register
FEE0: 39          RTS                             ;  Done


; ALL sound command start here
; 
FEE1: 26 06       BNE     $FEE9                   ;  Zero means ...
```

# Process Command 0

```code
ProcessCommand0: 
; Sound command $00
; Reinitialize RAM and disable all sounds
FEE3: BD FC 98    JSR     $FC98                   ;  ... reinit RAM and hardware
FEE6: 7E FC AD    JMP     $FCAD                   ;  Disable all scripts/sounds and return

FEE9: 81 10       CMPA    #$10                    ;  Vector to ...
FEEB: 2B 03       BMI     $FEF0                   ;{ProcessCommands01-0F}  ... 01-0F or ...
FEED: 7E FF 25    JMP     $FF25                   ;  ... 10-1F
```

# Process Commands 01 - 0F

```code
ProcessCommands01-0F: 
; Sound commands $01 - $0F (samplers played out 801)
FEF0: 97 CB       STA     $CB                     ;{-1_lastCmd}  Hold command
FEF2: 96 D8       LDA     $D8                     ;{-1_brdStatus}  Get chip status
FEF4: 8A 01       ORA     #$01                    ;  Set bit 0 in A
FEF6: 16          TAB                             ;  To B
FEF7: C4 FE       ANDB    #$FE                    ;  Clear bit 0 in B
FEF9: D7 D8       STB     $D8                     ;{-1_brdStatus}  Store value back with bit 0 clear
FEFB: C6 0F       LDB     #$0F                    ;  AY I/O register chip 0 B
FEFD: BD FC DE    JSR     $FCDE                   ;  Write value D8 with bit 0 set to output port
FF00: 86 05       LDA     #$05                    ;  Wait for 5 NMI counts
FF02: 7F 00 BD    CLR     $00BD                   ;{-1_nmiTick}  Clear NMI counter
FF05: D6 BD       LDB     $BD                     ;{-1_nmiTick}  Wait on ...
FF07: 27 FC       BEQ     $FF05                   ;  ... NMI counter ...
FF09: 4A          DECA                            ;  Wait for ...
FF0A: 26 F6       BNE     $FF02                   ;  ... specified time
FF0C: D6 CB       LDB     $CB                     ;{-1_lastCmd}  Command ...
FF0E: 58          ASLB                            ;  ... times ...
FF0F: 58          ASLB                            ;  .... 4
FF10: CE F4 00    LDX     #$F400                  ;  Sample table
FF13: 3A          ABX                             ;  Offset in table
FF14: 3C          PSHX                            ;  Remember the offset
FF15: EE 00       LDX     $00,X                   ;  Wouldn't it be great to have a Y register?
FF17: DF C7       STX     $C7                     ;{-1_ptr801}  Sample pointer
FF19: 38          PULX                            ;  Descriptor
FF1A: EE 02       LDX     $02,X                   ;  Get ...
FF1C: DF C3       STX     $C3                     ;{-1_byteCnt801}  ... number of samples
FF1E: 96 BE       LDA     $BE                     ;{-1_strmStatus}  Enable sample ...
FF20: 84 02       ANDA    #$02                    ;  ... player ...
FF22: 97 BE       STA     $BE                     ;{-1_strmStatus}  ... on 801
FF24: 39          RTS                             ;  Done

FF25: 16          TAB                             ;  Script number
FF26: 58          ASLB                            ;  *2
FF27: CE F4 24    LDX     #$F424                  ;  Script pointer table ($10 -> $F444)
FF2A: 3A          ABX                             ;  Offset to start of script
FF2B: EE 00       LDX     $00,X                   ;  Script start
FF2D: 81 14       CMPA    #$14                    ;  $10 - $14
FF2F: 2A 1C       BPL     $FF4D                   ;  $14 or above ... go
```

# Process Commands 10 - 13

```code
ProcessCommands10-13: 
; Commands $10, $11, $12, $13
; Start script in mode 0 on sequencer 2 if available
FF31: D6 82       LDB     $82                     ;{-1_seqV0}  Is sequencer 2 ...
FF33: 5C          INCB                            ;  ... available?
FF34: 27 06       BEQ     $FF3C                   ;  Yes ... use sequencer 2
FF36: 91 A6       CMPA    $A6                     ;{-1_cmdSeq3}  Already running on sequencer 2?
FF38: 27 02       BEQ     $FF3C                   ;  Yes ... restart sequencer 2
FF3A: 2A 10       BPL     $FF4C                   ;  Higher priority command running (lower number)? Ignore.
FF3C: 97 A6       STA     $A6                     ;{-1_cmdSeq3}  Sound command for sequence 2
FF3E: DF 88       STX     $88                     ;{-1_seqPtr3}  Script pointer for sequence 2
FF40: 7F 00 82    CLR     $0082                   ;{-1_seqV0}  Process seqence 2 next tick
FF43: 7F 00 8E    CLR     $008E                   ;{-1_seq3CmdType}  Mode 0 for sequencer 2
FF46: C6 89       LDB     #$89                    ;  10_001_001
FF48: DA BB       ORB     $BB                     ;{-1_curMix1}  Sequencer tied to voice A ...
FF4A: D7 BB       STB     $BB                     ;{-1_curMix1}  ... turn it off (for now)
FF4C: 39          RTS                             

FF4D: 26 11       BNE     $FF60                   ;  Go if not exactly $14
```

# Process Command 14

```code
ProcessCommand14: 
; Command $14
; Force script in mode 0 on seqencer 3 no matter what
FF4F: DF 8A       STX     $8A                     ;{-1_seqPtr4}  Script pointer for sequence 3
FF51: 97 A7       STA     $A7                     ;{-1_cmdSeq4}  Sound command for sequencer 3
FF53: 7F 00 83    CLR     $0083                   ;{-1_seqV0}  Process sequence 3 next tick
FF56: 7F 00 8F    CLR     $008F                   ;{-1_seq4CmdType}  Mode 0 for sequencer 3
FF59: 86 B6       LDA     #$B6                    ;  10_110_110
FF5B: 9A BB       ORA     $BB                     ;{-1_curMix1}  Sequencer 3 tied to voice BC ...
FF5D: 97 BB       STA     $BB                     ;{-1_curMix1}  ... turn them off (for now)
FF5F: 39          RTS                             

FF60: 81 18       CMPA    #$18                    ;  $18 or above?
FF62: 2A 0B       BPL     $FF6F                   ;{ProcessCommands18-1F}  Yes ...
```

# Process Commands 15 - 17

```code
ProcessCommands15-17: 
; Command $15, $16, $17
; For script in mode 0 on sequencer 1 no matter what
FF64: DF 86       STX     $86                     ;{-1_seqPtr2}  Script pointer for sequencer 1
FF66: 97 A5       STA     $A5                     ;{-1_cmdSeq2}  Sound command for sequencer 1
FF68: 7F 00 81    CLR     $0081                   ;{-1_seqV0}  Process sequence 1 next tick
FF6B: 7F 00 8D    CLR     $008D                   ;{-1_seq2CmdType}  Mode 0 for sequencer 1
FF6E: 39          RTS                             ;  Done
```

# Process Commands 18 - 1F

```code
ProcessCommands18-1F: 
; Command $18, 19, 1A, 1B, 1C, 1D, 1E, 1F
; Turn off all sounds and start command/script A/X on sequencer 0
FF6F: 3C          PSHX                            ;  Hold script pointer
FF70: 36          PSHA                            ;  Hold sound command
FF71: BD FC 98    JSR     $FC98                   ;  Initialize RAM and hardware
FF74: BD FC AD    JSR     $FCAD                   ;  Stop all sounds
FF77: 32          PULA                            ;  Restore sound command
FF78: 38          PULX                            ;  Restore script pointer
FF79: DF 84       STX     $84                     ;{-1_seqPtr1}  Script pointer for sequencer 0
FF7B: 97 A4       STA     $A4                     ;{-1_cmdSeq1}  Sound command for sequencer 0
FF7D: 7F 00 80    CLR     $0080                   ;{-1_seqV0}  Process sequence 0 next tick
FF80: 7F 00 8C    CLR     $008C                   ;{-1_seq1CmdType}  Force 0 sequencer 0
FF83: 86 BE       LDA     #$BE                    ;  10_111_110
```

# BUG 2

```code
BUG2: 
; The initialization at FCAD sets BA to 10_111_111. The OR here with a 0 is pointless.
FF85: 9A BA       ORA     $BA                     ;{-1_curMix0}  Flag off all but ...
FF87: 97 BA       STA     $BA                     ;{-1_curMix0}  ... AY0 tone A (THIS DOESN'T REALLY DO ANYTHING)
FF89: 39          RTS                             ;  Done

FF8A: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFAA: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFCA: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FFEA: 00 00 00 00 00 00
```

# Vectors

```code
Vectors: 
; Vectors
FFF0: FB 00                            ;  IRQ2 Serial I/O vector
FFF2: FB 00                            ;  IRQ2 timer overflow vector
FFF4: FB 00                            ;  IRQ2 timer output capture vector
FFF6: FB 00                            ;  IRQ2 timer input capture vector
FFF8: FC 8B                            ;  IRQ1 interrupt strobe 3 vector
FFFA: FB 00                            ;  SWI vector
FFFC: FB D9                            ;  Non-maskable (NMI) vector
FFFE: FB 00                            ;  RESET vector
```
