class MusicalNote:
    def __init__(self, name, pitch) -> None:
        self.__name = name
        self.__pitch = pitch
    
    @property
    def name(self):
        return self.__name
    
    @property
    def pitch(self):
        return self.__pitch
    