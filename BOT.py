import telebot
import config



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['join'])
def welcome(message):
	 sti = open('C:/Users/user/Desktop/web/welcome.tgs','rb')
	 bot.send_sticker(message.chat.id, sti)
	 bot.send_message(message.chat.id,"Welcome, {0.first_name}!\nI'm glad to see you!".format(message.from_user),
	 	parse_mode='html')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, как ты?')
    elif text == "mirix":
        bot.send_message(chat_id, 'Что тебе ?')
    






@bot.message_handler(content_types=['text'])
def qwerty(message):
	bot.send_message(message.chat.id, message.text)


bot.polling(none_stop = True)
