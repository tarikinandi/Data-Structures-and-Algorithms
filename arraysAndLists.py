#Şist
myList= [1 , 2 , 3 , 4 , 5]

myList.append(53)

#Array

import array as arr

myArray = arr.array("i" , [2 , 3 , 5 , 8 , 97])

print(myList)
print(myArray)

otherList = [32 , 59 , 243]

myList.extend(otherList)

print(f"New myList : {myList}")


import sys

n=30

myDynamicArray = []

for i in range(n):
    myLenght = len(myDynamicArray)
    myByte = sys.getsizeof(myDynamicArray)
    print(f"Lenght : {myLenght} , Byte : {myByte}")
    myDynamicArray.append(i)