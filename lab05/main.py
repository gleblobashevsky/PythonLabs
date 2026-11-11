import re
from re import findall
from itertools import zip_longest
from csv import writer

def task1():
    with open('task1-ru.txt', encoding='utf-8') as f:
        data = f.read()
    words = findall(r'\b[А-Яа-яЁё]+е\b', data)
    nums = findall(r'\([0-9]+\)', data)
    print('Числа:', "Слова:")
    for i in zip_longest(nums, words, fillvalue='   '):
        print('    '.join(i))


def task2():
    with open('task2.html', encoding='utf-8') as f:
        data = f.read()
    widths = re.findall(r'<img[^>]+?\bwidth\s*=\s*["\']?(\d+)', data)
    heights = re.findall(r'<img[^>]+?\bheight\s*=\s*["\']?(\d+)', data)
    print('Высоты:  Широты:')
    for i in zip_longest(heights, widths, fillvalue='   '):
        print(str(' '*(9-len(i[1]))).join(i))

def task3():
    with open("task3.txt", "r", encoding="utf-8") as f:
        data = f.read()

    ids = findall(r"(?<= )\d+(?= )", data)
    emails = findall(r"[a-zA-Z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}", data)
    dates = findall(r"(?:\d{4}|\d{2})-\d{2}-(?:\d{2}|\d{4})", data)
    urls = findall(r"https?://[^\s\"'<>{}|\\^`[\]]+", data)
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
    emails = findall(r"[a-zA-Z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}", data)
    dates = findall(r'(?:\d{4}|\d{2})[./-]\d{2}[./-](?:\d{2}|\d{4})', data)
    urls = findall(r"https?://[^\s\"'<>{}|\\^`[\]]+", data)
    print(urls)
    print(emails)
    print(dates)
    print(len(emails) + len(dates) + len(urls))

if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # add_task()
    pass
