"""
Script that calculate basic statistics
"""

numbers = [10, 20, 30, 40, 50]

def calculate(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return total_sum, average, minimum, maximum

total_sum, average, minimum, maximum = calculate(numbers)

print(f"Sum = {total_sum}")
print(f"Average = {average}")
print(f"Min = {minimum}")
print(f"Max = {maximum}")

