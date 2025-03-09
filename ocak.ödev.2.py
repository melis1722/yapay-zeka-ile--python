#Kullanıcının girdiği bir sayının tek mi çift mi olduğunu bulan bir Python programı yazın.
sayi=int(input("Lütfen bir sayi giriniz:"))

if sayi % 2 == 0 :
    print("Girdiğiniz sayi çifttir.")
else:
    print("Girdiğiniz sayi tektir.")