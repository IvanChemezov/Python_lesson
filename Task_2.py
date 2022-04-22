import os
os.system("cls")


#       Task #2
print('Task #2')
array = [1,20,5,4,0]
array_range = range(len(array))
max = array[0]
for i in array_range:
    print(array[i])
    if array[i] > max:
        max = array[i]
print(max)