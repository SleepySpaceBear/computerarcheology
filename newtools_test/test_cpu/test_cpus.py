import unittest

import cpu.cpu_common


class Test_CPUs(unittest.TestCase):

    def test_get_by_name(self):

        cp = cpu.cpu_common.CPU.get_cpu('6502')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('6803')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('6809')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('8052')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('DVG')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('Z80')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('Z80GB')
        self.assertTrue(cp != None)

    def test_disassembly(self):

        cp = cpu.cpu_common.CPU.get_cpu('6809')
        opc = cp.find_opcodes_for_binary([0x10, 0xA3, 0x9D, 1, 2])
        self.assertTrue(len(opc) == 1)
        self.assertTrue(opc[0].mnemonic == 'CMPD [k,PC]')

    def test_binary_to_string(self):

        cp = cpu.cpu_common.CPU.get_cpu('6809')

        binary = [0x10, 0xA3, 0x9D, 1, 2]
        opc = cp.find_opcodes_for_binary(binary)[0]

        fills = cp.get_mnemonic_fills(opc, 0x1000, binary)
        out = cp.binary_to_string(opc, 0x1000, binary, fills)

        print(out)
