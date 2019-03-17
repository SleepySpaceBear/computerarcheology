![Frogger Sound Board RAM Use](Frogger.jpg)

# Sound RAM

>>> memory

| | | |
| --- | --- | --- |
| 403F     | loopCount        | incremented with each main loop (never used) |
| 4040     | v1Command        | voice 1 command (0 for none) |
| 4041     | v1Init           | voice 1 init flag (0 for needs-init) |
| 4042     | v2Command        | voice 2 command (0 for none) |
| 4043     | v2Init           | voice 2 init flag (0 for needs-init) |
| 4044     | v3Command        | voice 3 command (0 for none) |
| 4045     | v3Init           | voice 3 init flag (0 for needs-init) |
| 4046     | cmdRequest       | requested command temporary for request processing |
| 4047     | m4047                 | never referenced |
| 4048     | m4048                 | never referenced |
| 4049     | v3priority       | voice 3 priority temporary for request processing |
| 404A     | m404A                 | never referenced |
| 404B     | voiceNum         | voice number (1,2, or 3) |
| 404C     | curEnable        | current value of the AY enable register |
| 404D     | m404D                 | never referenced |
| 404E     | curFilter        | current value of capacitor filters |
| 405D     | m405D                 | |
| 405E     | m405E                 | |
| 4064     | m4064                 | |
| 4065     | m4065                 | |
| 4067     | m4067                 | |
| 4110     | m4110                 | |
| 4113     | m4113                 | |
| 4130     | m4130                 | |
| 4170     | m4170                | |
| 4171     | m4171                 | |
| 4172     | m4172                 | |
| 4173     | m4173              | |
| 4175     | m4175                 | |
| 4176     | m4176                 | |
| 4178     | m4178                 | |
| 4180     | m4180                 | |
| 4182     | m4182                 | |
| 4184     | m4184                 | |
| 41E4     | m41E4                 | |
| 41E5     | m41E5                 | |
| 41E7     | m41E7                 | |
| 4280     | m4280                 | set to 43 at start up (stack at 4044) | 
| 42A2     | m42A2                 | |
| 42A3     | m42A3                 | |
| 42A5     | m42A5                 | |
| 42A6     | m42A6                 | |
| 42B2     | m42B2                 | |
| 42C2     | m42C2                 | |
| 42C3     | m42C3                 | |
| 42C4     | m42C4                 | |
| 42C5     | m42C5                 | |
| 42C8     | m42C8                 | |

Stack pointer is initialized to 4400. It builds down from there.
