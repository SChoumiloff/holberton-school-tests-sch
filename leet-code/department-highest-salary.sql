-- Employee Table
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+
-- Department Table
-- +-------------+---------+
--| Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+

select d.name, e.name, e.salary
from Employee e, Department d
where e.departmentId = d.id
and (e.departmentId, e.salary) in (
    select departmentId, max(salary) from Employee group by departmentId
);