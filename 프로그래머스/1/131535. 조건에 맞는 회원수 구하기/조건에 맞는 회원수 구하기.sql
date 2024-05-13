-- 코드를 입력하세요
SELECT count(*) as USERS
from USER_INFO
where 2021  = year(JOINED ) and AGE >= 20 and AGE <= 29;