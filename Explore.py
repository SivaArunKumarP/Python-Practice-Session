x=int(input("enter number 1 = "))
y=int(input("enter number 2 = "))
if x>y:
    greater=x
else:
    greater=y
while True:
    if greater%x==0 and greater%y==0:
        lcm=greater
        break
    greater+=1
while y:
    x,y=y,x%y
    k=x
    print(k)
while True:
    ch=int(input("enter your choice- 1.GCD 2.LCM 3.exit1"))
    if ch==1:
        print(x)
    elif ch==2:
        print(lcm)
    else:
        break

