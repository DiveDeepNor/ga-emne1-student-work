create user 'city_reader'@'%'
identified by 'ReadOnly_09!';

GRANT SELECT ON world.city
to 'city_reader'@'%';

show grants
for 'city_reader'@'%';

select current_user(), CONNECTION_ID();

select Name, Population
from city;

select *
from country

update city
set Population = 100
WHERE CountryCode = 'NOR'
    and Name = 'Oslo';