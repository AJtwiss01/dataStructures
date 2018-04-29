def getTextFile():
    fileName = input('Enter file to Check: ')
    textFile = open(fileName, 'r')
    return fileName, textFile

def outPutCountResults(fileName, lineCount, wordCount, charCount):
    print()
    print('****{0}****'.format(fileName))
    print('LineCount = {0}'.format(lineCount))
    print('WordCount = {0}'.format(wordCount))
    print('CharacterCount = {0}'.format(charCount))
    
def countCharacters(eachLine):
    charCount = 0
    for i in eachLine:
        if not i.isspace():
            charCount = charCount + 1
            
    return charCount
def countWords(numberOfWord):
    words = numberOfWord.split()
    return len(words)
def DocStats(docFile):
    lineCount = 0
    totalCharacters = 0
    totalWords = 0
    for line in docFile:
        lineCount = lineCount + 1
        totalCharacters = totalCharacters + countCharacters(line)
        totalWords = totalWords + countWords(line)
    return lineCount, totalCharacters, totalWords
    
def main():
    fileName, docFile = getTextFile()
    lineCount, totalCharacters, totalWords = DocStats(docFile)
    
    outPutCountResults(fileName, lineCount, totalWords ,totalCharacters)
    
main()
    
