def parseName(name):
    nameParts = name.split(' ')
    return nameParts[0], nameParts[1]

def main():
    names = [ 'Arthur Twiss', 'Sara Twiss']
    for name in names:
        firstName, lastName = parseName(name)
        print("Frist Name: {0}, Last Name: {1}".format(firstName, lastName))
        
        
main()