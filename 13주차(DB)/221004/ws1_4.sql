CREATE TABLE user(
  id INTEGER PRIMARY KEY,
  firsr_name TEXT,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT,
  balance INTEGER NOT NULL
);

ALTER TABLE user RENAME COLUMN firsr_name to first_name;

INSERT INTO user(first_name, last_name, age, country, phone, balance)
VALUES
  ('미현', '김', 19, '경기도', '011-211-8482', 300),
  (NULL, '최', 33, '제주특별자치도', NULL, 300),
  ('미숙', '이', 21, '서울특별시', '010-2122-4958', 480),
  ('남석', '박', 18, '경기도', '011-484-8667', 260),
  ('철수', '박', 22, '경상남도', '016-295-8989', 500),
  (NULL, '박', 45, '전라북도', NULL, 320),
  ('민준', '이', 35, '전라남도', '019-965-8833', 350),
  (NULL, '남', 24, '충청남도', '010-5882-5969', 210),
  ('신', '유', 29, '경상북도', '010-4949-2848', 290),
  (NULL, '김', 18, '대전광역시', NULL, 300);

SELECT id, age, balance
FROM user
ORDER BY age DESC;

SELECT first_name, balance
FROM user
WHERE first_name is NOT NULL and balance > 400;

UPDATE user
SET phone='알수없음'
where phone IS NULL;
