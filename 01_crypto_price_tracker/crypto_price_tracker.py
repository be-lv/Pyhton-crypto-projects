import requests

def get_price(coin_id="bitcoin", currency="usd"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}"
    response = requests.get(url)
    data = response.json()
    price = data[coin_id][currency]
    return price

print("Crypto Price Tracker")
print("----------------------")

while True:
    coin = input("Enter coin name (e.g. bitcoin, ethereum) or 'exit': ").lower()
    if coin == 'exit':
        break
    try:
        price = get_price(coin)
        print(f"Current price of {coin}: ${price}")
    except Exception as e:
        print("Error fetching price. Make sure the coin name is correct.")
