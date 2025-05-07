numbers = [12, -50, 0, 5, -8, 94, 0, 27, -3, 9, 20, 45, 324, 23, 0, -52, -93, 23, 10, 67, -238]

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
