# Flask MVC Project

Proyecto base con arquitectura MVC en Python Flask. Incluye una vista principal `index.html` que muestra el perfil de un developer.

## Estructura del proyecto

```text
aws-python/
|-- app/
|   |-- controllers/
|   |   `-- home_controller.py
|   |-- models/
|   |   `-- developer.py
|   |-- templates/
|   |   `-- index.html
|   `-- __init__.py
|-- app.py
|-- config.py
|-- requirements.txt
|-- Dockerfile
`-- README.md
```

## Requisitos

- Python 3.11 o superior
- pip
- Docker (opcional)

## Ejecucion local

1. Crear un entorno virtual:

```powershell
python -m venv .venv
```

2. Activar el entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

4. Ejecutar la aplicacion:

```powershell
python app.py
```

5. Abrir en el navegador:

```text
http://127.0.0.1:5000/
```

## Ejecucion con Docker

1. Construir la imagen:

```powershell
docker build -t flask-mvc-app .
```

2. Ejecutar el contenedor:

```powershell
docker run -p 5000:5000 flask-mvc-app
```

3. Abrir en el navegador:

```text
http://127.0.0.1:5000/
```

## Nota

La aplicacion arranca en modo debug cuando se ejecuta localmente con `python app.py`. En Docker se utiliza el servidor integrado de Flask escuchando en `0.0.0.0:5000`.
