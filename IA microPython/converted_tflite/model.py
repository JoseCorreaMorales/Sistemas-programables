import numpy as np
import tensorflow as tf

# Reemplaza 'modelo.tflite' con el nombre de tu archivo TFLite.
modelo_tflite_path = 'vww_96_grayscale_quantized.tflite'
modelo_tflite = tf.lite.Interpreter(model_path=modelo_tflite_path)
modelo_tflite.allocate_tensors()

# Obtener los detalles del tensor de entrada y salida
entrada_detalles = modelo_tflite.get_input_details()
salida_detalles = modelo_tflite.get_output_details()

# Obtener los índices de los tensores de entrada y salida
entrada_indice = entrada_detalles[0]['index']
salida_indice = salida_detalles[0]['index']


# Supongamos que tu entrada es un array NumPy llamado 'entrada'
entrada = np.array(entrada)

# Asegúrate de que la forma de la entrada coincida con la forma esperada por el modelo
modelo_tflite.resize_tensor_input(entrada_indice, entrada.shape)
modelo_tflite.allocate_tensors()

# Establecer los datos de entrada
modelo_tflite.set_tensor(entrada_indice, entrada)


# Ejecutar la inferencia
modelo_tflite.invoke()

# Obtener los resultados de la inferencia
resultado = modelo_tflite.get_tensor(salida_indice)


# Realiza cualquier postprocesamiento necesario en el resultado
# ...

# Imprime o utiliza el resultado según sea necesario
print(resultado)
