import time, math
import machine
from board import ADC0

# x_pin = machine.Pin()#ADC PINS: A2, A3, A4, A7(32), A9(33)
# y_pin= machine.Pin()
# button_pin = machine.Pin()
# button = machine.Pin(button_pin, machine.Pin.OUT, pull=machine.Pin.PULL_UP)
# x_axis = machine.ADC(x_pin)
# y_axis = machine.ADC(y_pin)

adc0 = machine.ADC(Pin(ADC0))
#set full-scale range
adc0.atten(ADC.ATTN_0DB)

#DAC: A0, A1
dac1 = machine.DAC(1)#pin A1
# dac.write(128) #write a val to the DAC, 1.56 V = 128

# x_val = x_axis.read() #1024 = 1V
# y_val = y_axis.read()

for val in range(0, 256):
    dac1.write(val)
    #perform conversion
    code = 4095*(adc0.read()/1.1)
    vout = (val/255)*3.3
    print("DAC: {} Volts, ADC: {}".format(vout, code))
