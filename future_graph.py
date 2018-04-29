from graphics import *

def main():
    #introduction
    print('This program plots the growth of a 10-year investment')
    #get princaple on intrest
    principal = float(input('Enter the intial principal: '))
    
    apr = float(input('Enter the annual interest rate: '))
    #create Graphics window
    win = GraphWin("Investment Growth", 320, 240)
    win.setBackground('white')
    Text(Point(20,230), '0.0k').draw(win)
    Text(Point(20,180), '2.5k').draw(win)
    Text(Point(20,130), '5.0k').draw(win)
    Text(Point(20,80), '7.5k').draw(win)
    Text(Point(20,30), '10.0k').draw(win)
    #draw intial principal bar
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)
    #loop and drawbars for growth
    for year in range(1,11):
        #calculate value for next year
        principal = principal * (1 + apr)
        #draw for next value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)
        
    input("Press <Enter> To Quit")
    win.close()

    

    
main()