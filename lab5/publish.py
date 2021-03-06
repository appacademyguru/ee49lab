from mqttclient import MQTTClient
from math import sin
import network
import sys

session = "wigglesc"
BROKER = "mqtt.thingspeak.com"

TS_CHANNEL_ID = '437688'
TS_WRITE_KEY = 'UU8PB5LQU09GHLN2'
topic = "channels/" + TS_CHANNEL_ID + "/publish/" + TS_WRITE_KEY
############################# WIFI #######################################################
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == '0.0.0.0 ':
    print("no wifi connection")
    sys.exit()
else:
    print("connected to WiFi at IP", ip)

print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = MQTTClient(BROKER, user="", password="", ssl=True)
print("connected!")

############################# INA219 #######################################################
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

for _ in range(100):
    v=ina.voltage()
    i=ina.current()
    message = "field1={}&field2={}".format(v, i)
    print("PUBLISH topic = {}, msg = {}".format(topic, message))
    mqtt.publish(topic, message)
    print("published")
    time.sleep(15)
    # add additional values as required by application


mqtt.disconnect()
