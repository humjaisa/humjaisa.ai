from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def get_bot_reply(msg):
    blob = TextBlob(msg)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "Aap khush lag rahe ho! 😊"
    elif polarity < -0.2:
        return "Aap thode udaas lag rahe ho. Sab thik hai? 😔"
    else:
        return "Hmm... main samajh gaya. Batao aur kya chal raha hai?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-response", methods=["POST"])
def get_response():
    user_msg = request.json.get("message")
    if not user_msg:
        return jsonify({"reply": "Kuch toh likho! 😅"})
    return jsonify({"reply": get_bot_reply(user_msg)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
