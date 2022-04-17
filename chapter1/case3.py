"""

    留下 N 個項目

"""

from collections import deque

def search(lines, pattern, history = 5):
    pre_lines = deque(maxlen=history)

    for line in lines:
        if pattern in line:
            yield line, pre_lines
        
        pre_lines.append(line)

if __name__ == "__main__":

    with open("test.txt") as f:
        for line, pre_line in search(f, "python"):
            for pline in pre_line:
                print(pline, end="")
            
            print(line)
            print("-" * 20)

        
