CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

UPDATE users
SET country = '경기도'
WHERE first_name = '옥자' and last_name = '김';

DELETE FROM users WHERE first_name = '진호' and last_name = '백';

SELECT country, max(balance), age
FROM users
WHERE age like '3_'
GROUP BY country;
