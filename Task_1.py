import os
os.system("cls")

#       Task #1
print('Task #1')
a = int(input('Enter number a - '))
b = int(input('Enter number b - '))
if a**2 == b or b**2 == a:
    print('One number is Pow of another one')
else:
    print('Numbers are not Pow of each others')
