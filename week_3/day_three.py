# Student score tracker using dictionaries..........................................

# students = {}

# while True:
#     print('Score tracker')
#     print('1. add student')
#     print('2. view student')
#     print('3. update score')
#     print('4. delete student')
#     print('5. Exit')

#     choice = input('enter your choice: ')

#     if choice == '1':
#         name = input('enter student name: ')
#         score = int(input('enter score: '))

#         students[name] = score
#         print('student added successfully')

#     elif choice == '2':
#         if students:
#             for name, score in students.items():
#                 print(f'{name} : {score}')
#         else:
#             print('no students found')

#     elif choice == '3':
#         name = input('enter students name to update: ')
#         if name in students:
#             new = int(input('enter new score: '))
#             students[name] = new
#             print('score updated successfully')
#         else:
#             print('student not found')

#     elif choice == '4':
#         name = input('enter student name to delete: ')
#         if name in students:
#             students.pop(name)
#             print('student removed ')
#         else:
#             print('student not found')

#     elif choice == '5':
#         print('exiting....bye')
#         break

#     else:
#         print('invalid input. try again')


# a = [1,2,2,3,3,4,5,5,5,7,8]
# print(a)

# b = list(set(a))
# print(b)


# a = [(1, 'apple', 10), (7,'banana',15), (4,'cherri',5)]

# b = sorted(a, key= lambda x: x[2])
# print(b)


# words = ["apple", "bat", "car", "elephant", "dog", "banana", "ant","mango"]

# sorted_dict = {}

# for word in words:
#     length = len(word)
#     if length not in sorted_dict:
#         sorted_dict[length] = []
#     sorted_dict[length].append(word)

# for ky, vlu in sorted_dict.items():
#     print(f'{ky} = {vlu}')

