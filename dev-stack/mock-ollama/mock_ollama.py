from flask import Flask, request, jsonify
import hashlib, json

app = Flask(__name__)

@app.route('/')
def health():
    return 'OK', 200

@app.route('/api/tags', methods=['GET'])
def list_models():
    return jsonify({"models": ["mock-model:latest"]})

@app.route('/api/embeddings', methods=['POST'])
def embeddings():
    data = request.get_json()
    prompt = data.get('prompt', '')
    # Deterministic 100-dim vector based on SHA1
    h = hashlib.sha1(prompt.encode()).digest()
    vec = [ (b / 255.0) * 2 - 1 for b in h[:100] ]
    return jsonify({"embedding": vec})

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt', '')
    return jsonify({"response": "Mock response to: " + prompt})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])
    last_user = messages[-1].get('content', '') if messages else ''
    return jsonify({
        "message": {"role": "assistant", "content": "Mock chat response to: " + last_user},
        "done": True
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11434)
