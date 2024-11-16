# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name}"

class Room:
    def __init__(self):
        self.persons = []
        
    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
        
    def print_contents(self):
        num_of_persons = len(self.persons)
        combined_height = 0
        for person in self.persons:
            combined_height += person.height 
        print(f"There are {num_of_persons} persons in the room, and their combined height is {combined_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height})")     

    def shortest(self):
        if self.is_empty() == True:
            return None
        shortest = self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
               shortest = person
        return shortest
    
    def remove_shortest(self):
        if self.is_empty() == True:
            return None
        shortest = self.shortest()
        shortest_index = self.persons.index(shortest)
        return self.persons.pop(shortest_index)

if __name__ == "__main__":
    # Part 1
    room1 = Room()
    print("Is the room empty?", room1.is_empty())
    room1.add(Person("Lea", 183))
    room1.add(Person("Kenya", 172))
    room1.add(Person("Ally", 166))
    room1.add(Person("Nina", 162))
    room1.add(Person("Dorothy", 155))
    print("Is the room empty?", room1.is_empty())
    room1.print_contents()

    # Part 2
    room2 = Room()

    print("Is the room empty?", room2.is_empty())
    print("Shortest:", room2.shortest())

    room2.add(Person("Lea", 183))
    room2.add(Person("Kenya", 172))
    room2.add(Person("Nina", 162))
    room2.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room2.is_empty())
    print("Shortest:", room2.shortest())

    print()

    room2.print_contents()

    # Part 3
    room3 = Room()

    room3.add(Person("Lea", 183))
    room3.add(Person("Kenya", 172))
    room3.add(Person("Nina", 162))
    room3.add(Person("Ally", 166))
    room3.print_contents()

    print()

    removed = room3.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room3.print_contents()