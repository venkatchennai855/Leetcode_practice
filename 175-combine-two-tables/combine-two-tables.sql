# Write your MySQL query statement below
SELECT firstName,lastName,city,state
FROM Address Right join Person
ON Person.personId = Address.personId
