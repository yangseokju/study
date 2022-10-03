di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
 
def war():
 
    INF = 10000000
    D = [[INF] * n for _ in range(n)]
    D[0][0] = 0
 
    q = [[0, 0]]
    rear, tail = -1, 0
 
    while rear != tail:
        rear += 1
        a, b = q[rear][0], q[rear][1]
        for i in range(4):
            ni = di[i] + a
            nj = dj[i] + b
            if 0 <= ni < n and 0 <= nj < n:
                temp = 0
                if arr[ni][nj] > 0:
                    temp = arr[ni][nj]
                if D[ni][nj] > D[a][b] + temp:
                    D[ni][nj] = D[a][b] + temp
                    tail += 1
                    q.append([ni, nj])
    return D[n-1][n-1]
 
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
 
    print(f'#{tc} {war()}')