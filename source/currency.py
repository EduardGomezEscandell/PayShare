class Currency:
    def __init__(self, units : float = 0, cents : float = 0) -> None:
        if self.__isnumber(units) and self.__isnumber(cents):
            self.value = units * 100 + cents
        elif isinstance(units, Currency):
            self.value = units.value
            if cents != 0:
                raise TypeError("Currency object only takes one argument when initialized from another currency object")
        else:
            raise TypeError("Currency object can only be initialized from integers, floats or other curency objects")
    
    def __neg__(self):
        return Currency(0, -self.value)

    def __add__(self, other : float):
        if isinstance(other, Currency):
            return Currency(0, self.value + other.value)
        else:
            return self + Currency(other.value)
    
    def __iadd__(self, other : float):
        if isinstance(other, Currency):
            self.value += other.value
        else:
            self += Currency(other)
        return self
    
    def __sub__(self, other : float):
        if isinstance(other, Currency):
            return Currency(0, self.value - other.value)
        else:
            return self - Currency(other.value)
    
    def __isub__(self, other : float):
        if isinstance(other, Currency):
            self.value -= other.value
        else:
            self -= Currency(other)
        return self
    
    def __mul__(self, other : float):
        if self.__isnumber(other):
            return Currency(0, self.value * other)
        raise TypeError("Curency can only be multiplied with integers and floats")
    
    def __imul__(self, other : float):
        if self.__isnumber(other):
            self.value = int(self.value * other)
            return self
        raise TypeError("Curency can only be multiplied with integers and floats")
    
    def __truediv__(self, other : float):
        if self.__isnumber(other):
            return Currency(0, self.value / other)
        raise TypeError("Curency can only be divided by integers and floats")

    def __itruediv__(self, other : float):
        if self.__isnumber(other):
            self.value = int(self.value / other)
            return self
        raise TypeError("Curency can only be divided by integers and floats")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Currency):
            return self.value == other.value
        else:
            return self == Currency(other)
    
    def __ne__(self, other: object) -> bool:
        return not self==other
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, Currency):
            return self.value > other.value
        else:
            return self > Currency(other)
    
    def __lt__(self, other: object) -> bool:
        if isinstance(other, Currency):
            return self.value < other.value
        else:
            return self < Currency(other)
    
    def __ge__(self, other: object) -> bool:
        if isinstance(other, Currency):
            return self.value >= other.value
        else:
            return self >= Currency(other)

    def __le__(self, other: object) -> bool:
        if isinstance(other, Currency):
            return self.value <= other.value
        else:
            return self <= Currency(other)    

    def __str__(self):
        units = str(int(self.value / 100))

        cents = str(int(self.value % 100))
        if len(cents) == 1:
            cents = "0"+cents

        return units + "." + cents

    @classmethod
    def __isnumber(cls, x):
        return isinstance(x, int) or isinstance(x, float)