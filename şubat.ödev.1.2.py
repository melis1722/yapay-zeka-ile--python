#Kullanıcının girdiği bir kelimenin palindrom olup olmadığını kontrol eden bir fonksiyon yazın.
#Örnek: "kek" -> palindrom, "masa" -> değil

def palindrom(kelime):
    if kelime.lower()== kelime.lower()[::-1]:
        return "palindrom"
    else:
        return "palindrom değil"
    
print(palindrom("kek"))
print(palindrom("masa"))
