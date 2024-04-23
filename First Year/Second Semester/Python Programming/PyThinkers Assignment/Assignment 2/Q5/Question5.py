from dataclasses import dataclass
from datetime import datetime, time, date, timedelta

@dataclass
class Task:
    """
    Instantiates a class called 'Task' with an attribute for the name of the task, a description of the task,
    and lastly the due date of the task. Also includes a method for detecting if the task is completed or pending
    based on the current date and time in comparison to the due date.
    """
    task_name:str = ''
    task_description:str = ''
    due_date:datetime = None

    def status(self):
        # Assesses whether the current datetime is past the proposed due date or not and returns the proper status.
        if self.due_date > datetime.now():
            return 'Pending'
        else:
            return 'Completed'

@dataclass
class Homework(Task):
    """
    Instantiates a subclass called 'Homework' of the Task superclass. This subclass has an additional attribute
    'subject' that describes the subject the homework is for (i.e. Math, English, etc.) and a hidden private attribute
    '__task_status' that is used for determining whether the homework is in progress, completed, or not started in
    collaboration with the status method.
    """
    def __init__(self, task_name='', task_description='', due_date=None, subject=''):
        Task.__init__(self, task_name, task_description, due_date)
        self.subject = subject
        self.__task_status = None

    def status(self):
        """
        Method for assessing whether the homework is in progress, not started, or Completed by comparing the current
        datetime to the proposed due date, using the __task_status attribute to properly store and access the value.
        """
        delta = self.due_date - datetime.now()
        if delta > timedelta(days=14):
            self.__task_status = 'Not started'
        elif delta <= timedelta(days=14) and delta > timedelta(days=0):
            self.__task_status = 'In progress'
        elif delta <= timedelta(days=0):
            self.__task_status = 'Completed'
        else:
            self.__task_status = 'Invalid'
        return self.__task_status

@dataclass
class Meeting(Task):
    """
    Instantiates a subclass of the Task superclass called 'Meeting' which incorporates an additional location attribute
    and modifies the status method to return 'Scheduled' if the meeting is scheduled in the future or 'Happened' if
    the due date has already passed.
    """
    location:str = ''

    def status(self):
        # Assesses whether the current datetime is past the proposed due date or not and returns the proper status.
        if self.due_date > datetime.now():
            return 'Scheduled'
        else:
            return 'Happened'


homework = Homework("Math Homework", "Complete exercises 1-5", datetime(2024,3, 13), "Math")
meeting = Meeting("Team Meeting", "Discuss project updates", datetime(2024,9, 20), "Office A")

print("Homework:")
print("Task Name:", homework.task_name)
print("Task Description:", homework.task_description)
print("Due Date:", homework.due_date)
print("Subject:", homework.subject)
print("Status:", homework.status())
print("\n")
print("Meeting:")
print("Task Name:", meeting.task_name)
print("Task Description:", meeting.task_description)
print("Due Date:", meeting.due_date)
print("Location:", meeting.location)
print("Status:", meeting.status())
