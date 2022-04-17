"""

    維持字典的順序

"""

from collections import OrderedDict
import json

d = OrderedDict()

d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4


if __name__ == "__main__":
    for key in d:
        print(key)

    print(json.dumps(d))

    