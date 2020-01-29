import cpu.base_cpu

OPCODES = [
    {"mnem": "LD (t),SP", "code": "08tltm", "bus": "w"},
    {"mnem": "STOP b", "code": "10bb", "bus": ""},
    {"mnem": "LD (HLI),A", "code": "22", "bus": ""},
    {"mnem": "LD A,(HLI)", "code": "2A", "bus": ""},
    {"mnem": "LD (HLD),A", "code": "32", "bus": ""},
    {"mnem": "LD A,(HLD)", "code": "3A", "bus": ""},
    {"mnem": "RETI", "code": "D9", "bus": ""},
    {"mnem": "LDFF00 (b),A", "code": "E0bb", "bus": ""},
    {"mnem": "LDFF00 (C),A", "code": "E2", "bus": ""},
    {"mnem": "ADD SP,b", "code": "E8bb", "bus": ""},
    {"mnem": "LD (t),A", "code": "EAtltm", "bus": "w"},
    {"mnem": "LD A,(b)", "code": "F0bb", "bus": ""},
    {"mnem": "LDHL SP,b", "code": "F8bb", "bus": ""},
    {"mnem": "LD A,(t)", "code": "FAtltm", "bus": "r"},
    {"mnem": "ADC A,A", "code": "8F", "bus": ""},
    {"mnem": "ADC A,B", "code": "88", "bus": ""},
    {"mnem": "ADC A,C", "code": "89", "bus": ""},
    {"mnem": "ADC A,D", "code": "8A", "bus": ""},
    {"mnem": "ADC A,E", "code": "8B", "bus": ""},
    {"mnem": "ADC A,H", "code": "8C", "bus": ""},
    {"mnem": "ADC A,L", "code": "8D", "bus": ""},
    {"mnem": "ADC A,(HL)", "code": "8E", "bus": ""},
    {"mnem": "ADC HL,BC", "code": "ED4A", "bus": ""},
    {"mnem": "ADC HL,DE", "code": "ED5A", "bus": ""},
    {"mnem": "ADC HL,HL", "code": "ED6A", "bus": ""},
    {"mnem": "ADC HL,SP", "code": "ED7A", "bus": ""},
    {"mnem": "ADC b", "code": "CEbb", "bus": ""},
    {"mnem": "ADD A,A", "code": "87", "bus": ""},
    {"mnem": "ADD A,B", "code": "80", "bus": ""},
    {"mnem": "ADD A,C", "code": "81", "bus": ""},
    {"mnem": "ADD A,D", "code": "82", "bus": ""},
    {"mnem": "ADD A,E", "code": "83", "bus": ""},
    {"mnem": "ADD A,H", "code": "84", "bus": ""},
    {"mnem": "ADD A,L", "code": "85", "bus": ""},
    {"mnem": "ADD A,(HL)", "code": "86", "bus": ""},
    {"mnem": "ADD HL,BC", "code": "09", "bus": ""},
    {"mnem": "ADD HL,DE", "code": "19", "bus": ""},
    {"mnem": "ADD HL,HL", "code": "29", "bus": ""},
    {"mnem": "ADD HL,SP", "code": "39", "bus": ""},
    {"mnem": "ADD b", "code": "C6bb", "bus": ""},
    {"mnem": "AND A", "code": "A7", "bus": ""},
    {"mnem": "AND B", "code": "A0", "bus": ""},
    {"mnem": "AND C", "code": "A1", "bus": ""},
    {"mnem": "AND D", "code": "A2", "bus": ""},
    {"mnem": "AND E", "code": "A3", "bus": ""},
    {"mnem": "AND H", "code": "A4", "bus": ""},
    {"mnem": "AND L", "code": "A5", "bus": ""},
    {"mnem": "AND (HL)", "code": "A6", "bus": ""},
    {"mnem": "AND b", "code": "E6bb", "bus": ""},
    {"mnem": "OR A", "code": "B7", "bus": ""},
    {"mnem": "OR B", "code": "B0", "bus": ""},
    {"mnem": "OR C", "code": "B1", "bus": ""},
    {"mnem": "OR D", "code": "B2", "bus": ""},
    {"mnem": "OR E", "code": "B3", "bus": ""},
    {"mnem": "OR H", "code": "B4", "bus": ""},
    {"mnem": "OR L", "code": "B5", "bus": ""},
    {"mnem": "OR (HL)", "code": "B6", "bus": ""},
    {"mnem": "OR b", "code": "F6bb", "bus": ""},
    {"mnem": "XOR A", "code": "AF", "bus": ""},
    {"mnem": "XOR B", "code": "A8", "bus": ""},
    {"mnem": "XOR C", "code": "A9", "bus": ""},
    {"mnem": "XOR D", "code": "AA", "bus": ""},
    {"mnem": "XOR E", "code": "AB", "bus": ""},
    {"mnem": "XOR H", "code": "AC", "bus": ""},
    {"mnem": "XOR L", "code": "AD", "bus": ""},
    {"mnem": "XOR (HL)", "code": "AE", "bus": ""},
    {"mnem": "XOR b", "code": "EEbb", "bus": ""},
    {"mnem": "BIT 0,A", "code": "CB47", "bus": ""},
    {"mnem": "BIT 0,B", "code": "CB40", "bus": ""},
    {"mnem": "BIT 0,C", "code": "CB41", "bus": ""},
    {"mnem": "BIT 0,D", "code": "CB42", "bus": ""},
    {"mnem": "BIT 0,E", "code": "CB43", "bus": ""},
    {"mnem": "BIT 0,H", "code": "CB44", "bus": ""},
    {"mnem": "BIT 0,L", "code": "CB45", "bus": ""},
    {"mnem": "BIT 1,A", "code": "CB4F", "bus": ""},
    {"mnem": "BIT 1,B", "code": "CB48", "bus": ""},
    {"mnem": "BIT 1,C", "code": "CB49", "bus": ""},
    {"mnem": "BIT 1,D", "code": "CB4A", "bus": ""},
    {"mnem": "BIT 1,E", "code": "CB4B", "bus": ""},
    {"mnem": "BIT 1,H", "code": "CB4C", "bus": ""},
    {"mnem": "BIT 1,L", "code": "CB4D", "bus": ""},
    {"mnem": "BIT 2,A", "code": "CB57", "bus": ""},
    {"mnem": "BIT 2,B", "code": "CB50", "bus": ""},
    {"mnem": "BIT 2,C", "code": "CB51", "bus": ""},
    {"mnem": "BIT 2,D", "code": "CB52", "bus": ""},
    {"mnem": "BIT 2,E", "code": "CB53", "bus": ""},
    {"mnem": "BIT 2,H", "code": "CB54", "bus": ""},
    {"mnem": "BIT 2,L", "code": "CB55", "bus": ""},
    {"mnem": "BIT 3,A", "code": "CB5F", "bus": ""},
    {"mnem": "BIT 3,B", "code": "CB58", "bus": ""},
    {"mnem": "BIT 3,C", "code": "CB59", "bus": ""},
    {"mnem": "BIT 3,D", "code": "CB5A", "bus": ""},
    {"mnem": "BIT 3,E", "code": "CB5B", "bus": ""},
    {"mnem": "BIT 3,H", "code": "CB5C", "bus": ""},
    {"mnem": "BIT 3,L", "code": "CB5D", "bus": ""},
    {"mnem": "BIT 4,A", "code": "CB67", "bus": ""},
    {"mnem": "BIT 4,B", "code": "CB60", "bus": ""},
    {"mnem": "BIT 4,C", "code": "CB61", "bus": ""},
    {"mnem": "BIT 4,D", "code": "CB62", "bus": ""},
    {"mnem": "BIT 4,E", "code": "CB63", "bus": ""},
    {"mnem": "BIT 4,H", "code": "CB64", "bus": ""},
    {"mnem": "BIT 4,L", "code": "CB65", "bus": ""},
    {"mnem": "BIT 5,A", "code": "CB6F", "bus": ""},
    {"mnem": "BIT 5,B", "code": "CB68", "bus": ""},
    {"mnem": "BIT 5,C", "code": "CB69", "bus": ""},
    {"mnem": "BIT 5,D", "code": "CB6A", "bus": ""},
    {"mnem": "BIT 5,E", "code": "CB6B", "bus": ""},
    {"mnem": "BIT 5,H", "code": "CB6C", "bus": ""},
    {"mnem": "BIT 5,L", "code": "CB6D", "bus": ""},
    {"mnem": "BIT 6,A", "code": "CB77", "bus": ""},
    {"mnem": "BIT 6,B", "code": "CB70", "bus": ""},
    {"mnem": "BIT 6,C", "code": "CB71", "bus": ""},
    {"mnem": "BIT 6,D", "code": "CB72", "bus": ""},
    {"mnem": "BIT 6,E", "code": "CB73", "bus": ""},
    {"mnem": "BIT 6,H", "code": "CB74", "bus": ""},
    {"mnem": "BIT 6,L", "code": "CB75", "bus": ""},
    {"mnem": "BIT 7,A", "code": "CB7F", "bus": ""},
    {"mnem": "BIT 7,B", "code": "CB78", "bus": ""},
    {"mnem": "BIT 7,C", "code": "CB79", "bus": ""},
    {"mnem": "BIT 7,D", "code": "CB7A", "bus": ""},
    {"mnem": "BIT 7,E", "code": "CB7B", "bus": ""},
    {"mnem": "BIT 7,H", "code": "CB7C", "bus": ""},
    {"mnem": "BIT 7,L", "code": "CB7D", "bus": ""},
    {"mnem": "BIT 0,(HL)", "code": "CB46", "bus": ""},
    {"mnem": "BIT 1,(HL)", "code": "CB4E", "bus": ""},
    {"mnem": "BIT 2,(HL)", "code": "CB56", "bus": ""},
    {"mnem": "BIT 3,(HL)", "code": "CB5E", "bus": ""},
    {"mnem": "BIT 4,(HL)", "code": "CB66", "bus": ""},
    {"mnem": "BIT 5,(HL)", "code": "CB6E", "bus": ""},
    {"mnem": "BIT 6,(HL)", "code": "CB76", "bus": ""},
    {"mnem": "BIT 7,(HL)", "code": "CB7E", "bus": ""},
    {"mnem": "CALL t", "code": "CDtltm", "bus": "x"},
    {"mnem": "CALL NZ,t", "code": "C4tltm", "bus": "x"},
    {"mnem": "CALL Z,t", "code": "CCtltm", "bus": "x"},
    {"mnem": "CALL NC,t", "code": "D4tltm", "bus": "x"},
    {"mnem": "CALL C,t", "code": "DCtltm", "bus": "x"},
    {"mnem": "CCF", "code": "3F", "bus": ""},
    {"mnem": "CP A", "code": "BF", "bus": ""},
    {"mnem": "CP B", "code": "B8", "bus": ""},
    {"mnem": "CP C", "code": "B9", "bus": ""},
    {"mnem": "CP D", "code": "BA", "bus": ""},
    {"mnem": "CP E", "code": "BB", "bus": ""},
    {"mnem": "CP H", "code": "BC", "bus": ""},
    {"mnem": "CP L", "code": "BD", "bus": ""},
    {"mnem": "CP (HL)", "code": "BE", "bus": ""},
    {"mnem": "CP b", "code": "FEbb", "bus": ""},
    {"mnem": "CPD", "code": "EDA9", "bus": ""},
    {"mnem": "CPI", "code": "EDA1", "bus": ""},
    {"mnem": "CPDR", "code": "EDB9", "bus": ""},
    {"mnem": "CPIR", "code": "EDB1", "bus": ""},
    {"mnem": "DAA", "code": "27", "bus": ""},
    {"mnem": "DI", "code": "F3", "bus": ""},
    {"mnem": "EI", "code": "FB", "bus": ""},
    {"mnem": "HALT", "code": "76", "bus": ""},
    {"mnem": "IM 0", "code": "ED46", "bus": ""},
    {"mnem": "IM 1", "code": "ED56", "bus": ""},
    {"mnem": "IM 2", "code": "ED5E", "bus": ""},
    {"mnem": "IND", "code": "EDAA", "bus": ""},
    {"mnem": "INDR", "code": "EDBA", "bus": ""},
    {"mnem": "INI", "code": "EDA2", "bus": ""},
    {"mnem": "INIR", "code": "EDB2", "bus": ""},
    {"mnem": "LDDR", "code": "EDB8", "bus": ""},
    {"mnem": "LDIR", "code": "EDB0", "bus": ""},
    {"mnem": "OTDR", "code": "EDBB", "bus": ""},
    {"mnem": "OTIR", "code": "EDB3", "bus": ""},
    {"mnem": "OUTD", "code": "EDAB", "bus": ""},
    {"mnem": "OUTI", "code": "EDA3", "bus": ""},
    {"mnem": "RETI", "code": "ED4D", "bus": ""},
    {"mnem": "RETN", "code": "ED45", "bus": ""},
    {"mnem": "RLD", "code": "ED6F", "bus": ""},
    {"mnem": "RRD", "code": "ED67", "bus": ""},
    {"mnem": "CPL", "code": "2F", "bus": ""},
    {"mnem": "DEC A", "code": "3D", "bus": ""},
    {"mnem": "DEC B", "code": "05", "bus": ""},
    {"mnem": "DEC C", "code": "0D", "bus": ""},
    {"mnem": "DEC D", "code": "15", "bus": ""},
    {"mnem": "DEC E", "code": "1D", "bus": ""},
    {"mnem": "DEC H", "code": "25", "bus": ""},
    {"mnem": "DEC L", "code": "2D", "bus": ""},
    {"mnem": "DEC (HL)", "code": "35", "bus": ""},
    {"mnem": "DEC BC", "code": "0B", "bus": ""},
    {"mnem": "DEC DE", "code": "1B", "bus": ""},
    {"mnem": "DEC HL", "code": "2B", "bus": ""},
    {"mnem": "DEC SP", "code": "3B", "bus": ""},
    {"mnem": "IN A,(C)", "code": "ED78", "bus": ""},
    {"mnem": "IN B,(C)", "code": "ED40", "bus": ""},
    {"mnem": "IN C,(C)", "code": "ED48", "bus": ""},
    {"mnem": "IN D,(C)", "code": "ED50", "bus": ""},
    {"mnem": "IN E,(C)", "code": "ED58", "bus": ""},
    {"mnem": "IN H,(C)", "code": "ED60", "bus": ""},
    {"mnem": "IN L,(C)", "code": "ED68", "bus": ""},
    {"mnem": "INC A", "code": "3C", "bus": ""},
    {"mnem": "INC B", "code": "04", "bus": ""},
    {"mnem": "INC C", "code": "0C", "bus": ""},
    {"mnem": "INC D", "code": "14", "bus": ""},
    {"mnem": "INC E", "code": "1C", "bus": ""},
    {"mnem": "INC H", "code": "24", "bus": ""},
    {"mnem": "INC L", "code": "2C", "bus": ""},
    {"mnem": "INC (HL)", "code": "34", "bus": ""},
    {"mnem": "INC BC", "code": "03", "bus": ""},
    {"mnem": "INC DE", "code": "13", "bus": ""},
    {"mnem": "INC HL", "code": "23", "bus": ""},
    {"mnem": "INC SP", "code": "33", "bus": ""},
    {"mnem": "JP (HL)", "code": "E9", "bus": ""},
    {"mnem": "JP t", "code": "C3tltm", "bus": "x"},
    {"mnem": "JP NZ,t", "code": "C2tltm", "bus": "x"},
    {"mnem": "JP Z,t", "code": "CAtltm", "bus": "x"},
    {"mnem": "JP NC,t", "code": "D2tltm", "bus": "x"},
    {"mnem": "JP C,t", "code": "DAtltm", "bus": "x"},
    {"mnem": "JR r", "code": "18rr", "bus": "x"},
    {"mnem": "JR NZ,r", "code": "20rr", "bus": "x"},
    {"mnem": "JR Z,r", "code": "28rr", "bus": "x"},
    {"mnem": "JR NC,r", "code": "30rr", "bus": "x"},
    {"mnem": "JR C,r", "code": "38rr", "bus": "x"},
    {"mnem": "LD A,A", "code": "7F", "bus": ""},
    {"mnem": "LD A,B", "code": "78", "bus": ""},
    {"mnem": "LD A,C", "code": "79", "bus": ""},
    {"mnem": "LD A,D", "code": "7A", "bus": ""},
    {"mnem": "LD A,E", "code": "7B", "bus": ""},
    {"mnem": "LD A,H", "code": "7C", "bus": ""},
    {"mnem": "LD A,L", "code": "7D", "bus": ""},
    {"mnem": "LD A,(HL)", "code": "7E", "bus": ""},
    {"mnem": "LD A,(BC)", "code": "0A", "bus": ""},
    {"mnem": "LD A,(DE)", "code": "1A", "bus": ""},
    {"mnem": "LD B,A", "code": "47", "bus": ""},
    {"mnem": "LD B,B", "code": "40", "bus": ""},
    {"mnem": "LD B,C", "code": "41", "bus": ""},
    {"mnem": "LD B,D", "code": "42", "bus": ""},
    {"mnem": "LD B,E", "code": "43", "bus": ""},
    {"mnem": "LD B,H", "code": "44", "bus": ""},
    {"mnem": "LD B,L", "code": "45", "bus": ""},
    {"mnem": "LD B,(HL)", "code": "46", "bus": ""},
    {"mnem": "LD C,A", "code": "4F", "bus": ""},
    {"mnem": "LD C,B", "code": "48", "bus": ""},
    {"mnem": "LD C,C", "code": "49", "bus": ""},
    {"mnem": "LD C,D", "code": "4A", "bus": ""},
    {"mnem": "LD C,E", "code": "4B", "bus": ""},
    {"mnem": "LD C,H", "code": "4C", "bus": ""},
    {"mnem": "LD C,L", "code": "4D", "bus": ""},
    {"mnem": "LD C,(HL)", "code": "4E", "bus": ""},
    {"mnem": "LD D,A", "code": "57", "bus": ""},
    {"mnem": "LD D,B", "code": "50", "bus": ""},
    {"mnem": "LD D,C", "code": "51", "bus": ""},
    {"mnem": "LD D,D", "code": "52", "bus": ""},
    {"mnem": "LD D,E", "code": "53", "bus": ""},
    {"mnem": "LD D,H", "code": "54", "bus": ""},
    {"mnem": "LD D,L", "code": "55", "bus": ""},
    {"mnem": "LD D,(HL)", "code": "56", "bus": ""},
    {"mnem": "LD E,A", "code": "5F", "bus": ""},
    {"mnem": "LD E,B", "code": "58", "bus": ""},
    {"mnem": "LD E,C", "code": "59", "bus": ""},
    {"mnem": "LD E,D", "code": "5A", "bus": ""},
    {"mnem": "LD E,E", "code": "5B", "bus": ""},
    {"mnem": "LD E,H", "code": "5C", "bus": ""},
    {"mnem": "LD E,L", "code": "5D", "bus": ""},
    {"mnem": "LD E,(HL)", "code": "5E", "bus": ""},
    {"mnem": "LD H,A", "code": "67", "bus": ""},
    {"mnem": "LD H,B", "code": "60", "bus": ""},
    {"mnem": "LD H,C", "code": "61", "bus": ""},
    {"mnem": "LD H,D", "code": "62", "bus": ""},
    {"mnem": "LD H,E", "code": "63", "bus": ""},
    {"mnem": "LD H,H", "code": "64", "bus": ""},
    {"mnem": "LD H,L", "code": "65", "bus": ""},
    {"mnem": "LD H,(HL)", "code": "66", "bus": ""},
    {"mnem": "LD L,A", "code": "6F", "bus": ""},
    {"mnem": "LD L,B", "code": "68", "bus": ""},
    {"mnem": "LD L,C", "code": "69", "bus": ""},
    {"mnem": "LD L,D", "code": "6A", "bus": ""},
    {"mnem": "LD L,E", "code": "6B", "bus": ""},
    {"mnem": "LD L,H", "code": "6C", "bus": ""},
    {"mnem": "LD L,L", "code": "6D", "bus": ""},
    {"mnem": "LD L,(HL)", "code": "6E", "bus": ""},
    {"mnem": "LD (HL),A", "code": "77", "bus": ""},
    {"mnem": "LD (HL),B", "code": "70", "bus": ""},
    {"mnem": "LD (HL),C", "code": "71", "bus": ""},
    {"mnem": "LD (HL),D", "code": "72", "bus": ""},
    {"mnem": "LD (HL),E", "code": "73", "bus": ""},
    {"mnem": "LD (HL),H", "code": "74", "bus": ""},
    {"mnem": "LD (HL),L", "code": "75", "bus": ""},
    {"mnem": "LD (BC),A", "code": "02", "bus": ""},
    {"mnem": "LD (DE),A", "code": "12", "bus": ""},
    {"mnem": "LD SP,HL", "code": "F9", "bus": ""},
    {"mnem": "LD I,A", "code": "ED47", "bus": ""},
    {"mnem": "LD A,I", "code": "ED57", "bus": ""},
    {"mnem": "LD R,A", "code": "ED4F", "bus": ""},
    {"mnem": "LD A,R", "code": "ED5F", "bus": ""},
    {"mnem": "LD BC,(t)", "code": "ED4Btltm", "bus": "r"},
    {"mnem": "LD DE,(t)", "code": "ED5Btltm", "bus": "r"},
    {"mnem": "LD HL,(t)", "code": "ED6Btltm", "bus": "r"},
    {"mnem": "LD SP,(t)", "code": "ED7Btltm", "bus": "r"},
    {"mnem": "LD (t),BC", "code": "ED43tltm", "bus": "w"},
    {"mnem": "LD (t),DE", "code": "ED53tltm", "bus": "w"},
    {"mnem": "LD (t),SP", "code": "ED73tltm", "bus": "w"},
    {"mnem": "LD BC,w", "code": "01wlwm", "bus": ""},
    {"mnem": "LD DE,w", "code": "11wlwm", "bus": ""},
    {"mnem": "LD HL,w", "code": "21wlwm", "bus": ""},
    {"mnem": "LD SP,w", "code": "31wlwm", "bus": ""},
    {"mnem": "LD A,b", "code": "3Ebb", "bus": ""},
    {"mnem": "LD B,b", "code": "06bb", "bus": ""},
    {"mnem": "LD C,b", "code": "0Ebb", "bus": ""},
    {"mnem": "LD D,b", "code": "16bb", "bus": ""},
    {"mnem": "LD E,b", "code": "1Ebb", "bus": ""},
    {"mnem": "LD H,b", "code": "26bb", "bus": ""},
    {"mnem": "LD L,b", "code": "2Ebb", "bus": ""},
    {"mnem": "LD (HL),b", "code": "36bb", "bus": ""},
    {"mnem": "LDD", "code": "EDA8", "bus": ""},
    {"mnem": "LDI", "code": "EDA0", "bus": ""},
    {"mnem": "NEG", "code": "ED44", "bus": ""},
    {"mnem": "NOP", "code": "00", "bus": ""},
    {"mnem": "OUT (C),A", "code": "ED79", "bus": ""},
    {"mnem": "OUT (C),B", "code": "ED41", "bus": ""},
    {"mnem": "OUT (C),C", "code": "ED49", "bus": ""},
    {"mnem": "OUT (C),D", "code": "ED51", "bus": ""},
    {"mnem": "OUT (C),E", "code": "ED59", "bus": ""},
    {"mnem": "OUT (C),H", "code": "ED61", "bus": ""},
    {"mnem": "OUT (C),L", "code": "ED69", "bus": ""},
    {"mnem": "RES 0,A", "code": "CB87", "bus": ""},
    {"mnem": "RES 0,B", "code": "CB80", "bus": ""},
    {"mnem": "RES 0,C", "code": "CB81", "bus": ""},
    {"mnem": "RES 0,D", "code": "CB82", "bus": ""},
    {"mnem": "RES 0,E", "code": "CB83", "bus": ""},
    {"mnem": "RES 0,H", "code": "CB84", "bus": ""},
    {"mnem": "RES 0,L", "code": "CB85", "bus": ""},
    {"mnem": "RES 1,A", "code": "CB8F", "bus": ""},
    {"mnem": "RES 1,B", "code": "CB88", "bus": ""},
    {"mnem": "RES 1,C", "code": "CB89", "bus": ""},
    {"mnem": "RES 1,D", "code": "CB8A", "bus": ""},
    {"mnem": "RES 1,E", "code": "CB8B", "bus": ""},
    {"mnem": "RES 1,H", "code": "CB8C", "bus": ""},
    {"mnem": "RES 1,L", "code": "CB8D", "bus": ""},
    {"mnem": "RES 2,A", "code": "CB97", "bus": ""},
    {"mnem": "RES 2,B", "code": "CB90", "bus": ""},
    {"mnem": "RES 2,C", "code": "CB91", "bus": ""},
    {"mnem": "RES 2,D", "code": "CB92", "bus": ""},
    {"mnem": "RES 2,E", "code": "CB93", "bus": ""},
    {"mnem": "RES 2,H", "code": "CB94", "bus": ""},
    {"mnem": "RES 2,L", "code": "CB95", "bus": ""},
    {"mnem": "RES 3,A", "code": "CB9F", "bus": ""},
    {"mnem": "RES 3,B", "code": "CB98", "bus": ""},
    {"mnem": "RES 3,C", "code": "CB99", "bus": ""},
    {"mnem": "RES 3,D", "code": "CB9A", "bus": ""},
    {"mnem": "RES 3,E", "code": "CB9B", "bus": ""},
    {"mnem": "RES 3,H", "code": "CB9C", "bus": ""},
    {"mnem": "RES 3,L", "code": "CB9D", "bus": ""},
    {"mnem": "RES 4,A", "code": "CBA7", "bus": ""},
    {"mnem": "RES 4,B", "code": "CBA0", "bus": ""},
    {"mnem": "RES 4,C", "code": "CBA1", "bus": ""},
    {"mnem": "RES 4,D", "code": "CBA2", "bus": ""},
    {"mnem": "RES 4,E", "code": "CBA3", "bus": ""},
    {"mnem": "RES 4,H", "code": "CBA4", "bus": ""},
    {"mnem": "RES 4,L", "code": "CBA5", "bus": ""},
    {"mnem": "RES 5,A", "code": "CBAF", "bus": ""},
    {"mnem": "RES 5,B", "code": "CBA8", "bus": ""},
    {"mnem": "RES 5,C", "code": "CBA9", "bus": ""},
    {"mnem": "RES 5,D", "code": "CBAA", "bus": ""},
    {"mnem": "RES 5,E", "code": "CBAB", "bus": ""},
    {"mnem": "RES 5,H", "code": "CBAC", "bus": ""},
    {"mnem": "RES 5,L", "code": "CBAD", "bus": ""},
    {"mnem": "RES 6,A", "code": "CBB7", "bus": ""},
    {"mnem": "RES 6,B", "code": "CBB0", "bus": ""},
    {"mnem": "RES 6,C", "code": "CBB1", "bus": ""},
    {"mnem": "RES 6,D", "code": "CBB2", "bus": ""},
    {"mnem": "RES 6,E", "code": "CBB3", "bus": ""},
    {"mnem": "RES 6,H", "code": "CBB4", "bus": ""},
    {"mnem": "RES 6,L", "code": "CBB5", "bus": ""},
    {"mnem": "RES 7,A", "code": "CBBF", "bus": ""},
    {"mnem": "RES 7,B", "code": "CBB8", "bus": ""},
    {"mnem": "RES 7,C", "code": "CBB9", "bus": ""},
    {"mnem": "RES 7,D", "code": "CBBA", "bus": ""},
    {"mnem": "RES 7,E", "code": "CBBB", "bus": ""},
    {"mnem": "RES 7,H", "code": "CBBC", "bus": ""},
    {"mnem": "RES 7,L", "code": "CBBD", "bus": ""},
    {"mnem": "RES 0,(HL)", "code": "CB86", "bus": ""},
    {"mnem": "RES 1,(HL)", "code": "CB8E", "bus": ""},
    {"mnem": "RES 2,(HL)", "code": "CB96", "bus": ""},
    {"mnem": "RES 3,(HL)", "code": "CB9E", "bus": ""},
    {"mnem": "RES 4,(HL)", "code": "CBA6", "bus": ""},
    {"mnem": "RES 5,(HL)", "code": "CBAE", "bus": ""},
    {"mnem": "RES 6,(HL)", "code": "CBB6", "bus": ""},
    {"mnem": "RES 7,(HL)", "code": "CBBE", "bus": ""},
    {"mnem": "SET 0,A", "code": "CBC7", "bus": ""},
    {"mnem": "SET 0,B", "code": "CBC0", "bus": ""},
    {"mnem": "SET 0,C", "code": "CBC1", "bus": ""},
    {"mnem": "SET 0,D", "code": "CBC2", "bus": ""},
    {"mnem": "SET 0,E", "code": "CBC3", "bus": ""},
    {"mnem": "SET 0,H", "code": "CBC4", "bus": ""},
    {"mnem": "SET 0,L", "code": "CBC5", "bus": ""},
    {"mnem": "SET 1,A", "code": "CBCF", "bus": ""},
    {"mnem": "SET 1,B", "code": "CBC8", "bus": ""},
    {"mnem": "SET 1,C", "code": "CBC9", "bus": ""},
    {"mnem": "SET 1,D", "code": "CBCA", "bus": ""},
    {"mnem": "SET 1,E", "code": "CBCB", "bus": ""},
    {"mnem": "SET 1,H", "code": "CBCC", "bus": ""},
    {"mnem": "SET 1,L", "code": "CBCD", "bus": ""},
    {"mnem": "SET 2,A", "code": "CBD7", "bus": ""},
    {"mnem": "SET 2,B", "code": "CBD0", "bus": ""},
    {"mnem": "SET 2,C", "code": "CBD1", "bus": ""},
    {"mnem": "SET 2,D", "code": "CBD2", "bus": ""},
    {"mnem": "SET 2,E", "code": "CBD3", "bus": ""},
    {"mnem": "SET 2,H", "code": "CBD4", "bus": ""},
    {"mnem": "SET 2,L", "code": "CBD5", "bus": ""},
    {"mnem": "SET 3,A", "code": "CBDF", "bus": ""},
    {"mnem": "SET 3,B", "code": "CBD8", "bus": ""},
    {"mnem": "SET 3,C", "code": "CBD9", "bus": ""},
    {"mnem": "SET 3,D", "code": "CBDA", "bus": ""},
    {"mnem": "SET 3,E", "code": "CBDB", "bus": ""},
    {"mnem": "SET 3,H", "code": "CBDC", "bus": ""},
    {"mnem": "SET 3,L", "code": "CBDD", "bus": ""},
    {"mnem": "SET 4,A", "code": "CBE7", "bus": ""},
    {"mnem": "SET 4,B", "code": "CBE0", "bus": ""},
    {"mnem": "SET 4,C", "code": "CBE1", "bus": ""},
    {"mnem": "SET 4,D", "code": "CBE2", "bus": ""},
    {"mnem": "SET 4,E", "code": "CBE3", "bus": ""},
    {"mnem": "SET 4,H", "code": "CBE4", "bus": ""},
    {"mnem": "SET 4,L", "code": "CBE5", "bus": ""},
    {"mnem": "SET 5,A", "code": "CBEF", "bus": ""},
    {"mnem": "SET 5,B", "code": "CBE8", "bus": ""},
    {"mnem": "SET 5,C", "code": "CBE9", "bus": ""},
    {"mnem": "SET 5,D", "code": "CBEA", "bus": ""},
    {"mnem": "SET 5,E", "code": "CBEB", "bus": ""},
    {"mnem": "SET 5,H", "code": "CBEC", "bus": ""},
    {"mnem": "SET 5,L", "code": "CBED", "bus": ""},
    {"mnem": "SET 6,A", "code": "CBF7", "bus": ""},
    {"mnem": "SET 6,B", "code": "CBF0", "bus": ""},
    {"mnem": "SET 6,C", "code": "CBF1", "bus": ""},
    {"mnem": "SET 6,D", "code": "CBF2", "bus": ""},
    {"mnem": "SET 6,E", "code": "CBF3", "bus": ""},
    {"mnem": "SET 6,H", "code": "CBF4", "bus": ""},
    {"mnem": "SET 6,L", "code": "CBF5", "bus": ""},
    {"mnem": "SET 7,A", "code": "CBFF", "bus": ""},
    {"mnem": "SET 7,B", "code": "CBF8", "bus": ""},
    {"mnem": "SET 7,C", "code": "CBF9", "bus": ""},
    {"mnem": "SET 7,D", "code": "CBFA", "bus": ""},
    {"mnem": "SET 7,E", "code": "CBFB", "bus": ""},
    {"mnem": "SET 7,H", "code": "CBFC", "bus": ""},
    {"mnem": "SET 7,L", "code": "CBFD", "bus": ""},
    {"mnem": "SET 0,(HL)", "code": "CBC6", "bus": ""},
    {"mnem": "SET 1,(HL)", "code": "CBCE", "bus": ""},
    {"mnem": "SET 2,(HL)", "code": "CBD6", "bus": ""},
    {"mnem": "SET 3,(HL)", "code": "CBDE", "bus": ""},
    {"mnem": "SET 4,(HL)", "code": "CBE6", "bus": ""},
    {"mnem": "SET 5,(HL)", "code": "CBEE", "bus": ""},
    {"mnem": "SET 6,(HL)", "code": "CBF6", "bus": ""},
    {"mnem": "SET 7,(HL)", "code": "CBFE", "bus": ""},
    {"mnem": "RET", "code": "C9", "bus": ""},
    {"mnem": "POP BC", "code": "C1", "bus": ""},
    {"mnem": "POP DE", "code": "D1", "bus": ""},
    {"mnem": "POP HL", "code": "E1", "bus": ""},
    {"mnem": "POP AF", "code": "F1", "bus": ""},
    {"mnem": "PUSH BC", "code": "C5", "bus": ""},
    {"mnem": "PUSH DE", "code": "D5", "bus": ""},
    {"mnem": "PUSH HL", "code": "E5", "bus": ""},
    {"mnem": "PUSH AF", "code": "F5", "bus": ""},
    {"mnem": "RET NZ", "code": "C0", "bus": ""},
    {"mnem": "RET Z", "code": "C8", "bus": ""},
    {"mnem": "RET NC", "code": "D0", "bus": ""},
    {"mnem": "RET C", "code": "D8", "bus": ""},
    {"mnem": "RL A", "code": "CB17", "bus": ""},
    {"mnem": "RL B", "code": "CB10", "bus": ""},
    {"mnem": "RL C", "code": "CB11", "bus": ""},
    {"mnem": "RL D", "code": "CB12", "bus": ""},
    {"mnem": "RL E", "code": "CB13", "bus": ""},
    {"mnem": "RL H", "code": "CB14", "bus": ""},
    {"mnem": "RL L", "code": "CB15", "bus": ""},
    {"mnem": "RL (HL)", "code": "CB16", "bus": ""},
    {"mnem": "RLA", "code": "17", "bus": ""},
    {"mnem": "RLC A", "code": "CB07", "bus": ""},
    {"mnem": "RLC B", "code": "CB00", "bus": ""},
    {"mnem": "RLC C", "code": "CB01", "bus": ""},
    {"mnem": "RLC D", "code": "CB02", "bus": ""},
    {"mnem": "RLC E", "code": "CB03", "bus": ""},
    {"mnem": "RLC H", "code": "CB04", "bus": ""},
    {"mnem": "RLC L", "code": "CB05", "bus": ""},
    {"mnem": "RLC (HL)", "code": "CB06", "bus": ""},
    {"mnem": "RLCA", "code": "07", "bus": ""},
    {"mnem": "RR A", "code": "CB1F", "bus": ""},
    {"mnem": "RR B", "code": "CB18", "bus": ""},
    {"mnem": "RR C", "code": "CB19", "bus": ""},
    {"mnem": "RR D", "code": "CB1A", "bus": ""},
    {"mnem": "RR E", "code": "CB1B", "bus": ""},
    {"mnem": "RR H", "code": "CB1C", "bus": ""},
    {"mnem": "RR L", "code": "CB1D", "bus": ""},
    {"mnem": "RR (HL)", "code": "CB1E", "bus": ""},
    {"mnem": "RRA", "code": "1F", "bus": ""},
    {"mnem": "RRC A", "code": "CB0F", "bus": ""},
    {"mnem": "RRC B", "code": "CB08", "bus": ""},
    {"mnem": "RRC C", "code": "CB09", "bus": ""},
    {"mnem": "RRC D", "code": "CB0A", "bus": ""},
    {"mnem": "RRC E", "code": "CB0B", "bus": ""},
    {"mnem": "RRC H", "code": "CB0C", "bus": ""},
    {"mnem": "RRC L", "code": "CB0D", "bus": ""},
    {"mnem": "RRC (HL)", "code": "CB0E", "bus": ""},
    {"mnem": "RRCA", "code": "0F", "bus": ""},
    {"mnem": "SLA A", "code": "CB27", "bus": ""},
    {"mnem": "SLA B", "code": "CB20", "bus": ""},
    {"mnem": "SLA C", "code": "CB21", "bus": ""},
    {"mnem": "SLA D", "code": "CB22", "bus": ""},
    {"mnem": "SLA E", "code": "CB23", "bus": ""},
    {"mnem": "SLA H", "code": "CB24", "bus": ""},
    {"mnem": "SLA L", "code": "CB25", "bus": ""},
    {"mnem": "SLA (HL)", "code": "CB26", "bus": ""},
    {"mnem": "SRA A", "code": "CB2F", "bus": ""},
    {"mnem": "SRA B", "code": "CB28", "bus": ""},
    {"mnem": "SRA C", "code": "CB29", "bus": ""},
    {"mnem": "SRA D", "code": "CB2A", "bus": ""},
    {"mnem": "SRA E", "code": "CB2B", "bus": ""},
    {"mnem": "SRA H", "code": "CB2C", "bus": ""},
    {"mnem": "SRA L", "code": "CB2D", "bus": ""},
    {"mnem": "SRA (HL)", "code": "CB2E", "bus": ""},
    {"mnem": "SRL A", "code": "CB3F", "bus": ""},
    {"mnem": "SWAP B", "code": "CB30", "bus": ""},
    {"mnem": "SWAP C", "code": "CB31", "bus": ""},
    {"mnem": "SWAP (HL)", "code": "CB36", "bus": ""},
    {"mnem": "SWAP A", "code": "CB37", "bus": ""},
    {"mnem": "SRL B", "code": "CB38", "bus": ""},
    {"mnem": "SRL C", "code": "CB39", "bus": ""},
    {"mnem": "SRL D", "code": "CB3A", "bus": ""},
    {"mnem": "SRL E", "code": "CB3B", "bus": ""},
    {"mnem": "SRL H", "code": "CB3C", "bus": ""},
    {"mnem": "SRL L", "code": "CB3D", "bus": ""},
    {"mnem": "SRL (HL)", "code": "CB3E", "bus": ""},
    {"mnem": "RST 0X00", "code": "C7", "bus": ""},
    {"mnem": "RST 0X08", "code": "CF", "bus": ""},
    {"mnem": "RST 0X10", "code": "D7", "bus": ""},
    {"mnem": "RST 0X18", "code": "DF", "bus": ""},
    {"mnem": "RST 0X20", "code": "E7", "bus": ""},
    {"mnem": "RST 0X28", "code": "EF", "bus": ""},
    {"mnem": "RST 0X30", "code": "F7", "bus": ""},
    {"mnem": "RST 0X38", "code": "FF", "bus": ""},
    {"mnem": "SCF", "code": "37", "bus": ""},
    {"mnem": "SBC A", "code": "9F", "bus": ""},
    {"mnem": "SBC B", "code": "98", "bus": ""},
    {"mnem": "SBC C", "code": "99", "bus": ""},
    {"mnem": "SBC D", "code": "9A", "bus": ""},
    {"mnem": "SBC E", "code": "9B", "bus": ""},
    {"mnem": "SBC H", "code": "9C", "bus": ""},
    {"mnem": "SBC L", "code": "9D", "bus": ""},
    {"mnem": "SBC (HL)", "code": "9E", "bus": ""},
    {"mnem": "SBC HL,BC", "code": "ED42", "bus": ""},
    {"mnem": "SBC HL,DE", "code": "ED52", "bus": ""},
    {"mnem": "SBC HL,HL", "code": "ED62", "bus": ""},
    {"mnem": "SBC HL,SP", "code": "ED72", "bus": ""},
    {"mnem": "SBC b", "code": "DEbb", "bus": ""},
    {"mnem": "SUB A", "code": "97", "bus": ""},
    {"mnem": "SUB B", "code": "90", "bus": ""},
    {"mnem": "SUB C", "code": "91", "bus": ""},
    {"mnem": "SUB D", "code": "92", "bus": ""},
    {"mnem": "SUB E", "code": "93", "bus": ""},
    {"mnem": "SUB H", "code": "94", "bus": ""},
    {"mnem": "SUB L", "code": "95", "bus": ""},
    {"mnem": "SUB (HL)", "code": "96", "bus": ""},
    {"mnem": "SUB b", "code": "D6bb", "bus": ""}
]


class CPU_Z80GB(cpu.base_cpu.CPU):

    def __init__(self):
        super().__init__(OPCODES)
