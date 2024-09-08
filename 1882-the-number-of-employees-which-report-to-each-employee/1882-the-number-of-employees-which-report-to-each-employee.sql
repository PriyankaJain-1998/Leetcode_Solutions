# Write your MySQL query statement below
-- select mgr.employee_id, 
-- mgr.name, count(emp.employee_id) as reports_count, round(avg(emp.age)) as average_age
-- from Employees emp join employees mgr on emp.reports_to = mgr.employee_id
-- group by employee_id
-- order by employee_id

SELECT
    m.employee_id AS employee_id,
    m.name AS name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM
    employees m
    JOIN employees e ON m.employee_id = e.reports_to
GROUP BY
    m.employee_id, m.name
HAVING
    COUNT(e.employee_id) > 0
ORDER BY
    m.employee_id;