from flask import Flask, render_template, request
from textblob import TextBlob
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import SQLiteChatMessageHistory

app = Flask(__name__)

# Chat memory using SQLite
chat_history = SQLiteChatMessageHistory(database_path="chat_memory.db", session_id="default")
memory = ConversationBufferMemory(chat_memory=chat_history, return_messages=True)

# Response logic using TextBlob for sentiment analysis
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
def index():
    return render_template("index.html")

@app.route("/get")
def get_response():
    user_msg = request.args.get("msg")
    memory.add_user_message(user_msg)
    bot_reply = get_bot_reply(user_msg)
    memory.add_ai_message(bot_reply)
    return bot_reply

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
