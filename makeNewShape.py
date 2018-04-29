##make new shape
import graphics as g
clickPointY = 30

clickPointY > 0 and clickPointY <= 50 or clickPointY > 450 and clickPointY <= 500

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

win = g.GraphWin("Drawing Generator", WINDOW_WIDTH, WINDOW_HEIGHT)

while True:
    shapeRequest = input("What shape did you want to draw" + "('r' for rectangle, 'c' for circle)? ")
    
    while