n, m = input().split()

if int(n[::-1]) > int(m[::-1]):
    print(int(n[::-1]))
else:
    print(int(m[::-1]))