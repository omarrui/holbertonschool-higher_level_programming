-- creating a table with unique id s
CREATE TABLE IF NOT EXISTS  unique_id(
    id NOT NULL DEFAULT 1 UNIQUE,
    name varchar(256)
)