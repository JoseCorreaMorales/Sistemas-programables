from machine import Pin
from time import sleep

Ap = Pin(19, Pin.OUT)
Am = Pin(17, Pin.OUT)
Bp = Pin(18, Pin.OUT)
Bm = Pin(16, Pin.OUT)

pines = [Ap, Bp, Am, Bm]
paso = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
    for p in paso:
        for b in range(len(pines)):
            pines[b].value(p[b])
            sleep(0.001)
    