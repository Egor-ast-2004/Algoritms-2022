n = int(input())
s = list(map(int, input().split()))
lst = []
for i in s:
    if i == 0:
        lst.append(0)
    else:
        lst.append(1)
for i in range(n):
    if lst[i] != 0:
        if i != 0:
            c = lst[i - 1] + 1
        if i != n - 1:
            if lst[i + 1] == 0:
                c = 1
        lst[i] = c
print(*lst)
