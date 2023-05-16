-- Command lists all names and score
-- in descending order of score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
