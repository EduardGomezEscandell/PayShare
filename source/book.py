from operation import Operation
from agent import Agent

class Book:
    def __init__(self):
        self.operations = []
        self.corrections = []
        self.agents = dict()
    
    def new_operation(self, payer : str, consumers : list, value : float, description : str):
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