# main.py
# Oyunu başlatan ana giriş dosyası

# Tkinter kütüphanesini içe aktar
# Grafik arayüz oluşturmak için kullanılır
import tkinter as tk

# Ana oyun sınıfını içe aktar
from oyun import CriminalCaseOyunu


# Bu blok sadece dosya doğrudan çalıştırıldığında çalışır
# Başka bir dosyadan import edilirse çalışmaz
if __name__ == "__main__":

    # Ana uygulama penceresini oluştur
    kok = tk.Tk()

    # Oyun sınıfını başlat
    # Tüm oyun ekranları bu pencere üzerinde çalışır
    CriminalCaseOyunu(kok)

    # Tkinter olay döngüsünü başlat
    # Pencerenin açık kalmasını sağlar
    kok.mainloop()
