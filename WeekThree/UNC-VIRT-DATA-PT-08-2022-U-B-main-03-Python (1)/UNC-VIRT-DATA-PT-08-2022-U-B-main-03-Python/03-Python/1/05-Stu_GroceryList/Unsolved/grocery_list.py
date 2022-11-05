# Create a Python list to store your grocery list
glist = ["grapes", "celery", "chicken", "peanut butter", "jelly", "cheese" ]
# Print the grocery list
print(glist)
print(glist.index("peanut butter"))
# Change "Peanut Butter" to "Almond Butter" and print out the updated list
glist[3] = "almond butter"
# Remove "Jelly" from grocery list and print out the updated list
print(glist.pop(4))
glist.pop(4)
print(glist)
# Add "Coffee" to grocery list and print the updated list
glist.append("coffee")
print(glist)