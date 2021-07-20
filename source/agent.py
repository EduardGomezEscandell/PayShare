from operation import Operation
from currency import Currency

class Agent:
    __id_counter = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.__balance = Currency()
        self.operations = set()
        self.corrections = set()
        
        self.balance_updated = False
        self.corrections_updated = False

    @property
    def id(self):
        try:
            return self.__id
        except AttributeError:
            self.__id = self.__id_counter
            type(self).__id_counter += 1
            return self.__id
    
    def operation_balance(self):
        if self.balance_updated:
            return self.__balance
        else:
            self.__balance = Currency()
            for op in self.operations:
                if self == op.payer:
                    self.__balance += op.value
                if self in op.consumers:
                    self.__balance -= op.value_per_agent()
            self.balance_updated = True
            return self.__balance

    def correction_balance(self):
        if self.corrections_updated:
            return self.__correction_balance
        else:
            self.__correction_balance = Currency()
            for op in self.corrections:
                if self == op.payer:
                    self.__correction_balance += op.value
                if self in op.consumers:
                    self.__correction_balance -= op.value_per_agent()
            self.corrections_updated = True
            return self.__correction_balance

    def net_balance(self):
        return self.operation_balance() + self.correction_balance()

    def append_operation(self, op : Operation) -> None:
        if self == op.payer or self in op.consumers:
            self.operations.add(op)
            self.balance_updated = False
    
    def append_correction(self, op : Operation) -> None:
        if self == op.payer or self in op.consumers:
            self.corrections.add(op)
            self.corrections_updated = False
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, Agent):
            return self.id == o.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __str__(self):
        return "<Agent with ID=" + str(self.id) + " and name " + str(self.name) + ">"