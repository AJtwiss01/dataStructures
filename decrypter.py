inputFileName = input('Enter the file nane to dycrypt: ')
key = int(input('Enter the shift key: '))

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

inputFile = open(inputFileName, 'r')
encryptMessage = inputFile.readline()
print(encryptMessage)
dycryptedMessage = ''
for character in encryptMessage.strip():
    letterIndex = shiftedAlphabet.find(character)
    decreptCharcter = alphabet[letterIndex]
    dycryptedMessage = dycryptedMessage + decreptCharcter
print('The dycrypted message is: {0}'.format(dycryptedMessage))

inputFile.close()