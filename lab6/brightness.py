import time, math
import machine
from board import LED, A12


dut = 0
led = machine.Pin(LED, mode=machine.Pin.OPEN_DRAIN)
led(0)
pwm = machine.PWM(led, freq=500)
pwm.duty(dut)

def lcb(timer):
    global dut
    global pwm
    if dut < 100:
        dut += 1
    else:
        dut = 0
    pwm.duty(dut)
t0 = machine.Timer(2)
t0.init(period=50, mode=t0.PERIODIC, callback=lcb)
