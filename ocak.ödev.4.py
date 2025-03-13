#Kullanıcıdan 5 adet sayı alarak bir listeye ekleyin ve bu listenin toplamını, ortalamasını, en büyük ve en küçük elemanını bulun.
list=[]
for i in range(5):
    sayi=int(input(f" {i+1} .sayi giriniz:"))
    list.append(sayi)
      
print("listedeki sayilar:",list)


top=print("listedeki sayilerin toplami:",sum(list))


ort=print("listedeki sayilarin ortalaması:",sum(list)/len(list)) 

en_kücük=min(list)
print("listedeki en küçük sayi:",en_kücük)

en_büyük=max(list)
print("listedeki en büyük sayi:",en_büyük)

  


    
    