import tkinter as tk
import random

# Renk sabitlerini içe aktar
from renkler import *

# Oyun bölümlerini içe aktar
from veri import BOLUMLER


class CriminalCaseOyunu:
    def __init__(self, kok):

        # Ana pencereyi oluştur
        self.kok = kok

        # Pencere başlığı
        self.kok.title("🔍 Criminal Case: İstanbul Dosyaları")

        # Pencere boyutu
        self.kok.geometry("1280x780")

        # Arka plan rengi
        self.kok.configure(bg=BG)

        # Yeniden boyutlandırmaya izin ver
        self.kok.resizable(True, True)

        # Minimum pencere boyutu
        self.kok.minsize(1100, 700)

        
        # OYUN DURUM DEĞİŞKENLERİ
       

        # Aktif bölüm indexi
        self.bolum_idx = 0

        # Toplanan delillerin listesi
        self.envanter = []

        # Analiz edilen deliller
        self.analiz_edilenler = []

        # Mevcut bölüm skoru
        self.skor = 0

        # Toplam skor
        self.toplam_skor = 0

        # Her bölüm için yıldız sayısı
        self.bolum_yildizlari = [0, 0, 0]

        # Laboratuvar meşgul mü?
        self.lab_mesgul = False

       
        # UI ELEMAN REFERANSLARI
       

        # Skor etiketi
        self.skor_etiketi = None

        # Delil sayısı etiketi
        self.delil_sayisi_etiketi = None

        # Bilgi mesaj etiketi
        self.bilgi_etiketi = None

        # Envanter listesi
        self.envanter_listesi = None

        # Analiz sonuç etiketi
        self.analiz_etiketi = None

        # Olay yeri sahnesi canvası
        self.sahne_canvas = None

        # Ana çerçeve
        self.ana_cerceve = None

        # Başlangıç ekranını göster
        self.goster_baslik()

   
    # EKRAN TEMİZLEME
    

    def _temizle(self):

        # Eğer mevcut çerçeve varsa sil
        if self.ana_cerceve:
            self.ana_cerceve.destroy()

        # Yeni ana çerçeve oluştur
        self.ana_cerceve = tk.Frame(self.kok, bg=BG)

        # Çerçeveyi ekrana yerleştir
        self.ana_cerceve.pack(fill="both", expand=True)

   
    # NAVİGASYON METOTLARI
  

    def goster_baslik(self):

        # Ekranı temizle
        self._temizle()

        # Başlık ekranını aç
        from ekranlar.baslik import BaslikEkrani
        BaslikEkrani(self)

    def goster_bolum_giris(self):

        # Ekranı temizle
        self._temizle()

        # Bölüm değişkenlerini sıfırla
        self.envanter.clear()
        self.analiz_edilenler.clear()
        self.skor = 0
        self.lab_mesgul = False

        # Bölüm giriş ekranını aç
        from ekranlar.bolum_giris import BolumGirisEkrani
        BolumGirisEkrani(self)

    def goster_sorusturma(self):

        # Ekranı temizle
        self._temizle()

        # Soruşturma ekranını aç
        from ekranlar.sorusturma import SorusturmaEkrani
        SorusturmaEkrani(self)

    def goster_oyun_sonu(self):

        # Ekranı temizle
        self._temizle()

        # Oyun sonu ekranını aç
        from ekranlar.sonuc import OyunSonuEkrani
        OyunSonuEkrani(self)

    def sonraki_bolum(self):

        # Sonraki bölüme geç
        self.bolum_idx += 1

        # Bölüm giriş ekranını göster
        self.goster_bolum_giris()

    def yeniden_baslat(self):

        # Tüm oyun verilerini sıfırla
        self.bolum_idx = 0
        self.envanter = []
        self.analiz_edilenler = []
        self.skor = 0
        self.toplam_skor = 0
        self.bolum_yildizlari = [0, 0, 0]

        # Başlık ekranına dön
        self.goster_baslik()

    
    # OLAY YERİ İNCELEME
   

    def olay_yeri_incele(self):

        # Mevcut bölüm bilgilerini al
        bolum = BOLUMLER[self.bolum_idx]

        # Henüz bulunmayan delilleri filtrele
        kalanlar = [
            d for d in bolum["tum_deliller"]
            if d not in self.envanter
        ]

        # Eğer delil kalmadıysa kullanıcıyı bilgilendir
        if not kalanlar:
            self._bilgi_guncelle(
                "🔍 Olay yerinde toplanacak başka delil kalmadı!",
                YELLOW
            )
            return

        # Rastgele kaç delil bulunacağını belirle
        adet = random.randint(1, min(3, len(kalanlar)))

        # Rastgele delilleri seç
        bulunanlar = random.sample(kalanlar, adet)

        # Bulunan delilleri envantere ekle
        for delil in bulunanlar:
            self.envanter.append(delil)

            # Liste kutusuna ekle
            self.envanter_listesi.insert(
                tk.END,
                f"  {delil}"
            )

        # Delil sayısını güncelle
        self._delil_sayisi_guncelle()

        # Skora puan ekle
        self.skor_guncelle(adet * 10)

        # Bilgi mesajı göster
        self._bilgi_guncelle(
            f"🔎  Bulunan: {', '.join(bulunanlar)}",
            GREEN
        )

        # Kısa sahne efekti oluştur
        self._sahne_flas()

    def _sahne_flas(self):

        # Eğer canvas varsa efekt uygula
        if self.sahne_canvas:

            # Yeşil kenarlık yap
            self.sahne_canvas.configure(
                highlightbackground=GREEN,
                highlightthickness=3
            )

            # 300 ms sonra eski haline döndür
            self.kok.after(
                300,
                lambda: self.sahne_canvas.configure(
                    highlightbackground=BORDER,
                    highlightthickness=2
                )
            )

   
    # LABORATUVAR AÇMA
   

    def lab_ac(self):

        # Listeden seçili elemanı al
        secim = self.envanter_listesi.curselection()

        # Eğer seçim yoksa hata mesajı ver
        if not secim:
            self._bilgi_guncelle(
                "⚠️  Önce listeden bir delil seç!",
                RED
            )
            return

        # Laboratuvar doluysa kullanıcıyı beklet
        if self.lab_mesgul:
            self._bilgi_guncelle(
                "⚗️  Laboratuvar meşgul, lütfen bekle...",
                YELLOW
            )
            return

        # Seçilen delili al
        delil = self.envanter_listesi.get(secim[0]).strip()

        # Eğer daha önce analiz edildiyse
        if delil in self.analiz_edilenler:
            self._bilgi_guncelle(
                f"✅  '{delil}' zaten analiz edildi!",
                CYAN
            )
            return

        # Laboratuvarı meşgul yap
        self.lab_mesgul = True

        # Laboratuvar penceresini aç
        from ekranlar.lab import LaboratuvarPenceresi
        LaboratuvarPenceresi(self, delil)

    
    # SUÇLAMA
    

    def sucla(self, supheli_isim):

        # Suçlama popup ekranını aç
        from ekranlar.sonuc import SuclamaPopup
        SuclamaPopup(self, supheli_isim)

   
    # KARAR VERME
  

    def karar_ver(self, supheli):

        # Şüpheli suçlu mu?
        dogru = supheli["suclu"]

        # Eğer doğru kişiyi suçladıysa
        if dogru:

            # Analiz bonusu hesapla
            bonus = len(self.analiz_edilenler) * 20

            # Skor ekle
            self.skor += 200 + bonus

            # Toplam skoru güncelle
            self.toplam_skor += self.skor

            # Yıldız hesaplama
            yildiz = min(
                3,
                1
                + (len(self.analiz_edilenler) >= 3)
                + (
                    len(self.envanter)
                    >= BOLUMLER[self.bolum_idx]["min_delil"] + 2
                )
            )

            # Bölüm yıldızını kaydet
            self.bolum_yildizlari[self.bolum_idx] = yildiz

        else:

            # Yanlış suçlamada puan düş
            self.skor = max(0, self.skor - 50)

            # Toplam skoru güncelle
            self.toplam_skor += self.skor

            # Yıldız yok
            yildiz = 0

        # Ekranı temizle
        self._temizle()

        # Karar ekranını aç
        from ekranlar.sonuc import KararEkrani
        KararEkrani(self, supheli, dogru, yildiz)

   
    # NOTLARI DOSYAYA KAYDET
  

    def notlari_kaydet(self):

        # Kaydetme fonksiyonunu çağır
        from araclar.kaydet import dosya_kaydet

        # Dosya yolunu al
        yol = dosya_kaydet(self)

        # Başarılı mesajı göster
        self._bilgi_guncelle(
            f"💾  Kaydedildi: {yol}",
            GREEN
        )

    # UI GÜNCELLEME YARDIMCILARI
    

    def skor_guncelle(self, artis=0):

        # Skora puan ekle
        self.skor += artis

        # Skor etiketi varsa güncelle
        if self.skor_etiketi:
            self.skor_etiketi.configure(
                text=f"⭐ Skor: {self.skor}"
            )

    def _delil_sayisi_guncelle(self):

        # Bölüm bilgilerini al
        bolum = BOLUMLER[self.bolum_idx]

        # Toplanan delil sayısı
        n = len(self.envanter)

        # Gerekli minimum delil
        req = bolum["min_delil"]

        # Yeterli delil varsa yeşil, yoksa sarı
        renk = GREEN if n >= req else YELLOW

        # Etiketi güncelle
        if self.delil_sayisi_etiketi:
            self.delil_sayisi_etiketi.configure(
                text=f"🗂 Delil: {n} / {req} gerekli",
                fg=renk
            )

    def _bilgi_guncelle(self, mesaj, renk=GRAY):

        # Bilgi mesajını güncelle
        if self.bilgi_etiketi:
            self.bilgi_etiketi.configure(
                text=mesaj,
                fg=renk
            )

    def analiz_guncelle(self):

        # Analiz etiketi varsa güncelle
        if self.analiz_etiketi:

            # Son 6 analiz sonucunu göster
            metin = (
                "\n".join(
                    f"✅ {a}"
                    for a in self.analiz_edilenler[-6:]
                )
                or "Henüz analiz yok."
            )

            # Etiketi güncelle
            self.analiz_etiketi.configure(
                text=metin,

                # Analiz varsa yeşil yoksa koyu renk
                fg=GREEN if self.analiz_edilenler else DARK
            )

