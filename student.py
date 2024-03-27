class Student:
    def __init__(self, ad, soyad, ogrenci_no):
        self.ad = ad
        self.soyad = soyad
        self.ogrenci_no = ogrenci_no
        self.katilim_durumu = ""
        self.diger_bilgiler = {}

    def katilim_durumu_ekle(self, durum):
        self.katilim_durumu = durum

    def diger_bilgi_ekle(self, anahtar, deger):
        self.diger_bilgiler[anahtar] = deger
