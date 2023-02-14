from math import log2, floor

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2

def com1(A,l,r,k):
    if l < len(A):
        if len(A[l]) == len(A[r]) and len(A[l]==A[k]):
            return min(A[l],A[r],A[k])
        elif len(A[l]) == len(A[r]):
            if len(A[k])>len(A[l]):
                return min(A[l],A[r])
            else:
                return len(A[k])
        elif len(A[l]) == len(A[k]):
            if len(A[r])>len(A[l]):
                return min(A[l],A[r])
            else:
                return len(A[r])
        elif len(A[k]) == len(A[r]):
            if len(A[l])>len(A[r]):
                return min(A[r],A[k])
            else:
                return len(A[l])
        else:
            return min(len(A[l]),len(A[r]),len(A[k]))
 
def m(A,k,p):
    l = left(k)
    r = right(k)
    if l < len(A) and len(A[l]) < len(A[k]):
        smallest = l
    elif l < len(A):
        if len(A[l]) == len(A[k]) and A[l] < A[k]:
            smallest = l
        else:
            smallest = k
    if r < len(A):
        if len(A[r]) < len(A[smallest]):
            smallest = r
        elif len(A[r]) == len(A[smallest]) and A[r] < A[k]:
            smallest = r
        else:
            pass
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        if smallest not in range(p-1,2**(floor(log2(p)))-2,-1):
            m(A, smallest, len(A))
        else:
            pass

def build_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        m(A,k,len(A))
        print(b)
        print(k)

a = int(input())

b = []
for i in range(a):
    b.append(input())

build_heap(b)
print(b)