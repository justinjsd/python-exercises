# Write your solution here
def oldest_person(people: list):
    i = 0
    min = 5000
    for i in range(len(people)):
        if people[i][1] < min:
            min = people[i][1]
            min_loc = i
    oldie = people[min_loc][0]
    return oldie

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))