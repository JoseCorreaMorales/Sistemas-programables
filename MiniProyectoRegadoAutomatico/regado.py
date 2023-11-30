import machine
import time

# Pin analógico para el sensor de humedad 
sensor_pin = machine.ADC(0)

# Umbral de humedad para encender y apagar la bomba
umbral_encendido = 500  # Ajustar 
umbral_apagado = 800   # Ajustar

# Pin para el relé 
relay_pin = machine.Pin(27, machine.Pin.OUT)

def read_soil_moisture():
    # Lee el valor analógico del sensor de humedad del suelo
    return sensor_pin.read()

def turn_on_pump():
    # Enciende la bomba de agua
    relay_pin.value(1)

def turn_off_pump():
    # Apaga la bomba de agua
    relay_pin.value(0)

def main():
    while True:
        soil_moisture = read_soil_moisture()
        print("Valor de humedad del suelo:", soil_moisture)

        if soil_moisture < umbral_encendido:
            print("El suelo está seco. Encendiendo la bomba de agua.")
            turn_on_pump()
        elif soil_moisture > umbral_apagado:
            print("El suelo está húmedo. Apagando la bomba de agua.")
            turn_off_pump()

        time.sleep(3600)  # Espera 1 hora antes de volver a verificar


