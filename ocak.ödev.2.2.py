#Kullanıcının yaşına göre hangi yaş grubunda olduğunu bulan bir program yazın:
#0-12 yaş: Çocuk
#13-19 yaş: Genç
#20-59 yaş: Yetişkin
#60 ve üzeri: Yaşlı

yas=int(input("Lütfen yaşınızı giriniz:"))

if yas <= 12 :
    print(f"{yas} yaşında çocuktur.")
elif yas <= 19:
    print(f"{yas} yaşında gençtir.")
elif yas <= 59:
    print(f"{yas} yaşında yetişkindir.")
elif yas >= 60 :
    print(f"{yas} yaşında yaşlıdır.")