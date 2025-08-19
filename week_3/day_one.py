# swap two variables................................................

# a = 'hello'
# b = 'world'
# print(f'{a} {b}')

# a ,b = b, a

# print(f'{a} {b}')

# check a number even or odd......................................

# num = int(input('enter number: '))

# if num % 2 == 0:
#     print(f'{num} is an even number')
# else:
#     print(f'{num} is an odd number')

# simple calculator......................................................

# num1 = int(input('first number: '))
# num2 = int(input('second number: '))

# opr = input('select operator ( + - / * ): ')

# if opr == '+':
#     print(f'{num1} + {num2} = {num1 + num2}')
# elif opr == '-':
#     print(f'{num1} - {num2} = {num1 - num2}')
# elif opr == '/':
#     print(f'{num1} / {num2} = {num1 / num2}')
# elif opr == '*':
#     print(f'{num1} * {num2} = {num1 * num2}')
# else:
#     print('you entered wrong command')   

# fizzbuzz implementation......................................................

# for i in range(1,50):
#     if i % 3 == 0 and i % 5 == 0:
#         print('fizzbuzz')
#     elif i % 3 == 0:
#         print('fizz')
#     elif i % 5 == 0:
#         print('buzz')
#     else:
#         print(i)       

# star pattern.......................................................

# rows = int(input('enter rows: '))

# for i in range(rows,0,-1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))