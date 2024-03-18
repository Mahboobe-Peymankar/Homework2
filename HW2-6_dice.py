import random
No_player = int ( input ( "How many players are there in this game?   ") )

while input("enter exit to calculate the average of scores  or enter C to continue   ") != "exit" :
    i=1
    while i <= No_player :   
        dice_number = random.randint ( 1 , 6 )
        print ("dice number of player" , i , ":" , dice_number)
        while dice_number == 6 :
            dice_number = random.randint ( 1 , 6 )
            print ("bonus of player" , i , ":" , dice_number)  
        i += 1
    print ( "----------------" )