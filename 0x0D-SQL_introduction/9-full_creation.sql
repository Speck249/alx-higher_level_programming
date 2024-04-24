-- Query creates 'second_table' inside hbtn_0c_0
-- Query inserts rows to second_table for 'id, name and score'
-- Query creates new records
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT);

INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);
