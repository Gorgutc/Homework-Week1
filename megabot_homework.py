from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
	level = logging.INFO,
	filename = 'bot.log'
	)

def greet_user(bot, update):
	text = 'Приветствую, тебя, искатель вдохновения и истины. Воспользуйся же моими знаниями и помощью. Для начала работы со мной можно написать сюда /start'
	print(text)
	text2 = 'Было запущено приветствие'
	logging.info(text2)
	um = update.message
	um.reply_text(text) # Здесь написать приветственное сообщение.

def talk_to_me(bot,update):
	user_text = 'Привет, юный падаван {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
	logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
				update.message.chat.id, update.message.text)
	update.message.reply_text(user_text)

def main():
	mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
	logging.info('Бот запускается')
	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()

main()