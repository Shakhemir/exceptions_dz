"""
Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
Посмотрите на код, и подумайте сколько разных типов исключений вы тут сможете получить?
Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. Если длины массивов не равны,
необходимо как-то оповестить пользователя.
* Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив,
каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке. Если длины массивов не равны,
необходимо как-то оповестить пользователя. Важно: При выполнении метода единственное исключение,
которое пользователь может увидеть - RuntimeException, т.е. ваше.
"""


def method_1(prompt: str = "Введите число"):
    while True:
        try:
            number = int(input(f"{prompt}: "))
            return number
        except ValueError:
            print("Вы не ввели целое число. Попробуйте заново!")


def method_2():
    file_name = input('Введите имя файла: ')
    try:
        f = open(file_name)
        print(f.read())
    except FileNotFoundError:
        print('Файл с таким именем не найден')
    except PermissionError:
        print('Нет доступа к файлу')
    except IsADirectoryError:
        print('Это директория!')


def method_3(arr: list):
    index = method_1(f'Введите индекс списка [0..{len(arr) - 1}]')
    try:
        value = arr[index]
        print(f"Значение списка с индексом {index} = {value}")
    except IndexError:
        print("Индекс из аут оф рендж")


print('Метод 1. Введенное число:', method_1())

print('Метод 2. Считываем содержимое файла')
method_2()

print('Метод 3. Индекс из списка')
method_3([1, 345, 5, -1])