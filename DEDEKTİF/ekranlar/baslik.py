# ekranlar/baslik.py — Başlık Ekranı

import tkinter as tk          # Arayüz oluşturmak için tkinter kütüphanesi
import random                 # Rastgele sayı üretmek için
from renkler import *         # Oyunda kullanılan renk sabitlerini içe aktarır
from veri import BOLUMLER     # Bölüm verilerini içe aktarır


class BaslikEkrani:
    def __init__(self, oyun):
        self.oyun = oyun      # Ana oyun nesnesini saklar
        self._olustur()       # Başlık ekranını oluşturur

    def _olustur(self):
        f = self.oyun.ana_cerceve   # Oyunun ana çerçevesini alır

        # Tüm ekranı kaplayan canvas oluşturur
        canvas = tk.Canvas(f, bg=BG, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Dekoratif arka plan daireleri
        for _ in range(8):
            x = random.randint(50, 1230)   # Dairenin x konumu
            y = random.randint(50, 730)    # Dairenin y konumu
            r = random.randint(20, 80)     # Dairenin yarıçapı

            # Rastgele koyu tonlarda renk seçer
            col = random.choice(["#0d2045", "#0a1a35", "#122040", "#0e1c38"])

            # Canvas üzerine daire çizer
            canvas.create_oval(
                x - r, y - r, x + r, y + r,
                fill=col,
                outline=""
            )

        # Başlık / Logo
        canvas.create_text(
            640, 155,
            text="🔍",
            font=("Segoe UI Emoji", 60),
            fill=GOLD
        )  # Büyüteç emojisi çizer

        canvas.create_text(
            640, 255,
            text="CRIMINAL CASE",
            font=("Impact", 52, "bold"),
            fill=GOLD
        )  # Ana oyun başlığı

        canvas.create_text(
            640, 315,
            text="İSTANBUL DOSYALARI",
            font=("Consolas", 22, "bold"),
            fill=CYAN
        )  # Alt başlık

        canvas.create_text(
            640, 365,
            text="─── ✦ Üç Bölümlü Dedektiflik Macerası ✦ ───",
            font=("Segoe UI", 13),
            fill=GRAY
        )  # Açıklama yazısı

        # Bölüm önizlemeleri
        onizleme = [
            ("1", "Müzedeki Cinayet", "#dc2626"),
            ("2", "Limandaki Şifre",  "#059669"),
            ("3", "Karanlık Orman",   "#6d28d9"),
        ]  # Bölüm bilgileri listesi

        # Her bölüm için kutu oluşturur
        for i, (num, isim, renk) in enumerate(onizleme):

            # Kutuların x koordinasyonu
            bx = 340 + i * 200

            # Bölüm kutusu çizer
            canvas.create_rectangle(
                bx - 80, 415,
                bx + 80, 488,
                fill=CARD,
                outline=renk,
                width=2
            )

            # Bölüm numarasını yazar
            canvas.create_text(
                bx, 438,
                text=f"Bölüm {num}",
                font=("Consolas", 11, "bold"),
                fill=renk
            )

            # Bölüm adını yazar
            canvas.create_text(
                bx, 462,
                text=isim,
                font=("Segoe UI", 10),
                fill=WHITE
            )

        # Toplam yıldız gösterimi
        toplam = sum(self.oyun.bolum_yildizlari)  # Tüm yıldızları toplar

        # Kazanılan ve eksik yıldızları oluşturur
        yildiz_str = "⭐" * toplam + "☆" * (9 - toplam)

        # Yıldız bilgisini ekrana yazar
        canvas.create_text(
            640, 522,
            text=f"Toplam Yıldız:  {yildiz_str}",
            font=("Segoe UI", 12),
            fill=YELLOW
        )

        # Butonları tutacak çerçeve
        btn_cerceve = tk.Frame(canvas, bg=BG)

        # Çerçeveyi canvas üzerine yerleştirir
        canvas.create_window(640, 588, window=btn_cerceve)

        # Oyuna başla butonu
        tk.Button(
            btn_cerceve,
            text="▶  OYUNA BAŞLA",
            font=("Impact", 18),
            bg=GOLD,
            fg=BG,
            relief="flat",
            padx=30,
            pady=12,
            cursor="hand2",

            # Butona basınca bölüm giriş ekranını açar
            command=self.oyun.goster_bolum_giris
        ).pack(side="left", padx=10)

        # Skor tablosu butonu
        tk.Button(
            btn_cerceve,
            text="🏆  SKORLAR",
            font=("Impact", 18),
            bg=CARD2,
            fg=YELLOW,
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2",

            # Butona basınca skor ekranını açar
            command=self._goster_skorlar
        ).pack(side="left", padx=10)

        # Alt slogan yazısı
        canvas.create_text(
            640, 655,
            text="Delil topla  •  Analiz et  •  Suçluyu yakala!",
            font=("Segoe UI", 11, "italic"),
            fill=DARK
        )

        # Sürüm ve telif bilgisi
        canvas.create_text(
            640, 685,
            text="v1.0  |  © 2025 Criminal Case: İstanbul",
            font=("Segoe UI", 9),
            fill=DARK
        )

    def _goster_skorlar(self):

        # Yeni pencere oluşturmak için tkinter tekrar içe aktarılır
        import tkinter as tk

        # Yeni pencere açılır
        pencere = tk.Toplevel(self.oyun.kok)

        pencere.title("🏆 Skor Tablosu")   # Pencere başlığı
        pencere.geometry("400x360")        # Pencere boyutu
        pencere.configure(bg=PANEL)        # Arka plan rengi

        # Bu pencere açıkken ana pencereyi pasif yapar
        pencere.grab_set()

        # Başlık etiketi
        tk.Label(
            pencere,
            text="🏆  SKOR TABLOSU",
            font=("Impact", 20),
            bg=PANEL,
            fg=GOLD
        ).pack(pady=20)

        # Her bölümün yıldız bilgilerini gösterir
        for i, bolum in enumerate(BOLUMLER):

            yildiz = self.oyun.bolum_yildizlari[i]  # Bölüm yıldızı

            # Satır çerçevesi
            satir = tk.Frame(
                pencere,
                bg=CARD,
                pady=8,
                padx=15
            )

            satir.pack(fill="x", padx=20, pady=4)

            # Bölüm adı etiketi
            tk.Label(
                satir,
                text=f"Bölüm {i + 1}: {bolum['title']}",
                font=("Segoe UI", 11, "bold"),
                bg=CARD,
                fg=WHITE
            ).pack(side="left")

            # Yıldız göstergesi
            tk.Label(
                satir,
                text="⭐" * yildiz + "☆" * (3 - yildiz),
                font=("Segoe UI", 14),
                bg=CARD,
                fg=YELLOW
            ).pack(side="right")

        # Toplam skor yazısı
        tk.Label(
            pencere,
            text=f"Toplam Skor:  {self.oyun.toplam_skor} puan",
            font=("Consolas", 14, "bold"),
            bg=PANEL,
            fg=GREEN
        ).pack(pady=15)

        # Pencereyi kapatma butonu
        tk.Button(
            pencere,
            text="Kapat",
            bg=CARD2,
            fg=WHITE,
            font=("Segoe UI", 11),
            relief="flat",
            padx=20,
            pady=6,

            # Butona basınca pencere kapanır
            command=pencere.destroy
        ).pack()