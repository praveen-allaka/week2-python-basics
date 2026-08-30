# import pandas as pd
# import numpy as np
# print("Environment working!")
# print(f"Pandas version: {pd.__version__}")
# print(f"NumPy version: {np.__version__}")
# import torch
# print(f"PyTorch version: {torch.__version__}")
# print(f"GPU available: {torch.cuda.is_available()}")
# name = "pk2"
# print(f"My name is {name} and I am learning python")

# # Variables
# price = 45.50
# location = "ERCOT"
# hour = 14

# print(f"At hour {hour}, the LMP price in {location} is ${price:.2f}")

# # Simple math
# peak_price = price * 2
# print(f"Peak price estimate: ${peak_price:.2f}")

# A list of hourly LMP prices
# prices = [10.0,32.10, 41.50, 55.80, 78.20, 91.00, 85.50, 62.30, 45]

# print(f"Number of hours: {len(prices)}")
# print(f"Highest price: {max(prices)}")
# print(f"Lowest price: {min(prices)}")
# print(f"Average price: {sum(prices)/len(prices):.2f}")
# print(f"First hour price: {prices[0]}")
# print(f"Last hour price: {prices[-1]}")

# prices = [32.10, 41.50, 55.80, 78.20, 91.00, 85.50, 62.30]

# for price in prices:
#     if price > 70:
#         print(f"High price alert: ${price:.2f}")
#     else:
#         print(f"Normal price: ${price:.2f}")

# def check_price(price, threshold=70):
#     if price > threshold:
#         return f"High alert: ${price:.2f}"
#     else:
#         return f"Normal: ${price:.2f}"

# # Use it
# print(check_price(91.00))
# print(check_price(45.50))
# print(check_price(45.50, threshold=40))  # change the threshold
prices = [32.10, 41.50, 55.80, 78.20, 91.00, 85.50, 62.30]

def check_price(price, threshold=70):
    if price > threshold:
        return f"High alert: ${price:.2f}"
    else:
        return f"Normal: ${price:.2f}"

for price in prices:
    print(check_price(price))