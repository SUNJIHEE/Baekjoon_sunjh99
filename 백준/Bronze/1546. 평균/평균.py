n = int(input())
real = list(map(int, input().split()))
max = max(real)
fake = 0
for i in range(n):
    fake += real[i]/max*100
print(fake/n)