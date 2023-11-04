n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
b=x+y
a=set(b)
a=list(a)
if 0 in a:
    if len(a)-1==n:
      print("I become the guy.")
    else:
      print("Oh, my keyboard!")
else:
    if len(a)==n:
      print("I become the guy.")
    else:
      print("Oh, my keyboard!")


