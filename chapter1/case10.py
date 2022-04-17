"""

    從一個序列中移除重複的項目，並維持原本的順序

"""

def dedupe(items, key = None):
    seen = set()

    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == "__main__":
    a = [1,2,3,1,2,3,4,5,98]
    print(list(dedupe(a)))

    b = [{"x" : 1, "y" : 2}, {"x" : 1, "y" : 3}, {"x" :2, "y" : 4}, {"x" : 1, "y" : 2}]
    bb = list(dedupe(b, key= lambda data : (data["x"], data["y"]) ))
    print(bb)