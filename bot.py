import telebot
import countri
import json
def correct_code(change2alpha):
    f = open('D:\c++ project\pythonProject\plfa_code.json','r')
    data = json.load(f)
    for select_counri in data:
      if str(change2alpha) in select_counri['englishShortName']:
             alfa_code = str(change2alpha)
             return alfa_code
    else:
         x= 'pleas enter the corrct name'
         return  x



token = "5251757800:AAGnLxnTb9GigCCFPN6N9T0uFO8cV7tVYU0"
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda msg:True)
def echo_all(message):
    give_from_user = message.text
    give_from_user = give_from_user.capitalize()
    corect = correct_code(give_from_user)
    last_one = countri.country(corect)
    bot.reply_to(message,last_one)
 
bot.infinity_polling()



