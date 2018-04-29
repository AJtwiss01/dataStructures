def fibo( num ):
    x = 0
    y = 1
    for count in range( num ):
        prevX = x
        print( x )
        x = y
        y = y + prevX


num = int( input( "How many terms? " ) )

fibo( num )