from Devs import Bob_Robins, Jaghatai
from Publishers import Rob_Peterson, Lion_Johnson

class DeveloperTeam:
    
    members = [Bob_Robins, Jaghatai]

    def __init__(self, members):
        self.members = members

        # self.members: List[Bob_Robins, Jaghatai]
        # members.append(Bob_Robins, Jaghatai)

    def CheckFired(self):
        CheckingDevDict = {}
        for worker in self.members:
            if worker.IsFired == False:
                # print(worker.name, 'is not currently fired')
                CheckingDevDict[worker.name] = False
            else:
                # print(worker.name, 'is currently fired')
                CheckingDevDict[worker.name] = True
#       print(CheckingDevDict)
        return CheckingDevDict
            


class PublisherTeam:
    
    members = [Rob_Peterson, Lion_Johnson]

    def __init__(self, members):
        self.members = members

    def CheckFired(self):
        CheckingPubDict = {}
        for worker in self.members:
            if worker.IsFired == False:
                # print(worker.name, 'is not currently fired')
                CheckingPubDict[worker.name] = False
            else:
                # print(worker.name, 'is currently fired')
                CheckingPubDict[worker.name] = True
#        print(CheckingPubDict)
        return CheckingPubDict

# PublisherTeam.CheckFired(PublisherTeam)
# DeveloperTeam.CheckFired(DeveloperTeam)