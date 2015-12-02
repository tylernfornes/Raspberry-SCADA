#!/usr/bin/env python
# modified from: http://pymodbus.readthedocs.org/en/latest/examples/synchronous-client.html
'''
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

    with ModbusClient('127.0.0.1') as client:
        result = client.read_coils(1,10)
        print result
'''
#---------------------------------------------------------------------------# 
# import the various server implementations
#---------------------------------------------------------------------------# 
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

#---------------------------------------------------------------------------# 
# configure the client logging
#---------------------------------------------------------------------------# 
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#---------------------------------------------------------------------------# 
# choose the client you want
#---------------------------------------------------------------------------# 
client = ModbusClient('10.80.100.54', port=502)
client.connect()

#---------------------------------------------------------------------------# 
# specify slave to query
#---------------------------------------------------------------------------# 
# The slave to query is specified in an optional parameter for each
# individual request. This can be done by specifying the `unit` parameter
# which defaults to `0x00`
#---------------------------------------------------------------------------# 
#rr = client.read_coils(1, 1, unit=0x02)
print "ABOUT TO GET HOLDING REGISTERS"
#rr = client.read_holding_registers(1,10)
rr = client.read_holding_registers(0x00,1,unit=1)
print rr.registers
#
##---------------------------------------------------------------------------# 
## example requests
##---------------------------------------------------------------------------# 
## simply call the methods that you would like to use. An example session
## is displayed below along with some assert checks. Note that some modbus
## implementations differentiate holding/input discrete/coils and as such
## you will not be able to write to these, therefore the starting values
## are not known to these tests. Furthermore, some use the same memory
## blocks for the two sets, so a change to one is a change to the other.
## Keep both of these cases in mind when testing as the following will
## _only_ pass with the supplied async modbus server (script supplied).
##---------------------------------------------------------------------------# 
#rq = client.write_coil(1, True)
#rr = client.read_coils(1,1)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits[0] == True)          # test the expected value
#
#rq = client.write_coils(1, [True]*8)
#rr = client.read_coils(1,8)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits == [True]*8)         # test the expected value
#
#rq = client.write_coils(1, [False]*8)
#rr = client.read_discrete_inputs(1,8)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.bits == [False]*8)         # test the expected value
#
#rq = client.write_register(1, 10
#
#)
#rr = client.read_holding_registers(1,1)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers[0] == 10)       # test the expected value
#
#rq = client.write_registers(1, [10]*8)
#rr = client.read_input_registers(1,8)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rr.registers == [10]*8)      # test the expected value
#
#arguments = {
#    'read_address':    1,
#    'read_count':      8,
#    'write_address':   1,
#    'write_registers': [20]*8,
#}
#rq = client.readwrite_registers(**arguments)
#rr = client.read_input_registers(1,8)
#assert(rq.function_code < 0x80)     # test that we are not an error
#assert(rq.registers == [20]*8)      # test the expected value
#assert(rr.registers == [20]*8)      # test the expected value
#
##---------------------------------------------------------------------------# 
## close the client
##---------------------------------------------------------------------------# 
client.close()

