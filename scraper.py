import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_gold_price():
    # Contoh ambil dari situs harga-emas.org (Bisa diganti sesuai kebutuhan)
    url = "https://www.harga-emas.org/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Mencari angka harga emas (logika scraping sederhana)
    price_text = soup.find("td", {"style": "font-weight:bold; color:#000000;"}).text
    # Bersihkan teks jadi angka (misal: 1.250.000 -> 1250000)
    price = int(''.join(filter(str.isdigit, price_text)))
    return price

# Update data.json
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "gold_price": get_gold_price(),
    "inflation": 0.03, # Bisa diset manual atau scraping juga
    "sbn_rate": 0.06
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
