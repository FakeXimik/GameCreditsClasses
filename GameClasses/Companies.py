from Teams import DeveloperTeam
from Teams import PublisherTeam

class DeveloperCompany:

    team = list(DeveloperTeam.members)

    def __init__(self, team):
        self.team = team

    def info(self):
        print('The coolest developer company in the whole universe')

    def ShowWorkers(self):
        for worker in self.team:
            print(worker.name)

#DeveloperCompany.ShowWorkers(DeveloperCompany)

class PublisherCompany:

    team = list(PublisherTeam.members)
    
    def __init__(self, team):
        self.team = team

    def info(self):
        print('The coolest publisher company in the whole universe')

    def ShowWorkers(self):
        for worker in self.team:
            print(worker.name)

# PublisherCompany.ShowWorkers(PublisherCompany)