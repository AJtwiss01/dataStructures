from graphics import *
from msdie import MultiSidedDie

class DieView:
    
    def __init__( self, window ,centerPoint, size):
        self.die = MultiSidedDie( 6, 1)
        minX = centerPoint.getX() - size / 2.0
        maxX = centerPoint.getX() + size / 2.0
        
        minY = centerPoint.getY() - size / 2.0
        maxY = centerPoint.getY() + size / 2.0
        
        ulPt = Point( minX, minY)
        lrPt = Point( maxX, maxY)
        
        self.dieOutline = Rectangle( ulPt, lrPt )
        self.dieOutline.setFill("white")
        self.dieOutline.draw(window)
        
        pipRadius = size / 7 / 2
        
        column1x = centerPoint.getX() - size / 4
        column3x = centerPoint.getX() + size / 4
        row1x = centerPoint.getY() - size /4
        row3x = centerPoint.getY() + size /4
    
        self.pip1_1 = self.__makePip(column1x,row1x, pipRadius)
        self.pip1_2 = self.__makePip(column1x,row3x, pipRadius)

        self.pip2_1 = self.__makePip(column1x, centerPoint.getY(), pipRadius)
        self.pip2_2 = self.__makePip(centerPoint.getX(), centerPoint.getY(), pipRadius)
        self.pip2_3 = self.__makePip(column3x, centerPoint.getY(), pipRadius)

        self.pip3_3 = self.__makePip(column3x,row3x, pipRadius)
        self.pip3_1 = self.__makePip(column3x,row1x, pipRadius)

        self.pip1_1.draw(window)
        self.pip1_2.draw(window)
        self.pip2_1.draw( window )
        self.pip2_2.draw( window )
        self.pip2_3.draw( window )
        self.pip3_1.draw(window)
        self.pip3_3.draw(window)

        
    def __makePip(self, x, y, r):
        pip = Circle( Point(x,y),r)
        pip.setFill('black')
        return pip
        
    
    def roll(self):
        self.die.roll()
        print( self.die.getValue() )

w = GraphWin("test", 500, 500)
d = DieView(w, Point(250,250), 100)
d.roll()
d.roll()
d.roll()