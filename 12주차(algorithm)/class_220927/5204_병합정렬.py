def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    left, right = [], []
    middle = len(arr)//2

    for i in range(middle):
        left.append(arr[i])
    for j in range(middle,len(arr)):
        right.append(arr[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global result
    new_list = []
    a, b = 0, 0

    if left[-1] > right[-1]:
        result += 1
    while a < len(left) or b < len(right):
        if a < len(left) and b < len(right):
            if left[a] < right[b]:
                new_list.append(left[a])
                a += 1
            else:
                new_list.append(right[b])
                b += 1
        elif a < len(left):
            while a < len(left):
                new_list.append(left[a])
                a += 1
        elif b < len(right):
            while b < len(right):
                new_list.append(right[b])
                b += 1
    return new_list

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0

    temp = merge_sort(arr)
    print(f'#{tc} {temp[n//2]} {result}')