def quick(arr, s, e):
    if s < e:
        k = partition(arr, s, e)
        quick(arr, s, k-1)
        quick(arr, k+1, e)

def partition(arr, s, e):
    p = arr[s]
    i, j = s, e
    while i <= j:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[s], arr[j] = arr[j], arr[s]
    return j

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    quick(arr, 0, n-1)
    print(f'#{tc} {arr[n//2]}')