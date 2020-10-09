import opcodetools.cpu.base_cpu


OPCODES = [
    {"mnemonic": "NOP",              "code": "01",               "use": ""             },
    {"mnemonic": "LSRD",             "code": "04",               "use": ""             },
    {"mnemonic": "TAP",              "code": "06",               "use": ""             },
    {"mnemonic": "TPA",              "code": "07",               "use": ""             },
    {"mnemonic": "INX",              "code": "08",               "use": ""             },
    {"mnemonic": "DEX",              "code": "09",               "use": ""             },
    {"mnemonic": "CLV",              "code": "0A",               "use": ""             },
    {"mnemonic": "SEV",              "code": "0B",               "use": ""             },
    {"mnemonic": "CLC",              "code": "0C",               "use": ""             },
    {"mnemonic": "SEC",              "code": "0D",               "use": ""             },
    {"mnemonic": "CLI",              "code": "0E",               "use": ""             },
    {"mnemonic": "SEI",              "code": "0F",               "use": ""             },
    {"mnemonic": "SBA",              "code": "10",               "use": ""             },
    {"mnemonic": "CBA",              "code": "11",               "use": ""             },
    {"mnemonic": "TAB",              "code": "16",               "use": ""             },
    {"mnemonic": "TBA",              "code": "17",               "use": ""             },
    {"mnemonic": "DAA",              "code": "19",               "use": ""             },
    {"mnemonic": "ABA",              "code": "1B",               "use": ""             },
    {"mnemonic": "BRA r",            "code": "20rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BRN r",            "code": "21rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BHI r",            "code": "22rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BLS r",            "code": "23rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BCC r",            "code": "24rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BHS r",            "code": "24rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BCC r",            "code": "24rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BLO r",            "code": "25rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BNE r",            "code": "26rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BEQ r",            "code": "27rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BVC r",            "code": "28rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BVS r",            "code": "29rr",             "use": "r=code_pcr"   },
    {"mnemonic": "BPL r",            "code": "2Arr",             "use": "r=code_pcr"   },
    {"mnemonic": "BMI r",            "code": "2Brr",             "use": "r=code_pcr"   },
    {"mnemonic": "BGE r",            "code": "2Crr",             "use": "r=code_pcr"   },
    {"mnemonic": "BLT r",            "code": "2Drr",             "use": "r=code_pcr"   },
    {"mnemonic": "BGT r",            "code": "2Err",             "use": "r=code_pcr"   },
    {"mnemonic": "BLE r",            "code": "2Frr",             "use": "r=code_pcr"   },
    {"mnemonic": "TSX",              "code": "30",               "use": ""             },
    {"mnemonic": "INS",              "code": "31",               "use": ""             },
    {"mnemonic": "PULA",             "code": "32",               "use": ""             },
    {"mnemonic": "PULB",             "code": "33",               "use": ""             },
    {"mnemonic": "DES",              "code": "34",               "use": ""             },
    {"mnemonic": "TXS",              "code": "35",               "use": ""             },
    {"mnemonic": "PSHA",             "code": "36",               "use": ""             },
    {"mnemonic": "PSHB",             "code": "37",               "use": ""             },
    {"mnemonic": "PULX",             "code": "38",               "use": ""             },
    {"mnemonic": "RTS",              "code": "39",               "use": ""             },
    {"mnemonic": "ABX",              "code": "3A",               "use": ""             },
    {"mnemonic": "RTI",              "code": "3B",               "use": ""             },
    {"mnemonic": "PSHX",             "code": "3C",               "use": ""             },
    {"mnemonic": "MUL",              "code": "3D",               "use": ""             },
    {"mnemonic": "WAI",              "code": "3E",               "use": ""             },
    {"mnemonic": "SWI",              "code": "3F",               "use": ""             },
    {"mnemonic": "NEGA",             "code": "40",               "use": ""             },
    {"mnemonic": "COMA",             "code": "43",               "use": ""             },
    {"mnemonic": "LSRA",             "code": "44",               "use": ""             },
    {"mnemonic": "RORA",             "code": "46",               "use": ""             },
    {"mnemonic": "ASRA",             "code": "47",               "use": ""             },
    {"mnemonic": "LSLA",             "code": "48",               "use": ""             },
    {"mnemonic": "ASLA",             "code": "48",               "use": ""             },
    {"mnemonic": "ROLA",             "code": "49",               "use": ""             },
    {"mnemonic": "DECA",             "code": "4A",               "use": ""             },
    {"mnemonic": "INCA",             "code": "4C",               "use": ""             },
    {"mnemonic": "TSTA",             "code": "4D",               "use": ""             },
    {"mnemonic": "CLRA",             "code": "4F",               "use": ""             },
    {"mnemonic": "NEGB",             "code": "50",               "use": ""             },
    {"mnemonic": "COMB",             "code": "53",               "use": ""             },
    {"mnemonic": "LSRB",             "code": "54",               "use": ""             },
    {"mnemonic": "RORB",             "code": "56",               "use": ""             },
    {"mnemonic": "ASRB",             "code": "57",               "use": ""             },
    {"mnemonic": "LSLB",             "code": "58",               "use": ""             },
    {"mnemonic": "ASLB",             "code": "58",               "use": ""             },
    {"mnemonic": "ROLB",             "code": "59",               "use": ""             },
    {"mnemonic": "DECB",             "code": "5A",               "use": ""             },
    {"mnemonic": "INCB",             "code": "5C",               "use": ""             },
    {"mnemonic": "TSTB",             "code": "5D",               "use": ""             },
    {"mnemonic": "CLRB",             "code": "5F",               "use": ""             },
    {"mnemonic": "NEG i,X",          "code": "60ii",             "use": "i=const"      },
    {"mnemonic": "COM i,X",          "code": "63ii",             "use": "i=const"      },
    {"mnemonic": "LSR i,X",          "code": "64ii",             "use": "i=const"      },
    {"mnemonic": "ROR i,X",          "code": "66ii",             "use": "i=const"      },
    {"mnemonic": "ASR i,X",          "code": "67ii",             "use": "i=const"      },
    {"mnemonic": "ASL i,X",          "code": "68ii",             "use": "i=const"      },
    {"mnemonic": "LSL i,X",          "code": "68ii",             "use": "i=const"      },
    {"mnemonic": "ROL i,X",          "code": "69ii",             "use": "i=const"      },
    {"mnemonic": "DEC i,X",          "code": "6Aii",             "use": "i=const"      },
    {"mnemonic": "INC i,X",          "code": "6Cii",             "use": "i=const"      },
    {"mnemonic": "TST i,X",          "code": "6Dii",             "use": "i=const"      },
    {"mnemonic": "JMP i,X",          "code": "6Eii",             "use": "i=const"      },
    {"mnemonic": "CLR i,X",          "code": "6Fii",             "use": "i=const"      },
    {"mnemonic": "NEG t",            "code": "70t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "COM t",            "code": "73t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "LSR t",            "code": "74t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "ROR t",            "code": "76t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "ASR t",            "code": "77t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "ASL t",            "code": "78t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "LSL t",            "code": "78t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "ROL t",            "code": "79t1t0",           "use": "t=data_rw"    },
    {"mnemonic": "DEC t",            "code": "7At1t0",           "use": "t=data_rw"    },
    {"mnemonic": "INC t",            "code": "7Ct1t0",           "use": "t=data_rw"    },
    {"mnemonic": "TST t",            "code": "7Dt1t0",           "use": "t=data_r"     },
    {"mnemonic": "JMP t",            "code": "7Et1t0",           "use": "t=code"       },
    {"mnemonic": "CLR t",            "code": "7Ft1t0",           "use": "t=data_w"     },
    {"mnemonic": "SUBA #b",          "code": "80bb",             "use": "b=const"      },
    {"mnemonic": "CMPA #b",          "code": "81bb",             "use": "b=const"      },
    {"mnemonic": "SBCA #b",          "code": "82bb",             "use": "b=const"      },
    {"mnemonic": "SUBD #w",          "code": "83w1w0",           "use": "w=const"      },
    {"mnemonic": "ANDA #b",          "code": "84bb",             "use": "b=const"      },
    {"mnemonic": "BITA #b",          "code": "85bb",             "use": "b=const"      },
    {"mnemonic": "LDA #b",           "code": "86bb",             "use": "b=const"      },
    {"mnemonic": "EORA #b",          "code": "88bb",             "use": "b=const"      },
    {"mnemonic": "ADCA #b",          "code": "89bb",             "use": "b=const"      },
    {"mnemonic": "ORA #b",           "code": "8Abb",             "use": "b=const"      },
    {"mnemonic": "ADDA #b",          "code": "8Bbb",             "use": "b=const"      },
    {"mnemonic": "CPX #w",           "code": "8Cw1w0",           "use": "w=const"      },
    {"mnemonic": "BSR r",            "code": "8Drr",             "use": "r=code_pcr"   },
    {"mnemonic": "LDS #w",           "code": "8Ew1w0",           "use": "w=const"      },
    {"mnemonic": "SUBA p",           "code": "90pp",             "use": "p=data_r"     },
    {"mnemonic": "CMPA p",           "code": "91pp",             "use": "p=data_r"     },
    {"mnemonic": "SBCA p",           "code": "92pp",             "use": "p=data_r"     },
    {"mnemonic": "SUBD p",           "code": "93pp",             "use": "p=data_r"     },
    {"mnemonic": "ANDA p",           "code": "94pp",             "use": "p=data_r"     },
    {"mnemonic": "BITA p",           "code": "95pp",             "use": "p=data_r"     },
    {"mnemonic": "LDA p",            "code": "96pp",             "use": "p=data_r"     },
    {"mnemonic": "STA p",            "code": "97pp",             "use": "p=data_w"     },
    {"mnemonic": "EORA p",           "code": "98pp",             "use": "p=data_r"     },
    {"mnemonic": "ADCA p",           "code": "99pp",             "use": "p=data_r"     },
    {"mnemonic": "ORA p",            "code": "9App",             "use": "p=data_r"     },
    {"mnemonic": "ADDA p",           "code": "9Bpp",             "use": "p=data_r"     },
    {"mnemonic": "CPX p",            "code": "9Cpp",             "use": "p=data_r"     },
    {"mnemonic": "JSR p",            "code": "9Dpp",             "use": "p=code"       },
    {"mnemonic": "LDS p",            "code": "9Epp",             "use": "p=data_r"     },
    {"mnemonic": "STS p",            "code": "9Fpp",             "use": "p=data_w"     },
    {"mnemonic": "SUBA i,X",         "code": "A0ii",             "use": "i=const"      },
    {"mnemonic": "CMPA i,X",         "code": "A1ii",             "use": "i=const"      },
    {"mnemonic": "SBCA i,X",         "code": "A2ii",             "use": "i=const"      },
    {"mnemonic": "SUBD i,X",         "code": "A3ii",             "use": "i=const"      },
    {"mnemonic": "ANDA i,X",         "code": "A4ii",             "use": "i=const"      },
    {"mnemonic": "BITA i,X",         "code": "A5ii",             "use": "i=const"      },
    {"mnemonic": "LDA i,X",          "code": "A6ii",             "use": "i=const"      },
    {"mnemonic": "STA i,X",          "code": "A7ii",             "use": "i=const"      },
    {"mnemonic": "EORA i,X",         "code": "A8ii",             "use": "i=const"      },
    {"mnemonic": "ADCA i,X",         "code": "A9ii",             "use": "i=const"      },
    {"mnemonic": "ORA i,X",          "code": "AAii",             "use": "i=const"      },
    {"mnemonic": "ADDA i,X",         "code": "ABii",             "use": "i=const"      },
    {"mnemonic": "CPX i,X",          "code": "ACii",             "use": "i=const"      },
    {"mnemonic": "JSR i,X",          "code": "ADii",             "use": "i=const"      },
    {"mnemonic": "LDS i,X",          "code": "AEii",             "use": "i=const"      },
    {"mnemonic": "STS i,X",          "code": "AFii",             "use": "i=const"      },
    {"mnemonic": "SUBA t",           "code": "B0t1t0",           "use": "t=data_r"     },
    {"mnemonic": "CMPA t",           "code": "B1t1t0",           "use": "t=data_r"     },
    {"mnemonic": "SBCA t",           "code": "B2t1t0",           "use": "t=data_r"     },
    {"mnemonic": "SUBD t",           "code": "B3t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ANDA t",           "code": "B4t1t0",           "use": "t=data_r"     },
    {"mnemonic": "BITA t",           "code": "B5t1t0",           "use": "t=data_r"     },
    {"mnemonic": "LDA t",            "code": "B6t1t0",           "use": "t=data_r"     },
    {"mnemonic": "STA t",            "code": "B7t1t0",           "use": "t=data_w"     },
    {"mnemonic": "EORA t",           "code": "B8t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ADCA t",           "code": "B9t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ORA t",            "code": "BAt1t0",           "use": "t=data_r"     },
    {"mnemonic": "ADDA t",           "code": "BBt1t0",           "use": "t=data_r"     },
    {"mnemonic": "CPX t",            "code": "BCt1t0",           "use": "t=data_r"     },
    {"mnemonic": "JSR t",            "code": "BDt1t0",           "use": "t=code"       },
    {"mnemonic": "LDS t",            "code": "BEt1t0",           "use": "t=data_r"     },
    {"mnemonic": "STS t",            "code": "BFt1t0",           "use": "t=data_w"     },
    {"mnemonic": "SUBB #b",          "code": "C0bb",             "use": "b=const"      },
    {"mnemonic": "CMPB #b",          "code": "C1bb",             "use": "b=const"      },
    {"mnemonic": "SBCB #b",          "code": "C2bb",             "use": "b=const"      },
    {"mnemonic": "ADDD #w",          "code": "C3w1w0",           "use": "w=const"      },
    {"mnemonic": "ANDB #b",          "code": "C4bb",             "use": "b=const"      },
    {"mnemonic": "BITB #b",          "code": "C5bb",             "use": "b=const"      },
    {"mnemonic": "LDB #b",           "code": "C6bb",             "use": "b=const"      },
    {"mnemonic": "EORB #b",          "code": "C8bb",             "use": "b=const"      },
    {"mnemonic": "ADCB #b",          "code": "C9bb",             "use": "b=const"      },
    {"mnemonic": "ORB #b",           "code": "CAbb",             "use": "b=const"      },
    {"mnemonic": "ADDB #b",          "code": "CBbb",             "use": "b=const"      },
    {"mnemonic": "LDD #w",           "code": "CCw1w0",           "use": "w=const"      },
    {"mnemonic": "LDX #w",           "code": "CEw1w0",           "use": "w=const"      },
    {"mnemonic": "SUBB p",           "code": "D0pp",             "use": "p=data_r"     },
    {"mnemonic": "CMPB p",           "code": "D1pp",             "use": "p=data_r"     },
    {"mnemonic": "SBCB p",           "code": "D2pp",             "use": "p=data_r"     },
    {"mnemonic": "ADDD p",           "code": "D3pp",             "use": "p=data_r"     },
    {"mnemonic": "ANDB p",           "code": "D4pp",             "use": "p=data_r"     },
    {"mnemonic": "BITB p",           "code": "D5pp",             "use": "p=data_r"     },
    {"mnemonic": "LDB p",            "code": "D6pp",             "use": "p=data_r"     },
    {"mnemonic": "STB p",            "code": "D7pp",             "use": "p=data_w"     },
    {"mnemonic": "EORB p",           "code": "D8pp",             "use": "p=data_r"     },
    {"mnemonic": "ADCB p",           "code": "D9pp",             "use": "p=data_r"     },
    {"mnemonic": "ORB p",            "code": "DApp",             "use": "p=data_r"     },
    {"mnemonic": "ADDB p",           "code": "DBpp",             "use": "p=data_r"     },
    {"mnemonic": "LDD p",            "code": "DCpp",             "use": "p=data_r"     },
    {"mnemonic": "STD p",            "code": "DDpp",             "use": "p=data_w"     },
    {"mnemonic": "LDX p",            "code": "DEpp",             "use": "p=data_r"     },
    {"mnemonic": "STX p",            "code": "DFpp",             "use": "p=data_r"     },
    {"mnemonic": "SUBB i,X",         "code": "E0ii",             "use": "i=const"      },
    {"mnemonic": "CMPB i,X",         "code": "E1ii",             "use": "i=const"      },
    {"mnemonic": "SBCB i,X",         "code": "E2ii",             "use": "i=const"      },
    {"mnemonic": "ADDD i,X",         "code": "E3ii",             "use": "i=const"      },
    {"mnemonic": "ANDB i,X",         "code": "E4ii",             "use": "i=const"      },
    {"mnemonic": "BITB i,X",         "code": "E5ii",             "use": "i=const"      },
    {"mnemonic": "LDB i,X",          "code": "E6ii",             "use": "i=const"      },
    {"mnemonic": "STB i,X",          "code": "E7ii",             "use": "i=const"      },
    {"mnemonic": "EORB i,X",         "code": "E8ii",             "use": "i=const"      },
    {"mnemonic": "ADCB i,X",         "code": "E9ii",             "use": "i=const"      },
    {"mnemonic": "ORB i,X",          "code": "EAii",             "use": "i=const"      },
    {"mnemonic": "ADDB i,X",         "code": "EBii",             "use": "i=const"      },
    {"mnemonic": "LDD i,X",          "code": "ECii",             "use": "i=const"      },
    {"mnemonic": "STD i,X",          "code": "EDii",             "use": "i=const"      },
    {"mnemonic": "LDX i,X",          "code": "EEii",             "use": "i=const"      },
    {"mnemonic": "STX i,X",          "code": "EFii",             "use": "i=const"      },
    {"mnemonic": "SUBB t",           "code": "F0t1t0",           "use": "t=data_r"     },
    {"mnemonic": "CMPB t",           "code": "F1t1t0",           "use": "t=data_r"     },
    {"mnemonic": "SBCB t",           "code": "F2t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ADDD t",           "code": "F3t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ANDB t",           "code": "F4t1t0",           "use": "t=data_r"     },
    {"mnemonic": "BITB t",           "code": "F5t1t0",           "use": "t=data_r"     },
    {"mnemonic": "LDB t",            "code": "F6t1t0",           "use": "t=data_r"     },
    {"mnemonic": "STB t",            "code": "F7t1t0",           "use": "t=data_w"     },
    {"mnemonic": "EORB t",           "code": "F8t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ADCB t",           "code": "F9t1t0",           "use": "t=data_r"     },
    {"mnemonic": "ORB t",            "code": "FAt1t0",           "use": "t=data_r"     },
    {"mnemonic": "ADDB t",           "code": "FBt1t0",           "use": "t=data_r"     },
    {"mnemonic": "LDD t",            "code": "FCt1t0",           "use": "t=data_r"     },
    {"mnemonic": "STD t",            "code": "FDt1t0",           "use": "t=data_w"     },
    {"mnemonic": "LDX t",            "code": "FEt1t0",           "use": "t=data_r"     },
    {"mnemonic": "STX t",            "code": "FFt1t0",           "use": "t=data_w"     },
]


class CPU_6803(opcodetools.cpu.base_cpu.CPU):

    def __init__(self):
        super().__init__(OPCODES)
