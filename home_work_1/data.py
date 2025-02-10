def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                try:
                    _, salary = line.strip().split(",")
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")
                    continue
            
            total = sum(salaries)
            average = total / len(salaries) if salaries else 0
            
            return total, average
    
    except FileNotFoundError:
        print("Файл {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None
