


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

n = 4

ans = []
itr = []
while len(L) >= n:
    ans.append(itr)
    itr = []
    for x in range(0, n):
        itr.append(L[x])
    L = L[1:]

print(ans[1:])
