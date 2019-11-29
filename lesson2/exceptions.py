def ask_user():
    while True:
        try:
            ans = input('Как дела?')
            if ans == 'Хорошо':
                break
        except KeyboardInterrupt:
            print('Пока')
            break

def discounted(price, discount, max_discount=20):
    try:
        if any((
            isinstance(price, bool),
            isinstance(discount, bool),
            isinstance(max_discount, bool)
        )):
            raise TypeError
        price = abs(price)
        discount = abs(discount)
        max_discount = abs(max_discount)
    except TypeError:
        return 'Умею работать только с числами'
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)
    

if __name__ == "__main__":
    ask_user()
    print(discounted(100, 10))