-- 코드를 입력하세요
# SELECT Avg(DAILY_FEE) as AVERAGE_FEE
# from CAR_RENTAL_COMPANY_CAR
# where CAR_TYPE = "SUV"
# group by CAR_TYPE;

select round(avg(daily_fee)) as AVERAGE_FEE
from CAR_RENTAL_COMPANY_CAR
group by car_type
having car_type = "SUV";