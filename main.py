import requests
import json
import time

coin = input("Enter the coin: ")
leverage = float(input("Enter the leverage: "))
duration = float(input("Enter the duration (in minutes): "))
quantity = float(input("Enter the quantity: "))

current_price = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT").json()["price"])

print(f"\nCurrent {coin} price: {current_price}\n")

start_time = time.time()
end_time = start_time + (duration * 60)

long_short = ""

while time.time() < end_time:
    time.sleep(10)
    current_price = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT").json()["price"])
    prediction = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT").json()["price"])*0.01
    if prediction >= current_price:
        long_short = "short"
        color = "\033[31m"
    else:
        long_short = "long"
        color = "\033[32m"
    print(f"Current {coin} price: {current_price}, {color}Profit: {round(quantity*current_price*leverage*prediction/100,2)} ({round(prediction,2)}%){color}\033[0m, {color}{long_short}\033[0m")

print("\n\nTrade Summary:")
final_price = float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}USDT").json()["price"])
if final_price >= current_price:
    profit = round(quantity*final_price*leverage*(final_price-current_price)/current_price,2)
    color = "\033[32m"
else:
    profit = round(quantity*final_price*leverage*(current_price-final_price)/current_price,2)
    color = "\033[31m"
print(f"Current {coin} price: {final_price}, {color}Profit: {profit} ({round((final_price-current_price)/current_price*100,2)}%){color}\033[0m, {color}{long_short}\033[0m")
