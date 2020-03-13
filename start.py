#
#
# Made for Python 3
# Copyright (c) 2020 Cisco Systems, Inc. and/or its affiliates
#


import configparser
import os                      
from pyModbusTCP.client import ModbusClient
from time import sleep
from random import randint

# Read the package_config.ini file that contains the PLC IP address
config_file_dir = os.getenv("CAF_APP_CONFIG_DIR",".")
config_file_path = os.path.join(config_file_dir,"package_config.ini")

cfg = configparser.ConfigParser()
cfg.read(config_file_path)

# Read the "IP_Address" variable in the "PLC" section
if (cfg['PLC']['IP_Address'] != ''):
    ip_addr = cfg['PLC']['IP_Address']
    print("IP address acquired from package_config.ini")
else:
     # If none found, then use a default
     print("No IP address found in package_config.ini, using default")
     ip_addr = "192.168.2.167"

print("Using IP: " + ip_addr)

# Configure ModBus TCP connection to the specificed target IP address
c = ModbusClient(host=ip_addr, port=502, auto_open=True)

# This is based on how your PLC has been configured
# Refer to your Modbus Exchange table for exact base address
r_addr_hex = "0008"
r_addr_dec = int(r_addr_hex, 16)

# For our Knight Rider effect we will use 6 registers from 0 to 5
# Need to enter the max register # (that is the number of registers - 1)
max_registers = 5; 

# n = the current register we will trigger on then off
n = 0; 

# i = the increment. 
#   i = 1 when we move up from a lower to a higher register
#   i = -1 when we move down from a higher to a lower register
i = -1;

# Infinite loop
while True:
    print(n)

    # Turn on register "n"
    if not c.write_single_coil(r_addr_dec+n, 1):
        print("write error")

    # Read and display all the registers
    regs = c.read_coils(r_addr_dec, bit_nb=max_registers+1)
    if regs:
        print(regs)
    else:
        print("read error") 
    
    # Amount of time to keep the register on
    sleep(0.05)

    # Turn off the register
    if not c.write_single_coil(r_addr_dec+n, 0):
        print("write error")
    
    # When we need to change direction, swap i for -i
    if ((n>=max_registers) or (n<=0)):
        i=-i

    # Increment, will do either +1 or -1 depending on direction
    n=n+i
    
       