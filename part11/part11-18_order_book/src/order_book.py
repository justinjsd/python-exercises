# Write your solution here:

class Task:
    # Unique Task increments by 1 for each Programmer
    tasks = 0

    def __init__(self, description, programmer, workload, finished = "NOT FINISHED"):
        self.description = description
        self.workload = workload
        self.programmer = programmer
        self.finished = finished
        Task.tasks += 1
        self.id = Task.tasks

    def mark_finished(self):
        self.finished = "FINISHED"

    def is_finished(self):
        return self.finished == "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"
    
class OrderBook:
    def __init__(self):
        self.tasks = []
        self.programmers_names = []

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.tasks.append(task)
        self.programmers_names.append(programmer)

    def all_orders(self):
        return self.tasks
    
    def programmers(self):
        return list(set(self.programmers_names))
    
    def mark_finished(self, id: int):
        i = 0
        for task in self.tasks:
            if task.id == id:
                task.finished = "FINISHED"
                i = 1
        if i == 0:
            raise ValueError

    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished() == True]
    
    def unfinished_orders(self):
        return [task for task in self.tasks if task.is_finished() == False]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f'No such {programmer} exists')
        tasks = [task for task in self.tasks if task.programmer == programmer]
        finished = 0
        unfinished = 0
        finished_workload = 0
        unfinished_workload = 0
        for task in tasks:
            if task.is_finished():
                finished += 1
                finished_workload += task.workload
            else:
                unfinished += 1
                unfinished_workload += task.workload
        return (finished, unfinished, finished_workload, unfinished_workload)

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)