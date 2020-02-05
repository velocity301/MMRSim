# Matchmaker.py
'''
End goal is to be able to simulate the effects of game length, playerbase size, 
smurfing, and other factors on matchmaking both on the average player and either 
end of the skill spectrum.  
'''
import random
playerbase = 10

players = []
sortedPlayersMMRValues = []


class Player:
    def __init__(self):
        # generates a random MMR using a gaussian distribution (bell curve)
        # random.gauss(center, std deviation)
        self.MMR = round(random.gauss(2200, 1100))
        # sets any negative MMR values to zero instead
        if self.MMR < 0:
            self.MMR = 0
        # generates behavior score for a player between 0 and 10000.
        # Currently completely random
        self.behaviorScore = random.randrange(0, 10000, 1)
        # creates list of roles the player plays
        # Probability someone plays a given position is given by
        # the number the randint is less than.
        # The reason this is a while loop is to prevent a player being
        # generated without any roles they play.
        self.roles = []
        while len(self.roles) == 0:
            self.roles = []
            if random.randint(0, 100) < 30:
                self.roles.append(1)
            if random.randint(0, 100) < 50:
                self.roles.append(2)
            if random.randint(0, 100) < 20:
                self.roles.append(3)
            if random.randint(0, 100) < 15:
                self.roles.append(4)
            if random.randint(0, 100) < 10:
                self.roles.append(5)
        # This says whether the player is ingame or queueing or neither.
        # For later when we simulate actual games happenign
        self.status = "queueing"  # alternate values will be "playing" and "offline"

    # The eq and lt definitions are so that we can sort our player objects by MMR later.
    # This allows us to use the players.sort() and sorted(players) functions
    def __eq__(self, other):
        return self.MMR == other.MMR

    def __lt__(self, other):
        return self.MMR < other.MMR
    # defines how the object should be displayed when represented anywhere.
    # without this when we would try to print our objects, we would get memory addresses

    def __repr__(self):
        return str(self.MMR) + " " + str(self.roles)

    '''    
    other things to consider adding to the Player Class: 
    	-having MMR and actual skill be different values so we can have win probabilities of smurfs
    	-having preferred hours of play or number of hours they're willing to play in a day
	'''


# player generation
for i in range(playerbase):
    players.append(Player())
print(sorted(players))
