class Vehicle: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        return("{} {} {}").format(self.year, self.make, 
        self.model)
    
chrysler = Vehicle("Chrysler", "300", "2008")
nissan = Vehicle("Nissan", "Leaf", "2015")
bmw = Vehicle("BMW", "750", "2017")

print(chrysler.print_info())