
class DonorFinder:
    def __init__(self, donors): #initializer takes list of donors
        self.donors = donors #list of approved donors stored in self.donors

    def search(self, blood_group): #search method to find donors by blood group
        bg = blood_group.strip().upper()
        return [d for d in self.donors if d.blood_group == bg] #returns list of donors matching blood group
