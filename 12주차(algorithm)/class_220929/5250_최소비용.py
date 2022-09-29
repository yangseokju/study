di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs():

    INF = 10000
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = 0

    q = []
    q.append([0,0])

    while q:
        t = q.pop(0)
        a, b = t[0], t[1]
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                diff = 0
                if arr[ni][nj] - arr[a][b] > 0:
                    diff = arr[ni][nj] - arr[a][b]
                if dist[ni][nj] > dist[a][b] + diff + 1:
                    dist[ni][nj] = dist[a][b] + diff + 1
                    q.append([ni, nj])
    return dist[n-1][n-1]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc} {bfs()}')