n = int(input())

strings = []

for _ in range(n):
    string = input()
    strings.append(string)

for i in range(n):
    print(strings[i][0] + strings[i][len(strings[i])-1])