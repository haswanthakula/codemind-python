T = int(input())
for i in range(T):
    n = int(input())
    t = n
    rev = 0
    while n > 0:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
    print(t==rev)