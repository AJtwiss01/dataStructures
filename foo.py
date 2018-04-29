class Foo:
    def __init__( self, n ):
        print( 'Init Foo with', n)
        self.n = 2 * n

    def bar( self, x ):
        print( 'Barred:', x )
        print( x * self.n )
        return x + self.n

    def getN( self ):
       return self.n

def main():
    print('Starting up')
    f1 = Foo( 3 )
    f2 = Foo( 4 )
    print( f1.bar( f2.getN() ) )

main()