CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) insert 구문을 사용하면 순서를 지정하지 않으면 create 에서 생성한 순서대로 데이터가 들어가는데
-- 추가하는 데이터의 타입이 맞지 않아 오류가 발생되었다.
INSERT INTO zoo (age, weight, height, name, eat)
VALUES (5, 180, 210, 'gorilla', 'omnivore');

-- 2) rowid는 기본키를 설정하지 않았을때 자동으로 생성되는 pk 컬럼명인데 
-- 기본적으로 not null, unique 속성을 가지므로 rowid에 같은 데이터가 들어가 오류가 발생하였다.
INSERT INTO zoo (rowid, name, eat, weight, age) 
VALUES
(9, 'dolphin', 'carnivore', 210, 3),
(10, 'alligator', 'carnivore', 250, 50);

-- 3) height나 age는 기본값인 NULL 속성으로 지정되어 값이 NULL이 되어도 되지만
-- name, eat, weight 컬럼은 생성시 NOT NULL로 지정하여 만들었기 때문에 무조건 NULL이 아닌 값이 있어야한다.
INSERT INTO zoo (name, eat, weight, age) 
VALUES
('dolphin', 'carnivore', 150, 3);
