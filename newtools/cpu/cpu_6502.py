import cpu.base_cpu

OPCODES = [
    {"mnemonic":"BRK",              "code":"00",               "use":"",             },
    {"mnemonic":"ORA (p,X)",        "code":"01pp",             "use":"",             },
    {"mnemonic":"ORA p",            "code":"05pp",             "use":"r",            },
    {"mnemonic":"ASL p",            "code":"06pp",             "use":"rw",           },
    {"mnemonic":"PHP",              "code":"08",               "use":"",             },
    {"mnemonic":"ORA #b",           "code":"09bb",             "use":"",             },
    {"mnemonic":"ASL A",            "code":"0A",               "use":"",             },
    {"mnemonic":"ORA t",            "code":"0Dt0t1",           "use":"r",            },
    {"mnemonic":"ASL t",            "code":"0Et0t1",           "use":"rw",           },
    {"mnemonic":"BPL r",            "code":"10rr",             "use":"code_pcr",     },
    {"mnemonic":"ORA (p),Y",        "code":"11pp",             "use":"",             },
    {"mnemonic":"ORA p,X",          "code":"15pp",             "use":"",             },
    {"mnemonic":"ASL p,X",          "code":"16pp",             "use":"",             },
    {"mnemonic":"CLC",              "code":"18",               "use":"",             },
    {"mnemonic":"ORA t,Y",          "code":"19t0t1",           "use":"",             },
    {"mnemonic":"ORA t,X",          "code":"1Dt0t1",           "use":"",             },
    {"mnemonic":"ASL t,X",          "code":"1Et0t1",           "use":"",             },
    {"mnemonic":"JSR t",            "code":"20t0t1",           "use":"code",         },
    {"mnemonic":"AND (p,X)",        "code":"21pp",             "use":"",             },
    {"mnemonic":"BIT p",            "code":"24pp",             "use":"r",            },
    {"mnemonic":"AND p",            "code":"25pp",             "use":"r",            },
    {"mnemonic":"ROL p",            "code":"26pp",             "use":"rw",           },
    {"mnemonic":"PLP",              "code":"28",               "use":"r",            },
    {"mnemonic":"AND #b",           "code":"29bb",             "use":"",             },
    {"mnemonic":"ROL A",            "code":"2A",               "use":"",             },
    {"mnemonic":"BIT t",            "code":"2Ct0t1",           "use":"r",            },
    {"mnemonic":"AND t",            "code":"2Dt0t1",           "use":"r",            },
    {"mnemonic":"ROL t",            "code":"2Et0t1",           "use":"rw",           },
    {"mnemonic":"BMI r",            "code":"30rr",             "use":"code_pcr",     },
    {"mnemonic":"AND (p),Y",        "code":"31pp",             "use":"",             },
    {"mnemonic":"AND p,X",          "code":"35pp",             "use":"",             },
    {"mnemonic":"ROL p,X",          "code":"36pp",             "use":"",             },
    {"mnemonic":"SEC",              "code":"38",               "use":"",             },
    {"mnemonic":"AND t,Y",          "code":"39t0t1",           "use":"",             },
    {"mnemonic":"AND t,X",          "code":"3Dt0t1",           "use":"",             },
    {"mnemonic":"ROL t,X",          "code":"3Et0t1",           "use":"",             },
    {"mnemonic":"RTI",              "code":"40",               "use":"",             },
    {"mnemonic":"EOR (p,X)",        "code":"41pp",             "use":"",             },
    {"mnemonic":"EOR p",            "code":"45pp",             "use":"r",            },
    {"mnemonic":"LSR p",            "code":"46pp",             "use":"rw",           },
    {"mnemonic":"PHA",              "code":"48",               "use":"",             },
    {"mnemonic":"EOR #b",           "code":"49bb",             "use":"",             },
    {"mnemonic":"LSR A",            "code":"4A",               "use":"",             },
    {"mnemonic":"JMP t",            "code":"4Ct0t1",           "use":"code",         },
    {"mnemonic":"EOR t",            "code":"4Dt0t1",           "use":"r",            },
    {"mnemonic":"LSR t",            "code":"4Et0t1",           "use":"rw",           },
    {"mnemonic":"BVC r",            "code":"50rr",             "use":"code_pcr",     },
    {"mnemonic":"EOR (p),Y",        "code":"51pp",             "use":"",             },
    {"mnemonic":"EOR p,X",          "code":"55pp",             "use":"",             },
    {"mnemonic":"LSR p,X",          "code":"56pp",             "use":"",             },
    {"mnemonic":"CLI",              "code":"58",               "use":"",             },
    {"mnemonic":"EOR t,Y",          "code":"59t0t1",           "use":"",             },
    {"mnemonic":"EOR t,X",          "code":"5Dt0t1",           "use":"",             },
    {"mnemonic":"LSR t,X",          "code":"5Et0t1",           "use":"",             },
    {"mnemonic":"RTS",              "code":"60",               "use":"",             },
    {"mnemonic":"ADC (p,X)",        "code":"61pp",             "use":"",             },
    {"mnemonic":"ADC p",            "code":"65pp",             "use":"r",            },
    {"mnemonic":"ROR p",            "code":"66pp",             "use":"rw",           },
    {"mnemonic":"PLA",              "code":"68",               "use":"r",            },
    {"mnemonic":"ADC #b",           "code":"69bb",             "use":"",             },
    {"mnemonic":"ROR A",            "code":"6A",               "use":"",             },
    {"mnemonic":"JMP (t)",          "code":"6Ct0t1",           "use":"code",         },
    {"mnemonic":"ADC t",            "code":"6Dt0t1",           "use":"r",            },
    {"mnemonic":"ROR t",            "code":"6Et0t1",           "use":"r",            },
    {"mnemonic":"BVS r",            "code":"70rr",             "use":"code_pcr",     },
    {"mnemonic":"ADC (p),Y",        "code":"71pp",             "use":"",             },
    {"mnemonic":"ADC p,X",          "code":"75pp",             "use":"",             },
    {"mnemonic":"ROR p,X",          "code":"76pp",             "use":"",             },
    {"mnemonic":"SEI",              "code":"78",               "use":"",             },
    {"mnemonic":"ADC t,Y",          "code":"79t0t1",           "use":"",             },
    {"mnemonic":"ADC t,X",          "code":"7Dt0t1",           "use":"",             },
    {"mnemonic":"ROR t,X",          "code":"7Et0t1",           "use":"",             },
    {"mnemonic":"STA (p,X)",        "code":"81pp",             "use":"",             },
    {"mnemonic":"STY p",            "code":"84pp",             "use":"w",            },
    {"mnemonic":"STA p",            "code":"85pp",             "use":"w",            },
    {"mnemonic":"STX p",            "code":"86pp",             "use":"w",            },
    {"mnemonic":"DEY",              "code":"88",               "use":"",             },
    {"mnemonic":"TXA",              "code":"8A",               "use":"",             },
    {"mnemonic":"STY t",            "code":"8Ct0t1",           "use":"w",            },
    {"mnemonic":"STA t",            "code":"8Dt0t1",           "use":"w",            },
    {"mnemonic":"STX t",            "code":"8Et0t1",           "use":"w",            },
    {"mnemonic":"BCC r",            "code":"90rr",             "use":"code_pcr",     },
    {"mnemonic":"STA (p),Y",        "code":"91pp",             "use":"",             },
    {"mnemonic":"STY p,X",          "code":"94pp",             "use":"",             },
    {"mnemonic":"STA p,X",          "code":"95pp",             "use":"",             },
    {"mnemonic":"STX p,Y",          "code":"96pp",             "use":"",             },
    {"mnemonic":"TYA",              "code":"98",               "use":"",             },
    {"mnemonic":"STA t,Y",          "code":"99t0t1",           "use":"",             },
    {"mnemonic":"TXS",              "code":"9A",               "use":"",             },
    {"mnemonic":"STA t,X",          "code":"9Dt0t1",           "use":"",             },
    {"mnemonic":"LDY #b",           "code":"A0bb",             "use":"",             },
    {"mnemonic":"LDA (p,X)",        "code":"A1pp",             "use":"",             },
    {"mnemonic":"LDX #b",           "code":"A2bb",             "use":"",             },
    {"mnemonic":"LDY p",            "code":"A4pp",             "use":"r",            },
    {"mnemonic":"LDA p",            "code":"A5pp",             "use":"r",            },
    {"mnemonic":"LDX p",            "code":"A6pp",             "use":"r",            },
    {"mnemonic":"TAY",              "code":"A8",               "use":"",             },
    {"mnemonic":"LDA #b",           "code":"A9bb",             "use":"",             },
    {"mnemonic":"TAX",              "code":"AA",               "use":"",             },
    {"mnemonic":"LDY t",            "code":"ACt0t1",           "use":"r",            },
    {"mnemonic":"LDA t",            "code":"ADt0t1",           "use":"r",            },
    {"mnemonic":"LDX t",            "code":"AEt0t1",           "use":"r",            },
    {"mnemonic":"BCS r",            "code":"B0rr",             "use":"code_pcr",     },
    {"mnemonic":"LDA (p),Y",        "code":"B1pp",             "use":"",             },
    {"mnemonic":"LDY p,X",          "code":"B4pp",             "use":"",             },
    {"mnemonic":"LDA p,X",          "code":"B5pp",             "use":"",             },
    {"mnemonic":"LDX p,Y",          "code":"B6pp",             "use":"",             },
    {"mnemonic":"CLV",              "code":"B8",               "use":"",             },
    {"mnemonic":"LDA t,Y",          "code":"B9t0t1",           "use":"",             },
    {"mnemonic":"TSX",              "code":"BA",               "use":"",             },
    {"mnemonic":"LDY t,X",          "code":"BCt0t1",           "use":"",             },
    {"mnemonic":"LDA t,X",          "code":"BDt0t1",           "use":"",             },
    {"mnemonic":"LDX t,Y",          "code":"BEt0t1",           "use":"",             },
    {"mnemonic":"CPY #b",           "code":"C0bb",             "use":"",             },
    {"mnemonic":"CMP (p,X)",        "code":"C1pp",             "use":"",             },
    {"mnemonic":"CPY p",            "code":"C4pp",             "use":"r",            },
    {"mnemonic":"CMP p",            "code":"C5pp",             "use":"r",            },
    {"mnemonic":"DEC p",            "code":"C6pp",             "use":"rw",           },
    {"mnemonic":"INY",              "code":"C8",               "use":"",             },
    {"mnemonic":"CMP #b",           "code":"C9bb",             "use":"",             },
    {"mnemonic":"DEX",              "code":"CA",               "use":"",             },
    {"mnemonic":"CPY t",            "code":"CCt0t1",           "use":"r",            },
    {"mnemonic":"CMP t",            "code":"CDt0t1",           "use":"r",            },
    {"mnemonic":"DEC t",            "code":"CEt0t1",           "use":"rw",           },
    {"mnemonic":"BNE r",            "code":"D0rr",             "use":"code_pcr",     },
    {"mnemonic":"CMP (p),Y",        "code":"D1pp",             "use":"",             },
    {"mnemonic":"CMP p,X",          "code":"D5pp",             "use":"",             },
    {"mnemonic":"DEC p,X",          "code":"D6pp",             "use":"",             },
    {"mnemonic":"CLD",              "code":"D8",               "use":"",             },
    {"mnemonic":"CMP t,Y",          "code":"D9t0t1",           "use":"",             },
    {"mnemonic":"CMP t,X",          "code":"DDt0t1",           "use":"",             },
    {"mnemonic":"DEC t,X",          "code":"DEt0t1",           "use":"",             },
    {"mnemonic":"CPX #b",           "code":"E0bb",             "use":"",             },
    {"mnemonic":"SBC (p,X)",        "code":"E1pp",             "use":"",             },
    {"mnemonic":"CPX p",            "code":"E4pp",             "use":"r",            },
    {"mnemonic":"SBC p",            "code":"E5pp",             "use":"r",            },
    {"mnemonic":"INC p",            "code":"E6pp",             "use":"rw",           },
    {"mnemonic":"INX",              "code":"E8",               "use":"",             },
    {"mnemonic":"SBC #b",           "code":"E9bb",             "use":"",             },
    {"mnemonic":"NOP",              "code":"EA",               "use":"",             },
    {"mnemonic":"CPX t",            "code":"ECt0t1",           "use":"r",            },
    {"mnemonic":"SBC t",            "code":"EDt0t1",           "use":"r",            },
    {"mnemonic":"INC t",            "code":"EEt0t1",           "use":"rw",           },
    {"mnemonic":"BEQ r",            "code":"F0rr",             "use":"code_pcr",     },
    {"mnemonic":"SBC (p),Y",        "code":"F1pp",             "use":"",             },
    {"mnemonic":"SBC p,X",          "code":"F5pp",             "use":"",             },
    {"mnemonic":"INC p,X",          "code":"F6pp",             "use":"",             },
    {"mnemonic":"SED",              "code":"F8",               "use":"",             },
    {"mnemonic":"SBC t,Y",          "code":"F9t0t1",           "use":"",             },
    {"mnemonic":"SBC t,X",          "code":"FDt0t1",           "use":"",             },
    {"mnemonic":"INC t,X",          "code":"FEt0t1",           "use":"",             },
]


class CPU_6502(cpu.base_cpu.CPU):

    def __init__(self):
        super().__init__(OPCODES)
