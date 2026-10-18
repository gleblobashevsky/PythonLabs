'''Lobashevsky Gleb R3140 559599 variant 9'''
from csv import reader
from os import remove
from random import randint
from xml.dom.minidom import parse

'''Обработка исходного файла с данными'''
with open('books-en.csv') as csvfile:
    rdr = reader(csvfile, delimiter=';')
    data = [i for i in rdr]
    data.pop(0)


def task1():
    '''Задание 1: Вывод кол-ва записей с названием длиннее 30 символов'''
    global data
    counter = 0
    for row in data:
        if len(row[1]) > 30:
            counter += 1
    print(counter)


def task2():
    '''Задание 2: Поиск книги по автору + стоимость от 200Р'''
    global data
    author = input("Choose the current book's author: ")
    flag = False
    for row in data:
        if row[2].lower() == author.lower() and float(row[-1].replace(',', '.')) >= 200:
            print('\t', row[1])
            flag = True
    if not flag:
        print("There is no the current book's author")
        task2()


def task3():
    '''Задание 3: Генератор библиографических ссылок'''
    global data
    content = data.copy()
    try:
        remove('bibliographic_references.txt')
    except:
        pass
    flag = 20
    while flag:
        n_row = abs(flag - 20) + 1
        row = content[randint(1, len(content))]
        content.remove(row)
        link = (f'{n_row}) {row[2]}. {row[1]} - {row[3]}')
        print(link, file=open('bibliographic_references.txt', 'a'))
        flag -= 1


def task4():
    '''Задание 4: Распарсивание файла + Два отдельных списка NumCode и CharCode'''
    dom = parse('currency.xml')
    num_codes = [int(elem.firstChild.data) for elem in dom.getElementsByTagName('NumCode')]
    char_codes = [elem.firstChild.data for elem in dom.getElementsByTagName('CharCode')]

    print(num_codes)
    print(char_codes)


def dop1():
    '''Доп задание: Перечень издательств без повторений'''
    global data
    print(*set(el[5] for el in data), sep='\n')


def dop2():
    '''Доп задание: Самые популярные 20 книг'''
    global data
    content = data.copy()
    content.sort(key=lambda x: (-int(x[4])))
    print('The most famous books:')
    for n, el in enumerate(content[:20], start=1):
        print(f'{n}) {el[1]}  —  {el[4]} downloads')


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # dop1()
    # dop2()
    pass
