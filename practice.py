def fact(n):
    f=1
    for i in range (1,n+1):
        f=i*f
        print("Factorial is",f)

def pallindrome():
    string = input("Enter the string: ")
    rev_string = string[::-1]
    if (string == rev_string):
        print("String is a pallindrome")
    else:
        print("String is not a pallindrome")

def pallindromeNO():
    Number = input("Enter the number : ")
    Rev_Number = Number[::-1]
    print (Rev_Number)
    if (Number == Rev_Number):
        print("Number is a Pallindrome")
    else:
        print("Number is not a Pallindrome")
    
def swap(a,b):
    a,b = b,a
    print("After swapping a=",a)
    print("After swapping b=",b)

def evenodd(n):
    if (n%2==0):
        print("is even")
    else:
        print("is odd")

def even():
    for i in range(0,100,2):
        print(i)

def odd():
    for i in range(1,100,2):
        print(i)

def p(n):
    for i in range(0,n+1):
        for j in range(0,i+1):
            print("*",end=" ")
        print()

def p1(n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(end=" ")
        for j in range(0,i+1):
            print("*",end=" ")
        print()

p1(5)

