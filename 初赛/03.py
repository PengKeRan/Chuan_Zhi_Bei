n = int(input())
arr = input()


def func(n, arr):
    if n <= 2:
        return 0
    back = [0 for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                back[i] = back[j] + 1
                break
    front = [0 for _ in range(n)]
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[i] != arr[j]:
                front[i] += 1
            if arr[i] == arr[j]:
                front[i] += front[j]
                break

    res = 0
    for i in range(n):
        res += front[i] * back[i]
    return res

print(func(n, arr))
