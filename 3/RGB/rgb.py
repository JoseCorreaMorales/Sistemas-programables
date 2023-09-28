from machine import Pin, PWM
from time import sleep

red = PWM(Pin(0, Pin.OUT))
green= PWM(Pin(1, Pin.OUT))
blue = PWM(Pin(2, Pin.OUT))

def enciende(r, g, b):
    #red.value(r)
    #green.value(g)
    #blue.value(b)
    #print("red ", r, "green ", g, "blue ", b)
    red.duty_u16(r)
    green.duty_u16(g)
    blue.duty_u16(b)


#65535 = 100%
while True:
    #enciende(1, 1, 1)
    #sleep(1)
    enciende(4000, 0, 0)
    sleep(1)
    enciende(4000, 5000, 0)
    sleep(1)
    
