'''Lobashevsky Gleb R3140 559599 variant 9'''
from os import system, name
from time import sleep

# Цветовые коды ANSI для форматирования вывода в терминале
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
GREEN = '\u001b[42m'
RESET = '\u001b[0m'
YELLOW = '\u001b[43m'
BRIGHT_YELLOW = '\u001b[33m'


def country():
    '''Задание 1: Вывод флага Финляндии с помощью цветных блоков.'''
    string = '   '
    for i in range(5):
        if i != 2:
            print(f'{WHITE}{string * 3}{BLUE}{string}{WHITE}{string * 6}{RESET}')
        else:
            print(f'{BLUE}{string * 10}{RESET}')
    print()


def pattern(h=1, w=2):
    '''Задание 2: Вывод геометрического узора по заданным высоте и ширине.'''
    string = '   '
    print(f'{WHITE}{string * (w * 2 * 7 + w + 1)}{RESET}')
    for _ in range(h):
        print(
            f'{WHITE}{string}{RESET}' + f'{WHITE}{string * 2}{BLACK}{string * 3}{WHITE}{string * 4}{BLACK}{string * 3}{WHITE}{string * 3}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{WHITE}{string * 1}{BLACK}{string * 5}{WHITE}{string * 2}{BLACK}{string * 5}{WHITE}{string * 2}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{BLACK}{string * 14}{WHITE}{string}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{BLACK}{string * 14}{WHITE}{string}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{BLACK}{string * 14}{WHITE}{string}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{WHITE}{string * 1}{BLACK}{string * 5}{WHITE}{string * 2}{BLACK}{string * 5}{WHITE}{string * 2}{RESET}' * w,
            f'{WHITE}{string}{RESET}' + f'{WHITE}{string * 2}{BLACK}{string * 3}{WHITE}{string * 4}{BLACK}{string * 3}{WHITE}{string * 3}{RESET}' * w,
            sep='\n')
        print(f'{WHITE}{string * (w * 2 * 7 + w + 1)}{RESET}')
    print()


def file_process():
    '''Задание 3: Чтение чисел из sequence.txt, подсчет процентов для диапазонов [5;10] и [-10;-5] и вывод диаграммы.'''
    file = open('sequence.txt', 'r')
    l1, l2 = [], []
    for line in file:
        num = float(line)
        if 5.0 <= num <= 10.0:
            l1.append(num)
        elif -10.0 <= num <= -5.0:
            l2.append(num)
    file.close()
    first = int(len(l1) / (len(l2) + len(l1)) * 100)
    second = int(len(l2) / (len(l2) + len(l1)) * 100)
    maxfs = max(first, second)
    print(f'{YELLOW}{' ' * first}{RESET}    {' ' * (round(maxfs - first))}{first}%')
    print(f'{GREEN}{' ' * second}{RESET}    {' ' * (round(maxfs - second))}{second}%')


def animation():
    '''Задание 4: Анимация ракеты с эффектами в консоли (бесконечный цикл до Ctrl+C).'''
    frames = [
        r'''  ✦         *              .        ✦
     .           ✦              *        .
  *      .                                ✦
                        ___---___
                      .'         `.      ✦
   ✦                 /             \  *
      *             |               |      .
  .                 |               | ✦
        ✦            \             /      *
                      `.         .'
                        `---___--'
  ✦         .              *        ✦
     *           ✦              .        *''',
        fr'''   ✦         *              .        ✦
      .           ✦              *        .
   *      .                                ✦
                        ___---___
   ✦                  .'    |{BRIGHT_YELLOW}███{RESET} `.         ✦
       *             /      |{BRIGHT_YELLOW}████{RESET}  \    *
   .                |       |{BRIGHT_YELLOW}█████{RESET}  |        .
         ✦          |       |{BRIGHT_YELLOW}█████{RESET}  |   ✦
                     \      |{BRIGHT_YELLOW}████{RESET}  /         *
   ✦                  `.    |{BRIGHT_YELLOW}███{RESET} .'     ✦
                        `---___--'
   ✦         .              *        ✦
      *           ✦              .        *''',
        fr'''  ✦         *              .        ✦
     .           ✦              *        .
  *      .                                ✦
                        ___---___
                      .'{BRIGHT_YELLOW}█████████{RESET}`.        ✦
   ✦                 / {BRIGHT_YELLOW}████████████{RESET}\   *
      *             |{BRIGHT_YELLOW}███████████████{RESET}|     .
  .                 |{BRIGHT_YELLOW}███████████████{RESET}|  ✦
        ✦            \{BRIGHT_YELLOW}█████████████{RESET}/      *
                      `.{BRIGHT_YELLOW}█████████{RESET}.'
                        `---___--'
  ✦         .              *        ✦
     *           ✦              .        *''',
        fr'''   ✦         *              .        ✦
      .           ✦              *        .
   *      .                                ✦
                        ___---___
   ✦                  .' {BRIGHT_YELLOW}███{RESET}|    `.         ✦
       *             /  {BRIGHT_YELLOW}████{RESET}|      \    *
   .                | {BRIGHT_YELLOW}██████{RESET}|       |        .
         ✦          | {BRIGHT_YELLOW}██████{RESET}|       |   ✦
                     \  {BRIGHT_YELLOW}████{RESET}|      /         *
   ✦                  `. {BRIGHT_YELLOW}███{RESET}|    .'     ✦
                        `---___--'
   ✦         .              *        ✦
      *           ✦              .        *'''
    ]
    queue = [0, 1, 2, 3]
    try:
        while True:
            for i in queue:
                system('cls' if name == 'nt' else 'clear')
                print(frames[i])
                sleep(0.5)
    except KeyboardInterrupt:
        print("\n🌙 Цикл завершён...")


def func():
    '''Задание 5: Построение графика функции y = x/2 в первой четверти с осями координат.'''
    n, m = 17, 9
    table = [[0] * n for _ in range(m)]

    for y in range(n):
        for x in range(n):
            if x == 2 * y:
                row = (m - 1) - y
                table[row][x] = 1

    for i in table:
        print('│', end='')
        for j in i:
            match j:
                case 0:
                    print(' ' * 4, end='')
                case 1:
                    print(f' {WHITE}{' ' * 8}{RESET}', end='')
        print('')
    print(f'┼{"—" * len(table[0] * 5)}')


if __name__ == '__main__':
    # country()
    # pattern()
    # file_process()
    # animation()
    # func()
    pass
