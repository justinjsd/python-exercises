# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, date, month, year):
        self.date = date 
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.date}.{self.month}.{self.year}"
    
    def __eq__(self, value):
        return self.__str__() == value.__str__()
    
    def __ne__(self, value):
        return self.__str__() != value.__str__()
    
    def __gt__(self, value):
        if self.year > value.year:
            return True
        elif self.year == value.year and self.month > value.month:
            return True
        elif self.month == value.month and self.date > value.date:
            return True
        else: 
            return False
        
    def __lt__(self, value):
        if self.year < value.year:
            return True
        elif self.year == value.year and self.month < value.month:
            return True
        elif self.month == value.month and self.date < value.date:
            return True
        else: 
            return False
        
    def __convert_curr_date_to_days(self):
        return ((self.__year-1)*12*30) + ((self.__month-1)*30) + self.__day

    def __add__(self, days_to_add: int):
        days = self.__convert_curr_date_to_days()
        days += days_to_add
        year = (days//360)+1
        month = ((days//30)%12)+1
        day = days%30
        return SimpleDate(day, month, year)
        
    def __sub__(self, another: 'SimpleDate'):
        curr_days = self.__convert_curr_date_to_days()
        another_days = another.__convert_curr_date_to_days()
        return abs(curr_days - another_days)
    
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)