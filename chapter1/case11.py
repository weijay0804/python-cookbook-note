"""

    給一個 slice 命名

"""

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)

if __name__ == "__main__":
    print(items[2 : 4])
    print(items[a])
    print(a.start)
    print(a.stop)

    s = "HelloWorld!"
    a = slice(5, 50 , 2)
    for i in range(*a.indices(len(s))):
        print(s[i])