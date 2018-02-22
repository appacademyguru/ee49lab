from mqttclient import *
from time import sleep
#Connect
# BROKER = "iot.eecs.berkeley.edu"
# USER = "iot49"
# PWD = "rocks"

BROKER = "iot.eclipse.org"
broker = str(BROKER)
USER = ""
PWD = ""

print("Connecting to broker", "iot.eclipse.org", "...") #this is where it stops working
# mqtt = MQTTClient("iot.eclipse.org")
#that's the error i keep getting
# *** Syntax: ('exception', b'Connecting to broker iot.eclipse.org ...\r\n', b'Traceback (most recent call last):\r\n  File "<stdin>", line 24, in <module>\r\n  File "mqttclient.py", line 64, in connect\r\nOSError: 23\r\n')

mqtt = MQTTClient("iot.eclipse.org", user=USER, password=PWD, ssl=False)
def mqtt_callback(topic, msg):
    print("RECEIVE topic = {}, msg = {}".format(topic, msg))

mqtt.set_callback(mqtt_callback) # the error is on this line but it's in one of the mqttclient files
mqtt.connect("iot.eclipse.org")
print("Connected!")
#Publish-subscribe loop
for i in range(100):
    topic = "iot49/esp32"
    message = "hello " + str(i)
    mqtt.subscribe("iot49/esp32", mqtt_callback)
    print("PUBLISH topic = {} message = {}".format(topic, message))
    mqtt.publish(topic, message)
    for _ in range(10):
        mqtt.check_msg()
        sleep(0.5)
