from plotclient import PlotClient
from mqttclient import MQTTClient
from math import sin, cos, exp, pi

mqtt = MQTTClient("iot.eclipse.org")
mp = PlotClient(mqtt, session="hopla")

#give series unique name
SERIES = "sinusoid"

#data column names
mp.new_series(SERIES, 'time', 'cos', 'sin', 'sin*cos')

#generate data
def f1(t): return cos(2* pi *t) * exp(-t)
def f2(t): return sin(2 * pi *t) *exp(-t)
def f3(t): return sin(2 * pi *t) * cos(2* pi *t) * exp(-t)

for t in range(200):
    t *= 0.025
    #submit each datapoint to the plot server
    mp.data(SERIES, t, f1(t), f2(t), f3(t))

#save data as a pkl document
#see plot_load_pkl.py for an example of loading it back into python
mp.save_series(SERIES)

#create a plot, default dir is $IoT49
mp.plot_series(SERIES,
    filename="mqtt_plotter_example.pdf",
    xlabel="Time [s]",
    ylabel="Voltage [mV]",
    title=r"Damped exponential decay $e^{-t} \cos(2\pi t)$")
