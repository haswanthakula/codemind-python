n = int(input())
c = 0
e = o = 0
while n > 0:
    r = n % 10
    if r % 2 == 0:
        e += 1
    elif r % 2 != 0:
        o += 1
    n = n // 10
    c += 1
if  c == e:
    print('Even')
elif c == o:
    print('Odd')
else:
    print('Mixed')