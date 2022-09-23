di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def cal(i, j, cnt, num):
    if cnt == 6:
        if num not in check_num:
            check_num.append(num)
        return
    for v in range(4):
        ni = i + di[v]
        nj = j + dj[v]
        if 0 <= ni < 4 and 0 <= nj < 4:
            cal(ni, nj, cnt + 1, num+arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    check_num = []

    for i in range(4):
        for j in range(4):
            num = ""
            num += arr[i][j]
            cal(i, j, 0, num)

    print(f'#{tc} {len(check_num)}')