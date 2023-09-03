all = set(range(1,31))
list = set()
for _ in range(28):
    n = int(input())
    list.add(n)

res = sorted(all-list)
print(*res, sep='\n')