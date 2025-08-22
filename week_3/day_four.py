# with open ('test.txt','w') as file:
#     file.write('hello world')

# with open('test.txt', 'r') as file:
#     x = file.read()
#     print(x)    

# with open('test.txt', 'a') as file:
#     file.write('\n this for testing')



# odd = [x for x in range(1,21) if x % 2 != 0]
# print(odd)

# sqr = {x: x**2 for x in range(1,11) if x % 2 == 0}
# print(sqr) 

# words = ['apple', 'cat', 'elephant', 'orange']

# a = {w : len(w) for w in words}
# print(a)

# j = int(input('enter number: '))
# multi_table = {f'{i} * {j}' : i * j for i in range(1,11)}

# for key, value in multi_table.items():
#     print(f'{key} = {value}')

# num = [[1,2],[3,4],[5,6]]

# single_list = [a for row in num for a in row]
# print(single_list)

# with open('test.txt', 'r') as file:
#     my_file = file.read()

# my_list = my_file.lower().split()

# freq_dict = {word : my_list.count(word) for word in set(my_list) }
# print(freq_dict)

# name = input('Enter user name: ')
# password = input('Enter password: ')

# with open('user.txt', 'a') as user_data:
#     user_data.write(f'User name : {name} \n')
#     user_data.write(f'Password : {password} \n')


# primes = [x for x in range(100) if all(x % i != 0 for i in range(2, x)) ]

# print(primes)

