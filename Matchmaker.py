# Matchmaker.py
'''
End goal is to be able to simulate the effects of game length, playerbase size,
smurfing, and other factors on matchmaking both on the average player and either
end of the skill spectrum.
'''
import random
import time
# Using numbers higher than a million will make it take quite a while
playerbase = 1000
players = []
start_time = time.time()


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

    # These definitions are so that we can sort our player objects by MMR later.
    # This allows us to use the players.sort() and sorted(players) functions
    def __eq__(self, other):
        return self.MMR == other.MMR

    def __lt__(self, other):
        return self.MMR < other.MMR

    def __gt__(self, other):
        return self.MMR > other.MMR

    def __le__(self, other):
        return self.MMR <= other.MMR

    def __ge__(self, other):
        return self.MMR >= other.MMR
    # defines how the object should be displayed when represented anywhere.
    # without this when we would try to print our objects, we would get memory addresses
    # it is currently set to display the player's MMR followed by the roles they play.

    def __repr__(self):
        return str(self.MMR) + " " + str(self.roles)

    def getMMR(self):
        return int(self.MMR)

    def getRoles(self):
        return self.roles
    '''
    other things to consider adding to the Player Class:
        -having MMR and actual skill be different values so we can have win probabilities of smurfs
        -having preferred hours of play or number of hours they're willing to play in a day
    '''


class Game:
    def __init__(self, radiant, dire):
        self.radiant = radiant
        self.dire = dire
        # number of seconds in the game. Useful for later when we simulate people logging in and out.
        # currently set to about 36:40 with a standard deviation of 18:20
        self.duration = round(random.gauss(2200, 1100))

    def __repr__(radiant, dire):
        return str(self.radiant) + ' vs. ' + str(self.dire)
# This is going to iterate through all queueing players and create a 5v5 match.
# First iteration just grabs a player at the start of the list and finds 9 people within 100 MMR
# Roles are not yet implemented
# Once the match is created, it deletes them from the list of queueing players


def CreateMatch(MMRRange):
    matchPlayers = []
    radiant = []
    dire = []
    if len(players) > 0:
        basePlayer = players[0].getMMR()
        matchPlayers.append(players[0])
        del players[0]
    for num, player in enumerate(players):
        if abs(basePlayer - player.MMR) < MMRRange:
            matchPlayers.append(player)
            del players[num]
            if len(matchPlayers) == 10:
                break
    matchPlayers.sort()
    if len(matchPlayers) < 10:
        players.extend(matchPlayers)
        random.shuffle(players)
        return 1
    if len(matchPlayers) == 10:
        for i in range(0, 10, 2):
            radiant.append(matchPlayers[i])
        for i in range(1, 11, 2):
            dire.append(matchPlayers[i])

    if len(radiant) == 5 and len(dire) == 5:
        return str(radiant) + ' vs. ' + str(dire)


def main():
    matches = []
    for i in range(playerbase):
        players.append(Player())
    print("Created playerbase\nForming Matches\n")
    for i in range(10000):
        matches.append(CreateMatch(50))

    matches2 = [x for x in matches if isinstance(x, str)]
    print(10 * len(matches2))
    for i in matches2:
        print(i)
    print("\nReject Players\n\n" + str(len(players)))
    print(sorted(players))


main()
