# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# A list of actors
actors = ["Tom Cruise",
          "Angelina Jolie",
          "Kristen Stewart",
          "Denzel Washington"]

# A dictionary of an actor
actor = {"name": "Tom Cruise"}
print(f'{actor["name"]}')#references the key to get the value associated with that key 

# ---------------------------------------------------------------

# # A dictionary can contain multiple pairs of information
actor_info = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
} #you can access different values of these key pairs using the key value 

print(f'{actor_info["genre"]}')#make sure that you use the right ' pairs here 

# # ---------------------------------------------------------------

# # A dictionary can contain multiple types of information
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{another_actor["name"]} was in {another_actor["best movies"][0]}')
# # ---------------------------------------------------------------

# # A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")
# # ---------------------------------------------------------------
# # dictionaries will be a huge thing that we use in python
# it's important to know how to navigate and move through them
# These are where we will be storing data 