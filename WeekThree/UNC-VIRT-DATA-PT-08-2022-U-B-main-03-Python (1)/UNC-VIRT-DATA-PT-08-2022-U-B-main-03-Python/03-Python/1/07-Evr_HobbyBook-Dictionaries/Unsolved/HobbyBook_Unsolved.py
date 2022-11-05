# * Create a dictionary to store the following:
#   * Your pet's name
#   * Your pet's age
#   * A list of a few of your pet's hobbies
#   * A dictionary of a few times you wake up during the week

# * Print out the following:
#   * Your pet's name and age.
#   * How many hobbies your pet has.
#   * What your pet's favorite hobby is.
#   * What time your pet wakes on one of the days of the week.

pets = {
    "name": "Logan",
    "age": 1,
    "hobbies": ["squeaky donut", "snacks", "chase"],
    "wakeup": {"M": 5, "T": 6, "Daily": "Too Dang Early"}}

print(pets)

print(f'Hello I am {pets["name"]} and I am {pets["age"]} years old.')
print(f'I have {len(pets["hobbies"])} hobbies!')
print(f'One of my favorite hobbies is {pets["hobbies"][0]}.')
print(f'My normal wakeup time is {pets["wakeup"]["Daily"]}' )

