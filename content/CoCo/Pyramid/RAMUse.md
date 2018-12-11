
![RAM](Pyramid.jpg)

# Pyramid RAM Use

# Variables Kept Outside of Code (Not Saved)

> memory

| | | |
| --- | --- | --- |
| 007C      | m007C                | |
| 007D      | m007D                | |
| 007E      | m007E                | |
| 0088:0089 | cursor               | Screen cursor used by BASIC routines |
| 01B0      | m01B0                | |
| 01B1      | m01B1                | |
| 01B2      | m01B2                | |
| 01B3      | m01B3                | |
| 01B4      | m01B4                | |
| 01B5      | m01B5                | |
| 01B6      | m01B6                | |
| 01B7      | m01B7                | |
| 01B8      | m01B8                | |
| 01B9      | m01B9                | |
| 01BA      | m01BA                | |
| 01BB      | m01BB                | |
| 01BC      | m01BC                | |
| 01BD      | m01BD                | |
| 01BE      | m01BE                | |
| 01BF      | m01BF                | |
| 01C0      | m01C0                | |
| 01C1      | m01C1                | |
| 01C2      | m01C2                | |
| 01C3      | m01C3                | |
| 01C4      | m01C4                | |
| 01C5      | m01C5                | |
| 01C6      | m01C6                | |
| 01C7      | m01C7                | |
| 01C8      | m01C8                | |
| 01C9      | m01C9                | |
| 01CA      | m01CA                | |
| 01CB      | m01CB                | |
| 01CC      | m01CC                | |
| 01CD      | m01CD                | |
| 01CE      | m01CE                | |
| 01CF      | m01CF                | |
| 01D0      | m01D0                | |
| 01D1      | m01D1                | |
| 01D2      | m01D2                | |
| 01D3      | m01D3                | |
| 01D4      | m01D4                | |
| 01D5      | m01D5                | |
| 01D6      | m01D6                | |
| 01D7      | m01D7                | |
| 01D8      | m01D8                | |
| 01D9      | m01D9                | |
| 01DA      | m01DA                | |
| 01DB      | m01DB                | |
| 01DC      | m01DC                | |
| 01DD      | m01DD                | |
| 01DE      | m01DE                | |
| 01DF      | m01DF                | |
| 01E0      | m01E0                | |
| 01E1      | m01E1                | |
| 01E2      | m01E2                | |
| 01E3      | m01E3                | |
| 01E4      | m01E4                | |
| 01E5      | m01E5                | |
| 01E6      | m01E6                | |
| 01E7      | m01E7                | |
| 01E8      | m01E8                | |
| 01E9      | m01E9                | |
| 01EA      | m01EA                | |
| 01EB      | m01EB                | |
| 01EC      | m01EC                | |
| 01ED      | m01ED                | |
| 01EE      | m01EE                | |
| 01EF      | m01EF                | |
| 01F0      | m01F0                | |
| 01F2      | m01F2                | |
| 01F4      | m01F4                | |
| 01F8      | m01F8                | |
| 01FD      | m01FD                | |
| 01FE      | m01FE                | |
| 01FF      | m01FF                | |
| 0200      | m0200                | |
| 0201      | m0201                | |
| 0202      | m0202                | |
| 0203      | m0203                | |
| 0207      | m0207                | |
| 0208      | m0208                | |
| 0209      | m0209                | |

The game uses 65 bytes of memory in low memory beginning at 0x01B0 for temporaries.
These temporaries are NOT persisted in a SAVE.

# Variables Kept in the Code (Saved)

> memory

| | | | |
| --- | --- | --- |
| 18E5      | curRoom              | 01 RoomNumber (starts in 1) |
| 18E6      | turnsMSB             | 00 TurnCountMSB (BCD format) |
| 18E7      | turnsLSB             | 00 TurnCountLSB (BCD format) |
| 18E8      | lampTime             | 00 LampTime |
| 18E9      | m18E9                | 00 * NOT USED * |
| 18EA      | lastRoom             | 00 LastRoomNumber |
| 18EB      | numInPack            | 00 NumInPack |
| 18EC      | m18EC                | 00 * NOT USED * |

 
