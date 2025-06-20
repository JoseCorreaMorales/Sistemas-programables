
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite

# Ruta al archivo TFLite
modelo_tflite = 'vww_96_grayscale_quantized.tflite'

# Cargar el modelo TFLite
interprete = tflite.Interpreter(model_path=modelo_tflite)
interprete.allocate_tensors()

# Obtener información sobre los tensores de entrada y salida
input_details = interprete.get_input_details()
output_details = interprete.get_output_details()
input_shape = input_details[0]['shape']

# Etiquetas de clases
etiquetas_clases = {0: "deodorant", 1: "Class 2"}

# Iniciar la captura de video desde la webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Leer un fotograma desde la webcam
    ret, frame = cap.read()

    # Preprocesar la imagen de entrada
    imagen = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imagen = cv2.resize(imagen, (input_shape[1], input_shape[2]))
    imagen = imagen.astype(np.float32) / 255.0
    imagen = np.expand_dims(imagen, axis=0)
    imagen = np.expand_dims(imagen, axis=-1)

    # Cargar la imagen preprocesada en el tensor de entrada
    interprete.set_tensor(input_details[0]['index'], imagen)

    # Realizar la inferencia
    interprete.invoke()

    # Obtener los resultados de la inferencia
    resultados = interprete.get_tensor(output_details[0]['index'])

    # Procesar los resultados (por ejemplo, encontrar la clase con la probabilidad más alta)
    clase_predicha = np.argmax(resultados)

    # Obtener la etiqueta predicha
    etiqueta_predicha = etiquetas_clases[clase_predicha]

    # Imprimir la etiqueta predicha en la consola
    print(f"Etiqueta predicha: {etiqueta_predicha}")

    # Mostrar la imagen con la etiqueta predicha
    cv2.putText(frame, f"Etiqueta: {etiqueta_predicha}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Clasificación en tiempo real', frame)

    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
cap.release()
cv2.destroyAllWindows()
