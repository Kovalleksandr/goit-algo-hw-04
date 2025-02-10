from data import get_cats_info

path = "home_work_2\\cats_info.txt"
cats_info = get_cats_info(path)
for cat in cats_info:
    print(cat)