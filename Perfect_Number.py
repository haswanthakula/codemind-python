def isperfect(n):
    c = 0
    for i in range(1,n):
        if n%i==0:
            c+=i
    if c==n:
        return True
    else:
        return False

n = int(input())
res = isperfect(n)
print(res)