"""app.py
Microserviço Flask simples que expõe uma rota para resumir texto (contagem de palavras) - exemplo de API.
Uso: FLASK_APP=app.py flask run --host=0.0.0.0 --port=5000
"""
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status':'ok'})

@app.route('/api/summary', methods=['POST'])
def summary():
    data = request.get_json() or {}
    text = data.get('text', '')
    words = text.split()
    top = {}
    for w in words:
        top[w] = top.get(w,0) + 1
    sorted_top = sorted(top.items(), key=lambda x: x[1], reverse=True)[:10]
    return jsonify({'word_count': len(words), 'top_words': sorted_top})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
