# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите длину шоколадки (в дольках): '))
m = int(input('Введите ширину шоколадки (в дольках): '))
k = int(input('Введите нужное количество долек: '))

if (k in range(n, m*n + 1, n) or k in range(m, m*n + 1, m)): print(f"{n} {m} {k} -> yes")
else: print(f"{n} {m} {k} -> no")