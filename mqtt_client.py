from mqttclient import MQTTClient
from time import sleep
#Connect
# BROKER = "iot.eecs.berkeley.edu"
# USER = "iot49"
# PWD = "rocks"

BROKER = "iot.eclipse.org"
broker = str(BROKER)
USER = ""
PWD = ""

print("Connecting to broker", BROKER, "...")
mqtt = MQTTClient(BROKER)
# mqtt = MQTTClient(BROKER, user=USER, password=PWD, ssl=True)
# client = mqtt.Client(USER)

def mqtt_callback(topic, msg):
    print("RECEIVE topic = {}, msg = {}".format(topic, msg))

# client.on_message = mqqt_callback
# client.connect(BROKER)
mqtt.set_callback(mqtt_callback)
mqtt.connect(broker)
print("Connected!")
mqtt.subscribe("guru/esp32")
# mqtt.subscribe("iot49/b")
#Publish-subscribe loop
for i in range(100):
    topic = "guru/esp32"
    message = "hello " + str(i)
    print("PUBLISH topic = {} message = {}".format(topic, message))
    mqtt.publish(topic, message)
    for _ in range(10):
        mqtt.check_msg()
        sleep(0.5)
