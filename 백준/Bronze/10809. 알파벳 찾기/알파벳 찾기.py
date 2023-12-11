word = input()

alphabet_positions = [-1] * 26

for i in range(len(word)):
    if 'a' <= word[i] <= 'z':
        index = ord(word[i]) - ord('a')
        if alphabet_positions[index] == -1:
            alphabet_positions[index] = i

for position in alphabet_positions:
    print(position, end=' ')
