const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]


function solution(K, N, M, chargers) {
    // solution 함수 완성
    let result = 0
    let p = 0
    let flag = true

    while (p < N-K) {
        result += 1
        p += K
        if (chargers.includes(p)) {
            continue
        }
        let temp = 0
        while (true) {
            p -= 1
            temp += 1
            if (temp >= K) {
                p += N
                console.log(0)
                flag = false
                break
            }
            if (chargers.includes(p)) {
                break
            }
        }
    }
    if (flag === true) {
        console.log(result)
    }
    }

for (const input of inputs) {
solution(input[0], input[1], input[2], input[3])
}