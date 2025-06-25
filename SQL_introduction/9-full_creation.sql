-- creating a full database in hbtn
-- and add a few rows
create table if not exists second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT into second_table(is, name, score) 
VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);