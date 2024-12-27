from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request
import requests

app = Flask(__name__)
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("API_KEY")

bot = ChatBot(
    "chat-bot",
    read_only=False,
    logic_adapters=[
        {
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Sorry i don't have any answer",
            "maximum_similarity_threshold":0.9
            }
        ],
)

# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("chatterbot.corpus.spanish")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('UserInputMessage')
    rawData = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+userText+"&appid="+api_key)
    result = rawData.json()
    return result
    
if __name__ == "__main__":
    app.run(debug=True)