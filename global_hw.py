import sys
import logging

logging.basicConfig(filename='lottery.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def count_matching_numbers(list1, list2):
    # Проверка длины списков
    if len(list1) != 10 or len(list2) != 10:
        logging.error("Ошибка: списки должны содержать 10 чисел.")
        return None

    count = 0

    # Проверка совпадающих чисел
    for число in list1:
        if число in list2:
            count += 1

    # Логирование полезной информации
    logging.info("Первый список: %s", list1)
    logging.info("Второй список: %s", list2)
    logging.info("Количество совпадающих чисел: %d", count)

    return count


if __name__ == "__main__":
    # Получение списков чисел из командной строки
    if len(sys.argv) != 21:
        logging.error("Ошибка: неверное количество аргументов командной строки.")
        sys.exit(1)

    try:
        # Преобразование аргументов в целые числа
        list1 = [int(x) for x in sys.argv[1:11]]
        list2 = [int(x) for x in sys.argv[11:21]]

        # Вызов функции count_matching_numbers
        result = count_matching_numbers(list1, list2)

        # Вывод результата
        if result is not None:
            print("Количество совпадающих чисел:", result)
    except ValueError:
        logging.error("Ошибка: некорректные значения аргументов.")
        sys.exit(1)


""" Этот файл создан для запуска из консоли. 
                     для создания файла Ошибок и Полезной информации
                     для заполнения файла <<lottery.log>> ошибками и информацией
                     для (конечно же) для проверки 2х лотерейных билетов )))

    пример запуска : 
            python global_hw.py 1 2 3 4 5 6 7 8 9 10 2 4 6 8 10 12 14 16 18 20
    Результат: 
            Количество совпадающих чисел: 5            (я проверил)

"""