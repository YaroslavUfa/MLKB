a = float(input('введи число 1'))
b = float(input('введи число 2'))
c = int(input('введи до какого числа будет округляться среднее арифметическое 2-ух чисел'))
d = (a + b) / 2
e = round(d, c)
print(e)