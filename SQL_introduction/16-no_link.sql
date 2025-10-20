-- show all records from second table except empty names 
SELECT score, name from second_table where name IS NOT NULL ORDER BY score DESC;