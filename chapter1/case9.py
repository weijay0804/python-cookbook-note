"""

    找出兩個字典的共通處

"""

a = {
    "x" : 1,
    "y" : 2,
    "z" : 3
}

b = {
    "w" : 10,
    "x" : 11,
    "y" : 2
}

if __name__ == "__main__":

    # 找出共通的 key
    print(a.keys() & b.keys())

    # 找出在 a 中但不在 b 的 key
    print(a.keys() - b.keys())

    # 找出共通的 value
    print(a.items() & b.items())