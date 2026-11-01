/* User A (root) */

select Name, Population
from city
where CountryCode = 'NOR'
    and Name IN('Oslo', 'Bergen');

Start transaction;

update city
set Population = Population - 100000
where CountryCode = 'NOR'
    and Name = 'Oslo';

update city
set Population = Population + 100000
where CountryCode = 'NOR'
  and Name = 'Bergen';

/* ROLLBACK; */
COMMIT;