#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CRIMINAL CASE: İSTANBUL DOSYALARI
Çok Bölümlü Görsel Dedektiflik Oyunu
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time

#  RENK PALETİ

BG      = "#0a0f1e"
PANEL   = "#0d1526"
CARD    = "#162035"
CARD2   = "#1c2a45"
GOLD    = "#f59e0b"
BLUE    = "#3b82f6"
LBLUE   = "#60a5fa"
RED     = "#ef4444"
GREEN   = "#22c55e"
PURPLE  = "#a855f7"
ORANGE  = "#f97316"
CYAN    = "#06b6d4"
WHITE   = "#f1f5f9"
GRAY    = "#94a3b8"
DARK    = "#475569"
BORDER  = "#1e3a5f"
YELLOW  = "#facc15"


#  OYUN VERİSİ — 3 BÖLÜM

CHAPTERS = [
    {
        "num": 1,
        "title": "MÜZEDEKİ CİNAYET",
        "location": "📍 Şehir Tarih Müzesi, İstanbul",
        "scene_type": "museum",
        "story": (
            "Şehir Tarih Müzesi'nde değerli Osmanlı madalyaları çalındı!\n"
            "Müze bekçisi Ahmet Bey bayıltılmış halde bulundu.\n\n"
            "Gece yarısı gerçekleşen bu soygunun faillini bulmak için\n"
            "müzeyi dikkatlice incele, delilleri topla ve\n"
            "laboratuvarda analiz et. Suçluyu yakala!"
        ),
        "suspects": [
            {
                "name": "Prof. Kaplan",
                "role": "Baş Küratör",
                "color": "#dc2626",
                "emoji": "🎓",
                "guilty": False,
                "bio": "25 yıllık tecrübeli küratör.\nÇok dürüst ve düzgün biri olarak\ntanınıyor. O gece evde miydi?",
                "owned_clues": ["Profesörün not defteri", "Kırmızı boya lekesi"],
            },
            {
                "name": "Zeynep Avcı",
                "role": "Güvenlik Şefi",
                "color": "#7c3aed",
                "emoji": "🔐",
                "guilty": False,
                "bio": "Tüm güvenlik kodlarını biliyor.\nÇok sistemli ama o gece alarmı\nneden kapattı?",
                "owned_clues": ["Zeynep'in anahtarı", "Mor iplik"],
            },
            {
                "name": "Mert Demir",
                "role": "Restoratör",
                "color": "#0284c7",
                "emoji": "🎨",
                "guilty": True,
                "bio": "2 ay önce işe başladı.\nGeçmişi pek temiz değil...\nBorçları olduğu söyleniyor.",
                "owned_clues": ["Mert'in parmak izi", "Mavi boya tüpü", "Mert'e ait çanta"],
            },
        ],
        "all_clues": [
            "🔍 Kırık Cam Parçası",    "🩸 Kan Lekesi",
            "📌 Düşmüş Rozet",          "🧵 Yırtık Kumaş",
            "👣 Ayak İzi",              "🚬 Sigara İzmariti",
            "📝 Şifreli Not",           "🎨 Mavi Boya Tüpü",
            "👆 Parmak İzi",            "⚗️ Kimyasal Leke",
            "🔘 Kopuk Düğme",           "💡 Yanık Tel",
        ],
        "guilty_clues": ["🎨 Mavi Boya Tüpü", "👆 Parmak İzi", "📌 Düşmüş Rozet"],
        "min_clues": 5,
    },
    {
        "num": 2,
        "title": "LİMANDAKİ ŞIFRE",
        "location": "📍 Eski İstanbul Limanı",
        "scene_type": "harbor",
        "story": (
            "Eski İstanbul Limanı'nda bir gemi gece yarısı karaya oturdu!\n"
            "Kaptan ortada yok, değerli kargo tamamen çalınmış.\n\n"
            "Şifreli mesajları çöz, gizli belgeleri bul ve bu\n"
            "karanlık operasyonun arkasındaki kişiyi ortaya çıkar!\n"
            "Zaman daralıyor..."
        ),
        "suspects": [
            {
                "name": "Kaptan Yıldız",
                "role": "Eski Kaptan",
                "color": "#d97706",
                "emoji": "⚓",
                "guilty": False,
                "bio": "30 yıllık denizci.\nSigortacılarla sorunları var\nama hep dürüst biri oldu.",
                "owned_clues": ["Kaptanın günlüğü", "Turuncu halat"],
            },
            {
                "name": "Selma Koç",
                "role": "Gümrük Müdürü",
                "color": "#059669",
                "emoji": "📋",
                "guilty": True,
                "bio": "Tüm gümrük belgelerini\ndüzenliyor. Çok yetkili.\nBanka hesabında şüpheli para var.",
                "owned_clues": ["Selma'nın mühürü", "Gizli belge", "Yeşil mürekkep"],
            },
            {
                "name": "Hakan Bulut",
                "role": "Liman Bekçisi",
                "color": "#be185d",
                "emoji": "🔦",
                "guilty": False,
                "bio": "10 yıldır limanı koruyor.\nO gece nöbetini erken bıraktı.\nNeden?",
                "owned_clues": ["Hakan'ın el feneri", "Pembe boya izi"],
            },
        ],
        "all_clues": [
            "💧 Islak Ayak İzi",        "📦 Hasar Görmüş Sandık",
            "📜 Şifreli Mesaj",         "🪝 Metal Kanca",
            "🌿 Deniz Yosunu",          "📋 Sahte Belge",
            "🧭 Kırık Pusula",          "🔏 Mühür Baskısı",
            "⛽ Gemi Yağı",             "🖊️ Yeşil Mürekkep",
            "🪢 Kopuk Halat",           "🔑 Yedek Anahtar",
        ],
        "guilty_clues": ["📋 Sahte Belge", "🔏 Mühür Baskısı", "🖊️ Yeşil Mürekkep"],
        "min_clues": 6,
    },
    {
        "num": 3,
        "title": "KARANLIK ORMAN SIRRI",
        "location": "📍 Belgrad Ormanı Derinlikleri",
        "scene_type": "forest",
        "story": (
            "Belgrad Ormanı'nın derinliklerinde insan kemikleri bulundu!\n"
            "DNA analizi 10 yıl öncesine işaret ediyor.\n\n"
            "Bu soğuk dava kapandı sanılıyordu. Ama sen\n"
            "gerçeği gün yüzüne çıkarmak için son bir şansa sahipsin.\n"
            "Delilleri topla, suçluyu mahkûm et!"
        ),
        "suspects": [
            {
                "name": "Dr. Şahin",
                "role": "Orman Mühendisi",
                "color": "#6d28d9",
                "emoji": "🧪",
                "guilty": True,
                "bio": "Eski bir araştırmacı.\nO dönemde ormanda çok\nzaman geçiriyordu. DNA eşleşmesi!",
                "owned_clues": ["Dr. Şahin'in rozeti", "Mor ilaç şişesi", "Şahin'e ait DNA"],
            },
            {
                "name": "Leyla Yurt",
                "role": "Botanik Uzmanı",
                "color": "#15803d",
                "emoji": "🌿",
                "guilty": False,
                "bio": "Ormandaki bitkileri\naraştırıyor. Çok sakin\nve nazik biri.",
                "owned_clues": ["Leyla'nın not defteri", "Yeşil boya"],
            },
            {
                "name": "Rıza Kara",
                "role": "Avcı Rehberi",
                "color": "#92400e",
                "emoji": "🏹",
                "guilty": False,
                "bio": "Ormanda yıllardır rehberlik\nyapıyor. O gece ormanda\nmıydı gerçekten?",
                "owned_clues": ["Rıza'nın çakısı", "Kahve renkli tüy"],
            },
        ],
        "all_clues": [
            "🦴 Eski Kemik",            "🔪 Pas Tutmuş Bıçak",
            "📷 Solmuş Fotoğraf",       "👕 Yırtık Giysi",
            "🌱 Toprak Örneği",         "🧬 DNA İzi",
            "⌚ Kırık Saat",            "📦 Gömülü Kutu",
            "💊 İlaç Şişesi",          "🟣 Mor Leke",
            "📛 Rozet Parçası",         "📰 Eski Gazete",
        ],
        "guilty_clues": ["🧬 DNA İzi", "💊 İlaç Şişesi", "📛 Rozet Parçası"],
        "min_clues": 7,
    },
]

