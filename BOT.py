import telebot
import config
import random
import time
from datetime import datetime

names = ["Олег", "Али", "Атуш", "Саня", "Даня", "Ильяс"]
words = [" красавчик)", " ебан))", ", соснёшь?)))", " пидарок))", " лох))"]

bot = telebot.TeleBot(config.TOKEN)

while True:
		bot.send_message(-1001441045260,'{0}{1}'.format(names[random.randint(0,5)],words[random.randint(0,4)]))
		time.sleep(4000)


@bot.message_handler(commands=['start','go'])
def welcome(message):
	 print(str(datetime.now()))
	 print('NEW user : '+message.from_user.username + ', at  ' + str(datetime.now()) )
	 sti = open('C:/Users/user/Desktop/web/welcome.tgs','rb')
	 bot.send_sticker(message.chat.id, sti)
	 bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!Я рад тебя видеть!".format(message.from_user),parse_mode='html')
	 bot.send_message(message.chat.id,"Набери '/help' чтобы узнать что я умею",parse_mode='html')
	 print(message.chat.id)
@bot.message_handler(commands=['help'])
def help(message):
    
    print('user use "/help": '+message.from_user.username + ', at  ' + str(datetime.now()) )
    bot.send_message(message.chat.id,"\nСейчас я могу отвечать на вопросы по типу: \n'Привет'\n'Ты кто?''\n Oтзываться на: \n'Mirix'\n'Мирикс'\n\n Я не перестаю развиваться!",parse_mode='html')
    
@bot.message_handler(content_types=['text'])
def text_handler(message):
    
    print('User '+message.from_user.username  +' send message at '+str(datetime.now()) + ' \n >>>>'+ message.text + ' <<<<')
    print(message.chat.id)
    
    bot.forward_message(-349676070, message.chat.id, message.message_id)
    
    
    chat_id = message.chat.id
    
    if text.__contains__("привет"):
        bot.send_message(chat_id, 'ПривееееееееееееТ!')
    elif text.__contains__("мирикс"):
        bot.send_message(chat_id, 'Кто то меня звал ?')
    elif text.__contains__("mirix"):
        bot.send_message(chat_id, 'кто то меня звал ?')
    elif text.__contains__("ты кто"):
    	bot.send_message(chat_id, 'Я бот которого создал Мирикс')
    elif text.__contains__("чмо"):
        bot.send_message(chat_id, 'Сам {0.first_name} чмо'.format(message.from_user),parse_mode='html')
    elif text.__contains__("ебан"):
        bot.send_message(chat_id, 'Сам {0.first_name} чмо'.format(message.from_user),parse_mode='html')
    elif text.__contains__("лох"):
        bot.send_message(chat_id, 'Сам ты  {0.first_name} ЛОХ '.format(message.from_user),parse_mode='html')
    elif text.__contains__("сука"):
        bot.send_message(chat_id, 'Сам ты  {0.first_name} СУКА '.format(message.from_user),parse_mode='html')
    elif text.__contains__("уебать"):
        bot.send_message(chat_id, 'Уебать? Кого ? может тебя лучше уебать , а {0.first_name}?'.format(message.from_user),parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Нихуя не понятно, но оочень интересно))")





bot.polling(none_stop = True)
