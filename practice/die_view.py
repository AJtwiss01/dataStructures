from graphics import *
from msdie import MultiSidedDie

class DieView:
    def __init__( self, window, centerPoint, size ):
        self.die = MultiSidedDie( 6, 1 )
        self.window = window
        
        minX = centerPoint.getX() - size / 2.0
        maxX = centerPoint.getX() + size / 2.0
        
        minY = centerPoint.getY() - size / 2.0
        maxY = centerPoint.getY() + size / 2.0
        
        ulPt = Point( minX, minY)
        lrPt = Point( maxX, maxY)
        
        self.dieOutline = Rectangle( ulPt, lrPt )
        self.dieOutline.setFill( 'white' )
        self.dieOutline.draw( window )
    
        pipRadius = size / 7 / 2
        column1X = centerPoint.getX() - size / 4
        column3X = centerPoint.getX() + size / 4
        row1Y = centerPoint.getY() - size / 4
        row3Y = centerPoint.getY() + size / 4
        
        self.pips = []

        self.pips.append(self.__makePip( column1X, row1Y, pipRadius ))
        self.pips.append(self.__makePip( column3X, row1Y, pipRadius ))
        
        self.pips.append(self.__makePip( column1X, centerPoint.getY(), pipRadius ))
        self.pips.append(self.__makePip( centerPoint.getX(), centerPoint.getY(), pipRadius ))
        self.pips.append(self.__makePip( column3X, centerPoint.getY(), pipRadius ))
        
        self.pips.append(self.__makePip( column1X, row3Y, pipRadius ))
        self.pips.append(self.__makePip( column3X, row3Y, pipRadius ))
        
     
    def __makePip( self, x, y, r ):
        pip = Circle( Point( x, y ), r )
        pip.setFill( 'black' )
        return pip
    
    def __clearPips( self ):
        for pip in self.pips:
            pip.undraw()
            
    def __updatePips( self, dieValue ):
        self.__clearPips()
        pipsOnList = [[3], [0,6], [0,3,6], [0,1,5,6],[0,1,3,5,6]]
        pipsTurnOnList = pipsOnList[ dieValue - 1 ]
        
        for index in pipsTurnOnList:
            self.pips[index].draw( self.window)
    
    def roll( self ):
        self.die.roll()
        self.__updatePips( self.die.getValue() )
        
    def getValue( self ):
        return self.die.getValue()
    
def main():
    w = GraphWin( "Test DieView", 200, 200 )
    w.setBackground( 'dark green' )
    d = DieView( w, Point( 100, 100), 100 )
    
    while True:
        w.getMouse()
        d.roll()
    
main()
