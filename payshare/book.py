from payshare.currency import Currency
from payshare.operation import Operation
from payshare.agent import Agent
from payshare.localization import Localization
from typing import List, Tuple

class Book:
    def __init__(self):
        self.operations: List[Operation] = []
        self.corrections: List[Operation] = []
        self.agents: dict[str, Agent] = dict()

    def load_from_file(self, log_reader) -> None:
        log_reader.open()    
        while log_reader.next():
            pass
        log_reader.close()
    
    def new_operation(self, payer : str, consumers : list, value : float, description : str) -> Operation:
        _payer = self[payer]
        _consumers = [self[c] for c in consumers]
        new_operation = Operation(self, _payer, _consumers, value, description)
        self.operations.append(new_operation)

        for agent in _consumers + [_payer]:
            agent.append_operation(new_operation)

        return new_operation
    
    def __getitem__(self, name : str) -> Agent:
        _name = name.strip()
        if _name in self.agents:
            return self.agents[_name]
        new_agent = Agent(_name)
        self.agents[_name] = new_agent
        return new_agent
    
    def compute_corrections(self) -> None:
        agents = list(self.agents.values())

        agents.sort(key=lambda a : -a.net_balance())
        
        i_most_balance, i_least_balance = self.__find_most_and_least_balance(agents)

        while i_most_balance != i_least_balance:
            most_balance = agents[i_most_balance]
            least_balance = agents[i_least_balance]
            
            correction_value = min(most_balance.net_balance(), -least_balance.net_balance())

            new_correction = Operation(self, least_balance, [most_balance], correction_value, "Correction payment")

            self.corrections.append(new_correction)

            most_balance.append_correction(new_correction)
            least_balance.append_correction(new_correction)

            i_most_balance, i_least_balance = self.__find_most_and_least_balance(agents, i_most_balance, i_least_balance)

    def report(self, loc: Localization = None) -> str:
        if not loc:
            loc = Localization()
        report: str = loc["book_report"]
        
        buffer = ""
        number_width = 8
        for op in self.operations:
            if op.value < Currency(0,1):
                    continue
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            consumers = ", ".join([c.name for c in op.consumers])
            buffer += "  " + amount + " " + Currency.symbol + "\t" + op.payer.name + " -> " + consumers + " : " + op.description + "\n"
        
        report = report.replace("$OPERATIONS", buffer)

        buffer = ""
        for op in self.corrections:
            if op.value < Currency(0,1):
                    continue
            amount = str(op.value)
            amount = " " * (number_width - len(amount)) + amount
            consumers = ", ".join([c.name for c in op.consumers])
            buffer += "  " + amount + " " + Currency.symbol + "\t" + op.payer.name + " -> " + consumers + "\n"
        
        report = report.replace("$CORRECTIONS", buffer)

        return report

    @classmethod
    def __find_most_and_least_balance(cls, agents: List[Agent], begin=None, end=None) -> Tuple[int, int]:
        """
        Finds the agents with most positive and negative balances, ignoring those with zero balance.
        Searches only between begin and end.
        """
        if begin is None:
            begin = 0
        if end is None:
            end = len(agents)-1

        most_balance = agents[begin]
        least_balance = agents[end]
        
        while most_balance.net_balance() == 0:
            begin += 1
            most_balance = agents[begin]

            if begin == end:
                return begin, end

        while least_balance.net_balance() == 0:
            end -= 1
            least_balance = agents[end]
            
            if begin == end:
                return begin, end
        
        return begin, end
