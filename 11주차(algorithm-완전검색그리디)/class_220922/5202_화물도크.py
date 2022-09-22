T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    time = []
    result = 0

    for i in range(n):
        s = list(map(int, input().split()))
        time.append(s)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if time[i][1] >= time[j][1]:
                time[i], time[j] = time[j], time[i]

    for i in range(len(time)-1):
        for j in range(i+1, len(time)):
            if time[i][1] > time[j][0]:
                result += 1
                time[j] = [25,0]
    print(f'#{tc} {n-result}')