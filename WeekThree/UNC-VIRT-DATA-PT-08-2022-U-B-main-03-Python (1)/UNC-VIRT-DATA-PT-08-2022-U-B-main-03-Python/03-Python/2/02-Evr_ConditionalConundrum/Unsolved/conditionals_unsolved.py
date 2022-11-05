# 1. Would print OOOO needs some work because 5*2 is not greater than 10 it's equal to. 
# this would need to have an OR statement to trigger number 1 
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")


# 2. len() tells us how many characters are in the string passed in (ex "dog")  This would
#print out Question 2 works because 3 is less than 5 
x = 5
y = 10
if len("Dog") < x:
    print("Question 2 works!")
else:
    print("Still missing out")

# 3. ** takes X to the power of 3 and Y to the power of 2 
# there are other math operators (Mindie will be sharing a list of them)
# both parts of these conditions will need to be true. 
# this would return the IF statement commant. 
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")

# 4. Does name exist in any of these lists?   This will show "Dan is in group three"
# conditions that can be checked when working with a list. 
# you can also check where the indexes for a list or a value associated with an index. 
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
elif name in group_three:
    print(name + " is in group three")
else:
    print(name + " does not have a group")


# 5. 
height = 66
age = 16
adult_permission = False

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)): 
    #watch this one because it is very complex.  
    print("Can ride bumper cars")
else:
    print("Stick to lazy river")
