print('This program computes the slope of the line between two points: p1 and p2')

try:
    p1_x = int( input('Enter p1\'s x value: ') )
    p1_y = int( input('Enter p1\'s y value: ') )
    print('')

    p2_x = int( input('Enter p2\'s x value: ') )
    p2_y = int( input('Enter p2\'s y value: ') )
    print('')

    slope = (p2_y - p1_y) / (p2_x - p1_x)

    print('The slope is: {0:0.3f}'.format( slope ) )
except ZeroDivisionError:
    print('The points are on a vertical line: there is no slope')
except ValueError:
    print('bad input')

    