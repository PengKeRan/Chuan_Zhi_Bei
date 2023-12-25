w = input().split(' ')
n = int(w[0])
a = int(w[1])
days = input().split(' ')
for i in range(n):
    days[i] = int(days[i])

cnt = 0
for i in range(0,n-1):
    if days[i] < a and days[i+1] >= a:
        cnt += 1
print(cnt)