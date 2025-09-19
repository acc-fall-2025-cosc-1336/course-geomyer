def multiply_numbers(num1, num2):
    '''Returns the product of two numbers.'''
    return num1 * num2
meal_amount = float(input("Enter the meal amount: "))
tip = float(input("Enter the tip percentage (e.g., 15 for 15%): ")) / 100
sales_tax_rate = 0.0675
sales_tax = multiply_numbers(meal_amount, sales_tax_rate)
tip = multiply_numbers(meal_amount, tip)
total = meal_amount + sales_tax + tip

def get_sales_tax_rate():
    '''Returns the sales tax rate.'''
    return sales_tax_rate

def get_tip_percentage():
    '''Returns the tip percentage.'''
    return tip / meal_amount if meal_amount != 0 else 0     

print("\nReceipt")
print(f"Meal Amount: ${meal_amount:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")