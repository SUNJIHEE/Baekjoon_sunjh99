import sys
N = int(sys.stdin.readline())
for y in range(0,N):
    for x in range(0,y+1):
        print("*",end='')
    print()