#!/usr/bin/env python
# modified from: http://pymodbus.readthedocs.org/en/latest/examples/synchronous-client.html

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import argparse

def get_args():
	parser = argparse.ArgumentParser(description='Copies a given file')
	parser.add_argument('-s', dest='slave_addr', help='Address of the slave device', default='localhost', required=True)

	# read arguments (the address of the server)
	return parser.parse_args()


def main():
	args = get_args()

	# configure logging
	logging.basicConfig()
	log = logging.getLogger()
	log.setLevel(logging.DEBUG)

	# connect to modbus slave
	client = ModbusClient(args.slave_addr, port=502)
	client.connect()

	# get value of holding registers (first has the temperature value)
	rr = client.read_holding_registers(0x00,1,unit=1)
	print str(type(rr.registers[0]))

if __name__ == '__main__':
	main()
