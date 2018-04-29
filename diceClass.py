from random import randrange

class MSDie:
    
    def __init__(self,sides):
        self.sides = sides
        self.value = 1
        
    def roll(self):
        self.value = randrage(1,self.side+1)
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        
def main():
    die1 = MSDie(12)
    die1.setValue(8)
    print(die1.sides)
    
main()
    