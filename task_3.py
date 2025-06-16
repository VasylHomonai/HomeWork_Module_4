from colorama import Fore, Back, Style
import sys
from pathlib import Path, PurePath
import shutil


def color_text(path, fore_color):
    # Ця ф-ція для друку назв каталогів та файлів з заповненням чоним фоном всього рядка терміналу
    # Отримання назви кореневої директорії
    dir_file = f'{PurePath(path).name}/'
    # Отримати ширину терміналу
    terminal_width = shutil.get_terminal_size().columns
    # Створення рядка із заповненням пробілами
    full_line = dir_file.ljust(terminal_width)
    # Виведення назви директорії синім кольором з чорним фоном на весь рядок
    print(Back.BLACK + fore_color + full_line + Style.RESET_ALL)


def print_dir(path, count=1):

    for item in path.iterdir():
        indent = '    ' * count
        path = f"{indent}{item.name}"
        if item.is_file():
            # Відрисовуємо кожний файл
            color_text(path, Fore.GREEN)
        elif item.is_dir():
            # Відрисовуємо кожну директорію
            color_text(path, Fore.BLUE)
            # Рекурсивно провіряємо кожну директорію на її вміст
            print_dir(item, count + 1)


# Провірка на параметр в скрипті
if len(sys.argv) >= 2:
    param = sys.argv[1]
    path = Path(param)

    # Провірка на існування директорії
    if path.exists():

        # Провірка на файл
        if path.is_file():
            print("The parameter must be a directory!")
            sys.exit(1)  # Завершити програму

        # Відрисовуємо кореневу директорію
        color_text(path, Fore.BLUE)

        # Передаємо кореневу директорію в рекурсивну ф-цію для відрисовки всіх вкладених файлів та директорій
        print_dir(path)
    else:
        print(f"This directory '{path}' does not exist!")
else:
    print('Parameter not specified!')


"""
Правильний запуск скрипта з командного рядка на Windows: python .\task_3.py files/picture
Результат: https://prnt.sc/w6cVKF7sMiMI

Не правильний запуск скрипта з командного рядка на Windows: python .\task_3.py files/pic
Результат: https://prnt.sc/e5xBAPNCL_Uq

Запуск скрипта без параметрів з командного рядка на Windows: python .\task_3.py
Результат: https://prnt.sc/UDDrtEEGXziy
"""
