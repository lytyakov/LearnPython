from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import logging
import ephem
from datetime import date
from csv import DictReader
from string import digits
from copy import deepcopy

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

def calculator(bot, update):
    """
    Простой калькулятор
    """
    to_calc = update.message.text.partition(' ')[2].strip()
    symbols = set(digits) | set('.+-*/() ')
    if not set(to_calc).difference(symbols):
        try:
            res = eval(to_calc)
        except ZeroDivisionError:
            res = 'На ноль делить нельзя'
        except SyntaxError:
            res = 'Проверьте правильность выражения для вычисления'
    else:
        res = "Недопустимое вычисление. Я умею только складывать, вычитать, умножать и делить числа. Пробелы ставить не надо. Десятичная часть числа отделяется точкой"
    update.message.reply_text(res)
    logging.info(res)

def play_cities(bot, update):
    """
    Игра в города с ботом
    """
    city = update.message.text.partition(' ')[2].lower().strip()
    chat_id = update.message.chat.id
    if chat_id not in games:
        game = dict()
        game['cities'] = deepcopy(cities_dict)
        games[chat_id] = game
    if city in cities:
        if games[chat_id].get('next_letter') and (city[0] != games[chat_id].get('next_letter')):
            res = 'Тебе на {}!'.format(games[chat_id].get('next_letter'))
        else:
            if city in games[chat_id]['cities'][city[0]]:
                games[chat_id]['cities'][city[0]].remove(city)
                if games[chat_id]['cities'].get(city[-1], set()):
                    res = games[chat_id]['cities'][city[-1]].pop().capitalize() 
                    games[chat_id]['next_letter'] = res[-1]
                    res += ', твой ход!'
                else:
                    res = 'Ты выиграл!'
                    games.pop(chat_id)
            else:
                res = 'Такой город уже был!' 
    elif 'сдаюсь' in city:
        games.pop(chat_id)   
        res = 'Ладно!'    
    else:
        res = 'Нет такого города!'
    update.message.reply_text(res)
    logging.info(res)

def main():
    
    with open('../lesson1/bot/auth_config.json', 'r') as f:
        token = json.loads(f.read())['token']

    my_bot = Updater(token)
    logging.info('Бот запускается')

    dp = my_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", process_planet))
    dp.add_handler(CommandHandler("calc", calculator))
    dp.add_handler(CommandHandler("cities", play_cities))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    my_bot.start_polling()
    my_bot.idle()

if __name__ == "__main__":
    cities = set()
    with open('cities.csv', 'r', encoding='cp1251') as f:
        fields = [
            'id',
            'country_en',
            'region_en',
            'city_en',
            'country',
            'region',
            'city',
            'lat',
            'lng',
            'population'
        ]
        reader = DictReader(f, fields, delimiter=';')
        for row in reader:
            cities.add(row['city'].lower())
    letters = set([c[0] for c in cities])
    cities_dict = {l: set([c for c in cities if c[0] == l]) for l in letters}
    games = {}

    main()