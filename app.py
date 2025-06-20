from flask import Flask, render_template, request, jsonify
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import SQLiteChatMessageHistory

app = Flask(__name__)

# LangChain memory using SQLite (no OpenAI)
chat_history = SQLiteChatMessageHistory(database_path="chat_memory.db", session_id="user1")
memory = ConversationBufferMemory(chat_memory=chat_history, return_messages=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')

    if not user_input:
        return jsonify({"response": "Please provide a message."})

    # Basic local logic for reply
    if "/hello" in user_input.lower():
        reply = "Hello! How can I help you today?"
    elif "/bye" in user_input.lower():
        reply = "Goodbye! Have a great day."
    else:
        reply = "I'm still learning! Try saying /hello or /bye."

    # Store in memory
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(reply)

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
