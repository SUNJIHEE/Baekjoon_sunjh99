dial = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]

word = input()

time = 0
for i in word:
    time += dial[ord(i) - ord('A')] + 1

print(time)
