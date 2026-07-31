FROM ghcr.io/astral-sh/uv:debian-slim
WORKDIR /usr/local/ciiccte-server-backend-v2
COPY . ./
RUN uv sync
