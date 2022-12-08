import argparse
import datetime

class Task:
  def __init__(self, title, due_date):
    self.title = title
    self.due_date = due_date
    self.is_complete = False
class TaskManager:
  # Other methods...

  def mark_complete(self, task_title):
    # Find the task with the given title
    try:
      task = next(task for task in self.tasks if task.title == task_title)
    except StopIteration:
      # The task does not exist
      print(f"Task '{task_title}' does not exist.")
      return

    # Mark the task as complete
    task.is_complete = True
# Define command-line arguments
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

# Add a new task
parser_add = subparsers.add_parser('add')
parser_add.add_argument('title', help='the title of the task')
parser_add.add_argument('due_date', help='the due date of the task')

# List all the tasks
parser_list = subparsers.add_parser('list')

# Mark a task as complete
parser_complete = subparsers.add_parser('complete')
parser_complete.add_argument('title', help='the title of the task')

# Parse the command-line arguments
args = parser.parse_args()

# Create a task manager
task_manager = TaskManager()

# Handle the different commands
if args.command == 'add':
  # Parse the due date
  due_date = datetime.datetime.strptime(args.due_date, '%Y-%m-%d %H:%M')

  # Create a new task
  task = Task(args.title, due_date)

  # Add the task to the task manager
  task_manager.add_task(task)

elif args.command == 'list':
  # List the tasks
  task_manager.list_tasks()

elif args.command == 'complete':
  # Mark the task as complete
  task_manager.mark_complete(args.title)
