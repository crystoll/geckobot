# Geckobot

## What is it?

This is a tiny bot that uses Coingecko API to fetch cryptocurrency prices, based on a defined list of cryptocurrencies. Then it will check if the price is higher than a defined threshold. If the price is higher, it will send a message to a Discord chat.

Motivation for this little script is to keep sane in Cryptowinter periods. No need to check the price of every cryptocurrency every time. The bot will alarm if there's a significant enough price increase to warrant a message. And then the thresholds may be readjusted based on your hunger.

To put it short, activating this bot with proper parameters allows you to forget obsessing about your wallets and crypto daily or hourly prices. Instead it lets you focus on other things than crypto prices. If it pings you one day, you may wake up to pleasant news.

## Prerequisites

pip install pycoingecko discord-webhook python-dotenv

You will also need to add a .env file that contains your Discord Webhook URL, since it's a secret that should not be put to Git, and will vary depending on your Discord server. For this, I provided a sample.env file, that you can rename to .env and add your Webhook URL.

Finally, edit the coins_and_thresholds.json tile to setup your own coins and price thresholds to alarm. Use Coingecko ticket names for this, see the provided examples.

## Use

python check_prices.py

## Install

Preferred way to run this is to set it up as a cron job/service. This is outside the scope of this README, however, as it depends on your own setup, and can be done in various different ways.