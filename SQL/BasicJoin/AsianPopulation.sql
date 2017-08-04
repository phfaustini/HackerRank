select sum(CITY.population) from country, city where CITY.CountryCode = COUNTRY.Code and COUNTRY.CONTINENT = "Asia";
