import os

import requests
from dotenv import load_dotenv

# .env dosyasındaki API anahtarını yükle
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API anahtarı bulunamadı. Lütfen .env dosyasını kontrol edin.")


def fetch_max_quality_satellite_image(location, zoom=16, size="640x640", scale=2):
    """
    Belirtilen konum için maksimum çözünürlükte ve en kaliteli uydu görüntüsünü PNG formatında indirir.
    Eğer belirtilen konum için dosya mevcutsa, API çağrısı yapmadan var olan dosyayı kullanır.

    Args:
        location (str): Konum bilgisi (örneğin, "New York, USA").
        zoom (int): Harita yakınlaştırma düzeyi (0-21 arası, varsayılan 16).
        size (str): Base boyut (örneğin "640x640").
        scale (int): Ölçek faktörü. 2 kullanıldığında görüntü 2 kat daha yüksek çözünürlükte gelir.
    Returns:
        Oluşturulan veya mevcut dosya adını (str) döndürür.
    """
    filename = f"imgs/{location.replace(' ', '_').lower()}_satellite.png"

    # Eğer dosya mevcutsa, API çağrısı yapmadan dosyanın var olduğunu bildir
    if os.path.exists(filename):
        print(f"'{filename}' dosyada mevcut. Dosyadan yüklenecek.")
        return filename

    # Dosya yoksa API'den çek
    base_url = "https://maps.googleapis.com/maps/api/staticmap"
    params = {
        "center": location,
        "zoom": zoom,
        "size": size,
        "scale": scale,
        "maptype": "satellite",
        "key": api_key,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Uydu görüntüsü '{filename}' olarak kaydedildi.")
        return filename
    else:
        print("Görüntü alınamadı. Hata kodu:", response.status_code)
        return None


if __name__ == "__main__":
    location = input("Lütfen konumu giriniz (örneğin: 'New York, USA'): ")
    fetch_max_quality_satellite_image(location)
