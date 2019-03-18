![Space Invaders RAM](SpaceInvaders.jpg)

# RAM Usage

>>> memory

| | | |
| --- | --- | --- |
|2000|waitOnDraw|Cleared by alien-draw and set by next-alien. This ensures no alien gets missed while drawing.|
|2001| | |
|2002|alienIsExploding|Not-0 if an alien is exploding, 0 if not exploting|
|2003|expAlienTimer|Time (ISR ticks) left in alien-explosion|
|2004|alienRow|Row number of current alien (cursor)|
|2005|alienFrame|Animation frame number (0 or 1) for current alien (cursor)|
|2006|alienCurIndex|Alien cursor index (from 0 to 54)|
|2007|refAlienDYr|Reference alien delta Yr|
|2008|refAlienDXr|Reference alien deltaXr|
|2009|refAlienYr|Reference alien Yr coordinate|
|200A|refAlienXr|Reference alien Xr coordinate|
|200B|alienPosLSB|Alien cursor bit pos (LSB)|
|200C|alienPosMSB|Alien cursor bit pos (MSB)|
|200D|rackDirection|Value 0 if rack is moving right or 1 if rack is moving left|
|200E|rackDownDelta|Constant value of alien rack dropping after bumping screen edge|
|200F| | |
|2010|obj0TimerMSB| |
|2011|obj0TimerLSB|Wait 128 interrupts (about 2 secs) before player task starts|
|2012|obj0TimerExtra| |
|2013|obj0HanlderLSB| |
|2014|oBJ0HanlderMSB|Player handler code at 028E|
|2015|playerAlive|Player is alive (FF=alive). Toggles between 0 and 1 for blow-up images.|
|2016|expAnimateTimer|Time till next blow-up sprite change (reloaded to 5)|
|2017|expAnimateCnt|Number of changes left in blow-up sequence|
|2018|plyrSprPicL|Player sprite descriptor ... picture LSB|
|2019|plyrSprPicM|Player sprite descriptor ... picture MSB|
|201A|playerYr|Player sprite descriptor ... location LSB|
|201B|playerXr|Player sprite descriptor ... location MSB|
|201C|plyrSprSiz|Player sprite descriptor ... size of sprite|
|201D|nextDemoCmd|Next movement command for demo|
|201E|hidMessSeq|Set to 1 after 1st of 2 sequences are entered for hidden-message display|
|201F| |Appears to be unused|
|2020|obj1TimerMSB| |
|2021|obj1TimerLSB| |
|2022|obj1TimerExtra|All 0's ... run immediately|
|2023|obj1HandlerLSB| |
|2024|obj1HandlerMSB|Shot handler code at 03BB|
|2025|plyrShotStatus|0 if available, 1 if just initiated, 2 moving normally, 3 hit something besides alien, 5 if alien explosion is in progress, 4 if alien has exploded (remove from active duty)|
|2026|blowUpTimer|Sprite blow-up timer|
|2027|obj1ImageLSB| |
|2028|obj1ImageMSB|Sprite image at 1C90 (just one byte)|
|2029|obj1CoorYr|Player shot Y coordinate|
|202A|obj1CoorXr|Player shot X coordinate|
|202B|obj1ImageSize|Size of shot image (just one byte)|
|202C|shotDeltaX|Shot's delta X|
|202D|fireBounce|1 if button has been handled but remains down|
|202E| | |
|202F| | |
|2030|obj2TimerMSB| |
|2031|obj2TimerLSB| |
|2032|obj2TimerExtra|GO-3 runs when this is 1. GO-4 runs when this is 2. (copied to 2080 in game loop)|
|2033|obj2HandlerLSB| |
|2034|obj2HandlerMSB|Handler code at 0476|
|2035|rolShotStatus| |
|2036|rolShotStepCnt| |
|2037|rolShotTrack|A 0 means this shot tracks the player|
|2038|rolShotCFirLSB|Pointer to column-firing table LSB (not used for targeting)|
|2039|rolShotCFirMSB|Pointer to column-firing table MSB (not used for MSB counter|
|203A|rolShotBlowCnt| |
|203B|rolShotImageLSB| |
|203C|rolShotImageMSB| |
|203D|rolShotYr| |
|203E|rolShotXr| |
|203F|rolShotSize| |
|2040|obj3TimerMSB| |
|2041|obj3TimerLSB| |
|2042|obj3TimerExtra| |
|2043|obj3HandlerLSB| |
|2044|obj3HandlerMSB|Handler code at 04B6|
|2045|pluShotStatus| |
|2046|pluShotStepCnt| |
|2047|pluShotTrack|A 1 means this shot does not track the player|
|2048|pluShotCFirLSB|Pointer to column-firing table LSB|
|2049|pluShotCFirMSB|Pointer to column-firing table MSB|
|204A|pluShotBlowCnt| |
|204B|pluShotImageLSB| |
|204C|pluShotImageMSB| |
|204D|pluShotYr| |
|204E|pluSHotXr| |
|204F|pluShotSize| |
|2050|obj4TimerMSB| |
|2051|obj4TimerLSB| |
|2052|obj4TimerExtra| |
|2053|obj4HandlerLSB| |
|2054|obj4HandlerMSB|Handler code at 0682|
|2055|squShotStatus| |
|2056|squShotStepCnt| |
|2057|squShotTrack|A 1 means this shot does not track the player|
|2058|squShotCFirLSB|Pointer to column-firing table LSB|
|2059|squShotCFirMSB|Pointer to column-firing table MSB|
|205A|squSHotBlowCnt| |
|205B|squShotImageLSB| |
|205C|squShotImageMSB| |
|205D|squShotYr| |
|205E|squShotXr| |
|205F|squShotSize| |
|2060|endOfTasks|FF marks the end of the tasks list|
|2061|collision|Set to 1 if sprite-draw detects collision|
|2062|expAlienLSB| |
|2063|expAlienMSB|Exploding alien picture 1CC0|
|2064|expAlienYr|Y coordinate of exploding alien|
|2065|expAlienXr|X coordinate of exploding alien|
|2066|expAlienSize|Size of exploding alien sprite (16 bytes)|
|2067|playerDataMSB|Current player's data-pointer MSB (21xx or 22xx)|
|2068|playerOK|1 means OK, 0 means blowing up|
|2069|enableAlienFire|1 means aliens can fire, 0 means not|
|206A|alienFireDelay|Count down till aliens can fire (2069 flag is then set)|
|206B|oneAlien|1 when only one alien is on screen|
|206C|temp206C|Holds the value ten ... number of characters in each "=xx POINTS" string but gets set to 18 in mem copy before game.|
|206D|invaded|Set to 1 when player blows up because rack has reached bottom|
|206E|skipPlunger|When there is only one alien left this goes to 1 to disable the plunger-shot when it ends|
|206F| | |
|2070|otherShot1|When processing a shot, this holds one of the other shot's info|
|2071|otherShot2|When processing a shot, this holds one of the other shot's info|
|2072|vblankStatus|80=screen is being drawn (don't touch), 0=blanking in progress (ok to change)|
|2073|aShotStatus|Bit 0 set if shot is blowing up, bit 7 set if active|
|2074|aShotStepCnt|Count of steps made by shot (used for fire reload rate)|
|2075|aShotTrack|0 if shot tracks player or 1 if it uses the column-fire table|
|2076|aShotCFirLSB|Pointer to column-firing table LSB|
|2077|aShotCFirMSB|Pointer to column-firing table MSB|
|2078|aShotBlowCnt|Alen shot blow up counter. At 3 the explosion is drawn. At 0 it is done.|
|2079|aShotImageLSB|Alien shot image LSB|
|207A|aShotImageMSB|Alien shot image MSB|
|207B|alienShotYr|Alien shot delta Y|
|207C|alienShotXr|Alien shot delta X|
|207D|alienShotSize|Alien shot size|
|207E|alienShotDelta|Alien shot speed. Normally -1 but set to -4 with less than 9 aliens|
|207F|shotPicEnd|the last picture in the current alien shot animation|
|2080|shotSync|All 3 shots are synchronized to the GO-2 timer. This is copied from timer in the game loop|
|2081|tmp2081|Used to hold the remember/restore flag in shield-copy routine|
|2082|numAliens|Number of aliens on screen|
|2083|saucerStart|Flag to start saucer (set to 1 when 2091:2092 counts down to 0)|
|2084|saucerActive|Saucer is on screen (1 means yes)|
|2085|saucerHit|Saucer has been hit (1 means draw it but don't move it)|
|2086|saucerHitTime|Hit-sequence timer (explosion drawn at 1F, score drawn at 18)|
|2087|saucerPriLocLSB|Mystery ship print descriptor ... coordinate LSB|
|2088|saucerPriLocMSB|Mystery ship print descriptor ... coordinate MSB|
|2089|saucerPriPicLSB|Mystery ship print descriptor ... message LSB|
|208A|saucerPriPicMSB|Mystery ship print descriptor ... message MSB|
|208B|saucerPriSize|Mystery ship print descriptor ... number of characters|
|208C|saucerDeltaY|Mystery ship delta Y|
|208D|sauScoreLSB|Pointer into mystery-ship score table (MSB)|
|208E|sauScoreMSB|Pointer into mystery-ship score table (LSB)|
|208F|shotCountLSB|Bumped every shot-removal. Saucer's direction is bit 0. (0=2/29, 1=-2/E0)|
|2090|shotCountMSB|Read as two-bytes with 208F, but never used as such.|
|2091|tillSaucerLSB| |
|2092|tillSaucerMSB|Count down every game loop. When it reaches 0 saucer is triggerd. Reset to 600.|
|2093|waitStartLoop|1=in wait-for-start loop, 0=in splash screens|
|2094|soundPort3|Current status of sound port (out $03)|
|2095|changeFleetSnd|Set to 1 in ISR if time to change the fleet sound|
|2096|fleetSndCnt|Delay until next fleet movement tone|
|2097|fleetSndReload|Reload value for fleet sound counter|
|2098|soundPort5|Current status of sound port (out $05)|
|2099|extraHold|Duration counter for extra-ship sound|
|209A|tilt|1 if tilt handling is in progress|
|209B|fleetSndHold|Time to hold fleet-sound at each change|
|209C| | |
|209D| | |
|209E| | |
|209F| | |
|20A0| | |
|20A1| | |
|20A2| | |
|20A3| | |
|20A4| | |
|20A5| | |
|20A6| | |
|20A7| | |
|20A8| | |
|20A9| | |
|20AA| | |
|20AB| | |
|20AC| | |
|20AD| | |
|20AE| | |
|20AF| | |
|20B0| | |
|20B1| | |
|20B2| | |
|20B3| | |
|20B4| | |
|20B5| | |
|20B6| | |
|20B7| | |
|20B8| | |
|20B9| | |
|20BA| | |
|20BB| | |
|20BC| | |
|20BD| | |
|20BE| | |
|20BF| | |
|20C0|isrDelay|Delay counter decremented in ISR|
|20C1|isrSplashTask|1=In demo, 2=Little-alien and Y, 4=shooting extra 'C'|
|20C2|splashAnForm|Image form (increments each draw)|
|20C3|splashDeltaX|Delta X|
|20C4|splashDeltaY|Delta Y|
|20C5|splashYr|Y coordinate|
|20C6|splashXr|X coordinate|
|20C7|splashImageLSB| |
|20C8|splashImageMSB|Base image 1BA0 (small alien with upside down Y)|
|20C9|splashImageSize|Size of image (16 bytes)|
|20CA|splashTargetY|Target Y coordinate|
|20CB|splashReached|Reached target Y flag (1 when reached)|
|20CC|splashImRestLSB|Base image for restore 1BA0 is small alien with upside down Y|
|20CD|splashImRestMSB| |
|20CE|twoPlayers|1 for yes, 0 means 1 player|
|20CF|aShotReloadRate|Based on the MSB of the player's score ... how fast the aliens reload their shots|
|20D0| |; This is where the alien-sprite-carying-the-Y ...|
|20D1| |; ... lives in ROM|
|20D2| | | |
|20D3| | | |
|20D4| | | |
|20D5| | | |
|20D6| | | |
|20D7| | | |
|20D8| | | |
|20D9| | | |
|20DA| | | |
|20DB| | | |
|20DC| | | |
|20DD| | | |
|20DE| | | |
|20DF| | | |
|20E0| | | |
|20E1| | | |
|20E2| | | |
|20E3| | | |
|20E4| | | |
|20E5|player1Ex|Extra ship has been awarded = 0|
|20E6|player2Ex|Extra ship has been awarded = 0|
|20E7|player1Alive|1 if player is alive, 0 if dead (after last man)|
|20E8|player2Alive|1 if player is alive, 0 if dead (after last man)|
|20E9|suspendPlay|1=game things are moving, 0=game things are suspended|
|20EA|coinSwitch|1=switch down, 0=switch up (used to debounce coin switch)|
|20EB|numCoins|number of coin credits in BCD format (99 max)|
|20EC|splashAnimate|0 for animation during splash and 1 for not. This alternates after every cycle.|
|20ED|demoCmdPtrLSB|pointer to demo commands LSB 1663|
|20EE|demoCmdPtrMSB|pointer to demo commands MSB|
|20EF|gameMode|1=game running, 0=demo or splash screens|
|20F0| | | |
|20F1|adjustScore|Set to 1 if score needs adjusting|
|20F2|scoreDeltaLSB|Score adjustment (LSB)|
|20F3|scoreDeltaMSB|Score adjustment (MSB)|
|20F4|HiScorL|Hi-score descriptor ... value LSB|
|20F5|HiScorM|Hi-score descriptor ... value MSB|
|20F6|HiScorLoL|Hi-score descriptor ... location LSB|
|20F7|HiScorLoM|Hi-score descriptor ... location MSB|
|20F8|P1ScorL|Hi-score descriptor ... value LSB|
|20F9|P1ScorM|Hi-score descriptor ... value MSB|
|20FA|P1ScorLoL|Hi-score descriptor ... location LSB|
|20FB|P1ScorLoM|Hi-score descriptor ... location MSB|
|20FC|P2ScorL|Hi-score descriptor ... value LSB|
|20FD|P2ScorM|Hi-score descriptor ... value MSB|
|20FE|P2ScorLoL|Hi-score descriptor ... location LSB|
|20FF|P2ScorLoM|Hi-score descriptor ... location MSB|

# Player 1 specific data

>>> memory

| | | |
| --- | --- | --- |
| 2100:2136 | | Player 1 alien ship indicators (0=dead) 11*5 = 55 |
| 2137:2141 | | Unused 11 bytes (room for another row of aliens?) |
| 2142:21F1 | | Player 1 shields remembered between rounds 44 bytes * 4 shields ($B0 bytes) |
| 21F2:21FA | | Unused 9 bytes |
| 21FB | p1RefAlienDX | Player 1 reference-alien delta X  |
| 21FC | p1RefAlienY  | Player 1 reference-alien Y coordinate |
| 21FD | p1RefAlienX  | Player 1 reference-alien X coordiante |
| 21FE | p1RackCnt    | Player 1 rack-count (starts at 0 but get incremented to 1-8) |
| 21FF | p1ShipsRem   | Ships remaining after current dies  |

# Player 2 specific data

>>> memory

| | | |
| --- | --- | --- |
| 2200:2236 | | Player 2 alien ship indicators (0=dead) 11*5 = 55 |
| 2237:2241 | | Unused 11 bytes (room for another row of aliens?) |
| 2242:22F1 | | Player 2 shields remembered between rounds 44 bytes * 4 shields ($B0 bytes) |
| 22F2:22FA | | Unused 9 bytes |
| 22FB | p2RefAlienDX | Player 2 reference-alien delta X |
| 22FC | p2RefAlienYr | Player 2 reference-alien Y coordinate |
| 22FD | p2RefAlienXr | Player 2 reference-alien X coordinate |
| 22FE | p2RackCnt    | Player 2 rack-count (starts at 0 but get incremented to 1-8) |
| 22FF | p2ShipsRem   | Ships remaining after current dies |

# Stack

>>> memory

| | | |
| --- | --- | --- |
| 2300:23DD | | Unused (stack space) |
| 23DE:23FF | | In the emulator the stack consumes this area (roughly 16 levels) |
