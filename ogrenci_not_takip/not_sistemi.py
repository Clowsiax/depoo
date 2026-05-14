from ogrenci import Ogrenci


class NotSistemi:
    def __init__(self):
        self.ogrenciler = []

    def ogrenci_ekle(self, ad, soyad, numara):
        ogrenci = Ogrenci(ad, soyad, numara)
        self.ogrenciler.append(ogrenci)

    def ogrenci_bul(self, numara):
        for ogrenci in self.ogrenciler:
            if ogrenci.numara == numara:
                return ogrenci

        return None

    def not_gir(self, numara, vize, final):
        ogrenci = self.ogrenci_bul(numara)

        if ogrenci:
            ogrenci.not_gir(vize, final)
            return True

        return False

    def ogrencileri_getir(self):
        return self.ogrenciler
