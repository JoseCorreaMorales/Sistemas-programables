import utime
import tflite

# Cargar el modelo TensorFlow Lite
modelo_tflite_path = 'vww_96_grayscale_quantized.tflite'
with open(modelo_tflite_path, 'rb') as f:
    modelo_tflite = tflite.Model.from_bytearray(f.read())

# Crear un intérprete TensorFlow Lite
intérprete = tflite.Interpreter(model=modelo_tflite)
intérprete.allocate_tensors()

# Obtener los tensores de entrada y salida
entrada_detalles = intérprete.get_input_details()
salida_detalles = intérprete.get_output_details()
entrada_indice = entrada_detalles[0]['index']
salida_indice = salida_detalles[0]['index']

# Ejecutar la inferencia (suponiendo que 'entrada' es tu entrada)
intérprete.set_tensor(entrada_indice, entrada)
intérprete.invoke()
resultado = intérprete.get_tensor(salida_indice)

# Imprimir o usar el resultado según sea necesario
print(resultado)
