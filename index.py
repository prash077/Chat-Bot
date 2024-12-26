from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy

# Load the SpaCy language model
spacy_nlp = spacy.load("en_core_web_sm")

# Create a ChatBot instance
bot = ChatBot(
    "chat-bot",
    read_only=False,
    logic_adapters=["chatterbot.logic.BestMatch"],
    spacy_nlp=spacy_nlp  # Pass the loaded model
)

list_to_train = [
    "Hi",
    "Hi There",
    "What's your name?",
    "I'm a chatbot.",
    "How old are you?",
    "I don't age. I'm just an assistant.",
]

# Train the bot
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