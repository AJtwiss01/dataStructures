def main():
    candyFile = open('candy-data.txt','r')
    
##    noChocCanWitMaxWinPct =
    
    for line in candyFile:
        line = line.strip()
        print(line)
        candyData = parseData(line)
        if not candyData.isChoclate():


main()