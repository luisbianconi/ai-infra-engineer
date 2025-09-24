# app/main.py
import os
import time
import gradio as gr
from functools import lru_cache
from transformers import pipeline


from prometheus_client import Counter, Histogram, start_http_server

METRICS_PORT = int(os.getenv("METRICS_PORT", "8000"))
REQUESTS = Counter("inferences_total", "Total de requisições de inferência", ["model"])
ERRORS   = Counter("inferences_errors_total", "Total de erros de inferência", ["model"])
LATENCY  = Histogram("inference_latency_seconds", "Latência da inferência (s)", ["model"])


# Configuráveis por ENV (se quiser trocar depois)
MODEL_ID = os.getenv("MODEL_ID", "distilbert-base-uncased-finetuned-sst-2-english")
PORT = int(os.getenv("PORT", "7860"))

# Força CPU (evita problemas de CUDA em ambientes sem GPU compatível)
# Em versões atuais do Transformers, device=-1 == CPU.
#clf = pipeline("sentiment-analysis", model=MODEL_ID, device=-1)

@lru_cache(maxsize=1)
def get_clf():
    # mantém as mesmas opções que você usava no clf global
    from transformers import pipeline
    return pipeline("sentiment-analysis", model=MODEL_ID, device=-1)


def predict(text: str) -> str:
    REQUESTS.labels(MODEL_ID).inc()
    t0 = time.perf_counter()
    try:
        if not text or not text.strip():
            return "Digite um texto."
        clf = get_clf()
        out = clf(text)[0]
        dt = time.perf_counter() - t0
        LATENCY.labels(MODEL_ID).observe(dt)
        return f"{out['label']} ({out['score']:.2f}) • {dt*1000:.1f} ms"
    except Exception:
        ERRORS.labels(MODEL_ID).inc()
        raise

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=3, label="Texto"),
    outputs=gr.Textbox(label="Resultado"),
    title="Hello AI Infra — Sentiment",
    description="Modelo leve (CPU) via 🤗 Transformers. Experimente uma frase positiva e outra negativa."
)

if __name__ == "__main__":
    start_http_server(METRICS_PORT)  # expõe métricas em http://localhost:8000/metrics
    demo.launch(server_name="0.0.0.0", server_port=PORT)
