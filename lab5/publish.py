
# prerequisites:
# - Thingspeak account
# - Thingspeak channel to publish data
# - Thinkspeak Write API Key for the channel
# - Thinkspeak MQTT API Key for the account
#

import network
import os
import gc
############ina219########################
from mqttclient import MQTTClient
from machine import I2C, Pin
from board import SDA, SCL
import time
import json
import sys
from ina219 import INA219
############ina219########################
#
# WiFi connection information
#
wifiSSID = "megan's laptop"          # EDIT - enter name of WiFi connection point
wifiPassword = "285F>6e3"
# wifiSSID = "EECS-PSK"          # EDIT - enter name of WiFi connection point
# wifiPassword = "Thequickbrown"  # EDIT - enter WiFi password

#
# turn off the WiFi Access Point
#
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

#
#   connect the ESP8266 device to the WiFi network
#
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(wifiSSID, wifiPassword)

#
# wait until the ESP8266 is connected to the WiFi network
#
maxAttempts = 20
attemptCount = 0
while not wifi.isconnected() and attemptCount < maxAttempts:
  attemptCount +=1
  time.sleep(1)
  print('did not connect...trying again')

#
# create a random MQTT clientID
#
randomNum = int.from_bytes(os.urandom(3), 'little')
myMqttClient = bytes("client_"+str(randomNum), 'utf-8')

#
# connect to Thingspeak MQTT broker
# connection uses unsecure TCP (port 1883)
#
# Steps to change to a secure connection (encrypted) using TLS
#   a) change port below to "port=8883
#   b) add parameter "ssl=True"
#   Note:  TLS uses about 9k bytes of the heap. That is a lot.
#          (about 1/4 of the micropython heap on the ESP8266 platform)
#
thingspeakUrl = b"mqtt.thingspeak.com"
thingspeakUserId = b"megan2651"          # EDIT - enter Thingspeak User ID
thingspeakMqttApiKey = b"SG175MRDQUTWZNQA" # EDIT - enter Thingspeak MQTT API Key
client = MQTTClient(client_id=myMqttClient,
                    server=thingspeakUrl,
                    user=thingspeakUserId,
                    password=thingspeakMqttApiKey,
                    port=1883)

client.connect()

# ############################################################################################################
from lib.ina219_app import *
def measure_vi():
    # ina = INA()

    #read measurements
    # print("Bus Voltage: %.3f V" % ina.voltage())
    # print("Current: %.3f mA" % ina.current())
    # print("Power: %.3f mW" % ina.power())
    for _ in range(30):
        # v = ina.voltage()
        # i = ina.current()
        v = 1
        i = 2
        print("V = {:6.2f}, I = {:6.2f}, R = {:6.2f}, P={:6.2f}".format(v, i, r, p))
        credentials = bytes("channels/{:s}/publish/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey), 'utf-8')
        payload = bytes("field1={:.1f}&field2={:.1f}\n".format(v, i), 'utf-8')
        client.publish(credentials, payload)
        time.sleep(publishPeriodInSec)
###############################################################################################################
#
# publish data to Thingspeak using MQTT
#
thingspeakChannelId = b"437688"             # EDIT - enter Thingspeak Channel ID
thingspeakChannelWriteApiKey = b"UU8PB5LQU09GHLN2" # EDIT - enter Thingspeak Write API Key
publishPeriodInSec = 30
while True:
    measure_vi()

client.disconnect()
