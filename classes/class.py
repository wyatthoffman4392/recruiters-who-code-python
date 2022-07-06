class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def get_car_info(self):
        print(f'{self.year} {self.make} {self.model}')

my_car = Car(1998, 'Honda', 'Civic')
my_car.get_car_info()

my_car = Car(2001, 'Toyota', 'Camry')
my_car.get_car_info()