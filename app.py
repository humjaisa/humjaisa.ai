from flask import Flask, request, jsonify, render_template
import text2emotion as t2e

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # 👈 yeh dikhaega UI

@app.route("/get")
def get_bot_response():
    try:
        user_msg = request.args.get('msg')
        if not user_msg:
            return jsonify({"error": "Message missing"}), 400
        emotions = t2e.get_emotion(user_msg)
        return jsonify(emotions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
