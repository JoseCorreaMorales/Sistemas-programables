from machine import Pin, PWM
from time import sleep
pwm = PWM(Pin(28))
pwm.freq(50) #50Hz
#1/50
duty_min = 65536 / 20000 * 500 #ciclo minimos de trabajo 2.5% de 65... para el 2.5% de 20ms
#duty_min = 65536 * (500 / 20000) #equvalencia para encontrar el % correspondiente
duty_max = 65536 / 20000 * 2450 #ciclo maximo de trabajo para el 12.5% de 20ms
def setServoCycle (grados):
    position = int (duty_min + ((duty_max - duty_min) / 180) * grados)
    pwm.duty_u16(position)

i = 0
while True:
    setServoCycle(i)
    sleep(1)
    i = i + 10