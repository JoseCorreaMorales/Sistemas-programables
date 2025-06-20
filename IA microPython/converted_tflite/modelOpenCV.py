import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo TFLite
modelo_tflite_path = 'vww_96_grayscale_quantized.tflite'  # Reemplaza con el nombre de tu modelo
modelo_tflite = tf.lite.Interpreter(model_path=modelo_tflite_path)
modelo_tflite.allocate_tensors()

# Obtener los detalles del tensor de entrada
entrada_detalles = modelo_tflite.get_input_details()
entrada_indice = entrada_detalles[0]['index']

# Abrir la conexión a la webcam (0 indica la cámara predeterminada)
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame desde la webcam
    ret, frame = cap.read()

    # Preprocesar la imagen (ajustar tamaño, normalizar, etc.)
    # Asegúrate de que la forma de la imagen coincida con la esperada por el modelo
    # Realiza la normalización requerida por tu modelo

    # Establecer los datos de entrada en el modelo
    modelo_tflite.set_tensor(entrada_indice, cap)

    # Ejecutar la inferencia
    modelo_tflite.invoke()

    # Obtener los resultados de la inferencia
    resultado = modelo_tflite.get_tensor(0)  # Ajustar el índice según la salida esperada por tu modelo

    # Realizar acciones basadas en los resultados (por ejemplo, mostrar resultados en pantalla)
    # ...

    # Mostrar el frame en una ventana
    cv2.imshow('Webcam', frame)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
