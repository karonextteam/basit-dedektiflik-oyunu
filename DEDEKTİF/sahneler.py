# sahneler.py
# Olay yeri sahnelerini canvas üzerine çizen dosya

import random

# Renk sabitlerini içe aktar
from renkler import *


# ANA SAHNE ÇİZİM FONKSİYONU


def ciz_sahne(canvas, sahne_turu):

    # Canvas üzerindeki eski çizimleri temizle
    canvas.delete("all")

    # Canvas genişliğini al
    # Eğer genişlik alınamazsa varsayılan olarak 800 kullan
    w = int(canvas.cget("width")) if canvas.cget("width") != "0" else 800

    # Sabit yükseklik
    h = 380

    # Sahne türüne göre uygun çizim fonksiyonunu çağır
    if sahne_turu == "muze":
        _ciz_muze(canvas, w, h)

    elif sahne_turu == "liman":
        _ciz_liman(canvas, w, h)

    elif sahne_turu == "orman":
        _ciz_orman(canvas, w, h)



# MÜZE SAHNESİ


def _ciz_muze(c, w, h):

    # Arka plan
    c.create_rectangle(0, 0, w, h,
                       fill="#0d1a2e",
                       outline="")

    # Üst duvar bölgesi
    c.create_rectangle(0, 0, w, 60,
                       fill="#162035",
                       outline="")

    # Sütunları çiz
    for x in [80, 200, w - 220, w - 100]:

        c.create_rectangle(
            x, 55,
            x + 30, h - 40,

            fill="#1c2a45",

            outline="#1e3a5f",
            width=1
        )

    # Zemin
    c.create_rectangle(
        0, h - 40,
        w, h,

        fill="#0f1a2e",
        outline=""
    )

    # Zemin çizgisi
    c.create_line(
        0, h - 40,
        w, h - 40,

        fill="#1e3a5f",
        width=2
    )

    # Müzedeki tablolar
    for bx, col in [
        (140, "#7c3aed"),
        (350, "#dc2626"),
        (500, "#0284c7")
    ]:

        # Tablo çerçevesi
        c.create_rectangle(
            bx, 80,
            bx + 80, 190,

            fill=CARD2,

            outline=col,
            width=2
        )

        # İç panel
        c.create_rectangle(
            bx + 8, 88,
            bx + 72, 182,

            fill="#1a1f35",
            outline=""
        )

        # Resim emojisi
        c.create_text(
            bx + 40, 135,

            text="🖼️",

            font=("Segoe UI Emoji", 22),

            fill=col
        )

    # Soyulmuş vitrin
    c.create_rectangle(
        280, 200,
        480, 310,

        fill=CARD2,

        outline=GOLD,
        width=2
    )

    # Kırık cam efektleri
    c.create_line(
        330, 200,
        310, 260,

        fill=RED,
        width=2,
        dash=(4, 2)
    )

    c.create_line(
        310, 260,
        350, 310,

        fill=RED,
        width=2,
        dash=(4, 2)
    )

    # Vitrin yazıları
    c.create_text(
        380, 255,

        text="💎 BOŞ VİTRİN",

        font=("Consolas", 11, "bold"),

        fill=RED
    )

    c.create_text(
        380, 278,

        text="SOYULDU!",

        font=("Impact", 14),

        fill=RED
    )

    # Güvenlik kamerası
    c.create_rectangle(
        w - 100, 70,
        w - 50, 100,

        fill=CARD2,

        outline=CYAN,
        width=1
    )

    c.create_text(
        w - 75, 85,

        text="📷",

        font=("Segoe UI Emoji", 14),

        fill=CYAN
    )

    c.create_text(
        w - 75, 108,

        text="KAMERA",

        font=("Consolas", 8),

        fill=CYAN
    )

    # Başlık
    c.create_text(
        w // 2, 30,

        text="🏛️  OLAY YERİ: ŞEHİR TARİH MÜZESİ",

        font=("Impact", 16),

        fill=GOLD
    )

    # Polis şeridi
    c.create_line(
        0, h - 42,
        w, h - 42,

        fill=YELLOW,

        width=3,

        dash=(10, 5)
    )

    # Uyarı yazısı
    c.create_text(
        w // 2, h - 20,

        text="⚠️  POLİS KORDONU — İZİNSİZ GİRİLMEZ",

        font=("Consolas", 10, "bold"),

        fill=YELLOW
    )

    # Kan lekeleri
    for x, y in [
        (260, 320),
        (420, 290),
        (150, 350)
    ]:

        c.create_oval(
            x, y,
            x + 12, y + 8,

            fill="#7f1d1d",

            outline=""
        )


# LİMAN SAHNESİ


