from utils import find_max

numbers = [5,41,32,56,7,67,7,534,123]
max = find_max(numbers)
print(max(numbers))


#utils

# def find_max(numbers):
#     max = numbers[0]
#     for number in numbers:
#         if number > max:
#             max = number
#     return max