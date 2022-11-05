#what is the score?
score = int(input("What is your test score"))

#Determine the grade 
if score >=90:
    print("Your grade is an A")
else:
    if score >=80:
        print ("Your grade is a B")
    else: 
        if score >= 70: 
            print ("Your grade is a C")
        else: 
            if score >=70:
                print ("Your grade is a D.")
            else:
                print("Your grade is an F")

#What is the second score 
second_score = int(input("What is your second test score?"))

#determine the grade
if second_score >=90:
    print("Your second grade is an A.")
elif second_score >=80:
    print("Your second grade is a B")
elif second_score >=70:
    print("Your second grade is a C")
elif second_score >=60:
    print("Your second grade is a D")
else: 
    print("Your second grade is an F")
