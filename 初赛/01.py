a = input()
b = input()

for i in range(len(a)):
    if a[i] not in b:
        print(a[i], end='')


