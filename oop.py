#nesne yönelimli programlama
#object oriented programing

class Car():
 #   pass #içi boş bir fonk.
    def __init__(self):
        self.__model = model 
        print("yeni car üretildi.")

    def start(self):
        model = "toyota"
        print(f"{self.__model} araba başlatılıyor...")
    
    def increase_speed(self,amount):
        print(f"hız şu kadar arttırılıyor: {amount}")


    #getter-okuma
    def get_model(self):
        return self.__model
    #setter-yazma
    def set_model(self,model):
        if len(model) < 3:
            print("marka işlemi 3 haneden küçük olamaz.")
            return
        self.__model = model



car=Car("hyundai")  #instance
#car.model = "Hyundai" yerine
car.set_model("a") #yazılabilir
car.start()
car.increase_speed(50)

car1 = Car("honda") #ilgili classın yapıcı metodunu çağırır (canstructor)
#car1.model = "honda"
car1.start()

#__model classın içinde old için fonk dışındakileri çalıştırmaz.


