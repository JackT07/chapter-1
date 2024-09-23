# task 2 to 6
# author: jack
# Task 2
Fname = (input("please enter your first name: "))
Sname = (input("please enter your Last name: "))
print(Fname)
print(Sname)
print("\n")
# Task 3
hour = int(input("enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
print(hour*60*60)
print(minutes*60)
print(seconds)
print("\n")
# Task 4
five_digit = int(input("Please enter your five digit number in the form of second "))
print(five_digit //60)
print("\n")
# Task 5
characters1 = input("enter a character from the key board:")
characters2 = input("enter a character from the key board:")
characters3 = input("enter a character from the key board:")
characters4 = input("enter a character from the key board:")
characters5 = input("enter a character from the key board:")
print("\n")
print(str((ord(characters1))))
print(str((ord(characters2))))
print(str((ord(characters3))))
print(str((ord(characters4))))
print(str((ord(characters5))))

# Task 6
units = int(input("total number of units used: "))
cost_per_unit = float(input("cost per unit: "))
standing_charge = float(input("enter the standing charge: "))
print(units * cost_per_unit + standing_charge)

# Task 7
fish = float(("4.50"))
chips = float(("2.80"))
order1 = int(input("How many orders of fish do you want: "))
order2 = int(input("How many orders of chips do you want: "))
total = (order1*fish)
total1 = (order2*chips)
print(total+total1)
vat = float(("0.09"))
print(total+total1 + vat)

# Task 8
word = input("Enter a five letter word in lower case: ")
key = int("5")
ascii = ord(word)
encrypted_word = chr(ascii + key)
print("The encrypted word: ",encrypted_word)
