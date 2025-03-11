#Kullanıcıdan bir sayı alıp, bu sayının faktöriyelini hesaplayan bir program yazın.
#Örnek: 5! = 5 * 4 * 3 * 2 * 1 = 120
n=int(input("bir sayi giriniz:"))
def faktoriyel(x):
    sonuc=1
    for i in range(1,x+1):
        sonuc*=i
    return sonuc

print(f"{n} sayısının faktoriyel sonucu: {faktoriyel(n)}")
