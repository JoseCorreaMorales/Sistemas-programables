from dth import DHT11
from machine import Pin
from time import sleep

global temp
global hum

pin = DHT11(0, Pin.IN)
d = DHT11(pin)

while True:
    sleep(5)
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    print(f"temperatura : {temp}" )
    print(f"humedad : {hum}" )