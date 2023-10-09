
from machine import Pin, ADC
from time import sleep

global d0
global a0

pinD = Pin(22, Pin.IN)
pinA = ADC(26)

while True:
    d0 = pinD.value()
    a0 = pinA.read_u16()
    print(f"Digital: {d0}")
    print(f"Analogico: {a0}")
    print()
    sleep(3)
