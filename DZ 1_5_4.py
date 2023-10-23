a = input().split()
b = input().split()
c = input().split()
d = []
for i in a:
    if i in b and i in c:
        d.append(i)
if d:
    d.sort()
    print(' '.join(d))
else:
    print('Все три задачи никто не решил')
