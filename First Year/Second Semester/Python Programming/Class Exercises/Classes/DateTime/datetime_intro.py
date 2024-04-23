from datetime import datetime, date, time, timedelta

# Simple examples
date_today = date.today()
print(date_today)

datetime_now = datetime.now()
print(datetime_now)

# Constructors
# date(year, month, day)
# time([hour] [,min] [,sec] [,microsec])
# datetime(year, month, day [,hour] [,min] [,sec] [,microsec])

halloween = date(2024, 10, 31)
print('\n', halloween)
print(type(halloween))

meeting = time(14, 30)
print('\n', meeting)
print(type(meeting))

appointment = datetime(2024, 10, 28, 14, 30)
print('\n', appointment)
print(type(appointment))

appointment = datetime(2024, 10, 28, 14, 30, 48, 345678)
print('\n', appointment)
print(type(appointment))

print(halloween.day)
print(halloween.month)
print(halloween.year)
print()
print(appointment.hour)
print(appointment.minute)
print(appointment.second)
print(appointment.microsecond)
print()

halloween = ('10/31/2024')
american_halloween = datetime.strptime(halloween, '%m/%d/%Y')
print(american_halloween)
print()
halloween = ('10/31/2024 22:30')
american_halloween = datetime.strptime(halloween, '%m/%d/%Y %H:%M')
print(american_halloween)
print()
halloween = ('10/31/2024 22:48')
american_halloween = datetime.strptime(halloween, '%m/%d/%Y %H:%M')
print(f'{american_halloween: %B %d, %I:%M %p}')
print()
halloween = ('10*31,2024 22:30')
american_halloween = datetime.strptime(halloween, '%m*%d,%Y %H:%M')
print(american_halloween)
print()
print(f'{american_halloween:%c}')
print()
custom_format = '%m*%d-%Y'
print(f'{american_halloween:{custom_format}}')

timedelta_example = american_halloween - appointment
print()
print(timedelta_example)
print(type(timedelta_example))
print()
# Constructor for time delta
# timedelta([days] [,seconds] [,microseconds] [,milliseconds] [,minutes], [,hours] [,weeks])
time_span = timedelta(weeks=2, days=3, hours=8, minutes=10)
print(time_span)
print()
three_weeks_ago = datetime.now() - timedelta(weeks=3)
print(three_weeks_ago)