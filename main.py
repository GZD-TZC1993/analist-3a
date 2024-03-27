from student import Student
from teacher import Teacher

# Öğretmen sınıfından bir örnek oluşturalım
ogretmen = Teacher()

# Öğrenci bilgilerini ekleyelim
ogrenci1 = Student("Gözde", "Tuzcu", "96")
ogrenci1.katilim_durumu_ekle("Katıldı")
ogretmen.not_ekle(ogrenci1, 60, 85, 80)
ogrenci1.diger_bilgi_ekle("Doğum Tarihi", "01/01/2000")
ogrenci1.diger_bilgi_ekle("E-posta:", "tuzcu523@gmail.com")

ogrenci2 = Student("Kerim", "Göktürk", "34")
ogrenci2.katilim_durumu_ekle("Katıldı")
ogretmen.not_ekle(ogrenci2, 85, 95, 100)
ogrenci2.diger_bilgi_ekle("Doğum Tarihi", "01/01/2000")
ogrenci2.diger_bilgi_ekle("E-posta:", "kerim@gmail.com")

ogrenci3 = Student("Merve", "Kaya", "105")
ogrenci3.katilim_durumu_ekle("Katılmadı")
ogretmen.not_ekle(ogrenci3, 45, 70, 50)
ogrenci3.diger_bilgi_ekle("Doğum Tarihi", "01/01/2000")
ogrenci3.diger_bilgi_ekle("E-posta:", "merve@gmail.com")

ogretmen.ogrenci_bilgileri_goster()
