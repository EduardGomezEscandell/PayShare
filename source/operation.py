class Operation:
    def __init__(self, book, payer, consumers : str, value : float, description : str):
        self.book = book
        self.payer = payer
        self.consumers = consumers
        self.value = value
        self.description = description