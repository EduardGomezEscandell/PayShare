from source.currency import Currency

class Operation:
    __id_counter = 0

    def __init__(self, book, payer, consumers : str, value : float, description : str):
        self.book = book
        self.payer = payer
        self.consumers = consumers
        self.value = Currency(value)
        self.description = description

    @classmethod
    def reset_id_counter(cls):
        """
        Dangerous method! Be sure no pre-existing operations exist.
        """
        cls.__id_counter = 0
    
    def value_per_consumer(self):
        return self.value / len(self.consumers)
    
    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            self.__id = self.__id_counter
            type(self).__id_counter += 1
            return self.__id
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Operation):
            return self.id == other.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __hash__(self) -> int:
        return self.id