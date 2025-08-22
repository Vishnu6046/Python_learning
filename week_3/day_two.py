# to check a number is prime or not...............................................

# def chk_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             print(f'{num} is not a prime')
#             break
#     else:
#         print(f'{num} is prime')
   
# a = int(input('enter number: '))
# chk_prime(a)

# temperature converter...................................................

# def temp_conv(temp, unit):
#     if unit == 'c':
#         f = (9 / 5 * temp) + 32
#         print(f'given temperature = {temp} °C')
#         print(f'fahrenheit temperature is {f} °F')
#     elif unit == 'f':
#         c = ((temp - 32) * 5) / 9
#         print(f'given temperature = {temp} °F')
#         print(f'Celcius temperature is {c} °C')
#     else:
#         print('wrong unit')

# temp = int(input('enter temperature: '))
# unit = input('enter temperature unit: ')

# temp_conv(temp, unit.lower())

# ZeroDivisionError handling.............................................

# try:
#     a = int(input('enter first number: '))
#     b = int(input('enter second number: '))

#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print('dividing by Zero not allowed') 

# custom exception handling..................................................

# def check_age(age):
#     if age < 18:
#         raise ValueError('age must be 18 or above')
#     print('Registration successfull')

# try:
#     check_age(15)   
# except ValueError as a:
#     print(a)
