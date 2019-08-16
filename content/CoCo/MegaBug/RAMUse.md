![RAM](megabug.jpg)

# Game variables DP=??

>>> memory
| | | |
| ---   | --- | --- |
| AB:AC |  | |
| AD | | |
| AE | | |
| 92    | RequestedPage | Upper byte of address of visible screen page (04 or ??) |
| 9A:9B | ?ScreenPointerA | |
| 9C:9D | ?ScreenPointerB | |
| C5    | ??AtBoot??    | set to 8 normally or $10 if ENTER pressed at start |
| C7    | VisiblePage   | Upper byte of address of visible screen page (04 or ??) |

Graphics pages (3K each)
 - 0400 - 0FFF
 - 1000 - 1BFF
 - 1C00 - 27FF