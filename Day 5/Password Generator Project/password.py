import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+',]


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? : "))
nr_symbols = int(input(f"How many symbols would you like? : "))
nr_numbers = int(input(f"How many numbers would you like? : "))

ran_letters=random.choices(letters,k=nr_letters)
ran_symbol=random.choices(symbols,k=nr_symbols)
ran_numbers=random.choices(numbers,k=nr_numbers)

total_character=nr_symbols+nr_numbers+nr_letters
password_list=[]
for i in ran_letters:
    password_list.append(i)
for i in ran_symbol:
    password_list.append(i)
for i in ran_numbers:
    password_list.append(i)

random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print(f"\nYour {total_character} Character password is :"+password)