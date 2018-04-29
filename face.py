import graphics as g

win = g.GraphWin('happy face', 300,300)
leftPupil = g.Point(100,70)



rightPupil = g.Point(200,70)


leftEye = g.Circle(leftPupil, 25)
leftEye.setFill('white')
leftEye.setOutline('magenta')
leftEye.draw( win )
leftPupil.draw( win )

rightEye = g.Circle(rightPupil, 25)
rightEye.setFill('white')
rightEye.setOutline('magenta')
rightEye.draw( win )
rightPupil.draw( win )

nose = g.Rectangle( g.Point(125, 150), g.Point(175, 175))
nose.setOutline('red')
nose.draw( win )

centerMouthPoint = g.Point(150, 200)
leftMouthLine = g.Line( g.Point( 40, 180), centerMouthPoint)
leftMouthLine.setOutline('green')
leftMouthLine.draw( win )


rightMouthLine = g.Line( centerMouthPoint, g.Point(260, 175))
rightMouthLine.setOutline('green')
rightMouthLine.draw( win )
