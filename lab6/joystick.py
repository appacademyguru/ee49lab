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
    x = 4095*(adcx.read()/1.1)
    y = 4095*(adcy.read()/1.1)
    # vout = (val/255)*3.3
    print("x: {}, y: {}".format(x, y))
    time.sleep_ms(1000)
