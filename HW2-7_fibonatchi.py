a = 0
b = 1
i = 1
n = int ( input ("Enter a number of Fibonacci sequence ...") )
if n == 0 :
    print ("---")
elif n == 1 :
    print ("1")

elif n > 1 :
    while i <= n :
        print ( b , " ", end = " ")
        c = a + b
        a = b
        b = c
        i += 1


