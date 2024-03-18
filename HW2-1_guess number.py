import random

coomputer_number = random.randint ( 10 , 99 )
for i in range ( 100 ) :
    user_number = int ( input ( "Enter your guess number..." ) )

    if coomputer_number == user_number :
        print ( "🌹🌹Congratulation🌹🌹 " )
        print ( "------You Win---------")
        print ( "Number of unsuccessful attempts :", i )
        print ( "Number of attempts :", i+1 )
        break
    
    elif coomputer_number > user_number :
        print ( "Go UP ⏫⏫" )
    
    else :
        print ( "Go Down ⏬⏬" )