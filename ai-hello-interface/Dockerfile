# ---- builder ----
FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) instalar system deps mínimos (ex.: gcc não deve ser necessário para Gradio puro)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl && \
    rm -rf /var/lib/apt/lists/*

# 2) copiar requirements e instalar em diretório isolado
COPY app/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --prefix=/install -r /app/requirements.txt

# ---- runtime ----
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:/usr/local/sbin:/usr/local:/usr/sbin:/usr/bin:/sbin:/bin"

WORKDIR /app

# 3) criar usuário não-root
RUN useradd -m appuser
USER appuser

# 4) copiar libs do builder + código
COPY --from=builder /install /usr/local
COPY app/ /app/

# 5) expor porta do Gradio
EXPOSE 7860

# 6) healthcheck simples (HTTP)
# (Se quiser, pode deixar pro próximo passo)
# HEALTHCHECK --interval=30s --timeout=3s \
#   CMD curl -fsS http://localhost:7860/ || exit 1

# 7) comando de entrada
CMD ["python", "main.py"]

