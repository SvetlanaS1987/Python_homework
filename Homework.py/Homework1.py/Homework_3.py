""" 12 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """

""" my_list = [2, 3, 5, 9, 3]
print(sum(my_list[1::2])) """


""" Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] """

""" my_list = [int(input("Введи элемент списка : ")) for _ in range(int(input("Введи количество элементов списка: ")))]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list) """



""" Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 """

""" Округляет до десятичных((( """

""" my_list = [float(input("Введи элемент списка : ")) for _ in range(int(input("Введи количество элементов списка: ")))]
min = 1
max = 0
for i in my_list:
     if (i - int(i)) <= min:
         min = i - int(i)
     if (i - int(i)) >= max:
         max = i - int(i)  
print(round((max-min), 2)) """

""" Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10 """

""" a = int(input("Введи число : "))
dvoich = ""
while a > 0:
     dvoich = str(a%2) + dvoich
     a//=2
print(dvoich) """ 

""" Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
[Негафибоначчи] """

""" g = int(input("Введите к: "))  
list_f = [0]*(g*2+1) 
print(list_f) 
list_f[g] = 0 
list_f[g+1] = 1  
for i in range(g+2, len(list_f)):
          list_f[i] = list_f[i-2]+list_f[i-1]  
          for i in range(g, -1, -1):     
             list_f[i] = list_f[i+2]-list_f[i+1]

print(list_f) """