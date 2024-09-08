# Write your MySQL query statement below
select ed.employee_id, coalesce(max(case when ed.primary_flag = 'Y'
then ed.department_id end),
max(ed.department_id)) as department_id
from employee ed
group by ed.employee_id