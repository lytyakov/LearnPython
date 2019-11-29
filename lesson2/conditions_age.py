

def age_converter(age):
    
    try:
        age = float(age)
    except ValueError:
        return 'Ошибка'
    
    if age < 7:
        return 'Детский сад'
    elif age < 18:
        return 'Школа'
    elif age < 23:
        return 'ВУЗ'
    elif age < 60:
        return 'Работа'
    else:
        return 'Пенсия'
    return

if __name__ == "__main__":  
    print(age_converter(input('Введите возраст:')))