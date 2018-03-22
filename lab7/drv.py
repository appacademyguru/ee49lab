import machine as m

#define pins
xin1 = m.Pin(id, Pin.OUT)
xin2 = m.Pin(id, Pin.OUT)
#joystick
# adcx = machine.ADC(machine.Pin(ADC5))
# adcy = machine.ADC(machine.Pin(ADC4))
# #set full-scale range
# adcx.atten(machine.ADC.ATTN_0DB)

#for current control
# RSENSE = 1000
# VREF = .2/RSENSE
#use pwm to control motors
def forward():
    xin1.init()
    pwm = m.PWM(xin2, freq=5000, duty=20)
def reverse():
    xin2.init()
    pwm = m.PWM(xin1, freq=5000, duty=20)
