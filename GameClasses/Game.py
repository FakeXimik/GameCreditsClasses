from Companies import PublisherCompany, DeveloperCompany, DeveloperTeam, PublisherTeam
from typing import List

from Publishers import Rob_Peterson

class Game:

    def ShowCredits(self):
        print("\n Developer Team: \n")
        for check in DeveloperTeam.CheckFired(DeveloperTeam):
            if DeveloperTeam.CheckFired(DeveloperTeam)[check] == True:
                continue
            else:
                print(check)
            # print(check)
            # PublisherCompany.ShowWorkers(PublisherCompany)
        print("\n Publisher Team: \n")
        for check in PublisherTeam.CheckFired(PublisherTeam):
            if PublisherTeam.CheckFired(PublisherTeam)[check] == True:
                continue
            else:
                print(check)  

    def Info(self):
        print("The coolest game in the whole universe")

Game.ShowCredits(Game)
# Game.Info(Game)