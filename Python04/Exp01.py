# Discount Calculation Based on Amount

def calculate_discount(amount):
    if amount <= 5000:
        discount_rate = 5
    elif amount <= 15000:
        discount_rate = 12
    elif amount <= 25000:
        discount_rate = 20
    else:
        discount_rate = 30

    discount = (discount_rate / 100) * amount
    print(f"Amount: {amount}, Discount Rate: {discount_rate}%, Discount: {discount}, Final Amount: {amount - discount}")

# Input
amount = float(input("Enter the amount: "))
calculate_discount(amount)
