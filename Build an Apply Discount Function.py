def apply_discount(price, discount):
    # Check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    # Check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    
    # Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # Check if discount is in the valid range 0-100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    
    # Calculate final price
    return price * (1 - discount / 100)

apply_discount("100", 20)   # "The price should be a number"
apply_discount(100, "20")   # "The discount should be a number"
apply_discount(-5, 20)      # "The price should be greater than 0"
apply_discount(100, -5)     # "The discount should be between 0 and 100."
apply_discount(100, 105)    # "The discount should be between 0 and 100."
apply_discount(100, 20)     # 80
apply_discount(50, 0)       # 50
apply_discount(100, 100)    # 0
apply_discount(74.5, 20.0)  # 59.6
