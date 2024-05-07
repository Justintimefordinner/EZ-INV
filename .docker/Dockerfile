# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.10.1-alpine3.14 AS builder

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m venv venv && \
    venv/bin/pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["venv/bin/python3"]
CMD ["app/main.py"]

FROM builder as dev-envs

RUN apk update && \
    apk add --no-cache git && \
    addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

# Switch to non-root user
USER vscode