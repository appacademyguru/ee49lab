import time, machine, board

led = machine.Pin(2, mode=Pin.OUT, pull=Pin.PULL_UP)
p = machine.Pin(27, mode=Pin.OUT, pull=Pin.PULL_UP)
pwm = machine.PWM(pin=led, freq=500, duty=50)
pwm1 = machine.PWM(pin=p, freq=500, duty=50)
# define frequency for each tone
C3 = 131
CS3 = 139
D3 = 147
DS3 = 156
E3 = 165
F3 = 175
FS3 = 185
G3 = 196
GS3 = 208
A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587
DS5 = 622
E5 = 659
F5 = 698
FS5 = 740
G5 = 784
GS5 = 831
A5_ = 880
AS5 = 932
B5 = 988
C6 = 1047
CS6 = 1109
D6 = 1175
DS6 = 124
E6 = 1319
F6 = 1397
FS6 = 1480
G6 = 1568
GS6 = 1661
A6 = 1760
AS6 = 1865
B6 = 1976
C7 = 2093
CS7 = 2217
D7 = 2349
DS7 = 2489
E7 = 2637
F7 = 2794
FS7 = 2960
G7 = 3136
GS7 = 3322
A7 = 3520
AS7 = 3729
B7 = 3951
C8 = 4186
CS8 = 4435
D8 = 4699
DS8 = 4978
rest = 0
q = 1000
h = 2000
e = 500
w = 4000
s = 250
bach = [ C4, E4, G4, C5, E5, rest, G4, C5, E5, C4, E4,rest, G4, C5, E5, G4, C5, E5, C4, D4, G4, D5, F5, G4, D5, F5, C4, D4, G4, D5, F5, G4, D5, F5, B3, D4, G4, D5, F5, G4, D5, F5, B3, D4, G4, D5, F5, G4, D5, F5, C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, G4, C5, E5, G4, C5, E5, C4, E4, A4, E5, A5_, A4, E5, A4, C4, E4, A4, E5, A5_, A4, E5, A4, C4, D4, FS4, A4, D5, FS4, A4, D5, C4, D4, FS4, A4, D5, FS4, A4, D5, B3, D4, G4, D5, G5, G4, D5, G5, B3, D4, G4, D5, G5, G4, D5, G5, B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5, B3, C4, E4, G4, C5, E4, G4, C5, A3, C4, E4, G4, C5, E4, G4, C5, A3, C4, E4, G4, C5, E4, G4, C5, D3, A3, D4, FS4, C5, D4, FS4, C5, D3, A3, D4, FS4, C5, D4, FS4, C5, G3, B3, D4, G4, B4, D4, G4, B4, G3, B3, D4, G4, B4, D4, G4, B4 ]
def led_cb():
    dut = pwm.duty()
    if dut < 100:
        dut += 1
    else:
        dut = 50
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

def buzz_cb(song, length):
    for note in song:
        p.freq(note)
        time.sleep_ms(length)
def bcb(timer):
    buzz_cb(bach, 500)
t0 = machine.Timer(2)
t0.init(period=20, mode=t0.PERIODIC, callback=lcb)
t1 = machine.Timer(2)
t1.init(period=20, mode=t1.PERIODIC, callback=bcb)
