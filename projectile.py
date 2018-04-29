import math

class Projectile:
    def __init__( self, angle, velocity, height):
        self.xPos = 0
        self.yPos = height
    
        theta = math.radians( angle )
        self.yVel = velocity * math.sin( theta )
        self.xVel = velocity * math.cos( theta )
    
    def getX( self ):
        return self.xPos
    
    def getY( self ):
        return self.yPos
    
    def update( self, timeInterval ):
        self.xPos = self.xVel * timeInterval + self.xPos
        
        yNewVel = self.yVel - 9.8 * timeInterval
        self.yPos = self.yPos + (yNewVel + self.yVel ) / 2.0 * timeInterval
        self.yVel = yNewVel   