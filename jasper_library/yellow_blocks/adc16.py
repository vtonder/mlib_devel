from yellow_block import YellowBlock
from verilog import VerilogInstance
from constraints import PortConstraint

class adc16(YellowBlock):
    def initialize(self)
        self.num_units = 4*int(self.board_count)
        if self.zdok_rev == '1':
            self.num_clocks = int(self.board_count)
        else:
            self.num_clocks = self.num_units
        # The zdok revision 0 case is not completely implemented (it should be ok up till
        # physical constraint generation) so barf here.
        if self.zdok_rev == '1':
            raise NotImplementedError("adc16 not yet supported for zdok revisions other that '1'")
        self.add_source('adc16_interface')

        self.provides = ['adc0_clk','adc0_clk90', 'adc0_clk180', 'adc0_clk270']
        self.requires = ['user_clk']
        if self.num_units > 4:
            self.exc_requires = ['zdok0', 'zdok1']
        else:
            self.exc_requires = ['zdok0']

    #def set_dependencies(self):
    #    self.add_resource('adc0_clk')
    #    self.add_resource('adc0_clk90')
    #    self.add_resource('adc0_clk180')
    #    self.add_resource('adc0_clk270')
    #    self.add_requirement('user_clk')
    #    self.add_exc_requirement('zdok0')
    #    if self.num_units > 4:
    #        self.add_exc_requirement('zdok1')

    def modify_top(self,top):
        module = 'adc16_interface'
        inst = VerilogInstance(entity=module, name=self.fullname, comment=self.fullname)
        inst.add_parameter('G_NUM_CLKS', int(self.num_clocks))
        inst.add_parameter('G_ZDOK_REV', int(self.zdok_rev))
        inst.add_parameter('G_NUM_UNITS', int(self.num_units))

        # ports which go to simulink
        inst.add_port('a1', self.fullname+'_a1')
        inst.add_port('a2', self.fullname+'_a2')
        inst.add_port('a3', self.fullname+'_a3')
        inst.add_port('a4', self.fullname+'_a4')
        inst.add_port('b1', self.fullname+'_b1')
        inst.add_port('b2', self.fullname+'_b2')
        inst.add_port('b3', self.fullname+'_b3')
        inst.add_port('b4', self.fullname+'_b4')
        inst.add_port('c1', self.fullname+'_c1')
        inst.add_port('c2', self.fullname+'_c2')
        inst.add_port('c3', self.fullname+'_c3')
        inst.add_port('c4', self.fullname+'_c4')
        inst.add_port('d1', self.fullname+'_d1')
        inst.add_port('d2', self.fullname+'_d2')
        inst.add_port('d3', self.fullname+'_d3')
        inst.add_port('d4', self.fullname+'_d4')
        inst.add_port('e1', self.fullname+'_e1')
        inst.add_port('e2', self.fullname+'_e2')
        inst.add_port('e3', self.fullname+'_e3')
        inst.add_port('e4', self.fullname+'_e4')
        inst.add_port('f1', self.fullname+'_f1')
        inst.add_port('f2', self.fullname+'_f2')
        inst.add_port('f3', self.fullname+'_f3')
        inst.add_port('f4', self.fullname+'_f4')
        inst.add_port('g1', self.fullname+'_g1')
        inst.add_port('g2', self.fullname+'_g2')
        inst.add_port('g3', self.fullname+'_g3')
        inst.add_port('g4', self.fullname+'_g4')
        inst.add_port('h1', self.fullname+'_h1')
        inst.add_port('h2', self.fullname+'_h2')
        inst.add_port('h3', self.fullname+'_h3')
        inst.add_port('h4', self.fullname+'_h4')
        top.add_signal(self.fullname+'_a1', width=8)
        top.add_signal(self.fullname+'_a2', width=8)
        top.add_signal(self.fullname+'_a3', width=8)
        top.add_signal(self.fullname+'_a4', width=8)
        top.add_signal(self.fullname+'_b1', width=8)
        top.add_signal(self.fullname+'_b2', width=8)
        top.add_signal(self.fullname+'_b3', width=8)
        top.add_signal(self.fullname+'_b4', width=8)
        top.add_signal(self.fullname+'_c1', width=8)
        top.add_signal(self.fullname+'_c2', width=8)
        top.add_signal(self.fullname+'_c3', width=8)
        top.add_signal(self.fullname+'_c4', width=8)
        top.add_signal(self.fullname+'_d1', width=8)
        top.add_signal(self.fullname+'_d2', width=8)
        top.add_signal(self.fullname+'_d3', width=8)
        top.add_signal(self.fullname+'_d4', width=8)
        top.add_signal(self.fullname+'_e1', width=8)
        top.add_signal(self.fullname+'_e2', width=8)
        top.add_signal(self.fullname+'_e3', width=8)
        top.add_signal(self.fullname+'_e4', width=8)
        top.add_signal(self.fullname+'_f1', width=8)
        top.add_signal(self.fullname+'_f2', width=8)
        top.add_signal(self.fullname+'_f3', width=8)
        top.add_signal(self.fullname+'_f4', width=8)
        top.add_signal(self.fullname+'_g1', width=8)
        top.add_signal(self.fullname+'_g2', width=8)
        top.add_signal(self.fullname+'_g3', width=8)
        top.add_signal(self.fullname+'_g4', width=8)
        top.add_signal(self.fullname+'_h1', width=8)
        top.add_signal(self.fullname+'_h2', width=8)
        top.add_signal(self.fullname+'_h3', width=8)
        top.add_signal(self.fullname+'_h4', width=8)

        # ports which go to the wb controller. Any ports which don't go to top level need
        # corresponding signals to be added to top.v
        inst.add_port('fabric_clk', 'adc0_clk')
        top.add_signal('adc0_clk')
        inst.add_port('fabric_clk_90', 'adc0_clk90')
        top.add_signal('adc0_clk_90')
        inst.add_port('fabric_clk_180', 'adc0_clk180')
        top.add_signal('adc0_clk_180')
        inst.add_port('fabric_clk_270', 'adc0_clk270')
        top.add_signal('adc0_clk_270')

        inst.add_port('reset', 'adc16_reset')
        top.add_signal('adc16_reset', width=1)
        inst.add_port('iserdes_bitslip', 'adc16_iserdes_bitslip')
        top.add_signal('adc16_iserdes_bitslip', width=8)

        inst.add_port('delay_rst', 'adc16_delay_rst')
        top.add_signal('adc16_delay_rst', width=64)
        inst.add_port('delay_tap', 'adc16_delay_tap')
        top.add_signal('adc16_delay_tap', width=5)

        inst.add_port('snap_req', 'adc16_snap_req')
        top.add_signal('adc16_snap_req', width=1)
        inst.add_port('snap_we', 'adc16_snap_we')
        top.add_signal('adc16_snap_we', width=1)
        inst.add_port('snap_addr', 'adc16_snap_addr')
        top.add_signal('adc16_snap_addr', width=10)

        inst.add_port('locked', 'adc16_locked')
        top.add_signal('adc16_locked', width=2)

        # Now the external ports, which need corresponding ports adding to top.v

        if self.zdok_rev == '2':
            inst.add_port('clk_frame_p', '0')
            inst.add_port('clk_frame_n', '0')
        else:
            inst.add_port('clk_frame_p', 'adc16_clk_frame_p')
            top.add_port('clk_frame_p', 'in', width=int(self.num_units))
            inst.add_port('clk_frame_n', 'adc16_clk_frame_n')
            top.add_port('clk_frame_n', 'in', width=int(self.num_units))

        inst.add_port('clk_line_p', 'adc16_clk_line_p')
        top.add_port('adc16_clk_line_p', 'in', width=int(self.num_clocks))
        inst.add_port('clk_line_n', 'adc16_clk_line_n')
        top.add_port('adc16_clk_line_n', 'in', width=int(self.num_clocks))
        inst.add_port('ser_a_p', 'adc16_ser_a_p')
        top.add_port('adc16_ser_a_p', 'in', width=4*int(self.num_units))
        inst.add_port('ser_a_n', 'adc16_ser_a_n')
        top.add_port('adc16_ser_a_n', 'in', width=4*int(self.num_units))
        inst.add_port('ser_b_p', 'adc16_ser_b_p')
        top.add_port('adc16_ser_b_p', 'in', width=4*int(self.num_units))
        inst.add_port('ser_b_n', 'adc16_ser_b_n')
        top.add_port('adc16_ser_b_n', 'in', width=4*int(self.num_units))


        top.add_instance(inst)

        # wb controller

        wbctrl = VerilogInstance(entity='wb_adc16_controller', name='wb_adc16_controller')
        wbctrl.add_parameter('G_ROACH2_REV', int(self.roach2_rev))
        wbctrl.add_parameter('G_ZDOK_REV', int(self.zdok_rev))
        wbctrl.add_parameter('G_NUM_UNITS', int(self.num_units))
        # These are top-level ports -- they don't need signal declarations,
        # but they do need ports added to the top-level
        wbctrl.add_port('adc0_adc3wire_csn1', 'adc0_adc3wire_csn1')
        wbctrl.add_port('adc0_adc3wire_csn2', 'adc0_adc3wire_csn2')
        wbctrl.add_port('adc0_adc3wire_csn3', 'adc0_adc3wire_csn3')
        wbctrl.add_port('adc0_adc3wire_csn4', 'adc0_adc3wire_csn4')
        wbctrl.add_port('adc0_adc3wire_sdata','adc0_adc3wire_sdata')
        wbctrl.add_port('adc0_adc3wire_sclk', 'adc0_adc3wire_sclk')
        top.add_port('adc0_adc3wire_csn1', 'out')
        top.add_port('adc0_adc3wire_csn2', 'out')
        top.add_port('adc0_adc3wire_csn3', 'out')
        top.add_port('adc0_adc3wire_csn4', 'out')
        top.add_port('adc0_adc3wire_sdata','out')
        top.add_port('adc0_adc3wire_sclk', 'out')

        if self.num_units > 4:
            wbctrl.add_port('adc1_adc3wire_csn1', 'adc1_adc3wire_csn1')
            wbctrl.add_port('adc1_adc3wire_csn2', 'adc1_adc3wire_csn2')
            wbctrl.add_port('adc1_adc3wire_csn3', 'adc1_adc3wire_csn3')
            wbctrl.add_port('adc1_adc3wire_csn4', 'adc1_adc3wire_csn4')
            wbctrl.add_port('adc1_adc3wire_sdata','adc1_adc3wire_sdata')
            wbctrl.add_port('adc1_adc3wire_sclk', 'adc1_adc3wire_sclk')
            top.add_port('adc1_adc3wire_csn1', 'out')
            top.add_port('adc1_adc3wire_csn2', 'out')
            top.add_port('adc1_adc3wire_csn3', 'out')
            top.add_port('adc1_adc3wire_csn4', 'out')
            top.add_port('adc1_adc3wire_sdata','out')
            top.add_port('adc1_adc3wire_sclk', 'out')
        else:
            wbctrl.add_port('adc1_adc3wire_csn1', '')
            wbctrl.add_port('adc1_adc3wire_csn2', '')
            wbctrl.add_port('adc1_adc3wire_csn3', '')
            wbctrl.add_port('adc1_adc3wire_csn4', '')
            wbctrl.add_port('adc1_adc3wire_sdata','')
            wbctrl.add_port('adc1_adc3wire_sclk', '')

        # internal connections to the adc controller. We have already declared the corresponding
        # signals earlier.
        wbctrl.add_port('adc16_reset','adc16_reset')
        wbctrl.add_port('adc16_iserdes_bitslip','adc16_iserdes_bitslip')
        wbctrl.add_port('adc16_delay_rst', 'adc16_delay_rst')
        wbctrl.add_port('adc16_delay_tap', 'adc16_delay_tap')
        wbctrl.add_port('adc16_snap_req',  'adc16_snap_req')
        wbctrl.add_port('adc16_locked',    'adc16_locked')
        # and finally the wb interface
        wbctrl.add_wb_interface(nbytes=2**16)
        top.add_instance(wbctrl)

        snap_chan = ['a','b','c','d','e','f','g','h']
        for k in range(self.num_units):
            # Embedded wb-RAM
            din = self.fullname+'_%s'%snap_chan[k]
            wbram = VerilogInstance(entity='wb_bram', name='adc16_wb_ram%d'%k, comment='Embedded ADC16 bram')
            wbram.add_parameter('LOG_USER_WIDTH','5')
            wbram.add_parameter('USER_ADDR_BITS','10')
            wbram.add_parameter('REGISTER_OUTPUT','"True"')
            wbram.add_wb_interface(nbytes=4*2**10)
            wbram.add_port('user_clk','user_clk')
            wbram.add_port('user_addr','adc16_snap_addr')
            wbram.add_port('user_din','{%s1 & %s2 & %s3 & %s4}'%(din,din,din,din))
            wbram.add_port('user_we','adc16_snap_we')
            wbram.add_port('user_dout','')
            top.add_instance(wbram)

    def gen_constraints(self):
        cons = []
        # ADC SPI interface
        cons.append(PortConstraint('adc0_adc3wire_csn1',  iogroup='zdok0', index=21))
        cons.append(PortConstraint('adc0_adc3wire_csn2',  iogroup='zdok0', index=20))
        cons.append(PortConstraint('adc0_adc3wire_csn3',  iogroup='zdok0', index=4))
        cons.append(PortConstraint('adc0_adc3wire_csn4',  iogroup='zdok0', index=40))
        cons.append(PortConstraint('adc0_adc3wire_sdata', iogroup='zdok0', index=41))
        cons.append(PortConstraint('adc0_adc3wire_sclk',  iogroup='zdok0', index=3))
        # SPI interface for the second zdok, if we're using it...
        if self.num_units > 4:
            cons.append(PortConstraint('adc1_adc3wire_csn1',  iogroup='zdok1', index=21))
            cons.append(PortConstraint('adc1_adc3wire_csn2',  iogroup='zdok1', index=20))
            cons.append(PortConstraint('adc1_adc3wire_csn3',  iogroup='zdok1', index=4))
            cons.append(PortConstraint('adc1_adc3wire_csn4',  iogroup='zdok1', index=40))
            cons.append(PortConstraint('adc1_adc3wire_sdata', iogroup='zdok1', index=41))
            cons.append(PortConstraint('adc1_adc3wire_sclk',  iogroup='zdok1', index=3))

        cons.append(PortConstraint('adc16_clk_line_p',  iogroup='zdok0_p', index=39))
        cons.append(PortConstraint('adc16_clk_line_n',  iogroup='zdok0_n', index=39))
        # older zdok revisions need a frame clock...
        
        #ZDOK pins. ZDOK differential index

        # 'a' signals
        # D7  23
        # F5  32
        # C5  12
        # A5  2
        # D11 25
        # F9  34
        # C9  14
        # F7  33
        # F15 37
        # A15 7
        # C13 16
        # A13 6
        # A19 9
        # C19 19
        # D17 28
        # A17 8

        # 'b' signals
        # C7  13
        # A7  3
        # D5  22
        # F3  31
        # C11 15
        # A11 5
        # D9  24
        # A9  4
        # D15 27
        # F13 36
        # D13 26
        # F11 35
        # D19 29
        # C17 18
        # F17 38
        # C15 17
        a_group = [
        23,
        32,
        12,
        2,
        25,
        34,
        14,
        33,
        37,
        7,
        16,
        6,
        9,
        19,
        28,
        8,
        ]

        b_group = [
        13,
        3,
        22,
        31,
        15,
        5,
        24,
        4,
        27,
        36,
        26,
        35,
        29,
        18,
        38,
        17,
        ]

        cons.append(PortConstraint('adc16_ser_a_p', iogroup='zdok0_p', index=a_group))
        cons.append(PortConstraint('adc16_ser_a_n', iogroup='zdok0_n', index=a_group))

        cons.append(PortConstraint('adc16_ser_b_p', iogroup='zdok0_p', index=b_group))
        cons.append(PortConstraint('adc16_ser_b_n', iogroup='zdok0_n', index=b_group))

        return cons

        