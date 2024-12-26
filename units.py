from chatterbot import ChatBot

bot = ChatBot("units", logic_adapters=["chatterbot.logic.UnitConversion"])

  
print("Enter ex to terminate.")
check = True
while check:
    user_text = input("Ask a Question(unit conversion): ")
    if user_text == "ex":
        check = False
        break
    print("Chat-Bot: " + str(bot.get_response(user_text)))