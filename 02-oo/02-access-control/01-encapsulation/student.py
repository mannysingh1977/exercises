class Wizard:
    def __init__(self, name):
        self.name = name
        self.__health = 65
        self.__mana = 45

    def get_mana(self):
        return self.__mana

    def get_health(self):
        return self.__health
