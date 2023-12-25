n = int(input())
dots = []
for i in range(3*n):
    w = input().split(' ')
    dots.append([int(w[0]), int(w[1])])

has = {}
for i in range(n*3):
    for j in range(n*3):
        if dots[i][0] - dots[j][0] == 0:
            continue
        k = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
        if k in has:
            has[k] += 1
        else:
            has[k] = 1
print(has)
