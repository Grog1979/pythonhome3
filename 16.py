#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input('enter numbers of array elements: '))
list_1 = []
for i in range(n):
  i = int(input('enter number: '))
  list_1.append(i)
print(list_1)
x = int(input('enter number: '))
count = 0
for i in list_1:
  if x == i:
    count += 1
print(count)