# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Returns the index of the first object with a matching value
# Python is a zero indexed list.  (The first index is 0)
print(myList.index("Matt"))

# Changes a specified element within an List at the given index
# This uses the numeric index of the item we want to update/change.
# this will overwrite the item that is identified. 
# this change happens immediately - and there is no roll back 
# can cast to a new variable and update the new variable to prevent data loss. 
myList[3] = 85
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Matt") #this will remove the value Matt. It will only remove the one it finds
print(myList)

# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False) #not used often in python - used more in file storage, etc. 
#these are immutable values - cannot be changed. Do not have to have just one data type 
print(myTuple)
