"""

    將名稱映射至序列元素

"""

from collections import namedtuple


Subscriber = namedtuple("Subscriber", ["addr", "joined"])
sub = Subscriber("jonesy@example.com", "2012-10-19")

Stock = namedtuple("Stock", ["name", "shares", "price", "date", "time"])

def dict_to_stock(s):
    stock_prototype = Stock('', 0, 0.0, None, None)
    return stock_prototype._replace(**s)

if __name__ == "__main__":
    print(sub)
    print(sub.addr)
    print(sub.joined)

    a = {"name" : "ACME", "shares" : 100, "price" : 123.45}

    print(dict_to_stock(a))