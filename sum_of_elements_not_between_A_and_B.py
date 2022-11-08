a=int(input())
n=list(map(int,input().split()))
b,c=map(int,input().split())
s=0
q=0
for i in range(0,len(n)):
    if (n[i] in range (b,c+1)):
        continue
    else:
        s=s+n[i]
print(s)