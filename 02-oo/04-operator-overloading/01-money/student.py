class Money:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies")
        return Money(self.amount + other.amount, self.currency)
        
    def __sub__(self, other):
        if self.currency != other.currency:
            raise RuntimeError("Mismatched currencies")
        return Money(self.amount - other.amount, self.currency)
        
    def __mul__(self, amount):
        return Money(self.amount * amount, self.currency)
    
    def __str__(self) -> str:
        return f"Money({self.amount}, {self.currency})"

money1 = Money(500, "EUR")
money2 = Money(200, "EUR")
print(money1.__add__(money2))
print(money1.__sub__(money2))
print(money1.__mul__(5))