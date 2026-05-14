class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.vize = None
        self.final = None

    def not_gir(self, vize, final):
        self.vize = vize
        self.final = final

    def ortalama_hesapla(self):
        if self.vize is None or self.final is None:
            return 0

        return round((self.vize * 0.4) + (self.final * 0.6), 2)

    def durum_hesapla(self):
        ortalama = self.ortalama_hesapla()

        if ortalama >= 50:
            return "Geçti"
        else:
            return "Kaldı"
