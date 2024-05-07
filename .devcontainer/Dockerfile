# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m venv venv && \
    venv/bin/pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["venv/bin/python3"]
CMD ["main.py"]

FROM builder as dev-envs

RUN apk update && \
    apk add git && \
    addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /