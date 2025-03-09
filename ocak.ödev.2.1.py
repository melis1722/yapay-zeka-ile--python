#Kullanıcının notunu alarak aşağıdaki not sistemine göre harf notunu hesaplayın:
#90-100 -> A
#80-89  -> B
#70-79  -> C
#60-69  -> D
#0-59   -> F

not_bilgisi = int(input("Lütfen notunuzu giriniz:"))

if not_bilgisi <= 59:
    print("Harf notunuz F")
elif not_bilgisi <= 60 :
    print("Harf notunuz D")
elif not_bilgisi <= 79:
    print("Harf notunuz C")
elif not_bilgisi <= 89 :
    print("Harf notunuz B")
elif not_bilgisi <= 100:
    print("Harf notunuz A")
    