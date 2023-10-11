from st7735 import TFT
from sysfont import sysfont
from machine import SPI,Pin
from bmp import bmp
from time import sleep

spi = SPI(1, baudrate=8000000, polarity=0, phase=0)
tft=TFT(spi,14,15,13)

# definir el tamaño de la pantalla con dimencion de 80x160
tft.init_7735(tft.REDTAB80x160)

# pintar la pantalla de negro
tft.fill(TFT.BLACK);

# en las cordenadas 0,0 pintar hello world de blanco con al fuente espefificada
tft.text((0, 0), "Hello World!", TFT.WHITE, sysfont)
sleep(3)
bmp('sisprog.bmp', tft)
