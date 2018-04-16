#
## v1
def jump_search_v1(L, n, key):
    a, b = 0, int(n**0.5)
    while L[min(b, n) - 1] < key:
        a = b
        b += int(n**.5) 
        if a >= n:
          return -1
    while L[a] < key:
        a += 1
        if a == min(b, n):
            return -1
    if L[a] == key:
        return a
    return -1

### v2
import math
def jump_search_v2(arr,search):
    low = 0
    interval = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),interval):
        if arr[i] < search:
            low = i
        elif arr[i] == search:
            return i
        else:
            break
    el=low
    for j in arr[low:]:
        if j==search:
            return el
        el+=1
    return "Not found"
