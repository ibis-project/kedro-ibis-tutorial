FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends graphviz postgresql-client curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY codespace_requirements.txt /

RUN /root/.cargo/bin/uv pip install --system -r codespace_requirements.txt
