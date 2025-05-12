from random import*

print('Введите размер массива')
c = int(input())
print('Введите левую границу рандома')
left = int(input())
print('Введите правую границу рандома')
right = int(input())
numbers = []
for i in range(c):
    numbers.append(randint(left, right))
print(numbers)
min = numbers[0]
max = numbers[0]
for i in range(0, len(numbers)):
    if min > numbers[i]:
        min = numbers[i]
    if max < numbers[i]:
        max = numbers[i]
print('Минимальный элемент:', min, 'Максимальный элемент:', max)

count = 0
for i in numbers:
    if i < 0:
        count += 1
print('Кол-во отрицательных элементов:', count)

count = 0
for i in numbers:
    if i > 0:
        count += 1
print('Кол-во положительных элементов:', count)

count = 0
for i in numbers:
    if i == 0:
        count += 1
print('Кол-во нулей:', count)
