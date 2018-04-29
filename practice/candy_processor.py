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
    
    def __repr__( self ):
        return '{} , Win Pct: {}'.format(self.name,self.winPct)

def useWinPct(candy):
    return candy.getWinPct()
    
def parseCandyDataFromLine( line ):
    name, isChocolate, sugarPercentile, winPct = line.split('\t')
    return Candy( name, isChocolate, sugarPercentile, winPct )

def main():
    candyDataFile = open("candy-data.txt", "r")
    
    candyList = []
    
    for line in candyDataFile:
        line = line.strip()
        
        candyData = parseCandyDataFromLine( line )
        candyList.append(candyData)
        
        
    candyList.sort(key=useWinPct )
    print(candyList[0:6])
    candyList.reverse()
    print(candyList[0:6])

            
    candyDataFile.close()

main()