from random import randint

random_num = int(input('Введите число: '))

random_list = [randint(0, 9) for i in range(random_num)]
print(random_list)

print(f'Количество нулей в списке: {random_list.count(0)}')
