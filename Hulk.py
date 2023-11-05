n=int(input())
m=""
for i in range(n):
    if i%2==0:
        m=m+"I hate "
    else:
        m=m+"I love "
    if i!=n-1:
        m+="that "
    else:
        m+="it"
print(m)
