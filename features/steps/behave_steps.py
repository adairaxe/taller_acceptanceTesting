# Importa las decoraciones de Behave
from behave import *

# Importa tu clase ToDoListManager desde el módulo correspondiente
from features.toDoList.toDo import ToDoListManager

# Escenario 1
@given('the to-do list is empty')
def step_empty_todo_list(context):
    context.todo_manager = ToDoListManager()

@when('the user adds a task "{name}"')
def step_add_task(context, name):
    context.todo_manager.add_task(name)

@then('the to-do list should contain "{name}"')
def step_check_task_added(context, name):
    tasks = context.todo_manager.tasks
    assert any(task['name'] == name for task in tasks.values())

# Escenario 2
@given('the to-do list contains tasks:')
def step_todo_list_with_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        name = row['Task']
        context.todo_manager.add_task(name)

@when('the user lists all tasks')
def step_list_all_tasks(context):
    context.output = context.todo_manager.list_tasks()

@then('the output should contain:')
def step_output_contains(context):
    expected_output = context.text.split('\n')
    actual_output = context.output.split('\n')

    print(f'Expected output:\n{expected_output}')
    print(f'Actual output:\n{actual_output}')

    for task in expected_output:
        assert task.strip() in actual_output, f'Task "{task}" not found in the output'

# Escenario 3
@when('the user marks task "{name}" as completed')
def step_mark_task_completed(context, name):
    tasks = context.todo_manager.tasks
    task_id = next(key for key, value in tasks.items() if value['name'] == name)
    context.todo_manager.mark_as_completed(task_id)

@then('the to-do list should show task "{name}" as completed')
def step_check_task_completed(context, name):
    tasks = context.todo_manager.tasks
    task = tasks.get(name)
    
    assert task is not None, f'Task "{name}" not found in the to-do list'
    assert task['status'] == 'Completed', f'Task "{name}" is not marked as completed'

# Escenario 4
@when('the user clears the to-do list')
def step_clear_todo_list(context):
    context.todo_manager.clear_todo_list()

@then('the to-do list should be empty')
def step_check_empty_todo_list(context):
    assert not context.todo_manager.tasks, 'To-do list is not empty'

@given('the to-do list contains tasks:')
def step_todo_list_with_tasks(context):
    context.todo_manager = ToDoListManager()
    for row in context.table:
        name = row['Task']
        description = row.get('Description', '')
        context.todo_manager.add_task(name)
        task_id = next(key for key, value in context.todo_manager.tasks.items() if value['name'] == name)
        context.todo_manager.change_task_description(task_id, description)

@when('the user changes the description of task "{name}" to "{new_description}"')
def step_change_task_description(context, name, new_description):
    tasks = context.todo_manager.tasks
    task_id = next(key for key, value in tasks.items() if value['name'] == name)
    context.todo_manager.change_task_description(task_id, new_description)

@then('the to-do list should show task "{name}" with description "{new_description}"')
def step_check_task_description(context, name, new_description):
    tasks = context.todo_manager.tasks
    task = tasks.get(name)
    
    assert task is not None, f'Task "{name}" not found in the to-do list'
    assert task['description'] == new_description, f'Description of task "{name}" does not match the expected description'

@when('the user performs a special action on task "{name}"')
def step_special_action_on_task(context, name):
    tasks = context.todo_manager.tasks
    task_id = next(key for key, value in tasks.items() if value['name'] == name)
    context.todo_manager.perform_special_action(task_id)

@then('the special action should have the desired effect on task "{name}"')
def step_check_special_action(context, name):
    tasks = context.todo_manager.tasks
    task = tasks.get(name)
    
    assert task is not None, f'Task "{name}" not found in the to-do list'
    # Implementa la lógica específica de verificación de tu acción inventada aquí
