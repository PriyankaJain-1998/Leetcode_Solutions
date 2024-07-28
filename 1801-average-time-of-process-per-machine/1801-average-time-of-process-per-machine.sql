# Write your MySQL query statement below
select a.machine_id,  round(avg(a1.timestamp - a.timestamp),3) as processing_time
from Activity a
join Activity a1 on a1.machine_id = a.machine_id
where a.activity_type ='start' and a1.activity_type='end'
group by a.machine_id