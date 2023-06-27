-- SQL Query displays common values from cities table.
-- Query uses INNER JOIN.
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.state_id ORDER BY cities.id;
