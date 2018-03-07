from time import sleep
from machine import deepsleep, Pin
from board import LED

def handler(pin):


p = Pin(A2, mode=Pin.IN)
p.irq(handler, trigger=Pin.IRQ_RISING)
led = Pin(LED, mode=Pin.OUT)



led(1)
print("awake")
sleep(60)
print("deepsleep")
led(0)
deepsleep(60000)
