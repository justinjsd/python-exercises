# Write your solution here:
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def set(self, hours: int, minutes: int):
        self.seconds = 0
        self.minutes = minutes
        self.hours = hours

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
                if self.hours == 24:
                    self.seconds = 0
                    self.minutes = 0
                    self.hours = 0

    def __str__(self):
        return f"{"{:02}".format(self.hours)}:{"{:02}".format(self.minutes)}:{"{:02}".format(self.seconds)}"

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)