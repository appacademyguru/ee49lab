import time, math
from machine import deepsleep, Pin, PWM
from board import LED


count = 0
dut = 50
p = Pin(A2, mode=Pin.OUT, pull=Pin.PULL_UP)
p.init(p.OUT)
pwm = machine.PWM(pin=p, freq=500, duty=50)
def led_cb():
    global dut
    if dut < 100:
        dut += 1
    else:
        duty = 50
    pwm.duty(dut)
def lcb(timer):
    global count
    if count & 1:
        p.value(0)
    else:
        p.value(1)
    count += 1
    if (count % 5000) ==0:
        print("[tcb] timer: {} counter: {}".format(timer.timernum(), count))
        led_cb()
t0 = machine.Timer(2)
t0.init(period=20, mode=t0.PERIODIC, callback=lcb)
