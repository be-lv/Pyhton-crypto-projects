from binance.client import Client
import time

# === Paste your keys here (DO NOT commit to GitHub) ===
API_KEY = "your_api_key_here"
API_SECRET = "your_secret_key_here"

client = Client(API_KEY, API_SECRET)

symbol = input("Enter trading pair (e.g. BTCUSDT): ").upper()
quantity = float(input("How many units to buy/sell: "))
buy_below = float(input("Buy if price goes below: "))
sell_above = float(input("Sell if price goes above: "))

def get_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

print("\nRunning real trading bot...\n")

while True:
    try:
        price = get_price(symbol)
        print(f"[{symbol}] Current price: ${price}")

        if price <= buy_below:
            order = client.order_market_buy(
                symbol=symbol,
                quantity=quantity
            )
            print(">>> BOUGHT at", price)
            break  # stop after buying

        elif price >= sell_above:
            order = client.order_market_sell(
                symbol=symbol,
                quantity=quantity
            )
            print(">>> SOLD at", price)
            break  # stop after selling

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
