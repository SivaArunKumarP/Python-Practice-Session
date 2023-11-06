x=input("enter the string:")
y=x.lower()
vowel=['a','e','i','o','u']
c=0
v=0
n=0
for i in range(0,len(y)):
    if y[i] in vowel:
        v+=1
    elif y[i]>='a' and y[i]<='z':
        c+=1
    else:
        n+=1
print("consonants;",c)
print("vowels:",v)
print("numbers:",n)