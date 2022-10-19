// 1. people에서 admin 권한을 가진 요소를 찾으세요.
const people = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true },
]

// answer
const s=[]
people.find((find_s) => {
  if (find_s.admin == true) {
    s.push(find_s)
  }
})
console.log(s)


// 2. accounts에서 잔액이 24,000인 사람을 찾으세요.
const accounts = [
  { name: 'justin', balance: 1200 },
  { name: 'harry', balance: 50000 },
  { name: 'jason', balance: 24000 },
]

// answer
const s2=[]
accounts.find((find_s2) => {
  if (find_s2.balance == 24000) {
    s2.push(find_s2)
  }
})
console.log(s2)