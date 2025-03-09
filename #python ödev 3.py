#python ödev 3
metin = input("Lütfen yazmak istediğiniz metni giriniz:")

with open("dosya.txt","w") as dosya:
    dosya.write(metin)
print("Dosyadaki içerik:")
with open ("dosya.txt","r") as dosya:
    dosya_icerik=dosya.read()
    print(dosya_icerik)

print("farklı satır verisi giriniz:")
with open ("dosya.txt","a"):
    for i in range(3):
        satir=input(f"{i+1}.satırı girin:")
        dosya.write(satir + "\n")

print("dosyadaki satır satır içerik:")
with open ("dosya.txt","r") as dosya:
    for satir in dosya:
        print(satir.strip())  #satırdaki fazlalık boşlukları temizler