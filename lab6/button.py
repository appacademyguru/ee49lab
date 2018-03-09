import time, math
from machine import deepsleep, Pin, PWM
from board import LED, A12

last_time = time.ticks_ms()

count = 0
dut = 50
p = Pin(A12, mode=Pin.OUT, pull=Pin.PULL_UP)
# pwm = machine.PWM(pin=p, freq=500, duty=50)
def handler(pin):
    global count
    t = time.ticks_ms()
    if(t-last_time) > 20:
        last_time = t
        count+=1
        print(count)
p.irq(trigger=Pin.IRQ_RISING, handler=handler)
