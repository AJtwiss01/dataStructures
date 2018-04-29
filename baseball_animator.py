from graphics import *
from projectile_input_dialog import *
from baseball_tracker import *

def main():
    win = GraphWin( "Baseball Animation", 640, 480, autoflush=False )
    win.setCoords( -10, -10, 210, 155 )
    
    Line( Point(-10, 0), Point(210, 0)).draw( win )
    
    for x in range(0, 210, 50 ):
        Text( Point(x , -5), str( x )).draw( win )
        Line( Point(x, 0), Point( x, 2 )).draw( win )
        
    angle, vel, height = 45, 40, 2
    while True:
        inputDialog = ProjectileInputDialog( angle, vel, height )
        response = inputDialog.enable()
        inputDialog.close()
        
        if response == 'Quit':
            break
        
        angle, vel, height = inputDialog.getValues()
        tracker = BaseballTracker( win, angle, vel, height )
        
        while tracker.getY() >= 0 and tracker.getX() <= 210:
            tracker.update( 1/50 )
            update( 50 )
        
    # Work in here
    
    win.close()
    
main()