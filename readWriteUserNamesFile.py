inputFileName = input("enter the file name with peoples names: ")
outputFileName = input("enter the file name to write users names to: ")

infile = open(inputFileName, 'r')
outfile = open(outputFileName, 'w')

nameSeg = infile.readlines()
for name in nameSeg:
    splitName = name.strip().split(" ")
    firstName = splitName[0]
    lastName = splitName[1]
    username = firstName[0] + lastName[:7]
    username = username.lower()
    print(username, file=outfile)
infile.close()
outfile.close()
print('done')