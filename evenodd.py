n=list(map(int,input().split()))
m=n[0]
k=n[1]
a=[]
b=[]
for i in range(1,m+1):
    if i%2==0:
        b.append(i)
    else:
        a.append(i)
c=a+b
print(c[k-1])