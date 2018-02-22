from board import LED
from machine import Pin
from time import sleep

led = Pin(LED, mode=Pin.OUT)

def morse(num, slp):
    for _ in range(num):
        led(1)
        sleep(slp)
        led(0)
        sleep(0.5)

while True:
    # · · · - - - · · ·
    # S
    morse(3, 0.25)
    # O
    morse(3, 1)
    # S
    morse(3, 0.25)
    sleep(1)
