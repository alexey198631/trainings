"""

Example 1, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list
[[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]

Example 2, if L = [1, 1, 1, 1, 4] and n = 2 then your function should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]

    def itrf(M, x):
        itr = []
        if len(M) >= x:
            for l in range(0, x):
                itr.append(M[l])
                print(itr)
            ans.append(itr)
            return itrf(M[1:], x)

"""

L = [5, 2, 4, 1, 3]

n = 1


def getSublists(L, n):
    ans = []
    while len(L) >= n:
        itr = []
        for x in range(0, n):
            itr.append(L[x])
        ans.append(itr)
        L = L[1:]

    return ans


print(getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2], 8))


