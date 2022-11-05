# Incorporate the random library
from multiprocessing import RLock
import random #you can only import the libraries that you have installed. 

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]
options_dict = {"r":"rock", "p":"paper", "s":"scissors"}

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
# you could set up an options dictionary and pull the key into the print statements
if user_choice != options:
    print("Please enter a valid value")
elif user_choice == "r" and computer_choice == "r":
    print(computer_choice)
    print("Tie")
elif user_choice == "r" and computer_choice == "p":
    print(computer_choice)
    print("Lose")
elif user_choice == "r" and computer_choice == "s":
    print(computer_choice)
    print("Win")
elif user_choice == "p" and computer_choice =="r":
    print(computer_choice)
    print("Win")
elif user_choice == "p" and computer_choice =="p":
    print(computer_choice)
    print("Tie")
elif user_choice == "p" and computer_choice =="s":
    print(computer_choice)
    print("Lose")
elif user_choice == "s" and computer_choice =="r":
    print(computer_choice)
    print("Lose")
elif user_choice == "s" and computer_choice =="p":
    print(computer_choice)
    print("Win")
elif user_choice == "s" and computer_choice =="s":
    print(computer_choice)
    print("Tie")
else:
    print("Try again!")



