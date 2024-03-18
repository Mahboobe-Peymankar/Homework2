while ( input() != "exit" ) :
    TimeInSec = int ( input ( "Enter a time in second ...." ) )
    hr = TimeInSec // 3600
    min = ( TimeInSec % 3600 ) // 60
    sec = ( TimeInSec % 3600 ) % 60
    d = 0
    if hr >= 24 :
        d = hr // 24
        hr = hr % 24

    print ("Time = " , d , "day/days and ", hr , ":" , min , ":" ,sec)


