import telebot
import config

from telebot import types

bot=telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Продукты")
	markup.add(item1)
	bot.send_message(message.chat.id,"Добро пожалавать в чат-бот Фонда ИМОН!",parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type=='private':
		if message.text=='Продукты':
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
			item2=types.KeyboardButton('Button 1')
			item3=types.KeyboardButton('Button 2')
			item4=types.KeyboardButton('Button 3')
			item5=types.KeyboardButton('Главный меню')

			markup.add(item2,item3,item4,item5)
			bot.send_message(message.chat.id, 'Ваш выбор:', reply_markup=markup)
		if message.text=="Главный меню":
			markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
			item1=types.KeyboardButton("Продукты")
			markup.add(item1)
			bot.send_message(message.chat.id,"Добро пожалавать в чат-бот Фонда ИМОН!",parse_mode='html', reply_markup=markup)
bot.polling(none_stop=True)