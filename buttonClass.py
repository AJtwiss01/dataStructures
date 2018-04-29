from graphics import *

class Button:
    
    def __init__(self, window, centerPoint, height, widht, text):
        ulPt = Point(centerPoint.getX() - width / 2.0 , centerPoint.getX() - height / 2.0)
        lrPt =  Point(centerPoint.getX() + width / 2.0 , centerPoint.getX() + height / 2.0)
        
        self.rect = Rectangle(ulPt, lrPt)
        self.rect.draw(window)

        self.text = Text(centerPoint,text)
        self.text.draw(window)