"""

    取出一個字典的子集合

"""

prices = {
    "ACME" : 45.23,
    "AAPL" : 612.78,
    "IBM" : 205.55,
    "HPQ" : 37.20,
    "FB" : 10.75
}

# 找出股價大於 200 的股票
p1 = {key : value for key, value in prices.items() if value > 200}

# 製作科技股字典
tech_names = {"AAPL", "IBM", "HPQ", "MSFT"}
p2 = {key : value for key, value in prices.items() if key in tech_names}


if __name__ == "__main__":
    print(p1)
    print(p2)

