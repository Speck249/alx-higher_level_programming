-- Query displays score and name from second_table excluding records without names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
