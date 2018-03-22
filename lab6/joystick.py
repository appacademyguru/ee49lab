import time, math
import machine
from board import ADC5, ADC4


adcx = machine.ADC(machine.Pin(ADC5))
adcy = machine.ADC(machine.Pin(ADC4))
#set full-scale range
adcx.atten(machine.ADC.ATTN_0DB)

for val in range(0, 256):
    # dac1.write(val)
    #perform conversion
    x = adcx.read() #0 - 4095
    y = adcy.read()
    # vout = (val/255)*3.3
    print("x: {}, y: {}".format(x, y))
    time.sleep_ms(1000)
