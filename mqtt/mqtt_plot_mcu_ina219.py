from mqttclient import MQTTClient
from math import sin
import network
import sys
from plotclient import PlotClient
"""
Send measurement results from micropython board to host computer.
Use in combination with mqtt_plot_host.py.
' print ' statements throughout the code are for testing and can be removed once
verification is complete.
"""
# Important: change the line below to a unique string ,
# e.g. your name & make corresponding change in mqtt_plot_host.py
session = "wigglesc"
BROKER = "iot.eclipse.org"

# check wifi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
ip = wlan.ifconfig()[0]
if ip == '0.0.0.0':
    print("no wifi connection")
    sys.exit()
else:
    print("connected to WiFi at IP", ip)
# connect to MQTT broker
print("Connecting to MQTT broker", BROKER , "...", end="")
mqtt = MQTTClient("iot.eclipse.org")
print("Connected!")
############################# Plot Client#######################################################
mqtt = MQTTClient("iot.eclipse.org")
mp = PlotClient(mqtt, session)

SERIES = "data"
############################# DATA #######################################################
# initialize ina219
from ina219 import INA219
from machine import I2C, Pin
from board import SDA, SCL
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
# # on esp32
# def data2string(**args): # ** converts args to dict
#     string = json.dumps(args) #json.dumps converts dict to string
#     return string
# #on host
# def string2data(string):
#     data = json.loads(string) #convert back to dict
#     return data
############################# MEASUREMENTS #######################################################
#read measurements
# print("Bus Voltage: %.3f V" % ina.voltage())
# print("Current: %.3f mA" % ina.current())
# print("Power: %.3f mW" % ina.power())
#measure, subscribe, publish plot_load_pkl
mp.new_series(SERIES, 'v', 'i', 'p', 'r')
while i is not false:
    v = ina.voltage()
    i = ina.current()
    p = ina.power()
    if i != 0:
        r = v/i
    r = 0
    if r > 8:
        i = flase
    print("V = {:6.2f}, I = {:6.2f}, R = {:6.2f}, P={:6.2f}".format(v, i, r, p))
    mp.data(SERIES, v, i, p, r)
    time.sleep(0.5)

mp.save_series(SERIES)


# free up resources
# alternatively reset the micropython board before executing this program again
mqtt.disconnect()