from graphics import *
from button import Button

class ProjectileInputDialog:

    def __init__( self, angle, vel, height ):
        self.win = GraphWin( "Initial Values", 200, 300)
        
        self.win.setCoords( 0, 4.5, 4, .5 )
        
        Text( Point(1, 1), "Angle").draw( self.win )
        self.angle = Entry( Point(3, 1), 5).draw( self.win )
        self.angle.setText( str( angle ) )
        
        Text( Point(1, 2), "Velocity").draw( self.win )
        self.vel = Entry( Point(3, 2), 5).draw( self.win )
        self.vel.setText( str( vel ) )        
        
        Text( Point(1, 3), "Height").draw( self.win )
        self.height = Entry( Point(3, 3), 5).draw( self.win )
        self.height.setText( str( height ) )
        
        self.fire = Button( self.win, Point(1, 4), 1.25, .5, "Fire!" )
        self.fire.enable()
        
        self.quit = Button( self.win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.enable()
    
    def enable( self ):
        while True:
            pt = self.win.getMouse()
            if self.quit.wasClickedIn( pt ):
                return "Quit"
            if self.fire.wasClickedIn( pt ):
                return "Fire!"
            
    def getValues( self ):
        a = float( self.angle.getText() )
        v = float( self.vel.getText() )
        h = float( self.height.getText() )
        return a, v, h
    
    
    def close( self ):
        self.win.close()
        