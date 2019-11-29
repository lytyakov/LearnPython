def compare_strings(string_1, string_2):

    if not (isinstance(string_1, str) and isinstance(string_2, str)):
        return 0
    elif string_1 == string_2:
        return 1
    elif len(string_1) > len(string_2):
        return 2
    elif string_2 == 'learn':
        return 3

if __name__ == "__main__":
    print(
        compare_strings(
            input('Введите строку 1: '),
            input('Введите строку 2: ')
        )
    )