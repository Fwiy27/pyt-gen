import random

class Email:
    def email(self, first, middle, last):
        return f"{first}{middle[0]}{last[0]}{random.randint(100, 999)}@gmail.com"