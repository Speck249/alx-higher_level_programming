-- SQL Query displays common value of two tables via SELECT.
-- Query lists values by id(states) and name(cities).
-- Query uses FOREIGN KEY and PRIMARY KEY.
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE name="California" ORDER BY id);
