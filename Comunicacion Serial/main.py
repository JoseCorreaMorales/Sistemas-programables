from machine import Pin
from select import select
from sys import stdin
from time import sleep
#time.sleep(0.1) # Wait for USB to become ready

led = Pin(25, Pin.OUT)
led.value(1)

while True:
    if select([stdin], [], [], 0)[0]:
        linea = stdin.readline().strip()
        print(">" + linea)
        if linea == "on":
            led.value(1)
        if linea == "off":
            led.value(0)