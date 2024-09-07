# Write your MySQL query statement below


select s.product_id, s.quantity, s.price, year as first_year
from Sales as s
where (product_id, year) in (
    select product_id, min(year) as year
    from Sales
    group by product_id
)