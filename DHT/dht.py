from dth import DHT11
from machine import Pin
from time import sleep

sensor = DHT11(Pin(16))
temp = 0

humedad = 0

while True:
    sleep(3)
    sensor.measure()
    temp = sensor.temperature()
    humedad = sensor.humidity()
    print(f"temperatura : {temp}" )
    print(f"humedad : {humedad}" )