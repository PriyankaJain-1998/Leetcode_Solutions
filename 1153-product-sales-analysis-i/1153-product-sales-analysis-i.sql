# Write your MySQL query statement below
select p.product_name as product_name, s.year, s.price
from Sales as s left join Product p on p.product_id = s.product_id