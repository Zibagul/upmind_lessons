# - Пустой словарь: my_dict ={}
# - Заполненный словарь:
student = {
    "name": "Алексей",
    2: 33,
    True: [1, 2, 3],
    'status': True,
    'age': 21,
    'city': 'Москва'
}
# Обращение к значениям по ключу:
print(student['name']) #Алексей
print(student.get(333, 'default')) #get для уточнения есть ли ключ
print(student.get('status')) #value значение
#первый аргумент ключ по которому мы хотим забрать значение
#второй аргумент это дефолтное значение в случае отсутствия ключа

# Методы словарей
print(student.keys()) #возвращает все ключи
print(student.values()) # возвращает все значения
print(student.items()) #возвращает все пары(ключ, значение)
student.update({'first key':'first value'}) #добавляем значение
print(student)

print(student.pop('name')) #удаление пары
print(student)

student.clear()
print(student)

#5 Добавление и изменение элемментов:
student['age'] = 22 # Изменение значения
student['grade'] = 'A' # Добавление новой пары
print(student)
str2 = 'Helloo World'

#6 Удаление элементов:
# student.pop('city') # Удаляет пару с ключом 'city'
# del student['name'] # Удаляет ключ 'name'

# 7 Проверка наличия ключа:
if "name" in student:
    print('Ключ 'name' есть в словаре!')