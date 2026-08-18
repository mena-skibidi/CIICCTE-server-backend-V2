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

1. Se debera clonar el repositorio en el servidor con:

```bash
git clone https://github.com/mena-skibidi/CIICCTE-server-backend-V2
```

2. Desde la terminal se ingresara a ese directorio y se debera ejecutara el comando

```bash
docker compose up --build -d
```

Si el programa se ejecuto en modo detached (con la -d) se debera navegar al directorio y en la terminal correr lo siguiente para detener el proceso

```bash
docker compose down
```