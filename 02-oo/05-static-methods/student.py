class Duration:
    def __init__(self, duration_in_sec) -> None:
        self.__duration_in_sec = duration_in_sec
    
    @staticmethod
    def from_seconds(amount):
        return Duration(duration_in_sec=amount)

    @staticmethod
    def from_minutes(amount):
        return Duration(duration_in_sec = amount * 60)
    
    @staticmethod
    def from_hours(amount):
        return Duration(duration_in_sec= amount * 3600)
    
    @property
    def seconds(self):
        return  self.__duration_in_sec
    
    @property
    def minutes(self):
        return self.__duration_in_sec / 60
    
    @property
    def hours(self):
        return self.__duration_in_sec / 3600