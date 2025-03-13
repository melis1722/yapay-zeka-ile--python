#Kullanıcıdan aldığı kelimeleri bir listeye ekleyerek ters sıralayan bir program yazın.

kelimeler=[]

while True:
    kelime=input("bir kelime giriniz:(çıkmak için quit yazınız):")

    if kelime.lower() == 'quit':
        break
    kelimeler.append(kelime)

kelimeler.sort(reverse=True)

print("ters sıralanmış kelimeler:",kelimeler)