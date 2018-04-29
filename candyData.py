class Candy:
    def __init__( self, name, isChocolate, sugarPercentile, winPct ):
        self.name = name
        
        if isChocolate == "0":
            self.isChocolate = False
        else:
            self.isChocolate = True
            
        self.sugarPercentile = float( sugarPercentile )
        self.winPct = float( winPct )
        
    def getName( self ):
        return self.name
    
    def getIsChocolate( self ):
        return self.isChocolate
    
    def getSugarPercentile( self ):
        return self.sugarPercentile
    
    def getWinPct( self ):
        return self.winPct