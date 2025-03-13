#Bir liste içindeki tekrar eden elemanları kaldıran bir program yazın.
liste=input("listeyi girin (elemanları boşlukla ayırın):").split()
benzersiz_liste= list(set(liste))
print("tekrar eden elemanlar kaldırıldı:",benzersiz_liste)