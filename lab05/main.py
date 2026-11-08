from re import findall
from itertools import zip_longest
from csv import writer

def task1():
    with open('task1-ru.txt', encoding='utf-8') as f:
        data = f.read()
    words = findall(r'\b[А-Яа-яЁё]+е\b', data)
    nums = findall(r'\([0-9.,]+\)', data)
    print('Числа:', "Слова:")
    for i in zip_longest(nums, words, fillvalue='   '):
        print('    '.join(i))


def task2():
    with open('task2.html', encoding='utf-8') as f:
        data = f.read()
    img = findall(r'<img[^>]+>', data)
    sizes_w = []
    sizes_h = []
    for teg in img:
        szh = findall(r'(height)=["\']?(\d+)["\']?', teg)
        szw = findall(r'(width)=["\']?(\d+)["\']?', teg)
        if len(szw) != 0:
            sizes_w.append(szw[0][1])
        if len(szh) != 0:
            sizes_h.append(szh[0][1])
    print('Высоты:  Широты:')
    for sz in zip_longest(sizes_h, sizes_w, fillvalue=' '):
        print(str(' ' * (9 - len(sz[0]))).join(sz))

def task3():
    with open("task3.txt", "r", encoding="utf-8") as f:
        data = f.read()

    ids = findall(r"\b\d+\b", data)
    emails = findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)
    dates = findall(r"\d{4}-\d{2}-\d{2}", data)
    urls = findall(r"https?://[^\s]+", data)
    names = findall(r"\b[A-Z][a-z]+(?: [A-Z][a-z]+)?\b", data)

    table = list(zip(ids, names, emails, dates, urls))

    table_sorted = sorted(table, key=lambda x: int(x[0]))

    with open("result.csv", "w", newline="", encoding="utf-8") as csvfile:
        wr = writer(csvfile)
        wr.writerow(["ID", "Фамилия", "Email", "Дата", "Сайт"])
        wr.writerows(table_sorted)
    print("Данные сохранены в файл result.csv")

def add_task():
    with open("task_add.txt", "r", encoding="utf-8") as f:
        data = f.read()
    emails = findall(r" [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", data)
    dates1 = findall(r" \d{4}-\d{2}-\d{2}", data)
    dates2 = findall(r" \d{4}\.\d{2}\.\d{2}", data)
    dates3 = findall(r" \d{4}/\d{2}/\d{2}", data)
    dates4 = findall(r" \d{2}-\d{2}-\d{4}", data)
    dates5 = findall(r" \d{2}\.\d{2}\.\d{4}", data)
    dates6 = findall(r" \d{2}/\d{2}/\d{4}", data)
    urls = findall(r" https?://[^\s]+", data)
    print(len(emails) + len(dates1) + len(dates2) + len(dates3) + len(dates4) + len(dates5) + len(dates6) + len(urls))

if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    add_task()
    pass
