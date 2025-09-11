#Create four variables to use in the function for bill calculation

num1 = 'Subtotal:'
num2 = 'Sales Tax: '
num3 = 'Tip Percentage: '
num4 = 'Total: '

def multiply_numbers(num1, num2):
    '''Returns the product of two numbers.'''
    return num1 * num2

result1 = multiply_numbers(100, 1)  # Subtotal
result2 = multiply_numbers(100, 0.0825)  # Sales Tax
result3 = multiply_numbers(100, 0.15)  # Tip Percentage
result4 = multiply_numbers(100, 1.22)  # Total (example)
print(num1, result1)
print(num2, result2)
print(num3, result3)
print(num4, result4)