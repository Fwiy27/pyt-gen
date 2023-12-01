import sys
import random
from os import system
import pyperclip
from colorama import Fore

from Classes.Name.name import Name
from Classes.Location.location import Location
from Classes.Date.date import Date
from Classes.Email.email import Email
from Classes.Password.password import Password

def generator():
    print("                                 _             ")
    print("  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ ")
    print(" / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|")
    print("| (_| |  __/ | | |  __/ | | (_| | || (_) | |   ")
    print(" \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   ")
    print(" |___/                                         ")
    print("-----------------------------------------------")

def details():
    print("     _      _        _ _     ")
    print("  __| | ___| |_ __ _(_) |___ ")
    print(" / _` |/ _ \ __/ _` | | / __|")
    print("| (_| |  __/ || (_| | | \__ \\")
    print(" \__,_|\___|\__\__,_|_|_|___/")
    print("------------------------------")

def clear_screen():
        if sys.platform.startswith("win"):
            system("cls")
        else:
            system("clear")

n = Name()
d = Date()
e = Email()
l = Location()
p = Password()

class Generator:
    def generate_person(self, gender = None):
        if not gender:
            gender = random.choice(["Male", "Female"])
        name = n.name(gender)
        date = d.date()
        location = l.location()
        email = e.email(name["first"], name["middle"], name["last"])
        password = p.password(28)

        return {"gender": gender, 
                "first_name": name["first"],
                "middle_name": name["middle"],
                "last_name": name["last"],
                "dob": date["date"],
                "month": date["month"],
                "day": date["day"],
                "year": date["year"],
                "city": location["city"],
                "state": location["state"],
                "state_short": location["state_short"],
                "email": email,
                "password": password}
     
    def to_string(self, person):
        ret = f"Gender: {person['gender']}\n"
        ret += f"First Name: {person['first_name']}\n"
        ret += f"Middle Name: {person['middle_name']}\n"
        ret += f"Last Name: {person['last_name']}\n"
        ret += f"DOB: {person['dob']}\n"
        ret += f"   Month: {person['month']}\n"
        ret += f"   Day: {person['day']}\n"
        ret += f"   Year: {person['year']}\n"
        ret += f"City: {person['city']}\n"
        ret += f"State: {person['state']} ({person['state_short']})\n"
        ret += f"Email: {person['email']}\n"
        ret += f"Password: {person['password']}"
        return ret
     
    def ui(self):
        print(Fore.RED)
        clear_screen()
        generator()
        print("Seed: [1] YES | [2] NO")
        if int(input("Choice: ")) == 1:
            random.seed(input("Seed: "))
        clear_screen()
        generator()
        print("Gender: [1] MALE | [2] FEMALE | [3] RANDOM")
        match int(input("Choice: ")):
            case 1:
                gender = "Male"
            case 2:
                gender = "Female"
            case _:
                gender = random.choice(["Male", "Female"])
        person = self.generate_person(gender)
        clear_screen()
        print(Fore.CYAN if gender == "Male" else Fore.MAGENTA)
        details()
        personString = self.to_string(person)
        print(personString)
        try:
            pyperclip.copy(personString)
        except Exception:
            None
                
               