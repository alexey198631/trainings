def newSort(L):
    for i in range(len(L) - 1):
        print(L)
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                print(L[i],L[j])
                temp = L[i]
                print('temp = ', temp)
                L[i] = L[j]
                L[j] = temp
                print(L)
            j += 1

#L = [5,6,3,2,1]
#newSort(L)


def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        print(minIndx)
        minVal = L[i]
        print(minVal)
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]

            j += 1
        print(L, minIndx, minVal)
        if minIndx != i:
            temp = L[i]

            print(temp)
            L[i] = L[minIndx]
            L[minIndx] = temp
            print(L)

M = [5,6,3,2,1]

selSort(M)