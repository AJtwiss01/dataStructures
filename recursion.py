def listsumd(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsumd(numlist[1:])




print(listsumd([1, 3, 5, 7, 9]))