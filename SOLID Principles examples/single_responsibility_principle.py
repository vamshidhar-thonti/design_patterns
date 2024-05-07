# This violates the SRP as the ToDoList is performing task management, presentation and creation/deletion.

class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)
    
    def display_task(self):
        for task in self.tasks:
            print(task)
    
    def input_task(self):
        task = input("Enter a task: ")
        self.add_task(task)
    
    def remove_task(self):
        task = input("Enter the task to remove: ")
        self.delete_task(task)


# To fix it we can do as below
class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

class TaskPresenter:
    @staticmethod
    def display_task(tasks):
        for task in tasks:
            print(task)

class TaskInput:
    @staticmethod
    def input_task():
        return input("Enter a task: ")
    
    @staticmethod
    def remove_task():
        return input("Enter the task to remove: ")