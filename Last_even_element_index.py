n=int(input())
l=list(map(int,input().split()))
evenn=0 
for i in range(0,len(l)):
    if(l[i]%2==0):
        y=i 
print(y)