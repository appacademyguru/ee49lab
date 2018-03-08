import time, math
import machine, board
# x_pin = machine.Pin('')
# y_pin= machine.Pin('')
# button_pin = machine.Pin('')
# button = machine.Pin(button_pin, machine.Pin.OUT, pull=machine.Pin.PULL_UP)
# x_axis = machine.ADC(x_pin)
# y_axis = machine.ADC(y_pin)

adc = machine.ADC('A2')
value = adc.read()
