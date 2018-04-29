message = input('Enter the message to encrypt: ')
key = int(input('Enter the shift key: '))
outputFileName = input('Enter the name of the file to write the encrypted message to: ')

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

encryptedMessage = ''

for character in message:
    letterIndex = alphabet.find(character)
    encryptedCharcter = shiftedAlphabet[letterIndex]
##    print('{0} -> {1}'.format(character, encryptedCharcter))
    encryptedMessage = encryptedMessage + encryptedCharcter
print('The encrtypted message is:  {0}'.format(encryptedMessage))
outputFile = open(outputFileName, 'w')
print( encryptedMessage , file=outputFile)
outputFile.close()
