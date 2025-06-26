-- creates the table id_not_null on your MySQL server.
CREATE TABELE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);