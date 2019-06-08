n, m = list(map(int, input().split(" ")))
l = []

for i in range(n):
    Name, Score = input().split(" ")
    l.append([Name, int(Score)])

l.sort(key = lambda x: x[1], reverse=True)

for i in range(m):
    print(l[i][0])