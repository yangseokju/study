// 2*n-1 개만큼 공간을 만들고 * 넣어서 출력

function star(n) {
    for (let i=n-1 ; i != -1 ; i--) {
        let s = ''
        for (let v=0 ; v != i ; v++) {
            s += ' '
        }
        for (let w=0 ; w != ((2*n-1)-(2*i)) ; w++) {
            s += '*'
        }
        console.log(s)
    }
}

star(6)