SELECT name,bonus
FROM  Bonus  right join Employee
On Bonus.empId=Employee.empId
where Bonus.bonus is null or Bonus.bonus<1000


