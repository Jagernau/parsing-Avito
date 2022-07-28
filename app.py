from func import get_info
import random
import telebot
from resp import resp


num2 = random.randint(5, 12)
text = f"{resp()}"


token = '' # токен бота телеграмм
bot =telebot.TeleBot(token)
chat= # айди вашего чата

if text == "200":

    for i in range(1, num2):

        text = f"{get_info(i)}\n"

        text = text

        if text == "i":
            continue

        if text =="i\n":
            continue

        if text == " i ":
            continue

        if text != "i\n" or text != None or text != "None" or text != "None\n" or text != "i":

            bot.send_message(chat, text)
        

        else:
            pass

else:
    bot.send_message(chat, text)
