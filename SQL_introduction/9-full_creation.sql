-- creating a full new table 
CREATE table IF NOT EXISTS second_table(
        id INT,
        name VARCHAR(256),
        score INT
);
insert into second_table(id, name, score) 
VALUES 
(1, 'john', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);