-- script that lists all the cities of California,
-- that can be found in the database hbtn_0d_usa.


SELECT states.id, cities.name FROM states, cities WHERE states.id = 1 ORDER BY id;
