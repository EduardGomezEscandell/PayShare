from book import Book

class LogReader:
    """
    Reads a tab-separated-values file with the following rules:
    - Lines starting with # are ignored
    - Empty lines are not allowed
    - Each non-ignored line is a distinct operation
    - There must be at least 3 colums:
        + Payer name.
        + Consumer names (separated by commas, non-tab whitespace is ignored).
        + Value of the transaction.
        + All remaining columns (if any) will be considered part of the description.
    """
    def __init__(self, book : Book, file_name : str) -> None:
        self.book = book
        self.file_name = file_name
        self.file = None
    
    def open(self):
        self.file = open(self.file_name, "r")
    
    def close(self):
        self.file.close()
        self.file = None
    
    def next(self):
        invalid_line = True
        while invalid_line:
            line = self.file.readline().strip()
            
            if len(line) == 0: # End of file
                return False

            invalid_line = line[0] == '#'
        
        data = line.split('\t')
        payer = data[0]
        consumers = data[1].split(',')
        value = float(data[2])
        
        if len(data) < 3:
            description = "Operation without description"
        else:
            description = "".join(data[3:])

        self.book.new_operation(payer, consumers, value, description)
        return True


