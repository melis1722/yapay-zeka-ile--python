#Girilen iki sayının toplamını, farkını, çarpımını ve bölümünü bulan bir hesap makinesi fonksiyonu yazın

def hesap_makinesi(sayi1,sayi2):
    toplam = sayi1 + sayi2 
    fark = sayi1 - sayi2
    carpim = sayi1*sayi2

    if sayi2!=0:
        bolum = sayi1/sayi2
    else:
        bolum = "sıfıra bölme hatası!"

    return { 
        "toplam": toplam,
        "fark" : fark,
        "çarpım" : carpim ,
        "bölüm" : bolum
    }

sayi1 = float(input("birinci sayiyi giriniz:"))
sayi2 = float(input("ikinci sayiyi giriniz:"))

sonuclar = hesap_makinesi(sayi1,sayi2)
print("Toplam:", sonuclar["toplam"])
print("Fark:", sonuclar["fark"])
print("Çarpım:", sonuclar["çarpım"])
print("Bölüm:", sonuclar["bölüm"])