from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import spacy
from flask import Flask, render_template, request

app = Flask(__name__)

#spacy_nlp = spacy.load("en_core_web_sm")

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
    #spacy_nlp=spacy_nlp
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")
def main():
    return render_template("index.html")

# print("Enter ex to terminate.")
# check = True
# while check:
#     user_question = input("User: ")
#     if user_question == "ex":
#         check = False
#         break
#     print("Chat-Bot: " + str(bot.get_response(user_question)))

@app.route("/get")
def get_chatbot_response():
    userText = request.args.get('UserInputMessage')
    return str(bot.get_response(userText))
    
if __name__ == "__main__":
    app.run(debug=True)