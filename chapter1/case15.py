"""

    基於一個欄位來為記錄分組

"""


rows = [ 
    {"address" : "5421 N CLARK", "date" : "2021/01/02"},
    {"address" : "5418 M CLARK", "date" : "2021/01/02"},
    {"adress" : "5800 E 58TH", "date" : "2022/10/01"},
    {"adress" : "2122 N CLARK", "date" : "2021/05/12"},
    {"adress" : "1060 W ADDISON", "date" : "2021/05/12"},
    {"adress" : "1039 W GRANVILLE", "date" : "2021/01/02"}
]

from operator import itemgetter
from itertools import groupby

# 需要先排序，將同個日期的排在一起
rows.sort(key = itemgetter("date"))

for date, items in groupby(rows, key=itemgetter("date")):
    print(date)

    for i in items:
        print(' ' * 10, i)

from collections import defaultdict

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row["date"]].append(row)

for r in rows_by_date["2021/01/02"]:
    print(r)
    