from os.path import split
import random
import math
import re
import itertools
from datetime import datetime, timedelta

def num_in_money (number):
    # Если число отрицательное, то ошибка
    if number < 0:
        raise ValueError('Некорректный формат')

    # Преобразование типов
    rubles = int(number)
    kopeks = int(round((number - rubles) * 100))

    #Возвращение значения ф-ции
    return f'{rubles} рублей, {kopeks} копеек'

numbers_1 = [1, 2, 3, 2, 5, 6, 7]

def sequence_numbers (numbers):
    if len(numbers) <= 1:
        return True

        # Проходим по списку до предпоследнего элемента
    for i in range(len(numbers) - 1):
        # Если следующий элемент не больше текущего - последовательность не возрастающая
        if numbers[i] >= numbers[i + 1]:
            return False

        # Если дошли до конца и не нашли нарушений - последовательность возрастающая
    return True

def encryp (number_card):
    number_card = str(number_card)
    if len(number_card) == 16:
        result = number_card[:4] + ' **** **** ' + number_card[11:15]
        return result
    else:
        return 'Некорректный ввод!'

def text_to_words(text):
    words = text.lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()

    # Создаем три списка для разных категорий слов
    long_words = []  # длина > 7
    medium_words = []  # длина от 4 до 7
    short_words = []  # длина < 4
    for word in words:
        if len(word) > 7:
            long_words.append(word)
        if 4 <= len(word) <= 7:
            medium_words.append(word)
        if len(word) <= 3:
            short_words.append(word)
    return f'Слова, превышающие 7 символов: {long_words} \nСлова 4-7 символов: {medium_words} \nСлова меньше 4 символов: {short_words}'

def text_to_upper(text):
    # Разбиваем текст на слова, сохраняя разделители
    words = []
    current_word = ""
    separator = ""

    for char in text:
        if char in [' ', ',']:
            if current_word:
                words.append((current_word, separator))
            separator = char
            current_word = ""
        else:
            current_word += char

    # Добавляем последнее слово, если оно есть
    if current_word:
        words.append((current_word, ""))

    # Обрабатываем каждое слово
    result = ""
    for word, sep in words:
        # Если слово начинается с заглавной буквы, преобразуем его в верхний регистр
        if word and word[0].isupper():
            result += word.upper() + sep
        else:
            result += word + sep

    return result

def unique_words(text):
    # Создаем словарь для подсчета количества каждого символа
    char_count = {}

    # Подсчитываем количество каждого символа в тексте
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    # Находим символы, которые встречаются только один раз
    unique_chars = [char for char, count in char_count.items() if count == 1]

    return unique_chars

def web(urls):
    processed_urls = [
        ('http://' + url if url.startswith('www') else url) +
        ('.com' if not url.endswith('.com') else '')
        for url in urls
    ]

    # Вывод обработанных адресов
    print("Обработанные URLs:")
    for url in processed_urls:
        print(url)

def random_array():
    # Генерация случайного числа n в диапазоне от 1 до 10000
    n = random.randint(1, 10000)

    # Создание массива со случайными целыми числами
    random_array = [random.randint(-1000, 1000) for _ in range(n)]

    # Вычисление ближайшей степени двойки
    next_power_of_two = 2 ** math.ceil(math.log2(n))

    # Дополнение массива нулями до ближайшей степени двойки
    padded_array = random_array + [0] * (next_power_of_two - n)

    # Вывод информации о генерации
    print(f"Сгенерированное число n: {n}")
    print(f"Размер исходного массива: {len(random_array)}")
    print(f"Размер дополненного массива: {len(padded_array)}")
    print(f"Ближайшая степень двойки: {next_power_of_two}")

    # Демонстрация первых 10 элементов массива
    print("\nПервые 10 элементов дополненного массива:")
    print(padded_array[:10])

def money_atm(sum):
    money = [5000, 2000, 1000, 500, 200, 100]
    # Сортировка номиналов по убыванию
    denominations = sorted(money, reverse=True)

    # Отслеживание использованных купюр
    used_bankomats = {}

    # Попытка снятия денег
    for denomination in denominations:
        # Расчет количества купюр текущего номинала
        if denomination <= sum:
            needed_count = sum // denomination
            used_bankomats[denomination] = needed_count
            sum %= denomination

    # Проверка полноты снятия суммы
    if sum == 0:
        # Форматирование вывода как "5*1000 + 3*100 + 1*50 + 2*10"
        return ' + '.join([f"{count}*{denom}" for denom, count in used_bankomats.items()])
    else:
        return "Операция не может быть выполнена!"

def secure_pass(password):
    if len(password) < 8:
        return f'Пароль {password} содержит меньше 8 символов. Он небезопасен.'
    else:
        if password.isdigit():
            return f'Пароль {password} содержит одни цифры. Он небезопасен.'
        if password.isalpha():
            return f'Пароль {password} содержит одни буквы. Он небезопасен.'

            # Проверка, содержит ли пароль и цифры, и буквы
        has_digit = bool(re.search(r'\d', password))
        has_letter = bool(re.search(r'[A-Za-z]', password))

        # Проверка, содержит ли пароль специальные символы
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

        # Оценка пароля
        if has_digit and has_letter and has_special:
            return f'Пароль {password} отличный: содержит цифры, буквы и специальные символы.'
        elif has_digit and has_letter:
            return f'Пароль {password} хороший: содержит цифры и буквы.'
        else:
            return f'Пароль {password} простой: не соответствует требованиям.'

