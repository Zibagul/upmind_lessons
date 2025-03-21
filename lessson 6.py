# # Список (list) - это упорядлченная изменяемая коллекция элементов.
# #
# # Пример списка
# fruits = ['яблоко', 'банан', 'апельсин']
# # print(fruit[0]) #яблоко
# #
# # Списки могут содержать разные типы данных
# mixed_list = [42, 'hello', 3.14, [1,2,3]]
# print(mixed_list[3][2])
#
# # negative indexes
# print(mixed_list[-1])
#
# #editing index
# print(mixed_list)
# print(mixed_list[1])
# mixed_list[1] = 'first lesson'
# mixed_list[2] = 33.11
# print(mixed_list)
#
# print(len(mixed_list)) #длина списков
# concatenated_list = mixed_list + fruits
# print(concatenated_list)
#
# print(fruits * 2)
# print([1] * 10)
#
# print('апельсин' in fruits)
# print('банан' in fruits)
#
# # методы списков
# print(fruits)
# fruits.append('ананас')
# fruits.insert(1,'груша')
# print(fruits)
# fruits.pop()
# ananas = fruits.pop()
# mixed_list.remove(42)
# print(mixed_list)
#
# print(mixed_list.index('first lesson'))
# print(mixed_list.count(33.11))
# mixed_list.append(33.11)
# print(mixed_list.count(33.11))
# print(mixed_list)
#
# numbers = [2,6,1,9,3,4,7]
# print(numbers)
# numbers.sort()
# print(numbers)
# print(sorted(numbers))
#
# print(numbers)
# print(numbers[0:2])

# task 1
# dishes = [ 'манты', 'плов', 'куурдак', 'оромо', 'быжы' ]
# print(dishes[2])

#task2
# numbers = [10, 20, 30, 40, 50]
# numbers[2] = 99
# print(numbers)

#task3
# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3]
# concacenated_list = letters + numbers
# print(concacenated_list)

#task4
# numbers = [4, 2, 9, 1]
# numbers.append(7)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.sort()
# print(numbers)

# # task5
# languages = ['python', 'java', 'c++', 'javascript', 'php']
# print(languages[1],[2],[3])
# print(languages[0:3])
# print(languages.reverse())# fruits.insert(1,'груша')
