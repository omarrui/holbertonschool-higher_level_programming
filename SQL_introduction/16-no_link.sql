-- show all records from second table except empty names 
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;