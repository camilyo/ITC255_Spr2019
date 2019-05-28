class Payment():
    def __init__(self, calculateTotal):
        self.calculateTotal=calculateTotal
    
    def __str__(self):
        self.calculateTotal=round(self.calculateTotal,2)
        output="Your total is " + str(self.calculateTotal)
        return output