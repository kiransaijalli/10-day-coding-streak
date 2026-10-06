 # Day 5: check if an array is sorted in ascending order or not
numbers = [1, 3, 5, 7, 9, 11]

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted.")