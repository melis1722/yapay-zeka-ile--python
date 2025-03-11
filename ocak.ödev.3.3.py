#1’den 100’e kadar olan tüm asal sayıları bulan bir program yazın.

for sayi in range(2,101):
    asal=True
    for i in range(2,sayi):
        if sayi % i ==0:
            asal=False
            break
    if asal:
        print(sayi,end="")    
    