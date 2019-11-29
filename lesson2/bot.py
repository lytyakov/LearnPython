from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import logging
import ephem
from datetime import date

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

def process_planet(bot, update):
    planet_name = update.message.text.lower().split(' ')[1].strip().capitalize()
    try:
        planet = getattr(ephem, planet_name)(date.today().isoformat())
        _, constellation = ephem.constellation(planet)
        answer = '{} is in {} today'.format(planet_name, constellation)
    except AttributeError:
        answer = 'Cannot find anything for planet {}'.format(planet_name)
    logging.info(answer)
    update.message.reply_text(answer)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: {}".format(
        update.message.chat.first_name,
        update.message.text
    )
    logging.info(user_text)
    update.message.reply_text(user_text)
    
def main():
    
    with open('./lesson1/bot/auth_config.json', 'r') as f:
        token = json.loads(f.read())['token']

    my_bot = Updater(token)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", process_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()

main()