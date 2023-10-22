class Car:
    def __init__(self, brand, model, year, color, engine_type, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_type = engine_type
        self.speed = speed

    def start_engine(self):
        print(f"{self.brand} {self.model} started the engine.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"The car changed color from {self.color} to {new_color}.")

car1 = Car("Ford", "Fusion", 2017, "Pearl", "Hybrid", "212 km/h")
print(f'car1 details: {car1.brand}, {car1.model}, {car1.year}, {car1.color}, {car1.engine_type}, {car1.speed}')

car2 = Car("MAN", "TG-range", 2000, "White", "Disel", "120 km/h")
print(f'car1 details: {car2.brand}, {car2.model}, {car2.year}, {car2.color}, {car2.engine_type}, {car2.speed}')

car3 = Car("Toyota", "Camry XV30", 2004, "Black", "5 gasoline", "225 km/h")
print(f'car1 details: {car3.brand}, {car3.model}, {car3.year}, {car3.color}, {car3.engine_type}, {car3.speed}')

car4 = Car("Tesla", "Model X", 2017, "Grey", "Electric", "250 km/h")
print(f'car1 details: {car4.brand}, {car4.model}, {car4.year}, {car4.color}, {car4.engine_type}, {car4.speed}')