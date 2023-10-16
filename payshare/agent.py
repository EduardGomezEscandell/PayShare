from payshare.localization import Localization
from payshare.operation import Operation
from payshare.currency import Currency

class Agent:
    __id_counter: int = 0
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.__balance: Currency = Currency()
        self.operations: set[Operation] = set()
        self.corrections: set[Operation] = set()
        
        self.balance_updated: bool= False
        self.corrections_updated: bool = False
    
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
    
    def operation_balance(self) -> Currency:
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

    def correction_balance(self) -> Currency:
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

    def net_balance(self) -> Currency:
        return self.operation_balance() + self.correction_balance()

    def append_operation(self, op : Operation) -> None:
        if self == op.payer or self in op.consumers:
            self.operations.add(op)
            self.balance_updated = False
    
    def append_correction(self, op : Operation) -> None:
        if self == op.payer or self in op.consumers:
            self.corrections.add(op)
            self.corrections_updated = False
    
    def report(self, loc: Localization = None) -> str:
        if loc is None:
            loc = Localization()
        report: str = loc["agent_report"]
        report = report.replace("$NAME", self.name)
        
        # Operations
        number_width = 8
        payed_for = []
        benefited_from = []
        
        for op in self.operations:
            if self == op.payer:
                payed_for.append(op)
            if self in op.consumers:
                benefited_from.append(op)
         
        buffer = ""
        if len(payed_for) == 0:
            buffer += "  (" + loc["no_operation"] + ")\n"
        for op in payed_for:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            buffer += "  " + amount + " " + Currency.symbol +" : " + op.description + "\n"
        
        report = report.replace("$OPERATIONS_PAYED", buffer)
        
        buffer = ""
        total = Currency(0)
        if len(benefited_from) == 0:
            buffer += "  (" + loc["no_operation"] + ")\n"
        for op in benefited_from:
            total += op.value_per_consumer()
            amount = str(op.value_per_consumer())
            amount = " " * (number_width - len(amount)) + amount
            buffer += "  " + amount + " " + Currency.symbol +" : " + op.description + "\n"
        report = report.replace("$OPERATIONS_CONSUMED", buffer)
        

        buffer = str(self.operation_balance()) + " " + Currency.symbol
        report = report.replace("$OPERATION_BALANCE", buffer)
        
        # Corrections
        payed_for = []
        benefited_from = []
        
        for op in self.corrections:
            if self == op.payer:
                if op.value < Currency(0,1):
                    continue
                payed_for.append(op)
            if self in op.consumers:
                if op.value < Currency(0,1):
                    continue
                benefited_from.append(op)
        
        buffer = ""
        if len(payed_for) == 0:
            buffer += "  (" + loc["no_operation"] + ")\n"
        for op in payed_for:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            buffer += "  " + amount + " " + Currency.symbol + " " + loc["to"] + " " +op.consumers[0].name + "\n"
        report = report.replace("$CORRECTIONS_TO_PAY", buffer).replace("$TOTAL_COST", f"{total} {Currency.symbol}")

        buffer = ""
        if len(benefited_from) == 0:
            buffer += "  (" + loc["no_operation"] + ")\n"
        for op in benefited_from:
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            buffer += "  " + amount + " " + Currency.symbol + " " + loc["from"] + " " + op.payer.name + "\n"
        report = report.replace("$CORRECTIONS_TO_GET", buffer)

        return report

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Agent):
            return self.id == o.id
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
    
    def __str__(self) -> str:
        return "<Agent with ID=" + str(self.id) + " and name " + str(self.name) + ">"