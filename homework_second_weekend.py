### 40 задач по темам: типы данных (int, float, str, bool), списки, условные конструкции, тернарные операторы, методы списков и строк (без использования циклов)

# 1. Создай список из 5 различных чисел и найди сумму первого и последнего элемента.
# num3 = [1234, 567, 789, 1234, 5678]
# print(num3[0] + num3[4])
#
# num1 = [1234, 567, 789, 1234, 5678]
# num2 = [3456, 789, 123, 456, 7890]
# print(num1[1] + num2[4])

# 2. Напиши программу, которая проверяет, делится ли введённое пользователем число на 3 и на 5 одновременно.
# num = int(input())
# if num//3 == int and num//5 == int:
#     print('true')
# else num == float :
# print('false').

# 3. Дан список чисел `[5, 10, 15, 20, 25]`. Проверь, есть ли в нём число 20.
# num = [5, 10, 15, 20, 25]
# print(num.index(20))

# 4. Создай строку и проверь, начинается ли она с заглавной буквы. Если нет, сделай первую букву заглавной.
# text = 'Zibagul'
# if text[0].isupper():
#     print(" начинается с заглавной:", text)
# else: text = text.upper()
# print(" исправленно на заглавную:", text)

# 5. Напиши программу, которая принимает строку от пользователя и выводит её задом наперёд, используя срезы.
# text = str(input())
# print(text[::-1])

# 6. Создай список из 4 вещественных чисел. Найди их сумму и произведение (через умножение элементов вручную).

# 7. Даны три числа. Найди максимальное из них, используя только условные операторы.
# num1 = [234, 343, 768]
# if num1[0] > num1[1] > num1[2]:
    # print(num1[1])
# elif num1[1] > num1[0] > num1[2]:
    # print(num1[2])
# elif num1[2] > num1[1] > num1[0]:
    # print(num1[2])

# 8. Напиши программу, которая принимает строку и проверяет, является ли она числом (целым или вещественным).

# 9. Создай список из имён `['Анна', 'Борис', 'Алексей', 'Вика']`. Проверь, есть ли в нём имя "Алексей". Если есть, выведи "Алексей найден".
# names = ['Анна', 'Борис', 'Алексей', 'Вика']
# if 'Алексей' in names:
#     print('да есть')
# else:
#     print('нет')

# 10. Напиши программу, которая принимает строку и проверяет, содержит ли она хотя бы один пробел.
# str1 = 'что то с пробелом'
# if ' ' in str1:
    # print('есть пробел')
# else:
    # print('нет пробела')

# 11. Создай список из 5 логических значений `[True, False, True, False, True]`. Подсчитай количество значений True, используя метод `.count()`.

# 12. Напиши программу, которая принимает строку и заменяет все пробелы на тире ("-") с помощью метода `.replace()`.

# 13. Создай список из 5 чисел и найди их среднее арифметическое.
# num = [34, 45, 67, 89,45]
# num1 = num[1] + num[2] + num [3] + num[4] + num[0]
# print(num1//5)

# 14. Дана строка. Если её длина больше 10 символов, обрежь её до 10 символов и добавь "...".
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 20, 34, 4535, 59]
# nums = nums[0:9]
# print(nums[0:9])
# nums.insert(10, '...')
# print(nums)



# 15. Напиши программу, которая принимает строку и проверяет, содержит ли она хотя бы одну цифру.
# str1 = (input('напишите что хотите:'))
# if int in '<string>':.
#     print('есть цифра')
# else:
    # print('нет цифры')

# 16. Дан список чисел `[1, -2, 3, -4, 5]`. Замени отрицательные числа на их абсолютные значения с помощью `abs()`.

# 17. Создай список из 5 строк `['a', 'b', 'c', 'd', 'e']`. Соедини их в одну строку через запятую.
# string = ['a', 'b', 'c', 'd', 'e']
# string1 = ['a', 'b', 'c', 'd', 'e']
# string2 = ['a', 'b', 'c', 'd', 'e']
# string3 = ['a', 'b', 'c', 'd', 'e']
# string4 = ['a', 'b', 'c', 'd', 'e']
# string5 = ['a', 'b', 'c', 'd', 'e']
# print(', '.join(string1))
# result = f"{string}, {string1}, {string2}, {string3}, {string4}, {string5}"
# print(result)

# 18. Напиши программу, которая проверяет, является ли введённое пользователем число чётным или нечётным.
# num = int(input())
# if num % 2 == 0:
    # print('четное')
# else:
    # print('нечетное')

# 19. Создай строку, которая является адресом электронной почты. Проверь, есть ли в ней символ "@".

# 20. Дана строка. Если она полностью состоит из заглавных букв, выведи "Заглавная строка".

# 21. Напиши программу, которая принимает строку и заменяет все строчные буквы на заглавные и наоборот, используя `.swapcase()`.

# 22. Дан список чисел `[5, -3, 7, -1, 0]`. Найди максимальное и минимальное число без использования `max()` и `min()` (через условные операторы).
# int1 = [5, -3, 7, -1, 0]
# int1.sort()
# print(int1)
# max = int1[4]
# min = int[0]

# 23. Напиши программу, которая принимает два числа и выводит большее из них (с использованием тернарного оператора).
# num1 = input('введите первое число:')
# num2 = input('введите второе число:')
# if num1>= num2:
    # print(num1)
# else:
    # print(num2)

# 24. Дана строка `"Python Programming"`. Удали пробелы с начала и конца строки.
# str1 = "  Python Programming   "
# str1 = str1.strip()
# print(str1)

# 25. Проверь, пустая ли строка, введённая пользователем.

# 26. Создай список строк и проверь, есть ли в нём пустая строка (`""`), используя оператор `in`.

# 27. Даны числа a и b. Если их сумма больше 100, выведи "Сумма больше 100", иначе "Сумма меньше или равна 100".

# 28. Напиши программу, которая принимает строку и заменяет все гласные буквы на символ "*".

# 29. Создай список из 5 целых чисел. Если сумма всех чисел больше 50, выведи "Большая сумма".

# 30. Даны числа x и y. Если их произведение больше 100, выведи произведение, иначе их сумму.

# 31. Напиши программу, которая принимает строку и удаляет из неё все знаки препинания (например, ".", ",", "!", "?") с помощью `.replace()`.

# 32. Даны три строки. Проверь, если хотя бы одна строка пуста, выведи "Есть пустая строка".

# 33. Напиши программу, которая проверяет, является ли введённое пользователем число положительным, отрицательным или нулём.

# 34. Дана строка. Если она начинается с буквы "А", выведи "Начинается на А".

# 35. Даны три числа. Если их произведение больше 1000, выведи произведение, иначе — их сумму.

# 36. Напиши программу, которая проверяет, является ли введённая строка целым числом с помощью метода `.isdigit()`.

# 37. Даны три строки. Если хотя бы одна из них начинается с заглавной буквы, выведи "Есть заглавная".

# 38. Создай строку и замени все строчные буквы на заглавные с помощью `.upper()`.

# 39. Напиши программу, которая принимает строку и проверяет, является ли она палиндромом (одинаково читается слева направо и справа налево) с использованием среза.

# 40. Дана строка. Если её длина нечётная, выведи средний символ, если чётная — два средних символа.
