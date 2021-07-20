from currency import Currency

class Agent:
    __id_counter = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.account = Currency()
        self.operations = []
        self.corrections = []

    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            self.__id = self.__id_counter
            type(self).__id_counter += 1
            return self.__id
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Agent):
            return self.id == o.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __str__(self):
        return "<Agent with ID=" + str(self.id) + " and name " + str(self.name) + ">"