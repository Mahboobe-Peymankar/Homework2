hr = int ( input ( "enter an hour..." ) )
min = int ( input ( "enter a minute between 0 and 60...") )
sec = int ( input ( "enter a second betweenn 0 and 60...") )
time_in_sec = hr * 3600 + min * 60 + sec
print ( "Time in second =",time_in_sec)