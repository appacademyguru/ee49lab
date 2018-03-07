from mqttclient import MQTTClient
from math import sin
import network
import sys

session = "wigglesc"
BROKER = "iot.eclipse.org"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == '0.0.0.0 ':
    print("no wifi connection")
    sys.exit()
else:
    print("connected to WiFi at IP", ip)

print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = MQTTClient(BROKER)
print("connected!")


# initialize ina219
from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
# from ina219_app import INA
import time
import json

i2c = I2C(id=0, scl=Pin(SCL), sda=Pin(SDA), freq=100000)

#optional: detetct all devices connecto to I2C bus
print("scanning I2C bus...")
print("I2C:", i2c.scan())

#initialize INA219
IRC_INTERFACE_NO = 2
SHUNT_RESISTOR_OHMS = 0.1
ina = INA219(SHUNT_RESISTOR_OHMS, i2c)
ina.configure()
# ina = INA()
############################# MEASUREMENTS #######################################################
v=[]
i=[]
p=[]
r=[]
for _ in range(100):
    v.append(ina.voltage())
    i.append(ina.current())
    p.append(ina.power())
    if ina.current() != 0:
        r.append(ina.voltage()/ina.current())
    else:
        r.append(0)
    # add additional values as required by application
topic = "{}/data".format(session)
data = "{} , {}".format(r, p)
print("send topic = '{} ' data = '{} ' ".format(topic, data))
mqtt.publish(topic, data)
# do the plotting (on host)
print("tell host to do the plotting ...")
mqtt.publish("{}/plot".format(session), "create the plot")

mqtt.disconnect()
