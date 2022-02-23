import dotenv
import json
import os
from discord_webhook import DiscordWebhook
from pycoingecko import CoinGeckoAPI


dotenv.load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
CURRENCY = 'usd'

def is_high_price(item, coins_and_thresholds):
    """
    Check if price for the item tuple is higher than the defined threshold price
    """
    return item[1].get(CURRENCY) and item[1].get(CURRENCY) > coins_and_thresholds[item[0]]


cg = CoinGeckoAPI()

with open('coins_and_thresholds.json') as json_file:
    coins_and_thresholds = json.load(json_file)


ids = list(coins_and_thresholds.keys())
print(f'Checking prices for {ids}')
coin_prices = cg.get_price(ids=ids, vs_currencies=CURRENCY)


high_prices = [item for item in coin_prices.items() if is_high_price(item, coins_and_thresholds)]
print(high_prices)

for high_price in high_prices:
    coin, price = high_price[0], high_price[1][CURRENCY]
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=f'High price for {coin}: {price} {CURRENCY}')
    response = webhook.execute()
