T = int(input())
for tc in range(1, T+1):
    n = list(input()) # 2진수 # 1010
    m = list(input()) # 3진수 # 212
    stop = True
    i = -1

    while stop:
        i += 1
        for j in range(len(m)):
            a, b, k, t = 0, 0, 1, 1
            # 2진수부터 0 이면 1 , 1 이면 0으로 바꿔준다.
            if int(n[i]) == 0:
                n[i] = 1
                for v in range(len(n)-1, -1, -1):
                    a += int(n[v])*k
                    k *= 2
                n[i] = 0
            elif int(n[i]) == 1:
                n[i] = 0
                for v in range(len(n)-1, -1, -1):
                    a += int(n[v])*k
                    k *= 2
                n[i] = 1
            # 3진수일때 0, 1, 2가 나올경우
            if int(m[j]) == 0:
                m[j] = 1
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                b, t = 0, 1
                m[j] = 2
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                m[j] = 0

            elif int(m[j]) == 1:
                m[j] = 2
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                b, t = 0, 1
                m[j] = 0
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                m[j] = 1

            elif int(m[j]) == 2:
                m[j] = 0
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                b, t = 0, 1
                m[j] = 1
                for w in range(len(m)-1, -1, -1):
                    b += int(m[w])*t
                    t *= 3
                if a == b:
                    result = a
                    stop = False
                    break
                m[j] = 2
    print(f'#{tc} {result}')