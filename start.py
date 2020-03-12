from pyModbusTCP.client import ModbusClient
from time import sleep
from random import randint

c = ModbusClient(host="192.168.2.167", port=502, auto_open=True)

r_addr_hex = "0008"
r_addr_dec = int(r_addr_hex, 16)
print(r_addr_dec)


while True:

    # Write value 
    if c.write_single_coil(r_addr_dec+randint(0,6), randint(0,1)):
        print("write ok")
    else:
        print("write error")

    # Read 2x 16 bits registers at modbus address 0 :
    regs = c.read_coils(r_addr_dec, bit_nb=6)
    if regs:
        print(regs)
    else:
        print("read error") 
    
    sleep(1/randint(3,10))
