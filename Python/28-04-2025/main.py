#Задание 1

a = int(input('num1: '))
b = int(input('num2: '))
if a >= b: a,b = b,a
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)

#Задание 2

a = int(input('num1: '))
b = int(input('num2: '))
count = 0
if a >= b: a,b = b,a
for i in range(a, b+1):
    print(i)
print('_______________________')
for i in range(b, a-1, -1):
    print(i)
print('_______________________')
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)
print('_______________________')
for i in range(a, b+1):
    if i % 5 == 0:
        count+=1
print(count)

#Задание 3

a = int(input('num1: '))
b = int(input('num2: '))
if a >= b: a,b = b,a
for i in range(a, b+1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)