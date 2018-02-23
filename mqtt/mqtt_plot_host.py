import paho.mqtt.client as paho
import matplotlib.pyplot as plt
from plotclient import PlotClient
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
mqtt.connect(BROKER , 1883)
print("Connected!")
# initialize data vectors
# in this example we plot only 1 value , add more as needed
mp = PlotClient(mqtt, session)
mp.new_series(SERIES, 'time', 'sin')
t=[]
s=[]
SERIES = "sinusoid"
# mqtt callbacks
def data(c, u, message ):
    # extract data from MQTT message
    msg = message.payload.decode(' ascii ')
    # convert to vector of floats
    f = [float(x) for x in msg.split(' , ')]
    print("received", f)
    # append to data vectors , add more as needed
    t.append(f[0])
    s.append(f[1])

def plot(client , userdata , message ):
    # customize this to match your data
    print("plotting ...")
    mp.data(SERIES, t, s)
    # plt.plot(t, s, ' rs ')
    # plt.xlabel(' Time ')
    # plt.ylabel(' Sinusoid ')
    print("show plot ...")
    # show plot on screen
    # 3
    plt.show()
for _ in range(300):
    # subscribe to topics
    data_topic = "{}/data".format(session, qos)
    plot_topic = "{}/plot".format(session, qos)
    mqtt.subscribe(data_topic)
    mqtt.subscribe(plot_topic)
    mqtt.message_callback_add(data_topic, data)
    mqtt.message_callback_add(plot_topic, plot)
    # wait for MQTT messages
    # this function never returns
    print("waiting for data ...")

    mp.save_series(SERIES)
    mp.plot_series(SERIES,
        filename="mqtt_plotter_example.pdf",
        xlabel="Time [s]",
        ylabel="Sinusoid",
        title=r"\sin(t)$")
