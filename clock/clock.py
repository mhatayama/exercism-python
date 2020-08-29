from math import floor


class Clock:
    MINUTES_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

    def __init__(self, hour, minute):
        self.minutes = (hour * self.MINUTES_PER_HOUR +
                        minute) % self.MINUTES_PER_DAY

    def __repr__(self):
        return f'Clock(hour = {self.hour}, minute = {self.minute})'

    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self.minutes == other.minutes
        else:
            raise TypeError("Only Clock objects are allowed.")

    def __add__(self, other):
        if isinstance(other, Clock):
            return Clock(0, self.minute + other.minutes)
        elif isinstance(other, int):
            return Clock(0, self.minutes + other)
        else:
            raise TypeError("Only Clock objects or integers are allowed.")

    def __sub__(self, other):
        if isinstance(other, Clock):
            return Clock(0, self.minute - other.minutes)
        elif isinstance(other, int):
            return Clock(0, self.minutes - other)
        else:
            raise TypeError("Only Clock objects or integers are allowed.")

    @property
    def hour(self):
        return floor(self.minutes / self.MINUTES_PER_HOUR) % self.HOURS_PER_DAY

    @property
    def minute(self):
        return self.minutes % self.MINUTES_PER_HOUR
