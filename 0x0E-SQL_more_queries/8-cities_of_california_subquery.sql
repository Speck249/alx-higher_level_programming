-- SQL Query displays common value of two tables via SELECT.
-- Query lists values by id(states) and name(cities).
-- Query uses FOREIGN KEY and PRIMARY KEY.
SELECT id, name FROM hbtn_0d_usa.cities WHERE state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name="California" ORDER BY id);
