import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    
    # 1 ile 100 arasında rastgele bir sayı seçilir
    gizli_sayi = random.randint(1, 100)
    
    # Tahmin sayacı
    tahmin_sayisi = 0
    
    while True:
        try:
            tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
            tahmin_sayisi += 1

            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
            elif tahmin < gizli_sayi:
                print("Daha büyük bir sayı deneyin.")
            elif tahmin > gizli_sayi:
                print("Daha küçük bir sayı deneyin.")
            else:
                print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahminde bulundunuz.")
                break
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

# Oyunu başlat
sayi_tahmin_oyunu()
