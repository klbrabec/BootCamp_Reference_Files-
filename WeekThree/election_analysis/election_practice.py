my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(float(input("What is the total votes in the election? ")))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


#note - this code works - just not in the visual studio code terminal - need to figure out why 
#we saw that it's copying/pasting into the next input string incorrectly which will cause an 
#invalid literal for int() error.  