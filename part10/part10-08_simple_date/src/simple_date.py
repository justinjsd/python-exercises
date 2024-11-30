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
    
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)