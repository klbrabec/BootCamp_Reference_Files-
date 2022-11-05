#Requirements (data we need to retrieve)
#1. total number of votes cast
#2. Complete list of candiates that received votes 
#3. percentage of votes each candidate won
#4. Total number of votes each candidate won 
#5. Winner of the election based on the popular vote 

#pseudocode 
# read in the vote file 
# process file to determine list of candidates that received votes 
# process file to determine number of votes per candidate
# process file to determine total number of votes 
# determine percentage of total for votes per candidate
# determine winner of election based on popular vote

#path to CSV file - resources\election_results.csv

#import the date time class from the date time module and set alias
#import datetime as dt

#use the now() attribute to get the present time. 
#now = dt.datetime.now()

#print present time
#print("The time right now is ", now)
import csv 
import os 


file_to_load = os.path.join("Resources", "election_results.csv")
#open and read the file 
with open(file_to_load) as election_data:
    #Print the file object 
    print(election_data)



#create a filename variable to a direct or indirect path 
file_to_save = os.path.join("analysis","election_analysis.txt")
#use the with statement function with W mode to write data 
with open(file_to_save,"w") as txt_file: 
    # write data to the file 
    txt_file.write("Jello world!")
    txt_file.write("Araphaoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")