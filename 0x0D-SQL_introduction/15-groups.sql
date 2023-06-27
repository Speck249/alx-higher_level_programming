-- Command displays the number of records
-- with the same number of scores.
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
