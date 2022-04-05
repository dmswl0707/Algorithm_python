
n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
end = len(array)-1

def bs_first(array, target, start, end):

    if start > end:
        return None

    mid = (start+end) // 2
    if (mid==0 or target>array[mid -1]) and array[mid]==target:
        return mid
    elif array[mid]>target:
        return bs_first(array, target, start, mid - 1)
    else:
        return bs_first(array, target, mid + 1, end)

def bs_last(array, target, start, end):

    if start > end:
        return None

    mid = (start+end) // 2
    if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
        return mid
    elif array[mid]>target:
        return bs_last(array, target, start, mid - 1)
    else:
        return bs_last(array, target, mid + 1, end)


first = bs_first(array, m, 0, end)
last = bs_last(array, m, 0, end)

if first==None or last==None:
    print(-1)
else:
    print(last-first + 1)

