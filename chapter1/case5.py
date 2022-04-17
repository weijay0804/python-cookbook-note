"""

    實作一個優先佇列

"""

import heapq

class Item:

    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Item {self.name}"



class PriorityQueue:
    """ 優先佇列 """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item : Item, priority : int):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]



if __name__ == "__main__":

    q = PriorityQueue()

    foo = Item("foo")
    bar = Item("bar")
    spam = Item("spam")
    grok = Item("grok")

    q.push(foo, 1)
    q.push(bar, 3)
    q.push(spam, 5)
    q.push(grok, 1)

    for _ in range(len(q._queue)):
        print(q.pop())