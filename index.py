from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy

spacy_nlp = spacy.load("en_core_web_sm")

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
    spacy_nlp=spacy_nlp
)

list_to_train = [
    "Hi",
    "Hi There",
    "What's your name?",
    "I'm a chatbot.",
    "How old are you?",
    "I don't age. I'm just an assistant.",
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

print("Enter ex to terminate.")
check = True
while check:
    user_question = input("User: ")
    if user_question == "ex":
        check = False
        break
    print("Chat-Bot: " + str(bot.get_response(user_question)))