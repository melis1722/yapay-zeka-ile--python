class Vehicle():
    def __init__(self,model):
        self.model = model
    def start(self):
        print(f"{self.model} araç başlatılıyor..")

class Car(Vehicle):
    def start(self): #method -> polymorphism
        print(f"{self.model} araba başlatılıyor...")
    
class Truck(Vehicle):
    def load(self):
        print("yük yükleniyor...")


car = Car("hyundai")
car.start 
 
truck=Truck("scania")
truck.start()
truck.load()

#fonk içinde olan yani özelleştirilmiş olan çalışır.
