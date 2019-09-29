class Employee:
    def __init__(self, first, last, income):
        self.first = first.title()
        self.last = last.title()
        self.income = income

    def give_raise(self, amount=''):
        if amount:
            self.income += amount
        else:
            self.income += 5000

        
        
