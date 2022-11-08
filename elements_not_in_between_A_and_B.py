n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=[]
for i in range(len(l)):
    if(l[i]<a or l[i]>b):
        r.append(l[i])
if(len(r)==0):
    print(-1)
else:
    print(*r)