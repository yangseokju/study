def check(x):
    if arr[x] == x:
        return x
    else:
        return check(arr[x])


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [i for i in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        arr[check(b)] = check(a)

    result = 0
    for i in range(1, n+1):
        if arr[i] == i:
            result += 1
    
    print(f'#{tc} {result}')