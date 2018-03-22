import machine as m
from board import ADC4, ADC5, SCL, SDA, A5
import mpu9250
#pins - need 4 for drv, 2 for encoders
A6 = 19#14
A10 = 23#27
A8 = 21#15
A5 = 10#A5
A15 = 18#scl
A14 = 17#SDA
A18 = 13#MI
A19 = 14#RX
A20 = 15#TX
A21 = 16#21


#define pins
#motor A
Ain1 = m.Pin(, Pin.OUT)
Ain2 = m.Pin(id, Pin.OUT)
#motor B
Bin1 = m.Pin(id, Pin.OUT)
Bin2 = m.Pin(id, Pin.OUT)
#define pwm
fwdA = m.PWM(Ain1, freq=9000)
fwdB = m.PWM(Bin1, freq=9000)
rvsA = m.PWM(Ain2, freq=9000)
rvsB = m.PWM(Bin2, freq=9000)
#define encoders
encA = m.ENC()
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
    global adcx, adcy
    x = adcx.read()/40.95
    y = adcy.read()/40.95
    if
    pwm1.duty(x)
    pwm2.duty(y)

t0 = machine.Timer(2)
t0.init(period=50, mode=t0.PERIODIC, callback=drive)

#MPU9250
i2c = m.I2C(scl=m.Pin(A15), sda=m.Pin(A14))
mpu = MPU9250(i2c)
def measure():
    #acceleration, rate, magnetic field
    accel, gyro, mag = mpu.sensors()
    print("Acceleration: {}, Rate: {}, Mag-Field: {}".format(accel,gyro,mag))
    #temp
    print(mpu.temperature())

t1 = machine.Timer(3)
t1.init(period=200, mode=t1.PERIODIC, callback=measure)
