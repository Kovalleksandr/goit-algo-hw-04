def get_cats_info(path):
    cat_list = []
    try:
        with open(path, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) == 3:
                            cat_id, name, age = parts
                            cat_list.append({"id": cat_id, "name": name, "age": age})
                        else:
                            print(f'Помилка у форматі рядка: {line}')
    except FileNotFoundError:
        print(f'Файл {path} не знайдено')
    except Exception as e:
        print(f'Виникла помилка: {e}')
    return cat_list        