
# instalar opencv en la raspberry pi (Thonny)
# pip install opencv-python


import utime
import tflite
import cv2
import numpy as np

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

# Inicializar la webcam (asegúrate de que la webcam esté conectada)
webcam = cv2.VideoCapture(0)  # 0 indica el primer dispositivo de cámara

while True:
    # Capturar un cuadro de video desde la webcam
    ret, frame = webcam.read()

    # Preprocesar la imagen según lo que requiera tu modelo
    # Aquí debes ajustar la preprocesamiento según los requisitos de tu modelo
    entrada = preprocess_image(frame)

    # Ejecutar la inferencia
    intérprete.set_tensor(entrada_indice, entrada)
    intérprete.invoke()
    resultado = intérprete.get_tensor(salida_indice)

    # Interpretar el resultado
    clase_predicha = np.argmax(resultado)

    # Mapear el índice de clase a la etiqueta
    labels = ["cutter", "Pelota"]
    etiqueta_predicha = labels[clase_predicha]

    # Mostrar el resultado en la ventana de la webcam
    cv2.putText(frame, f"Objeto predicho: {etiqueta_predicha}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Webcam", frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
webcam.release()
cv2.destroyAllWindows()
