# Write your solution here!
from statistics import mean

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.num_list = []

    def add_number(self, number:int):
        self.counter += 1
        self.num_list.append(number)

    def count_numbers(self):
        return self.counter
    
    def get_sum(self):
        return sum(self.num_list)
    
    def average(self):
        # return self.get_sum()/self.count_numbers()
        try:
            return float(mean(self.num_list))
        except:
            print("No Numbers to get the average of")
    
num  = 0
stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

print("Please type in integer numbers:")

while True:
    num = int(input())
    if num == -1:
        break
    stats.add_number(num)
    if num % 2 == 0:
        even_stats.add_number(num)
    else:
        odd_stats.add_number(num)

print("Numbers added:", stats.count_numbers())
print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even_stats.get_sum())
print("Sum of odd numbers:", odd_stats.get_sum())