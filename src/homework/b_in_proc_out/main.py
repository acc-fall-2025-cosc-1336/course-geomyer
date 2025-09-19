
from output import multiply_numbers, get_sales_tax_rate, get_tip_percentage
meal_amount = float(input("Enter the meal amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))


sales_tax_rate = get_sales_tax_rate()
sales_tax = multiply_numbers(meal_amount, sales_tax_rate)   

tip_amount = get_tip_percentage() * meal_amount
tip = multiply_numbers(meal_amount, tip_percentage / 100)
total = meal_amount + sales_tax + tip

print("\nReceipt")
print(f"Meal Amount: ${meal_amount:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
# The above code imports functions from output.py to calculate sales tax and tip.

     
    

from output import multiply_numbers

def main():
    result1 = multiply_numbers(5, 5)
    result2 = multiply_numbers(7, 7)
    print(f"Product of 5 and 5 is: {result1}")
    print(f"Product of 7 and 7 is: {result2}")  



       


