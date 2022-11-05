x = 1
y = 10


# a lot of data is stored as nested dictionaries. 
# It's important to understand how to navigate through them.
# reference notes from last class.  
# Bracket notation and indexing is helpful here. 

# Checks if one value is equal to another
if x == 1:#<---this ends the condition 
    print("x is equal to 1") #<---this runs ONLY if the condition above is True.  
                            #  The index here is VERY important.  
                            #  Without the tab, it will run the next line of code, 
                            #  true or not. 
                            #  == something is equal (converts to the same type 
                            #  before doing the comparison)
                            #  = assignment 
                            #  === is the same AND the same type. 
                            #  (does not do any conversion before doing the comparison)
# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")
    
# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")
    #both conditions need to be true to return true. 
# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")
    #only one of these conditions need to be true to return true. 
# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
        #any type of code can be included in conditional evaluations - we're just
        #using print for examples. 