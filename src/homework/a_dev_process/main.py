from dev_process import multiply_numbers
sales_tax_rate = 0.0825
tip_percentage = 0.15
subtotal = 100
sales_tax = multiply_numbers(subtotal, sales_tax_rate)
tip = multiply_numbers(subtotal, tip_percentage)
total = subtotal + sales_tax + tip
print(f'Subtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Tip: ${tip:.2f}')
print(f'Total: ${total:.2f}')