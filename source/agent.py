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
    
    @classmethod
    def reset_id_counter(cls):
        """
        Dangerous method! Be sure no pre-existing agents exist.
        """
        cls.__id_counter = 0

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
                    self.__balance -= op.value_per_consumer()
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
                    self.__correction_balance -= op.value_per_consumer()
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
    
    def report(self):
        report = ""
        report += "Report for " + self.name + "\n\n"
        number_width = 8
        # Operations
        payed_for = []
        benefited_from = []
        
        for op in self.operations:
            if self == op.payer:
                payed_for.append(op)
            if self in op.consumers:
                benefited_from.append(op)
         
        report += "You have payed for the following operations:\n"
        if len(payed_for) == 0:
            report += "  (nothing)\n"
        for op in payed_for:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            report += "  " + amount + " " + Currency.symbol +" : " + op.description + "\n"
        
        report += "You have benefited from the following operations:\n"
        if len(benefited_from) == 0:
            report += "  (nothing)\n"
        for op in benefited_from:
            amount = str(op.value_per_consumer())
            amount = " " * (number_width - len(amount)) + amount
            report += "  " + amount + " " + Currency.symbol +" : " + op.description + "\n"
        report += "This results in a balance of " + str(self.operation_balance()) + " " + Currency.symbol + "\n\n"
        
        # Corrections
        payed_for = []
        benefited_from = []
        
        for op in self.corrections:
            if self == op.payer:
                payed_for.append(op)
            if self in op.consumers:
                benefited_from.append(op)
        
        report += "In order to set the balance to zero you will pay:\n"
        if len(payed_for) == 0:
            report += "  (nothing)\n"
        for op in payed_for:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            report += "  " + amount + " " + Currency.symbol + " to " +op.consumers[0].name + "\n"

        report += "and you will receive:\n"
        if len(benefited_from) == 0:
            report += "  (nothing)\n"
        for op in benefited_from:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            report += "  " + amount + " " + Currency.symbol + " from " + op.payer.name + "\n"

        return report

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Agent):
            return self.id == o.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __str__(self):
        return "<Agent with ID=" + str(self.id) + " and name " + str(self.name) + ">"