def frange(num1, num2, step):
    # Инициализация текущего значения
    current = num1
    # Генерация чисел
    while current < num2:
        yield current
        current += step

def get_frames(signal, size, overlap):

    step = int(size * (1 - overlap))  # Шаг для следующего фрагмента
    index = 0  # Начальный индекс

    # Генерация фрагментов
    while index + size <= len(signal):
        yield signal[index:index + size]
        index += step

def extra_enumerate(iterable):

    total = sum(iterable)  # Общая сумма элементов
    cum = 0  # Накопленная сумма

    for i, elem in enumerate(iterable):
        cum += elem  # Обновляем накопленную сумму
        frac = cum / total  # Вычисляем долю накопленной суммы
        yield i, elem, cum, frac

def non_empty(func):
    def wrapper(*args, **kwargs):
        # Получаем результат оригинальной функции
        result = func(*args, **kwargs)
        # Фильтруем пустые строки и None
        if isinstance(result, list):
            return [x for x in result if x and x is not None]
        return result
    return wrapper

def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            # Создаем копию списка для обработки
            processed = [s[0]]  # Первый элемент остается без изменений
            for i in range(1, len(s)):
                # Применяем формулу s[i] = s[i] - a*s[i-1]
                processed.append(s[i] - a * s[i-1])
            return func(processed)
        return wrapper
    return decorator

def pre_process(a=0.97):
    def decorator(func):
        def wrapper(s):
            # Создаем копию списка для обработки
            processed = [s[0]]  # Первый элемент остается без изменений
            for i in range(1, len(s)):
                # Применяем формулу s[i] = s[i] - a*s[i-1]
                processed.append(s[i] - a * s[i-1])
            return func(processed)
        return wrapper
    return decorator


def create_football_schedule():
    # Список команд
    teams = [
        "Реал Мадрид", "Барселона", "Бавария", "ПСЖ",
        "Манчестер Сити", "Ливерпуль", "Челси", "Ювентус",
        "Интер", "Милан", "Аякс", "Порту",
        "Боруссия Д", "Атлетико", "Бенфика", "РБ Лейпциг"
    ]

    # Перемешиваем команды
    random.shuffle(teams)

    # Создаем 4 группы по 4 команды
    groups = [teams[i:i + 4] for i in range(0, 16, 4)]

    # Выводим группы
    for i, group in enumerate(groups, 1):
        print(f"\nГруппа {i}:")
        for team in group:
            print(team)

    # Создаем календарь игр
    print("\nКалендарь игр:")
    # Начальная дата (14 сентября текущего года)
    current_year = datetime.now().year
    start_date = datetime(current_year, 9, 14, 22, 45)

    # Для каждой группы создаем расписание матчей
    for group_num, group in enumerate(groups, 1):
        print(f"\nМатчи группы {group_num}:")
        # Создаем все возможные пары команд в группе
        matches = list(itertools.combinations(group, 2))

        for i, (team1, team2) in enumerate(matches):
            # Каждая следующая игра через 2 недели
            match_date = start_date + timedelta(weeks=2 * i)
            print(f"{match_date.strftime('%d/%m/%Y, %H:%M')} - {team1} vs {team2}")

def main():
    try:
        number_1 = 23.45
        number_2 = 10

        print(num_in_money(number_1))
        print(num_in_money(number_2))

        print('\n')

        print(sequence_numbers(numbers_1))
        print('\n')

        print(encryp(1000256756454455))
        print('\n')

        print(text_to_words('Добрый день. Сегодня мы изучим тему, как Объекты, Инкапсуляция, наследование.'))
        print('\n')

        print(text_to_upper('улица Артема, проспект Мира, парк Щербакова'))
        print('\n')

        print(unique_words("Донецкий Государственный Университет"))
        print('\n')

        # Исходный список адресов
        urls = [
            'www.google.com',
            'www.yandex.ru',
            'python.org',
            'www.github.net'
        ]

        print(web(urls))
        print('\n')

        random_array()
        print('\n')

        print(money_atm(3450))
        print(money_atm(18400))
        print('\n')

        print(secure_pass('12345678'))
        print(secure_pass('1234hgf'))
        print(secure_pass('jonyjony'))
        print(secure_pass('Jony1325'))
        print('\n')

        for x in frange(1, 5, 0.5):
            print(x)
        print('\n')

        signal = [i for i in range(16)]  # Пример сигнала (список чисел от 0 до 15)
        for frame in get_frames(signal, size=4, overlap=0.4):
            print(frame)
        print('\n')

        x = [1, 3, 4, 2]
        for i, elem, cum, frac in extra_enumerate(x):
            print(f"({elem}, {cum}, {frac})", end=" ")
        print('\n')

        @non_empty
        def get_pages():
            return ['chapter1', '', 'contents', '', 'line1']

        result = get_pages()
        print(result)
        print('\n')

        @pre_process(a=0.93)
        def plot_signal(s):
            for sample in s:
                print(sample)

        signal = [1.0, 2.0, 3.0, 4.0, 5.0]
        plot_signal(signal)
        print('\n')

        print("\nФутбольное расписание:")
        create_football_schedule()

    except ValueError as e:
        if str(e) == "Некорректный формат!":
            print(e)
        else:
            print("Некорректный формат!")


if __name__ == "__main__":
    main()