const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

// for(i of participantNums) {
//     for (v in i) {
//         let flag = true
//         for (w in i) {
//             if (v !== w) {
//                 if (i[v] === i[w]) {
//                     flag = false
//                 }
//             }
//         }
//     if (flag === true) {
//         console.log(i[v])
//     }
//     }
// }
// // 3
// // 100
// // 62

function findSolo(arr) {
    const candidates = {};


    for (num of arr) {
        if (candidates[num] === undefined) {
            candidates[num] = 1
        } else {
            candidates[num] += 1
        }
    }

    for (candidate in candidates) {
        if (candidates[candidate] === 1) {
            console.log(candidate)
            break
        }
    }
}

participantNums.forEach(function (tc) {
    findSolo(tc)
})