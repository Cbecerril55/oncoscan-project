import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

# Crear carpeta para modelos si no existe
os.makedirs("models", exist_ok=True)

# Cargar los datos (Asegúrate de tener un archivo CSV en la carpeta data)
DATA_PATH = "data/cancer_data.csv"

def cargar_datos():
    try:
        data = pd.read_csv(DATA_PATH)
        print(f"Datos cargados correctamente. Total de registros: {len(data)}")
        return data
    except FileNotFoundError:
        print(f"Error: El archivo '{DATA_PATH}' no se encontró.")
        return None

def preprocesar_datos(data):
    # Dividir los datos en características (X) y etiquetas (y)
    X = data.drop("tipo_cancer", axis=1)
    y = data["tipo_cancer"]

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def entrenar_modelo(X_train, y_train):
    # Crear el modelo
    modelo = DecisionTreeClassifier(max_depth=10, random_state=42)
    modelo.fit(X_train, y_train)
    return modelo

def evaluar_modelo(modelo, X_test, y_test):
    # Hacer predicciones
    y_pred = modelo.predict(X_test)

    # Mostrar resultados
    print("\nMatriz de Confusión:")
    print(confusion_matrix(y_test, y_pred))
    print("\nReporte de Clasificación:")
    print(classification_report(y_test, y_pred))

def guardar_modelo(modelo, nombre_archivo="models/oncoscan_model.pkl"):
    # Guardar el modelo para uso futuro
    joblib.dump(modelo, nombre_archivo)
    print(f"Modelo guardado en: {nombre_archivo}")

def main():
    data = cargar_datos()
    if data is not None:
        X_train, X_test, y_train, y_test = preprocesar_datos(data)
        modelo = entrenar_modelo(X_train, y_train)
        evaluar_modelo(modelo, X_test, y_test)
        guardar_modelo(modelo)

if __name__ == "__main__":
    main()
