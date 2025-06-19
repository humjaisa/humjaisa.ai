from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data.get('message', '')

    if "/hello" in user_message.lower():
        reply = "Hello! 👋 I'm always here to help."
    else:
        reply = "I'm learning. Type /hello to start!"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
