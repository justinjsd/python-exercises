# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
            if self.minutes == 60:
                self.minutes = 0

    def __str__(self):
        return f"{"{:02}".format(self.minutes)}:{"{:02}".format(self.seconds)}"

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(120):
        print(watch)
        watch.tick()