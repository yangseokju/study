// 1. 배열에 담긴 중복된 이름을 {'이름': 수} 형태의 object로 반환하세요.

const names = ["harry", "aiden", "julie", "julie", "edward"];

// answer
const newNames = names.reduce(
  function (acc, value) {
    acc[value] += 1;
    return acc;
  },
  { harry: 0, aiden: 0, julie: 0, edward: 0 }
);

console.log(newNames);