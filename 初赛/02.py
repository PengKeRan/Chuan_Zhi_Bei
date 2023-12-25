n = int(input())
arr = input().split(' ')
arr = [int(arr[i]) for i in range(n)]

arr = sorted(arr)
res = arr[1] - arr[0]
for i in range(2, n):
    temp = arr[i] - arr[i-1]
    if temp < res:
        res = temp
print(res)




