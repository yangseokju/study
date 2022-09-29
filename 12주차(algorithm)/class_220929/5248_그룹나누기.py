def check(x):
    if arr[x] == x:
        return x
    else:
        return check(arr[x])


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [i for i in range(n+1)]
    number = list(map(int, input().split()))

    for i in range(m):
        arr[check(number[2*i+1])] = check(number[2*i])

    count = 0
    for i in range(1, n+1):
        if i == arr[i]:
            count += 1

    print(f'#{tc} {count}')