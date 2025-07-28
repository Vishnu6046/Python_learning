def calculate_discounted_price(price,tax_percentage,discount_percentage):
    
#this function is used to calculate discounted price

    tax_amount = price * ( tax_percentage / 100 )
    price_withtax = price + tax_amount
    discount_amount = price_withtax * ( discount_percentage / 100 )
    final_price = price_withtax - discount_amount

    return final_price
#...............................................................................

def check_prime_number(num):

#This function checks if a number prime or not

    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number") 
#--------------------------------------------------------------------------------

def calculate_BMI(height,weight):

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight")
    elif bmi < 25:
        print("You have a normal weight")
    elif bmi < 30:
        print("You are overweight")
    else:
        print("You are obese")   
#------------------------------------------------------------------------------------     