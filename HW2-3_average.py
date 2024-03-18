student_name = input ("Enter student's name... ")
student_family = input ("Enter student's surname... ")
count = 0
sum = 0

while input(" enter exit to calculate the average of scores  or enter C to continue   ") != "exit" :
    score = int ( input ("Enter the score between 0-20 : ...") )
    if score <= 20 and score >= 0 :
        sum += score
        count += 1
    elif score == "exit":
        break
    else:
        print ( "Error: Wrong score." )
        print ( "Enter a number between 0 and 20." )
if count > 0 :
    average = sum / count 
    print ( "The averge of " , student_name, " " , student_family , "is : ", average )   

