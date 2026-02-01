
import json
from donor import Donor

class DonorDatabase:
    def __init__(self, filename="donors.json"):
        self.filename = filename #file to store donor data
        self.load() #load existing data

    def load(self):
        try:
            with open(self.filename) as f: #open file
                self.donors = [Donor.from_dict(d) for d in json.load(f)] #load donors from file
        except FileNotFoundError: #if file not found
            self.donors = [] #initialize empty list

    def save(self): #save donors to file
        with open(self.filename, "w") as f: #open file in write mode
            json.dump([d.to_dict() for d in self.donors], f, indent=4) #write donor data as json

    def add(self, donor): #add new donor
        self.donors.append(donor) #append to list
        self.save() #save updated list

    def approved(self):
        return [d for d in self.donors if d.status == "approved"]

    def pending(self):
        return [d for d in self.donors if d.status == "pending"]
