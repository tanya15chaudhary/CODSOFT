class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('To-Do List:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('Invalid task index.')

def main():
    todo_list = ToDoList()

    while True:
        print('\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit')
        choice = input('Enter your choice (1/2/3/4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_index = int(input('Enter the index of the task to mark as completed: '))
            todo_list.complete_task(task_index)
        elif choice == '4':
            print('Exiting the to-do list program. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a valid option.')

if __name__ == "__main__":
    main()
