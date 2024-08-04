# Write a Python program to find the second largest number in a list.

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    first = float('-inf')
    second = float('-inf')

    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None


numbers = [5, 5, 5, 5, 5]
numbers = [1, 2, 3, 4, 5, 6]
print("The second largest number in the list is:", find_second_largest(numbers))
