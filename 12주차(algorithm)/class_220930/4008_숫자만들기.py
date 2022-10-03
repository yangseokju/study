def cal(number, cnt, a, b, c, d):
    global min_num, max_num
 
    if cnt == n - 1:
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
        return
    if a > 0:
        cal(number + num_list[cnt+1], cnt+1, a-1, b, c, d)
    if b > 0:
        cal(number - num_list[cnt+1], cnt+1, a, b-1, c, d)
    if c > 0:
        cal(number * num_list[cnt+1], cnt+1, a, b, c-1, d)
    if d > 0:
        cal(int(number/num_list[cnt+1]), cnt+1, a, b, c, d-1)
 
 
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cal_list = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    min_num = 10000000000
    max_num = -123416543216
 
    cal(num_list[0], 0, cal_list[0], cal_list[1], cal_list[2], cal_list[3])
 
    print(f'#{tc} {max_num - min_num}')