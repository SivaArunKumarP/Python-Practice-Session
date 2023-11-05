n=int(input())
c=[1]
for i in range(2,n+1):
    if n%i==0:
        c.append(i)
m=0
for i in range(len(c)-1):
    m=m+c[i]
if m==n and sum(c)//2==n:
    print("Perfect")
else:
    print("not perfect")