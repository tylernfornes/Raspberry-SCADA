#!/usr/bin/env python
#Author: Tyler Fornes
#File: temp_scraper.py
#Function: Raspi temp scraper for BACnet SCADA implementation
#Adapted from: 
# https://projects.drogon.net/raspberry-pi/gpio-examples/tux-crossing/2-two-more-leds/
# http://www.modmypi.com/blog/ds18b20-one-wire-digital-temperature-sensor-and-the-raspberry-pi 
import subprocess
import time
import sys

try: 
    while True:
        # Initialize pins for output
        subprocess.call(['gpio', 'mode', '0', 'out'])
        subprocess.call(['gpio', 'mode', '1', 'out'])
        # Open the file temp is stored in
        temp_file = open('/sys/bus/w1/devices/28-000006efeb10/w1_slave')
        # Read line containing tempurature
        line = temp_file.readlines() 
        # Close the file
        temp_file.close()
        # Parse tempurature from read
        temp = line[1]
        temp=temp[29:]
        # Determine if higher or lower than 70 degrees F (sensor reads Celsius)
        # If higher, write 1 to red LED, if lower write 1 to green LED
        if int(temp) > 21111:
            subprocess.call(['gpio', 'write', '0', '1'])
            subprocess.call(['gpio', 'write', '1', '0'])
            print "GREATER"    
        else:
            subprocess.call(['gpio', 'write', '1', '1'])
            subprocess.call(['gpio', 'write', '0', '0'])
            print "LESS"
        print temp
        time.sleep(3)
except KeyboardInterrupt:
    # disable the lights
    subprocess.call(['gpio', 'write', '0', '0'])
    subprocess.call(['gpio', 'write', '1', '0'])
    sys.exit(0)
    
