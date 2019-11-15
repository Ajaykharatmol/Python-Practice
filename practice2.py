def prime():
    i = 1
    j = 100
    for x in range(i,j+1):
        if x > 1:
            for k in range(2,x):
                if(x % k)==0:
                    break
            else:
                print(x)

#prime()

def prime1(n):
    c = 0
    for i in range(2,n):
        if (n%i==0):
            c=c+1
            #break
            if (c==0):
                print("is prime",n)
            else:
                print("is not prime", n)

prime1(5)

def days():
    n = input("enter the number : ")
    num = {
    '1' : "Sunday",
    '2' : "Monday",
    '3' : "Tuesday",
    '4' : "Wednesday",
    '5' : "Thursday",
    '6' : "Friday",
    '7' : "Saturday"
    }
    l = len(n)
    for i in range(0,l):
         print(num[n[i]], end=" ")

#days()
