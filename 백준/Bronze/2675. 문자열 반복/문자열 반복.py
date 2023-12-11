num = int(input())

lists = []

for i in range(num):
    n, word = input().split()
    list = ""
    for j in range(len(word)):
        list += (word[j]*int(n))
    lists.append(list)

for i in range(num):
    print(lists[i])