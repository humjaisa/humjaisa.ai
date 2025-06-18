from flask import Flask, request, jsonify
from gpt4all import GPT4All

app = Flask(__name__)

# GPT4All model load (replace with actual path or logic)
model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf")

@app.route('/')
def home():
    return "HumJaisa AI is live!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input"}), 400

    response = model.generate(user_input, max_tokens=200)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
