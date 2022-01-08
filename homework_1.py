def ending_of_words(number: int) -> str:
    """
    Функция принимает число, переводит его в список, сверяет по индексам,
    и в зависимости от цифр числа подбирает нужные окончания к слову питон
    затем возвращает число вместе со словом с нужным окончанием
    :param number: число
    :return: строка
    """
    new_number = list(str(number))

    if int(new_number[-1]) == 0:
        return f'{number} питонов'
    elif int(new_number[-1]) == 1 and len(new_number) == 1:
        return f'{number} питон'
    elif int(new_number[-1]) in range(2, 5) and len(new_number) == 1:
        return f'{number} питона'
    elif int(new_number[-1]) == 1 and int(new_number[-2]) == 0:
        return f'{number} питон'
    elif int(new_number[-1]) == 1 and int(new_number[-2]) in range(2, 10):
        return f'{number} питон'
    elif int(new_number[-1]) in range(5, 10):
        return f'{number} питонов'
    elif int(new_number[-2]) == 1 and int(new_number[-1]) in range(1, 10):
        return f'{number} питонов'
    elif int(new_number[-2]) in range(2, 10) and int(new_number[-1]) in range(2, 5):
        return f'{number} питона'


def speciality(input_value: str) -> list:
    """
    Функция принимает на ввод название специальности
    и выводит список сотрудников с данной специальностью
    :param input_value: строка
    :return: список
    """

    dict_ = {
        "Мария А.": "Фронтендер",
        "Алексей А.": "Фронтендер",
        "Иван Б.": "Бэкендер",
        "Тоня И.": "Бэкендер",
        "Дарья Д.": "Тестировщик",
        "Валерия К.": "Бэкендер",
        "Дарья У.": "Тестировщик",
    }

    keys_list = []

    for key, value in dict_.items():
        if value == input_value:
            keys_list.append(key)
    return keys_list


def mendeleev(input_key: int) -> str:
    """
    Функция принимает номер элемента из таблицы Менделеева
    и выводит название этого элемента, а также соседние с ним элементы
    :param input_key: число
    :return: строка
    """
    dict_ = {
        1: 'Водород', 2: "Гелий", 3: "Литий", 4: "Бериллий", 5: "Бор", 6: "Углерод", 7: "Азот", 8: "Кислород",
        9: "Фтор", 10: "Неон", 11: "Натрий", 12: "Магний", 13: "Алюминий", 14: "Кремний", 15: "Фосфор", 16: "Сера",
        17: "Хлор", 18: "Аргон", 19: "Калий", 20: "Кальций", 21: "Скандий", 22: "Титан", 23: "Ванадий", 24: "Хром",
        25: "Марганец", 26: "Железо", 27: "Кобальт", 28: "Никель", 29: "медь", 30: "цинк"
    }
    for key, value in dict_.items():
        nearby_key1 = input_key - 1
        nearby_key2 = input_key + 1

        if key == input_key and nearby_key1 == 0:
            return f'{key} это {value}\nСоседи:\n{nearby_key2} {dict_.get(nearby_key2)}'

        elif key == input_key:
            return f'{key} это {value}\n' \
                   f'Соседи:\n{nearby_key1} {dict_.get(nearby_key1)}\n{nearby_key2} {dict_.get(nearby_key2)}'


def cipher() -> str:
    """
    Функция достает из зашифрованной строки каждый четвертый символ
    :return: строка
    """

    message = "Рооз наа фмдиц а ывч ыва оо ивкр ьке пвшпрце уенпвта"
    return message[3::4]


if __name__ == '__main__':
    start = int(input('Введите номер задания: '))
    if start == 1:
        input_ = int(input('Введите число: '))
        print(ending_of_words(input_))
    elif start == 2:
        input_2 = input('Введите специальность: ')
        print(speciality(input_2))
    elif start == 3:
        input_3 = int(input('Введите номер элемента таблицы Менделеева: '))
        print(mendeleev(input_3))
    elif start == 4:
        print(cipher())

