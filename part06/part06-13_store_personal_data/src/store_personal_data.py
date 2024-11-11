# Write your solution here

def store_personal_data(person: tuple):
    with open("people.csv", "a") as people:
        person_data = []
        person_data.append(person[0])
        person_data.append(str(person[1]))
        person_data.append(str(person[2]))
        line = ";".join(person_data)+"\n"
        people.write(f"{line}")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
    store_personal_data(("Justin Paulson", 37, 175.5))