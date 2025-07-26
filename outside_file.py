from my_package import learning_python

#this is to calculate discount using a function in another package.
#this function works because it imported.

price = float(input("Enter price of product: "))
tax_percentage = 18
discount_percentage = float(input("Enter discount percentage: "))

final_price = learning_python.calculate_discounted_price(price,tax_percentage,discount_percentage)
print("Final amount is: ", final_price)

#----------------------------------------------------------------------------

