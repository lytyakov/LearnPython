def ask_user():
    to_continue = True
    while to_continue:
        ans = input('Как дела?')
        to_continue = ans != 'Хорошо'

def ask_user_and_answer():
    print('Для прекращения работы программы введите "Стоп"')
    quest_answ = {
        'Как дела?': 'Хорошо',
        'Что делаешь?': 'Работаю',
        'Как настроение?': 'Нормально'
    }
    
    while True:
        quest = input('Введите вопрос: ')
        if 'стоп' in quest.lower():
            break
        print(quest_answ[quest])

if __name__ == "__main__":
    ask_user()
    ask_user_and_answer()