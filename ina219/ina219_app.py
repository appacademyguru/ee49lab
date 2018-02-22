from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
import time

i2c = I2C(id=0, scl=Pin(SCL), sda=Pin(SDA), freq=100000)

#optional: detetct all devices connecto to I2C bus
print("scanning I2C bus...")
print("I2C:", i2c.scan())

#initialize INA219
IRC_INTERFACE_NO = 2
SHUNT_RESISTOR_OHMS = 0.1
ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
ina.configure()

#read measurements
# print("Bus Voltage: %.3f V" % ina.voltage())
# print("Current: %.3f mA" % ina.current())
# print("Power: %.3f mW" % ina.power())
for _ in range(30):
    v = ina.voltage()
    i = ina.current()
    p = ina.power()
    if i != 0:
        r = v/i
    else:
        r = 0
    print("V = {:6.2f}, I = {:6.2f}, R = {:6.2f}, P={:6.2f}".format(v, i, r, p))
    time.sleep(1)
