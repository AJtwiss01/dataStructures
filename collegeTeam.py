class collegeSportsTeam:
    def __init__(self, name, collegeName, typeOfTeam, playerCount, division):
        
        self.name = name
        self.collegeName = collegeName
        self.typeOfTeam = typeOfTeam
        self.playerCount = playerCount
        self.division = division
        
        
     ##setters

    def setName(self, name):
        self.name = name
        
    def setCollegeName(self, collegeName):
        self.collegeName = collegeName
        
    def setTypeOfTeam(self, typeOfTeam):
        self.typeOfTeam = typeOfTeam
        
    def setPlayersCount(self, playerCount):
        self.playerCount = playerCount
        
    def setDivision(self, division):
        self.division = division
        
    #getters
        
    def getName(self):
        return self.name
    
    def getCollegName(self):
        return self.collegeName
    
    def getTypeOfTeam(self):
        return self.typeOfTeam
    
    def getPlayersCount(self):
        return self.playerCount
    
    def getDivision(self):
        return self.division

def main():
    
    name = input('Name of Team?: ')
    collegeName = input('What the name of University or College?: ')
    typeOfTeam = input('What sport?: ')
    playerCount = input('How many playes on the team?: ')
    division = input('What Division?: ')
 
    myCollegeTeam = collegeSportsTeam(name, collegeName, typeOfTeam, playerCount, division)
    #prints cars, make and model, year, and engine to check if works
    print('My team name is {}, I play for the university of {}, We play {}'.format(myCollegeTeam.getName(),myCollegeTeam.getCollegName(),myCollegeTeam.getTypeOfTeam()))
    
main()
    