-- Query lists records from second_table with common scores sorted by count
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
