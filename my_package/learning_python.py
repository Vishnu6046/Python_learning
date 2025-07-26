def calculate_discounted_price(price,tax_percentage,discount_percentage):
    tax_amount = price * ( tax_percentage / 100 )
    price_withtax = price + tax_amount
    discount_amount = price_withtax * ( discount_percentage / 100 )
    final_price = price_withtax - discount_amount

    return final_price
