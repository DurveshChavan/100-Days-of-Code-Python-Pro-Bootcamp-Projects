import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print(f"{len(letters)}\n{len(numbers)}\n{len(symbols)}")
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

password_list = []

for i in range (0, nr_letters):
    password_list.append(letters[random.randint(0, len(letters)-1)])

for i in range (0, nr_numbers):
    password_list.append(numbers[random.randint(0, len(numbers)-1)])

for i in range (0, nr_symbols):
    password_list.append(symbols[random.randint(0, len(symbols)-1)])


# print(password_list)

# New syntax random.choice() and random.shuffle()
random.shuffle(password_list)
real_password = ""

for i in password_list:
    real_password += i

print(real_password)

# for i in range(0, len(password_list)):
#     random_number4 = random.randint(0, len(password_list))
#     print(random_number4)
#     password_list[i] = password_list[random_number4]
#
# print(password_list)
