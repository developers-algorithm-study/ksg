import sys
n = int(input())

DS = []
NAME = 0
SCORES = 1
for i in range(n):
    Name, *Scores = input().split(" ")
    Scores = list(map(int, Scores))
    DS.append([Name, Scores])

DS.sort(key=lambda x: x[1][0], reverse=True)


NumberOneStudent = DS[0]
del DS[0]

sys.stdout.write(NumberOneStudent[NAME] + " ")
for i in range(1, n):
    Rank = 1
    for Other in DS:
        if NumberOneStudent[SCORES][i] < Other[SCORES][i]:
            Rank += 1

    sys.stdout.write(str(Rank) + " ")
        
