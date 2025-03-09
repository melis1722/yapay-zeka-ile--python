#python ödev 4
#Kullanıcıdan adını, yaşını ve doğum yılını alarak ekrana aşağıdaki gibi yazdıran bir Python programı yazın:
#Merhaba Ali! 25 yaşındasın ve 1998 yılında doğmuşsun.

isim = input("isminizi giriniz:")
yas = int(input("yaşınızı giriniz:"))
dogum_yili = int(input("doğum yılınızı giriniz:"))

print(f"Merhaba {isim} !")

print(f"{yas} yaşındasın ve {dogum_yili} yılında doğmuşsun.")