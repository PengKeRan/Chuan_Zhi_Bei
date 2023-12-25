w = input().split(' ')
n = int(w[0])
k = int(w[1])
arr = input()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
res = [0 for i in range(26)]
for i in range(n):
    for j in range(26):
        if arr[i] == alphabet[j]:
            res[j] += 1
res = sorted(res, reverse=True)
score = 0
temp = k
for i in range(k):
    if temp <= 0:
        break
    if res[i] <= temp:
        score += res[i] * res[i]
        temp -= res[i]
    else:
        score += temp*temp
        temp = 0
print(score)