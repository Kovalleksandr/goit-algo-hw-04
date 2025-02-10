from data import total_salary

path = "home_work_1\\salary.txt"
total, average = total_salary(path)

if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
