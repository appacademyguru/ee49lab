import paho.mqtt.client as paho
import matplotlib.pyplot as plt
import ast

session="wigglesc"
BROKER = "iot.eclipse.org"
qos = 0


print("Connecting to MQTT broker", BROKER, "...", end="")
mqtt = paho.Client()
mqtt.connect(BROKER, 1883)
print("Connected!")

p = []
r = []

def data(c, u, message):
  msg= message.payload.decode('ascii')
  msg = ast.literal_eval(msg)#turn askey payload into list
  for s in msg[0]:#unpack resistance data
      r.append(float(s))
  for t in msg[1]:#unpack power data
      p.append(float(t))
  print(p)
  print(r)
  # f = [str(x) for x in msg.split(', ') ]
  # print(f)
  # h = [ float(x) for x in ]
  # print("received", h)


def plot(client, userdata, message):
  print("plotting ...")
  plt.plot(r, p, 'rs')
  plt.xlabel( 'Resistance')
  plt.ylabel( 'Power')
  print("show plot ...")
  plt.show()

data_topic = "{}/data".format(session, qos)
plot_topic = "{}/plot".format(session, qos)
mqtt.subscribe(data_topic)
mqtt.subscribe(plot_topic)
mqtt.message_callback_add(data_topic, data)
mqtt.message_callback_add(plot_topic, plot)

print("waiting for data ...")
mqtt.loop_forever()
