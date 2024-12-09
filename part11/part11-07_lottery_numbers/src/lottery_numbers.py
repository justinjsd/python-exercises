# WRITE YOUR SOLUTION HERE:

class LotteryNumbers:
    def __init__(self, week: int, num: list):
        self.week = week
        self.num = num

    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.num])
    
if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]

    print(week5.number_of_hits(my_numbers))