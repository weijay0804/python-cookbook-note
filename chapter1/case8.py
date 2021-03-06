"""

    用字典進行運算

"""

prices = {
    "ACME" : 45.23,
    "AAPL" : 612.78,
    "IBM" : 205.55,
    "HPQ" : 37.20,
    "FB" : 10.75
}

if __name__ == "__main__":

    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(min_price)
    print(max_price)

    prices_sort = sorted(zip(prices.values(), prices.keys()))
    print(prices_sort)