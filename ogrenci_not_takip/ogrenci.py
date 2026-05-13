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
            return None
        return (self.vize * 0.40) + (self.final * 0.60)

    def durum_hesapla(self):
        ortalama = self.ortalama_hesapla()

        if ortalama is None:
            return "Not girilmedi"

        if ortalama >= 50:
            return "Geçti"
        else:
            return "Kaldı"

    def bilgi_goster(self):
        ortalama = self.ortalama_hesapla()

        print("\n----- Öğrenci Bilgileri -----")
        print(f"Ad Soyad   : {self.ad} {self.soyad}")
        print(f"Numara     : {self.numara}")

        if ortalama is None:
            print("Vize       : Not girilmedi")
            print("Final      : Not girilmedi")
            print("Ortalama   : Hesaplanmadı")
            print("Durum      : Not girilmedi")
        else:
            print(f"Vize       : {self.vize}")
            print(f"Final      : {self.final}")
            print(f"Ortalama   : {ortalama}")
            print(f"Durum      : {self.durum_hesapla()}")