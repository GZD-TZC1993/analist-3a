from student import Student

class Teacher:
    def __init__(self):
        self.ogrenciler = {}

    def not_ekle(self, ogrenci, vize_notu, final_notu, hoca_notu):
        ortalama = (((vize_notu * 0.4) + (final_notu * 0.6)) + hoca_notu) / 2
        if ortalama >= 90:
            kanaat_notu = "AA"
        elif ortalama >= 85:
            kanaat_notu = "BA"
        elif ortalama >= 80:
            kanaat_notu = "BB"
        elif ortalama >= 75:
            kanaat_notu = "CB"
        elif ortalama >= 70:
            kanaat_notu = "CC"
        elif ortalama >= 65:
            kanaat_notu = "DC"
        elif ortalama >= 60:
            kanaat_notu = "DD"
        elif ortalama >= 55:
            kanaat_notu = "FD"
        else:
            kanaat_notu = "FF"
        self.ogrenciler[ogrenci.ogrenci_no] = {'ad': ogrenci.ad, 'soyad': ogrenci.soyad, 'vize': vize_notu,'final': final_notu, 'ortalama': ortalama,
        'öğretmen_notu': hoca_notu, 'kanaat_notu': kanaat_notu,'katilim_durumu': ogrenci.katilim_durumu,'diger_bilgiler': ogrenci.diger_bilgiler}

    def ogrenci_bilgileri_goster(self):
        for ogrenci_no, bilgiler in self.ogrenciler.items():
            print(f"Öğrenci No: {ogrenci_no}")
            print(f"Ad: {bilgiler['ad']}")
            print(f"Soyad: {bilgiler['soyad']}")
            print(f"Vize: {bilgiler['vize']}")
            print(f"Final: {bilgiler['final']}")
            print(f"Hoca_notu: {bilgiler['öğretmen_notu']}")
            print(f"Ortalama: {bilgiler['ortalama']}")
            print(f"Kanaat Notu: {bilgiler['kanaat_notu']}")
            print(f"Katılım Durumu: {bilgiler['katilim_durumu']}")
            diger_bilgiler = bilgiler.get('diger_bilgiler')
            if diger_bilgiler:
                print("Diğer Bilgiler:")
                for anahtar, deger in diger_bilgiler.items():
                    print(f"- {anahtar}: {deger}")
            print()
