items = [
    ("r", 3, 25), ("p", 2, 15), ("a", 2, 15),
    ("m", 2, 20), ("i", 1, 5), ("k", 1, 15),
    ("x", 3, 20), ("t", 1, 25), ("f", 1, 15),
    ("s", 2, 20), ("c", 2, 20)
]

best = 0
best_items = []
combinations = []

start_score = 20 + 10
start_cells = 1

for i in range(2 ** len(items)):
    selected = [('d', 1, 10)]
    used_cells = start_cells
    score = start_score
    comb = bin(i)[2:].zfill(len(items))
    for j in range(len(items)):
        if comb[j] == '1':
            selected.append(items[j])
            used_cells += items[j][1]
            if used_cells > 8:
                break
            score += items[j][2]

        else:
            score -= items[j][2]

    if used_cells > 8:
        continue

    if score > best:
        best = score
        best_items = selected

    if score > 0:
        combinations.append((selected, score))


def show(selected):
    cells = []
    for symbol, size, points in selected:
        for _ in range(size):
            cells.append(symbol)

    while len(cells) < 8:
        cells.append(" ")

    print("[" + "][".join(cells[:4]) + "]")
    print("[" + "][".join(cells[4:8]) + "]")


print("Лучший результат:")
show(best_items)
print("Очки выживания:", best, end='\n\n')

print("Все положительные комбинации:")
print("Количество:", len(combinations), end='\n\n')

for selected, score in combinations:
    show(selected)
    print("Очки выживания:", score, end='\n\n')
