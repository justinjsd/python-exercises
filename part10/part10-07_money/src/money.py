# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, value):
        return self.__str__() == value.__str__()
    
    def __gt__(self, value):
        return self.__str__() > value.__str__()
    
    def __lt__(self, value):
        return self.__str__() < value.__str__()
    
    def __ne__(self, value):
        return self.__str__() != value.__str__()
    
    def __add__(self, value):
        val1 = float(f"{self.__euros}.{self.__cents:02}")
        val2 = float(f"{value.__euros}.{value.__cents:02}")
        sum = val1 + val2
        return f"{sum:.2f} eur"
    
    def __sub__(self, value):
        val1 = float(f"{self.__euros}.{self.__cents:02}")
        val2 = float(f"{value.__euros}.{value.__cents:02}")
        dif = val1 - val2
        if dif < 0:
            raise ValueError("Negative Number")
        return f"{dif:.2f} eur"

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1