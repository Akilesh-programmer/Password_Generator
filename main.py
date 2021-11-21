# Password Generator Project

# Importing the random module
import random

# Required Data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome statement
print("Welcome to the PyPassword Generator!")

# Getting the inputs
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Creating Random Letters
number_of_times_letter = 0
random_letter = []
for letter in letters:
    number_of_times_letter = number_of_times_letter + 1
    if number_of_times_letter <= nr_letters:
        random_letter1 = random.choice(letters)
        random_letter.append(random_letter1)

# Creating Random Symbols
number_of_times_symbols = 0
random_symbol = []
for symbol in symbols:
    number_of_times_symbols = number_of_times_symbols + 1
    if number_of_times_symbols <= nr_symbols:
        random_symbol1 = random.choice(symbols)
        random_symbol.append(random_symbol1)

# Creating Random Numbers
number_of_times_numbers = 0
random_number = []
for number in numbers:
    number_of_times_numbers = number_of_times_numbers + 1
    if number_of_times_numbers <= nr_numbers:
        random_number1 = random.choice(numbers)
        random_number.append(random_number1)

# Putting letters, symbols and numbers into a same list
password12 = []
password12.extend(random_letter)
password12.extend(random_symbol)
password12.extend(random_number)

# Shuffling the data in the password12
random.shuffle(password12)

# Joining the data in password12
password = ''.join(password12)

# Printing the generated password
print(f"Your password is: {password}")
