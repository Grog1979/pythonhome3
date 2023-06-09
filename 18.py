#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('enter numbers of array elements: '))
list_1 = []
for i in range(n):
  i = int(input('enter number: '))
  list_1.append(i)
print(list_1)
x = int(input('enter number: '))
minraz = x - list_1[0]
if minraz < 0:
  minraz = - minraz
for i in list_1:
  raz = x - i
  if raz < 0: 
    raz = - raz
  if raz < minraz:
    minraz = raz
for i in range(len(list_1)):
  if x - list_1[i] == minraz or x - list_1[i] == - minraz:
    print('index', i, 'value', list_1[i])