import time, math
from machine import deepsleep, Pin, PWM
from board import LED
# import time
# button = Pin(…)
# last_state= 0
# counter = 0
# last_time = time.ticks_ms()
# while True:
# 	state = button()
# 	t = ticks.time_ms()
# 	if (t-last_time) > 20 and state == 1 and last_state == 0:
# 		last_time = t
# 		counter += 1
# last_state =  state

count = 0
dut = 50
p = Pin('A2', mode=Pin.OUT, pull=Pin.PULL_UP)
# pwm = machine.PWM(pin=p, freq=500, duty=50)
def handler(pin):
    count+=1
    print(count)
p.irq(trigger=Pin.IRQ_RISING, handler=handler)
