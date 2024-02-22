class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.secondes = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self.__hours = value
        else:
            raise ValueError("Invalid value for hours")

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self.__minutes = value
        else:
            raise ValueError("Invalid value for minutes")

    @property
    def secondes(self):
        return self.__secondes

    @secondes.setter
    def secondes(self, value):
        if 0 <= value <= 59:
            self.__secondes = value
        else:
            raise ValueError("")
