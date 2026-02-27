import requests
import json
from datetime import datetime

def get_finance_data():
    data = {}
    
    # 1 frankfurter usd idr
    try:
        res_forex = requests.get("https://api.frankfurter.dev/v1/latest?base=USD&symbols=IDR")
        data['usd_idr'] = res_forex.json()['rates']['IDR']
    except:
        data['usd_idr'] = "Error"

    # 2 CoinGecko btc idr
    try:
        res_crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=idr")
        data['btc_idr'] = res_crypto.json()['bitcoin']['idr']
    except:
        data['btc_idr'] = "Error"

    # 3 inflation
    try:
        res_inflasi = requests.get("https://api.worldbank.org/v2/country/ID/indicator/FP.CPI.TOTL.ZG?format=json&per_page=5")
        inflation_list = res_inflasi.json()[1]
        # data terbaru  bukan none
        latest_val = next(item['value'] for item in inflation_list if item['value'] is not None)
        data['inflation_idr'] = round(latest_val, 2)
    except:
        data['inflation_idr'] = "Error"
    
    # hantam ke data.json
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    get_finance_data()
