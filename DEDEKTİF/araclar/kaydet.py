# araclar/kaydet.py — Dosya Kaydetme Yardımcısı

# İşletim sistemiyle ilgili dosya işlemlerini yapabilmek için os modülü içe aktarılır
import os


# Oyunun mevcut verilerini txt dosyasına kaydeden fonksiyon
def dosya_kaydet(oyun):

    # Fonksiyonun ne yaptığını açıklayan kısa açıklama (docstring)
    """Mevcut bölüm notlarını .txt dosyasına kaydeder."""

    # veri.py dosyasındaki BOLUMLER listesini içe aktarır
    from veri import BOLUMLER

    # Oyuncunun şu an bulunduğu bölüm bilgilerini alır
    bolum = BOLUMLER[oyun.bolum_idx]

    # Kaydedilecek metin içeriği hazırlanır
    icerik = (

        # Oyunun başlığı eklenir
        f"=== Criminal Case: İstanbul Dosyaları ===\n"

        # Bölüm numarası ve başlığı eklenir
        f"Bölüm {bolum['num']}: {bolum['title']}\n"

        # Olayın geçtiği konum eklenir
        f"Konum: {bolum['location']}\n\n"

        # Toplanan deliller başlığı ve delil sayısı yazılır
        f"--- Toplanan Deliller ({len(oyun.envanter)}) ---\n"

        # Envanterdeki tüm delilleri alt alta liste haline getirir
        + "\n".join(f"  • {d}" for d in oyun.envanter)

        # Analiz edilenler başlığı eklenir
        + f"\n\n--- Analiz Edilenler ({len(oyun.analiz_edilenler)}) ---\n"

        # Analiz edilen delilleri alt alta yazar
        + "\n".join(f"  ✓ {a}" for a in oyun.analiz_edilenler)

        # Oyuncunun skorunu ekler
        + f"\n\n--- Skor: {oyun.skor} puan ---\n"
    )

    # Şu anki dosyanın bulunduğu klasörün üst dizinini alır
    klasor = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Kaydedilecek txt dosyasının tam yolunu oluşturur
    yol = os.path.join(klasor, f"dosya_bolum{bolum['num']}.txt")

    # Dosya yazma modunda açılır (w = write)
    # encoding="utf-8" Türkçe karakter desteği sağlar
    with open(yol, "w", encoding="utf-8") as f:

        # Hazırlanan içerik dosyaya yazılır
        f.write(icerik)

    # Kaydedilen dosyanın yolu geri d