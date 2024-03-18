import random

computer_score = 0
user_score = 0

for i in range (100) :
   
    x = random.randint ( 1 , 3 )
    
    if x == 1 :
        computer_choice = "rock"
    elif x == 2 :
        computer_choice = "paper"
    else :
        computer_choice = "scissors"

    user_choice = input ("Enter your choice (rock,paper or scissors...)")

    print ( "💻   : " , computer_choice )
    print ( "👩👨 : " , user_choice )

    if ( user_choice == "rock" and computer_choice == "paper" ) or ( user_choice == "paper" and computer_choice == "scissors" ) or ( user_choice == "scissors" and computer_choice == "rock" ):
        print ( "Computer win" )
        computer_score += 1
    
    elif ( user_choice == "rock" and computer_choice == "scissors" ) or ( user_choice == "paper" and computer_choice == "rock" ) or ( user_choice == "scissors" and computer_choice == "paper" ):
        print ( "User win" )
        user_score +=1

    elif ( user_choice == computer_choice ):
        print ( "whitout score..." )
       
    
    if ( user_score == 3 ) :
        print ( "🌹CONGRATULATION 🌹" )
        print ( "      YOU WIN     " )
        break
    elif (computer_score == 3):
        print ( "😐 GAME OVER 😑" )
        print ( "     YOU LOSE   " )
        break
    else :
        print ( "TRY AGAIN " )
    

    






