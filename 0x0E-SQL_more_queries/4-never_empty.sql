-- SQL Query creates tables with two attributes.
-- Query sets default id value to 1.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256));