def _ciz_liman(c, w, h):

    # Gece gökyüzü
    c.create_rectangle(
        0, 0,
        w, h // 2,

        fill="#050e1a",
        outline=""
    )

    # Rastgele yıldızlar oluştur
    for _ in range(40):

        sx = random.randint(0, w)
        sy = random.randint(0, h // 2 - 20)

        c.create_oval(
            sx, sy,
            sx + 2, sy + 2,

            fill=WHITE,

            outline=""
        )

    # Ay
    c.create_oval(
        w - 160, 20,
        w - 110, 70,

        fill="#fef9c3",

        outline=""
    )

    # Ay gölgesi
    c.create_oval(
        w - 145, 15,
        w - 95, 65,

        fill="#050e1a",

        outline=""
    )

    # Deniz
    c.create_rectangle(
        0, h // 2,
        w, h,

        fill="#0c2340",

        outline=""
    )

    # Deniz dalga çizgileri
    for y in range(h // 2, h, 18):

        c.create_line(
            0, y,
            w, y,

            fill="#0e2a4d",

            width=1
        )

    # Gemi gövdesi
    c.create_polygon(
        150, 200,
        600, 200,
        620, 260,
        130, 260,

        fill="#1a2e45",

        outline="#2563eb",

        width=2
    )

    # Gemi üst kısmı
    c.create_rectangle(
        200, 140,
        560, 200,

        fill="#162035",

        outline="#1d4ed8",

        width=1
    )

    # Baca
    c.create_rectangle(
        340, 80,
        380, 145,

        fill=CARD2,

        outline=GRAY
    )

    # Duman
    c.create_oval(
        330, 60,
        390, 85,

        fill="#1a1a2e",

        outline=""
    )

    c.create_text(
        360, 72,

        text="💨",

        font=("Segoe UI Emoji", 12),

        fill=GRAY
    )

    # Patlama efekti
    c.create_line(
        150, 260,
        220, 290,

        fill=RED,

        width=3
    )

    c.create_text(
        185, 278,

        text="💥",

        font=("Segoe UI Emoji", 14)
    )

    # Kargo kutuları
    for bx in [650, 720, 790]:

        c.create_rectangle(
            bx, 295,
            bx + 55, 345,

            fill=CARD2,

            outline=ORANGE,

            width=2
        )

        c.create_text(
            bx + 27, 320,

            text="📦",

            font=("Segoe UI Emoji", 16)
        )

    # Suç alanı
    c.create_rectangle(
        630, 278,
        860, 360,

        fill="#1a0a00",

        outline=RED,

        width=2
    )

    # Bilgi yazıları
    c.create_text(
        745, 308,

        text="KARGO ÇALINDI!",

        font=("Impact", 14),

        fill=RED
    )

    c.create_text(
        745, 333,

        text="⚠️  Soruşturma Aktif",

        font=("Consolas", 10),

        fill=YELLOW
    )

    # Başlık
    c.create_text(
        w // 2, 25,

        text="⚓  OLAY YERİ: ESKİ İSTANBUL LİMANI",

        font=("Impact", 16),

        fill=GOLD
    )

    # Polis şeridi
    c.create_line(
        0, h - 40,
        w, h - 40,

        fill=YELLOW,

        width=3,

        dash=(10, 5)
    )

    # Uyarı yazısı
    c.create_text(
        w // 2, h - 20,

        text="⚠️  POLİS KORDONU — İZİNSİZ GİRİLMEZ",

        font=("Consolas", 10, "bold"),

        fill=YELLOW
    )



# ORMAN SAHNESİ


def _ciz_orman(c, w, h):

    # Arka plan
    c.create_rectangle(
        0, 0,
        w, h,

        fill="#030a06",

        outline=""
    )

    # Ay ışığı efekti
    c.create_oval(
        w - 180, -40,
        w - 20, 100,

        fill="#0a1a0f",

        outline=""
    )

    # Ay
    c.create_oval(
        w - 160, 10,
        w - 100, 70,

        fill="#e2e8c0",

        outline=""
    )

    # Ağaç konumları
    tree_positions = [
        50, 130, 220, 310,
        430, 550, 640, 730,
        820, 910, 990,
        1070, 1150, 1230
    ]

    # Ağaçları çiz
    for tx in tree_positions:

        # Rastgele yükseklik
        th = random.randint(140, 220)

        # Rastgele genişlik
        tw = random.randint(50, 80)

        # Ağaç gövdesi
        c.create_rectangle(
            tx + tw // 2 - 8,
            h - 60,

            tx + tw // 2 + 8,
            h - 60 - th // 2,

            fill="#0a1505"
        )

        # Alt yaprak bölgesi
        c.create_oval(
            tx,
            h - 60 - th,

            tx + tw,
            h - 60 - th // 2 + 30,

            fill="#071208",

            outline=""
        )

        # Üst yaprak bölgesi
        c.create_oval(
            tx + 5,
            h - 60 - th - 20,

            tx + tw - 5,
            h - 60 - th // 2 + 10,

            fill="#0b1a0d",

            outline=""
        )

    # Zemin
    c.create_rectangle(
        0, h - 60,
        w, h,

        fill="#060e05",

        outline=""
    )

    # Kazı alanı
    c.create_rectangle(
        380, 265,
        580, 340,

        fill="#0e1a0c",

        outline="#15803d",

        width=2
    )

    # Kazı alanı yazısı
    c.create_text(
        480, 298,

        text="⛏️  KAZINTI YERİ",

        font=("Consolas", 12),

        fill=GREEN
    )

    # Kemik emojisi
    c.create_text(
        480, 330,

        text="🦴",

        font=("Segoe UI Emoji", 26)
    )

    # Açıklama yazısı
    c.create_text(
        480, 362,

        text="Eski kemik — 10 yıl öncesi?",

        font=("Consolas", 9),

        fill=RED
    )

    # Polis inceleme alanı
    c.create_rectangle(
        300, 248,
        660, 378,

        fill="",

        outline=YELLOW,

        width=3,

        dash=(8, 4)
    )

    # Başlık
    c.create_text(
        w // 2, 25,

        text="🌲  OLAY YERİ: KARANLIK ORMAN",

        font=("Impact", 16),

        fill=GOLD
    )

    # Polis şeridi
    c.create_line(
        0, h - 40,
        w, h - 40,

        fill=YELLOW,

        width=3,

        dash=(10, 5)
    )

    # Uyarı yazısı
    c.create_text(
        w // 2, h - 20,

        text="⚠️  POLİS KORDONU — İZİNSİZ GİRİLMEZ",

        font=("Consolas", 10, "bold"),

        fill=YELLOW
    )
