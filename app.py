from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "HumJaisa AI is running!"

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message', '')
    return jsonify({"response": f"HumJaisa AI ka jawab: {user_input[::-1]}"})  # bas demo

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
