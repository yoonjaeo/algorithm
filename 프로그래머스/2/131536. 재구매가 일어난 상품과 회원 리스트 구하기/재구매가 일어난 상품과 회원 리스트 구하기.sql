-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
from online_sale
group by user_id, product_id
having count(online_sale_id) >= 2
order by USER_ID asc , PRODUCT_ID desc