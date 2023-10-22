def a():
    n = int(input("Введите количество городов: "))
    b = []
    for i in range(n):
        d = input("Введите название города: ")
        b.append(d.lower())  
    c = set([x for x in b if b.count(x) > 1])
    print("Количество городов, названия которых повторяются:", len(c) * 2)
a()
