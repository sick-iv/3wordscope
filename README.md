# Flask Text API

Pequeño microserviço em Flask que recebe JSON com campo `text` e devolve contagem de palavras e as top 10 palavras.

**Como usar (local)**
```
pip install -r requirements.txt
FLASK_APP=app.py flask run
```
**Exemplo**
```
curl -X POST http://127.0.0.1:5000/api/summary -H 'Content-Type: application/json' -d '{"text":"oi oi testando oi"}'
```
