import requests

symbol = "BTCUSDT"
url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit=5000"

response = requests.get(url)
data = response.json()

print(data)
