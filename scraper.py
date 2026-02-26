import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_gold_price():
    url = "https://www.harga-emas.org/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mencari angka di dalam tabel harga emas terbaru
        # Kita cari teks yang mengandung "gram" karena biasanya harga per gram ada di sana
        rows = soup.find_all("tr")
        for row in rows:
            if "gram" in row.text.lower():
                cells = row.find_all("td")
                for cell in cells:
                    digits = ''.join(filter(str.isdigit, cell.text))
                    if len(digits) >= 6: # Harga emas biasanya 6-7 digit (jutaan)
                        return int(digits)
        
        # Jika cara di atas gagal, coba cara cadangan (default)
        return 1250000 
    except Exception as e:
        print(f"Error scraping: {e}")
        return 1250000 # Return harga terakhir jika gagal agar file tidak rusak

# Update data.json
data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "gold_price": get_gold_price(),
    "inflation": 0.03,
    "sbn_rate": 0.06
}

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
