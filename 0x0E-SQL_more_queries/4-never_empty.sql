-- Query creates new table with id (has default value) and name attributes.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256));
