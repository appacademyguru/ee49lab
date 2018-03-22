import machine as m
from board import ADC4, ADC5
#define pins
xin1 = m.Pin(id, Pin.OUT)
xin2 = m.Pin(id, Pin.OUT)
pwm1 = m.PWM(xin1, freq=9000)
pwm2 = m.PWM(xin2, freq=9000)
#joystick
adcx = machine.ADC(machine.Pin(ADC5))
adcy = machine.ADC(machine.Pin(ADC4))
#set full-scale range
adcx.atten(machine.ADC.ATTN_0DB)

#for current control
# RSENSE = 1000
# VREF = .2/RSENSE
#use pwm to control motors
MAX = 4095/40.95
MIN = 0
def forward(speed):
    xin1.init()
    pwm1.duty(speed)
def reverse(speed):
    xin2.init()
    pwm2.duty(speed)
def drive():
    global adcx, adcy, xin1, xin2, pwm1, pwm2
    x = adcx.read()/40.95
    y = adcy.read()/40.95
    pwm1.duty(x)
    pwm.duty(y)

t0 = machine.Timer(2)
t0.init(period=50, mode=t0.PERIODIC, callback=drive)
