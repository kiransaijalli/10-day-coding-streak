# Day 4: Find the Largest Element in an Array
numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest element:", largest)