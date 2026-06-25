# veri.py
# Oyun içerisindeki tüm bölüm, şüpheli ve delil verileri burada tutulur.

# ══════════════════════════════════════
# BÖLÜMLER LİSTESİ
# ══════════════════════════════════════

BOLUMLER = [

  
    # 1. BÖLÜM
  
    {
        # Bölüm numarası
        "num": 1,

        # Bölüm başlığı
        "title": "MÜZEDEKİ CİNAYET",

        # Olay yeri konumu
        "location": "📍 Şehir Tarih Müzesi, İstanbul",

        # Kullanılacak sahne türü
        "sahne_turu": "muze",

        # Bölüm hikayesi
        "hikaye": (
            "Şehir Tarih Müzesi'nde değerli Osmanlı madalyaları çalındı!\n"
            "Müze bekçisi Ahmet Bey bayıltılmış halde bulundu.\n\n"
            "Gece yarısı gerçekleşen bu soygunun faillini bulmak için\n"
            "müzeyi dikkatlice incele, delilleri topla ve\n"
            "laboratuvarda analiz et. Suçluyu yakala!"
        ),

        # Şüpheli listesi
        "supheliler": [

            # Şüpheli 1
            {
                # Şüpheli adı
                "isim": "Prof. Kaplan",

                # Mesleği / rolü
                "rol": "Baş Küratör",

                # Arayüzde kullanılacak renk
                "renk": "#dc2626",

                # Emoji simgesi
                "emoji": "🎓",

                # Suçlu mu?
                "suclu": False,

                # Karakter açıklaması
                "biyografi": (
                    "25 yıllık tecrübeli küratör.\n"
                    "Çok dürüst ve düzgün biri\n"
                    "olarak tanınıyor."
                ),

                # Şüpheliye ait deliller
                "deliller": [
                    "Profesörün not defteri",
                    "Kırmızı boya lekesi"
                ],
            },

            # Şüpheli 2
            {
                "isim": "Zeynep Avcı",
                "rol": "Güvenlik Şefi",
                "renk": "#7c3aed",
                "emoji": "🔐",
                "suclu": False,

                "biyografi": (
                    "Tüm güvenlik kodlarını biliyor.\n"
                    "O gece alarmı neden\n"
                    "kapattı?"
                ),

                "deliller": [
                    "Zeynep'in anahtarı",
                    "Mor iplik"
                ],
            },

            # Şüpheli 3 (Gerçek suçlu)
            {
                "isim": "Mert Demir",
                "rol": "Restoratör",
                "renk": "#0284c7",
                "emoji": "🎨",

                # Gerçek suçlu
                "suclu": True,

                "biyografi": (
                    "2 ay önce işe başladı.\n"
                    "Geçmişi pek temiz değil...\n"
                    "Borçları olduğu söyleniyor."
                ),

                "deliller": [
                    "Mert'in parmak izi",
                    "Mavi boya tüpü",
                    "Mert'e ait çanta"
                ],
            },
        ],

        # Olay yerinde bulunabilecek tüm deliller
        "tum_deliller": [

            "🔍 Kırık Cam Parçası",
            "🩸 Kan Lekesi",

            "📌 Düşmüş Rozet",
            "🧵 Yırtık Kumaş",

            "👣 Ayak İzi",
            "🚬 Sigara İzmariti",

            "📝 Şifreli Not",
            "🎨 Mavi Boya Tüpü",

            "👆 Parmak İzi",
            "⚗️ Kimyasal Leke",

            "🔘 Kopuk Düğme",
            "💡 Yanık Tel",
        ],

        # Suçluyu kanıtlayan özel deliller
        "suclu_deliller": [
            "🎨 Mavi Boya Tüpü",
            "👆 Parmak İzi",
            "📌 Düşmüş Rozet"
        ],

        # Bölümü geçmek için gereken minimum delil sayısı
        "min_delil": 5,
    },

    # 2. BÖLÜM

    {
        "num": 2,

        "title": "LİMANDAKİ ŞIFRE",

        "location": "📍 Eski İstanbul Limanı",

        "sahne_turu": "liman",

        "hikaye": (
            "Eski İstanbul Limanı'nda bir gemi gece yarısı karaya oturdu!\n"
            "Kaptan ortada yok, değerli kargo tamamen çalınmış.\n\n"
            "Şifreli mesajları çöz, gizli belgeleri bul ve bu\n"
            "karanlık operasyonun arkasındaki kişiyi ortaya çıkar!\n"
            "Zaman daralıyor..."
        ),

        # Şüpheliler
        "supheliler": [

            # Kaptan
            {
                "isim": "Kaptan Yıldız",
                "rol": "Eski Kaptan",
                "renk": "#d97706",
                "emoji": "⚓",
                "suclu": False,

                "biyografi": (
                    "30 yıllık denizci.\n"
                    "Sigortacılarla sorunları var\n"
                    "ama hep dürüst biri oldu."
                ),

                "deliller": [
                    "Kaptanın günlüğü",
                    "Turuncu halat"
                ],
            },

            # Gerçek suçlu
            {
                "isim": "Selma Koç",
                "rol": "Gümrük Müdürü",
                "renk": "#059669",
                "emoji": "📋",

                "suclu": True,

                "biyografi": (
                    "Tüm gümrük belgelerini\n"
                    "düzenliyor. Banka hesabında\n"
                    "şüpheli para var."
                ),

                "deliller": [
                    "Selma'nın mühürü",
                    "Gizli belge",
                    "Yeşil mürekkep"
                ],
            },

            # Bekçi
            {
                "isim": "Hakan Bulut",
                "rol": "Liman Bekçisi",
                "renk": "#be185d",
                "emoji": "🔦",
                "suclu": False,

                "biyografi": (
                    "10 yıldır limanı koruyor.\n"
                    "O gece nöbetini erken\n"
                    "bıraktı. Neden?"
                ),

                "deliller": [
                    "Hakan'ın el feneri",
                    "Pembe boya izi"
                ],
            },
        ],

        # Limanda bulunabilecek deliller
        "tum_deliller": [

            "💧 Islak Ayak İzi",
            "📦 Hasar Görmüş Sandık",

            "📜 Şifreli Mesaj",
            "🪝 Metal Kanca",

            "🌿 Deniz Yosunu",
            "📋 Sahte Belge",

            "🧭 Kırık Pusula",
            "🔏 Mühür Baskısı",

            "⛽ Gemi Yağı",
            "🖊️ Yeşil Mürekkep",

            "🪢 Kopuk Halat",
            "🔑 Yedek Anahtar",
        ],

        # Gerçek suçluyu kanıtlayan deliller
        "suclu_deliller": [
            "📋 Sahte Belge",
            "🔏 Mühür Baskısı",
            "🖊️ Yeşil Mürekkep"
        ],

        # Minimum gerekli delil
        "min_delil": 6,
    },

    # 3. BÖLÜM

    {
        "num": 3,

        "title": "KARANLIK ORMAN SIRRI",

        "location": "📍 Belgrad Ormanı Derinlikleri",

        "sahne_turu": "orman",

        "hikaye": (
            "Belgrad Ormanı'nın derinliklerinde insan kemikleri bulundu!\n"
            "DNA analizi 10 yıl öncesine işaret ediyor.\n\n"
            "Bu soğuk dava kapandı sanılıyordu. Ama sen\n"
            "gerçeği gün yüzüne çıkarmak için son bir şansa sahipsin.\n"
            "Delilleri topla, suçluyu mahkûm et!"
        ),

        # Şüpheliler
        "supheliler": [

            # Gerçek suçlu
            {
                "isim": "Dr. Şahin",
                "rol": "Orman Mühendisi",
                "renk": "#6d28d9",
                "emoji": "🧪",

                "suclu": True,

                "biyografi": (
                    "Eski bir araştırmacı.\n"
                    "O dönemde ormanda çok\n"
                    "zaman geçiriyordu."
                ),

                "deliller": [
                    "Dr. Şahin'in rozeti",
                    "Mor ilaç şişesi",
                    "Şahin'e ait DNA"
                ],
            },

            # Botanik uzmanı
            {
                "isim": "Leyla Yurt",
                "rol": "Botanik Uzmanı",
                "renk": "#15803d",
                "emoji": "🌿",
                "suclu": False,

                "biyografi": (
                    "Ormandaki bitkileri\n"
                    "araştırıyor. Çok sakin\n"
                    "ve nazik biri."
                ),

                "deliller": [
                    "Leyla'nın not defteri",
                    "Yeşil boya"
                ],
            },

            # Avcı rehberi
            {
                "isim": "Rıza Kara",
                "rol": "Avcı Rehberi",
                "renk": "#92400e",
                "emoji": "🏹",
                "suclu": False,

                "biyografi": (
                    "Ormanda yıllardır rehberlik\n"
                    "yapıyor. O gece ormanda\n"
                    "mıydı gerçekten?"
                ),

                "deliller": [
                    "Rıza'nın çakısı",
                    "Kahve renkli tüy"
                ],
            },
        ],

        # Ormanda bulunabilecek deliller
        "tum_deliller": [

            "🦴 Eski Kemik",
            "🔪 Pas Tutmuş Bıçak",

            "📷 Solmuş Fotoğraf",
            "👕 Yırtık Giysi",

            "🌱 Toprak Örneği",
            "🧬 DNA İzi",

            "⌚ Kırık Saat",
            "📦 Gömülü Kutu",

            "💊 İlaç Şişesi",
            "🟣 Mor Leke",

            "📛 Rozet Parçası",
            "📰 Eski Gazete",
        ],

        # Gerçek suçluyu kanıtlayan deliller
        "suclu_deliller": [
            "🧬 DNA İzi",
            "💊 İlaç Şişesi",
            "📛 Rozet Parçası"
        ],

        # Gerekli minimum delil sayısı
        "min_delil": 7,
    },
]