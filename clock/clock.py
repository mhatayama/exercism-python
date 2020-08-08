from math import floor 

class Clock:
    def __init__(self, hour, minute):
        self.minutes = hour * 60 + minute

    def __repr__(self):
        hour = floor(self.minutes / 60) % 24
        minute = self.minutes % 60
        return f'{hour:02}:{minute:02}'

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
