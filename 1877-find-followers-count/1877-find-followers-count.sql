# Write your MySQL query statement below
select distinct user_id, count(follower_id) as followers_count
from Followers
group by user_id
ORDER BY user_id  ASC;