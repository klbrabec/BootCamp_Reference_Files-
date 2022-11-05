
counties = ["Arapahoe", "Denver", "Jefferson"] #creates list of counties
for county in counties: 
    print(county)
#-----

if counties[1] == "Denver": #checks value of county in second index position 
    print(counties[1]) #prints to terminal screen if index 1 is equal to Denver. 
#-----

if "El Paso" in counties: #looks for El Paso in the county listing
    print("El Paso is in the list of counties.")
else: #indicates county is not present 
    print("El Paso is not in the list of counties.")
#----- Looks for Araphoe OR ElPaso in counties - OR statement
if "Arapahoe" in counties or "El Paso" in counties:
    print ("Arapahoe or El Paso are in the list of counties.")
else:
    print ("Arapahoe or El Paso is not in the list of counties.")
#-----True if El Paso is not in the county listing 
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not")
#-----
counties = ["Arapahoe", "Denver", "Jefferson"] #creates list of counties
for county in counties: #sets county = counties
    print(county)
#----- Defines a range 
numbers = [0, 1, 2,3,4]
for num in numbers:
    print(num)
#-----
for num in range(5):#same as above, but does not require the implicit definition of the range
    print(num)
#----- defines the range based on the length of the counties list
for i in range(len(counties)): #uses the length command to determine the size of the range and then triggers the loop 
    print(counties[i]) 
#-----

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict: #prints all counties in the dictionary 
    print(county) 
#-----
for anything in counties_dict.keys():
    print(anything)
#-----
for voters in counties_dict.values():
    print(voters)
#-----
for county in counties_dict:
    print(counties_dict[county])
#-----
for county in counties_dict: 
    print(counties_dict.get(county))
#-----
#skill drill on concatenation (found on https://realpython.com)
for key, value in counties_dict.items():
    print(str(key) + " county has " + str(value) + " registered voters")
   
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#-----
#same code using fstrings 
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
#-----
#formatted code using fstrings 
#skill drill
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
#-----
for county_dict in voting_data:
    print(county_dict)
#-----   
#iterating through a list of dictionaries 
# this code will pull just the counties out of the voting_data dictionary and print it.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} # county has {voters:,} registered voters.")

#-----
#getting values from a list of dictionaries 
for county_dict in voting_data: #retrieves each dictionary 
    for value in county_dict.values(): #retrieves each value in each dictionary
        print(value) #prints to screen 

#-----
for county_dict in voting_data:
    print = (f"{county} has {voters} registered voters")
#-----    
#skilldrill with fStrings
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.") #need to include the index for EACH value that is being called so it can match it up. 
 