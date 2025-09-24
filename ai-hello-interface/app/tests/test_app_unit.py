def test_empty_text_returns_message():
    # import tardio para não inicializar coisas desnecessárias
    from app import main
    assert main.predict("") == "Digite um texto."

class DummyPipeline:
    def __call__(self, text):
        return [{"label": "POSITIVE", "score": 0.98123}]

def test_predict_formats_and_uses_pipeline(monkeypatch):
    from app import main
    # não baixa modelo: trocamos o carregador por um stub
    monkeypatch.setattr(main, "get_clf", lambda: DummyPipeline())

    out = main.predict("great")
    assert "POSITIVE" in out
    assert "(0.98)" in out  # arredondado a 2 casas