# ══════════════════════════════════════════
#  ANA OYUN SINIFI
# ══════════════════════════════════════════
class CriminalCaseGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🔍 Criminal Case: İstanbul Dosyaları")
        self.root.geometry("1280x780")
        self.root.configure(bg=BG)
        self.root.resizable(True, True)
        self.root.minsize(1100, 700)

        # ── Durum değişkenleri
        self.chapter_idx   = 0
        self.inventory     = []
        self.analyzed      = []
        self.score         = 0
        self.total_score   = 0
        self.chapter_stars = [0, 0, 0]
        self.lab_busy      = False
        self.selected_evidence = tk.StringVar(value="")
        self.selected_suspect  = None

        # ── Ana frame
        self.main = None
        self._show_title()

    # ──────────────────────────────────────
    #  EKRAN TEMİZLEME
    # ──────────────────────────────────────
    def _clear(self):
        if self.main:
            self.main.destroy()
        self.main = tk.Frame(self.root, bg=BG)
        self.main.pack(fill="both", expand=True)

    # ══════════════════════════════════════
    #  1) BAŞLIK EKRANI
    # ══════════════════════════════════════
    def _show_title(self):
        self._clear()
        f = self.main

        # Arka plan gradient efekti (canvas)
        canvas = tk.Canvas(f, bg=BG, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Dekoratif daireler
        for i in range(8):
            x = random.randint(50, 1230)
            y = random.randint(50, 730)
            r = random.randint(20, 80)
            col = random.choice(["#0d2045","#0a1a35","#122040","#0e1c38"])
            canvas.create_oval(x-r, y-r, x+r, y+r, fill=col, outline="")

        # Logo / Başlık
        canvas.create_text(640, 160, text="🔍", font=("Segoe UI Emoji", 64), fill=GOLD)
        canvas.create_text(640, 260, text="CRIMINAL CASE",
                           font=("Impact", 52, "bold"), fill=GOLD)
        canvas.create_text(640, 320, text="İSTANBUL DOSYALARI",
                           font=("Consolas", 22, "bold"), fill=CYAN)
        canvas.create_text(640, 370, text="─── ✦ Üç Bölümlü Dedektiflik Macerası ✦ ───",
                           font=("Segoe UI", 13), fill=GRAY)

        # Bölüm önizleme
        chapters_preview = [
            ("1", "Müzedeki Cinayet",   "#dc2626"),
            ("2", "Limandaki Şifre",    "#059669"),
            ("3", "Karanlık Orman",     "#6d28d9"),
        ]
        for i, (num, name, col) in enumerate(chapters_preview):
            bx = 340 + i * 200
            canvas.create_rectangle(bx-80, 420, bx+80, 490,
                                    fill=CARD, outline=col, width=2)
            canvas.create_text(bx, 445, text=f"Bölüm {num}",
                               font=("Consolas", 11, "bold"), fill=col)
            canvas.create_text(bx, 465, text=name,
                               font=("Segoe UI", 10), fill=WHITE)

        # Toplam skor göster
        total = sum(self.chapter_stars)
        stars_str = "⭐" * total + "☆" * (9 - total)
        canvas.create_text(640, 525, text=f"Toplam Yıldız:  {stars_str}",
                           font=("Segoe UI", 12), fill=YELLOW)

        # Butonlar — canvas üzerine window embed
        btn_frame = tk.Frame(canvas, bg=BG)
        canvas.create_window(640, 590, window=btn_frame)

        tk.Button(
            btn_frame, text="▶  OYUNA BAŞLA",
            font=("Impact", 18), bg=GOLD, fg=BG,
            relief="flat", padx=30, pady=12, cursor="hand2",
            command=self._show_chapter_intro
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame, text="🏆  SKORLAR",
            font=("Impact", 18), bg=CARD2, fg=YELLOW,
            relief="flat", padx=20, pady=12, cursor="hand2",
            command=self._show_scores
        ).pack(side="left", padx=10)

        canvas.create_text(640, 660, text="Delil topla • Analiz et • Suçluyu yakala!",
                           font=("Segoe UI", 11, "italic"), fill=DARK)
        canvas.create_text(640, 690, text="v1.0  |  © 2025 Criminal Case: İstanbul",
                           font=("Segoe UI", 9), fill=DARK)

    # ══════════════════════════════════════
    #  SKORLAR
    # ══════════════════════════════════════
    def _show_scores(self):
        win = tk.Toplevel(self.root)
        win.title("🏆 Skor Tablosu")
        win.geometry("400x350")
        win.configure(bg=PANEL)
        win.grab_set()

        tk.Label(win, text="🏆  SKOR TABLOSU", font=("Impact", 20),
                 bg=PANEL, fg=GOLD).pack(pady=20)

        for i, ch in enumerate(CHAPTERS):
            stars = self.chapter_stars[i]
            row = tk.Frame(win, bg=CARD, pady=8, padx=15)
            row.pack(fill="x", padx=20, pady=4)
            tk.Label(row, text=f"Bölüm {i+1}: {ch['title']}",
                     font=("Segoe UI", 11, "bold"), bg=CARD, fg=WHITE).pack(side="left")
            tk.Label(row, text="⭐" * stars + "☆" * (3 - stars),
                     font=("Segoe UI", 14), bg=CARD, fg=YELLOW).pack(side="right")

        tk.Label(win, text=f"Toplam Skor:  {self.total_score} puan",
                 font=("Consolas", 14, "bold"), bg=PANEL, fg=GREEN).pack(pady=15)
        tk.Button(win, text="Kapat", bg=CARD2, fg=WHITE,
                  font=("Segoe UI", 11), relief="flat", padx=20, pady=6,
                  command=win.destroy).pack()

    # ══════════════════════════════════════
    #  2) BÖLÜM GİRİŞ EKRANI
    # ══════════════════════════════════════
    def _show_chapter_intro(self):
        self._clear()
        ch = CHAPTERS[self.chapter_idx]

        # Reset chapter state
        self.inventory.clear()
        self.analyzed.clear()
        self.score = 0
        self.selected_suspect = None

        f = self.main
        canvas = tk.Canvas(f, bg=PANEL, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Başlık şeridi
        canvas.create_rectangle(0, 0, 1280, 80, fill=CARD, outline="")
        canvas.create_text(640, 25, text=f"BÖLÜM  {ch['num']}  /  3",
                           font=("Consolas", 13), fill=GRAY)
        canvas.create_text(640, 55, text=ch["title"],
                           font=("Impact", 30, "bold"), fill=GOLD)

        # Konum
        canvas.create_text(640, 105, text=ch["location"],
                           font=("Segoe UI", 13, "italic"), fill=CYAN)

        # Hikaye kutusu
        canvas.create_rectangle(240, 125, 1040, 310,
                                 fill=CARD, outline=BORDER, width=2)
        canvas.create_text(640, 215, text=ch["story"],
                           font=("Segoe UI", 13), fill=WHITE,
                           width=750, justify="center")

        # Şüpheliler önizleme
        canvas.create_text(640, 345, text="─── ŞÜPHELİLER ───",
                           font=("Impact", 16), fill=GRAY)

        for i, s in enumerate(ch["suspects"]):
            bx = 280 + i * 240
            canvas.create_rectangle(bx-100, 370, bx+100, 490,
                                    fill=CARD, outline=s["color"], width=2)
            canvas.create_text(bx, 400, text=s["emoji"],
                               font=("Segoe UI Emoji", 28), fill=s["color"])
            canvas.create_text(bx, 440, text=s["name"],
                               font=("Impact", 14), fill=s["color"])
            canvas.create_text(bx, 462, text=s["role"],
                               font=("Segoe UI", 10), fill=GRAY)
            canvas.create_text(bx, 480, text="❓",
                               font=("Segoe UI Emoji", 13), fill=DARK)

        # Gereksinim bilgisi
        canvas.create_text(640, 530,
                           text=f"Bu bölümü çözmek için en az  {ch['min_clues']}  delil toplamalısın!",
                           font=("Segoe UI", 12), fill=YELLOW)

        # Buton
        btn_f = tk.Frame(canvas, bg=PANEL)
        canvas.create_window(640, 590, window=btn_f)

        tk.Button(
            btn_f, text="🔍  SORUŞTURMAYA BAŞLA",
            font=("Impact", 19), bg=RED, fg=WHITE,
            relief="flat", padx=30, pady=12, cursor="hand2",
            command=self._show_investigation
        ).pack(side="left", padx=10)

        tk.Button(
            btn_f, text="◀  Ana Menü",
            font=("Segoe UI", 12), bg=CARD2, fg=GRAY,
            relief="flat", padx=16, pady=12, cursor="hand2",
            command=self._show_title
        ).pack(side="left", padx=5)

    # ══════════════════════════════════════
    #  3) SORUŞTURMA EKRANI
    # ══════════════════════════════════════
    def _show_investigation(self):
        self._clear()
        ch = CHAPTERS[self.chapter_idx]
        f  = self.main

        # ── Üst bar
        topbar = tk.Frame(f, bg=CARD, height=55)
        topbar.pack(fill="x", side="top")
        topbar.pack_propagate(False)

        tk.Label(topbar, text=f"🔍  {ch['title']}",
                 font=("Impact", 17), bg=CARD, fg=GOLD).pack(side="left", padx=15, pady=10)
        tk.Label(topbar, text=ch["location"],
                 font=("Segoe UI", 10, "italic"), bg=CARD, fg=CYAN).pack(side="left", padx=5)

        # Skor
        self.score_lbl = tk.Label(topbar, text=f"⭐ Skor: {self.score}",
                                   font=("Consolas", 13, "bold"), bg=CARD, fg=YELLOW)
        self.score_lbl.pack(side="right", padx=15)

        self.clue_count_lbl = tk.Label(topbar,
                                        text=f"🗂 Delil: 0 / {ch['min_clues']} gerekli",
                                        font=("Consolas", 12), bg=CARD, fg=GRAY)
        self.clue_count_lbl.pack(side="right", padx=10)

        # ── Ana içerik alanı
        content = tk.Frame(f, bg=BG)
        content.pack(fill="both", expand=True)

        # ── SOL PANEL — şüpheliler
        left = tk.Frame(content, bg=PANEL, width=230)
        left.pack(side="left", fill="y", padx=(8,4), pady=8)
        left.pack_propagate(False)

        tk.Label(left, text="👥  ŞÜPHELİLER",
                 font=("Impact", 14), bg=PANEL, fg=GOLD).pack(pady=(12,6))

        self.suspect_frames = {}
        for s in ch["suspects"]:
            sf = tk.Frame(left, bg=CARD, cursor="hand2")
            sf.pack(fill="x", padx=8, pady=5)
            sf.bind("<Enter>", lambda e, fr=sf, col=s["color"]:
                    fr.configure(bg=col, highlightbackground=col))
            sf.bind("<Leave>", lambda e, fr=sf:
                    fr.configure(bg=CARD))

            tk.Label(sf, text=f"{s['emoji']}  {s['name']}",
                     font=("Impact", 13), bg=CARD, fg=s["color"],
                     cursor="hand2").pack(anchor="w", padx=10, pady=(8,2))
            tk.Label(sf, text=s["role"],
                     font=("Segoe UI", 9), bg=CARD, fg=GRAY).pack(anchor="w", padx=12)
            tk.Label(sf, text=s["bio"],
                     font=("Segoe UI", 9), bg=CARD, fg=DARK,
                     justify="left", wraplength=190).pack(anchor="w", padx=12, pady=(2,8))

            btn_acc = tk.Button(
                sf, text="⚖️  Suçla",
                font=("Segoe UI", 9, "bold"), bg=RED, fg=WHITE,
                relief="flat", padx=8, pady=3, cursor="hand2",
                command=lambda sname=s["name"]: self._accuse(sname)
            )
            btn_acc.pack(anchor="e", padx=8, pady=(0,8))
            self.suspect_frames[s["name"]] = sf

        # ── ORTA PANEL — olay yeri + butonlar
        mid = tk.Frame(content, bg=BG)
        mid.pack(side="left", fill="both", expand=True, padx=4, pady=8)

        # Olay yeri canvas
        self.scene_canvas = tk.Canvas(mid, bg=CARD, highlightthickness=2,
                                       highlightbackground=BORDER, height=380)
        self.scene_canvas.pack(fill="x", pady=(0,6))
        self._draw_scene(ch["scene_type"])

        # Aksiyon butonları
        act_frame = tk.Frame(mid, bg=BG)
        act_frame.pack(fill="x", pady=4)

        tk.Button(
            act_frame, text="🔎  Olay Yerini İncele  (+Delil)",
            font=("Impact", 14), bg=BLUE, fg=WHITE,
            relief="flat", padx=18, pady=10, cursor="hand2",
            command=self._inspect_scene
        ).pack(side="left", padx=(0,8))

        tk.Button(
            act_frame, text="🔬  Delili Laboratuvara Gönder",
            font=("Impact", 14), bg=PURPLE, fg=WHITE,
            relief="flat", padx=18, pady=10, cursor="hand2",
            command=self._open_lab
        ).pack(side="left", padx=4)

        tk.Button(
            act_frame, text="💾  Dosyayı Kaydet",
            font=("Impact", 14), bg="#065f46", fg=WHITE,
            relief="flat", padx=18, pady=10, cursor="hand2",
            command=self._save_notes
        ).pack(side="left", padx=4)

        # Bilgi alanı
        self.info_label = tk.Label(
            mid,
            text="💡  'Olay Yerini İncele' butonuna basarak delil toplayabilirsin!",
            font=("Segoe UI", 10, "italic"), bg=BG, fg=GRAY,
            wraplength=680, justify="left"
        )
        self.info_label.pack(fill="x", pady=(4,0))

        # ── SAĞ PANEL — envanter
        right = tk.Frame(content, bg=PANEL, width=260)
        right.pack(side="right", fill="y", padx=(4,8), pady=8)
        right.pack_propagate(False)

        tk.Label(right, text="🗂️  DELİL ENVANTERİ",
                 font=("Impact", 14), bg=PANEL, fg=GOLD).pack(pady=(12,4))
        tk.Label(right, text="Bir delil seçip lab'a gönder:",
                 font=("Segoe UI", 9, "italic"), bg=PANEL, fg=GRAY).pack()

        # Scrollable listbox
        listbox_frame = tk.Frame(right, bg=PANEL)
        listbox_frame.pack(fill="both", expand=True, padx=8, pady=6)

        scrollbar = tk.Scrollbar(listbox_frame, bg=CARD2)
        scrollbar.pack(side="right", fill="y")

        self.inv_listbox = tk.Listbox(
            listbox_frame,
            font=("Consolas", 11),
            bg=CARD, fg=WHITE,
            selectbackground=BLUE, selectforeground=WHITE,
            relief="flat", bd=0,
            yscrollcommand=scrollbar.set,
            activestyle="none", cursor="hand2",
            height=14
        )
        self.inv_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.inv_listbox.yview)

        # Analiz edilenler
        tk.Label(right, text="✅  ANALİZ EDİLENLER",
                 font=("Impact", 12), bg=PANEL, fg=GREEN).pack(pady=(8,2))

        self.analyzed_frame = tk.Frame(right, bg=PANEL)
        self.analyzed_frame.pack(fill="x", padx=8)

        self.analyzed_lbl = tk.Label(
            self.analyzed_frame,
            text="Henüz analiz yok.",
            font=("Segoe UI", 9, "italic"), bg=PANEL, fg=DARK,
            wraplength=220, justify="left"
        )
        self.analyzed_lbl.pack(anchor="w")

    # ──────────────────────────────────────
    #  SAHNE ÇİZİMİ
    # ──────────────────────────────────────
    def _draw_scene(self, scene_type):
        c = self.scene_canvas
        c.delete("all")
        w, h = 800, 380

        if scene_type == "museum":
            self._draw_museum(c, w, h)
        elif scene_type == "harbor":
            self._draw_harbor(c, w, h)
        elif scene_type == "forest":
            self._draw_forest(c, w, h)

    def _draw_museum(self, c, w, h):
        # Zemin
        c.create_rectangle(0, 0, w, h, fill="#0d1a2e", outline="")
        # Tavan
        c.create_rectangle(0, 0, w, 60, fill="#162035", outline="")
        # Sütunlar
        for x in [80, 200, 560, 680]:
            c.create_rectangle(x, 55, x+30, h-40, fill="#1c2a45", outline="#1e3a5f", width=1)
        # Zemin çizgisi
        c.create_rectangle(0, h-40, w, h, fill="#0f1a2e", outline="")
        c.create_line(0, h-40, w, h-40, fill="#1e3a5f", width=2)
        # Tablolar
        for bx, col in [(140, "#7c3aed"), (350, "#dc2626"), (500, "#0284c7")]:
            c.create_rectangle(bx, 80, bx+80, 190, fill=CARD2, outline=col, width=2)
            c.create_rectangle(bx+8, 88, bx+72, 182, fill="#1a1f35", outline="")
            c.create_text(bx+40, 135, text="🖼️", font=("Segoe UI Emoji", 22), fill=col)
        # Vitrin — kırık
        c.create_rectangle(280, 200, 480, 310, fill=CARD2, outline=GOLD, width=2)
        c.create_line(330, 200, 310, 260, fill="#ef4444", width=2, dash=(4,2))
        c.create_line(310, 260, 350, 310, fill="#ef4444", width=2, dash=(4,2))
        c.create_text(380, 255, text="💎 BOŞ VİTRİN", font=("Consolas", 11, "bold"), fill=RED)
        c.create_text(380, 278, text="SOYULDU!", font=("Impact", 14), fill=RED)
        # Kamera
        c.create_rectangle(680, 70, 730, 100, fill=CARD2, outline=CYAN, width=1)
        c.create_text(705, 85, text="📷", font=("Segoe UI Emoji", 14), fill=CYAN)
        c.create_text(705, 108, text="KAMERA", font=("Consolas", 8), fill=CYAN)
        # Başlık
        c.create_text(w//2, 30, text="🏛️  OLAY YERİ: ŞEHİR TARİH MÜZESİ",
                      font=("Impact", 16), fill=GOLD)
        # Kordon şeridi
        c.create_line(0, h-42, w, h-42, fill=YELLOW, width=3, dash=(10,5))
        c.create_text(w//2, h-20, text="⚠️  POLİS KORDonu — İZİNSİZ GİRİLMEZ",
                      font=("Consolas", 10, "bold"), fill=YELLOW)
        # Kan lekeleri
        for x, y in [(260,320),(420,290),(150,350)]:
            c.create_oval(x, y, x+12, y+8, fill="#7f1d1d", outline="")

    def _draw_harbor(self, c, w, h):
        # Gece gökyüzü
        c.create_rectangle(0, 0, w, h//2, fill="#050e1a", outline="")
        # Yıldızlar
        for _ in range(40):
            sx, sy = random.randint(0,w), random.randint(0, h//2-20)
            c.create_oval(sx, sy, sx+2, sy+2, fill=WHITE, outline="")
        # Ay
        c.create_oval(680, 20, 730, 70, fill="#fef9c3", outline="")
        c.create_oval(695, 15, 745, 65, fill="#050e1a", outline="")
        # Deniz
        c.create_rectangle(0, h//2, w, h, fill="#0c2340", outline="")
        for y in range(h//2, h, 18):
            c.create_line(0, y, w, y, fill="#0e2a4d", width=1)
        # Gemi
        c.create_polygon(150, 200, 600, 200, 620, 260, 130, 260,
                         fill="#1a2e45", outline="#2563eb", width=2)
        c.create_rectangle(200, 140, 560, 200, fill="#162035", outline="#1d4ed8", width=1)
        # Baca
        c.create_rectangle(340, 80, 380, 145, fill=CARD2, outline=GRAY)
        c.create_oval(330, 60, 390, 85, fill="#1a1a2e", outline="")
        c.create_text(360, 72, text="💨", font=("Segoe UI Emoji",12), fill=GRAY)
        # Hasar
        c.create_line(150, 260, 220, 290, fill=RED, width=3)
        c.create_text(185, 275, text="💥", font=("Segoe UI Emoji",14))
        # Sandıklar
        for bx in [650, 720, 790]:
            c.create_rectangle(bx, 295, bx+55, 345, fill=CARD2, outline=ORANGE, width=2)
            c.create_text(bx+27, 320, text="📦", font=("Segoe UI Emoji",16))
        # Kargo çalındı etiketi
        c.create_rectangle(630, 280, 860, 360, fill="#1a0a00", outline=RED, width=2)
        c.create_text(745, 310, text="KARGO ÇALINDI!", font=("Impact",14), fill=RED)
        c.create_text(745, 335, text="⚠️  Soruşturma Aktif", font=("Consolas",10), fill=YELLOW)
        # Başlık
        c.create_text(w//2, 25, text="⚓  OLAY YERİ: ESKİ İSTANBUL LİMANI",
                      font=("Impact", 16), fill=GOLD)
        c.create_line(0, h-40, w, h-40, fill=YELLOW, width=3, dash=(10,5))
        c.create_text(w//2, h-20, text="⚠️  POLİS KORDonu — İZİNSİZ GİRİLMEZ",
                      font=("Consolas", 10, "bold"), fill=YELLOW)

    def _draw_forest(self, c, w, h):
        # Gece ormanı
        c.create_rectangle(0, 0, w, h, fill="#030a06", outline="")
        # Ay ışığı
        c.create_oval(360, -40, 520, 100, fill="#0a1a0f", outline="")
        c.create_oval(700, 10, 760, 70, fill="#e2e8c0", outline="")
        # Ağaçlar
        tree_positions = [50,130,220,310,550,640,730,820,900,980,1050,1130,1200]
        for tx in tree_positions:
            th = random.randint(140, 220)
            tw = random.randint(50, 80)
            c.create_rectangle(tx+tw//2-8, h-60, tx+tw//2+8, h-60-th//2, fill="#0a1505")
            c.create_oval(tx, h-60-th, tx+tw, h-60-th//2+30, fill="#071208", outline="")
            c.create_oval(tx+5, h-60-th-20, tx+tw-5, h-60-th//2+10,
                          fill="#0b1a0d", outline="")
        # Zemin
        c.create_rectangle(0, h-60, w, h, fill="#060e05", outline="")
        # Kazmak
        c.create_rectangle(380, 270, 580, 340, fill="#0e1a0c", outline="#15803d", width=2)
        c.create_text(480, 305, text="⛏️  KAZINTI YERİ", font=("Consolas",12), fill=GREEN)
        # Kemik
        c.create_text(480, 340, text="🦴", font=("Segoe UI Emoji", 28))
        c.create_text(480, 370, text="Eski kemik bulundu — 10 yıl öncesi?",
                      font=("Consolas",10), fill=RED)
        # Polis bandı
        c.create_rectangle(300, 250, 660, 390, fill="", outline=YELLOW, width=3, dash=(8,4))
        # Sis efekti
        for sy in range(h-80, h-30, 10):
            c.create_rectangle(0, sy, w, sy+8, fill="#040c04", stipple="gray25", outline="")
        # Başlık
        c.create_text(w//2, 25, text="🌲  OLAY YERİ: KARANLIK ORMAN",
                      font=("Impact", 16), fill=GOLD)
        c.create_line(0, h-40, w, h-40, fill=YELLOW, width=3, dash=(10,5))
        c.create_text(w//2, h-20, text="⚠️  POLİS KORDonu — İZİNSİZ GİRİLMEZ",
                      font=("Consolas", 10, "bold"), fill=YELLOW)

    # ──────────────────────────────────────
    #  OLAY YERİ İNCELEME
    # ──────────────────────────────────────
    def _inspect_scene(self):
        ch = CHAPTERS[self.chapter_idx]
        remaining = [c for c in ch["all_clues"] if c not in self.inventory]

        if not remaining:
            self._set_info("🔍 Olay yerinde toplanacak başka delil kalmadı!", YELLOW)
            return

        count = random.randint(1, min(3, len(remaining)))
        found = random.sample(remaining, count)

        for clue in found:
            self.inventory.append(clue)
            self.inv_listbox.insert(tk.END, f"  {clue}")

        self._update_clue_count()
        self.score += count * 10
        self._update_score()

        msg = f"🔎  Bulunan deliller: {', '.join(found)}"
        self._set_info(msg, GREEN)

        # Sahneye animasyon efekti
        self._flash_scene()

    def _flash_scene(self):
        orig = self.scene_canvas.cget("highlightbackground")
        self.scene_canvas.configure(highlightbackground=GREEN, highlightthickness=3)
        self.root.after(300, lambda: self.scene_canvas.configure(
            highlightbackground=BORDER, highlightthickness=2))

    def _update_clue_count(self):
        ch = CHAPTERS[self.chapter_idx]
        n = len(self.inventory)
        req = ch["min_clues"]
        col = GREEN if n >= req else YELLOW
        self.clue_count_lbl.configure(
            text=f"🗂 Delil: {n} / {req} gerekli", fg=col)

    def _update_score(self):
        self.score_lbl.configure(text=f"⭐ Skor: {self.score}")

    def _set_info(self, msg, color=GRAY):
        self.info_label.configure(text=msg, fg=color)

    # ══════════════════════════════════════
    #  4) LABORATUVAR EKRANI
    # ══════════════════════════════════════
    def _open_lab(self):
        sel = self.inv_listbox.curselection()
        if not sel:
            self._set_info("⚠️  Önce envanter listesinden bir delil seç!", RED)
            return
        if self.lab_busy:
            self._set_info("⚗️  Laboratuvar meşgul, lütfen bekle...", YELLOW)
            return

        clue = self.inv_listbox.get(sel[0]).strip()
        if clue in self.analyzed:
            self._set_info(f"✅  '{clue}' zaten analiz edildi!", CYAN)
            return

        self.lab_busy = True

        # Lab penceresi
        lab_win = tk.Toplevel(self.root)
        lab_win.title("🔬 Dedektif Laboratuvarı")
        lab_win.geometry("520x420")
        lab_win.configure(bg=PANEL)
        lab_win.grab_set()
        lab_win.resizable(False, False)

        # Başlık
        tk.Label(lab_win, text="🔬  DEDEKTİF LABORATUVARI",
                 font=("Impact", 18), bg=PANEL, fg=CYAN).pack(pady=15)
        tk.Label(lab_win, text=f"Analiz ediliyor:  {clue}",
                 font=("Consolas", 13), bg=PANEL, fg=WHITE).pack(pady=5)

        # Animasyonlu durum etiketi
        status_lbl = tk.Label(lab_win, text="⚗️  Kimyasal analiz başlatılıyor...",
                               font=("Segoe UI", 11, "italic"), bg=PANEL, fg=GRAY)
        status_lbl.pack(pady=8)

        # İlerleme çubuğu
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Lab.Horizontal.TProgressbar",
                        troughcolor=CARD2,
                        background=GREEN,
                        bordercolor=PANEL,
                        lightcolor=GREEN,
                        darkcolor=GREEN,
                        thickness=28)

        progress_frame = tk.Frame(lab_win, bg=CARD2, pady=5)
        progress_frame.pack(fill="x", padx=30)

        progress = ttk.Progressbar(progress_frame, style="Lab.Horizontal.TProgressbar",
                                   orient="horizontal", length=460, mode="determinate",
                                   maximum=100)
        progress.pack(pady=8)

        pct_lbl = tk.Label(lab_win, text="0%", font=("Consolas", 14, "bold"),
                           bg=PANEL, fg=GREEN)
        pct_lbl.pack(pady=4)

        # Adımlar
        steps = [
            "🔬  Örnek hazırlanıyor...",
            "⚗️   Kimyasal bileşenler analiz ediliyor...",
            "🧬  DNA / parmak izi taranıyor...",
            "💾  Sonuçlar veritabanıyla eşleştiriliyor...",
            "✅  Analiz tamamlandı!",
        ]

        result_lbl = tk.Label(lab_win, text="", font=("Consolas", 13, "bold"),
                               bg=PANEL, fg=WHITE, wraplength=460, justify="center")
        result_lbl.pack(pady=12)

        close_btn = tk.Button(lab_win, text="Kapat", state="disabled",
                              font=("Segoe UI", 12), bg=CARD2, fg=GRAY,
                              relief="flat", padx=20, pady=8,
                              command=lab_win.destroy)
        close_btn.pack(pady=5)

        def run_analysis():
            for i, step in enumerate(steps):
                if not lab_win.winfo_exists():
                    break
                status_lbl.configure(text=step)
                target = (i + 1) * 20
                current = progress["value"]
                while current < target:
                    current += 2
                    progress["value"] = current
                    pct_lbl.configure(text=f"{int(current)}%")
                    time.sleep(0.04)

            if not lab_win.winfo_exists():
                self.lab_busy = False
                return

            # Sonuç belirleme
            ch = CHAPTERS[self.chapter_idx]
            owner = None
            for s in ch["suspects"]:
                for sc in s["owned_clues"]:
                    if sc.lower() in clue.lower() or clue.lower() in sc.lower():
                        owner = s
                        break
                if owner:
                    break

            # Eğer direkt eşleşme yoksa guilty_clues kontrolü
            if not owner:
                for s in ch["suspects"]:
                    for gc in ch["guilty_clues"]:
                        if gc.lower() in clue.lower() or clue.lower() in gc.lower():
                            owner = s if s["guilty"] else owner
                            break

            if owner:
                result_text = (
                    f"🎯  SONUÇ BULUNDU!\n\n"
                    f"Bu delil  '{owner['name']}'  ile eşleşti!\n"
                    f"({owner['role']})\n\n"
                    f"{'⚠️  Şüpheli işaretlendi!' if owner['guilty'] else '✅  Bu kişi temize çıktı.'}"
                )
                result_col = RED if owner["guilty"] else GREEN
                self.score += 30
            else:
                result_text = (
                    f"🔍  Delil analiz edildi.\n\n"
                    f"Şimdiye kadar bilinen şüphelilerle\n"
                    f"doğrudan bağlantı kurulaMAdı.\n"
                    f"Daha fazla delil gerekebilir."
                )
                result_col = CYAN
                self.score += 15

            result_lbl.configure(text=result_text, fg=result_col)

            # Analiz edilenler listesine ekle
            self.analyzed.append(clue)
            self._update_analyzed_display()
            self._update_score()

            pct_lbl.configure(text="100%", fg=GREEN)
            progress["value"] = 100

            close_btn.configure(state="normal", bg=GREEN, fg=BG,
                                 command=lab_win.destroy)
            self.lab_busy = False

        threading.Thread(target=run_analysis, daemon=True).start()

    def _update_analyzed_display(self):
        self.analyzed_lbl.configure(
            text="\n".join(f"✅ {a}" for a in self.analyzed[-6:]) or "Henüz analiz yok.",
            fg=GREEN if self.analyzed else DARK
        )

    # ══════════════════════════════════════
    #  5) SUÇLAMA SİSTEMİ
    # ══════════════════════════════════════
    def _accuse(self, suspect_name):
        ch = CHAPTERS[self.chapter_idx]
        n_clues = len(self.inventory)

        if n_clues < ch["min_clues"]:
            messagebox.showwarning(
                "Yeterli Delil Yok!",
                f"Suçlama yapmak için en az {ch['min_clues']} delil toplamalısın!\n"
                f"Şu anda {n_clues} delilin var."
            )
            return

        suspect = next((s for s in ch["suspects"] if s["name"] == suspect_name), None)
        if not suspect:
            return

        acc_win = tk.Toplevel(self.root)
        acc_win.title("⚖️  Suçlama")
        acc_win.geometry("500x380")
        acc_win.configure(bg=PANEL)
        acc_win.grab_set()
        acc_win.resizable(False, False)

        tk.Label(acc_win, text="⚖️  SUÇLAMA",
                 font=("Impact", 22), bg=PANEL, fg=GOLD).pack(pady=15)

        tk.Label(acc_win,
                 text=f"{suspect['emoji']}  {suspect['name']}  ({suspect['role']})",
                 font=("Impact", 16), bg=PANEL, fg=suspect["color"]).pack(pady=5)

        tk.Label(acc_win,
                 text=(
                     f"Toplanan delil sayısı:  {n_clues}\n"
                     f"Analiz edilen delil:   {len(self.analyzed)}"
                 ),
                 font=("Consolas", 12), bg=PANEL, fg=GRAY).pack(pady=8)

        tk.Label(acc_win,
                 text=f"'{suspect['name']}' kişisini bu suçtan\nsorumlu tuttuğunu onaylıyor musun?",
                 font=("Segoe UI", 12), bg=PANEL, fg=WHITE,
                 justify="center").pack(pady=10)

        def confirm():
            acc_win.destroy()
            self._verdict(suspect)

        btn_row = tk.Frame(acc_win, bg=PANEL)
        btn_row.pack(pady=15)

        tk.Button(btn_row, text="⚖️  EVET, SUÇLUYORUM!",
                  font=("Impact", 14), bg=RED, fg=WHITE,
                  relief="flat", padx=18, pady=10, cursor="hand2",
                  command=confirm).pack(side="left", padx=8)

        tk.Button(btn_row, text="🔙  Vazgeç",
                  font=("Segoe UI", 12), bg=CARD2, fg=GRAY,
                  relief="flat", padx=14, pady=10, cursor="hand2",
                  command=acc_win.destroy).pack(side="left", padx=4)

    # ──────────────────────────────────────
    #  VERDİKT (DOĞRU / YANLIŞ)
    # ──────────────────────────────────────
    def _verdict(self, suspect):
        ch = CHAPTERS[self.chapter_idx]
        correct = suspect["guilty"]

        stars = 0
        if correct:
            base = 200
            bonus = len(self.analyzed) * 20
            penalty = max(0, 50 - len(self.inventory) * 5)
            earned = base + bonus - penalty
            self.score += earned
            self.total_score += self.score
            stars = min(3, 1 + (len(self.analyzed) >= 3) + (len(self.inventory) >= ch["min_clues"] + 2))
            self.chapter_stars[self.chapter_idx] = stars
        else:
            self.score -= 50
            self.total_score += max(0, self.score)

        self._show_verdict_screen(suspect, correct, stars)

    def _show_verdict_screen(self, suspect, correct, stars):
        self._clear()
        ch = CHAPTERS[self.chapter_idx]
        f  = self.main

        canvas = tk.Canvas(f, bg=BG if correct else "#1a0505", highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        if correct:
            # BAŞARI
            canvas.create_text(640, 80, text="🎉  TEBRIKLER!", font=("Impact", 42), fill=GREEN)
            canvas.create_text(640, 150, text="DOĞRU KİŞİYİ BULDUN!",
                               font=("Consolas", 20, "bold"), fill=YELLOW)
            canvas.create_text(640, 200,
                               text=f"{suspect['emoji']}  {suspect['name']}  ({suspect['role']})",
                               font=("Impact", 22), fill=suspect["color"])
            canvas.create_text(640, 255,
                               text=f"Bölüm {ch['num']}:  {ch['title']}  çözüldü!",
                               font=("Segoe UI", 14), fill=WHITE)
            # Yıldızlar
            star_str = "⭐" * stars + "☆" * (3 - stars)
            canvas.create_text(640, 310, text=star_str,
                               font=("Segoe UI Emoji", 38), fill=YELLOW)
            canvas.create_text(640, 370, text=f"Bu bölüm skoru:  {self.score} puan",
                               font=("Consolas", 16, "bold"), fill=GOLD)
            canvas.create_text(640, 410, text=f"Toplam skor:  {self.total_score} puan",
                               font=("Consolas", 14), fill=GRAY)
        else:
            # BAŞARISIZLIK
            canvas.create_text(640, 80, text="💀  YANLIŞ KİŞİYİ SUÇLADIN!",
                               font=("Impact", 36), fill=RED)
            canvas.create_text(640, 150,
                               text=f"'{suspect['name']}' masum biri!",
                               font=("Consolas", 18), fill=WHITE)
            guilty = next(s for s in ch["suspects"] if s["guilty"])
            canvas.create_text(640, 210,
                               text=f"Gerçek suçlu:  {guilty['emoji']}  {guilty['name']}",
                               font=("Impact", 20), fill=YELLOW)
            canvas.create_text(640, 270,
                               text="Daha fazla delil toplayarak tekrar dene.",
                               font=("Segoe UI", 13), fill=GRAY)

        # Buton satırı
        btn_f = tk.Frame(canvas, bg=BG if correct else "#1a0505")
        canvas.create_window(640, 500, window=btn_f)

        if correct and self.chapter_idx < len(CHAPTERS) - 1:
            tk.Button(
                btn_f, text=f"▶  Bölüm {self.chapter_idx + 2}'ye Geç",
                font=("Impact", 17), bg=GREEN, fg=BG,
                relief="flat", padx=25, pady=12, cursor="hand2",
                command=self._next_chapter
            ).pack(side="left", padx=8)

        elif correct and self.chapter_idx == len(CHAPTERS) - 1:
            tk.Button(
                btn_f, text="🏆  Sonuç Ekranı",
                font=("Impact", 17), bg=GOLD, fg=BG,
                relief="flat", padx=25, pady=12, cursor="hand2",
                command=self._show_ending
            ).pack(side="left", padx=8)
        else:
            tk.Button(
                btn_f, text="🔄  Bu Bölümü Tekrar Oyna",
                font=("Impact", 15), bg=BLUE, fg=WHITE,
                relief="flat", padx=20, pady=12, cursor="hand2",
                command=self._show_chapter_intro
            ).pack(side="left", padx=8)

        tk.Button(
            btn_f, text="🏠  Ana Menü",
            font=("Impact", 15), bg=CARD2, fg=GRAY,
            relief="flat", padx=20, pady=12, cursor="hand2",
            command=self._show_title
        ).pack(side="left", padx=8)

    # ──────────────────────────────────────
    #  BÖLÜM GEÇİŞ
    # ──────────────────────────────────────
    def _next_chapter(self):
        self.chapter_idx += 1
        self._show_chapter_intro()

    # ══════════════════════════════════════
    #  6) OYUN SONU EKRANI
    # ══════════════════════════════════════
    def _show_ending(self):
        self._clear()
        f = self.main
        canvas = tk.Canvas(f, bg=BG, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        # Dekorasyon
        for _ in range(25):
            x = random.randint(0,1280)
            y = random.randint(0,780)
            col = random.choice([GOLD, GREEN, CYAN, PURPLE, ORANGE])
            canvas.create_text(x, y, text="✨", font=("Segoe UI Emoji",14), fill=col)

        canvas.create_text(640, 90,  text="🏆  TÜM BÖLÜMLER TAMAMLANDI!",
                           font=("Impact", 40), fill=GOLD)
        canvas.create_text(640, 155, text="İstanbul'un sırları çözüldü!",
                           font=("Segoe UI", 16, "italic"), fill=CYAN)

        # Bölüm sonuçları
        for i, ch in enumerate(CHAPTERS):
            bx, by = 180 + i*300, 240
            stars = self.chapter_stars[i]
            canvas.create_rectangle(bx-130, by, bx+130, by+180,
                                    fill=CARD, outline=GOLD, width=2)
            canvas.create_text(bx, by+25, text=f"Bölüm {i+1}",
                               font=("Consolas", 12, "bold"), fill=GRAY)
            canvas.create_text(bx, by+55, text=ch["title"],
                               font=("Impact", 13), fill=WHITE, width=240)
            canvas.create_text(bx, by+105, text="⭐" * stars + "☆" * (3-stars),
                               font=("Segoe UI Emoji", 28), fill=YELLOW)
            canvas.create_text(bx, by+155, text=f"{stars}/3 yıldız",
                               font=("Consolas", 11), fill=GRAY)

        total_stars = sum(self.chapter_stars)
        canvas.create_text(640, 465,
                           text=f"Toplam Yıldız:  {'⭐' * total_stars}{'☆' * (9-total_stars)}",
                           font=("Segoe UI Emoji", 28), fill=YELLOW)
        canvas.create_text(640, 530,
                           text=f"TOPLAM SKOR:  {self.total_score} PUAN",
                           font=("Impact", 30, "bold"), fill=GREEN)

        if total_stars >= 8:
            rank = "🥇 EFSANEVİ DEDEKTİF"
            rc = GOLD
        elif total_stars >= 5:
            rank = "🥈 UZMAN DEDEKTİF"
            rc = LBLUE
        else:
            rank = "🥉 ÇAYLAK DEDEKTİF"
            rc = GRAY

        canvas.create_text(640, 590, text=rank, font=("Impact", 26), fill=rc)

        btn_f = tk.Frame(canvas, bg=BG)
        canvas.create_window(640, 660, window=btn_f)

        tk.Button(btn_f, text="🔄  Yeniden Oyna",
                  font=("Impact", 16), bg=GREEN, fg=BG,
                  relief="flat", padx=22, pady=12, cursor="hand2",
                  command=self._restart).pack(side="left", padx=8)

        tk.Button(btn_f, text="🏠  Ana Menü",
                  font=("Impact", 16), bg=CARD2, fg=GRAY,
                  relief="flat", padx=22, pady=12, cursor="hand2",
                  command=self._show_title).pack(side="left", padx=8)

    def _restart(self):
        self.chapter_idx   = 0
        self.inventory     = []
        self.analyzed      = []
        self.score         = 0
        self.total_score   = 0
        self.chapter_stars = [0, 0, 0]
        self._show_title()

    # ──────────────────────────────────────
    #  NOTLAR KAYDET
    # ──────────────────────────────────────
    def _save_notes(self):
        ch = CHAPTERS[self.chapter_idx]
        notes = (
            f"=== Criminal Case: İstanbul Dosyaları ===\n"
            f"Bölüm {ch['num']}: {ch['title']}\n"
            f"Konum: {ch['location']}\n\n"
            f"--- Toplanan Deliller ({len(self.inventory)}) ---\n"
            + "\n".join(f"  • {c}" for c in self.inventory)
            + f"\n\n--- Analiz Edilenler ({len(self.analyzed)}) ---\n"
            + "\n".join(f"  ✓ {a}" for a in self.analyzed)
            + f"\n\n--- Skor: {self.score} ---\n"
        )
        import os
        path = os.path.join(os.path.dirname(__file__), f"dosya_bolum{ch['num']}.txt")
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(notes)
        self._set_info(f"💾  Dosya kaydedildi: dosya_bolum{ch['num']}.txt", GREEN)


# ══════════════════════════════════════════
#  BAŞLATMA
# ══════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    game = CriminalCaseGame(root)
    root.mainloop()
