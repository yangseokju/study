T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().split())
    n_list = list(map(int,input().split())) # 화물의 크기들   # 1 5 3
    m_list = list(map(int,input().split())) # 트럭의 적재량들 # 8 3

    result = 0
    while True:
        n_max_num = 0
        for i in range(len(n_list)):
            if n_max_num <= n_list[i]:
                n_max_num = n_list[i]
                n_max_index = i
        
        m_max_num = 0
        for i in range(len(m_list)):
            if m_max_num <= m_list[i]:
                m_max_num = m_list[i]
                m_max_index = i
        
        if m_max_num >= n_max_num:
            result += n_max_num
            n_list.pop(n_max_index)
            m_list.pop(m_max_index)
        else:
            n_list.pop(n_max_index)
        
        if len(n_list) == 0 or len(m_list) == 0:
            break
    print(f'#{tc} {result}')