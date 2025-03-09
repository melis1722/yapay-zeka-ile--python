#Kullanıcıdan iki sayı alarak bu sayıların toplamını, farkını, çarpımını ve bölümünü ekrana yazdırın
sayi1=int(input("birinci sayiyi giriniz:"))
sayi2=int(input("ikinci sayiyi giriniz:"))
işlem=input("+,-,*,/ işlerinden birini seçiniz.")

if işlem == "+" :
    print(f"{sayi1}+{sayi2}={sayi1+sayi2}")
elif işlem == "-" :
    print(f"{sayi1} - {sayi2}={sayi1-sayi2}")
elif işlem == "*" :
    print(f"{sayi1}*{sayi2}={sayi1*sayi2}")
elif işlem == "/":
        if işlem != 0 :
            print(f"{sayi1}/{sayi2}={sayi1/sayi2}")
        else:
            print("sıfır için bölme işlemi gerçekleştirelemez.")
else:
    print("işlem geçersiz.")