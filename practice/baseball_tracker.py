from graphics import *
from projectile import Projectile

class BaseballTracker:
    def __init__( self, window, angle, velocity, height ):
        
        self.projectile = Projectile( angle, velocity, height )
        
        self.ball = Circle( Point( 0, height ), 3 )
        self.ball.setOutline( 'red' )
        self.ball.setFill( 'red' )
        self.ball.draw( window )
        
    def update( self, timeInterval ):
        prevX = self.projectile.getX()
        prevY = self.projectile.getY()
        
        self.projectile.update( timeInterval )
        
        dx = self.projectile.getX() - prevX
        dy = self.projectile.getY() - prevY
        
        self.ball.move( dx, dy )
        
    def clear( self ):
        self.ball.undraw()
        
    def getX( self ):
        return self.projectile.getX()
        
    def getY( self ):
        return self.projectile.getY()       
        
        
        
    