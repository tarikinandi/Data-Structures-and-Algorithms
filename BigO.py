#BigO Notation -> 0()

#Time Complexity - Space Complexity

def bigoN(n):
    for i in range(0,n):
        print(i)

bigoN(6)
print("*"*150)

def bigoN2(x):
    for z in range(0,x):
        for y in range(0,x):
            print(z,y)

bigoN2(4)
print("*"*150)

def bigoN3(n):
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                print(i,j,k)

bigoN3(3)
print("*"*150)


import math

def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)


logn(42)
print("*"*150)


def nlogn(n):
    lim = n
    while n > 1:
        n = math.floor(n/2)
        for i in range(1,lim):
            print(i)


nlogn(5)
print("*"*150)


def nfactorial(n):
    if n == 0:
        return 1
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1)  #recursive

nfactorial(4)
print("*"*150)

def actualFactorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * actualFactorial(n-1)


print(actualFactorial(4))