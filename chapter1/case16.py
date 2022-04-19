"""

    過濾序列的元素

"""

from itertools import  compress

mylist = [1, 4, 5, -1 ,10 ,5, 3, 10, -92]

list1 = [n for n in mylist if n > 0]
list2 = [n for n in mylist if n < 0]

def is_int(val):
    try:
        x = int(val)
        return True
    
    except:
        return False


if __name__ == "__main__":
    print(list1)
    print(list2)

    values = ["1", "2", "-1", "-", "N/A", "5"]
    ivals = list(filter(is_int, values))
    print(ivals)

    addresses = [ 
        "5412 N CLARK",
        "5148 N CLARK",
        "5800 E 58TH",
        "2122 N CLARK",
        "5645 N RAVENSWOOD",
        "1060 W ADDISON",
        "4801 N BROADWAY"
    ]

    counts = [0, 5, 3, 9, 10, 56, 1]

    more5 = [n > 5 for n in counts]
    print(more5)
    print(list(compress(addresses, more5)))



    