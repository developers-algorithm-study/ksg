from bisect import bisect
N = int(input())

dic = {}
input_data = list(map(int, input().split(" ")[:-1]))
copy_data = list(input_data)
input_data.sort()

print(" ".join([str(bisect(input_data, x) - 1) for x in copy_data]))