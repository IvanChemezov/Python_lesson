import os
os.system("cls")

#       Task #5
#       5.	Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
print('Task #5')
number = int(input('Enter value = '))
if ((number % 5 == 0) or (number % 10 == 0) or (number % 15 == 0)) and (number % 30 != 0):
    print('number is correct')
else:
    print('number is not correct')