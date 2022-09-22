T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int,input().split()))
    player1 = []
    player2 = []
    result = 0

    for i in range(0, 12, 2):
        player1.append(num_list[i])
        player1.sort()
        player2.append(num_list[i+1])
        player2.sort()

        if len(player1) < 3:
            continue
        else:
            for v in range(len(player1)-1):
                cnt = 1
                for w in range(v+1, len(player1)):
                    if player1[v] == player1[w]:
                        cnt += 1
                        if cnt == 3 and result == 0:
                            result = 1
                            break
                    else:
                        break
            for v in range(len(player1)-1):
                cnt = 1
                k = 1
                test = player1[v]
                for w in range(v+1, len(player1)):
                    if player1[v] == player1[w]-k:
                        cnt += 1
                        k += 1
                        test = player1[w]
                        if cnt == 3 and result == 0:
                            result = 1
                            break
                    elif test == player1[w]:
                        continue
                    else:
                        break
            for v in range(len(player2)-1):
                cnt = 1
                for w in range(v+1, len(player2)):
                    if player2[v] == player2[w]:
                        cnt += 1
                        if cnt == 3 and result == 0:
                            result = 2
                            break
                    else:
                        break
            for v in range(len(player2)-1):
                cnt = 1
                k = 1
                test = player2[v]
                for w in range(v+1, len(player2)):
                    if player2[v] == player2[w]-k:
                        cnt += 1
                        k += 1
                        test = player2[w]
                        if cnt == 3 and result == 0:
                            result = 2
                            break
                    elif test == player2[w]:
                        continue
                    else:
                        break

    print(f'#{tc} {result}')