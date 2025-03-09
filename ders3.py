#sınıflar => classlar
#modules
#paket yönetimi
#self => this

class Human:
    def talk(self):
        print("Human is talking..")
    def walk(self):
        print("Human is walking")


class Human:
    def talk(self,sentence):
        print(f"Human: {sentence}")
    def walk(self):
        print("Human is walking")

class Human:
    name = "Melis"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

class Human:
    #built-in #constructor #initalize 
    def __init__(self,name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")
    


#instance => örnek
human1 = Human()
human1.name = "Melis"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Melis")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")
