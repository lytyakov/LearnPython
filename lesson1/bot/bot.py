from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import logging

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(
        update.message.chat.first_name,
        update.message.text
    )
    logging.info(user_text)
    update.message.reply_text(user_text)

def main():
    
    with open('auth_config.json', 'r') as f:
        token = json.loads(f.read())['token']

    my_bot = Updater(token)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()

main()
