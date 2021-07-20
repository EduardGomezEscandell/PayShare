from operation import Operation
from currency import Currency

class Agent:
    __id_counter = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.__balance = Currency()
        self.operations = []
        self.corrections = []
        self.balance_updated = False

    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            self.__id = self.__id_counter
            type(self).__id_counter += 1
            return self.__id
    
    @property
    def balance(self):
        if self.balance_updated:
            return self.__balance
        else:
            self.__balance = Currency()
            for op in self.operations:
                if op.payer == self:
                    self.__balance += op.value
                else:
                    self.__balance -= op.value
            self.balance_updated = True
            return self.__balance

    def append_operation(self, op : Operation) -> bool:
        if self == op.payer or self in op.consumers:
            self.operations.append(op)
            self.balance_updated = False
            return True
        return False
    
    def append_correction(self, op : Operation) -> bool:
        if self == op.payer or self in op.consumers:
            self.corrections.append(op)
            return True
        return False
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Agent):
            return self.id == o.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __str__(self):
        return "<Agent with ID=" + str(self.id) + " and name " + str(self.name) + ">"