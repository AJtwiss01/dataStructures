from candyData import Candy
def parseCandyDataFromLine( line ):
    name, isChocolate, sugarPercentile, winPct = line.split('\t')
    return Candy( name, isChocolate, sugarPercentile, winPct )

def main():
    candyDataFile = open("candy-data.txt", "r")
    
    noChocCandyWithMaxWinPct = None
    
    for line in candyDataFile:
        line = line.strip()
        
        )
        
        if not candyData.getIsChocolate():
            if noChocCandyWithMaxWinPct == None or candyData.getWinPct() > noChocCandyWithMaxWinPct.getWinPct():
               noChocCandyWithMaxWinPct = candyData
            
    print( noChocCandyWithMaxWinPct.getName() )
    print( noChocCandyWithMaxWinPct.getWinPct() )
    candyDataFile.close()

main()