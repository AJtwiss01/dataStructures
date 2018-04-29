movieRatingsFile = None

while True:
    movieRatingsFileName = input("Enter File Name: ")
    try:
        movieRatingsFiles = open(movieRatingsFileName, "r")
        break
    except FileNotFoundError:
        print("{0} was not found".format(movieRatingsFileName))

firstLine = movieRatingsFiles.readline();
firstLineTokens = firstLine.split(",")
movieTitle = firstLineTokens[1]

totalRatings = 0
totalRatingsAboveCool = 0

for line in movieRatingsFiles:
    ratings = line.split(",")
  
    for rating in ratings:
        numericRating = int(rating)
        totalRatings += 1
        if numericRating >= 6:
            totalRatingsAboveCool += 1

coolPct = totalRatingsAboveCool / totalRatings


print("Movie Title: {0}".format(movieTitle))
print("Total Number of Ratings: {0}".format(totalRatings))
print("Cool Percentage: {0}".format(coolPct))

ratingImageFileName = ''
if totalRatings < 10 :
    print("To soon to rule")
    ratingImageFileName = 'tooSoonToRule.gif'
elif coolPct >= .6:
    print("Cool")
    ratingImageFileName = 'cool.gif'
else :
    print('Drool')
    ratingImageFileName = 'drool.gif'
import graphics as g
win = g.GraphWin('Cool Drool Rater', 400, 400)
titleText = g.Text(g.Point(200,50), movieTitle)
titleText.draw(win)
ratingImage = g.Image(g.Point(200, 200), ratingImageFileName)
ratingImage.draw(win)

coolPctText = g.Text(g.Point(200,350), "{0:0.0f}% {1}".format(coolPct * 100, rating))
coolPctText.draw(win)