list = []
for _ in range(9):
    n = int(input())
    list.append(n)
max = 1
for i in range(9):
    if max < list[i]:
        max = list[i]
    continue
print(max)
for i in range(9):
    if max == list[i]:
        print(i+1)