# Oncoscan-Project

### Descripción del Proyecto

Oncoscan es un proyecto basado en inteligencia artificial para predecir la presencia de cáncer a partir de datos médicos. El sistema se compone de dos scripts principales:

1. **oncoscan\_model.py** - Entrenamiento y evaluación del modelo de IA.
2. **oncoscan\_app.py** - Interfaz gráfica para capturar datos de pacientes y hacer predicciones.

### Estructura del Proyecto

```
ONCOSCAN-PROJECT/
│
├── venv/                   # Entorno virtual
├── oncoscan_model.py       # Script del modelo de IA
├── oncoscan_app.py         # Interfaz gráfica
├── data/
│   └── cancer_data.csv    # Datos de entrenamiento
├── models/
│   └── oncoscan_model.pkl  # Modelo entrenado
├── README.md               # Documentación del proyecto
└── .gitignore              # Archivos a ignorar en Git
```

### Instalación y Configuración del Entorno Virtual

#### **1. Crear el Entorno Virtual**

```bash
python3 -m venv venv
source venv/bin/activate  # Para macOS/Linux
```

#### **2. Instalar las Dependencias**

```bash
pip install -r requirements.txt
```

#### **3. Crear la Carpeta de Datos**

```bash
mkdir data
```

Asegúrate de tener un archivo de datos en la carpeta **`data/`** llamado **`cancer_data.csv`** para entrenar el modelo.

### Uso del Proyecto

#### **Entrenar el Modelo**

Para entrenar y evaluar el modelo, usa:

```bash
python oncoscan_model.py
```

#### **Ejecutar la Interfaz Gráfica**

Una vez que el modelo esté entrenado y guardado, puedes usar la interfaz gráfica con:

```bash
python oncoscan_app.py
```

### Requisitos del Proyecto

* Python 3.11+
* scikit-learn
* pandas
* numpy
* matplotlib
* tkinter

### Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio y abre un pull request con tus mejoras.

### Licencia

Este proyecto está bajo la licencia MIT.
