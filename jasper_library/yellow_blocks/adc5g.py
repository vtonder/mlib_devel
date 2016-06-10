from yellow_block import YellowBlock
from verilog import VerilogModule
from constraints import PortConstraint, ClockConstraint


#when te the adc5g somewhere (don't know where yet) need to pass it the yellowblock object (don't know why yet)
#3 spaces for a def is standard
class adc5g(yellowblock)
   #need to add sources at a minimum
   def initialize(self):
       #add_source is defined in 
       self.add_source('adc5g_dmux1_interface_v1_00_a')


   def modify_top(self,top):

   def port_constraints(self): 







