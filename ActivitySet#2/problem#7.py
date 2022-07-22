class Menu:
    """fill in class definition here"""
    def __init__(self):
        self.orders = dict()
    
    def __add__(self, order):
        self.orders[order[0]] = order[1]
        return self
    
    def __str__(self):
        return "\n".join(" ".join((k, str(v))) for k, v in self.orders.items())

m = Menu()
m = m + ("idly", 10) + ("vada", 20)