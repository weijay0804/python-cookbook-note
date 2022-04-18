"""

    找出一個序列中出現最頻繁的項目

"""

words = [ 
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    "the", 'eye', 'the', 'eye', 'the', 'eyes', 'not', 'around',
    "the", 'eyes', 'look', 'around'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)