-- SQL Query creates table with two attributes.
-- Query prevents null name value.
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL);
