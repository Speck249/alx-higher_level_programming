-- Query displays maximum temperature of states
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
