def check(r, V):
    MST = [0] * (V + 1)  # MST 포함여부
    key = [10000] * (V + 1)  # 가중치를 최대값으로 초기화
    # key[v] => v 가 MST 속한 정점과 연결될 때의 최소 가중치
    key[r] = 0  # 시작점의 key

    for i in range(V):  # 정점중에 선택
        # MST에 포함되지 않은 정점 중에 key 가 최소인 것 찾기
        # MST[i] == 0 ==> MST에 포함되지 않은 정점
        u = 0
        minV = 10000
        for j in range(V + 1):
            if MST[j] == 0 and key[j] < minV:
                u = j
                minV = key[j]
        MST[u] = 1  # 정점 u 를 MST에 추가
        # u 에 인접한 정점들 v 에 대해서 MST 에 포함되지 않은 정점이면
        for v in range(V + 1):
            if MST[v] == 0 and adj_m[u][v] > 0:
                key[v] = min(key[v], adj_m[u][v])
                # u 를 통해서 MST 에 포함되는 비용과 기존 비용을 비교해서 최소값을 사용
    return sum(key)  # 가중치의 합


T = int(input())
for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj_m = [[0]*(v+1) for i in range(v+1)]
    adj_l = [[] for _ in range(v+1)]

    for i in range(e):
        a, b, c = map(int, input().split())

        adj_m[a][b] = c
        adj_m[b][a] = c
        adj_l[a].append((b, c))
        adj_l[b].append((a, c))

    print(f'#{tc} {check(0, v)}')