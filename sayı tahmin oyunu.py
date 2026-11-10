import random
alt_sınır=int(input("Rastgele üretilecek sayının alt sınırını giriniz : "))
üst_sınır=int(input("Rastgele üretilecek sayının üst sınırını giriniz : "))
numara=random.randint(alt_sınır,üst_sınır)
deneme=0
while True:
    tahmin=int(input("alt sınırınız ile üst sınırınız arasında bir sayı tahmin ediniz : "))
    deneme+=1
    if tahmin==numara:
        print("*****************Tebrikler ! Sayıyı doğru tahmin ettiniz.************************" )
        print("----->Tahmin etme sayacınız : ",deneme)
        print("--------->Bulduğunuz sayı : ",numara)
        break
    elif tahmin<numara:
        print("Daha büyük bir sayı tahmin ediniz.")
        
    elif tahmin>numara:
        print("Daha küçük bir sayı tahmin ediniz.")
        
        
#### tahminlere sınırlar dahildir. 
