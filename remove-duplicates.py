#REMOVE DUPLICATES IN A LIST
numbers = [3,1,3,45,5,32,5,6,4,4,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)