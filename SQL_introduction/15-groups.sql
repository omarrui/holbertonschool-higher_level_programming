-- lists the number of records with the
-- same score in second_table
SELECT score, count(id) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;