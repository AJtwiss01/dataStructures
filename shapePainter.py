from graphics import * 
def getColor(colorString):
    tokens = colorString.split(',')
    if len(tokens) == 3:
        print(int(tokens[1]))
        
        return color_rgb(int(tokens[0]), int(tokens[1]) , int(tokens[2]))
    elif len(colorString) > 0:
        print(colorString)
        return colorString
    else:
        print('white')
        return 'white'
    
def getPoint(pointString):
    x,y = pointString.split(',')
    return Point(int(x),int(y))