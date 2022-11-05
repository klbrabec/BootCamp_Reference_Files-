# * Using a while loop, ask the user "How many numbers?", then print out a chain of ascending numbers, starting at 0.

# * After the results have printed ask the user if they would like to continue.

#   * If "y", restart the process, starting at 0 again.

#   * If "n", exit the chain.

# ## Bonus

# * Rather than just displaying numbers constantly starting at 0, have the numbers begin at the end of the previous chain.

# # Initial variable to track game play
user_play = "y"

# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    number = input("How many numbers would you like to use?")

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(int(number)):
            # Print each number in the range
       print(x + 1) # this is how you could do this to show the name
       

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")