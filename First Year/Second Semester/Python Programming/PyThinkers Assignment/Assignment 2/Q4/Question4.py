from dataclasses import dataclass
from datetime import datetime
#import dataclass and datetime modules for proper functionality of program

@dataclass
class Event:
    """
    instantiates class named 'Event' having a name, location, start date, and end date attribute,
    and a method to calculate the difference between the start date and end date in days
    """
    name:str = ''
    location:str = ''
    start_date:datetime = None
    end_date:datetime = None

    def duration(self):
        #Calculates event duration in days
        diff = self.end_date - self.start_date
        return diff.days

@dataclass
class Conference(Event):
    """
    Instantiates a subclass of the Event superclass called 'Conference'  with an additional attendees attribute
    and a modified duration method to return the duration in hours instead of days.
    """
    attendees:int = 0

    def duration(self):
        #Properly calculates the duration of the conference in hours
        diff = (self.end_date - self.start_date)
        hours = diff.seconds // 3600
        hours2 = diff.days * 24
        hours = hours + hours2
        return hours

event = Event("Birthday Party", "New York", datetime(2023, 8, 25),
                                            datetime(2024, 8, 26))
conference = Conference("Tech Conference", "San Francisco", datetime(2023, 9,15),
                                                    datetime(2023, 9, 17), 500)

print("Event:")
print("Name:", event.name)
print("Location:", event.location)
print("Start Date:", event.start_date)
print("End Date:", event.end_date)
print("Duration (days):", event.duration())
print()
print("Conference:")
print("Name:", conference.name)
print("Location:", conference.location)
print("Start Date:", conference.start_date)
print("End Date:", conference.end_date)
print("Attendees:", conference.attendees)
print("Duration (hours):", conference.duration())

