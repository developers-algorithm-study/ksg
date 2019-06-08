N = int(input())

L = []
for i in range(N):
    L.append(tuple(map(int, input().split(" "))))

L.sort(key = lambda x : x[0])
for i in L:
    print(str(i[0]) + " " + str(i[1]))