#her dosya  bir modüldür.
#pythonda built-in bulunn modüller
#local modüller ( kendi proje dosyalarım)
#3.taraf kütüphaneler


from math import sqrt as karekok , pi #sadece ikisini import et demek 
#from inheritance import Car
import requests
#alias -> takma ad
#print(math.sqrt(25))
#sqrt ın takma adını karekok yaptık.
print(karekok(25))
#print(math.pi)
print(pi)

#c1 = Car("hyundai")
#c1.start()

response = requests.get("https://google.com")
print(response.status_code)