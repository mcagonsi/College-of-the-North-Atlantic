-- Question 1
use world;
select  * from city ;

-- Question 2
use world;
select distinct  Language 
from countrylanguage;

-- Question 3
select Name, Region 
from country;

-- Question 4
select Name from city
where CountryCode = "CAN"
order by Name
;


-- Question 5
select Name,Population from country
where Population > 100000000
;

-- Quedstion 6
select Name, Continent from country
where Continent = 'Asia' or Continent = 'Africa'
		or Continent = 'Europe'
order by Continent;

-- Quedstion 7
select Language from countrylanguage
where CountryCode = "FRA";

-- Question 8
select Capital from country
where code = 'USA';
select Name from city
where ID = 3813;