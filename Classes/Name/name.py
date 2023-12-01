import random
class Name:
    def __init__(self):
        with open("Classes/Name/Names/males.txt") as file:
            self.males = file.readlines()
        with open("Classes/Name/Names/females.txt") as file:
            self.females = file.readlines()
        with open("Classes/Name/Names/mname.txt") as file:
            self.middles = file.readlines()
        with open("Classes/Name/Names/lname.txt") as file:
            self.lasts = file.readlines()

    def first(self, gender):
        match gender:
            case "Male":
                return random.choice(self.males).strip()
            case "Female":
                return random.choice(self.females).strip()
        return "Jerry"
    
    def middle(self):
        return random.choice(self.middles).strip()
    
    def last(self):
        return random.choice(self.lasts).strip()
    
    def name(self, gender):
        return {"first": self.first(gender),
                "middle": self.middle(),
                "last": self.last()}