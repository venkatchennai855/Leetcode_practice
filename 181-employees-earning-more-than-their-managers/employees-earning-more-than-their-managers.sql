SELECT e2.name as Employee 
FROM Employee e1Boss inner join Employee e2 
on e1Boss.id = e2.managerId
WHERE e2.salary>e1Boss.salary