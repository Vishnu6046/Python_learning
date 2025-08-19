# a = [[1,2,3,4,5,6,7,8,9]]

# def to_sum(a):
#     su = 0
#     for i in a:
#         su += i
#     return su

# x = set(map(to_sum,a))

# print(x)

# a = 10
# print(a)
# print(f'{a} is {type(a)}')

# text = " HELLO, python !"
# print(text)
# print(text.strip())
# print(text.lower())
# print(text.upper())
# print(text.replace(' HELLO', 'world'))

# my_dict = {'name':'sooraj','age': 25, 'city':'calicut'}

# print(my_dict['name'])

# my_dict['age'] = 30
# print(my_dict['age'])

# my_dict['country'] = 'india'

# for key,value in my_dict.items():
#     print(f'{key} : {value}')

# a = {1,2,3,4}
# b = {4,5,2,6}

# x = a.intersection(b)
# print(x)

# y = a.union(b)

# print(y)

# a = [1,2,2,3,4,5,5,6]

# sum = 0
# for i in a:
#     if a.count(i) == 1:
#         sum += i

# print(sum)

# a = 10
# b = 5

# c = a < 20 and b <10
# print(c)

# s = "Programming"

# print(s[1:10])

# x = float(input('enter a number : '))

# if x > 0:
#     print(f'{x} is positive number')
# elif x == 0:
#     print('this is zero')
# else:
#     print(f'{x} is a negtive number')

# x = int(input('enter a number : '))

# if x == 0:
#     print('this is zero')
# elif x % 2 == 0:
#     print(f'{x} is a even number ')
# else:
#     print(f'{x} is a odd number')

# name = input('enter name: ')
# age = int(input('enter age: '))

# if age < 13:
#     print(f'{name} is a child')
# elif age < 19:
#     print(f'{name} is a teen')
# elif age < 59:
#     print(f'{name} is a adult')
# elif age < 110:
#     print(f'{name} is a senior')     
# else:
#     print('this is a legend')    

# co = [10, 20, 30, 40, 50]

# for i in co:
#     print(i)

# for i in range(1,11):
#     if i == 6:
#         break
#     print(i)

# for i in range(1,6): 
#     if i == 3:
#         continue
#     print(i)
# import re
# x = 'my id is 123a457'

# # y = re.findall(r'\d+', x)
# # print(y)

# y = re.search(r'\d+', x)

# if y:
#     print(y.group())


# with open("welcome.txt", 'w') as file:
#     file.write('welcome to python')

# with open("welcome.txt", 'r') as files:
#     content = files.read()
#     print(content)


# for i in range(1,6):
#     print(' ' * (5 - i) + '*' * (2 * i - 1))

# import datetime

# x = datetime.datetime.now()
# print(x)

# x = lambda a,b: a + b

# print(x(1,2))

# rows = int(input('enter number of rows:'))

# for i in range(1,rows+1):
#     print('*' * i + ' ' * (rows - i))

# import json

# data = {'name':'soo', 'age': 25, 'place': 'clt'}

# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

# with open('data.json', 'r') as file:
#     x = json.load(file)
# print(x)

# x = 0
# for i in range(1,10):
#     if i % 2 == 0:
#         x += 1
#         print(i)
# print(f'we have {x} even numbers')        

# for i in range(10):
#     if i == 3:
#         break
#     print(i)

