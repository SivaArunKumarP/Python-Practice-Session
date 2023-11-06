a=list(map(str,input().split()))
a[0],a[(len(a)-1)]=a[(len(a)-1)],a[0]
print(a)