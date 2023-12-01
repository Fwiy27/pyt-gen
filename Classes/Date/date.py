import random

class Date:
    def __init__(self):
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.thirty=['April', 'June', 'September', 'November']
        self.thirtyone=['January', 'March', 'May', 'July', 'August', 'October', 'December']
    
    def date(self):
        month = random.choice(self.months)
        if month in self.thirty:
            day = random.randint(1, 30)
        elif month in self.thirtyone:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 28)
        year = random.randint(1959, 2002)
        date = f"{self.months.index(month) + 1}/{day}/{year}"
        ret = {"year": year, "month": month, "day": day, "date": date}

        return ret
        