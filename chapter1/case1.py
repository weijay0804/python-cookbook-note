"""

    拆解一個序列

"""

test = (1,2,3)

num1, num2, num3 = test

test2 = ["ace", 50, 31, (2012, 12, 20)]

name, num, price, (year, mon, day) = test2

if __name__ == "__main__":
    print(num1)
    print(num2)
    print("-" * 20)
    print(name)
    print(num)
    print(price)
    print(year)
    print(mon)
    print(day)
