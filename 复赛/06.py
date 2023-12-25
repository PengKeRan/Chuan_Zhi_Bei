w = input().split(' ')
n = int(w[0])
q = int(w[1])
s = input()
arr = [i for i in s]

commands = []
for i in range(q):
    command = input().split(' ')
    commands.append(command)

def match(arr, l1,r1,l2,r2):
    if hTree[l1][r1][l2] == 1:
        return True
    if hTree[l1][r1][l2] == 0:
        return False
    for i in range(len(arr[l1:r1])):
        if arr[l1:r1][i] != arr[l2:r2][i]:
            target = i
            for i in range(n):
                for j in range(i, n):
                    for k in range(0, n):
                        if (k + j - i > target and k <= target) or (i <= target and j > target):
                            hTree[i][j][k] = 0
            return False
    return True

# -1待定，0假，1真
hTree = [[[-1 for i in range(n)] for i in range(n)] for i in range(n)]

for command in commands:
    if command[0] == '1':
        target = int(command[1])-1
        arr[target] = command[2]
        for i in range(n):
            for j in range(i, n):
                for k in range(0, n):
                    if (k+j-i > target and k <= target) or (i <= target and j > target):
                        hTree[i][j][k] = -1
    if command[0] == '2':
        l1 = int(command[1]) - 1
        r1 = int(command[2])
        l2 = int(command[3]) - 1
        r2 = int(command[4])
        if match(arr, l1, r1, l2, r2):
            print('Yes')
            i = l1
            for i in range(l1, r1):
                for j in range(i, r1):
                    hTree[i][j][i+l2-l1] = 1
        else:
            print('No')

