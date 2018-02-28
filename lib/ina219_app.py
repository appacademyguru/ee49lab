from lib.ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
import time
import json

class INA:
    def __init__():
        i2c = I2C(id=0, scl=Pin(SCL), sda=Pin(SDA), freq=100000)

        #optional: detetct all devices connecto to I2C bus
        print("scanning I2C bus...")
        print("I2C:", i2c.scan())

        #initialize INA219
        IRC_INTERFACE_NO = 2
        SHUNT_RESISTOR_OHMS = 0.1
        self.ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
        self.ina.configure()

    # on esp32
    def data2string(**args): # ** converts args to dict
        string = json.dumps(args) #json.dumps converts dict to string
        return string

    #on host
    def string2data(string):
        data = json.loads(string) #convert back to dict
        return data

    def measure_all():
        #read measurements
        # print("Bus Voltage: %.3f V" % ina.voltage())
        # print("Current: %.3f mA" % ina.current())
        # print("Power: %.3f mW" % ina.power())
        for _ in range(30):
            v = self.ina.voltage()
            i = self.ina.current()
            p = self.ina.power()
            if i != 0:
                r = v/i
            else:
                r = 0

            msg = self.data2string(v, i, p, r)
            #mqtt.publish('data', msg)
            data = self.string2data(msg) #send string from esp32 to host with mqtt
            print("V = {:6.2f}, I = {:6.2f}, R = {:6.2f}, P={:6.2f}".format(v, i, r, p))
            time.sleep(1)
