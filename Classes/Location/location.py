import random


class Location:
    def __init__(self):
        with open("Classes/Location/Cities/Cities.txt") as file:
            self.cities = file.readlines()

    
    def location(self):
        full_loc = random.choice(self.cities).strip()
        state = full_loc[full_loc.find(",")+1:]
        ret = {"city": full_loc[0:full_loc.find(",")], "state": state[state.find(",")+1:], "state_short": state[0:state.find(",")]}
        return ret
    