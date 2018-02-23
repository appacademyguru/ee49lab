import plotserver as pls
import matplotlib.pyplot as plt
import pickle
"""
Get measurement results from microphyton board and plot on host computer.
Use in combination with mqtt_plot_mpy.py.
Install paho MQTT client and matplotlib on host , e.g.
$ pip install paho−mqtt
$ pip install matplotlib
Start this program first on the host from a terminal prompt , e.g.
$ python mqtt_plot_host.py
then run mqtt_plot_mpy.py on the ESP32.
' print ' statements throughout the code are for testing and can be removed once
verification is complete.
"""
# Important: change the line below to a unique string ,
# e.g. your name & make corresponding change in mqtt_plot_mpy.py

session = "wigglesc"
BROKER = "iot.eclipse.org"
qos = 0
# connect to MQTT broker
print("Connecting to MQTT broker", BROKER , "...", end="")
mqtt = paho.Client()
mqtt.connect(BROKER, 1883)
print("Connected!")
# initialize data vectors
# in this example we plot only 1 value , add more as needed
v = []
i = []
p = []
r = []

def appenb(d, f):  # append consecutive members of f to each member of d
    for a, i in zip(d,f):
        a.append(f[i])

with open('wigglesc.pkl', 'rb') as f:
    data = pickle.load(f)

print("received", data)
# append to data vectors , add more as needed
appenb([v,i,p,r], data)

print("plotting ...")
fig = pyplot.figure()
axes = fig.gca()
plt.plot(v, i, p, r)
print("show plot ...")
# show plot on screen
plt.show(fig)
