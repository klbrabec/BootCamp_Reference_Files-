# Documentation should be reviewed as posted - that's where
# we learn things - use it where appropriate
# make sure you are not re-using variables that have been used previously
# can be confusing if used in multiple places and are passing things in
# and out of loops. 
# Integers are not iterable (why?)
# Learning on how to interpret errors (and handle them) is important! 

# Loop through a range of numbers (0 through 4)
for x in range(5):#(Will start at 0 and increment by 1 (0,1,2,3,4)
    print(x)

print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 7):# start number and end of range ex 100 1-101
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
word = "Peace"
for letters in word:
    print(letters)

print("----------------------------------------")

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)
    for character in animal: #nested for loops 
        print(character)

print("----------------------------------------")

# Loop while a condition is being met
run = "y" #you can get caught in infinite while loops 

while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y'") #(input is what the user enters on the keyboard)
    
