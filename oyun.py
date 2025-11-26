while True:  # tekrar oynama döngüsü
    tahmin_sayisi = 0
    sayi = random.randint(1, 100)
    tahmin = None

    print("1 ile 100 arasında bir sayı tuttum. Tahmin et!")

    while tahmin != sayi:
        tahmin = int(input("Tahmininiz: "))
        tahmin_sayisi += 1

        if tahmin < sayi:
            print("Daha büyük bir sayı söyle.")
        elif tahmin > sayi:
            print("Daha küçük bir sayı söyle.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede bildiniz.")
            break  # doğru tahmin olunca iç döngüden çık

    # Tekrar oynama sorusu
    tekrar = input("Tekrar oynamak ister misiniz? (E/H): ")
    if tekrar.lower() != "e":
        print("Oyun kapatılıyor...")
        break  # dış döngüyü kır, oyun tamamen biter
