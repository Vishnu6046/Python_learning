# my_dict = {'puttu':10, 'porotta':20, 'appam':15,'chappathi':12}
# print(my_dict)

# #add to dictionary
# my_dict['idiyappam'] = 25
# print(my_dict)

# #add multiple items to dictionary
# my_dict.update({'dosa':10, 'pathiri':5})
# print(my_dict)

# #remove from dictionary
# del my_dict['appam']
# print(my_dict)

# #update existing keyvalue in dictionary
# my_dict['chappathi'] = 18
# print(my_dict)

# #remove using pop
# my_dict.pop('puttu')
# print(my_dict)

# #remove using popitem
# my_dict.popitem()
# print(my_dict)

# #clear entire dictionary
# my_dict.clear()
# print(my_dict)

# #avoid error while removing non key
# b = my_dict.pop('dosa','not found')
# print(b)
# print(my_dict)

# #to loop through dictionary and print key value pair line by line
# for key, value in my_dict.items():
#     print(f"{key} = {value}")


# --------------------------------------------------------

# my_list = ['apple','orange','mango',10,20,30]
# print(my_list)

# #to add to a list
# my_list.append('grape')
# print(my_list)

# #insert item at a specified index
# my_list.insert(1,'40')
# print(my_list)

# #adding multiple items
# my_list.extend(['kiwi',50])
# print(my_list)

# #removing a specified item
# my_list.remove('orange')
# print(my_list)

# #removing last item
# my_list.pop()
# print(my_list)

# #to find length of a list
# print(len(my_list))

# #to print every items line by line
# for n in my_list:
#     print(n)

# a = [1, 2, 3, 4, 8, 7, 11, 25, 15, 14]
# prime_numbers = []
# non_prime = []

# for i in a:
#     if i > 1:
#         for x in range(2, i):
#             if i % x == 0:
#                 non_prime.append(i)
#                 break
#         else:
#             prime_numbers.append(i)


# print(f'prime numbers = {prime_numbers}')
# print(f'non primes = {non_prime}')

