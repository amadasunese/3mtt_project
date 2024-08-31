"""Script to convert integer to fload
"""

def integer_to_float(integer_value):
    return float(integer_value)

integer_value = input('Enter any integer value ')
float_value = integer_to_float(integer_value)

print(f"Integer: {integer_value}")
print(f"Float: {float_value}")
