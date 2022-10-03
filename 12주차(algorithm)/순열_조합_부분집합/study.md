## 순열

1. 단순하게 순열을 생성하는 방법
```python
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```
1. 재귀 호출을 통한 순열 생성
```python
def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]] + p)
    return result

arr = [1, 2, 3, 4]
print(perm(arr, 3))
```

## 조합
1. 재귀호출을 이용한 조합 생성 알고리즘
```python
an[] : n개의 원소를 가지고 있는 배열
tr[] : r개의 크기의 배열, 조합이 임시 저장될 배열

def comb(n, r):
    if r == 0:
        print(tr)
    else:
        if n < r:
            return
        else:
            tr[r-1] = arr[n-1]
            comb(n-1, r-1)
            comb(n-1, r)

arr = [1, 2, 3, 4, 5]
tr = [0] * 2
comb(5, 2)
```

## 부분집합
1. 바이너리 카운팅(모든 부분집합을 출력)
```python
def counting():
    for i in range(1 << n):
        s = []
        for j in range(i):
            if i & (1 << j):
                s.append(j)
        p.append(s)


arr = [1, 2, 3, 4]
n = len(arr)
p = []
counting()
print(p)
```

2. 부분집합의 합 구현하기
- 아래의 10개의 정수 집합에 모든 부분 집합 중 원소의 합이 0이 되는 부분집합을 모두 출력하시오.
- [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
```python
def cal():
    for i in range(1 << n):
        s = []
        sum_num = 0
        for j in range(i):
            if i & (1 << j):
                s.append(j)
        for v in s:
            sum_num += arr[v]
        if sum_num == 0:
            s2 = []
            for w in s:
                s2.append(arr[w])
            result.append(s2)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
result = []
cal()
print(result)
print(len(result))
```