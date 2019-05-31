#what we want the program to do
#what variables we need
#how ar we going to do

#WEIGHT TRANSFORMER
weight = int(input("Weight: "))
unit = input("P(Lbs) or K(kg)?: ")
if unit.upper() == "P":
    switch = weight * 0.45
    print(f"you have {switch} kg")
else:
    switch = weight / 0.45
    print(f"you have {switch} pounds")

#GUESSING GAME
guess_count = 0
guess_limit = 3
secret_number = 9
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("YEA MAN, YOU WON")
        break
else:
    print("lost..")

# DECISION GAME
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
- start: start car
- stop: stop car
- quit : exit
           """)
    elif command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == 'stop':
        if not started:
             print("car is already stopped...")
        else:
            started = False
            print("car stopped.")
    elif command == 'quit':
        print('EXIT, bye')
        break
    else:
        print("i don't understand...")

# PRICE CALCULATOR
prices = [10,20,30]
total = 0
for price in prices:
    total += price
print (f"Total: {total}")
0
#FINDING THE BIGGEST NUMBER IN A LIST
numbers = [5,41,32,56,7,67,7,534,123]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#REMOVE DUPLICATES IN A LIST
numbers = [3,1,3,45,5,32,5,6,4,4,3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#UNPACKING
coordinates = (1,2,3)
x, y, z = coordinates
print(y)

#CHANGE NUMBERS IN WORDS [DICTIONARIES]
phone = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

#emoji converter [DICTIONARIES]
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😞"
}
output = ""
print(words)
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#define function
def greet_user():
    print('hi there')
    print('welcome aboard')


print('start')
greet_user()
print('finish')

#define parameter | arguments & function
def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}!")
    print('welcome aboard')


print('start')
greet_user('john','killa')
greet_user('nilu','biddi')
print('finish')

#keyword arguments
def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}!")
    print('welcome aboard')


print('start')
greet_user( 'john', last_name= 'snow')
print('finish')