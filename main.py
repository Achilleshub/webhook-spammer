import time
import requests
import pyfiglet
import threading
import random

print(pyfiglet.figlet_format("Achilles"))

msg = input("Lütfen WebHook Spam Mesajını Girin: ")
webhook = input("Lütfen WebHook URL'sini Girin: ")
th = int(input('Kaç tane thread (iş parçacığı) oluşturulsun? (200 önerilir): '))
sleep = int(input("Bekleme süresi ne kadar olsun? (2 önerilir): "))

def spam():
    while True:
        try:
            # Webhook'a POST isteği gönderiyoruz
            data = requests.post(webhook, json={'content': msg})

            # Eğer istek başarılıysa 204 status code dönüyorsa, başarılı mesaj gönderildiğini yazdır
            if data.status_code == 204:
                print(f"Mesaj Gönderildi: {msg}")
            else:
                print(f"Mesaj gönderilirken bir hata oluştu, HTTP Durum Kodu: {data.status_code}")
        except requests.exceptions.RequestException as e:
            # Bağlantı hatası veya diğer istek hatalarını yakalar
            print(f"Hata: {e} - Geçersiz Webhook: {webhook}")
        
        # Random bekleme süresi ekleyerek daha doğal bir işlem simüle edebiliriz
        time.sleep(sleep + random.uniform(0, 1))  # Sleep süresine küçük bir rastgelelik ekledim

# Thread'leri başlatıyoruz
for x in range(th):
    t = threading.Thread(target=spam)
    t.daemon = True  # Program sonlandığında thread'lerin de sonlanmasını sağlar
    t.start()

# Ana thread'in bitmesini engellemek için sonsuz döngü ekliyoruz
# Bu, threading işlemlerinin devam etmesini sağlar
while True:
    time.sleep(1000)
