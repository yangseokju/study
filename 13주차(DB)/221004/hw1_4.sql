CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;

-- 첫번째 delete문은 commit 되기 전에 rollback되어서 결과적으로 실행되지 않았고, 두 번째 delete문은 commit되어서 eat가 'omnivore'인 레코드들의 데이터는 삭제되었다. 그러므로 3개의 레코드들만 남게되어 결과로 3이 출력된다.
