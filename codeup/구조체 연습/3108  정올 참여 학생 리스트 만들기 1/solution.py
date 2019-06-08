import sys
import bisect
n = int(input())

data = []
names = []
for _ in range(n):
    c, no, name = input().split(" ")
    no = int(no)
    if no not in data:
        if c == 'I':
            data.append(no)
            names.append(name)
    else:
        if c == 'D':
            i = bisect.bisect(data, no)
            del data[i-1]
            del names[i-1]

S = False
R = sorted(list(zip(data, names)), key=lambda x:x[0])
for x in input().split(" "):
    if S: sys.stdout.write("\n")
    x = int(x) - 1
    sys.stdout.write(str(R[x][0]) + " " + R[x][1])
    S = True

    
