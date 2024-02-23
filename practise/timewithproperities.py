
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError(f"Hour ({hour}) must be between 0 and 24")
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError(f"Minute ({minute}) must be between 0 and 59")
        self._minute = minute

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError(f"Second ({second}) must be between 0 and 59")
        self._second = second

    @property
    def time(self):
        return (self.hour, self.minute, self.second)

    @time.setter
    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return (f"Time(hour={self.hour}, minute={self.minute}, " +
                f"second={self._second})")

    def __str__(self):
        return (("12" if self.hour in (0, 12) else str(self.hour%12) +
                f":{self.minute:0 > 2} : {self._second: 0 > 2} " +
                (" AM" if self.hour < 12 else " PM")))



#wake_up = Time(6, 30, 0)
#wake_up.set_time(7, 45)
#wake_up = Time(7, 45, 0)
#print(wake_up.hour, wake_up.min)























