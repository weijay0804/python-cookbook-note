"""

    最出最大或最小的 N 個項目

"""

import heapq

nums = [1, 8, 9, 10, 100, 234, -1, -234, 34]

portfolio = [ 
    {"name" : "IBM", "shares" : 100, "price" : 91.1},
    {"name" : "AAPL" , "shares" : 50, "price" : 543.22},
    {"name" : "FB", "shares" : 200, "price" : 21.09},
    {"name" : "HPQ", "shares" : 35, "price" : 31.75},
    {"name" : "YHOO", "shares" : 45, "price" : 16.35}
]

if __name__ == "__main__":
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    print("-" * 20)
    cheap = heapq.nsmallest(3, portfolio, key= lambda data : data["price"])
    expensive = heapq.nlargest(3, portfolio, key= lambda data : data["price"])
    print(cheap)
    print(expensive)