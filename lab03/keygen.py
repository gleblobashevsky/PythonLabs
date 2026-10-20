'''Lobashevsky Gleb R3140 559599'''
from random import randint


def choose_random_boundaries():
    '''Функция для случайного выбора гранич интервала'''
    start = randint(1, 26)
    end = randint(start, 26)
    return start, end


def generate_key():
    '''Функция для генерации самого ключа'''
    start, end = choose_random_boundaries()
    key = ''.join([str(chr(64 + randint(start, end))) for _ in range(7)])
    return key, start, end


def main_func():
    '''Функция для представления готового ключа в удобном для меня виде'''
    k, s, e = generate_key()
    return (f'{str(s).rjust(2, "0")}\n'
            f'{k}\n'
            f'{str(e).rjust(2, "0")}')
