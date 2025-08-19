# pairs = [('a', 1), ('b', 2), ('c', 3)]
# result = dict(pairs)
# print(result)

# a = [[1, 2], [3, 4]]
# b = []

# for sublist in a:
#     for item in sublist:
#         b.append(item)

# print(b)

# a = [1,2,3,4,8,7,11,20,15,14]

# odd = []
# even = []

# for i in a:
#     if i % 2 != 0:
#         odd.append(i)
#     else:
#         even.append(i)
# print(odd)
# print(even)            

#-------------------------------------------------------------------
# cities = ('kozhikode','wayand','malapprm','ernklm','alppy')

# # c1,c2,c3,c4,c5 = cities

# a = input('enter city:' )

# if a in cities:
#     print(f'{a} is in the tuple')
# else:
#     print(f'{a} is not in the tuple')    

# wrksp_1 = {'symen','sooraj','dude','sayed','rajan'}
# wrksp_2 = {'agraj','anshi','dude','sree','rajan'}

# n = wrksp_1 & wrksp_2
# print(n)
# o = wrksp_1 ^ wrksp_2
# print(o)

# wrksp_1.add('ashik')
# print(wrksp_1)
# wrksp_2.add('jishnu')
# print(wrksp_2)
#-----------------------------------------------------------------

# c = lambda a,b: a + b
# a = 5
# b = 4
# print(c(a,b))

# a = [1,2,3,4]

# def square(x):
#     sq = x ** 2
#     return sq

# b = map(square,a)

# print(list(b))
#-----------------------------------------------------------------------

# class bankaccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposite(self,amount):
#         self.balance += amount
#         print(f'{amount} deposited successfully') 

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'{amount} withdrawed successfully')    
#         else:
#             print('insufficient balance')     
        
#     def display_balance(self):
#         print(f'{self.account_holder}, your balance is {self.balance}')  

# ac1 = bankaccount('sooraj', 10000) 
# ac2 = bankaccount('vishnu',1000)

# ac1.deposite(int(input('enter deposite amount: ')))
# ac1.withdraw(3000)
# ac1.display_balance()
#----------------------------------------------------------------------------------

# class personskill:
#     def __init__(self):
#         self.skills = set()

#     def add_skill(self,skill_name):
#         if skill_name in self.skills:
#             print(f'{skill_name} already added')
#         else:
#             self.skills.add(skill_name)
#             print(f'added {skill_name}')

#     def show_skills(self):
#         if self.skills:
#             print('your skills are :')
#             for i in self.skills:
#                 print(i)
#         else:
#             print('No skills added yet')        

#     def remove_skill(self,skill_name):
#         if skill_name in self.skills:
#             self.skills.remove(skill_name)
#             print(f'{skill_name} removed')
#         else:
#             print(f'{skill_name} not found')    


# p1 = personskill()

# p1.show_skills()
# p1.add_skill('python')
# p1.add_skill('html')
# p1.add_skill('css')
# p1.add_skill('c lang')
# p1.show_skills()
# p1.remove_skill('python')
# p1.remove_skill('java')
# p1.show_skills()

# choices = ('r','p','s')

# while True:
#     choice_1 = input('enter choice one: ')
#     choice_2 = input('enter choice two: ')
#     if choice_1 not in choices:
#         print(f'{choice_1} is invalid choice')
#         continue
#     elif choice_2 not in choices:
#         print(f'{choice_2} is invalid choice')
#         continue   

#     if choice_1 == choice_2:
#         print('Tie')
#     elif (choice_1 == 'r' and choice_2 == 's') or (choice_1 == 'p' and choice_2 == 'r') or (choice_1 == 's' and choice_2 == 'p'):
#         print(f'{choice_1} wins')
#     elif (choice_2 == 'r' and choice_1 == 's') or (choice_2 == 'p' and choice_1 == 'r') or (choice_2 == 's' and choice_1 == 'p'):
#         print(f'{choice_2} wins')   
#     break        
           