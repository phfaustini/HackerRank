select COUNTRY.Continent, FLOOR(AVG(CITY.Population)) from city, country where CITY.COUNTRYCODE = COUNTRY.CODE Group by COUNTRY.Continent;
