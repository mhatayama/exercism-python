from math import floor


class Clock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

    def __init__(self, hour, minute):
        self.minutes = (hour * self.MINUTES_PER_HOUR +
                        minute) % self.MINUTES_PER_DAY

    def __repr__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)

    @property
    def hour(self):
        return floor(self.minutes / self.MINUTES_PER_HOUR) % self.HOURS_PER_DAY

    @property
    def minute(self):
        return self.minutes % self.MINUTES_PER_HOUR
