# Write your MySQL query statement below
select stu.student_id, stu.student_name, sub.subject_name, count(e.student_id) as attended_exams
from Students stu 
CROSS JOIN Subjects sub
left join Examinations e on stu.student_id=e.student_id and sub.subject_name=e.subject_name
group by stu.student_id, stu.student_name, sub.subject_name
order by stu.student_id, sub.subject_name;