n=int(input("Enter the number to be checked:"))
m=n
rev=""
while n:
    rev= rev + str(n%10)
    n=n//10
rev=int(rev)
if rev == m:
    print("Give number is palindrome.")
else:
    print("It is not a palindrome")