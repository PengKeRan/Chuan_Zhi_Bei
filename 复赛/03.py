n = int(input())
arr = input().split(' ')
for i in range(n):
    arr[i] = int(arr[i])
# n = 3
# arr = [1,3,2]

def checkPrime(num):
    for i in range(2, (num // 2)+1):
        if num % i == 0:
            return False
    return True

def scanArr(arr):
    strange = []
    for i in range(len(arr)-1):
        if not checkPrime(arr[i]+arr[i+1]):
            strange.append(i)
    return strange

def main(arr, n):
    result = []
    if n < 3:
        return -1
    if len(scanArr(arr)) == 0 or len(scanArr(arr)) > 2:
        return (-1)
    strange = scanArr(arr)
    if len(strange) == 2:
        arr2 = arr.copy()
        i = strange[0]+1
        temp = arr2[i+1]
        arr2[i+1] = arr2[i+2]
        arr2[i+2] = temp
        if len(scanArr(arr2)) == 0:
            result.append(i+2)

    if len(strange) == 1:
        arr3 = arr.copy()
        i = strange[0]
        temp = arr3[i+1]
        arr3[i+1] = arr3[i+2]
        arr3[i+2] = temp
        if len(scanArr(arr3)) == 0:
            result.append(i+2)
        else:
            arr4 = arr.copy()
            i = strange[0]
            temp = arr4[i - 1]
            arr4[i - 1] = arr4[i]
            arr4[i] = temp
            if len(scanArr(arr4)) == 0:
                result.append(i+1)
    return result

result = main(arr,n)
if len(result) != 1:
    print(-1)
else:
    print(result[0])


