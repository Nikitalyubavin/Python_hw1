# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

quantity = int(input("Введите количество сделанных журавликов: "))

a = round(quantity / 6, 1)
b = a * 4

print(f"{quantity} -> Петя - {a}, Сережа - {a}, Катя - {b}")