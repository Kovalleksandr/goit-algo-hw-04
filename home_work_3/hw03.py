import sys
import os
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama (для Windows)
init(autoreset=True)

def print_directory_structure(directory: Path, indent: str = ""):
    """Рекурсивно виводить структуру директорії з кольоровим оформленням"""
    if not directory.is_dir():
        print(Fore.RED + f"Помилка: {directory} не є директорією!")
        return

    try:
        entries = sorted(directory.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
        for entry in entries:
            if entry.is_dir():
                print(indent + Fore.BLUE + f"{entry.name}")  # Синій для директорій
                print_directory_structure(entry, indent + "    ")  # Рекурсія
            else:
                print(indent + Fore.GREEN + f"{entry.name}")  # Зелений для файлів
    except PermissionError:
        print(Fore.RED + "Доступ заборонено")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python hw03.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + f"Помилка: директорія {directory_path} не існує!")
        sys.exit(1)

    print(Fore.YELLOW + f"{directory_path.resolve()}")
    print_directory_structure(directory_path)
