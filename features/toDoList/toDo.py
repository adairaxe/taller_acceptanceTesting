class ToDoListManager:
    def __init__(self):
        self.tasks = {}
        self.task_id_counter = 1

    def add_task(self, name):
        task = {
            'name': name,
            'description': 'Description',
            'status': 'Incomplete'
        }
        self.tasks[self.task_id_counter] = task
        self.task_id_counter += 1
        print(f'Task "{name}" added to the to-do list.')

    def list_tasks(self):
        if not self.tasks:
            print("The to-do list is empty.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task.name}")

    def mark_as_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = 'Completed'
            print(f'Task {task_id} marked as completed.')
        else:
            print(f'Task {task_id} not found.')

    def clear_todo_list(self):
        self.tasks = {}
        self.task_id_counter = 1
        print('To-do list cleared.')

    def change_task_description(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id]['description'] = new_description
            print(f'Description of task {task_id} changed to "{new_description}".')
        else:
            print(f'Task {task_id} not found.')

    def perform_special_action(self, task_id):
        if task_id in self.tasks:
            # Implementa la lógica específica de tu acción inventada aquí
            print(f'Special action performed on task {task_id}.')
        else:
            print(f'Task {task_id} not found.')