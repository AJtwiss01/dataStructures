from graphics import *

def drawBullsEye(centerPoint,window):
    for radius in (50, 5 , -5):
        bullseyeRing = Circle(centerPoint, radius)
        bullseyeRing.draw(window)
    

def main():
    windowWidth = 400
    windowHeight = 400
    
    win = GraphWin("bullseye", windowWidth, windowHeight)
    drawBullsEye(Point(100,200),win)
    drawBullsEye(Point(300,200),win)
    
    
main()