"""

    在一個字典中將一個 key map 到多個值

"""


from collections import defaultdict

d = defaultdict(list)

d["a"].append(1)
d["b"].append(2)
d["c"].append(3)
d["d"]

if __name__ == "__main__":
    print(d.get("a"))
    print(d.get("test"))