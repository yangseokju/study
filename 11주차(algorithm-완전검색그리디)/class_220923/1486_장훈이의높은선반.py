def cal(k):
    global result
    if k == n:
        if b > sum(check):
            return
        if result > sum(check):
            result = sum(check)
    else:
        check[k] = hei[k]
        cal(k+1)
        check[k] = 0
        cal(k+1)


T = int(input())
for tc in range(1, T+1):
    n, b = map(int,input().split())
    hei = list(map(int,input().split()))
    check = [0] * n
    result = sum(hei)

    cal(0)
    print(f'#{tc} {result - b}')