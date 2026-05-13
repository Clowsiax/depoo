from ogrenci import Ogrenci


class NotSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ad, soyad, numara):
        ogrenci = Ogrenci(ad, soyad, numara)
        self.ogrenciler.append(ogrenci)
        print("\nÖğrenci başarıyla eklendi.")

    def ogrenci_bul(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == numara:
                return ogrenci
        return None

    def not_gir(self, numara, vize, final):
        ogrenci = self.ogrenci_bul(numara)

        if ogrenci is None:
            print("\nÖğrenci bulunamadı.")
        else:
            ogrenci.not_gir(vize, final)
            print("\nNotlar başarıyla kaydedildi.")

    def ogrencileri_listele(self):
        if len(self.ogrenciler) == 0:
            print("\nSistemde kayıtlı öğrenci yok.")
        else:
            for ogrenci in self.ogrenciler:
                ogrenci.bilgi_goster()