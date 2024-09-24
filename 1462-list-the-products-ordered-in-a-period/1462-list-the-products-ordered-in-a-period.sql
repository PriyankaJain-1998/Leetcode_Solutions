# Write your MySQL query statement below
select p.product_name as product_name, sum(o.unit) AS unit
from Products as p join Orders as o
on p.product_id = o.product_id
where year(o.order_date)='2020' and month(o.order_date)='02'
group by p.product_id
having sum(o.unit)>=100