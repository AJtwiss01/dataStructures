## Arhut Twiss

def Max(list):
    #returns 
    if len(list) == 1:
        print('yes')
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
    
def Min(list):
    if len(list) == 1:
        print('yes')
        return list[0]
    else:
        m = Min(list[1:])
        return m if m < list[0] else list[0]


def main():
    list = [1,3,4,5,6]
    print("the largest number is: ", Max(list))
    print("the largest number is: ", Min(list))
main()