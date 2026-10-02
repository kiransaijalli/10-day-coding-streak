# Day 1: check if a number is Even or Odd

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Test the function
sample_number = 14
print(check_even_odd(sample_number))


