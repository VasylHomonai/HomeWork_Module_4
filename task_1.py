from pathlib import Path
import sys

path = Path('files/Salaries.txt')

def total_salary(path) -> tuple:
    try:
        with open(path, encoding='utf-8') as file:
            list_numb = []  # Створюємо список для збереження в ньому всіх зарплат
            for line in file:
                temp_list = line.strip().split(',') # Тимчасовий список для кожного рядку
                list_numb.append(int(temp_list[1])) # Додаємо кожну зарплату до списку
    
        total = sum(list_numb)  # Вираховуємо загальну суму зарплат
        average = round(total / len(list_numb)) # Вираховуємо середню суму зарплат

        return (total, average) # Передаємо результат
    
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        sys.exit(1)  # Завершити програму
    except UnicodeDecodeError:
        print("Файл пошкоджений або має неправильне кодування.")
        sys.exit(1)  # Завершити програму
    except Exception as e:
        print(f"Сталася помилка: {e}")
        sys.exit(1)  # Завершити програму
    
def print_result(total, average):
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    
total, average = total_salary(path)

# Вивід результату
print_result(total, average)