import sys
n = int(input())

data = []
for _ in range(n):
    memo, *args = input().split(" ")
    data.append([memo, list(map(int, args))])

data.sort(key = lambda x: x[0])
data.sort(key = lambda x: x[1][2])
data.sort(key = lambda x: x[1][1])
data.sort(key = lambda x: x[1][0])

for i in data:
    print(i[0])
