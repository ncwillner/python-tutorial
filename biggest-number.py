#FINDING THE BIGGEST NUMBER IN A LIST
numbers = [5,41,32,56,7,67,7,534,123]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
