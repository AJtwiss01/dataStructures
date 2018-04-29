## Arthur Twiss (AJ)
List = [1,2,3,4,[5,8,9,10]]

result = []
def makeArray(myList):
    for i in myList:
        print('{} this is i'.format(i))
        # checking in i is a list
        if isinstance(i, list):
            #hits second array and makes it to int that will hit the else and append to results
            print('hit 2 array')
            return makeArray(i)
        else:
            #then ruturns the and appends the to the reauslt arrayu
            result.append(i)
    #returns Resuslts 
    return result
#prints out results by calling and running function 
print(makeArray(List))