from my_package import learning_python

#this is to calculate discount using a function in another package.
#this function works because it imported.

# price = float(input("Enter price of product: "))
# tax_percentage = 18
# discount_percentage = float(input("Enter discount percentage: "))

# final_price = learning_python.calculate_discounted_price(price,tax_percentage,discount_percentage)
# print("Final amount is: ", final_price)
# #-------------------------------------------------------------------------------

#finding a number is prime or not using a function
# num = int(input("Enter a number: "))

# learning_python.check_prime_number(num)
# ---------------------------------------------------------------------------------         

#finding BMI
# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kilograms: "))

# learning_python.calculate_BMI(height,weight)       
#----------------------------------------------------------------------------------

# assignment_score = float(input("Enter score of assignment(out of 100) = "))
# test_score = float(input("Enter score of test(out of 100) = "))

# assignment_weight = 0.4
# test_weight = 0.6

# weighted_average = (assignment_score * assignment_weight) + (test_score * test_weight)

# if weighted_average > 90:
#     letter_grade = "A"
# elif weighted_average > 80:
#     letter_grade = "B"
# elif weighted_average > 70:
#     letter_grade = "C"
# elif weighted_average > 60:
#     letter_grade = "D"
# elif weighted_average > 50:
#     letter_grade = "E"
# else:
#     letter_grade = "F"

# print("Your final grade is {} and letter grade is {}" .format(weighted_average,letter_grade)) 
#----------------------------------------------------------------------------------------------------

# #a portal to search food items using list

# foods = [ ["biriyani","thalassery","favorite for most people"],
#          ["mandhi","alfahm-mandhi","choosen by all the youths"],
#          ["porotta and beef","kozhikoden","emotion for everyone"]]

# print("Welcome to the official foods page")

# #first display options
# while True:
#     print("Enter 1 to check food items")
#     print("Enter 2 to add new food items")
#     print("Enter 3 to exit")
#     choise = input("Enter your choise:")

# #when option selected
#     if choise == "1":
#         food_name = input("enter a food item:")
#         found = False
#         for food in foods:
#             if food[0] == food_name:
#                 print(f"Details of {food[0]}")
#                 print(f"most famous {food[0]} is {food[1]}")
#                 print(food[2])
#                 found = True
#                 break
#         if not found:
#             print("food not found in list")

#     elif choise == "2":
#         new_food = []
#         new_food.append(input("Enter the name of food:"))
#         new_food.append(input("Enter the most famous:"))
#         new_food.append(input("Enter a quote for it:"))
#         foods.append(new_food)
#         print("New details added successfully")

#     elif choise == "3":
#         print("goodbye!!")
#         break

#     else:
#         print("Invalid choise, choose 1,2 or 3")    
# --------------------------------------------------------------------------------------    

# celsius_temps = [22, 25, 30, 18, 20]
# print(celsius_temps)
# fahrenheit_temps = [(temp * 9/5) + 32 for temp in celsius_temps]
# print(fahrenheit_temps)
#--------------------------------------------------------------------------------------------

# for i in range(1,11):
#     a = i * 5
#     print("{} * 5 = {}".format(i,a))
#---------------------------------------------------------------------------------------------