#!/usr/bin/env python
# modified from: http://pymodbus.readthedocs.org/en/latest/examples/synchronous-client.html

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging
import argparse
import subprocess
import time
import sys

def get_args():
	parser = argparse.ArgumentParser(description='Copies a given file')
	parser.add_argument('-s', dest='slave_addr', help='Address of the slave device', default='localhost', required=True)
	parser.add_argument('-d', dest='debug', help='Enable debugging', action="store_true", default=False)
	args = parser.parse_args()

	# if the -d flag is set (True), configure logging
	if args.debug:
		logging.basicConfig()
		log = logging.getLogger()
		log.setLevel(logging.DEBUG)

	# read arguments (the address of the server)
	return args

def enable_light(temp):
	"""
	Enables the red or green light, depending on the temp
	@param temp - the value of the temperature in degrees Fahrenheit * 100
	"""
	# Initialize pins for output
	subprocess.call(['gpio', 'mode', '0', 'out'])
	subprocess.call(['gpio', 'mode', '1', 'out'])

	# If higher, write 1 to red LED, if lower write 1 to green LED
	if int(temp) > 7400:
		subprocess.call(['gpio', 'write', '0', '1'])
		subprocess.call(['gpio', 'write', '1', '0'])
		print "GREATER"	
	else:
		subprocess.call(['gpio', 'write', '1', '1'])
		subprocess.call(['gpio', 'write', '0', '0'])
		print "LESS"
	print temp

def main():
	args = get_args()

	# connect to modbus slave
	client = ModbusClient(args.slave_addr, port=502)
	client.connect()

	# get value of holding registers (first has the temperature value)
	rr = client.read_holding_registers(0x00,1,unit=1)
	temp = rr.registers[0]
	try:
		while True:
			enable_light(temp)
			time.sleep(3)
	except KeyboardInterrupt:
		subprocess.call(['gpio', 'write', '0', '0'])
		subprocess.call(['gpio', 'write', '1', '0'])
		print "Exiting..."

if __name__ == '__main__':
	main()

