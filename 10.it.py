# Python, 3.10
                                      #10

#demo

"""1) Запишите по синтаксису любого языка программирования следующее логическое
высказывание: «Число X не принадлежит ни одному из отрезков [-2, 9] и [5, 87]». Укажите
используемый язык программирования.
2) Вводится последовательность натуральных чисел, не превосходящих 1000. Ноль –
признак конца. Выведите два самых больших числа. Напишите программу на любом
языке программирования. Укажите используемый язык программирования.
3) Вводится последовательность символов. Точка – признак конца. Подсчитайте, сколько
малых латинских букв каждого вида входит в данную последовательность. Структуры
данных, размер которых зависит от длины входной последовательности, не использовать.
Напишите программу на любом языке программирования. Укажите используемый язык
программирования.
4) Напишите функцию, которая циклически сдвигает массив на k позиций влево. Укажите
используемый язык программирования. Эффективность алгоритма также учитывается при
оценке решения.
5) Дана следующая рекурсивная функция.
void call(int k);
{
 if (k > 1)
 {
 сall(k - 1);
 call(k - 2);
 cout << k;
 }
};
Что будет на экране, если обратиться к данной функции с помощью оператора call(5)?"""
# Python, 3.10
# 1)    x < - 2 and x > 87

# 2)
n = int(input())
MAX = 0
preMAX = 0
while n != 0:
    if preMAX < n > MAX:
        preMAX = MAX
        MAX = n
    n = int(input())
print(MAX)
print(preMAX)

# 3)
a = input()
A = [0]*26  # i-ый элемент соответствует i-ой буквы латинского алфавита
while a != '.':
    if 97 <= ord(a) <= 122:  # в ASC-II символа "a" - 97, "z" - 122
        i = ord(a) - 97
        A[i] += 1
    a = input()
for i in range(26):
    print(chr(i + 97), ':', A[i], sep='')


# 4)


def list_shift(A, k):
    if k < 0:
        return A[k:] + A[:k]
    else:
        return A[len(A) - k:] + A[:len(A) - k]


array = [0, 1, 2, 3, 4, 5]
n = int(input())
print(list_shift(array, n))

       #10_it:

#3)
"""3. (4) Программа. На вход программе подаётся последовательность целых чисел. Признак конца ввода —
ноль. Напишите программу, которая находит максимальное число, которое делится на 7 и минимальная
цифра которого равна 3 (число не содержит 1, 2 и 0). Числа по модулю не превосходят 10000. Массивы
и строки не использовать. Укажите используемый язык программирования."""
"""
35
63
336
343
357
364
378
385
399
434
483"""
n = int(input())
MAX = - 10001
while n != 0:
  var = n
  boo = False
  MIN = 9
  while n >= 1:
    tmp = n % 10
    if tmp < MIN:
      MIN = tmp
    n //= 10
  if MIN == 3:
    boo = True
  if boo and not(var % 7) and var > MAX:
    MAX = var
  n = int(input())
print(MAX)
#4)
"""4. (4) Программа. Дана последовательность натуральных чисел, не превосходящих 30000.
Ноль — признак конца. Требуется подсчитать в ней количество пар чисел, произведение которых
делится на 65. Под парой подразумеваются два любых элемента последовательности (не обязаны стоять рядом).
Напишите как можно более эффективную по времени и по используемой памяти программу для решения данной задачи.
Неэффективная, но работающая корректно программа оценивается на частичный балл.
Укажите используемый язык программирования."""

s = input()
A = [int(s) for s in s.split()]
k65 = 0
k5 = 0
k13 = 0
k = 0
for i in range(len(A)):
    if A[i] % 65 == 0:
        k65 += 1
    elif A[i] % 13 == 0:
        k13 += 1
    elif A[i] % 5 == 0:
        k5 += 1
    else:
        k += 1
print((k65 * k) + (k65 * k13) + (k65 * k5) + (k65 * k65) + (k5 * k13) - 1)
#27 (5): ...