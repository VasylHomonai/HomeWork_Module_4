from pathlib import Path

path = Path('files/Cats_info.txt')

def get_cats_info(path)->list:
    try:
        with open(path, encoding='utf-8') as file:
            list_cats = []  # Створюємо список для збереження в ньому інформації про котів
            keys = ['id', 'name', 'age']
            for line in file:
                temp_cats = line.strip().split(',') # Тимчасовий список для кожного рядку
                list_cats.append(dict(zip(keys, temp_cats)))
        
        return list_cats # Передаємо результат

    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except UnicodeDecodeError:
        print("Файл пошкоджений або має неправильне кодування.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


if __name__ == '__main__':
    cats_info = get_cats_info(path)
    if cats_info:
        print(cats_info)
    else:
        print("Неможливо обробити файл, або він порожній!")