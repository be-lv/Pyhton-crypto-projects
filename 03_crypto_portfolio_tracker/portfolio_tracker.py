import requests

# Your portfolio: coin IDs and amounts
portfolio = {
    "bitcoin": 0.002,
    "ethereum": 0.1,
    "solana": 3,
    "dogecoin": 200
}

def get_prices(coin_list):
    ids = ",".join(coin_list)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    return response.json()

def show_portfolio_value():
    prices = get_prices(portfolio.keys())
    total_value = 0
    print("\n--- Portfolio Value (Live Prices) ---\n")
    for coin, amount in portfolio.items():
        price = prices[coin]["usd"]
        value = price * amount
        total_value += value
        print(f"{coin.title()}: {amount} x ${price:.2f} = ${value:.2f}")
    
    print("\nTOTAL Portfolio Value: ${:.2f}".format(total_value))

show_portfolio_value()
