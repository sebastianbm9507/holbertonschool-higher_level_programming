-- Select cities 
-- lists all cities contained in the database hbtn_0d_usa.
select cities.id, cities.name, states.name from cities, states ORDER BY cities.id ASC;
