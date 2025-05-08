# core/speaker.py
# Açıklama: Gerçek zamanlı sesli bildirim sistemi.
# Amaç: Kuyruk tabanlı yapı ile pyttsx3 motoru kullanarak konuşmaları yönetmek.

import threading
import pyttsx3
import queue
import time

# --- Başlangıç Ayarları ---
engine = pyttsx3.init()  # Ses motorunu başlat
engine.setProperty('rate', 150)   # Konuşma hızı ayarı (kelime/dakika)
engine.setProperty('volume', 1.0)  # Ses seviyesi (1.0 = maksimum)

# Konuşma sırasını kontrol eden kuyruk ve durum değişkeni
speak_queue = queue.Queue()
currently_speaking = False

def speak(text):
    """
    Yeni bir konuşma mesajı ekler.
    Args:
        text (str): Seslendirilecek metin.
    """
    speak_queue.put(text)  # Mesajı kuyruğa ekle

def speaker_worker():
    """
    Kuyruktaki mesajları sırayla seslendiren işçi thread.
    Her zaman bir mesaj bittiğinde sıradakine geçer.
    """
    global currently_speaking
    while True:
        text = speak_queue.get()  # Kuyruktan mesaj al
        if text is None:
            break  # None gelirse threadi durdur (şu anda kullanılmıyor)
        currently_speaking = True
        print(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
        currently_speaking = False
        speak_queue.task_done()  # Mesajı tamamladı olarak işaretle

# TODO: Gerçek zamanlı sistemde kuyruk büyürse eski mesajlar güncellenmeden sıraya girebilir.
# TODO: İlerleyen sürümlerde kuyruk temizleme veya güncel veriyi güncelleme sistemi eklenmeli.


# --- Arka planda sürekli çalışan konuşma işçisi thread başlat ---
threading.Thread(target=speaker_worker, daemon=True).start()
