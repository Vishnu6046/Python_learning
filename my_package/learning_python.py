def calculate_discounted_price(price,tax_percentage,discount_percentage):
    """
    this function is used to calculate discounted price

    Args:
        price (int or float): actual price without tax
        tax_percentage (int or float): GST or taxes to include
        discount_percentage (int or float): total discount

    Returns:
        int or float: final price including tax
    """
 
    tax_amount = price * ( tax_percentage / 100 )
    price_withtax = price + tax_amount
    discount_amount = price_withtax * ( discount_percentage / 100 )
    final_price = price_withtax - discount_amount

    return final_price
#...............................................................................

