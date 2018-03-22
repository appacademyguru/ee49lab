import time, math
import machine
from board import A20, A21
pwm = machine.PWM(machine.Pin(A20), freq=5000, duty=20)
pwm1 = machine.PWM(machine.Pin(A21), freq=8000, duty=60)
