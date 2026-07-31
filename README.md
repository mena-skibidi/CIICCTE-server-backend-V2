# CIICCTE-server-backend-V2

## Sobre el proyecto

- Software que funge como servidor para gestionar la abstraccion entre el frontend y los workspaces personales dentro de el CIICCTE
- Esta escrito a mano en python, hace uso de fastapi y sqlmodel
- La version de python y las dependencias estan gestionadas por uv es decir que se requiere tener instalado uv en el servidor
- Y al ejecutar el comando uv sync en el folder de este proyecto, la version de python usada por las dependencias del proyecto juntos a estas, seran descargadas y un entorno virtual sera creado para trabajar de manera local

## Como iniciar el backend

- Para facilitar el proceso de levantar y mantener el backend hay dos maneras de utilizarlo, la mas sencilla y recomendada es levantar todo con docker compose y la otra opcion es correr los comandos a mano

### Usando docker compose

1. Se debera clonar el repositorio en el servidor con git clone https://github.com/mena-skibidi/CIICCTE-server-backend-V2 y se debe descomprimir
2. Desde la terminal se ingresara a ese directorio y se debera ejecutara el comando
```bash
docker compose up --build -d
```

### De manera tradicional

1. Se debera clonar el repositorio en el servidor con git clone https://github.com/mena-skibidi/CIICCTE-server-backend-V2 y se debe descomprimir
2. Tras esto se debera asegurar que uv este instalado, si no es asi, se deberan seguir los pasos de este link https://docs.astral.sh/uv/
3. Al asegurarse que uv esta instalado, en el directorio del repositorio clonado se debera correr el siguiente comando
```bash
uv sync
```
4. Y para ejecutar el programa se debera correr esto
```bash
uv run fastapi dev
```