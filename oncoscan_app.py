# oncoscan_app.py

import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Cargar el modelo entrenado
modelo = joblib.load("models/oncoscan_model.pkl")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Oncoscan - Predicción de Cáncer")
ventana.geometry("400x500")

# Etiqueta de título
titulo = tk.Label(ventana, text="Predicción de Cáncer", font=("Arial", 18, "bold"))
titulo.pack(pady=20)

# Campos de entrada para los datos del paciente
labels = ["Tamaño del Tumor (cm)", "Edad", "Peso (kg)", "Fumador (0/1)", "Antecedentes Familiares (0/1)", "Uso de Alcohol (0/1)"]
entradas = []

for label_text in labels:
    label = tk.Label(ventana, text=label_text, font=("Arial", 12))
    label.pack()
    entrada = tk.Entry(ventana, font=("Arial", 12))
    entrada.pack(pady=5)
    entradas.append(entrada)

# Función para hacer la predicción
def predecir_cancer():
    try:
        # Obtener los datos del formulario
        datos = [float(entrada.get()) for entrada in entradas]
        datos = np.array([datos])  # Convertir a matriz 2D para el modelo

        # Hacer la predicción
        prediccion = modelo.predict(datos)[0]

        # Mostrar el resultado
        if prediccion == 0:
            resultado = "No se detecta cáncer"
        else:
            resultado = "Posible presencia de cáncer"
        
        messagebox.showinfo("Resultado de la Predicción", resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa todos los datos correctamente.")

# Botón para hacer la predicción
boton = tk.Button(ventana, text="Predecir", font=("Arial", 14, "bold"), command=predecir_cancer, bg="#4CAF50", fg="white")
boton.pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()
