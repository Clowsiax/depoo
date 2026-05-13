from not_sistemi import NotSistemi


def menu_goster():
    print("\n===== ÖĞRENCİ NOT TAKİP SİSTEMİ =====")
    print("1- Öğrenci Ekle")
    print("2- Not Gir")
    print("3- Öğrencileri Listele")
    print("4- Çıkış")


def main():
    sistem = NotSistemi()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ")

        if secim == "1":
            ad = input("Öğrenci adı: ")
            soyad = input("Öğrenci soyadı: ")
            numara = input("Öğrenci numarası: ")

            sistem.ogrenci_ekle(ad, soyad, numara)

        elif secim == "2":
            numara = input("Öğrenci numarası: ")

            try:
                vize = float(input("Vize notu: "))
                final = float(input("Final notu: "))

                if vize < 0 or vize > 100 or final < 0 or final > 100:
                    print("\nNotlar 0 ile 100 arasında olmalıdır.")
                else:
                    sistem.not_gir(numara, vize, final)

            except ValueError:
                print("\nLütfen sayısal bir değer giriniz.")

        elif secim == "3":
            sistem.ogrencileri_listele()

        elif secim == "4":
            print("\nProgramdan çıkış yapılıyor...")
            break

        else:
            print("\nGeçersiz seçim yaptınız.")


if __name__ == "__main__":
    main()