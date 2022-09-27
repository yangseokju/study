def cal(n, arr, k):
    global result

    low = 0
    high = n-1
    cnt = 0

    while low <= high:
        if cnt == 0:
            mid = low + (high - low)//2
            if arr[mid] == k:
                result += 1
                return 1
            elif arr[mid] > k:
                high = mid - 1
                flag = 0
            else:
                low = mid + 1
                flag = 1
            cnt += 1
        else:
            mid = low + (high - low)//2
            if arr[mid] == k:
                result += 1
                return 1
            elif flag == 1:
                high = mid - 1
                flag = 0
            else:
                low = mid + 1
                flag = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    a.sort()
    for v in b:
        cal(n, a, v)

    print(f'#{tc} {result}')