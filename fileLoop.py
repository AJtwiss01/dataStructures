wordsFileName = "words_3.csv"
wordsFile = open(wordsFileName, 'r')


totalNumberOfEs = 0
nextLine = wordsFile.readline()
while nextLine != '':
    words = nextLine.split(',')
    for word in words:
        numberOfEs = word.count('e')
        totalNumberOfEs = totalNumberOfEs + numberOfEs
    nextLine = wordsFile.readline()
wordsFile.close()
print(totalNumberOfEs)