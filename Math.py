from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import re
import nltk
from word2number import w2n

nltk.download('punkt')
bot = ChatBot("Math", 
              logic_adapters=[
                  "chatterbot.logic.BestMatch"
              ])

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")

print("------------------- Math Chatbot ----------------------")
print("Enter 'ex' to terminate.")

check = True
while check:
    user_question = input("User: ")
    
    if user_question == "ex":
        check = False
        break

    if re.search(r'\d+\s*[\+\-\*/\^%]\s*\d+', user_question):  # Match basic math expressions
        try:
            result = eval(user_question)
            print("Chat-Bot: " + str(result))
        except Exception as e:
            print(f"Error evaluating math: {e}")
    
    else:
        try:
            user_question = user_question.lower().replace("plus", "+").replace("minus", "-").replace("times", "*").replace("divided by", "/")
            words = nltk.word_tokenize(user_question)
            for i, word in enumerate(words):
                if word.isalpha() and word not in ["plus", "minus", "times", "divided"]:
                    try:
                        words[i] = str(w2n.word_to_num(word))
                    except ValueError:
                        pass
            user_question = " ".join(words)
            
            if re.search(r'\d+\s*[\+\-\*/\^%]\s*\d+', user_question):
                result = eval(user_question)
                print("Chat-Bot: " + str(result))
            else:
                response = bot.get_response(user_question)
                print("Chat-Bot: " + str(response))
        
        except Exception as e:
            print(f"Error processing the input: {e}")
