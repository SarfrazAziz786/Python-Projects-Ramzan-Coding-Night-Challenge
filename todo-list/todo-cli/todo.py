import click 
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):  # os file exist or not 
        return []
    with open(TODO_FILE, "r") as file:  # resources management with keyword
        return json.load(file)


def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4) #dump function get task and provide indentation for syntex json

@click.group() #ek function ko kisi dusre function me put krna decorator provide by click group name decorator
def cli():
    """Simple Todo List Manager"""  #doc string
    pass

@click.command()   
@click.argument("task") #decorate task from user 
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task" : task , "done" : False}) #bydefault done property false jab user task likhe ga tab true hoga
    save_tasks(tasks)  #save task k function ko  upar wala task name ka varible pass kiya
    click.echo(f"task added successfully : {task}") #echo is print function 








@click.command()

def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("no tasks found")
        return
    for index, task in enumerate(tasks,1): #loop every task with numbering
        status = "✅" if task ["done"] else "❌"
        click.echo(f"{index}, {task ['task']} [{status}]")


@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f" Task {task_number} marked as complete")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Remove Task: {remove_task} ")
    else:
        click.echo(f"Invalid task number")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()
    




    