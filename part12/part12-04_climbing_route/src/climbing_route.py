class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def by_length(route: ClimbingRoute):
    return route.length

def by_difficulty(route: ClimbingRoute):
    return (route.grade, route.length)

def sort_by_length(routes: list):
    return sorted(routes, key = by_length, reverse=True)

def sort_by_difficulty(routes: list):
    return sorted(routes, key = by_difficulty, reverse=True)

if __name__ == "__main__":
    # r1 = ClimbingRoute("Edge", 38, "6A+")
    # r2 = ClimbingRoute("Smooth operator", 11, "7A")
    # r3 = ClimbingRoute("Synchro", 14, "8C+")
    # r4 = ClimbingRoute("Small steps", 12, "6A+")

    # routes = [r1, r2, r3, r4]

    # for route in sort_by_length(routes):
    #     print(route)

    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]
    for route in sort_by_difficulty(routes):
        print(route)