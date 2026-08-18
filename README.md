# CIICCTE-server-backend-V2

## Sobre el proyecto

Software que funge como servidor para gestionar la abstraccion entre el frontend y los workspaces personales dentro de el CIICCTE
- Esta escrito a mano en python, se hace uso de fastapi y sqlmodel
- La version de python y las dependencias estan gestionadas por uv es decir que se requiere tener instalado uv en el servidor
- Y al ejecutar el comando uv sync en el folder de este proyecto, la version de python usada por las dependencias del proyecto juntos a estas, seran descargadas y un entorno virtual sera creado para trabajar de manera local
- En este proyecto se hace uso de fastapi por lo mismo si se accede a localhost:8000/docs o localhost:8000/redoc se podra acceder a documentacion sobre los endpoints del backend

## Tech stack

Por motivos de documentacion, este es el stack de tecnologias usado para el desarrollo de este repo

- uv para gestionar version de python y paquetes
- python como lenguaje de programacion debido a su facilidad de uso
- fastapi como servidor tambien debido a su facilidad de uso y rendimiento
- sqlmodel por ser un proyecto mantenido por el quipo de fastapi y ser un wrapper alrededor de sqlalchemy
- docker como runtime de contenedores
- dockerfiles para generar la imagen del servidor
- docker compose para el depliegue del contenedor
- ruff para el formato y linting
- bruno para probar los endpoints

## Como iniciar el backend

Antes de correrlo es importante asegurarse que la db ya esta configurada, consultar https://github.com/mena-skibidi/CIICCTE-server-DB
Al asegurarse que la db esta corriendo se puede levantar el backend de dos maneras:

- la mas sencilla y recomendada es levantar todo con docker compose
- la otra opcion es correr los comandos a mano

### Usando docker compose

1. Se debera clonar el repositorio en el servidor con git clone https://github.com/mena-skibidi/CIICCTE-server-backend-V2 y se debe descomprimir
2. Desde la terminal se ingresara a ese directorio y se debera ejecutara el comando

```bash
docker compose up --build -d
```

o

```
docker compose up --build
```

Esta version se puede apagar con docker compose stop, o ctrl + c si se corrio el comando sin -d

### De manera tradicional

1. Se debera clonar el repositorio en el servidor con git clone https://github.com/mena-skibidi/CIICCTE-server-backend-V2 y se debe descomprimir
2. Tras esto se debera asegurar que uv este instalado, si no es asi, se deberan seguir los pasos de este link https://docs.astral.sh/uv/
3. Al asegurarse que uv esta instalado, en el directorio del repositorio clonado se debera correr el siguiente comando
```bash
uv sync
```
4. Y para ejecutar el programa se debera correr esto
```bash
uv run fastapi dev src/main.py --host 0.0.0.0
```

Esta version se puede apagar mediante ctrl + c o matando el proceso en algun gestor de procesos