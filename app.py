from flask import Flask, request, render_template
import text2emotion as t2e

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get('msg')
    emotions = t2e.get_emotion(user_msg)
    return str(emotions)

if __name__ == "__main__":
    app.run(debug=True)
