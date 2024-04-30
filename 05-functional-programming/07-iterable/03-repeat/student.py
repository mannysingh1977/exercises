class Repeat:
    def __init__(self, x):
        self.__x = x
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.__x