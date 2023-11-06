n=int(input())
m=list(map(int,input().split()))
x=sum(m)
y=0
c=0
while y<=x:
    y+=max(m)
    x=x-max(m)
    m.remove(max(m))
    c+=1
print(c)
