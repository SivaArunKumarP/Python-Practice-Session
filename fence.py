x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=x[0]
w=0
for i in range(c):
    if y[i]>x[1]:
        w+=2
    else:
        w+=1
print(w)