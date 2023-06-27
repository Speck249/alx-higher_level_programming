-- Command calculates and displays
-- the average of temperatures.
SELECT city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
