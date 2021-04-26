![RAM Use 2](HauntedHouse.jpg)

# RAM Use 2 (Second Floor Code)

>>> memory

| | | |
| --- | --- | --- |
| 44D9      | LoneObject            | 1 if a lone-object was given last input      |  
| 45AD      | NounDataSize          | Number of bytes in noun's data area          |
| 45AE      | DecodeEmpty           | 1 if something was decoded from input        |
| 45AF:45B0 | NounData              | Pointer to noun data                         |
| 465F:4660 | InputBuffer           | 32 byte input buffer                         |
| 4680      | InputNoun             | The user input noun                          |
| 4681      | InputVerb             | The user input verb                          |
| 4682      | GrammarType           | The phrase's grammar type                    |
| 4683      | InputEntroy           | Running counter ... never used               |
| 4684:4685 | NextWord              | Pointer to next word while parsing           |
| 4686      | WordSize              | Character counter in word parsing            |
| 4687      | CurrentWord           | Current word data                            |
| 468A:468B | PtrHold               | Input pointer hold (never used)              |
| 468C:46B9 | Stack                 | Stack space                                  |
| 477E      | Unpack1               | RAM used by unpack routine                   |
| 477F      | Unpack2               | RAM used by unpack routine                   |
| 4780      | Unpack3               | RAM used by unpack routine                   |
| 4781      | Unpack4               | RAM used by unpack routine                   |
| 492F      | CurrentRoom           | Player's current room number                 |

