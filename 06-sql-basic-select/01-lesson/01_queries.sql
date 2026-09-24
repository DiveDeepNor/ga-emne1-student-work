-- Enkel spørring for å henta alle kolonner og rader i oppgit tabell (city):
SELECT *
from city;

-- Enkel spørring for å henta gitte  kolonner og rader i oppgit tabell (city):
SELECT Name, Population, ID
from city
where Population > 1000000;

SELECT Name, Population
from country
where Continent = 'Europe';

-- Med sortering
SELECT Name, Population
from city
where (CountryCode = 'NOR'
        or CountryCode = 'SWE')
and Population > 200000
order by Name ASC ;

SELECT Name, Population
from city
where Population > 1000000
order by Population DESC ;

-- Med limit
SELECT Name, Population
from city
order by Population DESC
LIMIT 5;


-- Hent navn og folketall for svenske byer med mer enn
-- 100 000 innbyggere

SELECT Name, Population
from city
where CountryCode = 'SWE'
    and Population > 100000
order by Population DESC;

-- Bruker wildcard, altså % tegn. Viser alle som starter på O og slutter på o. Uavhenig av hvor mange bokstaver mellom
SELECT Name
from city
where Name like 'O%o'

-- Bruker wildcard, altså __ tegn. Viser alle som starter på O og slutter på o. Med 2 bokstaver mellom (gitt av antall _)
SELECT Name
from city
where Name like 'O__o'

-- Sjekke at IndepYear er <Null> som da altså sier ingen verdi
SELECT *
from country
where IndepYear is null

-- Teller antall rader som stemmer med spørringen og returnerer som CityCount
SELECT count(*) as CityCount
from city
where CountryCode = 'NOR'