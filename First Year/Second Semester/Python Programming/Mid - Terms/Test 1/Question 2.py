# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 10:39:15 2024

@author: Michael.Agonsi
"""

from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Countdown:
    target_datetime:datetime

    @property
    def time_left(self):
        current_datetime = datetime.now()
        TF = current_datetime - self.target_datetime
        if current_datetime > self.target_datetime:
            if TF.days > 0:
                timeleft = timedelta(hours=TF.seconds/3600)
                return '-{} days , {}'.format(TF.days, timeleft)
            else:
                timeleft = timedelta(hours=TF.seconds / 3600)
                return '-{}'.format(timeleft)
        elif current_datetime < self.target_datetime:
            if TF.days > 0:
                timeleft = timedelta(hours=TF.seconds/3600)
                return '{} days , {}'.format(TF.days, timeleft)
            else:
                timeleft = timedelta(hours=TF.seconds / 3600)
                return '{}'.format(timeleft)
    @property
    def is_expired(self):
        if self.target_datetime > datetime.now():
            return True
        else:
            return False
if __name__ == '__main__':
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    hour = int(input('Enter a hour: '))
    minute = int(input('Enter a minute: '))
    print()
    Count = Countdown(datetime(year, month, day, hour, minute))

    print('Time Left: ', Count.time_left)
    print('Expired:', Count.is_expired)















